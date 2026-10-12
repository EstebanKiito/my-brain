---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/complemento]
prerrequisitos: ["[[06 - Forma normal de Boyce-Codd|Forma normal de Boyce-Codd]]", "[[02 - Reglas de inferencia de dependencias funcionales|Reglas de inferencia de dependencias funcionales]]"]
---
# Descomposición en BCNF y 3NF

Los algoritmos para llevar una tabla a BCNF o a 3NF dividiéndola en tablas más pequeñas **sin perder información**. La 3NF además preserva todas las dependencias.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 7: Dependencias y Formas Normales")
> **Algoritmo BCNF.** Input: el esquema $R(A_1,\dots,A_n)$ y sus dependencias funcionales.
> 1. Tomar una dependencia X → Y donde X **no** es superllave y descomponer en dos tablas: $R_1(X, Y)$ y $R_2(\{A_1,\dots,A_n\} - Y)$.
> 2. Repetir con las tablas que aún no están en BCNF.
>
> Optimización: elegir el Y más grande posible, por ejemplo usando la clausura de X.
>
> Ejemplo: `S(a,b,c,d,e,f)` con a,b → c,e, que rompe BCNF ⇒ `S1(a,b,c,e)` y `S2(a,b,d,f)`.

> [!example] Ejemplo extra — R(a, b, c, d) con a → b y b → c (slides "Clase 7")
> Se deduce a → c y a → b, c. La llave es (a, d).
> | Descomposición 1 (con a → b, c) | Descomposición 2 (con a → b) |
> |---|---|
> | R1(a,b,c) + R2(a,d) | R1'(a,b) + R2'(a,c,d) |
> | R1 rompe BCNF por b → c ⇒ R11(b,c), R12(a,b) | R2' rompe BCNF por a → c ⇒ R21'(a,c), R22'(a,d) |
> | **Resultado:** R11(b,c), R12(a,b), R2(a,d) | **Resultado:** R1'(a,b), R21'(a,c), R22'(a,d) |
>
> En ambas, el join natural reconstruye R. Pero la segunda **perdió** b → c: ninguna tabla la contiene.

> [!tip] Complemento — descomposición sin pérdida (slides "Clase 7")
> R(A, B, C) descompuesta en R1(A, B) y R2(A, C) es **sin pérdida de información** si, para toda instancia, $\pi_{A,B}(R) \bowtie \pi_{A,C}(R) = R$.
>
> **Teorema:** si X → Y (con X, Y, Z disjuntos), la descomposición de R(X, Y, Z) en R1(X, Y) y R2(X, Z) es sin pérdida. Por eso el algoritmo BCNF **nunca pierde información**.
>
> **Problema de BCNF:** puede perder dependencias. En R(a,b,c,d,e) con DF1: a,b,c → d,e y DF2: d,e → b (llaves: abc y deac), DF2 viola BCNF. Al descomponer en R1(d,e,b) y R2(a,c,d,e), ninguna tabla permite validar DF1: hay que hacer el join. **Pero el esquema original ya está en 3NF**, porque b es parte de la llave abc.

> [!tip] Complemento — algoritmo 3NF (idea, slides "Clase 7")
> Input: el esquema R y sus dependencias en formato estandarizado, sin dependencias inútiles (lado izquierdo minimal, sin dependencias deducibles de otras).
> 1. Para cada dependencia X → Y, crear una tabla con esquema X ∪ Y. Esto **asegura las dependencias**: cada una queda en su tabla.
> 2. Si ninguna tabla contiene una llave de R, agregar una. Esto **asegura que no se pierda información**.
>
> Ejemplo de la clase (avalúos): NombreComuna, Región → Tasa; RUT → Nombre, Apellido; Tasa, m2 → Avalúo; NombreComuna, Región, Rol → RUT, M2. Resultan cuatro tablas, una por dependencia.
>
> **Ejemplo MAL(cine, película, director, dirección, teléfono, horario, precio)**, con cine → dirección, teléfono; película → director; cine, película, horario → precio. Se divide en `Cines(cine, dirección, teléfono)`, `Películas(película, director)` y `Funciones(cine, película, horario, precio)`. No hay anomalías, no se pierden dependencias ni información.

## Preguntas de repaso

1. Describe un paso del algoritmo de descomposición BCNF.
> [!question]- Respuesta
> Se elige una dependencia X → Y con X no superllave y se divide R en R1(X ∪ Y) y R2(todos los atributos menos Y). Se repite hasta que todas las tablas estén en BCNF.

2. ¿Por qué la descomposición BCNF es sin pérdida de información?
> [!question]- Respuesta
> Porque se hace a partir de una dependencia X → Y, y el teorema garantiza que R(X,Y,Z) = R1(X,Y) ⋈ R2(X,Z) cuando X → Y.

3. ¿Qué desventaja puede tener BCNF frente a 3NF?
> [!question]- Respuesta
> Puede no preservar dependencias: alguna dependencia queda repartida entre tablas y solo se puede validar haciendo un join.

4. Descompón MAL(cine, película, director, dirección, teléfono, horario, precio).
> [!question]- Respuesta
> Cines(cine, dirección, teléfono), Películas(película, director) y Funciones(cine, película, horario, precio).
