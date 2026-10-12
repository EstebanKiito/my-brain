---
ramo: Ingeniería de Software
tema: Historias de usuario
tags: [ingsoft/requisitos, origen/complemento]
prerrequisitos: ["[[01 - Historias de usuario|Historias de usuario]]"]
---
# Épicas, temas e historias

> [!tip] Complemento — nota nueva (fuente: slides "Historias de Usuario" y libro del curso, cap. 4.4 y 4.6)
> **Qué es:** las historias se pueden escribir en **distintos niveles de abstracción (granularidad)**:
>
> | Nivel | Qué es | ¿Tiene valor por sí solo? |
> |---|---|---|
> | **Historia de usuario** | Tamaño adecuado para implementarse **dentro de un sprint** | Sí |
> | **Épica** | Historia **grande** que puede abarcar **meses** de desarrollo. Se refina progresivamente en historias más pequeñas, a menudo secuenciales. | Las partes por separado suelen no tener mucho valor |
> | **Tema** | **Contenedor de historias relacionadas** (por ejemplo, variaciones de un mismo objetivo) | Cada historia del tema tiene valor por sí misma |
>
> ```mermaid
> flowchart TD
>   T[Tema: acceso a la aplicación] --> E[Épica: inscribir los cursos del semestre]
>   T --> H1[Historia: iniciar sesión]
>   E --> H2[Historia: buscar un curso]
>   E --> H3[Historia: inscribir una sección]
>   E --> H4[Historia: ver mi horario]
> ```
>
> **Ejemplos del libro:**
> - **Épicas:** comprar un pasaje de avión a San Francisco; inscribir los cursos del semestre usando Banner.
> - **Temas:** todas las historias de análisis de datos de clientes; todas las de acceso a la aplicación; todas las de manejo de productos.
>
> **Nivel de detalle adecuado (libro):** "ir de paseo a San Francisco" es demasiado para una historia, porque incluye pasaje, hotel, auto, etc. Incluso "comprar el pasaje" puede ser demasiado. Un criterio útil es que **la historia se pueda implementar en unos pocos días**, y por lo tanto dentro de un sprint. Tampoco hay que dividir hasta llegar a subtareas elementales, porque el número de historias crecería demasiado.

## Preguntas de repaso

1. ¿Qué diferencia hay entre una épica y un tema?
> [!question]- Respuesta
> Una épica es una historia grande que se descompone en historias más pequeñas (a menudo secuenciales) que por separado tienen poco valor. Un tema es una agrupación de historias relacionadas, cada una con valor propio.

2. ¿Cuál es el nivel de detalle adecuado para una historia de usuario?
> [!question]- Respuesta
> El que permite implementarla en unos pocos días, dentro de un sprint, sin llegar a subtareas elementales.

3. ¿"Comprar un pasaje de avión a San Francisco" es una historia o una épica? ¿Por qué?
> [!question]- Respuesta
> Una épica: incluye varios pasos (buscar vuelos, comparar aerolíneas y horarios, elegir asiento, pagar) que no caben en una sola historia de un sprint.
