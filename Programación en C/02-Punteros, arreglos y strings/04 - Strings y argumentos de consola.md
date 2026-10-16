---
ramo: "Programación en C"
tema: "Punteros, arreglos y strings"
tags:
  - c
  - strings
  - argv
  - null-terminator
  - origen/complemento
prerrequisitos:
  - "[[03 - Aritmética de punteros y arreglos]]"
---

# Strings y argumentos de consola

**En C no existe un tipo string.** Un texto es un **arreglo de `char`**, y como los arreglos no saben su largo, hace falta otra forma de saber dónde termina: un carácter especial al final, el **null terminator** `'\0'`. Todo lo que trabaja con strings, como `printf("%s")` o `strlen`, avanza hasta encontrarlo.

## El null terminator: el "disco pare"

Sin `'\0'`, `printf` no sabe cuándo detenerse y sigue imprimiendo la memoria contigua:

```c
char a[2] = {'I', 'm'};
char b[6] = {'S', 't', 'r', 'i', 'n', 'g'};
printf("%s %s", a, b);   // puede imprimir "ImString String": a no termina y se "come" a b
```

Un **string literal** entre comillas dobles agrega el `'\0'` automáticamente: `"Hola"` ocupa 5 bytes. Hay tres formas de crear un string:

| Declaración | Qué es | ¿Se puede modificar? |
|---|---|---|
| `char a[5] = "Hola";` | Arreglo de 5 (4 letras + `'\0'`) | Sí |
| `char b[] = "como";` | El compilador calcula el largo (5) | Sí |
| `char* c = "estas?";` | Puntero a un literal constante | **No** |

> [!warning] `char A[4] = "Hola"` no tiene espacio para el `'\0'`
> Siempre hay que reservar **largo + 1**. Y modificar un literal apuntado por `char*` (`c[0] = 'E';`) es comportamiento indefinido: normalmente termina en *segmentation fault*.

## Strings en funciones

Una función recibe el string como `char*` y puede recorrerlo hasta el `'\0'`, sin necesidad de recibir el largo:

```c
void replace(char* string, char from, char to)
{
    for (int i = 0; string[i] != '\0'; i += 1)
        if (string[i] == from) string[i] = to;
}

char s[] = "Sorry";      // arreglo propio: se puede modificar
replace(s, 'r', 'w');
printf("%s\n", s);       // Sowwy
```

Con la misma idea se escribe una búsqueda: `bool contains(char* s, char c)` recorre hasta `'\0'` y retorna `true` apenas encuentra `c`. Para medir el largo está `strlen` (de `<string.h>`), que no cuenta el `'\0'`: `strlen("como")` es 4, aunque el arreglo ocupe 5 bytes.

## Argumentos de consola: `argv`

`char** argv` es un **arreglo de strings**: un arreglo de punteros, cada uno al primer `char` de un argumento. `argv[0]` es siempre el nombre del ejecutable.

![Imprimir los argumentos de consola](adjuntos/Imprimir%20los%20argumentos%20de%20consola.png)

> [!example]- Transcripción de la imagen
> `main` imprime "Recibi %d argumentos:" con `argc` y después cada `argv[i]` con un tab. Al ejecutar `./main Hello World!` la salida es "Recibi 3 argumentos:", seguida de `./main`, `Hello` y `World!`.

**Todos los argumentos son strings**, aunque parezcan números. Asignar `argv[2]` a un `int` guarda la dirección del texto, no el número:

![Argumento numérico leído sin atoi](adjuntos/Argumento%20num%C3%A9rico%20le%C3%ADdo%20sin%20atoi.png)

> [!example]- Transcripción de la imagen
> `char* string = argv[1]; int number = argv[2]; printf("%s %d\n", string, number);`. Con `./main cien 100` imprime `cien -1034752593`: un número sin sentido, que es parte de la dirección del string "100" leída como entero.

La solución es convertir con `atoi` (de `<stdlib.h>`):

![Argumento numérico convertido con atoi](adjuntos/Argumento%20num%C3%A9rico%20convertido%20con%20atoi.png)

> [!example]- Transcripción de la imagen
> El mismo programa con `int number = atoi(argv[2]);`. Con `./main cien 100` ahora imprime `cien 100`.

## Preguntas de repaso

> [!question]- ¿Cuántos bytes ocupa `"Hola"` y por qué?
> 5: las 4 letras más el null terminator `'\0'` que el compilador agrega a todo string literal.

> [!question]- ¿Por qué `replace` puede recorrer el string sin recibir su largo, a diferencia de `sum` con arreglos de `int`?
> Porque un string termina en `'\0'`, que funciona como marca de fin. Un arreglo de `int` no tiene marca, así que su largo hay que pasarlo aparte.

> [!question]- ¿Qué diferencia hay entre `char s[] = "Sorry";` y `char* s = "Sorry";`?
> El primero crea un arreglo propio con una copia del texto, que se puede modificar. El segundo es un puntero a un literal constante: escribir en él es comportamiento indefinido.

> [!question]- ¿Por qué `int number = argv[2];` no entrega el número que se escribió en la consola?
> Porque `argv[2]` es un `char*`. Se estaría guardando una dirección convertida a entero, no el valor numérico del texto. Hay que convertirlo con `atoi(argv[2])`.
