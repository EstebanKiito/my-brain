---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/complemento]
prerrequisitos: ["[[Proceso de desarrollo de software]]"]
---
# Cómo elegir un proceso de desarrollo

> [!tip] Complemento — nota nueva (fuente: slides "Procesos de Desarrollo de Software")
> **Qué es:** no existe un proceso universalmente mejor. La elección depende de factores de la organización, la tecnología, el negocio, la regulación y las personas.
>
> **Factores organizacionales**
> - ¿El equipo está en el mismo lugar o es remoto?
> - ¿Cómo está estructurado? ¿Hay project managers, senior devs? ¿Es un equipo pequeño o grande?
>
> **Factores tecnológicos**
> - ¿Cómo le gusta trabajar al equipo (pizarras, post-its)?
> - ¿Es posible tener una comunicación efectiva?
>
> **Factores del negocio**
> - ¿Qué tan familiar es el producto?
> - ¿Con qué frecuencia piden cambios o mejoras?
> - ¿Qué tan rápido cambia el estado del arte?
>
> **Factores regulatorios**
> - ¿Se construye algo que necesita aprobación del gobierno?
> - ¿Hay que entregar documentación muy específica?
>
> **Factores humanos**
> - ¿Cómo está compuesto el equipo? ¿Están en el mismo lugar, uno al lado del otro?
> - ¿Confían unos en otros?
> - ¿Cómo es la cultura de la compañía?
>
> **"Raya para la suma"**
> - No existe un buen proceso que tenga todo cubierto: **depende** del equipo, del cliente, del dominio, etc.
> - En realidad, la mayoría de las compañías **no usa un proceso de forma estricta**. Todo se personaliza al proyecto, al equipo o a la empresa.
> - Se puede tomar inspiración de varios procesos según las necesidades.

> [!example] Ejemplo extra — cómo se traduce en decisiones
> | Situación | Inclinación razonable |
> |---|---|
> | Requisitos estables, contrato cerrado, mucha documentación exigida | [[Modelo en cascada]] o un proceso con fases formales |
> | Mucha incertidumbre técnica y alto costo de fallar | [[Modelo en espiral]] |
> | El cliente no sabe bien lo que quiere | [[Modelo de prototipos]] |
> | Cambios frecuentes y necesidad de entregar valor pronto | [[Procesos iterativos e incrementales]] / [[Metodologías ágiles y manifiesto ágil\|ágil]] |
>
> Es una guía orientativa, no una regla. Ver también [[Comparación de modelos de proceso]].

## Preguntas de repaso

1. Nombra los cinco tipos de factores que influyen en la elección de un proceso.
> [!question]- Respuesta
> Organizacionales, tecnológicos, del negocio, regulatorios y humanos.

2. ¿Por qué un factor regulatorio puede empujar hacia un proceso más formal?
> [!question]- Respuesta
> Porque si el software requiere aprobación gubernamental o documentación muy específica, se necesitan fases con entregables documentados y trazables.

3. ¿Qué concluye la clase ("raya para la suma") sobre los procesos en la práctica?
> [!question]- Respuesta
> Que no hay un proceso perfecto: depende del equipo, el cliente y el dominio. La mayoría de las empresas no sigue un proceso de forma estricta, sino que lo adapta y combina ideas de varios.
