# Nivel de detalle y flujo de trabajo — Arquitectura de Sistemas de Software (IIC2173)

Referencia para mantener la consistencia de los 28 temas de **Arquisis**. El usuario migra el ramo mientras prepara la I2, que evalúa todo el curso hasta Escalabilidad con foco teórico en Integración, DDD táctico, Performance y Escalabilidad.

## Público y tono
- Estudiante de 4° año de Ciencia de la Computación que ya cursó Ingeniería de Software, Bases de Datos y Sistemas Distribuidos. No se explican HTTP, SQL ni UML de clases desde cero: se enlazan.
- Prosa explicativa con el porqué de cada decisión. En arquitectura casi nada es "correcto" en abstracto: cada concepto se presenta con **qué problema resuelve**, **qué cuesta** (el tradeoff) y **cuándo no conviene**.

## Qué lleva cada nota
- Un ejemplo concreto por concepto: el e-commerce que usa el curso (Catálogo, Checkout, Promociones, Inventario, Envío, Pagos, ERP), sistemas reales (Amazon Prime, Twitter, Instagram, Google, AWS) o un caso de prueba.
- Tablas comparativas cuando hay alternativas (relaciones del context map, cola vs log, REST vs gRPC vs GraphQL, sharding vs partitioning).
- Mermaid para flujos y topologías. Los diagramas de componentes UML se dibujan con Mermaid aproximado (componente = caja, interfaz provista = `--o`) solo cuando aclaran; si no, se usa la imagen de los apuntes o de la slide.
- `[!warning]` con las **trampas que castigan las pautas**, por ejemplo:
  - "Pipe & filter filtra datos; no es para procesamiento pesado."
  - "Cliente-servidor no se justifica solo por tener front y back."
  - "El broker, la API Gateway o la base de datos no son subdominios."
  - "Leader-follower no ayuda cuando el problema son muchos writes."
  - "Más cómputo es táctica de performance, no de integrabilidad."
- Cálculos resueltos y comprobados con `python3` (ley de Little, Amdahl, Gustafson, nueves de disponibilidad, latencias p95/p99).

## Preguntas de repaso
- De 5 a 8 por nota, en `[!question]-` plegables, mezclando los formatos de la prueba:
  - **Desarrollo** corto ("explique por qué…", "compare…", "¿qué tradeoff…?").
  - **Alternativas** con I/II/III o a)–d), con la respuesta justificada opción por opción.
  - **Verdadero o falso** con la justificación.
  - **Mini caso**: un enunciado de 2-3 líneas y la decisión de diseño esperada, con la razón que pide la pauta.
  - **Cálculo** cuando el tema lo permite.

## Lo que no va
- Marcas de procedencia en las notas de contenido ("clase N", "I1/I2", nombres de PDF, "sesión 04"). Las notas de `26-Resolución de casos de diseño` y `28-Gestión del curso` sí nombran las evaluaciones, porque ese es su tema.
- Placeholders de los apuntes (`[Copiar]`): se registran en `aceptados` y su contenido se toma de las slides.
