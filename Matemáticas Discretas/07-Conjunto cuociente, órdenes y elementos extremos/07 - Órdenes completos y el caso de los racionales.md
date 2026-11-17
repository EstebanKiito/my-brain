---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - origen/complemento
prerrequisitos:
  - "[[06 - Supremo e ínfimo de un conjunto]]"
---

# Órdenes completos y el caso de los racionales

Un conjunto puede estar acotado y aun así no tener supremo: en $\mathbb{R}$ eso no ocurre, en $\mathbb{Q}$ sí. Esa diferencia es lo que separa a los números reales de los racionales y se formaliza con la idea de orden completo.

## Cuándo hay cotas pero no supremo

En $(\mathbb{N},\le)$, $(\mathbb{Z},\le)$ y $(\mathbb{R},\le)$ todo conjunto no vacío acotado superiormente tiene supremo. En $(\mathbb{Q},\le)$, no. Sea

$$S = \{q \in \mathbb{Q} \mid q^2 \le 2\}.$$

Está acotado superiormente (por ejemplo por $2$). Las cotas superiores racionales son los $q$ con $q^2 > 2$, y el candidato a supremo sería $\sqrt{2}$, que no es racional. Como no hay un racional que sea la menor de esas cotas, $S$ **no tiene supremo en $\mathbb{Q}$**. La idea clave es que el supremo debe pertenecer al conjunto donde está definido el orden.

## Orden completo

> [!tip] Definición
> $(A,\preceq)$ es **superiormente completo** si todo $S \subseteq A$ no vacío y acotado superiormente tiene supremo. Es **inferiormente completo** si todo $S$ no vacío y acotado inferiormente tiene ínfimo.

$(\mathbb{Q},\le)$ no es superiormente completo. Tampoco es inferiormente completo: $S' = \{q \in \mathbb{Q} \mid q^2 \ge 2, q>0\}$ está acotado inferiormente y no tiene ínfimo en $\mathbb{Q}$. Es una señal de que las dos nociones van juntas.

> [!tip] Teorema
> $(A,\preceq)$ es superiormente completo si y sólo si es inferiormente completo. Por eso basta hablar de "orden completo".

## Demostración

($\Rightarrow$) Sea $(A,\preceq)$ superiormente completo y $S \subseteq A$ no vacío y acotado inferiormente. Sea $S_{ci}$ el conjunto de todas las cotas inferiores de $S$; no es vacío. Por definición, cada elemento de $S$ es mayor o igual que cada elemento de $S_{ci}$, es decir, $S_{ci}$ está acotado superiormente por los elementos de $S$. Como el orden es superiormente completo, existe $\sup(S_{ci})$.

Dos hechos concluyen. Primero, cada $y \in S$ es cota superior de $S_{ci}$, y el supremo es la **menor** cota superior, luego $\sup(S_{ci}) \preceq y$ para todo $y \in S$: es cota inferior de $S$. Segundo, es cota superior de $S_{ci}$, o sea mayor o igual que toda cota inferior de $S$. Así es la **mayor** cota inferior:

$$\inf(S) = \sup(S_{ci}).$$

($\Leftarrow$) Es análoga, intercambiando los papeles de cotas superiores e inferiores (y $\inf$ por $\sup$).

## Una comprobación finita

En un orden finito la completitud se puede revisar subconjunto por subconjunto. Una comprobación por fuerza bruta sobre cientos de órdenes parciales finitos al azar confirma que nunca ocurre que uno sea superiormente completo sin ser inferiormente completo; los que fallan, fallan en ambos sentidos.

## Preguntas de repaso

> [!question]- ¿Por qué $\sqrt{2}$ no sirve como supremo de $\{q \in \mathbb{Q} \mid q^2 \le 2\}$ dentro de $\mathbb{Q}$?
> Porque el supremo tiene que ser un elemento de $\mathbb{Q}$ y $\sqrt{2}$ es irracional; el conjunto tiene cotas racionales tan cerca de $\sqrt2$ como se quiera, pero ninguna es la menor.

> [!question]- ¿Cómo se construye el ínfimo de $S$ a partir de supremos en la demostración del teorema?
> Se toma el conjunto de todas las cotas inferiores de $S$; ese conjunto está acotado superiormente por los elementos de $S$, y su supremo es el ínfimo de $S$.

> [!question]- ¿Es $(\mathbb{Z},\le)$ completo? ¿Y $(\mathbb{N},\le)$?
> Ambos sí: un conjunto no vacío de enteros acotado superiormente tiene máximo, que es su supremo (y análogo para el ínfimo).

> [!question]- ¿Un conjunto vacío cuenta en la definición de completitud?
> No: se exige $S$ no vacío, porque el supremo del vacío sería el menor elemento del orden y puede no existir.
