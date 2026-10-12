# Estándar de notas del vault

Modelo extraído de las notas que se escribieron sin apuntes. En Sistemas Operativos y Redes son:
- [[02 - Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady]]
- [[03 - Algoritmo LRU e implementaciones con hardware y software]]
- [[04 - Algoritmo del reloj (Clock) y aproximaciones prácticas de LRU]]
- [[03 - Comunicación entre procesos y manejo de señales en C]]

Toda nota reescrita sigue este estándar. No existe otra guía de estilo en el vault.

## Estructura

```markdown
---
ramo: "<Ramo>"
tema: "<Tema = carpeta sin prefijo>"
tags:
  - <tags temáticos que ya tenía la nota>
  - origen/complemento
prerrequisitos:
  - "[[NN - Nota previa]]"
---

# <Título = nombre del archivo sin el prefijo NN ->

<Párrafo de entrada (2-4 líneas): qué problema resuelve el concepto y por qué importa.>

## <Sección 1: la idea central>
<Prosa. Cada afirmación va con su porqué.>

> [!tip] <Regla o definición clave>
> <Una o dos frases memorizables.>

## <Sección 2: mecanismo, ejemplo o comparación>
<Tabla o Mermaid cuando ordena la información. Código corto si corresponde.>

![<descripción>](adjuntos/<imagen>.png)

> [!example]- Transcripción de la imagen
> <Lo que muestra la imagen, en 2-5 viñetas o un párrafo.>

> [!warning] <Trampa o confusión típica>
> <Explicación breve.>

## Preguntas de repaso

> [!question]- <Pregunta que obliga a explicar un porqué>
> <Respuesta de 1-3 frases.>
```

## Tono y contenido
- **Prosa explicativa**, en español neutro y en tercera persona. Las viñetas se reservan para enumeraciones cortas (pasos de un algoritmo, clases o casos) y nunca reemplazan la explicación.
- **El porqué antes que el qué:** cada mecanismo dice qué problema resuelve y cuál es su costo o su límite (ej. "LRU exacto no se implementa porque exige actualizar la lista en cada acceso").
- **Términos técnicos** en **negrita** la primera vez. El término inglés va en *cursiva* entre paréntesis si es el que se usa en la práctica (*page fault*, *busy waiting*).
- **Fórmulas** en LaTeX inline (`$EAT = …$`). Identificadores de código, llamadas y señales entre backticks (`fork()`, `SIGKILL`).
- **Callouts** con moderación: `[!tip]` para la regla central, `[!warning]` para trampas o fenómenos patológicos, `[!example]-` (plegado) para transcripciones de imágenes o ejemplos largos, `[!question]-` solo en el repaso.
- **Diagramas:** Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`) para flujos y estados; tablas para comparar alternativas. Uno por nota suele bastar, y solo si aclara.
- **Ejemplos concretos:** una traza, un cálculo numérico o un fragmento de código breve. El código C compila con `gcc -Wall -pthread`; el Python corre con `python3`.
- **Preguntas de repaso:** de 3 a 5, al final, cada una con respuesta plegable `> [!question]- …`. Preguntan por causas, consecuencias o comparaciones, no por definiciones literales.
- **Largo:** de 60 a 120 líneas, máximo 150. Lo esencial para entender y repasar, sin ser exhaustivo.

## Qué conservar de los apuntes originales
Los apuntes marcan **qué** debe estar, no **cómo** se dice. Se conserva, reescrito, cada concepto técnico, ejemplo, analogía y mnemotecnia. Las erratas se corrigen sin comentarlas.

## Qué no va nunca en una nota
- Marcas de procedencia: "(mis apuntes)", el tag `origen/apuntes`, nombres de PDF, números de página, "clase N", "semana N", rutas a `_raw`.
- Citas literales `> …` de los apuntes, "Estudiar", "Por estudiar", "XD", recordatorios personales, comentarios sobre pruebas, clases o profesores.
- Callouts de "Posible error" (la errata se corrige en el texto; si hay una duda real de contenido, se registra en `_meta/<Ramo>/DUDAS.md`).
- Placeholders o texto que no sea contenido de la materia.

## Exactitud
- Si los apuntes, el material de clase y el conocimiento general no coinciden, la nota dice lo que muestra el material de clase, sin generalizar, y la discrepancia se registra en DUDAS.md.
- Si un dato técnico no es seguro, se omite.
- Las imágenes de `adjuntos/` siguen referenciadas, con una transcripción comprobada contra la imagen.
