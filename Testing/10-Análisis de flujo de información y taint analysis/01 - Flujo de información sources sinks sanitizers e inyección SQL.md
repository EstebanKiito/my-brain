---
ramo: "Testing"
tema: "Análisis de flujo de información y taint analysis"
tags:
  - testing/analisis-de-flujo-de-informacion-y-taint-analysis
  - origen/complemento
prerrequisitos:
  - "[[Testing/01-Fundamentos del testing de software/01 - Qué es el testing error defecto falla y el oráculo de prueba|Qué es el testing error defecto falla y el oráculo de prueba]]"
---

# Flujo de información: sources, sinks, sanitizers e inyección SQL

## Seguir la mancha de tinta: ¿por dónde viajan los datos de un usuario?

Imagina que en una planta de agua potable sospechas que una tubería exterior está filtrando agua sucia hacia la red de consumo. ¿Cómo averiguas hasta qué grifos llega esa filtración? Echas un **colorante fluorescente inofensivo (una mancha o *taint*)** en la entrada sospechosa y observas por qué tuberías viaja ese color y si llega a algún grifo antes de pasar por una planta purificadora.

En seguridad de software y depuración, **Taint Analysis** (análisis de contaminación o de flujo de información dinámico) hace exactamente lo mismo: **marca con una etiqueta de metadatos (*taint*) todos los datos que entran desde fuentes no confiables y rastrea cómo esa etiqueta se propaga en tiempo de ejecución cada vez que los datos se concatenan, cortan o transforman**, verificando que jamás lleguen crudos a una operación peligrosa.

---

## Las cuatro piezas del vocabulario de *Taint Analysis*

```
[ Source ] ──(dato tainted)──► [ Propagación ] ──┬──(sin limpiar)──► [ Sink ] 💥 ¡BLOQUEADO / ALERTA!
input HTTP,                    concatenación +,  │
archivo, socket                slice, replace    └──► [ Sanitizer ] ──(taint=None)──► [ Sink ] ✅ OK
```

1. **Source (fuente):** el punto de entrada por donde ingresa un dato externo o no confiable al programa (un formulario web, un parámetro de URL, un *socket*, la lectura de un archivo). Allí el dato nace marcado, por ejemplo con `taint='INSECURE'` o `taint='HIGH'`.
2. **Propagación:** la regla de oro del análisis de flujo:
   > *«Si un nuevo valor se calcula a partir de un dato contaminado (`tainted`), el resultado derivado también debe considerarse contaminado, a menos que exista una razón explícita para limpiarlo».*
3. **Sink (sumidero):** el lugar sensible del sistema donde usar un dato controlado por un atacante causaría un desastre: ejecutar una consulta en una base de datos (`db.execute(sql)`), correr un comando de sistema (`os.system(cmd)`), evaluar código (`eval(s)`) o renderizar HTML crudo en el navegador.
4. **Sanitizer (sanitizador o purificador):** una función de validación o escape (por ejemplo, escapar comillas SQL, validar que el string contenga solo dígitos o llamar a `clear_taint()`) que neutraliza el peligro y **remueve explícitamente la marca de contaminación** (`taint = None`) antes de que el dato llegue al *sink*.

---

## Caso clásico: Inyección SQL y ejecución de comandos de *shell*

Veamos por qué concatenar strings de usuario dentro de consultas SQL o comandos de consola es tan peligroso y cómo lo atrapa *Taint Analysis*:

```python
# Caso normal pensado por el programador:
user_name = "Mario"
sql_query = "SELECT * FROM Customers WHERE name ='" + user_name + "'"
# -> SELECT * FROM Customers WHERE name ='Mario'

# Ataque de Inyección SQL (SQLi):
user_name = tstr("'; DROP TABLE Customers --", taint="INSECURE")
sql_query = "SELECT * FROM Customers WHERE name ='" + user_name + "'"
# -> SELECT * FROM Customers WHERE name =''; DROP TABLE Customers --'
```

Para un motor SQL común, la cadena final `sql_query` es un `str` indistinguible de una consulta escrita por el propio programador: cierra la comilla `'`, ejecuta `DROP TABLE Customers` (borrando la tabla entera) y comenta el resto con `--`.

En cambio, cuando `user_name` es un string con seguimiento de flujo (`tstr` con `taint='INSECURE'`), la concatenación `"SELECT ... '" + user_name + "'"` **propaga automáticamente la etiqueta `'INSECURE'` a toda la variable `sql_query`**. Cuando `sql_query` llega al *sink* (el motor de base de datos o `sink_ejecutar_comando`), basta una verificación de una línea para detener el ataque:

```python
def sink_ejecutar_sql(query):
    if getattr(query, "taint", None) in ("INSECURE", "HIGH"):
        raise SecurityError(f"BLOQUEADO: dato contaminado llega al sink -> {query!r}")
    return ejecutar_en_bd(query)
```

### El balance entre falsos positivos y falsos negativos al sanitizar

* **¿Qué pasa si el análisis NO reconoce un *sanitizer* legítimo?** (Por ejemplo, el programador escapó correctamente todas las comillas SQL con una función propia, pero esa función no limpió `taint = None`). El dato llega seguro al *sink*, pero aún conserva la marca `taint='HIGH'`, disparando una falsa alarma (**falso positivo**).
* **¿Qué pasa si el análisis limpia el *taint* en una función que NO sanitizaba bien?** (Por ejemplo, alguien llama a `clear_taint()` después de hacer solo `.strip()`). El ataque sigue vivo dentro del string pero ahora tiene `taint=None`, pasando al *sink* sin ser detectado (**falso negativo**).

