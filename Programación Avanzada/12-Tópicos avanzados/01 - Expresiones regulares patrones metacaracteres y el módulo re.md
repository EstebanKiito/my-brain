---
ramo: "Programación Avanzada"
tema: "Tópicos avanzados"
tags:
  - programacion/regex
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[04 - Strings: inmutabilidad, escapes y métodos]]"
---

# Expresiones regulares patrones metacaracteres y el módulo re

Validar si una cadena de texto es un correo electrónico válido, extraer números de teléfono de un documento o verificar el formato de un RUT chileno usando métodos básicos como `str.split()` o `str.find()` resulta engorroso y frágil. Las **expresiones regulares** (**RegEx**, *Regular Expressions*) proporcionan un lenguaje formal conciso y estandarizado para describir patrones de búsqueda y transformación textual.

## Metacaracteres y clases de caracteres

Una expresión regular combina caracteres literales con metacaracteres especiales:

```
+---------------+-------------------------------------------------------------+
| Elemento      | Significado y rango de coincidencia                         |
+---------------+-------------------------------------------------------------+
| .             | Cualquier carácter individual (excepto salto de línea)      |
| \d / \D       | Dígito numérico [0-9] / Cualquier carácter NO numérico      |
| \w / \W       | Carácter alfanumérico o guion bajo [a-zA-Z0-9_] / No palabra|
| \s / \S       | Espacio en blanco (espacio, tab, salto) / No espacio        |
| [abc]         | Conjunto: coincide con 'a', 'b' o 'c'                       |
| [^0-9]        | Negación: cualquier carácter que NO sea un dígito           |
+---------------+-------------------------------------------------------------+
```

## Cuantificadores y anclas de posición

- **`*`:** cero o más repeticiones (avaro).
- **`+`:** una o más repeticiones.
- **`?`:** cero o una repetición (opcional).
- **`{n,m}`:** entre $n$ y $m$ repeticiones (ejemplo `\d{3,4}`).
- **`^`:** ancla que exige coincidir con el **inicio** estricto de la cadena.
- **`$`:** ancla que exige coincidir con el **final** de la cadena.
- **`( ... )`:** grupo de captura para aislar subpatrones y extraer datos.
- **`|`:** operador lógico de alternancia (OR).

![Anatomía de correo electrónico](adjuntos/Anatom%C3%ADa%20de%20una%20direcci%C3%B3n%20de%20correo%20y%20patr%C3%B3n%20regex.png)

> [!example]- Transcripción de la imagen
> - Desglose de una dirección de correo:
>   - Parte local (*username*), símbolo arroba `@`, nombre del dominio y dominio de nivel superior (*TLD* como `.com` o `.cl`).

## El módulo re en Python

El módulo estándar **`re`** provee las funciones fundamentales para operar con expresiones regulares:

- **`re.search(patron, texto)`:** busca la primera aparición del patrón en cualquier parte de la cadena; retorna un objeto `Match` o `None`.
- **`re.match(patron, texto)`:** busca coincidencias únicamente desde el primer carácter de la cadena.
- **`re.findall(patron, texto)`:** retorna una lista con todas las ocurrencias encontradas.
- **`re.sub(patron, reemplazo, texto)`:** sustituye las coincidencias por el string de reemplazo.

```python
import re

# Validación y extracción de RUT chileno con grupos de captura
# Formato esperado: XX.XXX.XXX-X o XXXXXXXX-X
patron_rut = r"^(\d{1,2})\.?(\d{3})\.?(\d{3})-([0-9kK])$"

texto = "El alumno tiene RUT 19.876.543-k para su matrícula."

# re.search busca el patrón dentro del texto largo
coincidencia = re.search(patron_rut.strip("^$"), texto)

if coincidencia:
    rut_completo = coincidencia.group(0)
    millones = coincidencia.group(1)
    digito_verificador = coincidencia.group(4)
    print(f"RUT detectado: {rut_completo}")
    print(f"Tramo millones: {millones}, Dígito Verificador: {digito_verificador}")
```

```
RUT detectado: 19.876.543-k
Tramo millones: 19, Dígito Verificador: k
```

> [!warning] Usa siempre Raw Strings con prefijo r
> En Python, la barra invertida `\` es el carácter de escape para strings normales (`\n`, `\t`). Al escribir expresiones regulares, antepón siempre la letra `r` (ejemplo `r"\d+\.\d+"`) para que Python no interprete las barras antes de que lleguen al motor de expresiones regulares.

> [!tip] Compilación de patrones con re.compile()
> Si vas a ejecutar la misma expresión regular miles de veces dentro de un bucle, compílala previamente con `patron = re.compile(r"...")` para evitar que Python vuelva a parsear el patrón en cada iteración.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre los métodos `re.match()` y `re.search()` en Python?
> `re.match()` solo verifica si la coincidencia comienza exactamente en el primer carácter del string, mientras que `re.search()` escanea toda la cadena hasta encontrar la primera ocurrencia en cualquier posición.

> [!question]- ¿Qué representan los símbolos `^` y `$` en una expresión regular?
> Son anclas de posición: `^` indica que el patrón debe comenzar al inicio exacto de la cadena o línea, y `$` indica que debe terminar en el final absoluto.

> [!question]- ¿Por qué es fundamental utilizar cadenas crudas (*raw strings* `r"..."`) al escribir patrones de regex?
> Para evitar que el analizador léxico de Python interprete las barras invertidas como escapes propios del lenguaje (`\n`, `\b`) antes de que el motor de `re` reciba los metacaracteres.

> [!question]- ¿Cómo se accede al texto capturado por el segundo paréntesis `(...)` en un objeto `Match`?
> Invocando el método `coincidencia.group(2)` (donde `group(0)` corresponde a la coincidencia total completa).
