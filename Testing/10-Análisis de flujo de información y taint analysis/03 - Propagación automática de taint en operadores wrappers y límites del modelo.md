---
ramo: "Testing"
tema: "Análisis de flujo de información y taint analysis"
tags:
  - testing/analisis-de-flujo-de-informacion-y-taint-analysis
  - origen/complemento
prerrequisitos:
  - "[[Testing/10-Análisis de flujo de información y taint analysis/02 - Implementación de strings contaminados con la clase tstr en Python|Implementación de strings contaminados con la clase tstr en Python]]"
---

# Propagación automática de taint en operadores, wrappers y límites del modelo

## El problema: los métodos nativos de `str` pierden el `taint`

Supongamos que tenemos nuestra clase `tstr` básica y ejecutamos `thello = tstr("hello", taint="LOW")`. ¿Qué pasa si hacemos `nuevo = thello + " world"` o `mayus = thello.upper()` sin sobrescribir esos métodos?
* Como `tstr` hereda de `str`, Python ejecuta el método original `str.__add__` o `str.upper` escrito en C.
* Ese método devuelve un objeto **`str` común y corriente**, no un `tstr`. ¡En la primera concatenación o `.strip()`, el objeto deja de ser `tstr` y **toda la información de `taint` se borra silenciosamente**!

Para que el `taint` sobreviva a cualquier manipulación de cadenas, debemos envolver todos los operadores y métodos de `str` para que devuelvan instancias de `tstr`.

---

## Envolver 25 métodos de golpe con `make_str_wrapper` e introspección

En lugar de escribir a mano 25 métodos casi idénticos (`upper`, `lower`, `strip`, `replace`, `__getitem__`, `__add__`, `__mul__`, `__mod__`, etc.), usamos funciones de orden superior y metaprogramación (`getattr` y `setattr`):

```python
class tstr(tstr):
    @staticmethod
    def make_str_wrapper(fun):
        """Recibe un método 'fun' de la clase str y devuelve un método proxy para tstr."""
        def proxy(self, *args, **kwargs):
            res = fun(self, *args, **kwargs)
            return self.create(res)  # envuelve el resultado heredando self.taint

        if hasattr(fun, "__doc__"):
            proxy.__doc__ = fun.__doc__
        return proxy

def informationflow_init_1():
    for name in ["__format__", "__mod__", "__rmod__", "__getitem__",
                 "__add__", "__mul__", "__rmul__",
                 "capitalize", "casefold", "center", "encode",
                 "expandtabs", "format", "format_map", "join",
                 "ljust", "lower", "lstrip", "replace",
                 "rjust", "rstrip", "strip", "swapcase", "title", "translate", "upper"]:
        fun = getattr(str, name)
        setattr(tstr, name, tstr.make_str_wrapper(fun))
```

¿Cómo funciona este truco?
1. `getattr(str, 'upper')` obtiene la función original `str.upper`.
2. `tstr.make_str_wrapper(fun)` fabrica una función `proxy(self, *args, **kwargs)` que primero llama a `str.upper(self, ...)` obteniendo `'HELLO'` y enseguida retorna `self.create('HELLO')` (que es `tstr('HELLO', taint=self.taint)`).
3. `setattr(tstr, 'upper', proxy)` instala ese `proxy` dentro de la clase `tstr`.

---

## El caso crítico de la suma por la derecha: ¿por qué hace falta `__radd__`?

Incluso después de correr `informationflow_init_1()` (que envuelve `__add__`), mira qué ocurre en una consulta SQL real:

```python
s1 = tstr("juampi", taint="INSECURE")
# Caso A: tstr a la izquierda -> llama a s1.__add__(" mundo") ✅
a = s1 + " mundo"

# Caso B: str normal a la izquierda y tstr a la derecha:
b = "SELECT * FROM users WHERE name = '" + s1
```

En el **Caso B**, el operando de la izquierda (`"SELECT ... '"`), ¡es un `str` normal, no un `tstr`! En Python, para que `izq + der` conserve el `taint` cuando el `tstr` está a la **derecha**, debemos implementar el método reflejado **`__radd__(self, other)`** (y en `__add__` combinar `self.taint or getattr(other, 'taint', None)`):

```python
class tstr(tstr):
    def __add__(self, other):
        t = self.taint or getattr(other, "taint", None)
        return tstr(str.__add__(self, other), taint=t)

    def __radd__(self, value):
        """Se invoca cuando hacemos: 'texto normal' + self (tstr a la derecha)."""
        t = getattr(value, "taint", None) or self.taint
        return tstr(str(value) + str(self), taint=t)
```

*(Nota técnica de Python: como `tstr` es subclase de `str`, el operador `+` en C de `str` acepta subclases directamente a menos que el operando izquierdo devuelva `NotImplemented` o se envuelvan los literales; por eso en `tstr` definimos tanto `__add__` como `__radd__`).*

---

## Límites del modelo: escape por conversión y flujo de datos implícito

¿Cómo puede un dato contaminado «escapar» (lavar su mancha) sin pasar por un *sanitizer* en nuestro modelo basado en `tstr`? Existen dos vías clásicas de escape que se preguntan en pruebas:

1. **Escape por conversión de tipos no instrumentados:**
   Si el programa convierte el `tstr` a otro tipo primitivo que no guarda `.taint` y luego lo reconstruye a `str`, la etiqueta se pierde:
   ```python
   secreto = tstr("42", taint="HIGH")
   numero = int(secreto)       # int común de Python: ¡no tiene .taint!
   lavado = str(numero)        # str común ("42"): perdió el taint='HIGH'
   ```
   Lo mismo ocurre al convertir carácter por carácter usando `chr(ord(c))`.
