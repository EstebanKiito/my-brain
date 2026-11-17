---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Consecuencia lógica en predicados y reglas de inferencia]]"
---

# Ejercicios de ayudantías de lógica de predicados

Cuatro ejercicios de ayudantías: formalizar enunciados, justificar cuándo una conclusión es consecuencia y refutar por resolución. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. El cahuín: formalizar afirmaciones
Sobre el dominio de personas, $R(x)$ significa «$x$ conoce el cahuín», $C(x, y)$ «$x$ le contó el cahuín a $y$» y $=$ es la igualdad. Escriba en lógica de predicados: (a) si una persona conoce el cahuín y se lo contó a otra, la otra lo conoce; (b) nadie conoce el cahuín y se lo contó a sí mismo; (c) existe un «cahuinero original»: alguien que lo conoce y a quien nadie se lo contó; (d) no existen triángulos de cahuineros: tres personas distintas que se lo contaron circularmente.

> [!example]- Solución
> (a) $\forall x\,\forall y\,\big((R(x) \wedge C(x, y)) \to R(y)\big)$: se cuantifica sobre todo par y el condicional ignora los pares donde el antecedente falla.
>
> (b) $\neg\exists x\,(R(x) \wedge C(x, x))$.
>
> (c) $\exists x\,\big(R(x) \wedge \forall y\,\neg C(y, x)\big)$: el $\forall y$ sólo afecta a $C(y, x)$, no a $R(x)$.
>
> (d) $\neg\exists x\,\exists y\,\exists z\,\big(x \ne y \wedge y \ne z \wedge z \ne x \wedge C(x, y) \wedge C(y, z) \wedge C(z, x)\big)$. Las desigualdades son necesarias: sin ellas bastaría $x = y = z$ con $C(x, x)$.

### 2. Consecuencia y refutación
Sean $\Sigma$ un conjunto de oraciones y $\varphi$ una oración. Demuestre que $\Sigma \models \varphi$ si y sólo si $\Sigma \cup \{\neg\varphi\}$ es inconsistente.

> [!example]- Solución
> ($\Rightarrow$) Por contrapositivo: si $\Sigma \cup \{\neg\varphi\}$ fuera satisfacible, existiría $I$ con $I \models \Sigma$ e $I \models \neg\varphi$, es decir $I \not\models \varphi$; eso contradice $\Sigma \models \varphi$. ($\Leftarrow$) Sea $I \models \Sigma$. Como ninguna interpretación satisface $\Sigma \cup \{\neg\varphi\}$, no puede ser $I \models \neg\varphi$; luego $I \models \varphi$. Esta equivalencia justifica probar consecuencias por resolución.

### 3. Simétrica y transitiva implican refleja (con serialidad)
Sea $\Sigma = \{\forall x\,\exists y\,R(x, y),\ \forall x\,\forall y\,(R(x, y) \to R(y, x)),\ \forall x\,\forall y\,\forall z\,((R(x, y) \wedge R(y, z)) \to R(x, z))\}$ y $\varphi = \forall x\,R(x, x)$. Demuestre que $\Sigma \models \varphi$.

> [!example]- Solución
> Por el ejercicio anterior se refuta $\Sigma \cup \{\neg\varphi\}$, con $\neg\varphi \equiv \exists x\,\neg R(x, x)$. Se hacen primero las especificaciones existenciales, con nombres nuevos:
> 1. $\neg R(a, a)$ (existencial sobre $\neg\varphi$).
> 2. $R(a, b)$ (universal en $a$ y existencial con $b$ nuevo, sobre $\forall x\,\exists y\,R(x, y)$).
> 3. $\neg R(a, b) \vee R(b, a)$ (universal de la simetría).
> 4. $R(b, a)$ (resolución de 2 y 3).
> 5. $\neg R(a, b) \vee \neg R(b, a) \vee R(a, a)$ (universal de la transitividad con $x = a$, $y = b$, $z = a$).
> 6. $R(a, a)$ (resolución de 2, 4 y 5).
> 7. $\square$ (resolución de 1 y 6).
>
> Si se hubiese instanciado el $\exists y$ antes de conocer $a$ no habría libertad para elegir; por eso las existenciales van primero y las universales, que admiten cualquier nombre ya introducido, después.

### 4. Números primos: no hay constantes
Con dominio $\mathbb{N}$, $\le$, $=$ y $P(n)$ = «$n$ es primo», escriba: «Para todo par de primos distintos de $2$ y $3$ existe un natural entre ellos que no es primo».

> [!example]- Solución
> No hay constantes, así que se definen. $\text{Entre}(x, y, z) := x \le y \wedge y \le z \wedge y \ne x \wedge y \ne z$. Sucesor: $S(x, y) := x \le y \wedge x \ne y \wedge \neg\exists z\,\text{Entre}(x, z, y)$. Luego $C_0(x) := \forall y\,(x \le y)$, $C_1(x) := \exists y\,(C_0(y) \wedge S(y, x))$, $C_2(x) := \exists y\,(C_1(y) \wedge S(y, x))$ y $C_3$ análogo. Con $Q(x) := P(x) \wedge \neg C_2(x) \wedge \neg C_3(x)$:
> $$\forall x\,\forall y\,\Big(\big(Q(x) \wedge Q(y) \wedge x \ne y\big) \to \exists z\,\big((\text{Entre}(x, z, y) \vee \text{Entre}(y, z, x)) \wedge \neg P(z)\big)\Big).$$
> Hay que exigir $x \ne y$ y considerar ambos órdenes: con $x = 7$, $y = 5$ no existe $z$ con $7 \le z \le 5$, y una fórmula que sólo mire $\text{Entre}(x, z, y)$ sería falsa.

## Preguntas de repaso

> [!question]- ¿Por qué en (d) del cahuín hacen falta las desigualdades entre las tres personas?
> Porque sin ellas una persona que se contó el cahuín a sí misma ($x = y = z$) formaría un «triángulo» degenerado. Las desigualdades fuerzan tres personas distintas.

> [!question]- ¿Por qué se hacen las especificaciones existenciales antes que las universales?
> La existencial exige un nombre nuevo, mientras que la universal acepta cualquier nombre ya presente. Instanciando primero las existenciales se tiene un conjunto de nombres sobre los cuales instanciar libremente las universales.

> [!question]- ¿Qué error comete formalizar «para todo par de primos» omitiendo $x \ne y$ y el orden de $x$ e $y$?
> Para $x = y$ o para $x > y$ no existe $z$ «entre» en el sentido $x \le z \le y$, y la conclusión sería falsa aunque el enunciado sea cierto.
