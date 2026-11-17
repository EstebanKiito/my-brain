---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/funciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Funciones inyectivas, sobreyectivas y biyectivas]]"
---

# Composición e inversa de funciones

Dos funciones se pueden encadenar (aplicar una y luego otra) y una función se puede "devolver" (leer sus flechas al revés). Estas dos operaciones se definen primero para relaciones cualesquiera y luego se estudia cuándo el resultado vuelve a ser función. Son la base para probar que la equinumerosidad es una relación de equivalencia.

## Relación inversa y composición

Si $R \subseteq A \times B$ es una relación, su **inversa** es $R^{-1} = \{(b, a) \in B \times A \mid a\,R\,b\}$: se dan vuelta los pares. Una función $f$ es **invertible** si $f^{-1}$ también es una función de $B$ en $A$.

Dadas $R \subseteq A \times B$ y $S \subseteq B \times C$, su **composición** es

$$S \circ R = \{(a, c) \in A \times C \mid \exists b \in B,\ a\,R\,b \wedge b\,S\,c\}.$$

Para funciones, $(g \circ f)(x) = g(f(x))$: primero actúa $f$ y luego $g$, aunque se escriba al revés.

## La composición de funciones es una función

> [!tip] Proposición
> Si $f : A \to B$ y $g : B \to C$ son funciones, $g \circ f : A \to C$ es una función total.

- **Es función.** Si $(g \circ f)(x) = z_1$ y $(g \circ f)(x) = z_2$, entonces $g(f(x)) = z_1$ y $g(f(x)) = z_2$. Como $f$ es función, $f(x)$ es un único $y$; y como $g$ es función, $g(y)$ es único. Luego $z_1 = z_2$.
- **Es total.** Dado $x \in A$, existe $y = f(x)$ por ser $f$ total, y existe $z = g(y)$ por ser $g$ total. Así $(x, z) \in g \circ f$.

## Qué propiedades se heredan

Si $f$ y $g$ son **inyectivas**, $g \circ f$ lo es: de $g(f(x_1)) = g(f(x_2))$, la inyectividad de $g$ da $f(x_1) = f(x_2)$ y la de $f$ da $x_1 = x_2$. Si ambas son **sobreyectivas**, $g \circ f$ también: dado $z \in C$ hay $y$ con $g(y) = z$ (por $g$) y $x$ con $f(x) = y$ (por $f$), de modo que $z = (g \circ f)(x)$. Por lo tanto, la composición de biyecciones es biyección.

La recíproca es parcial. Si $g \circ f$ es inyectiva, entonces $f$ es inyectiva (si $f(x_1) = f(x_2)$, al aplicar $g$ resultan iguales sus imágenes bajo $g \circ f$), pero $g$ puede no serlo: con $f : \{1\} \to \{1, 2\}$ y $g : \{1, 2\} \to \{1\}$ constante, $g \circ f$ es la identidad y $g$ no es inyectiva. Análogamente, si $g \circ f$ es sobreyectiva, entonces $g$ lo es.

## La inversa de una biyección

> [!tip] Teorema
> Si $f : A \to B$ es biyectiva, entonces $f^{-1}$ es una función biyectiva de $B$ en $A$. En particular, toda biyección es invertible.

Demostración, una propiedad a la vez:
1. **Función.** Si $y\,f^{-1}\,x_1$ e $y\,f^{-1}\,x_2$, entonces $f(x_1) = y = f(x_2)$, y la inyectividad de $f$ da $x_1 = x_2$.
2. **Total.** Dado $y \in B$, la sobreyectividad de $f$ da algún $x$ con $f(x) = y$, o sea $f^{-1}(y) = x$.
3. **Inyectiva.** Si $f^{-1}(y_1) = f^{-1}(y_2) = x$, entonces $f(x) = y_1$ y $f(x) = y_2$; como $f$ es función, $y_1 = y_2$.
4. **Sobreyectiva.** Dado $x \in A$, como $f$ es total existe $y = f(x)$, y entonces $f^{-1}(y) = x$.

Ejemplo concreto: $f : \mathbb{N}_4 \to \mathbb{N}_4$, $f(n) = (n + 2) \bmod 4$ cumple $f \circ f = \mathrm{id}$, así que es su propia inversa. En cambio $n \mapsto n \bmod 4$ de $\mathbb{N}$ en $\mathbb{N}_4$ no es invertible: su relación inversa asocia $0$ a $0, 4, 8, \dots$ y deja de ser función.

> [!warning] Inversa de relación frente a función inversa
> $f^{-1}$ siempre existe como **relación**; lo que hay que verificar es que sea función. Para eso hacen falta ambas condiciones: sin sobreyectividad algún $y$ no tiene imagen bajo $f^{-1}$, y sin inyectividad algún $y$ tendría dos.

## Preguntas de repaso

> [!question]- ¿Por qué hay que probar que $g \circ f$ es función y no basta con definirla?
> Porque la composición se define para relaciones y puede salir multivaluada. Para funciones, la unicidad de $f(x)$ y de $g(f(x))$ garantiza una única imagen, y la totalidad de ambas garantiza que exista.

> [!question]- Si $g \circ f$ es inyectiva, ¿qué se puede asegurar de $f$ y de $g$?
> Que $f$ es inyectiva; de $g$ no se puede asegurar nada, como muestra la función constante compuesta con una inclusión.

> [!question]- ¿Qué parte de la prueba de $f^{-1}$ biyectiva usa la inyectividad de $f$ y cuál la sobreyectividad?
> Que $f^{-1}$ sea función usa la inyectividad (una sola preimagen); que sea total usa la sobreyectividad (existe preimagen). Las otras dos partes son simétricas con las propiedades de $f$ como función.
