---
ramo: "Programación en C"
tema: "Structs"
tags:
  - c
  - structs
  - punteros
  - structs-recursivos
  - origen/complemento
prerrequisitos:
  - "[[02 - Punteros a structs y operador flecha]]"
---

# Structs anidados y structs recursivos

Un campo de un struct puede ser otro struct, ya sea **contenido** dentro de él o **referenciado** con un puntero. La diferencia define cuánta memoria ocupa el struct y si los datos se comparten o se copian. Cuando el struct se refiere a sí mismo (*recursivo*), el puntero es obligatorio, y esa es la base de las listas ligadas y los árboles.

## Struct dentro de struct: el otro struct está contenido

```c
struct dog  { char* name; double age; bool good_boy; };
struct kid  { char* name; struct dog dog; };       // el perro es PARTE del kid

struct kid matias = {
    .name = "matias",
    .dog = {.name = "bruno", .age = 3, .good_boy = true}
};
printf("%s tiene a %s\n", matias.name, matias.dog.name);
```

![Struct dentro de otro struct en memoria](adjuntos/Struct%20dentro%20de%20otro%20struct%20en%20memoria.png)

> [!example]- Transcripción de la imagen
> En la RAM, un bloque contiguo marcado "matias" con los campos `.name`, `.dog.name`, `.dog.age` y `.dog.good_boy`. Los tres últimos están agrupados además como "matias.dog": el perro está dentro del bloque de matias, no en otro lugar.

No hay ninguna referencia: el `dog` **es** parte del `kid`. Copiar a `matias` copia también al perro.

## Puntero a structs: el otro struct está en otra parte

```c
struct adult { char* name; struct dog* dogs; int dog_count; };   // guarda el largo

struct adult diego = {
    .name = "diego",
    .dogs = calloc(2, sizeof(struct dog)),     // arreglo de perros en el heap
    .dog_count = 2
};
diego.dogs[0] = (struct dog){"alan", 9, true};
diego.dogs[1] = (struct dog){"casi", 5, true};
// ... al terminar: free(diego.dogs);
```

![Struct con un arreglo de structs en el heap](adjuntos/Struct%20con%20un%20arreglo%20de%20structs%20en%20el%20heap.png)

> [!example]- Transcripción de la imagen
> A la izquierda, `struct dog` (`name`, `age`, `good_boy`) y `struct adult` (`name`, `dogs`, `dog_count`), y la inicialización de `diego` con `calloc(2, sizeof(struct dog))`. A la derecha, el bloque "diego" contiene `.dogs = 0x706cf4`, y en esa dirección hay otro bloque con dos perros seguidos (`.name`, `.age`, `.good_boy` dos veces).

Como un puntero puede apuntar al primero de varios structs contiguos, el campo `dogs` funciona como **arreglo**, y por eso hace falta guardar `dog_count`.

## Struct recursivo: solo con puntero

Un perro que tiene un amigo perro **no puede** contener un `struct dog` dentro:

```c
struct dog { char* name; struct dog friend; };   // error: field has incomplete type
```

![Struct recursivo de tamaño infinito](adjuntos/Struct%20recursivo%20de%20tama%C3%B1o%20infinito.png)

> [!example]- Transcripción de la imagen
> Un bloque de RAM que no termina nunca: `.name`, `.age`, `.good_boy`, `.friend.name`, `.friend.age`, `.friend.good_boy`, `.friend.friend.name`, ... `.friend.friend.friend.age`, y sigue. Para calcular el tamaño de `struct dog` habría que conocer el tamaño de `struct dog`.

La solución es guardar un **puntero**, que siempre mide 8 bytes, sea cual sea el tipo apuntado:

```c
typedef struct dog Dog;          // declaración adelantada: el alias existe antes de la definición
struct dog
{
    char* name;
    double age;
    bool good_boy;
    Dog* friend;                 // 8 bytes, no un struct completo
};

Dog A = {"bruno", 3, true, NULL};
Dog B = {"catalina", 4, true, NULL};
A.friend = &B;
B.friend = &A;                   // A.friend->friend->name es "bruno"
```

![Structs que se apuntan mutuamente](adjuntos/Structs%20que%20se%20apuntan%20mutuamente.png)

> [!example]- Transcripción de la imagen
> En `0x62df70` está A: `name = "bruno"`, `age = 3`, `good_boy = true`, `friend = 0x7d5ad4`. En `0x7d5ad4` está B: `name = "catalina"`, `age = 4`, `good_boy = true`, `friend = 0x62df70`. Cada uno guarda la dirección del otro.

> [!warning] El alias no existe dentro de su propia definición
> `typedef struct dog { Dog* friend; } Dog;` falla con "unknown type name 'Dog'", porque `Dog` recién existe al final de esa línea. Hay dos salidas: usar `struct dog*` dentro o declarar el `typedef` antes, como arriba.

## De aquí nace la lista ligada

Con un campo `next` que apunta al siguiente nodo, los structs recursivos forman una **lista ligada**: una secuencia de **largo variable** organizada en nodos. Insertar es fácil porque solo se cambian punteros. Para meter un 7 entre el 5 y el 3 de `1 → 5 → 3 → 10`, el 7 apunta al 3 y el 5 apunta al 7, y queda `1 → 5 → 7 → 3 → 10` sin mover ningún otro dato. Recorrerla es lento, en cambio, porque para llegar al nodo $i$ hay que seguir $i$ punteros desde el inicio. Su implementación completa es materia de Estructuras de Datos.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia de memoria entre `struct dog dog;` y `struct dog* dog;` como campo?
> El primero mete el struct completo dentro del bloque contenedor y ocupa todos sus bytes. El segundo guarda solo una dirección de 8 bytes hacia un struct que vive en otra parte.

> [!question]- ¿Por qué un struct no puede contener un campo de su mismo tipo, pero sí un puntero a él?
> Porque su tamaño quedaría definido en función de sí mismo y sería infinito. Un puntero mide siempre 8 bytes, así que el tamaño queda bien definido.

> [!question]- ¿Por qué `struct adult` necesita un campo `dog_count`?
> Porque `dogs` es solo la dirección del primer perro, y C no guarda el largo de los arreglos. Sin el contador no se sabe cuántos perros recorrer.

> [!question]- ¿Qué estructura de datos aparece si cada struct apunta al siguiente con un campo `next`?
> Una lista ligada: cada nodo guarda un valor y un puntero al siguiente, y el último apunta a `NULL`.
