---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/terminal
  - origen/complemento
prerrequisitos:
  - "[[06 - Navegación de directorios y pathlib]]"
---

# La terminal: comandos y navegación

Aunque los entornos gráficos permiten hacer muchas operaciones haciendo clic, la **terminal** o consola es una herramienta indispensable para el desarrollo de software. Permite ejecutar programas, automatizar tareas y controlar con precisión desde qué carpeta se ejecutan los scripts. Esta nota explica el funcionamiento básico de la línea de comandos y las instrucciones esenciales de navegación.

## Por qué usar la terminal en programación avanzada

En este curso la terminal ofrece dos ventajas decisivas frente al botón de ejecución de un editor:

1. **Control del directorio de trabajo:** permite saber con total certeza cuál es la carpeta activa, evitando confusiones y errores con las rutas relativas.
2. **Ejecución simultánea:** permite abrir múltiples terminales para correr programas en paralelo (por ejemplo, un servidor en una ventana y varios clientes en otras).

## Formato general de un comando

Cualquier comando en la terminal sigue una estructura común:

$$\text{comando} \quad [\text{argumentos}] \quad [-\text{opciones}]$$

- **Comando:** el nombre del programa a ejecutar (`pwd`, `cd`, `python3`, `pip`).
- **Argumentos:** datos o valores sobre los que actúa el comando (por ejemplo, el nombre de una carpeta o de un archivo).
- **Opciones o *flags*:** modificadores que alteran el comportamiento del comando, precedidos por `-` o `--` (por ejemplo, `-q` para instalación silenciosa en `pip install pyqt6 -q`).

## Comandos básicos: Unix frente a Windows

| Acción | Linux y macOS (Unix) | Windows (CMD) |
|---|---|---|
| Ver la carpeta actual | `pwd` (*print working directory*) | `cd` (sin argumentos) |
| Cambiar de directorio | `cd <ruta>` | `cd <ruta>` |
| Subir a la carpeta madre | `cd ..` | `cd ..` |
| Listar contenidos | `ls` | `dir` |
| Crear una carpeta | `mkdir <nombre>` | `mkdir <nombre>` |
| Crear un archivo vacío | `touch <archivo>` | `echo "" > <archivo>` |

### Navegar con `.` y `..`

- `.` representa el **directorio actual**.
- `..` representa el **directorio superior** (la carpeta contenedora).

Si te encuentras en `/home/pedro/libros`:

```bash
pwd
# Muestra: /home/pedro/libros

cd ..
pwd
# Muestra: /home/pedro

cd ../../data
pwd
# Muestra: /data
```

> [!tip] La tecla Tab es tu aliada
> En cualquier terminal moderna, escribir las primeras letras del nombre de un archivo o carpeta y presionar **Tab** autocompleta el nombre automáticamente. Si hay varias opciones, presionar Tab dos veces muestra la lista de coincidencias.

## Preguntas de repaso

> [!question]- ¿Qué responde el comando `pwd` en sistemas Unix?
> Entrega la ruta absoluta completa del directorio donde se encuentra ubicada la terminal en ese momento (*working directory*).

> [!question]- Si estás en la carpeta `proyecto/codigo`, ¿a dónde te lleva el comando `cd ../datos`?
> Sube a la carpeta `proyecto` (con `..`) y desde allí entra a la carpeta vecina `datos`.

> [!question]- ¿Por qué es fundamental dominar la terminal para temas como redes o concurrencia?
> Porque permite levantar de forma independiente y simultánea distintos procesos (como un servidor y múltiples clientes) y observar sus salidas por separado.
