---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Álgebra de conjuntos y cardinalidad]]"
  - "[[07 - Aplicaciones a encuestas]]"
---

# Ejercicios de prueba de conjuntos

Preguntas de la guía sobre conjuntos, álgebra de conjuntos y cardinalidad. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Subconjunto propio
Sea $I = \{2n + 1 \mid n \in \mathbb{Z}\}$ y $J = \{m^2 \mid m \in I\}$. Demuestre que $J \subsetneq I$.

> [!example]- Solución
> $I$ es el conjunto de los enteros impares. Si $m \in I$, entonces $m$ es impar, $m = 2n + 1$, y $m^2 = 4n^2 + 4n + 1 = 2(2n^2 + 2n) + 1$, que es impar, luego $m^2 \in I$. Así $J \subseteq I$.
> Además $J \neq I$: el $3 \in I$, pero $3$ no es cuadrado de ningún entero impar ($3 \neq m^2$ para todo $m \in \mathbb{Z}$). Por lo tanto $J \subsetneq I$.

### 2. Igualdad con diferencia
Emplee el álgebra de conjuntos para probar que $(A \setminus C) \cup (B \setminus C) = (A \cup B) \setminus C$.

> [!example]- Solución
> $(A \setminus C) \cup (B \setminus C) = (A \cap C^{c}) \cup (B \cap C^{c}) = (A \cup B) \cap C^{c} = (A \cup B) \setminus C$.

### 3. Distributividad con diferencia simétrica
Recuerde que $A \triangle B = (A \setminus B) \cup (B \setminus A)$. Pruebe que $A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C)$.

> [!example]- Solución
> El lado izquierdo es $A \cap [(B \setminus C) \cup (C \setminus B)] = (A \cap B \setminus C) \cup (A \cap C \setminus B)$.
> El lado derecho es $[(A \cap B) \setminus (A \cap C)] \cup [(A \cap C) \setminus (A \cap B)] = [A \cap B \cap (A \cap C)^{c}] \cup [A \cap C \cap (A \cap B)^{c}] = (A \cap B \cap C^{c}) \cup (A \cap C \cap B^{c})$, que coincide con el izquierdo.

### 4. Encuesta de dos marcas
En un estudio de $120$ consumidores, $80$ compran la marca $A$, $68$ la marca $B$ y $42$ ambas. Determine cuántos compran: a) al menos una; b) solo una; c) únicamente $A$; d) ninguna.

> [!example]- Solución
> a) $n(A \cup B) = 80 + 68 - 42 = 106$. b) Solo una: $(80 - 42) + (68 - 42) = 38 + 26 = 64$. c) Únicamente $A$: $80 - 42 = 38$. d) Ninguna: $120 - 106 = 14$.

### 5. Encuesta de un club
De $200$ miembros, $100$ irán a los Juegos de Verano, $60$ a los de Invierno y $40$ a ambos. ¿Cuántos irán: a) al menos a uno; b) solo a uno; c) únicamente a los de verano; d) a ninguno?

> [!example]- Solución
> a) $100 + 60 - 40 = 120$. b) $(100 - 40) + (60 - 40) = 60 + 20 = 80$. c) $100 - 40 = 60$. d) $200 - 120 = 80$.

### 6. Encuesta de tres cursos
De $1200$ estudiantes, $582$ tomaron física, $627$ filosofía y $543$ matemática; $217$ física y filosofía, $307$ física y matemática, $250$ matemática y filosofía, y $122$ los tres. ¿Cuántos no tomaron ninguno?

> [!example]- Solución
> Por inclusión-exclusión:
> $$n(F \cup Fil \cup M) = 582 + 627 + 543 - 217 - 307 - 250 + 122 = 1752 - 774 + 122 = 1100.$$
> Ninguno: $1200 - 1100 = 100$.

## Preguntas de repaso

> [!question]- ¿Qué distingue "al menos una marca" de "solo una marca" en una encuesta de dos conjuntos?
> "Al menos una" es $n(A \cup B) = n(A) + n(B) - n(A \cap B)$. "Solo una" es $(n(A) - n(A \cap B)) + (n(B) - n(A \cap B))$: se excluye a los que compran ambas.

> [!question]- En el ejercicio 1, ¿cómo se prueba que $J \neq I$?
> Exhibiendo un elemento de $I$ que no está en $J$: $3$ es impar pero no es un cuadrado. Basta un elemento para romper la igualdad.

> [!question]- En la encuesta de tres cursos, ¿por qué se suma $122$ al final?
> Porque es la triple intersección: al restar las tres intersecciones dobles se la restó tres veces, así que se suma una vez para dejarla contada exactamente una vez.
