---
ramo: "Testing"
tema: "Cobertura de código e instrumentación con settrace"
tags:
  - testing/cobertura-de-codigo-e-instrumentacion-con-settrace
  - origen/complemento
prerrequisitos:
  - "[[01 - Pruebas de caja blanca y métricas de cobertura estructural]]"
---

# Rastreo de ejecución en Python con sys settrace y frames de pila

## ¿Cómo sabe una herramienta qué líneas se ejecutaron?

Cuando corremos `coverage run` en la terminal, pareciera magia que Python sepa exactamente qué líneas de nuestro archivo fueron tocadas y cuáles no. Detrás de esa magia está la **instrumentación dinámica de la ejecución**: observar al intérprete paso a paso mientras el programa corre.

En Python no necesitamos modificar el código fuente a mano para lograrlo, porque el módulo estándar `sys` ofrece el gancho (*hook*) **`sys.settrace(trace_func)`**. Al registrar una función `trace_func`, el intérprete de Python la invoca automáticamente **justo antes de cada evento relevante de ejecución**.

---

## Anatomía de la función de rastreo: `frame`, `event` y `arg`

Toda función que pasemos a `sys.settrace` debe recibir exactamente tres parámetros: `trace_func(frame, event, arg)`:

![Ejemplo básico de función de rastreo trace_func activada y desactivada con sys.settrace](adjuntos/Ejemplo%20básico%20de%20trace_func%20con%20sys%20settrace.png)

1. **`frame` (objeto `FrameType`):** representa el **marco de ejecución actual en la pila de llamadas** (*call stack*). A través de sus atributos podemos inspeccionar todo el contexto en tiempo real:
   * `frame.f_lineno`: el **número de línea** actual del archivo fuente que está a punto de ejecutarse.
   * `frame.f_code.co_name`: el **nombre de la función** en la que se encuentra la ejecución (por ejemplo, `'cgi_decode'`).
   * `frame.f_code.co_filename`: el nombre del archivo `.py`.
   * `frame.f_locals`: un diccionario con los nombres y valores actuales de todas las **variables locales** de esa función en ese preciso instante.
2. **`event` (`str`):** una cadena que indica qué acaba de ocurrir en el intérprete:
   * `'call'`: se acaba de entrar a una función (antes de ejecutar su primera línea).
   * `'line'`: el intérprete está a punto de ejecutar una nueva línea de código fuente.
   * `'return'`: una función está a punto de retornar.
   * `'exception'`: se acaba de lanzar una excepción.
3. **`arg`:** información adicional cuyo valor depende de `event`: en `'call'` y `'line'` vale `None`; en `'return'` contiene el **valor exacto que está retornando la función**; y en `'exception'` es una tupla `(exc_type, exc_value, traceback)`.

> [!caution] Dos detalles que jamás debes olvidar al usar `sys.settrace`
> 1. **`return trace_func` al final del callback:** cuando ocurre un evento `'call'` (al entrar a una función), Python usa el valor retornado por `trace_func` como el rastreador local para las líneas internas de esa función. Si olvidas escribir `return trace_func` (y la función devuelve `None` por defecto), Python **dejará de rastrear las líneas dentro de la función llamada**.
> 2. **Desactivar con `sys.settrace(None)`:** al terminar de ejecutar la función bajo prueba, siempre debes apagar el rastreador llamando `sys.settrace(None)`. Si no lo apagas, `trace_func` seguirá disparándose para cada `print()` o instrucción posterior de tu propio script o de Jupyter.

---

## Capturando y visualizando las líneas ejecutadas de `cgi_decode`

Para medir qué líneas ejecuta `cgi_decode("a+b")`, creamos una función `traceit` que escucha el evento `'line'` y guarda `frame.f_lineno` en una lista `coverage`:

![Definición de traceit guardando números de línea y activación sobre cgi_decode](adjuntos/Registro%20de%20líneas%20ejecutadas%20en%20traceit.png)

Al envolver la llamada en `cgi_decode_traced("a+b")`:

![Envoltorio cgi_decode_traced encendiendo y apagando sys.settrace](adjuntos/Activación%20y%20desactivación%20de%20settrace%20en%20cgi_decode.png)

La lista `coverage` registra cada número de línea en el orden cronológico exacto en que se ejecutó (por ejemplo, las líneas dentro del ciclo `while` aparecen repetidas tres veces, una por cada carácter de `"a+b"`).

### Cruzando las líneas ejecutadas con el código fuente (`inspect.getsource`)

Para mostrar visualmente qué líneas quedaron sin probar, recuperamos el texto fuente de la función usando el módulo estándar `inspect`:

![Obtención del código fuente numerado mediante inspect.getsource](adjuntos/Inspección%20del%20código%20fuente%20con%20inspect%20getsource.png)

Luego convertimos la lista `coverage` en un conjunto **`covered_lines = set(coverage)`** (eliminando duplicados y permitiendo búsquedas en $O(1)$) e imprimimos cada línea del archivo anteponiendo un símbolo (`#` o `!`) cuando `lineno not in covered_lines`:

