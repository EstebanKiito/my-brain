---
ramo: "Programación en C"
tema: "Fundamentos del lenguaje"
tags:
  - c
  - funciones
  - stack
  - memoria
  - origen/complemento
prerrequisitos:
  - "[[03 - Control de flujo y valores de verdad en C]]"
---

# Funciones y stack de llamadas

Una función en C declara el tipo de lo que retorna, su nombre y el tipo de cada parámetro. Para usar bien punteros y memoria dinámica hay que entender **dónde viven las variables de una función** mientras se ejecuta: en el **stack**, una zona de memoria que crece con cada llamada y retrocede con cada retorno.

## Firma, `void`, declarar y definir

```c
tipo_salida nombre(tipo_1 arg_1, ..., tipo_n arg_n)
{
    // código
    return ...;
}
```

Una función que no retorna nada se declara con tipo **`void`**. Además, C distingue entre dos operaciones:

- **Declarar** es anunciar que algo existe, con su nombre y sus tipos: `int foo(int bar);` o `int foo(int);` (el nombre del parámetro es opcional). Se puede declarar varias veces, siempre que no haya conflicto.
- **Definir** es escribir el contenido, y se hace **una sola vez**.

La diferencia importa porque el compilador lee el archivo de arriba hacia abajo: para llamar a una función antes de su definición, basta con haberla declarado. Esto es lo que más adelante permite repartir el código en varios archivos (`.h` y `.c`).

```c
#include <stdio.h>

int div_count(int n);            // declaración: nombre y tipos

int main(void)
{
    printf("%d\n", div_count(4)); // 3 (1, 2 y 4)
    return 0;
}

int div_count(int n)             // definición: el cuerpo
{
    int count = 0;
    for (int i = 1; i <= n; i += 1)
        if (n % i == 0) count += 1;
    return count;
}
```

## El stack de llamadas

> [!info] Video
> El curso explica funciones y stack en este [video](https://www.loom.com/share/d6b049ddb12a4e9ca2ad99da017c28bf).

Todo el programa está en la RAM: los tipos y constantes, el código de las funciones y el **stack**. El stack guarda, para cada llamada activa, sus parámetros y **variables locales**, e incluso las de cada bloque `{ }`, como las de un `for` o un `if`. Un **stack pointer** (SP) marca hasta dónde está ocupado.

Supongamos que `main` llama a `r`, que `r` llama a `q` y después a `p`, y que `q` también llama a `p`:

![Stack con main y r activos](adjuntos/Stack%20de%20llamadas%20con%20main%20y%20r%20activos.png)

> [!example]- Transcripción de la imagen
> "STACK de memoria". A la izquierda, el código: `int p(...)`, `int q(...)` ("llama a p"), `int r(...)` ("llama a q y a p") e `int main()` ("llama a r"). A la derecha, la RAM tiene tres zonas: "tipos, constantes, etc", "funciones" (p, q, r, main) y "STACK". En el stack están activos "(main) variables en main" y "(r) variables en r", con la flecha SP justo debajo. Más abajo, en gris, quedan "(q) variables en q" y "(p) variables en p" de llamadas que ya retornaron.

Al retornar, la función **no borra** lo que escribió: el SP solo retrocede, y esos datos quedan como basura que la próxima llamada sobrescribe. Cuando `r` llama a `p`, el marco de `p` ocupa el espacio que antes usaba `q`:

![Stack cuando r llama a p](adjuntos/Stack%20de%20llamadas%20cuando%20r%20llama%20a%20p.png)

> [!example]- Transcripción de la imagen
> El mismo esquema, con `int p(...)` resaltado. El stack contiene "(main) variables en main", "(r) variables en r" y "(p) variables en p", con el SP debajo de p. Más abajo, en gris, se ve un "(p) variables en p" anterior que quedó sin borrar.

![Stack al terminar el programa](adjuntos/Stack%20de%20llamadas%20al%20terminar%20el%20programa.png)

> [!example]- Transcripción de la imagen
> Todo el código está en gris y el SP subió hasta el inicio del stack, justo bajo la zona de funciones. Las entradas de main, r y p siguen escritas pero en gris: el programa terminó y el stack quedó libre, aunque con los datos viejos.

Con un caso concreto, la llamada `div_count(4)` crea un marco con `n = 4` y `count`. Dentro, el `for` agrega `i`, y el `if` su propio contexto:

![Stack de div_count](adjuntos/Stack%20de%20llamadas%20de%20div_count.png)

> [!example]- Transcripción de la imagen
> Código de `div_count(int n)` con `return count;` resaltado y el comentario "Llama a div_count con n = 4 / int main();". En la RAM, la zona de funciones tiene div_count y main. El stack tiene "(main) variables en main", "(div_count)", `n = 4` y `count = 3`, con el SP justo debajo. En gris quedan "(for)", `i = 5` e "(if)", los contextos que ya terminaron.

> [!warning] Consecuencia directa
> Como el marco de una función se libera al retornar, **nunca se debe retornar la dirección de una variable local**: apunta a memoria que la próxima llamada va a sobrescribir. Para que un dato sobreviva a la función hay que pedirlo al *heap* (memoria dinámica).

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre declarar y definir una función, y cuántas veces se puede hacer cada una?
> Declarar es anunciar el nombre y los tipos, y se puede repetir sin conflicto. Definir es escribir el cuerpo, y se hace una sola vez. Declarar permite usar la función antes de su definición o desde otro archivo.

> [!question]- ¿Qué pasa con las variables locales de una función cuando esta retorna?
> El stack pointer retrocede y ese espacio queda libre. Los bytes no se borran, pero la próxima llamada los sobrescribe, así que ya no se puede confiar en ellos.

> [!question]- En el ejemplo de `main → r → q → p` y luego `r → p`, ¿dónde queda el marco del segundo `p`?
> En el mismo espacio del stack que antes ocupaba `q`, justo después del marco de `r`, porque `q` ya había retornado.

> [!question]- ¿Por qué es un error retornar un puntero a un arreglo local?
> Porque el arreglo vive en el marco de la función, que se libera al retornar. El puntero queda apuntando a memoria que otras llamadas van a reutilizar, y el comportamiento es indefinido.
