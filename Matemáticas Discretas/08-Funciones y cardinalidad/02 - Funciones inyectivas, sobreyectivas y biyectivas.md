---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/funciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones como relaciones y su conteo]]"
---

# Funciones inyectivas, sobreyectivas y biyectivas

Que una función exista no dice nada sobre cuán "fielmente" empareja los elementos. Las tres propiedades de esta nota miden eso: **inyectiva** (no se pierde información), **sobreyectiva** (se cubre todo el destino) y **biyectiva** (ambas a la vez, un emparejamiento perfecto). Son la herramienta para comparar tamaños de conjuntos.

## Las tres definiciones

Sea $f : A \to B$.

| Propiedad | Definición | En palabras |
|---|---|---|
| **Inyectiva** (1-1) | $\forall x, y \in A,\ f(x) = f(y) \Rightarrow x = y$ | no hay dos elementos distintos con la misma imagen |
| **Sobreyectiva** (sobre) | $\forall b \in B\ \exists a \in A,\ b = f(a)$ | todo elemento del codominio tiene preimagen |
| **Biyectiva** | inyectiva y sobreyectiva | cada $b$ tiene exactamente una preimagen |

![Una función inyectiva y una que colapsa puntos](adjuntos/Funci%C3%B3n%20inyectiva%20separa%20puntos.png)

> [!example]- Transcripción de la imagen
> Dos diagramas de flechas de un dominio $X$ a un codominio $Y$. Arriba (inyectiva), $x_1$ y $x_2$ van a $F(x_1)$ y $F(x_2)$, puntos distintos: elementos distintos se envían a elementos distintos. Abajo (no inyectiva), $x_1$ y $x_2$ llegan al mismo punto $F(x_1) = F(x_2)$: se "colapsan".

![Una función sobreyectiva y una que no lo es](adjuntos/Funci%C3%B3n%20sobreyectiva%20cubre%20el%20codominio.png)

> [!example]- Transcripción de la imagen
> Arriba (sobreyectiva), cada punto del codominio recibe al menos una flecha; varios puntos del dominio pueden llegar al mismo. Abajo (no sobreyectiva), hay puntos del codominio sin ninguna flecha, es decir, que no son $F(x)$ para ningún $x$.

> [!tip] Cómo se demuestra cada una
> Para **inyectiva**: tomar $f(x) = f(y)$ y deducir $x = y$. Para **sobreyectiva**: tomar $b$ arbitrario del codominio y exhibir un $a$ con $f(a) = b$. Para **no** serlo basta un contraejemplo: dos elementos con la misma imagen, o un $b$ sin preimagen.

## Ejemplos resueltos

1. $f : A \to \mathcal{P}(A)$, $f(a) = \{a\}$. Es inyectiva ($\{a\} = \{a'\}$ obliga $a = a'$) y no sobreyectiva (el conjunto $\emptyset$ no es un $\{a\}$).
2. $f : A \to \mathcal{P}(A)$, $f(a) = \emptyset$. Ni inyectiva (con $\lvert A \rvert \ge 2$) ni sobreyectiva.
3. $f : \mathbb{N} \to \mathbb{N}_4$, $f(n) = n \bmod 4$. Sobreyectiva (el resto $r$ viene de $n = r$) y no inyectiva ($f(0) = f(4)$).
4. $f : \mathbb{N}_4 \to \mathbb{N}_4$, $f(n) = (n + 2) \bmod 4$. Inyectiva y sobreyectiva: es una biyección que intercambia $0 \leftrightarrow 2$ y $1 \leftrightarrow 3$.

Un criterio que ahorra trabajo: si una función es **creciente** ($x < y \Rightarrow f(x) < f(y)$) entonces es inyectiva. Si $x \ne y$, uno es menor que el otro, y sus imágenes quedan estrictamente ordenadas, luego distintas.

## Cuántas hay en el caso finito

Con $\lvert A \rvert = m$ y $\lvert B \rvert = n$:
- **Inyectivas:** $n(n-1)\cdots(n-m+1)$, porque cada elemento elige una imagen que no usó el anterior (cero si $m > n$). De $\mathbb{N}_3$ a $\mathbb{N}_5$ son $5 \cdot 4 \cdot 3 = 60$.
- **Biyectivas** (con $m = n$): $n!$. De $\mathbb{N}_4$ a $\mathbb{N}_4$, $24$ de las $256$ funciones.
- **Sobreyectivas** de $\mathbb{N}_5$ en $\mathbb{N}_3$: $3^5 - 3\cdot 2^5 + 3 = 150$ (por inclusión-exclusión: se descartan las funciones que se pierden algún valor).

> [!warning] Finito frente a infinito
> Para un conjunto **finito**, $f : A \to A$ es inyectiva si y solo si es sobreyectiva. Para conjuntos infinitos esto falla: $n \mapsto n + 1$ en $\mathbb{N}$ es inyectiva y no sobreyectiva (nadie llega al $0$), mientras que $n \mapsto \lfloor n/2 \rfloor$ es sobreyectiva y no inyectiva. Esa asimetría es lo que permite que un conjunto infinito sea equinumeroso con una parte propia suya.

## Preguntas de repaso

> [!question]- ¿Por qué una función creciente de $\mathbb{N}$ en $\mathbb{N}$ es siempre inyectiva?
> Porque dos elementos distintos son comparables: si $x < y$, entonces $f(x) < f(y)$ y por tanto $f(x) \ne f(y)$. Nunca dos entradas distintas comparten salida.

> [!question]- ¿Puede haber una función sobreyectiva de $\mathbb{N}_3$ en $\mathbb{N}_5$?
> No: la imagen tiene a lo más tantos elementos como el dominio, es decir, $3 < 5$, y quedarían elementos del codominio sin preimagen.

> [!question]- ¿Qué se pierde al pasar de funciones sobre conjuntos finitos a infinitos?
> La equivalencia entre inyectiva y sobreyectiva. En finitos, una implica la otra cuando dominio y codominio coinciden; en infinitos pueden darse por separado (por ejemplo $n \mapsto n + 1$).
