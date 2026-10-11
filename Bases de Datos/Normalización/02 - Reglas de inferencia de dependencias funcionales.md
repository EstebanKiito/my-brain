---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/complemento]
prerrequisitos: ["[[01 - Dependencias funcionales|Dependencias funcionales]]"]
---
# Reglas de inferencia de dependencias funcionales

A partir de unas dependencias se pueden **deducir** otras (transitividad, descomposición, unión…). Con estas reglas se encuentran todas las dependencias de una tabla y sus llaves candidatas.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 7: Dependencias y Formas Normales")
> | # | Regla | Ejemplo |
> |---|---|---|
> | 1 | **Transitividad:** si X → Y y Y → Z, entonces X → Z | A,B → C y C → D ⇒ A,B → D |
> | 2 | **Descomposición:** si X → Y y Z ⊆ Y, entonces X → Z | A,B → C,D ⇒ A,B → D |
> | 3 | **Trivial:** X → Y es trivial si Y ⊆ X | A,B → A |
> | 4 | **Unión:** si X → Y y X → Z, entonces X → Y, Z | A → B y A → D ⇒ A → B,D |
> | 5 | **Aumentación:** si X → Y, para todo Z: X, Z → Y, Z | A → B ⇒ A,C → B,C |
> | 6 | **Llave:** si X → Y, y Y contiene todos los atributos de la relación que no están en X, entonces X es (candidato a) llave | R(A,B,C,D,E), A,B → C,D,E ⇒ A,B → A,B,C,D,E, así que A,B es llave |
>
> (X, Y, Z son conjuntos de atributos.) Estas reglas se demuestran directamente con la definición de dependencia funcional.

> [!example] Ejemplo extra — ejemplo de la clase
> Averiguar todas las dependencias de R(a, b, c) si a → b y b → a, c.
>
> Por transitividad (1) se infiere **a → a, c**; con la unión (4), **a → b, c**. Como `a` determina todo el resto, **a es llave**. También `b → a, c`, así que b también es llave.
>
> **Demostración** de a → b, c: sean $t_1, t_2$ con $t_1[a] = t_2[a]$. Como a → b, entonces $t_1[b] = t_2[b]$. Como b → a, c, entonces $t_1[a,c] = t_2[a,c]$. Finalmente $t_1[b,c] = t_2[b,c]$.

> [!example] Ejemplo extra — ejercicio de la clase
> `Toma(alumno, carrera, ramo, sala, hora)` con:
> - alumno → carrera
> - carrera, ramo → sala
> - ramo → hora
>
> Por aumentación: alumno, ramo → carrera, ramo. Con carrera, ramo → sala se obtiene alumno, ramo → sala. Con ramo → hora y la unión:
> **alumno, ramo → carrera, sala, hora**. Por la regla 6, **(alumno, ramo) es llave**.

> [!tip] Complemento — clausura de atributos (algoritmo estándar, Garcia-Molina/Ullman cap. 3)
> Para saber si X es superllave, se calcula $X^+$ (todo lo que X determina):
> 1. Empezar con $X^+ = X$.
> 2. Mientras exista una dependencia $A \to B$ con $A \subseteq X^+$, agregar B a $X^+$.
> 3. X es superllave si $X^+$ contiene todos los atributos.
>
> En `Toma`: $\{alumno, ramo\}^+$ = {alumno, ramo} → + carrera → + sala → + hora = todos los atributos. ✔

## Preguntas de repaso

1. Si A → B y B → C, ¿qué puedes deducir? ¿Con qué regla?
> [!question]- Respuesta
> A → C, por transitividad.

2. ¿Qué es una dependencia trivial? Da un ejemplo.
> [!question]- Respuesta
> Una X → Y donde Y ⊆ X, que se cumple siempre. Por ejemplo, A,B → A.

3. ¿Cuál es la llave de `Toma(alumno, carrera, ramo, sala, hora)` y por qué?
> [!question]- Respuesta
> (alumno, ramo), porque con las dependencias dadas determina carrera, sala y hora, es decir, todo el resto.

4. ¿Cómo usas la clausura $X^+$ para saber si X es superllave?
> [!question]- Respuesta
> Agregas a $X^+$ el lado derecho de toda dependencia cuyo lado izquierdo ya esté en $X^+$, hasta que no crezca más. Si al final contiene todos los atributos, X es superllave.
