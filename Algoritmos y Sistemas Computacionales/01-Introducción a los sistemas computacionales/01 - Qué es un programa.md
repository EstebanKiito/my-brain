---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Introducción a los sistemas computacionales"
tags:
  - algoritmos/programas
  - algoritmos/compilacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un algoritmo|Qué es un algoritmo]]"
---

# Qué es un programa

Un **programa** es una secuencia de instrucciones que el computador ejecuta para resolver un problema. Esta nota parte del programa más simple que existe —mostrar un saludo en pantalla— y muestra qué hay detrás: el texto que escribe una persona, los caracteres que lo representan y los bits que finalmente entiende la máquina.

## El programa más simple

En C, el lenguaje que usa el curso para hablar del hardware, un saludo se escribe así:

```c
#include <stdio.h>

int main() {
    printf("Hello, world\n");
    return 0;
}
```

Cada línea cumple un papel:
- `#include <stdio.h>` trae la biblioteca de entrada y salida, donde está definida `printf`.
- `int main()` marca el **punto de entrada**: por aquí empieza a ejecutarse el programa.
- `printf("Hello, world\n")` escribe el texto en pantalla; `\n` representa un salto de línea.
- `return 0` termina el programa e informa que todo salió bien.

> [!tip] La idea central
> Un programa no es magia: es una lista ordenada de instrucciones y los datos con los que trabaja. El computador las ejecuta una tras otra, exactamente como están escritas.

## Tres representaciones del mismo programa

El mismo programa se puede mirar en tres niveles:

| Nivel | Qué se ve | Quién lo entiende |
|---|---|---|
| **Código fuente** | `printf("Hello, world\n");` | Una persona |
| **Caracteres** | Cada letra con su número (por ejemplo, `#` = 35, `i` = 105) | Un editor de texto |
| **Bits** | Secuencias de 0 y 1 | El procesador |

El código fuente es texto, y todo texto se guarda como una secuencia de **caracteres**. Cada carácter tiene un número asociado (su código **ASCII**, que se ve en el tema de codificación). Al compilar, esos caracteres se traducen a instrucciones de máquina, que son secuencias de **bits**.

![Programa en C descompuesto en caracteres con su código ASCII](adjuntos/Programa%20en%20caracteres.png)

> [!example]- Transcripción de la imagen
> - El texto del programa aparece letra por letra, separado en filas.
> - Bajo cada carácter está su valor decimal en ASCII: `#` = 35, `i` = 105, `n` = 110, `t` = 116, etc.
> - `<sp>` marca un espacio y `\n` el salto de línea.
> - La idea es que el código fuente también es una secuencia de números, igual que cualquier otro texto.

## Un programa es un algoritmo escrito para una máquina

Un algoritmo y un programa persiguen lo mismo: resolver un problema con pasos ordenados. La diferencia es el destinatario. Un algoritmo se puede escribir en español o en pseudocódigo; un programa se escribe en un **lenguaje de programación**, que tiene reglas estrictas para que la máquina no tenga que interpretar nada.

Por eso el curso parte con un algoritmo real: el **Stock Span**, que recibe los precios de una acción durante varios días y calcula, para cada día, cuántos días seguidos el precio fue menor o igual. Es un recordatorio de que detrás de cada programa hay un problema que se quiere resolver.

> [!warning] El computador no adivina
> Si el programa dice `printf("Hola"` sin cerrar el paréntesis, no se ejecuta: no compila. La máquina hace lo que está escrito, no lo que se quiso escribir. Gran parte de aprender a programar es aprender a decir exactamente lo que se quiere.

## Preguntas de repaso

> [!question]- ¿Por qué un programa escrito en C no puede ejecutarse directamente en el procesador?
> Porque el procesador solo entiende instrucciones de máquina en binario. El código C debe traducirse primero con un compilador y un ensamblador.

> [!question]- ¿Qué diferencia hay entre el código fuente y el programa compilado?
> El código fuente es texto legible por personas, escrito en un lenguaje como C. El programa compilado es una secuencia de bits con instrucciones que el procesador puede ejecutar.

> [!question]- Si dos personas escriben programas distintos para el mismo problema, ¿necesariamente uno está mal?
> No. Puede haber muchas soluciones correctas. Se comparan por claridad, largo o eficiencia, pero ambas pueden llegar al resultado.

> [!question]- ¿Qué significa que `main` sea el punto de entrada?
> Que la ejecución del programa comienza en esa función. Sin un `main`, el sistema no sabe por dónde empezar.
