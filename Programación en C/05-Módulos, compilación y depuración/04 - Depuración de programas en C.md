---
ramo: "Programación en C"
tema: "Módulos, compilación y depuración"
tags:
  - c
  - depuracion
  - gdb
  - debugging
  - origen/complemento
prerrequisitos:
  - "[[03 - Make y Makefile]]"
  - "[[05 - Valgrind con valores no inicializados y accesos inválidos]]"
---

# Depuración de programas en C

A diferencia de Python, C casi nunca dice **qué** falló: un *segmentation fault* solo indica que el programa tocó memoria que no le correspondía. Por eso conviene depurar con un método ordenado, desde lo más simple (¿compila?) hasta lo más fino (seguir la ejecución línea por línea).

## 1. ¿Compila?

**El entorno.** Hacen falta `gcc`, `make` y, para revisar memoria, `valgrind`. En macOS, `gcc` y `make` vienen con `xcode-select --install`, y Valgrind se usa dentro de un contenedor Docker. En Windows, lo recomendado es trabajar en Linux con WSL. Algunos mensajes típicos de `make`:

| Mensaje | Causa |
|---|---|
| `No targets specified and no makefile found` | La terminal no está en la carpeta del proyecto |
| `gcc: not found` / `make: command not found` | Falta instalar la herramienta |
| `cannot execute binary file: Exec format error` | Ejecutable de otra compilación: `make clean && make` |

**Leer el error del compilador.** El formato es `archivo:línea:columna: error: mensaje`:

```text
src/ratatouille/main.c:63:3: error: expected ',' or ';' before 'FILE'
src/ratatouille/main.c:179:17: error: 'output_file' undeclared (first use in this function)
```

El primer error está en la línea 63, pero la causa real es un `;` faltante en la **línea anterior**. Ese error provocó el segundo: `output_file` nunca se declaró. En C muchos errores son **"de arrastre"**, así que hay que corregir **de a uno, empezando por el primero**, y volver a compilar.

## 2. ¿Se cae al ejecutarse?

Las causas típicas de cada síntoma están en [[03 - Errores de memoria y memory leaks|errores de memoria]]. Las más frecuentes son estas:

```c
char* s = "hello world";  *s = 'H';          // segfault: modificar un literal
int* p = NULL;  printf("%d", *p);            // segfault: desreferenciar NULL
int n = 2;  scanf("%d", n);                  // segfault: scanf necesita &n
int foo(void) { return foo(); }              // stack overflow: recursión sin caso base
```

El siguiente paso es **Valgrind**, con el comando completo:

```bash
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes \
         --log-file=valgrind-out.txt ./programa input.txt output.txt
```

Corregir los errores de memoria que reporta suele resolver también los *segfaults* y los resultados raros.

## 3. Compila y no se cae, pero el resultado está mal

Aquí el código es sintácticamente correcto, pero la lógica falla. Es como escribir "échale jugo de naranja al motor": la instrucción está bien escrita, pero el auto no anda. La herramienta para estos casos es un **debugger**, como **gdb** en Linux o **lldb** en macOS, que ejecuta el programa de forma controlada:

- **Breakpoints:** puntos donde el programa se detiene. También pueden ser **condicionales** (por ejemplo, detenerse solo si `x > n`).
- **Paso a paso:** *Next* avanza una línea, *Step Into* entra a la función llamada y *Step Out* sale de ella.
- **Inspección:** muestra el valor de las variables y la **pila de llamadas** en ese instante, lo que resulta útil en recursiones.

En VS Code se usa con la extensión C/C++ y un archivo `.vscode/launch.json` que indica el ejecutable (`"program"`) y sus argumentos (`"args": ["input.txt", "output.txt"]`). Con F5 parte la depuración. Hay que compilar con `-g`, igual que para Valgrind.

> [!tip] Si el corrector automático dice que la respuesta está mal
> Comparar la salida del programa con la esperada usando `diff salida.txt esperado.txt`. Revisar que se escriba en el **archivo** de salida (`fprintf`) y no solo en la consola (`printf`), y que no quede código de depuración que altere la salida.

## Preguntas de repaso

> [!question]- ¿Por qué hay que corregir los errores de compilación empezando por el primero?
> Porque en C un error (por ejemplo, un `;` faltante) suele provocar otros más adelante. Al corregir el primero y recompilar, muchos de los siguientes desaparecen.

> [!question]- ¿Por qué `scanf("%d", n)` provoca un segmentation fault?
> Porque `scanf` necesita la dirección donde guardar el valor (`&n`). Recibe el valor de `n` (2) y lo usa como dirección, así que escribe en una zona de memoria inválida.

> [!question]- ¿Qué herramienta conviene usar en cada situación: no compila, se cae, o da un resultado incorrecto?
> Si no compila, se leen los mensajes del compilador en orden. Si se cae, se usa Valgrind para encontrar el error de memoria. Si da un resultado incorrecto, se usa un debugger con breakpoints para seguir la ejecución.

> [!question]- ¿Para qué sirve un breakpoint condicional?
> Para detener el programa solo cuando se cumple una condición (por ejemplo, en la iteración 5000 de un ciclo), sin tener que avanzar paso a paso por todas las anteriores.
