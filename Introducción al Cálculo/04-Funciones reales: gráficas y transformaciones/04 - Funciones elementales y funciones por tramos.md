---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Cómo hallar el recorrido de una función]]"
---

# Funciones elementales y funciones por tramos

Casi todas las funciones que se grafican en el curso se obtienen a partir de un catálogo corto de funciones básicas, modificadas por las transformaciones de las notas siguientes. Reconocer a primera vista la forma de $x^n$, $\sqrt[n]{x}$, $\tfrac{1}{x^n}$ y $|x|$ es la mitad del trabajo.

## El catálogo

**Constante y lineal.** $f(x) = b$ es una recta horizontal; $f(x) = mx + b$ es una recta de pendiente $m$ que corta el eje $y$ en $b$.

![Funciones constante y lineal](adjuntos/Funciones%20constante%20y%20lineal.png)

> [!example]- Transcripción de la figura (clase 9)
> A la izquierda, una recta roja horizontal a la altura $b$ sobre el eje $y$ ($f(x) = b$). A la derecha, una recta roja creciente que corta el eje $y$ en $b$ ($f(x) = mx + b$).

**Potencias $x^n$.** Si $n$ es par ($x^2$, $x^4$) la gráfica es simétrica respecto del eje $y$, abre hacia arriba y su recorrido es $[0, \infty)$; si $n$ es impar ($x^3$, $x^5$) pasa por el origen, crece y se aplana cerca de $0$, con recorrido $\mathbb{R}$.

![Funciones potencia](adjuntos/Funciones%20potencia.png)

> [!example]- Transcripción de la figura (clase 9)
> Cuatro gráficos rojos: $f(x) = x^2$ (parábola en forma de U con vértice en el origen), $f(x) = x^3$ (curva creciente que pasa por el origen y se aplana en él), $f(x) = x^4$ (en forma de U más achatada en el fondo que $x^2$) y $f(x) = x^5$ (como $x^3$, más pegada al eje cerca del origen).

**Raíces $\sqrt[n]{x}$.** Para $n$ par ($\sqrt{x}$, $\sqrt[4]{x}$) el dominio es $[0, \infty)$ y el recorrido también; para $n$ impar ($\sqrt[3]{x}$, $\sqrt[5]{x}$) el dominio es $\mathbb{R}$ y la gráfica tiene tangente vertical en el origen. Son las inversas de las potencias.

![Funciones raíz](adjuntos/Funciones%20raíz.png)

> [!example]- Transcripción de la figura (clase 9)
> Cuatro gráficos rojos: $\sqrt{x}$ (solo para $x \ge 0$, creciente y con tangente vertical en el origen), $\sqrt[3]{x}$ (definida en todo $\mathbb{R}$, creciente, simétrica respecto del origen), $\sqrt[4]{x}$ (solo para $x \ge 0$) y $\sqrt[5]{x}$ (en todo $\mathbb{R}$).

**Recíprocas $\tfrac{1}{x^n}$.** No están definidas en $x = 0$. $\tfrac{1}{x}$ tiene dos ramas, una en el primer cuadrante y otra en el tercero; $\tfrac{1}{x^2}$ tiene ambas ramas sobre el eje $x$. Los ejes son **asíntotas**: la gráfica se acerca a ellos sin tocarlos.

![Funciones recíprocas](adjuntos/Funciones%20recíprocas.png)

> [!example]- Transcripción de la figura (clase 9)
> A la izquierda $f(x) = \frac{1}{x}$: una rama en el cuadrante superior derecho (arriba del eje $x$, a la derecha del eje $y$) y otra en el inferior izquierdo, ambas pegadas a los ejes. A la derecha $f(x) = \frac{1}{x^2}$: dos ramas por encima del eje $x$, una a cada lado del eje $y$, que se disparan hacia arriba al acercarse a $x = 0$.

## Valor absoluto

$f(x) = |x|$ coincide con $y = x$ a la derecha del eje $y$ y con $y = -x$ a la izquierda: una "V" con vértice en el origen, dominio $\mathbb{R}$ y recorrido $[0, \infty)$.

![Gráfica del valor absoluto](adjuntos/Gráfica%20del%20valor%20absoluto.png)

> [!example]- Transcripción de la figura (clase 9)
> Dos semirrectas rojas que parten del origen: una con pendiente $1$ hacia la derecha y otra con pendiente $-1$ hacia la izquierda, formando una "V" simétrica respecto del eje $y$. Debajo se lee $f(x) = |x|$.

## Parte entera

La **parte entera** $\lfloor x \rfloor$ (en la clase $[x]$) se define por $[x] = n \iff n \le x < n + 1$ para $n \in \mathbb{Z}$: es el mayor entero que no supera a $x$. Su gráfico es una escalera con saltos.

![Gráfica de la parte entera](adjuntos/Gráfica%20de%20la%20parte%20entera.png)

> [!example]- Transcripción de la figura (clase 9)
> Una escalera: en cada intervalo $[n, n + 1)$ hay un segmento horizontal rojo a la altura $n$, con punto lleno en el extremo izquierdo (incluido) y punto vacío en el derecho (excluido). En $x = 1$ el valor salta de $0$ a $1$. La escalera continúa hacia ambos lados con puntos suspensivos.

## Funciones por tramos

Una función **definida por tramos** usa una fórmula distinta en cada intervalo. Se grafica tramo a tramo y se **marca qué extremo pertenece a qué tramo** (punto lleno o vacío).

Ejemplo (clase 9): $f(x) = \begin{cases} x^2 & \text{si } x \le 1 \\ 2x + 1 & \text{si } x > 1 \end{cases}$. Hasta $x = 1$ es la parábola, con $f(1) = 1$ (punto lleno); desde $x = 1$ la recta, que empieza en el valor $2 \cdot 1 + 1 = 3$ con punto vacío porque $x = 1$ no pertenece a ese tramo. En $x = 1$ la gráfica da un **salto** de $1$ a $3$.

> [!tip] Cómo graficar por tramos
> 1. Dibujar cada fórmula solo sobre su intervalo.
> 2. Calcular el valor en cada extremo con ambas fórmulas.
> 3. Marcar con punto lleno el valor que cuenta y con punto vacío el límite del otro tramo.
> 4. El recorrido es la unión de los recorridos de cada tramo.

## Preguntas de repaso

> [!question]- ¿En qué se diferencian las gráficas de $x^2$ y de $x^3$ cerca del origen y en los extremos?
> $x^2$ es par: simétrica respecto del eje $y$, siempre $\ge 0$. $x^3$ es impar: simétrica respecto del origen, negativa para $x < 0$. En ambos casos son planas cerca de $0$, pero $x^3$ cruza el eje en vez de rebotar.

> [!question]- ¿Cuál es el dominio de $\sqrt[3]{x}$ y de $\sqrt[4]{x}$?
> $\mathbb{R}$ y $[0, \infty)$, respectivamente: la raíz de índice impar existe para todo real; la de índice par solo para $x \ge 0$.

> [!question]- ¿Cuánto vale $[-1{,}5]$ y por qué?
> $-2$, porque $-2 \le -1{,}5 < -1$: la parte entera es el mayor entero que no supera al número.

> [!question]- ¿Cuál es el recorrido de $f(x) = x^2$ si $x \le 1$, y $2x + 1$ si $x > 1$?
> En el primer tramo, $x^2$ con $x \le 1$ toma todos los valores $[0, \infty)$; en el segundo, $2x + 1 > 3$. La unión es $[0, \infty)$.
