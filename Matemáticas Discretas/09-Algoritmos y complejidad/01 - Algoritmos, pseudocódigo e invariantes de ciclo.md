---
ramo: "Matemáticas Discretas"
tema: "Algoritmos y complejidad"
tags:
  - discretas/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Algoritmos, pseudocódigo e invariantes de ciclo

Para razonar sobre un programa sin ejecutarlo hace falta decir con precisión qué recibe, qué debe entregar y por qué lo hace bien. Esta nota fija la noción de algoritmo, el significado de "correcto" y la técnica estándar para ciclos: el **invariante**, que se demuestra por inducción sobre las iteraciones.

## Qué es un algoritmo

Un **algoritmo** es un método que transforma una entrada (*input*) válida en una salida (*output*). Se le exigen tres propiedades: **precisión** (cada instrucción es no ambigua), **determinismo** (el comportamiento depende solo de la entrada) y **finitud** (el texto del algoritmo tiene un número finito de instrucciones). Los modelos formales (máquinas de Turing, cálculo $\lambda$, funciones recursivas) resultan equivalentes entre sí; para este curso basta la idea intuitiva de "pasos que resuelven un problema".

Se escribe en **pseudocódigo**: `if`, `while`, `for`, `return`, más notación cómoda para arreglos y conjuntos. La entrada se describe con **precondiciones** y la salida con **postcondiciones**.

> [!tip] Correcto e incorrecto
> Un algoritmo es **correcto** si para todo input válido se detiene y produce un output correcto. Es **incorrecto** si existe al menos un input válido para el que no se detiene o produce un output erróneo. Un solo contraejemplo basta para refutarlo; demostrar corrección exige un argumento general.

El análisis de algoritmos persigue dos objetivos: demostrar que son correctos (esta nota y la siguiente) y estimar los recursos que consumen (el resto del tema).

## Corrección parcial y terminación

En un algoritmo iterativo la demostración se parte en dos:

- **Corrección parcial:** si el algoritmo se detiene, se cumplen las postcondiciones.
- **Terminación:** el algoritmo efectivamente se detiene.

Solo importan los ciclos, porque el código sin ciclos es una secuencia finita de pasos. Un ciclo tiene una condición de continuación $G$ (`while (G) ...`).

## Invariante de ciclo

Un **invariante** $I(k)$ es una propiedad sobre las variables que es verdadera al terminar la iteración $k$, para todo $k$. Se elige de modo que, al salir del ciclo, implique la postcondición. La demostración es una inducción simple:

1. **Base:** las precondiciones implican $I(0)$ (estado previo a la primera iteración).
2. **Paso:** si $G$ e $I(k)$ valen antes de una iteración, entonces $I(k+1)$ vale después.
3. **Salida:** cuando $G$ es falsa e $I(N)$ es verdadero, las postcondiciones se cumplen.

La **terminación** se prueba exhibiendo una cantidad natural que decrece estrictamente en cada iteración; como no existen cadenas infinitas decrecientes en $\mathbb{N}$, $G$ termina siendo falsa (es el principio del buen orden).

## Ejemplo: multiplicar sin multiplicar

Para $n, m \in \mathbb{N}$ se quiere calcular $p = n \cdot m$ solo con sumas y restas.

![Algoritmo Multiply y su traza de variables](adjuntos/Algoritmo%20Multiply%20y%20traza%20de%20variables.png)

> [!example]- Transcripción de la imagen
> - Pseudocódigo de `Multiply(n, m)`: `z ← 0`, `w ← m`, `while w ≠ 0` hacer `z ← z + n` y `w ← w − 1`, y luego `return z`. (En la lámina el paso 4 dice `z + x`; es `z + n`.)
> - Tabla con $n = a$, $m = b$: en la iteración $i$ se tiene $z = i\cdot a$ y $w = b - i$; en la iteración $b$ queda $z = b \cdot a$ y $w = 0$.
> - Debajo se destaca que hay $b$ iteraciones y que al término de cada una vale $z_i = n \cdot (m - w_i)$.

La traza sugiere el invariante $P(i)$: tras la iteración $i$, $z_i = n\,(m - w_i)$.

- **Base:** $z_0 = 0 = n(m - m) = n(m - w_0)$.
- **Paso:** $z_{i+1} = z_i + n = n(m - w_i) + n = n(m - (w_i - 1)) = n(m - w_{i+1})$.
- **Salida:** el ciclo termina con $w = 0$, y entonces $z = n \cdot m$.
- **Terminación:** $w$ parte en $m \in \mathbb{N}$ y baja de a uno, así que llega a $0$ tras $m$ iteraciones.

> [!warning] Un invariante debe conectar con la postcondición
> Una propiedad cierta en cada iteración pero que no dice nada sobre el resultado (por ejemplo "$w \ge 0$") es invariante y a la vez inútil. El invariante bueno relaciona las variables de modo que, con la condición de salida, entregue exactamente lo pedido.

## Preguntas de repaso

> [!question]- ¿Por qué se separan corrección parcial y terminación?
> Porque son afirmaciones distintas: un ciclo infinito satisface trivialmente "si termina, entonces...". Sin terminación, la corrección parcial no garantiza que exista un resultado.

> [!question]- En Multiply, ¿qué ocurre con $I(k)$ cuando $w$ llega a $0$?
> $z = n(m - 0) = n \cdot m$, que es la postcondición. Por eso el invariante $z = n(m - w)$ sirve: al combinarlo con $w = 0$ da el resultado.

> [!question]- ¿Qué cantidad decrece en Multiply y por qué demuestra terminación?
> Es $w$: parte en $m$, baja en $1$ por iteración y es siempre natural. No puede decrecer indefinidamente, así que alcanza $0$ y la guarda $w \ne 0$ se vuelve falsa.

> [!question]- ¿Cómo se conecta el invariante con la inducción?
> La base es el estado antes del ciclo, el paso es "una iteración preserva $I$" y la conclusión vale para el número de iteraciones con que el ciclo termina.
