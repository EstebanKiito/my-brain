---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[03 - Arquitectura en capas|Arquitectura en capas]]"]
---
# Escalamiento y teorema CAP

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes")
> **Qué es:** cómo hacer que un sistema soporte más carga, y qué se sacrifica al distribuirlo en varias máquinas.
>
> ## Escalamiento vertical vs. horizontal
> ![Slide - escalamiento vertical y horizontal](adjuntos/Slide%20-%20escalamiento%20vertical%20y%20horizontal.png)
>
> | | Vertical (*scale up*) | Horizontal (*scale out*) |
> |---|---|---|
> | Cómo | una máquina **más potente** (más CPU, RAM) | **más máquinas** iguales |
> | Límite | el hardware máximo disponible | prácticamente ilimitado |
> | Complejidad | baja (nada cambia en el código) | alta: datos distribuidos, balanceo de carga |
>
> ## ¿Escalar horizontalmente es fácil? El teorema CAP
> ![Slide - teorema CAP](adjuntos/Slide%20-%20teorema%20CAP.png)
>
> Según el teorema, **no se pueden asegurar más de dos** de estas características simultáneamente:
> - **Consistency (consistencia):** todos los clientes ven la misma vista de los datos, incluso justo después de una actualización o borrado.
> - **Availability (disponibilidad):** todos los clientes pueden encontrar una réplica de los datos, incluso si hay nodos caídos.
> - **Partition tolerance (tolerancia a particiones):** el sistema sigue funcionando como se espera aunque la red se parta (fallos de comunicación entre nodos).
>
> Combinaciones: **CA**, **CP** y **AP**.
>
> **Precisión:** en un sistema distribuido real las particiones de red **van a ocurrir**, así que en la práctica la elección es **entre C y A cuando hay una partición**:
> - **CP:** rechaza o espera para no dar datos desactualizados (por ejemplo, un banco).
> - **AP:** responde siempre, aunque el dato pueda estar levemente desactualizado (por ejemplo, el contador de "likes").

## Preguntas de repaso

1. ¿Qué diferencia hay entre escalar vertical y horizontalmente?
> [!question]- Respuesta
> Vertical: aumentar la potencia de una sola máquina. Horizontal: agregar más máquinas que se reparten la carga.

2. Enuncia el teorema CAP.
> [!question]- Respuesta
> En un sistema distribuido no se pueden garantizar simultáneamente consistencia, disponibilidad y tolerancia a particiones; como máximo dos.

3. Durante una partición de red, ¿qué elige un sistema AP?
> [!question]- Respuesta
> Seguir respondiendo (disponibilidad), aun a costa de que algunos clientes vean datos no actualizados (sacrifica la consistencia).
