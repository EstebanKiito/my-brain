---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/git
  - origen/complemento
prerrequisitos:
  - "[[08 - Ejecutar Python en terminal y directorio de trabajo]]"
---

# Git: conceptos básicos y flujo de trabajo

En proyectos de programación es común querer guardar versiones seguras del trabajo, volver atrás cuando algo se rompe o colaborar con otros sin sobrescribir código ajeno. **Git** es un sistema de **control de versiones** que registra la evolución de los archivos a lo largo del tiempo. Esta nota explica sus cuatro áreas principales y el flujo de trabajo básico.

## Las cuatro áreas de Git

Al trabajar con Git, los archivos transitan entre cuatro ubicaciones lógicas:

1. **Mi computador (directorio de trabajo):** los archivos que ves y editas en tu editor o explorador.
2. **Lista de cambios (*staging area*):** el espacio donde seleccionas qué modificaciones formarán parte de la próxima versión.
3. **Repositorio local:** la base de datos dentro de la carpeta oculta `.git` en tu máquina, donde quedan registradas todas las versiones confirmadas.
4. **Repositorio remoto:** la copia almacenada en un servidor en la nube (como GitHub).

## El viaje de un archivo: add, commit y push

Imagina que creas un archivo nuevo (representado en color morado) en tu computador:

![Archivo nuevo solo en mi computador](adjuntos/Git%20-%20archivo%20nuevo%20solo%20en%20mi%20computador.png)

> [!example]- Transcripción de la imagen
> - Esquema con dos columnas: «Mi computador» a la izquierda y «GitHub» a la derecha.
> - En el computador hay tres archivos: dos en la parte superior y un archivo morado nuevo.
> - En GitHub solo existen los dos archivos originales; el archivo morado todavía no tiene seguimiento por parte de Git.

### 1. Seleccionar cambios con `git add`

Para avisar a Git qué archivos deben incluirse en la siguiente versión, se usa `git add`:

```bash
git add README.md
```

![Archivo en la lista de cambios tras git add](adjuntos/Git%20-%20archivo%20en%20la%20lista%20de%20cambios.png)

> [!example]- Transcripción de la imagen
> - Aparece una columna intermedia: «Lista de cambios (Staging area)».
> - El archivo morado pasa a la lista de cambios mediante una flecha que representa `git add`.
> - El archivo aún no forma parte de una versión guardada en el repositorio.

### 2. Registrar la versión con `git commit`

Un **commit** empaqueta todo lo que estaba en el *staging area* y crea una versión inmutable con fecha, autor y un mensaje explicativo:

```bash
git commit -m "Agrega documentación inicial del proyecto"
```

![Archivo en el repositorio local tras git commit](adjuntos/Git%20-%20archivo%20en%20el%20repositorio%20local.png)

> [!example]- Transcripción de la imagen
> - Se incorpora la columna «Repositorio local».
> - La lista de cambios se vacía y el archivo morado pasa a estar guardado dentro del historial local del repositorio.
> - En GitHub todavía no aparece esta nueva versión.

### 3. Publicar cambios con `git push`

Para sincronizar las versiones locales con el servidor en la nube, se ejecuta `git push`:

```bash
git push
```

![Archivo en el repositorio remoto tras git push](adjuntos/Git%20-%20archivo%20en%20el%20repositorio%20remoto.png)

> [!example]- Transcripción de la imagen
> - El archivo morado finalmente se copia al «Repositorio remoto (GitHub)».
> - Las cuatro columnas quedan en sincronía.

## Los 5 comandos esenciales

| Comando | Qué hace |
|---|---|
| `git clone <url>` | Descarga una copia completa de un repositorio remoto a tu máquina |
| `git pull` | Descarga los cambios nuevos desde GitHub a tu repositorio local |
| `git add <archivo>` | Pasa modificaciones al área de preparación (*staging area*) |
| `git commit -m "..."` | Guarda una versión definitiva en el repositorio local |
| `git push` | Sube los commits locales al repositorio en GitHub |

> [!tip] Usa `git status` constantemente
> Antes y después de ejecutar cualquier comando de Git, corre `git status`. Te dirá en qué rama estás, qué archivos fueron modificados, cuáles están listos para commit y te sugerirá el siguiente paso.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `git add` y `git commit`?
> `git add` solo selecciona los archivos que se quieren incluir en la próxima entrega (*staging area*); `git commit` sella efectivamente esa entrega y crea una nueva versión en el historial.

> [!question]- Si haces `git commit`, ¿los ayudantes o tu equipo ya pueden ver los cambios en GitHub?
> No. `commit` solo guarda la versión en el repositorio local de tu computador. Para que llegue a la nube se debe ejecutar `git push`.

> [!question]- ¿Por qué es conveniente escribir mensajes de commit claros y descriptivos?
> Porque permiten entender qué cambió y por qué en cada momento al revisar el historial, facilitando encontrar errores y revertir cambios específicos.
