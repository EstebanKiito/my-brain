---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, origen/complemento]
prerrequisitos: []
---
# Qué es el testing de software

> [!tip] Complemento — nota nueva (fuente: slides "Testing")
> **Qué es:** *software testing* es un proceso para evaluar la **correctitud, completitud y calidad** de un programa. Incluye las actividades para **encontrar errores** y corregirlos antes de lanzar el producto a los usuarios finales.
>
> **¿Por qué es importante?**
> - Los bugs pueden ser **costosos e incluso peligrosos**.
> - Las personas cometemos errores (somos falibles).
> - **Detectar los defectos temprano** facilita el desarrollo, y **repararlos es más barato** mientras antes se encuentren.
> - Queremos que el programa siga funcionando: si algo puede fallar, fallará.
> - Queremos que el equipo verifique **de forma rápida y confiable** que todo sigue funcionando igual. Eso son las pruebas automatizadas, clave para entregar seguido en los [[08 - Procesos iterativos e incrementales|procesos iterativos e incrementales]].
>
> **¿Qué causa los defectos?** Los errores pueden venir de:
> - **programadores:** errores de especificación, diseño o implementación;
> - **usuarios finales:** usan el software de forma "no esperada";
> - el uso del sistema, las condiciones del ambiente, daño intencional, etc.
>
> La terminología precisa está en [[02 - Error, defecto y falla|Error, defecto y falla]]. Los niveles de pruebas en Rails están en [[03 - Niveles de testing en Rails|Niveles de testing en Rails]].

> [!tip] Complemento — la pirámide de tests
> ```mermaid
> flowchart TD
>   S["System tests: pocos, lentos, prueban todo el sistema"] --> I["Integration tests: controladores y rutas"] --> U["Unit tests: muchos, rápidos, prueban modelos aislados"]
> ```
> Conviene tener **muchos tests unitarios** (baratos y rápidos), menos de integración y pocos de sistema.

## Preguntas de repaso

1. ¿Qué es el testing de software?
> [!question]- Respuesta
> Un proceso para evaluar la correctitud, completitud y calidad de un programa, buscando errores para corregirlos antes de que lleguen a los usuarios.

2. ¿Por qué conviene encontrar los defectos temprano?
> [!question]- Respuesta
> Porque repararlos es más barato y facilita el desarrollo: un defecto encontrado en producción cuesta mucho más que uno encontrado al programar.

3. ¿Por qué automatizar las pruebas?
> [!question]- Respuesta
> Para que el equipo pueda verificar de forma rápida y confiable, después de cada cambio, que todo sigue funcionando.
