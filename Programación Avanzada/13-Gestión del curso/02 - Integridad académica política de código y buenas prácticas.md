---
ramo: "Programación Avanzada"
tema: "Gestión del curso"
tags:
  - ramo/gestion
  - ramo/integridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Programa del curso metodología y reglas de evaluación]]"
---

# Integridad académica política de código y buenas prácticas

El desarrollo de software en la vida profesional exige altos estándares de ética, trazabilidad y atribución de autoría. En el contexto universitario del curso Programación Avanzada, la integridad académica no es solo un reglamento disciplinario, sino el pilar que garantiza que cada estudiante adquiera las competencias reales de diseño y resolución de problemas.

## Plataformas oficiales de aprendizaje

El curso centraliza toda su interacción en un ecosistema abierto basado en Git y GitHub:

```
+--------------------+-------------------------------------------------------------+
| Plataforma         | Propósito en el curso                                       |
+--------------------+-------------------------------------------------------------+
| Canvas UC          | Avisos oficiales de cátedra y publicación de notas          |
| GitHub Syllabus    | Enunciados de evaluaciones, fechas y foro de dudas (Issues) |
| GitHub Contenidos  | Notebooks .ipynb interactivos para estudio autónomo         |
| Wiki del Curso     | Guías de instalación de PyQt, tutoriales y guías de estilo  |
+--------------------+-------------------------------------------------------------+
```

El foro de dudas opera sobre los **Issues** de GitHub: permite formular preguntas técnicas públicas, formatear código en bloques markdown y buscar respuestas a inquietudes resueltas en semestres previos.

## Normas de integridad académica y sanciones

La Escuela de Ingeniería y el Departamento de Ciencia de la Computación (DCC) aplican tolerancia cero ante la deshonestidad académica:

- **Carácter individual:** todas las tareas, actividades y evaluaciones son estrictamente individuales. Está terminantemente prohibido compartir archivos de código, mostrar fragmentos a compañeros o programar en parejas.
- **Sanción directa:** cualquier situación de copia, plagio o colusión comprobada en una evaluación tiene como sanción inmediata una **nota final $1.1$ reprobatoria en el curso**, sin perjuicio de la elevación del caso a la Comisión de Integridad Académica.

## Política de uso y atribución de código de terceros

En la industria es habitual consultar librerías y documentación en internet. En el curso se permite utilizar fragmentos pequeños de código encontrados en la web siempre y cuando se cumplan dos condiciones:

1. **Atribución explícita obligatoria:** debes citar de forma transparente el enlace web de origen en los comentarios del archivo de código:
   ```python
   # Código adaptado para cálculo de distancias geográficas
   # Fuente: https://stackoverflow.com/questions/19412465/...
   ```
2. **Material del curso:** solo está permitido reutilizar código de semestres previos si fue publicado de manera oficial por el equipo docente en cátedras o ayudantías.

El omitir la cita de una fuente externa se considera plagio y constituye una falta grave a la ética.

## Política sobre herramientas generadoras de código

El uso de generadores automáticos de código basados en inteligencia artificial (como ChatGPT, GitHub Copilot u otros) se encuentra restringido en las evaluaciones evaluadas:

- **Pérdida de pensamiento crítico:** el objetivo del curso es que el estudiante interiorice cómo modularizar, cómo diagnosticar condiciones de carrera en memoria y cómo estructurar sockets en bajo nivel. Delegar la síntesis de código anula el proceso cognitivo de aprendizaje.
- **Impredecibilidad y alucinaciones:** estas herramientas frecuentemente introducen patrones obsoletos o librerías desactualizadas que no cumplen las restricciones del ramo.

> [!tip] Buenas prácticas para superar el ramo
> Comienza las tareas el mismo día de su publicación; nunca intentes resolver una tarea de PyQt o Sockets en las últimas 48 horas. Realiza commits locales frecuentes en Git tras cada función terminada para mantener un historial de respaldo seguro.

## Preguntas de repaso

> [!question]- ¿Qué consecuencia académica acarrea cometer plagio o copia en una entrega del curso?
> Una calificación final de $1.1$ en el ramo completo y el envío del expediente a la Comisión de Integridad Académica de la Escuela de Ingeniería.

> [!question]- ¿Está permitido utilizar una función auxiliar encontrada en StackOverflow para resolver parte de una tarea?
> Sí, siempre y cuando se incluya un comentario explícito en el código fuente con el enlace URL a la respuesta original reconociendo la autoría externa.

> [!question]- ¿Por qué el curso prohíbe el uso de asistentes generadores de código en las evaluaciones?
> Porque impide desarrollar las habilidades fundamentales de razonamiento algorítmico, diseño arquitectónico y depuración autónoma que el ramo busca certificar.

> [!question]- ¿Cuál es el canal oficial para formular dudas técnicas sobre los enunciados de las tareas?
> El sistema de *Issues* del repositorio público `IIC2233/Syllabus` en GitHub.
