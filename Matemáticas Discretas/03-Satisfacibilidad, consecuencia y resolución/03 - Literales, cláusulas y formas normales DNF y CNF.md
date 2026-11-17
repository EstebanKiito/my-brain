---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Satisfacibilidad de fórmulas y tautologías proposicionales]]"
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Literales, cláusulas y formas normales DNF y CNF

Las fórmulas pueden escribirse de infinitas maneras equivalentes. Las **formas normales** fijan un formato estándar: toda fórmula tiene una versión equivalente con esa estructura. La forma conjuntiva (CNF) es la que consume el método de resolución, y la disyuntiva (DNF) sale directo de una tabla de verdad.

## Los ladrillos: literales y cláusulas

Un **literal** es una variable ($p$) o su negación ($\neg p$). Una **cláusula** es una disyunción de literales, como $\neg p \lor q \lor \neg r$. Una conjunción de literales es la pieza análoga de la DNF.

## DNF y CNF

> [!tip] Las dos formas normales
> **DNF** (disyuntiva): $B_1 \lor \dots \lor B_k$, con cada $B_i$ una conjunción de literales.
> **CNF** (conjuntiva): $C_1 \land \dots \land C_k$, con cada $C_i$ una cláusula (disyunción de literales).

Ejemplos: $(p \land q) \lor (\neg p \land r \land s)$ está en DNF; $(p \lor \neg q) \land (\neg p \lor \neg r \lor s) \land (\neg r \lor s)$ está en CNF. Una cláusula suelta, o un literal suelto, está en ambas formas a la vez.

## Obtener la DNF desde la tabla de verdad

Se toma cada fila donde la fórmula vale $1$ y se escribe la conjunción de literales que describe exactamente esa valuación ($p$ si vale $1$, $\neg p$ si vale $0$). La DNF es la disyunción de todas esas conjunciones: es verdadera justo en las valuaciones elegidas. Esto prueba que **toda fórmula es equivalente a una en DNF** (si nunca vale $1$ es una contradicción, como $p \land \neg p$).

## Obtener la CNF: De Morgan sobre las filas falsas

Se aplica el mismo truco a las filas donde la fórmula vale $0$, obteniendo una DNF de $\neg\varphi$, y se niega con De Morgan.

Para $\varphi = (p \land q) \to (r \land \neg q)$, la fórmula solo vale $0$ en $(p, q, r) = (1, 1, 0)$ y $(1, 1, 1)$. Entonces $\neg\varphi \equiv (p \land q \land \neg r) \lor (p \land q \land r)$ y

$$\varphi \equiv (\neg p \lor \neg q \lor r) \land (\neg p \lor \neg q \lor \neg r).$$

Cada cláusula descarta exactamente una valuación falsa. (Se puede simplificar a $\neg p \lor \neg q$.) La DNF de la misma fórmula usa las seis filas verdaderas y es bastante más larga.

## Toda fórmula tiene una CNF equivalente

Otra forma de verlo, útil por su método: se parte de una DNF $B_0 \lor \dots \lor B_n$ y se prueba por inducción sobre el número de disyunciones que es equivalente a una CNF.

- **Base:** sin disyunciones queda una conjunción de literales $l_1 \land \dots \land l_k$, que ya es CNF (cada literal es una cláusula).
- **Paso:** por hipótesis, $B_0 \lor \dots \lor B_{n-1} \equiv \psi = C_1 \land \dots \land C_m$ (en CNF). Si $B_n = l_1 \land \dots \land l_k$, la distributividad de $\lor$ sobre $\land$ da
$$\psi \lor B_n \equiv \bigwedge_{i=1}^{m}\bigwedge_{j=1}^{k}(C_i \lor l_j),$$
y cada $C_i \lor l_j$ sigue siendo una cláusula.

> [!warning] El costo de convertir
> Distribuir puede hacer crecer la fórmula de forma exponencial. Las formas normales existen para todo, pero no siempre son cortas.

## Preguntas de repaso

> [!question]- ¿Por qué la DNF de una tabla de verdad usa las filas verdaderas y la CNF las falsas?
> Cada conjunción de la DNF "enciende" una fila verdadera. Cada cláusula de la CNF "apaga" una fila falsa (es falsa solo en esa valuación), y la conjunción de todas es verdadera solo en las filas no apagadas.

> [!question]- ¿Cuál es la DNF de una contradicción y la CNF de una tautología?
> La contradicción no tiene filas verdaderas, así que su DNF es una disyunción vacía (se escribe, por ejemplo, $p \land \neg p$). La tautología no tiene filas falsas: su CNF es una conjunción vacía, representable por $p \lor \neg p$.

> [!question]- ¿Por qué la inducción para la CNF es sobre el número de disyunciones de la DNF?
> Porque quitar la última conjunción deja una DNF más pequeña, a la que se aplica la hipótesis de inducción, y solo hay que distribuir la conjunción que se quitó.
