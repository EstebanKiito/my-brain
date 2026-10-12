---
ramo: Ingeniería de Software
tema: Historias de usuario
tags: [ingsoft/requisitos, origen/complemento]
prerrequisitos: ["[[02 - Estructura de una historia de usuario|Estructura de una historia de usuario]]", "[[04 - Criterio INVEST|Criterio INVEST]]"]
---
# Errores comunes en historias de usuario

> [!tip] Complemento — nota nueva (fuente: slides "Historias de Usuario" y libro del curso, cap. 4.5)
> **Qué es:** los errores típicos al escribir historias, los que en clase hacían perder la décima.
>
> **Errores que destacan las slides:**
> 1. **Historias técnicas:** se escriben desde el desarrollador y no desde el usuario. Ejemplo: *"As a developer I want to add a credit card field to the billing table…"*. No dice qué valor recibe un usuario.
> 2. **El "por qué" no queda claro:** el "para" no justifica nada. Ejemplo: *"As a customer ordering food I want to locate previous orders so to see how many orders I have placed to date."* ¿Para qué quiere saber cuántos pedidos hizo?
>
> **Directrices del libro (lo que sí hay que hacer):**
> - Idealmente, **independientes**, para poder reorganizarlas según la prioridad.
> - Deben aportar valor **al cliente**.
> - Deben permitir al equipo **estimar** con facilidad.
>
> **"Malos hábitos" según el libro:**
> - Usar el genérico **"as a user"**: hay que ser más específico con el rol.
> - **Concisión extrema**, por ejemplo *"Los resultados se deben guardar en formato XML"*.
> - Historias con **interdependencias**, que dificultan la planificación.
> - **Goldplating**: agregar características innecesarias (por ejemplo, "además de las pestañas, permitir arrastrar elementos").
> - **Exceso de detalle**: la tarjeta es pequeña a propósito.
> - Definir **detalles de la interfaz** demasiado pronto.
> - Copiar **requisitos formales** dentro de las historias.

> [!example] Ejemplo extra — corregir una historia técnica
> - ❌ *"Como desarrollador quiero agregar la columna `credit_card` a la tabla `billing`."*
> - ✅ *"Como comprador frecuente necesito guardar mi tarjeta de crédito para pagar más rápido en mis próximas compras."*
>
> El cambio en la base de datos pasa a ser una **tarea** dentro de la historia, no la historia en sí.

## Preguntas de repaso

1. ¿Qué es una "historia técnica" y por qué es un error?
> [!question]- Respuesta
> Una historia escrita desde el punto de vista del desarrollador ("como desarrollador quiero agregar un campo…"). Es un error porque no expresa valor para un usuario: describe una tarea de implementación, no una necesidad.

2. ¿Qué es el goldplating?
> [!question]- Respuesta
> Agregar funcionalidades o adornos que nadie pidió y que no aportan valor necesario, lo que gasta esfuerzo innecesario.

3. ¿Por qué se recomienda evitar "como usuario"?
> [!question]- Respuesta
> Porque es genérico: no dice qué tipo de usuario tiene la necesidad, y eso hace más difícil entender el contexto y priorizar.