---

---

## Ejemplo práctico: el recorrido completo source → sanitizer → sink

Usando `tstr` (que implementamos en la siguiente nota), seguimos tres versiones de la misma consulta:

```python
class SecurityError(Exception):
    pass

def sink_sql(query):
    if getattr(query, "taint", None) in ("INSECURE", "HIGH"):
        raise SecurityError(f"BLOQUEADO: {query!r}")
    return "ejecutado"

def escapar(s):
    """Sanitizer: duplica las comillas simples y declara el dato como limpio."""
    return s.replace("'", "''").clear_taint()
```

**1. Dato contaminado sin sanitizar → el sink lo bloquea.**

```python
nombre = tstr("Mario", taint="INSECURE")                      # source: viene del usuario
consulta = "SELECT * FROM Customers WHERE name ='" + nombre + "'"
print(type(consulta).__name__, consulta.taint)                # tstr INSECURE (la mancha se propagó)
sink_sql(consulta)                                            # SecurityError: BLOQUEADO
```

Notar que `"Mario"` es un nombre perfectamente inocente: el análisis **no mira el contenido**, solo el origen. Bloquea todo dato no confiable que llegue sin pasar por un sanitizer.

**2. Ataque pasando por el sanitizer → el sink acepta.**

```python
ataque = tstr("'; DROP TABLE Customers --", taint="INSECURE")
limpio = escapar(ataque)
print(limpio, limpio.taint)                                   # ''; DROP TABLE Customers --   None
sink_sql("SELECT ... '" + limpio + "'")                       # "ejecutado"
```

Con la comilla duplicada, el motor SQL interpreta el contenido como texto, no como una consulta nueva. El sanitizer hizo dos cosas: **arregló el dato** (escapar) y **declaró que ya es seguro** (`clear_taint`).

**3. El error silencioso: sanitizer incorrecto.**

```python
def mal_sanitizer(s):
    return s.clear_taint()        # limpia la marca sin escapar nada
```

El sink aceptaría el ataque original porque la etiqueta dice «limpio». El análisis confía en que los sanitizers hacen bien su trabajo: si alguien llama a `clear_taint()` sin sanear, se produce un **falso negativo** peligroso (el ataque pasa).

### Resumen de decisiones

| Situación | Resultado | Tipo de error si es incorrecto |
| :--- | :--- | :--- |
| Dato sin sanear llega al sink | Se bloquea | — |
| Dato correctamente sanitizado | Se acepta | — |
| Dato seguro pero el análisis no reconoce el sanitizer | Se bloquea | **Falso positivo** (molesta al desarrollador) |
| Dato inseguro limpiado por un sanitizer defectuoso | Se acepta | **Falso negativo** (deja pasar el ataque) |

---

## Preguntas de repaso

> [!question]- Define qué son un *Source*, un *Sink* y un *Sanitizer* en *Taint Analysis* e identifica cuál es cuál en un servidor web que recibe un nombre de archivo por URL, verifica que sea alfanumérico y lo abre con `open(ruta)`.
> * **Source:** la lectura del parámetro desde la URL de la petición HTTP (donde el string nace con `taint='HIGH'`).
> * **Sanitizer:** la función que verifica que el nombre sea estrictamente alfanumérico (sin `../`) y limpia su etiqueta (`clear_taint()`).
> * **Sink:** la llamada sensible al sistema de archivos `open(ruta)`.

> [!question]- ¿Qué es la regla de propagación del *taint* y por qué debe aplicarse incluso a operaciones aparentemente inocentes como extraer una subcadena (`s[1:4]`) o pasar a mayúsculas (`s.upper()`)?
> La regla establece que todo dato derivado de una entrada contaminada hereda su contaminación. Debe aplicarse a `s[1:4]` o `s.upper()` porque un atacante puede inyectar un *payload* sabiendo que el programa descartará el primer carácter o lo pasará a mayúsculas (como `DROP TABLE` en SQL, que es insensible a mayúsculas); si esas operaciones borraran el *taint*, el atacante evadiría el control fácilmente.

> [!question]- Además de detectar vulnerabilidades de seguridad (como SQLi o Command Injection), ¿qué utilidad tiene *Taint Analysis* dentro del *fuzzing* y la inferencia de gramáticas?
> Permite saber **qué bytes o caracteres específicos de la entrada llegaron hasta qué comparación del parser**. Así, un *fuzzer* no muta la cadena a ciegas, sino que muta específicamente los caracteres cuya marca de *taint* alcanzó el condicional de la rama que se desea destrabar.

> [!question]- ¿Por qué el taint analysis bloquea `"Mario"` aunque sea un nombre inocente?
> Porque el análisis rastrea el **origen** del dato, no su contenido. Todo lo que viene de una fuente no confiable se considera contaminado hasta que pase por un sanitizer; juzgar el contenido caso a caso sería tan difícil como detectar ataques con filtros, y es justamente lo que el taint analysis busca evitar.

> [!question]- Identifica source, propagación, sanitizer y sink en: `n = request.args["id"]; q = "DELETE FROM t WHERE id=" + n; db.execute(q)`.
> Source: `request.args["id"]` (dato del usuario). Propagación: la concatenación `"DELETE ..." + n` produce un `q` contaminado. Sanitizer: no hay ninguno (convendría `int(n)` o una consulta parametrizada). Sink: `db.execute(q)`, que recibe una consulta contaminada.
