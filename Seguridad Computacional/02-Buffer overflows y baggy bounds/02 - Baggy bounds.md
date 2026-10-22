---
ramo: "Seguridad Computacional"
tema: "Buffer overflows y baggy bounds"
tags:
  - seguridad/memoria
  - c
  - origen/complemento
prerrequisitos:
  - "[[01 - Buffer overflows y sus defensas]]"
---

# Baggy bounds

Las defensas anteriores dificultan la explotación pero no evitan el error. Si se puede modificar el compilador, se puede comprobar automáticamente que cada acceso quede dentro de su objeto, y así detener cualquier desborde, incluso en programas C grandes y con errores. **Baggy bounds** es una forma práctica de hacerlo.

## Primer intento: punteros gordos
Cada puntero guarda `start`, `end` y `curr`; al desreferenciar se exige `start <= curr < end`. Es simple pero poco práctico: las comprobaciones cuestan, cambia el tamaño de las estructuras, no se puede pasar a bibliotecas no modificadas y copiar un puntero deja de ser atómico (problema con hilos y señales).

## Idea de baggy bounds: tabla de límites aparte
No se cambia el puntero: se guarda en una **tabla** el tamaño de cada objeto, que mantienen `malloc` y el código generado. El compilador vigila dos operaciones:
- **Aritmética de punteros** (`q = p + 256`): si `q` sale del objeto original, se marca con el bit **OOB** (*out of bounds*).
- **Desreferencia** (`*q`): si `q` tiene OOB, el programa se detiene.

Se necesita OOB, y no basta con abortar al salir, porque código C legal crea punteros fuera de rango (como `end = arr + n` en un recorrido hacia atrás); solo es error usarlos para acceder.

## Trucos para que sea barato
- **Potencias de dos:** los objetos se reservan con tamaño potencia de dos y alineados a él; la tabla guarda solo $\log_2(\text{tamaño})$ en un byte, con una entrada por cada 16 bytes (`slot_size`).
- Tamaño e inicio se calculan con operaciones de bits:
```c
tamaño = 1 << tabla[p >> 4];
inicio = p & ~(tamaño - 1);
```
- **Memoria virtual para OOB:** se activa el bit más significativo del puntero y la mitad superior del espacio de direcciones se deja inaccesible, así la desreferencia falla sola sin instrucciones de comprobación. OOB solo vale hasta `slot_size/2` de distancia: si el puntero vuelve al objeto se limpia el bit; si se aleja más, aborta.

```c
p = malloc(25);  // se redondea a 32 bytes
q = p + 10;      // ok
r = p + 35;      // fuera: OOB; *r = 1 aborta
s = p + 35; s = s - 20; *s = 1;  // OOB se limpia: ok
t = p + 100;     // lejos del objeto: aborta
```

## Límites
No detecta desbordes de un arreglo dentro de una `struct` más grande, punteros convertidos a entero y de vuelta, asignadores propios ni punteros colgantes; y puede fallar con código que compara punteros como enteros por el bit OOB.

> [!tip] Patrón general
> Los defensores cometen un tipo de error, los atacantes lo explotan y los defensores construyen una herramienta para detectarlo.

## Preguntas de repaso

> [!question]- ¿Por qué se guarda el tamaño como potencia de dos?
> Reduce la tabla a un byte por entrada y permite calcular el inicio del objeto desde cualquier puntero interior con una máscara de bits, sin recorrer nada.

> [!question]- ¿Para qué sirve el bit OOB en lugar de abortar apenas el puntero sale del objeto?
> Porque programas legales crean punteros un paso más allá del final; OOB permite tolerarlo mientras no se desreferencie y reconocer cuándo el puntero vuelve a ser válido.

> [!question]- ¿Qué ventaja tiene baggy bounds sobre los punteros gordos?
> No cambia la representación de los punteros, por lo que es compatible con bibliotecas no modificadas y no rompe la atomicidad al copiar punteros.
