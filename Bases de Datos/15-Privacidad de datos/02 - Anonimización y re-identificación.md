---
ramo: Bases de Datos
tema: Privacidad de datos
tags: [bd/privacidad, origen/complemento]
prerrequisitos: ["[[01 - Privacidad vs seguridad|Privacidad vs seguridad]]"]
---
# Anonimización y re-identificación

**De-identificar** es quitar la asociación entre una persona y sus datos (por ejemplo, enmascarar el nombre). Pero los **cuasi-identificadores** que quedan (fecha de nacimiento, sexo, código postal) permiten **re-identificar** a la persona cruzándolos con otra fuente.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 15: Privacidad")
> **Los atributos de una tabla se dividen en 4 categorías disjuntas:**
> | Categoría | Qué es | Ejemplos |
> |---|---|---|
> | **Identificador explícito (IdE)** | atributos que **individualmente** identifican al dueño del registro | nombre, RUT |
> | **Cuasi-identificador (CId)** | atributos que **colectivamente** pueden identificar al dueño | fecha de nacimiento, sexo, dirección o código postal |
> | **Atributo sensible (AS)** | valores que se desea proteger | religión, etnia, enfermedad |
> | **Atributo no sensible (AnS)** | sin carácter privado | equipo de fútbol, película favorita |
>
> **De-identificación:** proceso que remueve la asociación entre una persona y un conjunto de datos. Busca **reducir el riesgo** de violar la privacidad y **maximizar la utilidad** de los datos. Técnicas: **supresión** (remover datos), **variación** ("revolver" los datos) y **enmascaramiento** (por ejemplo, reemplazar los nombres por `******`).

> [!example] Ejemplo extra — ataque de asociación de registros (slides "Clase 15")
> | Nombre | Fecha nac. | Sexo | Código postal | Enfermedad |
> |---|---|---|---|---|
> | \*\*\*\*\*\* | 26/02/2018 | M | 73909 | Resfrío |
> | \*\*\*\*\*\* | 08/05/2018 | M | 14890 | Hepatitis |
> | \*\*\*\*\*\* | 11/05/2018 | F | 58821 | Hepatitis |
> | \*\*\*\*\*\* | 31/03/2019 | F | 465113 | VIH |
> | \*\*\*\*\*\* | 26/04/2018 | F | 90825 | Bronquitis |
>
> Un dato auxiliar, "Rashad Arnold nació el 08/05/2018", basta para el join: **Rashad Arnold tiene hepatitis**. La **re-identificación** vuelve a asociar a una persona con sus datos, y depende de los datos auxiliares que tenga el atacante.

> [!example] Ejemplo extra — ataque de diferenciación (slides "Clase 15")
> Si uno puede diseñar sus propias consultas, el problema es peor. Una suma sobre un grupo grande parece inofensiva:
> ```sql
> SELECT sum(age) FROM person;                               -- 1256257
> SELECT sum(age) FROM person WHERE nombre <> 'Alan Brito';  -- 1256218
> ```
> $1256257 - 1256218 = 39$: **Alan Brito tiene 39 años.**

> [!tip] Complemento — lo que muestran los ataques (slides "Clase 15")
> - Un ataque de asociación combina **datos auxiliares** con datos de-identificados para re-identificar a las personas. En el caso más simple es un **join** de dos tablas.
> - Son sorprendentemente efectivos. **Un** CId basta para reducir todo a unos pocos registros; **dos** CId suelen re-identificar a gran parte de la población; **tres CId (sexo, código postal y fecha de nacimiento) identifican de forma única al 87% de las personas en EE.UU.**
> - Por eso hacen falta garantías formales: [[03 - k-anonimato|k-anonimato]].

## Preguntas de repaso

1. ¿Qué diferencia hay entre un identificador explícito y un cuasi-identificador?
> [!question]- Respuesta
> El explícito identifica por sí solo (nombre, RUT). Los cuasi-identificadores identifican al combinarse (fecha de nacimiento + sexo + código postal).

2. ¿Qué es un ataque de asociación de registros?
> [!question]- Respuesta
> Cruzar (hacer un join de) un dataset de-identificado con datos auxiliares que comparten cuasi-identificadores para re-identificar a las personas.

3. Explica el ataque de diferenciación con las sumas de edades.
> [!question]- Respuesta
> Se pide la suma de todas las edades y la suma sin Alan Brito. La diferencia (39) es exactamente la edad de Alan, aunque cada consulta por sí sola era agregada.

4. ¿Qué porcentaje de la población de EE.UU. identifican sexo, código postal y fecha de nacimiento?
> [!question]- Respuesta
> El 87%, de forma única.
