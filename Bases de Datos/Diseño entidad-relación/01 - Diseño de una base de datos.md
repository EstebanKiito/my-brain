---
ramo: Bases de Datos
tema: Diseño entidad-relación
tags: [bd/diseño, origen/complemento]
prerrequisitos: ["[[02 - Modelo relacional|Modelo relacional]]"]
---
# Diseño de una base de datos

Diseñar una base de datos es pasar de lo que necesitan los usuarios a un esquema relacional en tres etapas: análisis de requisitos, diseño conceptual (modelo E/R) y diseño lógico (modelo relacional).

> [!tip] Complemento — nota nueva (fuente: slides "Clase 5: Diseño de Bases de Datos" y "Clase 6: Diseño de Bases de Datos II")
> Ya conocemos el modelo relacional y SQL, así que podemos diseñar una base de datos. Pero… ¿sabemos si lo estamos haciendo bien? **Un error en la modelación puede ser muy costoso**; por ejemplo, olvidar añadir una columna.
>
> ```mermaid
> flowchart LR
>   U[Usuarios] -->|Análisis de requisitos| Req[Requisitos]
>   Req -->|Diseño conceptual| ER[Modelo entidad-relación]
>   ER -->|Diseño lógico| MR[Modelo relacional]
> ```
>
> **Construir una aplicación con un RDBMS:**
> - En la práctica es imposible saber de antemano todos los requisitos que debe cumplir un software.
> - Por eso el esquema de la base de datos va cambiando a medida que avanza el proyecto (ver [[05 - Migraciones en Rails|migraciones]]).
> - Un esquema bien diseñado no solo permite consultar con facilidad y guardar los datos de forma óptima: también permite **modificarlo y aumentarlo** con menos dolores de cabeza.
> - Los errores de diseño son muy costosos a la larga.
>
> **Por qué diseñar y diagramar la base de datos:**
> - Identificar las entidades.
> - Entender cómo se asocian esas entidades.
> - Visualizar las restricciones del dominio.
> - Lograr un buen diseño.
> - Mantener el esquema bien documentado.

> [!example] Ejemplo extra — las tres etapas con un caso
> 1. **Requisitos:** "Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y ciudad de origen; cada cerveza, ciudad de origen, tipo y grados. Ambos tienen un precio unitario y una cantidad en stock cada día."
> 2. **Conceptual (E/R):** entidad `Bebida` con subclases `Vino` y `Cerveza`, más el stock como entidad o relación ([[02 - Diagramas entidad-relación|diagramas E/R]]).
> 3. **Lógico (relacional):** tablas `Bebida(nombre, …)`, `Vino(nombre, año)`, … con sus llaves ([[05 - Del modelo E-R al relacional|del modelo E/R al relacional]]).

## Preguntas de repaso

1. ¿Cuáles son las tres etapas del diseño de una base de datos?
> [!question]- Respuesta
> Análisis de requisitos (usuarios → requisitos), diseño conceptual (requisitos → modelo E/R) y diseño lógico (modelo E/R → modelo relacional).

2. ¿Por qué conviene diagramar antes de crear las tablas?
> [!question]- Respuesta
> Para identificar las entidades y cómo se asocian, ver las restricciones del dominio, lograr un buen diseño y dejar el esquema documentado.

3. ¿Por qué el esquema de una base de datos cambia durante un proyecto?
> [!question]- Respuesta
> Porque es imposible conocer todos los requisitos de antemano. Un buen diseño permite modificar y extender el esquema con menos problemas.
