---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Consecuencia lógica e inconsistencia]]"
  - "[[07 - Demostraciones por resolución y completitud]]"
---

# Ejercicios de prueba de satisfacibilidad y resolución

En las interrogaciones y exámenes, las preguntas de este tema son de tres tipos: **demostrar propiedades de la consecuencia lógica** (con las definiciones, valuación por valuación, y no con tablas de verdad genéricas), **dar contraejemplos** a afirmaciones tipo verdadero-falso y **modelar un problema** como una fórmula satisfacible. Las preguntas de resolución sobre predicados aparecen con la lógica de predicados. La pauta puntúa partir de una valuación arbitraria, usar la definición exacta y cerrar la conclusión.

## Ejercicios

### 1. Consecuencia e inconsistencia (I1, 2018-1)
Demuestre que $\Sigma \models \alpha$ si y solo si $\Sigma \cup \{\neg\alpha\}$ es inconsistente.

> [!example]- Solución
> ($\Rightarrow$) Sea $v$ una valuación. Si $v$ falsifica alguna fórmula de $\Sigma$, no satisface $\Sigma \cup \{\neg\alpha\}$. Si satisface $\Sigma$, por hipótesis $v(\alpha) = 1$ y $v(\neg\alpha) = 0$. En ambos casos $v$ no satisface el conjunto ampliado.
>
> ($\Leftarrow$) Sea $v$ con $v(\Sigma) = 1$. Como $\Sigma \cup \{\neg\alpha\}$ es inconsistente, $v$ no lo satisface, así que $v(\neg\alpha) = 0$, es decir $v(\alpha) = 1$.

### 2. Inconsistencia y cláusula vacía (examen, 2015-2)
Demuestre que $\Sigma$ es inconsistente si y solo si $\Sigma \models \square$.

> [!example]- Solución
> ($\Rightarrow$) Si $\Sigma$ es inconsistente, ninguna valuación lo satisface, y la condición de $\Sigma \models \square$ se cumple vacuamente. ($\Leftarrow$) Si $\Sigma$ fuera satisfacible por $\sigma$, de $\Sigma \models \square$ saldría $\sigma(\square) = 1$; pero $\square$ es una contradicción, absurdo.

### 3. Implicación y tautologías (I1, 2021-2)
Sea $\Sigma$ un conjunto de fórmulas. (a) Si $\Sigma \models \varphi \to \psi$, pruebe que $\Sigma \cup \{\varphi\} \models \psi$. (b) Si $\varphi$ es tautología y $\Sigma \cup \{\varphi\} \models \psi$, pruebe que $\Sigma \models \psi$.

> [!example]- Solución
> (a) Sea $\sigma$ que satisface $\Sigma \cup \{\varphi\}$. Entonces $\sigma(\Sigma) = 1$, así que $\sigma(\varphi \to \psi) = 1$; además $\sigma(\varphi) = 1$. Por la tabla de $\to$, $\sigma(\psi) = 1$.
>
> (b) Sea $\sigma$ con $\sigma(\Sigma) = 1$. Como $\varphi$ es tautología, $\sigma(\varphi) = 1$, y por eso $\sigma$ satisface $\Sigma \cup \{\varphi\}$. La hipótesis da $\sigma(\psi) = 1$.

### 4. Consecuencia de uniones (I1, 2025-2)
Responda verdadero o falso, con demostración o contraejemplo: (a) si $\Sigma \models \varphi$ o $\Sigma' \models \varphi$, entonces $\Sigma \cup \Sigma' \models \varphi$; (b) si $\Sigma \cup \Sigma' \models \varphi$, entonces $\Sigma \models \varphi$ o $\Sigma' \models \varphi$.

> [!example]- Solución
> (a) **Verdadero** (monotonía). Si, por ejemplo, $\Sigma \models \varphi$ y $\sigma$ satisface $\Sigma \cup \Sigma'$, entonces satisface $\Sigma \subseteq \Sigma \cup \Sigma'$ y por tanto $\sigma(\varphi) = 1$.
>
> (b) **Falso.** Con $\Sigma = \{p\}$, $\Sigma' = \{q\}$ y $\varphi = p \land q$: $\{p, q\} \models p \land q$, pero $\{p\} \not\models p \land q$ (con $p = 1, q = 0$) y $\{q\} \not\models p \land q$ (con $p = 0, q = 1$).

