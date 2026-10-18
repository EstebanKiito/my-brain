---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/apuntes]
prerrequisitos: ["[[03 - Procesos iterativos|Procesos iterativos]]"]
---
# Proceso unificado (RUP)

El Proceso Unificado es un proceso **iterativo** muy completo y formal, organizado en **4 fases** y guiado por casos de uso, arquitectura y riesgos.

## Características
- Usa **UML** (*Unified Modeling Language*) como notación para sus modelos. UML no es exclusivo del Proceso Unificado: es un lenguaje de modelado general, estandarizado por el OMG. Aparecen juntos porque los crearon los mismos autores (Booch, Rumbaugh y Jacobson, en Rational).
- Contempla **cuatro fases**:
  1. **Inicio:** se establece el caso de negocio y se evalúa la viabilidad.
  2. **Elaboración:** se verifica que el equipo es capaz de construir el sistema (arquitectura y riesgos principales).
  3. **Construcción:** se construye un sistema que funcione, una **versión beta**.
  4. **Transición:** se entrega a los usuarios un sistema completamente funcional.

![Proceso unificado - fases y disciplinas](adjuntos/Proceso%20unificado%20-%20fases%20y%20disciplinas.png)

```mermaid
flowchart LR
  I[Inicio] --> E[Elaboración] --> C[Construcción] --> T[Transición]
```

## Ventajas
- **Dirigido por casos de uso:** el trabajo se organiza en torno a lo que el usuario necesita hacer con el sistema.
- **Centrado en la arquitectura:** la estructura del sistema se define y valida temprano, en la Elaboración.
- **Enfocado en los riesgos críticos:** lo más riesgoso se aborda primero.

## Desventajas
- Pone mucho **énfasis en la documentación**.
- Es **costoso** de implementar.
- Exige mucha **gestión y supervisión**.
- Es **iterativo, pero no siempre incremental**: las iteraciones no siempre entregan funcionalidad nueva y usable, lo que limita su adaptabilidad.

> [!tip] Complemento (libro del curso, cap. 2.3)
> - Antes se llamaba **RUP** (*Rational Unified Process*).
> - **Cómo leer la imagen:** las columnas son las fases (Inception, Elaboration, Construction, Transition), divididas en iteraciones (I1, E1, C1…Cn, T1, T2). Las filas son **disciplinas** o *workflows* (modelado, implementación, pruebas, despliegue, gestión de configuración, gestión de proyecto, entorno). El alto de cada curva indica **cuánto se trabaja** esa disciplina en cada momento. Por ejemplo, el modelado es fuerte en Inicio y Elaboración, y la implementación es fuerte en Construcción. En todas las fases se hace un poco de todo, pero con distinta intensidad.
> - **Cada fase puede tener varias iteraciones** hasta cumplir su objetivo.
> - Define con mucho detalle los *workflows*, roles, artefactos de entrada y de salida. Fue uno de los primeros intentos de un proceso iterativo completo.
> - **Mitigación temprana del riesgo:** desarrolla primero los casos de uso más riesgosos, en vez de esperar a etapas avanzadas como en la [[02 - Modelo en cascada|cascada]].
> - **Desafíos:** es complejo para equipos pequeños (una persona puede tener que asumir varios roles). Además, al no ser siempre incremental, encaja mal con las [[09 - Metodologías ágiles y manifiesto ágil|metodologías ágiles]].

## Preguntas de repaso

1. ¿Cuáles son las 4 fases del Proceso Unificado y el objetivo de cada una?
> [!question]- Respuesta
> Inicio (caso de negocio y viabilidad), Elaboración (verificar que se puede construir el sistema), Construcción (construir un sistema que funcione, versión beta) y Transición (entregar el sistema completamente funcional a los usuarios).

2. ¿Por qué se dice que RUP es "iterativo pero no siempre incremental" y qué consecuencia tiene?
> [!question]- Respuesta
> Porque cada fase se recorre en iteraciones, pero esas iteraciones no siempre entregan funcionalidad nueva y usable. Eso limita su adaptabilidad frente a los procesos ágiles.

3. En el diagrama de RUP, ¿qué representa la altura de cada curva?
> [!question]- Respuesta
> La intensidad del trabajo en esa disciplina (modelado, implementación, pruebas, etc.) en cada fase o iteración.

4. ¿Es UML parte exclusiva de RUP?
> [!question]- Respuesta
> No. UML es un lenguaje de modelado general, estandarizado por el OMG, que se puede usar con cualquier proceso; RUP lo adopta como su notación.
