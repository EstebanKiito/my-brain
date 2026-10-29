---
ramo: "Testing"
tema: "Cobertura de código e instrumentación con settrace"
tags:
  - testing/cobertura-de-codigo-e-instrumentacion-con-settrace
  - origen/complemento
prerrequisitos:
  - "[[Testing/02-Pruebas unitarias dobles de prueba y test smells/01 - Estado e invariante de objetos y estructura Arrange Act Assert|Estado e invariante de objetos y estructura Arrange Act Assert]]"
  - "[[Ingeniería de Software/06-Testing/09 - Cobertura de código con SimpleCov|Cobertura de código con SimpleCov]]"
---

# Pruebas de caja blanca y métricas de cobertura estructural

## ¿Cuándo tenemos suficientes pruebas?

Imagina que escribiste cinco pruebas unitarias para una función compleja y las cinco pasan en verde. ¿Cómo sabes si esas cinco pruebas realmente exploraron todos los casos del algoritmo o si las cinco recorrieron exactamente el mismo camino feliz dejando la mitad del código sin ejecutar jamás?

Para responder esta pregunta de manera objetiva abrimos la «caja» del programa y observamos su estructura interna (sus líneas, condicionales `if`, ciclos `while` y funciones). A este enfoque se le denomina **testing de caja blanca** (*white-box testing*) o **testing estructural**, en contraste con el testing de caja negra (que diseña pruebas mirando únicamente los requerimientos externos sin leer el código).

### Ventaja y limitación fundamental de la caja blanca

* **Ventaja:** permite descubrir errores en el comportamiento realmente implementado y encontrar ramas, excepciones o casos borde técnicos que la especificación de alto nivel ni siquiera mencionaba.
* **Limitación crítica (*no ve lo que falta*):** la caja blanca solo puede medir el código que **existe escrito en el archivo**. Si un requerimiento pedía aplicar un descuento especial a jubilados pero al programador se le olvidó escribir ese `if`, no hay líneas que cubrir: una suite puede alcanzar **$100\%$ de cobertura sobre código incompleto** sin enterarse de la omisión.

---

## ¿Qué es la cobertura de código (*Code Coverage*)?

La **cobertura de código** es una métrica de análisis dinámico que cuantifica qué porcentaje de los elementos estructurales del código fuente fue ejecutado por al menos un caso de nuestra batería de pruebas:

$$\text{Coverage} = \frac{\text{Número de elementos cubiertos por la suite}}{\text{Número total de elementos ejecutables}} \times 100\%$$

Dependiendo de qué definamos como «elemento», obtenemos distintas métricas de cobertura estructural:

| Tipo de cobertura | ¿Qué cuenta como elemento? | ¿Qué exige para llegar al $100\%$? |
| :--- | :--- | :--- |
| **Function Coverage** (Cobertura de funciones) | Cada función o método definido en el módulo. | Que cada función sea invocada al menos una vez. |
| **Statement Coverage** (Cobertura de sentencias / líneas) | Cada sentencia o línea ejecutable del código fuente. | Que cada línea ejecutable corra en al menos un test. |
| **Decision / Branch Coverage** (Cobertura de decisiones o ramas) | Cada salida posible (`True` y `False`) de las bifurcaciones `if` y `while`. | Que cada condición se evalúe como `True` al menos una vez y como `False` al menos una vez. |

En la industria, un umbral del $80\%$ o superior suele considerarse saludable como piso de referencia, aunque el valor exigido depende siempre del contexto del sistema (principio 6 del testing).

---

## El ejemplo guía: `cgi_decode`

A lo largo de este tema (siguiendo el enfoque de *The Fuzzing Book* de Andreas Zeller) utilizaremos la función `cgi_decode(s)`, que decodifica textos provenientes de una URL: transforma cada signo `'+'` en un espacio `' '` y cada secuencia hexadecimal `'%' + digit_high + digit_low` (como `'%20'`) en su carácter ASCII correspondiente:

```python
def cgi_decode(s: str) -> str:
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    t = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c == '+':
            t += ' '
        elif c == '%':
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 2
            if digit_high in hex_values and digit_low in hex_values:
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t
```

Observa la riqueza estructural de `cgi_decode`: tiene un ciclo `while`, tres caminos mutuamente excluyentes para cada carácter (`'+'`, `'%'` o carácter normal) y una validación anidada que lanza `ValueError` si los dígitos tras `'%'` no son hexadecimales válidos. Si solo probáramos `cgi_decode("abc")`, toda la lógica de `'+'` y `'%'` quedaría completamente a oscuras.

---

## Preguntas de repaso

> [!question]- ¿Por qué el testing de caja blanca es incapaz de detectar por sí solo los «errores de omisión» (requerimientos que nunca se programaron)?
> Porque las técnicas de caja blanca diseñan y miden pruebas exclusivamente a partir de la estructura del código fuente existente. Si una regla de negocio nunca fue escrita en el código, no existen sentencias ni ramas asociadas a ella, por lo que es posible obtener $100\%$ de cobertura sin que ninguna prueba reclame por la funcionalidad ausente.

> [!question]- En la función `cgi_decode`, ¿qué cuatro tipos de entradas necesitamos combinar como mínimo para cubrir todas sus ramas de ejecución?
> 1. Una cadena con `'+'` (ej. `'+'` o `'a+b'`) para entrar al `if c == '+'`.
> 2. Una cadena con un código hexadecimal válido (ej. `'%20'`) para entrar al `elif c == '%'` y a la rama verdadera del `if digit_high in hex_values...`.
> 3. Una cadena con un código hexadecimal inválido (ej. `'%?a'` o `'%zz'`) envuelta en `try / except ValueError` para cubrir la rama `else: raise ValueError(...)`.
> 4. Una cadena con caracteres normales (ej. `'abc'`) para cubrir el `else: t += c`.

> [!question]- ¿Cuál es la diferencia entre usar la cobertura como «detector de huecos» frente a usarla como «certificado de calidad»?
> Como **detector de huecos**, una cobertura baja (o la lista de líneas no ejecutadas) es información valiosísima: nos garantiza con certeza qué partes del código jamás han sido probadas. En cambio, como **certificado de calidad** es engañosa: tener $100\%$ de cobertura solo significa que las líneas se ejecutaron, pero no garantiza que las aserciones hayan verificado que el resultado fuera correcto.

