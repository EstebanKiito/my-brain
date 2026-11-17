---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles y caracterizaciones equivalentes]]"
---

# Árboles con raíz y su terminología

En computación casi siempre se trabaja con árboles en los que un vértice se distingue de los demás: la **raíz**. Elegir una raíz da una orientación natural (hacia abajo, lejos de la raíz) y un vocabulario para hablar de jerarquías, estructuras de datos y recorridos.

## La raíz y el dibujo

Un **árbol con raíz** es un árbol con un vértice $r$ marcado. Se dibuja con $r$ arriba y los demás vértices hacia abajo; las **hojas** (grado $\le 1$) quedan abajo. Como el árbol tiene un único camino entre cualquier par de vértices, cada vértice $x$ tiene un único camino hasta $r$, y de él salen todas las definiciones.

## Vocabulario

Sea $T$ un árbol con raíz $r$ y $x$ un vértice.

| Término | Significado |
|---|---|
| **Profundidad** de $x$ | Largo del camino de $r$ a $x$ (la raíz tiene profundidad $0$) |
| **Altura** del árbol | Máximo de las profundidades de sus vértices |
| **Ancestros** de $x$ | Vértices del camino de $x$ a $r$ (incluido el propio $x$) |
| **Padre** de $x$ | Su ancestro propio de mayor profundidad |
| **Hijo** | $x$ es hijo de su padre; la raíz no tiene padre |
| **Hermanos** | Vértices con el mismo padre |

![Definiciones sobre un árbol con raíz](adjuntos/Definiciones%20sobre%20un%20%C3%A1rbol%20con%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> Árbol con raíz $r$ arriba. Se marca un vértice $x$ en un nivel intermedio: la línea punteada de $r$ a $x$ son sus **ancestros**, el ancestro justo encima de $x$ es su **padre**, y los vértices bajo el mismo padre son sus **hermanos**. A la izquierda, "profundidad de $x$" mide el tramo desde la raíz hasta $x$ y "altura de $x$" el tramo desde $x$ hasta el nivel más bajo; a la derecha, "altura del árbol" cubre el nivel más profundo.

## Ejemplo pequeño

Sea el árbol de aristas $r\!-\!a$, $r\!-\!b$, $a\!-\!c$, $a\!-\!d$, $d\!-\!e$ con raíz $r$.

- Profundidades: $r{:}0$; $a, b{:}1$; $c, d{:}2$; $e{:}3$. La altura del árbol es $3$.
- Ancestros de $e$: $e, d, a, r$. Su padre es $d$.
- $c$ y $d$ son hermanos (padre $a$). Las hojas son $b$, $c$ y $e$.

> [!tip] Idea clave
> Todo se define a partir del único camino de $r$ a $x$: su largo es la profundidad, sus vértices son los ancestros y el penúltimo es el padre.

> [!warning] Dos "alturas"
> La altura **del árbol** es la profundidad máxima. La altura **de un vértice** $x$ (que aparece en algunos apuntes) se mide hacia abajo desde $x$; no son lo mismo. En los teoremas de este tema "altura" es siempre la del árbol.

## Preguntas de repaso

> [!question]- ¿Por qué el padre de un vértice está bien definido?
> Porque el camino de $x$ a la raíz es único; sus ancestros propios están ordenados por profundidad y el de mayor profundidad es único.

> [!question]- ¿Un vértice es ancestro de sí mismo?
> Sí, por definición: aparece en el camino entre él y $r$. Los ancestros propios son los demás.

> [!question]- ¿Cambia la altura del árbol al elegir otra raíz?
> Sí en general: las profundidades se miden desde la raíz elegida. El árbol como grafo no cambia, pero su altura sí.
