---
ramo: "Arquitectura de Sistemas de Software"
tema: "Medición de escalabilidad"
tags:
  - arquisis/escalabilidad
  - indice
---

# Índice — Medición de escalabilidad

Qué es la **escalabilidad** (adaptarse a más carga manteniendo un performance objetivo), cómo se escribe un **escenario** con su tiempo de escalamiento, dónde aparecen los cuellos de botella, qué métricas mirar, qué **pruebas** hacer (carga, estrés, soak, spike) y las tres leyes para calcular: **Little, Amdahl y Gustafson**.

## Contenido

1. [[01 - Escalabilidad escenarios y cuellos de botella]] — Definición, por qué escalar, heterogeneidad y portabilidad, escenarios con fuente, estímulo, entorno, artefacto, respuesta y medida, cuellos de botella y métricas.
2. [[02 - Tipos de pruebas de carga y monitoreo]] — Test de carga, de estrés, soak y spike, qué detecta cada uno, y proveedores de monitoreo manejados, open source y de la nube.
3. [[03 - Leyes de Little Amdahl y Gustafson]] — L = λW para dimensionar, el techo de Amdahl con su tabla de speedups, Gustafson con tiempo fijo y por qué no se contradicen.
