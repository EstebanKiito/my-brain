---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[05 - Tercera forma normal|Tercera forma normal]]", "[[03 - Superllaves, claves candidatas y clave primaria|Superllaves, claves candidatas y clave primaria]]"]
---
# Forma normal de Boyce-Codd

Una tabla está en **BCNF** si en **toda** dependencia funcional no trivial X → Y, X es una superllave. Es la forma normal que se busca en el curso: elimina las anomalías por dependencias funcionales.

## Forma normal de Boyce-Codd (BCNF)
Una relación está en BCNF si para toda dependencia funcional **no trivial** X → Y, X es una **superllave**.

Esto es más restrictivo que 3NF.

Ejemplo de relación que **no** está en BCNF:

| Curso | Profesor | Aula |
|---|---|---|
| CS101 | Dr. Smith | A101 |
| CS101 | Dr. Brown | A102 |

Dependencia funcional: Profesor → Aula, pero Profesor no es superllave.

Para llevarla a BCNF, se descompone la tabla:

Tabla 1:

| Curso | Profesor |
|---|---|
| CS101 | Dr. Smith |
| CS101 | Dr. Brown |

Tabla 2:

| Profesor | Aula |
|---|---|
| Dr. Smith | A101 |
| Dr. Brown | A102 |

> [!tip] Complemento — definición y cómo revisarla (slides "Clase 7")
> - **Causa de anomalías:** X → Y cuando X **no** es superllave. R está en BCNF si para toda dependencia **no trivial** X → Y, X es superllave. Un esquema está en BCNF si todas sus relaciones lo están.
> - **Truco:** basta mirar las dependencias. Las de la forma *llave → resto* están bien (ojo, puede haber varias llaves candidatas). Una de la forma *no-superllave → algo* rompe BCNF.
> - Ejemplo: `AlumnoTelefono(rut, teléfono, nombre, apellido)`, con única llave (rut, teléfono). La dependencia rut → nombre, apellido **rompe BCNF**, porque rut no es superllave.
> - En el ejemplo de arriba, la llave es (Curso, Profesor) y Profesor → Aula viola BCNF. Como Profesor es *parte* de la llave y Aula no es atributo de llave, también es una dependencia parcial: la tabla tampoco está en 2NF ni en 3NF. Un ejemplo de "3NF pero no BCNF" es el de R(a,b,c,d,e) en [[08 - Descomposición en BCNF y 3NF|Descomposición en BCNF y 3NF]].
>
> ```mermaid
> flowchart LR
>   A[1NF] --> B[2NF] --> C[3NF] --> D[BCNF]
> ```
> Cada forma incluye a las anteriores: toda tabla en BCNF está en 3NF, pero no al revés.

## Preguntas de repaso

1. ¿Cuándo está una relación en BCNF?
> [!question]- Respuesta
> Cuando, para toda dependencia funcional no trivial X → Y, X es superllave de la relación.

2. ¿Por qué la tabla (Curso, Profesor, Aula) no está en BCNF?
> [!question]- Respuesta
> Porque Profesor → Aula y Profesor no es superllave: un profesor puede aparecer en varios cursos, y su aula se repetiría.

3. ¿Está `AlumnoTelefono(rut, teléfono, nombre, apellido)` en BCNF?
> [!question]- Respuesta
> No: la llave es (rut, teléfono) y rut → nombre, apellido tiene un lado izquierdo que no es superllave.

4. ¿Qué diferencia a BCNF de 3NF?
> [!question]- Respuesta
> 3NF también acepta X → Y cuando Y es parte de una llave minimal. BCNF exige siempre que X sea superllave, así que es más restrictiva.