### 5. Consecuencia como equivalencia con la conjunción (examen, 2020-1)
Demuestre que $\alpha \models \beta$ si y solo si $\alpha \equiv \alpha \land \beta$.

> [!example]- Solución
> ($\Rightarrow$) Sea $\sigma$. Si $\sigma(\alpha) = 1$, la consecuencia da $\sigma(\beta) = 1$ y entonces $\sigma(\alpha \land \beta) = 1$. Si $\sigma(\alpha) = 0$, también $\sigma(\alpha \land \beta) = 0$. Coinciden en toda valuación.
>
> ($\Leftarrow$) Sea $\sigma(\alpha) = 1$. Como $\alpha \equiv \alpha \land \beta$, $\sigma(\alpha \land \beta) = 1$, luego $\sigma(\beta) = 1$.

### 6. Consecuencia por contradicción (I1, 2026-1)
Demuestre que $\big[(x_0 \lor x_1 \lor x_2 \lor x_3 \lor x_4) \to (x_5 \land x_6 \land x_7 \land x_8 \land x_9)\big] \models \neg x_2 \lor x_8$.

> [!example]- Solución
> Con diez variables, la tabla de verdad tiene $1024$ filas, así que se razona por contradicción. Si no fuera consecuencia, existiría $\sigma$ que hace verdadera la premisa y falsa $\neg x_2 \lor x_8$; esto exige $\sigma(x_2) = 1$ y $\sigma(x_8) = 0$. Pero con $x_2 = 1$ el antecedente vale $1$, y con $x_8 = 0$ el consecuente vale $0$, de modo que la premisa vale $1 \to 0 = 0$. Contradicción. (Se comprobó también revisando las $1024$ valuaciones.)

### 7. Consecuencia débil (I1, 2019-1)
Se define $\Sigma \vdash_d \varphi$ ("consecuencia débil") si toda valuación que haga verdadera **alguna** fórmula de $\Sigma$ hace verdadera $\varphi$. Responda con demostración o contraejemplo: (a) ¿si $\{\varphi_1, \dots, \varphi_n, \psi\} \vdash_d \varphi$, entonces $\{\varphi_1, \dots, \varphi_n\} \vdash_d \varphi$? (b) ¿$\{\varphi_1, \dots, \varphi_n\} \vdash_d \varphi$ si y solo si $\{\varphi_1, \dots, \varphi_n, \neg\varphi\}$ es insatisfacible?

> [!example]- Solución
> (a) **Verdadero.** Si $\sigma$ hace verdadera algún $\varphi_i$, también hace verdadera alguna fórmula del conjunto ampliado, luego satisface $\varphi$.
>
> (b) **Falso.** Con $\Sigma = \{p, \neg p\}$ y $\varphi = p \land \neg p$, el conjunto $\{p, \neg p, \neg(p \land \neg p)\}$ es insatisfacible (ya $\{p, \neg p\}$ lo es). Pero $\Sigma \not\vdash_d \varphi$: con $p = 1$ se hace verdadera una fórmula de $\Sigma$ y $\varphi$ vale $0$.

### 8. Conjuntos redundantes y consecuencias (I1, 2022-1)
Sea $\Sigma$ redundante, con $\alpha \in \Sigma$ tal que $\Sigma \setminus \{\alpha\} \models \alpha$. Demuestre que, para toda fórmula $\beta$, $\Sigma \models \beta$ si y solo si $\Sigma \setminus \{\alpha\} \models \beta$.

> [!example]- Solución
> ($\Leftarrow$) Es monotonía: un conjunto más grande conserva las consecuencias. ($\Rightarrow$) Sea $\sigma$ que satisface $\Sigma \setminus \{\alpha\}$. Por hipótesis $\sigma(\alpha) = 1$, así que $\sigma$ satisface $\Sigma$ y, como $\Sigma \models \beta$, $\sigma(\beta) = 1$. Quitar una fórmula redundante no cambia qué se deduce.