2. **Escape por flujo de información implícito (*implicit control flow*):**
   Ocurre cuando el valor de un `tstr` no se copia directamente con operaciones de string, sino que **decide qué rama de un `if` o `switch` se ejecuta**, y dentro de esa rama se asignan literales limpios:
   ```python
   copia = ""
   for c in tstr("abc", taint="HIGH"):
       if c == "a":
           copia += "a"   # 'a' es un literal limpio; el taint gobernó el if, no el +=
   ```
   En ambos casos, el contenido de `secreto` se transfirió a la salida, pero ningún operador de `tstr` participó en la creación del literal final.

---

---

## Ejemplo práctico: propagación, mezclas y fugas

Con la clase completa (wrappers + `__add__`/`__radd__`), comprobamos qué sobrevive y qué no.

**Cadena de operaciones: la mancha sobrevive a todas.**

```python
t = tstr("  Hola Mundo  ", taint="LOW")
r = t.strip().upper()[0:4].replace("O", "0")
print(r, type(r).__name__, r.taint)       # H0LA tstr LOW
```

**Formateo con `%`: sobrevive** (gracias a `__mod__`):

```python
"%s!" % tstr("x", taint="HIGH")           # tstr con taint == "HIGH"
```

**Mezcla de dos manchas distintas:** gana la del operando izquierdo si tiene una; si no, se usa la derecha (según nuestra implementación de `__add__`):

```python
print((tstr("a", taint="HIGH") + tstr("b", taint="LOW")).taint)     # HIGH
print((tstr("a", taint=None)   + tstr("b", taint="LOW")).taint)     # LOW
```

**Fugas que nuestro modelo no ve:**

```python
# 1. f-strings: se evalúan sin pasar por nuestros métodos
x = tstr("x", taint="HIGH")
print(type(f"{x}!").__name__)             # str  ← mancha perdida

# 2. Conversión de tipo
n = int(tstr("42", taint="HIGH"))
lavado = str(n)
print(type(lavado).__name__, hasattr(lavado, "taint"))   # str False

# 3. Flujo implícito: el secreto decide una rama, pero se copian literales
copia = ""
for c in tstr("abc", taint="HIGH"):
    if c == "a":
        copia += "a"                       # 'a' es un literal limpio
print(type(copia).__name__, copia)         # str a
```

En los tres casos la información del dato original llegó a la salida, pero `copia`, `lavado` y el f-string son `str` sin etiqueta. Por eso el taint analysis dinámico basado en wrappers es una **aproximación**: detecta los flujos explícitos que pasan por operaciones envueltas y no garantiza detectar todos.

### Qué haría falta para cerrar cada fuga

| Fuga | Posible mejora | Costo |
| :--- | :--- | :--- |
| f-strings | Instrumentar el AST para reescribirlos como `.format` | Una transformación (Tema 09) |
| Conversión de tipo (`int`, `float`) | Clases `tint`, `tfloat` análogas a `tstr` | Más clases y wrappers |
| Flujo implícito | Seguir el taint también de las **condiciones** de `if` y `while` | Mucho más complejo, aumenta los falsos positivos |

---

## Preguntas de repaso

> [!question]- ¿Por qué es necesario definir el método `__radd__(self, value)` en `tstr` si ya habíamos definido `__add__(self, other)`?
> Porque `__add__` solo se invoca cuando la instancia de `tstr` aparece a la **izquierda** del signo `+` (`tstr + str`). Cuando el programador escribe un prefijo constante a la izquierda y concatena la variable contaminada a la derecha (como `"sh -c " + entrada_tstr`), se requiere `__radd__` para interceptar la suma desde el operando derecho y devolver un `tstr` contaminado.

> [!question]- ¿Cómo funciona el patrón `make_str_wrapper(fun)` junto con `getattr` y `setattr` para no tener que reescribir manualmente 25 métodos de la clase `str`?
> Se itera sobre la lista de nombres de métodos de `str` que devuelven cadenas; para cada nombre, `getattr(str, name)` recupera la función nativa de `str`, `make_str_wrapper` la envuelve en una clausura `proxy` que aplica `self.create(res)` al resultado para preservar `self.taint`, y `setattr(tstr, name, proxy)` adjunta dinámicamente ese método a la clase `tstr`.

> [!question]- Explica qué es un «flujo de información implícito» (*implicit flow*) con un ejemplo breve en Python y por qué logra burlar el seguimiento dinámico de `tstr`.
> Un flujo implícito ocurre cuando el valor de una variable contaminada determina el camino de control (`if`/`elif`) en lugar de fluir directamente como operando de una expresión, por ejemplo: `if pin_tainted == "1234": salida = "1234"`. Como a `salida` se le asigna un literal constante nuevo dentro del bloque `if` sin invocar métodos de `pin_tainted`, `salida` nace sin marca de `taint` aunque revela el valor del dato contaminado.

> [!question]- ¿Por qué hay que implementar `__radd__` si `__add__` ya está envuelto?
> Porque en `"texto" + tstr_obj` Python intenta primero `str.__add__("texto", tstr_obj)`, que devuelve un `str` normal. Al implementar `__radd__` en `tstr` (y ser subclase de `str`), Python le da prioridad al método del operando derecho, de modo que el resultado es un `tstr` con la mancha preservada. Sin él, la concatenación típica de una consulta SQL perdería el taint.

> [!question]- Un atacante controla `s` (un `tstr` con taint). El programa hace `t = "".join(str(c) for c in s)` y luego usa `t` en un sink. ¿Lo detecta el modelo? ¿Por qué?
> No: `str(c)` llama a `__str__`, que devuelve un `str` nativo sin etiqueta, así que `"".join(...)` junta strings limpios. Es una fuga por conversión. El dato real del atacante llega al sink con taint `None`, produciendo un falso negativo.
