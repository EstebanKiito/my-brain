---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles y caracterizaciones equivalentes]]"
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Hojas, poda y número de aristas de un árbol

Para demostrar propiedades de árboles por inducción hace falta un modo de "achicar" un árbol y seguir teniendo un árbol. Ese modo es quitar una hoja. De ahí sale la caracterización más práctica: un grafo conexo con $n$ vértices es un árbol si y solo si tiene exactamente $n - 1$ aristas.

## Hojas y poda

Una **hoja** es un vértice de grado menor o igual a $1$ (en un árbol de un solo vértice, ese vértice tiene grado $0$). Todo árbol con al menos dos vértices tiene al menos dos hojas: el extremo de un camino de largo máximo no puede tener otro vecino, o el camino se alargaría o habría un ciclo.

> [!tip] Lema de la poda
> Si $T$ es un árbol y $v$ es una hoja de $T$, entonces $T - v$ (se quita el vértice y su arista) también es un árbol.

**Por qué.** Sean $u, w$ dos vértices distintos de $v$ y $P$ el único camino entre ellos en $T$. Los vértices interiores de un camino tienen grado al menos $2$, y $v$ tiene grado $1$, luego $v$ no está en $P$. Entonces $P$ sigue existiendo en $T - v$, y sigue siendo el único: un camino nuevo habría sido un segundo camino ya en $T$.

## El número de aristas: $|E| = n - 1$

> [!tip] Teorema
> Un grafo $T$ con $n$ vértices es un árbol si y solo si es conexo y tiene exactamente $n - 1$ aristas.

**(⇒) Por inducción en $n$.**
- *Base:* $n = 1$ es un vértice sin aristas, $0 = 1 - 1$.
- *HI:* todo árbol con $n$ vértices tiene $n - 1$ aristas.
- *TI:* un árbol $T$ con $n + 1$ vértices tiene una hoja $v$. Por el lema, $T - v$ es un árbol con $n$ vértices, luego $n - 1$ aristas. Como $v$ tiene grado $1$, $T$ tiene una arista más: $n$ aristas, que es $(n+1) - 1$.

**(⇐)** Se usa que un grafo con $n$ vértices y $k$ aristas tiene al menos $n - k$ componentes conexas (cada arista une a lo más dos componentes y por tanto reduce en a lo más uno su número). Sea $T$ conexo con $n - 1$ aristas y $e$ una arista cualquiera. $T - e$ tiene $n - 2$ aristas, así que tiene al menos $2$ componentes: $e$ es de corte. Como $e$ era arbitraria, todas las aristas son de corte y $T$ es un árbol.

## Para qué sirve

- **Chequear si un grafo conexo es árbol** basta con contar aristas: el árbol de diez vértices del tema tiene $9$ aristas.
- **Red mínima:** $n$ computadores se pueden comunicar entre sí con $n - 1$ cables y no con menos.
- **Bosques:** un bosque con $n$ vértices y $c$ componentes tiene $n - c$ aristas, pues cada componente es un árbol con (vértices $- 1$) aristas.

## Todo árbol es bipartito

Un grafo es bipartito si y solo si no tiene ciclos de largo impar. Un árbol no tiene ciclos, luego es bipartito. Concretamente se colorea cada vértice según la paridad de su distancia a un vértice fijo $r$: aristas vecinas difieren en distancia exactamente en $1$, así que sus colores son distintos.

> [!warning] Trampa
> "Conexo con $n - 1$ aristas" necesita la palabra **conexo**. Un grafo con $n - 1$ aristas puede tener un ciclo y estar desconectado (un triángulo más un vértice aislado tiene $4$ vértices y $3$ aristas y no es árbol).

## Preguntas de repaso

> [!question]- ¿Por qué se induce quitando una hoja y no un vértice cualquiera?
> Quitar un vértice cualquiera puede desconectar el grafo. Una hoja nunca está en el interior de un camino, así que el resto sigue conexo y sin ciclos.

> [!question]- ¿Dónde se usa que $v$ tiene grado exactamente $1$ en la inducción de $|E| = n - 1$?
> En el paso inductivo: quitar $v$ borra exactamente una arista, así que se pasa de $n - 1$ aristas a $n$.

> [!question]- ¿Por qué todo árbol con al menos dos vértices tiene dos hojas?
> Los extremos de un camino de largo máximo solo pueden tener un vecino (el del camino): otro vecino alargaría el camino o cerraría un ciclo.

> [!question]- ¿Cuántas aristas tiene un bosque de $7$ vértices y $3$ componentes?
> $7 - 3 = 4$ aristas.
