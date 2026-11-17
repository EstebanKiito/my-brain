---
ramo: "Matemáticas Discretas"
tema: "Lógica proposicional y equivalencia"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Proposiciones y sintaxis de las fórmulas proposicionales]]"
  - "[[06 - Inducción estructural]]"
---

# Largo y variables de una fórmula por inducción estructural

Dado que $L(P)$ se define por reglas, las medidas sobre fórmulas (cuántos símbolos tiene, cuántas variables aparecen) se definen **recursivamente**, una cláusula por regla. Y las relaciones entre ellas se demuestran siguiendo la misma estructura. Es el primer uso concreto de [[06 - Inducción estructural]] en lógica.

## Dos funciones recursivas

**Largo** $\mathrm{largo}(\varphi)$: cantidad de símbolos (variables, conectivos y paréntesis).

- $\mathrm{largo}(p) = 1$ para $p \in P$.
- $\mathrm{largo}((\neg\varphi)) = 3 + \mathrm{largo}(\varphi)$: se suman el $\neg$ y los dos paréntesis.
- $\mathrm{largo}((\varphi \star \psi)) = 3 + \mathrm{largo}(\varphi) + \mathrm{largo}(\psi)$.

**Variables** $\mathrm{var}(\varphi)$: número de **ocurrencias** de variables (se cuentan las repeticiones).

- $\mathrm{var}(p) = 1$.
- $\mathrm{var}((\neg\varphi)) = \mathrm{var}(\varphi)$.
- $\mathrm{var}((\varphi \star \psi)) = \mathrm{var}(\varphi) + \mathrm{var}(\psi)$.

Ejemplo con $\varphi = ((\neg p) \wedge q)$: $\mathrm{largo}((\neg p)) = 3 + 1 = 4$ y $\mathrm{largo}(\varphi) = 3 + 4 + 1 = 8$, mientras que $\mathrm{var}(\varphi) = 2$.

## Propiedad: sin negaciones, el largo es cuadrático en las variables

> [!tip] Enunciado
> Si $\varphi$ no contiene el símbolo $\neg$, entonces $\mathrm{largo}(\varphi) \le 4 \cdot \mathrm{var}(\varphi)^2$.

Se demuestra por inducción estructural sobre las fórmulas sin $\neg$.

- **Base.** $\varphi = p$: $\mathrm{largo}(p) = 1 \le 4 = 4 \cdot 1^2$.
- **HI.** $\mathrm{largo}(\varphi) \le 4\,\mathrm{var}(\varphi)^2$ y $\mathrm{largo}(\psi) \le 4\,\mathrm{var}(\psi)^2$.
- **Paso.** Sea $v_1 = \mathrm{var}(\varphi)$ y $v_2 = \mathrm{var}(\psi)$. Entonces
$$\mathrm{largo}((\varphi \star \psi)) = 3 + \mathrm{largo}(\varphi) + \mathrm{largo}(\psi) \le 3 + 4v_1^2 + 4v_2^2.$$
Como $4(v_1 + v_2)^2 = 4v_1^2 + 4v_2^2 + 8v_1v_2$, basta que $3 \le 8v_1v_2$, y eso vale porque toda fórmula tiene al menos una variable ($v_1, v_2 \ge 1$ implica $8v_1v_2 \ge 8$). Luego $\mathrm{largo}((\varphi\star\psi)) \le 4(v_1+v_2)^2 = 4\,\mathrm{var}((\varphi \star \psi))^2$.

Una comprobación numérica con $\varphi = (p \wedge q)$: $\mathrm{largo} = 5 \le 16 = 4 \cdot 2^2$.

## ¿Y con negaciones?

> [!warning] La propiedad deja de valer si se permite $\neg$
> La regla de la negación suma $3$ al largo sin agregar variables. Con $\neg\neg\cdots\neg p$ ($k$ negaciones) el largo es $1 + 3k$ y $\mathrm{var} = 1$: la cota $4$ se rompe para $k \ge 2$. En el paso inductivo la negación es justo el caso que no se puede cerrar. Una salida es prohibir negaciones sucesivas, lo que se justifica más adelante con la doble negación ($\neg\neg\varphi \equiv \varphi$, ver [[05 - Leyes de equivalencia y cadenas de demostración]]).

## Preguntas de repaso

> [!question]- ¿Por qué hace falta un solo caso base y dos casos inductivos en estas definiciones?
> Porque $L(P)$ tiene una regla base (las variables) y dos reglas que construyen fórmulas nuevas (negación y conectivo binario). Cada regla exige una cláusula en la función recursiva y un caso en la demostración; sin $\neg$, el caso de la negación desaparece.

> [!question]- ¿Cuál es el $\mathrm{largo}$ de $((p \vee q) \to (\neg r))$?
> $\mathrm{largo}((p\vee q)) = 5$ y $\mathrm{largo}((\neg r)) = 4$, así que el total es $3 + 5 + 4 = 12$.

> [!question]- ¿Dónde se usó que $\mathrm{var}(\theta) \ge 1$?
> En el paso: para asegurar $3 \le 8\,\mathrm{var}(\varphi)\,\mathrm{var}(\psi)$, que permite pasar de la cota con $3$ de sobra a la cota $4(v_1+v_2)^2$.
