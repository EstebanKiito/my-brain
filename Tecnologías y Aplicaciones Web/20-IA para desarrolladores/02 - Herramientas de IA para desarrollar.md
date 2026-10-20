---
ramo: "Tecnologías y Aplicaciones Web"
tema: "IA para desarrolladores"
tags:
  - web
  - ia
  - herramientas
  - origen/complemento
prerrequisitos:
  - "[[01 - IA, ML, DL y modelos de lenguaje]]"
  - "[[03 - Code review, GitHub flow y commits]]"
---

# Herramientas de IA para desarrollar

Los modelos de lenguaje ya son parte del día a día de quien programa: explican errores, generan código y revisan cambios. Hay muchas formas de usarlos, y elegir bien importa menos que usarlos con criterio: el código generado es responsabilidad de quien lo integra, no del modelo.

## Tres formas de interactuar con un modelo

Hay muchas maneras de usar modelos ya entrenados y especializados en actuar como agentes, varias de ellas gratuitas. Para desarrollar se agrupan en tres categorías:

| Categoría | Qué es | Útil para |
|---|---|---|
| **Interfaz web conversacional** | Un chat que mantiene un diálogo coherente y en tema; la más conocida es ChatGPT | Explicar conceptos, discutir un diseño, entender un error |
| **Integración o extensión en el editor** | Extensiones que llevan la IA a editores populares como VS Code, con su enorme ecosistema | Autocompletar mientras se escribe, generar tests, explicar el código seleccionado |
| **IDE con IA integrada** | Editores "AI-first", donde la IA es protagonista y está integrada por completo | Cambios en varios archivos, agentes que ejecutan tareas sobre el proyecto |

Además aparecen constantemente otras alternativas, como agentes de línea de comandos o asistentes de code review, que ganan popularidad y amplían el ecosistema de generación de código con IA.

## Escribir buenos prompts

Un **prompt** es la instrucción que se le da al modelo. Como el modelo genera lo más probable dado el contexto, **más contexto relevante produce mejores respuestas**:

- decir el **objetivo** y las **restricciones** (lenguaje, versión, librerías del proyecto);
- entregar el código, el error completo y lo que ya se intentó;
- pedir un formato concreto (solo el diff, una explicación paso a paso, tests);
- dar ejemplos de lo esperado (*few-shot*), o pedir que razone por pasos antes de responder.

Las guías de *prompt engineering* de Google, Cohere y la *Prompt Engineering Guide* profundizan en estas técnicas, y el *AI Engineer Roadmap* traza el camino para quien quiera dedicarse a esto.

## Usarlas con criterio

> [!warning] Entender al 100% lo que se pide y lo que se recibe
> El consejo del curso es usar estas herramientas solo cuando se entiende completamente qué se espera recibir y qué generó el modelo. Código que no se entiende no se puede depurar, mantener ni defender en una revisión.

- **Revisar como un code review**: el código generado puede compilar y aun así estar mal, usar APIs inexistentes o tener vulnerabilidades (por ejemplo, una consulta SQL sin parametrizar).
- **Probar**: los tests y el linter siguen siendo la red de seguridad, se haya escrito el código a mano o no.
- **Cuidar los datos**: pegar en un chat externo código privado, credenciales o datos de usuarios puede filtrarlos.
- **Respetar la integridad académica**: en un curso, cada evaluación define qué uso está permitido.

> [!tip] Donde más rinden
> Las tareas repetitivas y bien definidas (código de plantilla, tests para casos claros, traducir entre formatos) y las explicaciones de código ajeno o de mensajes de error. Donde menos: decisiones de diseño, código crítico de seguridad y problemas que nadie ha descrito antes.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre una extensión de IA en el editor y un IDE "AI-first"?
> La extensión agrega funciones de IA a un editor existente (autocompletar, explicar). En un IDE AI-first la IA está integrada en todo el flujo, y puede leer y modificar muchos archivos del proyecto o ejecutar tareas como agente.

> [!question]- ¿Por qué un buen prompt incluye el error completo y la versión de las librerías?
> Porque el modelo genera la respuesta más probable dado el contexto que recibe. Sin esos datos rellena con supuestos genéricos, y puede proponer soluciones para otra versión o para otro problema.

> [!question]- ¿Qué riesgos tiene integrar código generado sin revisarlo?
> Que tenga errores sutiles, use funciones que no existen o introduzca vulnerabilidades, y que nadie del equipo lo entienda lo suficiente para depurarlo o mantenerlo.
