---
ramo: Bases de Datos
tema: Privacidad de datos
tags: [bd/privacidad, origen/complemento]
prerrequisitos: ["[[01 - Funciones de agregación|Funciones de agregación]]"]
---
# Privacidad vs seguridad

La **privacidad** se trata de **qué se puede aprender** de los datos sobre una persona. La **seguridad**, de **quién puede ver o modificar** los datos. Un análisis preserva la privacidad si da un resultado útil y no importa si los datos de una persona se incluyen o no.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 15: Privacidad")
> **El uso de datos personales tiene riesgos:** los datos pueden contener información sensible o confidencial (financiera, médica, preferencias, artística…) y su uso puede filtrar parte de ella.
>
> Informalmente, **privacidad** es evitar que los datos de un individuo se hagan públicos o los conozcan terceros. Con la gran cantidad de datos que existe hoy, hace falta asegurar la privacidad de las bases de datos y de sus usos.
>
> **Un análisis de datos preserva privacidad si:**
> 1. Aprendes algo útil del análisis.
> 2. El análisis no viola la privacidad de ningún individuo.
>
> La privacidad de A se viola si el analista aprende B **sin** los datos de A, pero aprende B + C **con** ellos. Es decir, un análisis preserva la privacidad de un individuo si **no importa** que sus datos se consideren o no.
>
> | Seguridad | Privacidad |
> |---|---|
> | quién puede manipular los datos: **confidencialidad** (quién los ve) e **integridad** (quién los modifica) | qué podemos **aprender** de los datos (su contenido) |

> [!example] Ejemplo extra — dos casos reales (slides "Clase 15")
> - **Netflix (2007):** un concurso de US$ 1.000.000 para mejorar el recomendador publicó un dataset "anonimizado" ("all customer ids have been replaced by randomly assigned ids"). Cruzándolo con las calificaciones **públicas** de IMDb se re-identificó a usuarios: un **ataque de asociación de registros**.
> - **Gobernador de Massachusetts (1997):** William Weld aprobó liberar los registros médicos de los funcionarios públicos sin nombres. Los registros conservaban ZIP, fecha de nacimiento y sexo, que también aparecían en el **padrón electoral**, junto con el nombre. Dos días después, Latanya Sweeney (estudiante de doctorado del MIT) le envió por correo sus propios registros médicos.

> [!tip] Complemento — técnicas que se ven en el tema (slides "Clase 15")
> | Técnica | Funcionalidad | Nota |
> |---|---|---|
> | Anonimización | datos sintéticos | [[02 - Anonimización y re-identificación\|Anonimización y re-identificación]] |
> | k-Anonimato | datos sintéticos | [[03 - k-anonimato\|k-anonimato]] |
> | ℓ-diversidad | datos sintéticos | [[04 - ℓ-diversidad\|ℓ-diversidad]] |
> | Privacidad diferencial | respuestas a consultas | [[05 - Privacidad diferencial\|Privacidad diferencial]] |
>
> - **Datos sintéticos:** datos generados artificialmente que **lucen como los originales** (por ejemplo, con los nombres enmascarados). Permiten reutilizar análisis existentes, sirven para todas las consultas y facilitan el trabajo, pero es **imposible** tener a la vez utilidad perfecta y privacidad fuerte.
> - **Respuestas a consultas:** se entregan solo datos **agregados** ("¿cuántas personas nacieron en 2018?" → 4). Dependen de cada consulta y le complican la vida al analista, pero especializarse en una consulta permite mejor utilidad **y** mejor privacidad.
> - **Utilidad:** qué tan útil es la respuesta. "¿Cuántas personas se llaman Ford?": con datos anonimizados es imposible de responder; con privacidad diferencial se responde ± 1.

## Preguntas de repaso

1. ¿Qué diferencia hay entre privacidad y seguridad de los datos?
> [!question]- Respuesta
> La seguridad controla quién puede ver o modificar los datos (confidencialidad e integridad). La privacidad trata qué se puede aprender del contenido de los datos sobre una persona.

2. ¿Cuándo un análisis preserva la privacidad de un individuo?
> [!question]- Respuesta
> Cuando el resultado no depende de que sus datos estén incluidos o no: el analista aprende lo mismo con o sin ellos.

3. ¿Qué enseñan los casos de Netflix y de Massachusetts?
> [!question]- Respuesta
> Que quitar nombres o ids no basta: combinando el dataset con otra fuente pública (IMDb, el padrón electoral) se puede re-identificar a las personas.
