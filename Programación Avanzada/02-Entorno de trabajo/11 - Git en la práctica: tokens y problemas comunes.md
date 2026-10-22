---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/git
  - origen/complemento
prerrequisitos:
  - "[[10 - Commits como versiones completas y muñecas rusas]]"
---

# Git en la práctica: tokens y problemas comunes

Al utilizar Git en el semestre, la interacción con repositorios remotos en GitHub presenta ciertas exigencias de seguridad y situaciones que pueden trabar a un principiante. Esta nota explica cómo funciona la autenticación con tokens de acceso personal, los problemas más habituales y las buenas prácticas para evitar contratiempos.

## Autenticación con Token de Acceso Personal (PAT)

Por motivos de seguridad, GitHub no permite autenticarse desde la terminal usando la contraseña tradicional de la cuenta. En su lugar exige un **Token de Acceso Personal** (*Personal Access Token* o **PAT**).

El token es una cadena alfanumérica secreta (que comienza con `ghp_`) que actúa como contraseña temporal con permisos restringidos. Se genera desde la configuración de GitHub (`Settings > Developer Settings > Personal Access Tokens > Tokens (classic)`):
1. Se define una descripción (*Note*).
2. Se asigna una fecha de expiración (por ejemplo, al finalizar el semestre).
3. Se seleccionan los permisos de repositorios (marcando la casilla `repo`).

> [!warning] El token se muestra una sola vez
> Al crear el token, GitHub lo muestra una única vez en pantalla. Hay que copiarlo y guardarlo en un lugar seguro. Si se pierde, no se puede recuperar y se debe generar uno nuevo. Al pegarlo en la terminal, los caracteres no se muestran por seguridad.

## Problemas comunes y cómo resolverlos

### 1. Repositorio des-sincronizado

Ocurre cuando el repositorio remoto tiene commits que aún no existen en tu computador local (por ejemplo, si editaste el `README.md` directamente desde la página web de GitHub o si avanzaste código en otro equipo).

Al intentar hacer `git push`, la terminal rechaza la subida con un error como:

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
```

**Solución:** integrar primero los cambios remotos ejecutando `git pull`. Una vez que el historial local contenga lo nuevo de la nube, `git push` funcionará sin problemas.

### 2. Conflictos de fusión (*merge conflicts*)

Si se modificó la misma línea de un archivo tanto en el computador como en GitHub, Git no puede decidir cuál versión debe conservarse y detiene el proceso solicitando intervención humana. En la terminal y en los editores de código aparecerán marcas (`<<<<<<< HEAD`, `=======`, `>>>>>>>`) que delimitan ambos cambios para que el programador elija cuál conservar.

### 3. Archivos pesados (límite de 100 MB)

GitHub prohíbe de forma automática subir archivos individuales que pesen más de **100 MB**. Los repositorios de código están pensados para texto, no para videos, modelos gigantescos o archivos `.zip`.

El peligro radica en que Git sí permite hacer `git add` y `git commit` con un archivo pesado en tu máquina. El error salta recién al hacer `git push`:

```
remote: error: File 300MB.zip is 300.00 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected.
```

> [!warning] Borrar el archivo después del commit no basta
> Si hiciste un commit con un archivo de más de 100 MB, simplemente borrar el archivo y hacer otro commit no soluciona el problema: el archivo sigue existiendo en el historial del commit anterior y GitHub continuará rechazando el push.

### Solución de emergencia para estudiantes

Si tu repositorio queda bloqueado por un conflicto complejo o un archivo pesado en el historial, la estrategia más segura y rápida recomendada por el curso es:

1. En otra carpeta de tu computador, clona una copia limpia del repositorio con `git clone`.
2. Desde la carpeta problemática antigua, copia únicamente los archivos de código que quieras conservar y pégalos en la copia recién clonada.
3. En la copia limpia, ejecuta `git add`, `git commit` y `git push`.
4. Tras verificar en la página de GitHub que todo tu avance está seguro, elimina la carpeta antigua con errores.

## Buenas prácticas para el semestre

- **Sincroniza siempre:** haz `git pull` al iniciar una jornada de trabajo y `git push` al terminarla.
- **No edites en la web:** evita modificar código o el `README.md` desde la interfaz de GitHub en el navegador.
- **Commits frecuentes:** avanza paso a paso para evitar entregas atrasadas por inconvenientes de última hora.

## Preguntas de repaso

> [!question]- ¿Por qué GitHub exige un token de acceso personal (PAT) en vez de la contraseña habitual?
> Porque los tokens ofrecen mayor seguridad al tener alcance restringido (solo los permisos necesarios) y fecha de expiración, sin exponer la contraseña maestra de la cuenta.

> [!question]- ¿Por qué falla un `git push` si previamente modificaste un archivo desde la página web de GitHub?
> Porque el repositorio remoto tiene commits nuevos que no están en tu computador local. Hay que hacer `git pull` para sincronizar antes de poder subir.

> [!question]- Si se hizo un commit con un archivo de 200 MB, ¿por qué no basta con borrar el archivo y hacer otro commit?
> Porque Git guarda el historial completo: el archivo de 200 MB sigue empaquetado en el commit anterior, y al hacer `push` Git intentará enviar todo el historial a GitHub.