### 9. Cláusulas conjuntivas (examen, 2022-1)
Una *cláusula conjuntiva* es $\alpha = a_1 \land \dots \land a_n$ con cada $a_i$ literal. Si $\alpha = a_1 \land \dots \land a_n$ y $\beta = b_1 \land \dots \land b_m$ son satisfacibles, demuestre que $\alpha \models \beta$ si y solo si $\{b_1, \dots, b_m\} \subseteq \{a_1, \dots, a_n\}$.

> [!example]- Solución
> ($\Leftarrow$) Si cada $b_j$ es algún $a_i$, toda valuación que hace verdaderos todos los $a_i$ hace verdaderos todos los $b_j$.
>
> ($\Rightarrow$) Por contrapositivo: sea $b = b_j$ un literal que no está entre los $a_i$. Como $\alpha$ es satisfacible, no contiene un literal y su complemento. Si la variable de $b$ no aparece en $\alpha$, se toma una valuación que satisface $\alpha$ y se fija esa variable para falsificar $b$. Si aparece, lo hace como $\bar b$ y toda valuación que satisface $\alpha$ falsifica $b$. En ambos casos hay una valuación que satisface $\alpha$ y no $\beta$, es decir $\alpha \not\models \beta$. (Se comprobó la equivalencia revisando muchos casos con cuatro variables.)

### 10. Modelar la distribución de animales en jaulas (I1, 2015-2)
Hay $n$ animales y $m$ jaulas, cada jaula admite a lo más tres animales y una lista $D$ de pares $(i, j)$ indica que $i$ depreda a $j$; un depredador no puede compartir jaula con su presa y todo animal debe estar enjaulado. Construya $\varphi$ satisfacible si y solo si existe una distribución válida.

> [!example]- Solución
> Variables $p_{ij}$: el animal $i$ está en la jaula $j$. Restricciones:
> - Todos enjaulados: $\varphi_1 = \bigwedge_i \bigvee_j p_{ij}$.
> - Una sola jaula por animal: $\varphi_2 = \bigwedge_i \bigwedge_{j \neq k}\neg(p_{ij} \land p_{ik})$.
> - Depredador y presa separados: $\varphi_3 = \bigwedge_{(i,k) \in D}\bigwedge_{j}\neg(p_{ij} \land p_{kj})$.
> - Capacidad tres: no hay cuatro animales distintos en la misma jaula, $\varphi_4 = \bigwedge_j \bigwedge_{i_1<i_2<i_3<i_4}\neg(p_{i_1 j} \land p_{i_2 j} \land p_{i_3 j} \land p_{i_4 j})$.
>
> $\varphi = \varphi_1 \land \varphi_2 \land \varphi_3 \land \varphi_4$. De una valuación que la satisface sale la distribución (cada animal tiene exactamente una jaula) y recíprocamente. Se contrastó con instancias chicas ($n = 3, 4$; $m = 1, 2$), comparando satisfacibilidad con el conteo directo de asignaciones.

## Preguntas de repaso

> [!question]- ¿Por qué en los ejercicios 3 y 5 se parte de una valuación arbitraria?
> Porque consecuencia y equivalencia hablan de **todas** las valuaciones. Se toma una cualquiera que cumpla la hipótesis y se deduce lo pedido, sin suponer nada más de ella.

> [!question]- ¿Qué técnica sirve para refutar una consecuencia lógica falsa (ejercicios 4 y 7)?
> Un contraejemplo: una valuación que hace verdaderas las premisas y falsa la conclusión, como $p = 1, q = 0$ para $\{p\} \not\models p \land q$.

> [!question]- ¿Por qué en el ejercicio 10 no basta con $\varphi_1$ y $\varphi_3$?
> Sin $\varphi_2$ un animal podría ocupar varias jaulas, y sin $\varphi_4$ se violaría la capacidad. La valuación satisfaría $\varphi$ pero no definiría una distribución válida.
