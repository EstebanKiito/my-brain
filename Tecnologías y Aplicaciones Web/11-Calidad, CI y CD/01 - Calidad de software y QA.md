---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Calidad, CI y CD"
tags:
  - web
  - calidad
  - qa
  - origen/complemento
prerrequisitos:
  - "[[04 - Modelos, migraciones y seeds con Sequelize]]"
---

# Calidad de software y QA

Una aplicación web pasa rápidamente de unos pocos archivos a decenas, escritos por varias personas. ¿Cómo se desarrolla "bien" a esa escala? La pregunta no es estética: el software afecta a personas reales, y un error puede costar dinero, datos o incluso vidas. Esta nota define qué se entiende por calidad y qué prácticas existen para asegurarla.

## Qué es la calidad de software

La **calidad de software** es el área que describe los atributos deseables de un producto de software. Los dos más básicos son que **haga lo que debe hacer** y que **lo haga sin errores**.

Importa por dos razones:

- **Riesgo**: los problemas de software tienen consecuencias de distinta gravedad.
- **Costo**: el software de buena calidad reduce costos, y uno de mala calidad puede salir muy caro.

El software no existe en el vacío: influye en su contexto (personas, finanzas, política, adicciones) y hay deberes legales, éticos y morales en juego. Quien desarrolla tiene que ser consciente de ese impacto. Su responsabilidad incluye minimizar riesgos en:

- la privacidad;
- la seguridad de los datos;
- la seguridad de las personas;
- la confiabilidad;
- la facilidad de uso.

Las buenas prácticas existen justamente para reducir el riesgo de problemas.

| Baja calidad | Alta calidad |
|---|---|
| Caídas de tiendas en Cyberday y Cybermonday | El rover Perseverance de la NASA |
| Therac-25 (una máquina de radioterapia cuyos errores de software causaron sobredosis mortales) | Google Suite |
| Fallas de software en autos de Toyota y Tesla | |

Es más fácil recordar ejemplos de baja calidad, porque el software que funciona bien pasa desapercibido.

> [!warning] Una dependencia mínima puede romperlo todo
> En el incidente de **left-pad** (2016), un programador retiró de npm un paquete de 11 líneas que rellenaba strings con espacios. Miles de proyectos dependían de él, directa o indirectamente, y sus builds fallaron en todo el mundo. Es la imagen del xkcd *Dependency*: una infraestructura enorme apoyada en una pieza diminuta que mantiene una sola persona.

## Aseguramiento de calidad (QA)

El **aseguramiento de calidad** (*Quality Assurance*, QA) es el conjunto de prácticas y procesos que permiten asegurar una calidad de software adecuada. Lo razonable es cubrir los atributos deseables en mayor o menor medida, empezando por lo más **crítico** (lo que, si falla, causa más daño).

> [!tip] El software sin errores no existe
> Todo software lo escriben personas, y las personas se equivocan. El objetivo realista es **minimizar** los errores y verificar que el software funcione y sea mantenible.

Hay tres técnicas principales:

| Técnica | Qué es | Cuándo actúa |
|---|---|---|
| **Testing** | Pruebas automatizadas que someten al software a distintos escenarios | Ejecutando el código |
| **Análisis estático** | Revisión automática del código sin ejecutarlo | Sobre el código fuente |
| **Code review** | Revisión del código por parte de pares | Antes de integrar cambios |

El **testing** prueba que la funcionalidad cumple lo especificado y que es robusta frente a errores posibles. Es muy común en librerías de código abierto y en software en producción, y poco común en proyectos personales.

Las otras dos técnicas se detallan en [[02 - Análisis estático y linters|Análisis estático y linters]] y [[03 - Code review, GitHub flow y commits|Code review, GitHub flow y commits]]. La calidad desde la ingeniería de software está en [[03 - Calidad de software|Calidad de software]].

Detrás de las "buenas prácticas" hay una idea que Robert C. Martin (2008) resume así: cuidar los detalles le da al profesional dominio y confianza en su trabajo, mientras que un fallo de construcción produce desencanto por el trabajo en general.

## Preguntas de repaso

> [!question]- ¿Por qué la calidad de software es una responsabilidad ética y no solo técnica?
> Porque el software afecta a personas reales: sus datos, su seguridad, su dinero e incluso su salud (como en Therac-25). Quien lo construye responde por esos riesgos, incluidos los deberes legales y morales.

> [!question]- Si el software sin errores no existe, ¿cuál es el objetivo del QA?
> Minimizar los errores, priorizando las partes más críticas, y verificar que el software funcione y siga siendo mantenible.

> [!question]- ¿Qué enseña el incidente de left-pad?
> Que cada dependencia es un riesgo: un paquete mínimo, mantenido por una sola persona, puede romper miles de proyectos si desaparece o falla. Conviene saber de qué se depende y fijar versiones.