![Visualización línea por línea marcando con numeral las líneas no cubiertas](adjuntos/Visualización%20de%20líneas%20no%20cubiertas%20con%20numeral.png)

Así vemos de un vistazo que la entrada `"a+b"` cubrió el ciclo y la rama del `'+'`, pero dejó marcadas con `#` todas las líneas del bloque `elif c == '%':`.

---

---

## Ejemplo práctico: ver los eventos de `sys.settrace` uno por uno

Con una función minúscula se ve claramente qué recibe el *callback* en cada evento:

```python
import sys

def signo(x):
    if x > 0:
        return "positivo"
    return "no positivo"

def trace_func(frame, event, arg):
    print(f"{event:9} línea {frame.f_lineno:2} en {frame.f_code.co_name} locals={frame.f_locals} arg={arg!r}")
    return trace_func            # importante: sigue rastreando dentro de la función

sys.settrace(trace_func)
signo(5)
sys.settrace(None)
```

Salida (los números de línea dependen de dónde esté escrita la función en tu archivo):

```
call      línea  2 en signo locals={'x': 5} arg=None
line      línea  3 en signo locals={'x': 5} arg=None
line      línea  4 en signo locals={'x': 5} arg=None
return    línea  4 en signo locals={'x': 5} arg='positivo'
```

Cómo leerla:

* `call` ocurre al entrar a `signo`, antes de ejecutar su primera línea.
* Hay solo **dos** eventos `line` (el `if` y el `return "positivo"`): el `return "no positivo"` **nunca** aparece porque con `x = 5` esa línea no se ejecutó. Es exactamente la información que usa un reporte de cobertura.
* En `return`, `arg` contiene el valor devuelto (`'positivo'`).

### ¿Y si olvidamos `return trace_func`?

Si el callback no devuelve nada, Python deja de rastrear líneas dentro de la función: solo verías el evento `call` y ningún `line`. Es el error más común al escribir un tracer.

### Filtrar para no registrar ruido

```python
lineas = []

def traceit(frame, event, arg):
    if event == "line" and frame.f_code.co_name == "signo":
        lineas.append(frame.f_lineno)
    return traceit

sys.settrace(traceit)
signo(-3)
sys.settrace(None)
print(lineas)      # ahora aparece la línea del segundo return, no la del primero
```

Con `signo(5)` obtendrías las líneas del `if` y del primer `return`; con `signo(-3)`, las del `if` y del segundo `return`. Dos entradas distintas dejan huellas distintas.

---

## Preguntas de repaso

> [!question]- ¿Qué ocurre si en una función `trace_func(frame, event, arg)` pasada a `sys.settrace` olvidamos escribir la línea `return trace_func` al final?
> Al entrar a cualquier función (evento `'call'`), Python espera que `trace_func` retorne la función de rastreo local que debe observar el interior de ese nuevo *frame*. Si no retorna nada (devuelve `None`), el rastreo se desactiva dentro de la función llamada y no se registrará ningún evento `'line'` ni `'return'` de su cuerpo.

> [!question]- Dentro de `trace_func(frame, event, arg)`, ¿cómo puedes obtener (1) el nombre de la función actual, (2) el número de línea que se está ejecutando y (3) el valor de una variable local llamada `total`?
> 1. Nombre de la función: `frame.f_code.co_name`.
> 2. Número de línea actual: `frame.f_lineno`.
> 3. Valor de la variable local `total`: `frame.f_locals.get("total")` (o `frame.f_locals["total"]`).

> [!question]- ¿Por qué la lista cruda `coverage` recolectada por `traceit` al correr `cgi_decode("a+b")` contiene números de línea repetidos, y por qué la convertimos en un `set`?
> Contiene números repetidos porque `traceit` hace `coverage.append(lineno)` cada vez que el intérprete pasa por una línea, y las líneas de inicialización del diccionario o del ciclo `while i < len(s):` se ejecutan múltiples veces en una misma llamada. La convertimos en un `set` porque para calcular cobertura solo nos importa saber si cada línea fue ejecutada **al menos una vez** (además de habilitar operaciones de conjuntos como unión, intersección y resta).

> [!question]- Ejecutas `sys.settrace(traceit)` y luego una función con un `for` de $4$ iteraciones. El cuerpo del `for` es una línea. ¿Cuántas veces aparece esa línea en la lista de líneas ejecutadas?
> $4$ veces (una por iteración). Por eso al calcular cobertura se convierte la lista a `set`: nos interesa qué líneas se ejecutaron, no cuántas veces.

> [!question]- ¿Qué pasaría si después de la prueba no llamamos a `sys.settrace(None)`?
> El *callback* seguiría disparándose para todo el código que se ejecute después (incluso `print` y otras funciones), ralentizando el programa y llenando la lista de líneas con eventos que no pertenecen a la prueba. Por eso la clase `Coverage` lo encapsula en `__exit__`, que se ejecuta incluso si la función lanza una excepción.
