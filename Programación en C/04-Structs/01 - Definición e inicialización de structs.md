---
ramo: "Programación en C"
tema: "Structs"
tags:
  - c
  - structs
  - typedef
  - origen/complemento
prerrequisitos:
  - "[[02 - Tipos de datos, printf y casting]]"
---

# Definición e inicialización de structs

C no tiene clases. Para agrupar datos relacionados bajo un mismo nombre existe el **struct**: una colección de **campos** con nombre y tipo propios, que, a diferencia de un arreglo, pueden ser de tipos distintos. Es lo más parecido a un objeto sin métodos, o a una `namedtuple` de Python, y es la pieza con la que se construyen todas las estructuras de datos del curso (nodos de listas, árboles, grafos).

## Definir el tipo

```c
struct perro
{
    char* nombre;
    char* raza;
    double edad;
    bool good_boy;
};
```

Los campos se fijan en la definición: **no se pueden agregar después ni darles valores por defecto**. Para no escribir `struct point` en todas partes, se le da un alias con `typedef`, y por convención el alias va en CamelCase:

```c
typedef struct point          // forma corta: definición + alias en una sola declaración
{
    double x;
    double y;
} Point;
// equivale a: struct point { ... };  typedef struct point Point;
```

## Crear e inicializar

Los campos quedan **contiguos en memoria**, igual que un arreglo, así que un struct se puede inicializar con llaves al declararlo:

```c
struct point p = {5.12, 2.78};             // por posición (orden de los campos)
Point q = {.x = 5.12, .y = 2.78};          // por nombre: más claro y robusto

Point r;                                   // declarar sin inicializar...
r = (Point){.x = 7.18, .y = 2.52};         // ...y asignar con un "compound literal"
r.y *= 2;                                  // acceso y modificación con punto

Point A[2];                                // arreglo de structs
A[0] = (Point){.x = 1.26, .y = 25.3};
A[1] = (Point){0.54, 1.55};
```

> [!warning] Las llaves solas solo sirven al declarar
> `Point r; r = {.x = 7.18, .y = 2.78};` **no compila** ("expected expression"): fuera de una declaración, el compilador interpreta `{` como el inicio de un bloque de código. Para asignar después hay que escribir el tipo entre paréntesis, `(Point){...}`, o asignar campo por campo (`r.x = 7.18;`).

## Tamaño y copia

`sizeof(Point)` es 16 (dos `double` de 8 bytes). Un struct se **copia completo** al asignarlo o al pasarlo a una función: `Point s = r;` duplica todos los campos. Para structs grandes o que deben modificarse dentro de una función, conviene trabajar con [[02 - Punteros a structs y operador flecha|punteros a structs]].

> [!tip] Struct frente a arreglo
> Un arreglo agrupa **muchos valores del mismo tipo** a los que se accede por **índice**. Un struct agrupa **valores de tipos distintos** a los que se accede por **nombre**. Se combinan con frecuencia: arreglos de structs y structs que contienen arreglos.

## Preguntas de repaso

> [!question]- ¿Por qué `r = {.x = 1, .y = 2};` falla, pero `Point r = {.x = 1, .y = 2};` funciona?
> La segunda es una inicialización dentro de una declaración, donde las llaves están permitidas. En una asignación posterior, `{` se interpreta como el inicio de un bloque. Ahí hay que usar `(Point){.x = 1, .y = 2}`.

> [!question]- ¿Qué ventaja tiene inicializar por nombre (`.x = ...`) en vez de por posición?
> No depende del orden de los campos en la definición, así que si se reordenan o se agregan campos el código sigue siendo correcto. Además, deja claro qué valor va en qué campo.

> [!question]- ¿Para qué sirve `typedef` con un struct?
> Para darle un alias al tipo (`Point` en vez de `struct point`), lo que acorta y aclara el código. No cambia el tipo ni su tamaño.

> [!question]- ¿Qué pasa con los campos al hacer `Point s = r;`?
> Se copian todos, uno por uno. `s` y `r` quedan independientes: modificar `s.x` no afecta a `r.x`.
