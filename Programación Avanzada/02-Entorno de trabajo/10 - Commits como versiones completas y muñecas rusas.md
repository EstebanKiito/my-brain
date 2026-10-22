---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/git
  - origen/complemento
prerrequisitos:
  - "[[09 - Git: conceptos básicos y flujo de trabajo]]"
---

# Commits como versiones completas y muñecas rusas

Una de las dudas más frecuentes al empezar con Git es pensar que cada versión solo guarda el archivo que se acaba de modificar. En realidad, Git captura una fotografía (*snapshot*) del **estado completo del proyecto**. Esta nota explica el modelo mental correcto mediante la analogía de las muñecas rusas y el cambio de paradigma frente a las entregas tradicionales.

## ¿Qué contiene realmente un commit?

Muchos estudiantes se preguntan: *"Si en el último commit solo agregué `README.md`, ¿alguien que descargue ese commit solo obtendrá ese archivo?"*

La respuesta es **no**. Cada commit en Git registra el estado de **todos los archivos** del proyecto en ese instante preciso.

## La analogía de la muñeca rusa (Matryoshka)

Una forma visual de entender cómo se apilan los commits es compararlos con muñecas rusas (*matryoshkas*), donde cada muñeca más grande contiene a todas las anteriores en su interior.

![Commits como muñecas rusas](adjuntos/Commits%20como%20mu%C3%B1ecas%20rusas.png)

> [!example]- Transcripción de la imagen
> - Cuatro muñecas rusas de tamaño creciente, conectadas cronológicamente con flechas:
>   1. **Primer commit (más pequeña):** contiene únicamente `main.py`.
>   2. **Segundo commit:** agrega `utils.py` y se importan sus funciones en `main.py`.
>   3. **Tercer commit:** corrige un error en una función de `utils.py`.
>   4. **Cuarto commit (más grande):** agrega `README.md`.
> - Tabla inferior que detalla los cambios realizados en cada uno de los cuatro pasos.

### El último commit encapsula todo

Cuando descargas o clonas un proyecto, no recibes un fragmento suelto, sino la muñeca exterior completa con todo el contenido histórico preservado en su interior:

![El último commit contiene todo el proyecto](adjuntos/El%20%C3%BAltimo%20commit%20contiene%20todo%20el%20proyecto.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, la muñeca azul más grande cerrada (el último commit).
> - Una flecha hacia la derecha muestra cómo al abrirla se revelan las tres muñecas internas apiladas de los commits previos.
> - Representa que el commit final contiene el proyecto completo y todo su historial de cambios.

## El cambio de paradigma: Git no es Canvas

Al entregar una tarea en una plataforma como Canvas o Webcursos, se sube un archivo comprimido (`.zip`) con todos los archivos juntos cuando el trabajo ya está terminado. Si olvidas incluir un archivo, la entrega queda incompleta.

En Git la lógica es distinta:
- Un commit **no es una entrega final**, sino un **punto de control** en la evolución del programa.
- Puedes (y debes) hacer commits con partes individuales del proyecto, incluso si todavía están a medio terminar.
- Cada commit conserva intactos todos los archivos anteriores; no hay riesgo de perder código por hacer commits pequeños.

> [!tip] Haz commits pequeños y seguidos
> Trabajar con commits frecuentes tiene grandes ventajas: si introduces un error, puedes comparar exactamente qué líneas cambiaron o volver al punto anterior en segundos sin perder horas de trabajo.

## Preguntas de repaso

> [!question]- ¿Por qué al clonar un repositorio obtienes todos los archivos de commits pasados y no solo lo último que se subió?
> Porque cada commit representa una instantánea completa del proyecto y Git descarga el historial completo de versiones.

> [!question]- ¿Qué ventaja tiene hacer commits frecuentes en lugar de uno solo al final de la tarea?
> Permite registrar el avance de forma ordenada, identificar exactamente cuándo se introdujo un error y recuperar versiones previas funcionales en caso de fallas graves.

> [!question]- En la analogía de la muñeca rusa, ¿qué representa la muñeca más grande?
> Representa el último commit realizado, el cual encapsula todos los archivos y cambios acumulados desde el inicio del proyecto.
