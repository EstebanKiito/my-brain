---
ramo: "Programación en C"
tema: "Módulos, compilación y depuración"
tags:
  - c
  - modulos
  - headers
  - static
  - origen/complemento
prerrequisitos:
  - "[[04 - Funciones y stack de llamadas]]"
  - "[[04 - Structs como objetos y tipos compuestos]]"
---

# Archivos de cabecera, include y static

Un programa real no cabe en un solo archivo. C lo divide en **módulos**, cada uno formado por dos archivos: un **header** `.h`, que dice **qué** ofrece el módulo, y un `.c`, que dice **cómo** lo hace. Es la misma distinción entre [[04 - Funciones y stack de llamadas|declarar y definir]]: el `.h` declara y el `.c` define.

## Qué va en cada archivo

![Qué va en modulo.h y en modulo.c](adjuntos/Qu%C3%A9%20va%20en%20modulo.h%20y%20en%20modulo.c.png)

> [!example]- Transcripción de la imagen
> Dos archivos. `modulo.h`: "1. Declaración de funciones externas; 2. Definición de tipos públicos; 3. etc." `modulo.c`: "1. Definición de funciones externas; 2. Definición de funciones internas; 3. etc."

- **`.h` (interfaz pública):** los `typedef` de los structs que el usuario necesita y las **declaraciones** de las funciones que puede llamar.
- **`.c` (implementación):** las **definiciones** de esas funciones y de las **funciones internas**, que el usuario no ve.

![Módulo de lista ligada en list.h y list.c](adjuntos/M%C3%B3dulo%20de%20lista%20ligada%20en%20list.h%20y%20list.c.png)

> [!example]- Transcripción de la imagen
> `list.h`: `struct list { int value; struct list* next; };`, `typedef struct list List;` y las declaraciones de `list_init`, `list_append`, `list_at_index` y `list_destroy`. `list.c`: `#include "list.h"`, `static void aux_func(){ ... }` y las definiciones de las cuatro funciones públicas.

## `#include`: copiar y pegar

`#include` no "importa" como en Python: **reemplaza la línea por el contenido completo** del archivo antes de compilar.

| Forma | Busca el archivo en | Uso |
|---|---|---|
| `#include <stdio.h>` | Las bibliotecas instaladas en el sistema | Bibliotecas estándar (*globales*) |
| `#include "list.h"` | La carpeta del archivo actual (acepta rutas relativas) | Módulos propios (*locales*) |

> [!warning] Nunca `#include "modulo.c"`
> Incluir un `.c` es como el `from modulo import *` de Python, pero peor: copia **todas** las definiciones, incluidas las internas, en cada archivo que lo incluya. Si dos archivos lo hacen, la misma función queda definida dos veces y el enlazado falla. Siempre se incluye el `.h`.

## `static`: funciones privadas del módulo

Anteponer `static` a una función le dice al compilador que **solo existe dentro de su `.c`**. Es la herramienta para las funciones auxiliares, que no forman parte de la interfaz:

```c
// contador.c
#include <stdlib.h>
#include "contador.h"

static void registrar_paso(Contador* c)   // invisible fuera de contador.c
{
    c->pasos += 1;
}

void contador_sumar(Contador* c, int n)   // declarada en contador.h: pública
{
    c->valor += n;
    registrar_paso(c);
}
```

Si `main.c` intenta llamar a `registrar_paso`, aunque la declare a mano, el enlazador falla con *undefined symbols*: la función no es visible desde afuera.

> [!tip] Regla de diseño
> El `.h` debe ser lo más pequeño posible: solo lo que el usuario necesita. Todo lo demás va en el `.c`, y las funciones auxiliares van marcadas con `static`. Así la implementación se puede cambiar sin tocar a quienes usan el módulo.

## Preguntas de repaso

> [!question]- ¿Qué hace realmente `#include "list.h"`?
> Antes de compilar, reemplaza esa línea por todo el texto de `list.h`, con sus tipos y declaraciones. Así el compilador conoce las funciones de la lista sin ver su implementación.

> [!question]- ¿Por qué el `.h` lleva declaraciones y no definiciones de funciones?
> Porque el `.h` se incluye en muchos archivos. Si tuviera definiciones, cada uno tendría una copia del cuerpo y el enlazador encontraría la misma función definida varias veces. Las declaraciones, en cambio, se pueden repetir sin conflicto.

> [!question]- ¿Qué diferencia hay entre `#include <x.h>` y `#include "x.h"`?
> Con `< >` se busca entre las bibliotecas instaladas en el sistema. Con comillas se busca primero en la carpeta del archivo actual, y es la forma de incluir módulos propios.

> [!question]- ¿Para qué sirve declarar una función como `static` dentro de un `.c`?
> Para que solo sea visible dentro de ese archivo. Queda como función interna del módulo y no choca con otras funciones del mismo nombre en otros archivos.
