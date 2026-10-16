---
ramo: "Programación en C"
tema: "Fundamentos del lenguaje"
tags:
  - c
  - compilacion
  - gcc
  - main
  - origen/complemento
prerrequisitos: []
---

# Estructura y compilación de un programa en C

C es un lenguaje **compilado**: antes de ejecutarse, el código fuente se traduce completo a lenguaje de máquina. Python, en cambio, interpreta el código mientras lo ejecuta. Compilar tiene un costo inicial, pero el ejecutable que resulta corre mucho más rápido. Esa es la razón por la que C se usa para implementar estructuras de datos eficientes y sistemas operativos.

## El programa mínimo

```c
#include <stdio.h>

int main(int argc, char** argv)
{
    printf("Hola mundo! Recibí %d argumento(s); el primero es %s\n", argc, argv[0]);
    return 0;
}
```

- `#include <stdio.h>` es el equivalente a un `import`. Trae la biblioteca *standard input-output*, donde está `printf`, que no viene por defecto.
- `int main(...)` es la función que se ejecuta al correr el programa. El código puede tener otras funciones definidas al mismo nivel, pero el programa siempre parte por `main`. El `int` delante de `main` es el tipo de lo que retorna.
- `argc` es la **cantidad de argumentos** recibidos por consola y `argv` es el arreglo con esos argumentos como strings. El primero, `argv[0]`, siempre es el nombre del ejecutable. Estos argumentos se ven en detalle junto con los strings, en el tema de punteros.
- `return 0;` le avisa al sistema operativo que el programa **terminó bien**. Cualquier otro valor (de 1 a 255) es un código de error.
- `printf` no agrega el salto de línea: hay que escribir `\n` de forma explícita.

> [!tip] Regla de C
> Toda variable y toda función tiene un **tipo explícito que no cambia** durante la ejecución. Saber los tipos de antemano es lo que le permite al compilador optimizar el código.

## Compilar y ejecutar

```bash
gcc hola.c -o hola      # compila hola.c y deja el ejecutable "hola" (-o = output)
./hola uno dos          # ejecuta "hola" de la carpeta actual (./) con dos argumentos
# Hola mundo! Recibí 3 argumento(s); el primero es ./hola
```

El programa recibió 3 argumentos porque el nombre del ejecutable cuenta como uno. Si el ejecutable no existe o quedó desactualizado, hay que volver a compilar: **cada cambio en el `.c` exige recompilar**.

```mermaid
flowchart LR
    A["hola.c<br/>(código fuente)"] -->|gcc hola.c -o hola| B["hola<br/>(ejecutable)"]
    B -->|./hola| C["Proceso en ejecución"]
    C -->|return 0| D["Código de salida al SO"]
```

En proyectos con varios archivos no se escribe `gcc` a mano. Se usa `make`, que lee un `Makefile` y compila solo lo que cambió (se ve en el tema de módulos y compilación). Cuando el ejecutable queda "sucio" por compilaciones anteriores, `make clean && make` recompila desde cero.

> [!warning] Detalles que hacen caer un programa
> - Usar siempre `int main()` y retornar `0`. Otra firma puede hacer que un corrector automático marque error aunque el programa funcione.
> - Comparar `float` con `==` es poco confiable por las imprecisiones de punto flotante. Cuando se pueda, conviene trabajar con enteros.

## Preguntas de repaso

> [!question]- ¿Qué diferencia práctica hay entre un lenguaje compilado como C y uno interpretado como Python?
> En C, todo el código se traduce a lenguaje de máquina antes de ejecutarse, y se obtiene un ejecutable rápido. Por lo mismo, cada cambio exige recompilar. Python traduce el código mientras lo ejecuta: no hay ese paso previo, pero corre más lento.

> [!question]- Si se ejecuta `./main a b c`, ¿cuánto vale `argc` y qué hay en `argv[0]`?
> `argc` vale 4, porque el nombre del ejecutable también cuenta, y `argv[0]` es `"./main"`.

> [!question]- ¿Para qué sirve el `return 0` de `main`?
> Es el código de salida que recibe el sistema operativo. Un 0 indica que el programa terminó bien, y cualquier otro valor indica un error.

> [!question]- ¿Por qué hay que escribir `#include <stdio.h>` para usar `printf`?
> Porque `printf` no es parte del núcleo del lenguaje sino de la biblioteca estándar de entrada y salida. El `#include` inserta sus declaraciones para que el compilador conozca la función.
