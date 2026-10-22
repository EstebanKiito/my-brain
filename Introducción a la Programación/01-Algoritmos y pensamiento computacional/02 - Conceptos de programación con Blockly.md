---
ramo: "Introducción a la Programación"
tema: "Algoritmos y pensamiento computacional"
tags:
  - programacion/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un algoritmo]]"
---

# Conceptos de programación con Blockly

**Blockly** es un entorno donde se programa encajando bloques de colores en vez de escribir texto. Sirve para aprender las ideas básicas de la programación sin preocuparse de la sintaxis (comas, paréntesis, mayúsculas). Los juegos **Turtle** (una tortuga que dibuja) y **Maze** (un personaje que recorre un laberinto) muestran, problema a problema, los conceptos que después se usan en Python.

## Turtle: una tortuga que dibuja

La tortuga tiene un lápiz y obedece órdenes como "avanza 100 pasos" (`move forward by 100`) o "gira 90 grados a la derecha" (`turn right by 90`). Cada problema de dibujo introduce un concepto nuevo.

### Instrucción y orden
- **Dibujar una línea:** basta un bloque. Una **instrucción** es una orden que el computador ejecuta.
- **Dibujar una esquina:** avanzar, girar y avanzar. Las instrucciones se ejecutan una tras otra, de arriba hacia abajo: el **orden** cambia el resultado.
- **Dibujar un cuadrado:** avanzar y girar, cuatro veces.

![Blockly: cuadrado dibujado con siete bloques en orden](adjuntos/Blockly%20cuadrado%20con%20instrucciones%20en%20orden.png)

> [!example]- Transcripción de la imagen
> - Arriba, el dibujo: un cuadrado con la tortuga en la esquina inferior izquierda.
> - Abajo, los bloques: `move forward by 100`, `turn right by 90`, repetido hasta completar cuatro lados (cuatro avances y tres giros).
> - Concepto marcado: **orden**.

### Repetición
Para dibujar un **círculo** la tortuga avanza 1 paso y gira 1 grado… 360 veces. Escribir 720 bloques sería absurdo, así que se usa el bloque `repeat 360 times`, que repite lo que tiene adentro. Esta es la idea de **repetición** o **ciclo**, que en Python serán `while` y `for` (ver el tema de ciclos).

El cuadrado también se puede escribir así: `repeat 4 times` con `move forward 100` y `turn right 90` adentro. Menos bloques, mismo dibujo.

### Funciones: darle nombre a un grupo de pasos
Para dibujar **dos círculos** se podría copiar dos veces el bloque del círculo, pero eso es **código repetitivo**: más largo, y si hay que cambiar algo se debe cambiar en dos lugares. La solución es crear un bloque nuevo, `dibujar circulo`, que agrupa los pasos, y **llamarlo** cada vez que se necesite.

![Blockly: función dibujar circulo y dos llamadas](adjuntos/Blockly%20dos%20c%C3%ADrculos%20con%20funci%C3%B3n%20dibujar%20circulo.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, el resultado: dos círculos que se tocan sobre fondo negro.
> - Bloque morado **definición** `to dibujar circulo`: adentro, `repeat 360 times` con `move forward by 1` y `turn right by 1`.
> - Bloques de **llamada**: `dibujar circulo`, luego `pen up` (levantar el lápiz), girar 90 a la derecha, avanzar 100, girar 90 a la izquierda, `pen down`, otra vez `dibujar circulo` y finalmente `hide turtle`.

Eso es una **función**: un grupo de instrucciones con nombre, que se define una vez y se usa muchas. En Python se escriben con `def`.

### Variables
En dibujos como una espiral, la tortuga avanza un poco más en cada vuelta. Para eso se necesita guardar un número que va cambiando ("cuánto avanzo ahora"): una **variable**. Es un espacio con nombre donde se guarda un valor que se puede leer y modificar.

## Maze: decidir según lo que hay

En el laberinto, el personaje debe llegar a la meta usando bloques como "avanzar", "girar" y "repetir hasta llegar". En los niveles más avanzados aparece un bloque nuevo: **si hay camino a la izquierda, girar a la izquierda**. Esa es la idea de **condición**: el programa toma decisiones según la situación, lo que en Python será `if`.

## Resumen de conceptos

| Concepto | En Blockly | En Python (más adelante) |
|---|---|---|
| Instrucción | Un bloque | Una línea, como `print(...)` |
| Orden (secuencia) | Bloques apilados | Líneas de arriba hacia abajo |
| Repetición | `repeat … times` | `for`, `while` |
| Condición | `if path ahead` | `if`, `elif`, `else` |
| Función | Bloque `to …` y su llamada | `def nombre():` y `nombre()` |
| Variable | Bloque de variable | `x = 10` |

> [!tip] Idea clave
> Todo programa, por grande que sea, se construye con estos pocos ingredientes: instrucciones en orden, repeticiones, decisiones, funciones y variables. Lo que cambia de un lenguaje a otro es cómo se escriben.

> [!warning] Copiar y pegar es una señal
> Si te encuentras copiando el mismo grupo de instrucciones varias veces, probablemente necesitas una repetición o una función.

## Preguntas de repaso

> [!question]- ¿Por qué conviene usar `repeat` en vez de copiar los bloques?
> Porque el programa queda más corto y fácil de leer, y si hay que cambiar algo (por ejemplo el tamaño del paso) se cambia en un solo lugar.

> [!question]- ¿Qué diferencia hay entre definir una función y llamarla?
> Definirla es enseñarle al computador qué pasos agrupa el nombre (no dibuja nada todavía). Llamarla es pedirle que ejecute esos pasos en ese momento; se puede llamar todas las veces que se quiera.

> [!question]- Para dibujar una espiral, ¿por qué no basta con repeticiones y se necesita una variable?
> Porque en cada vuelta el largo del avance cambia. Hace falta un lugar donde guardar ese largo y aumentarlo en cada repetición.
