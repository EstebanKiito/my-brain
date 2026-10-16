---
ramo: "Programación en C"
tema: "Punteros, arreglos y strings"
tags:
  - c
  - arreglos
  - aritmetica-de-punteros
  - origen/complemento
prerrequisitos:
  - "[[02 - Paso por valor y punteros como referencia]]"
---

# Aritmética de punteros y arreglos

Un **arreglo** en C es un bloque de celdas **contiguas** en memoria, todas del mismo tipo y con largo fijo. Es muy distinto de una lista de Python: no puede mezclar tipos, no sabe su propio largo y no revisa los índices. A cambio, acceder a cualquier posición cuesta $O(1)$, porque la dirección de cada celda se **calcula** con aritmética de punteros.

## Sumarle 1 a un puntero avanza una celda

Es lo único que C hace "solo": si `A` es de tipo `type*`, `A + i` no suma `i` bytes, sino `i * sizeof(type)`. Un `int*` más 1 avanza 4 bytes.

![Aritmética de punteros con sizeof](adjuntos/Aritm%C3%A9tica%20de%20punteros%20con%20sizeof.png)

> [!example]- Transcripción de la imagen
> "`type* A`" y una flecha hacia la regla "`A + i = A + i * sizeof(type)`".

![Variables contiguas en el stack](adjuntos/Variables%20contiguas%20en%20el%20stack.png)

> [!example]- Transcripción de la imagen
> Marco de `(main)` con `l = 7` en `0x7c35f4`, `m = 13` en `0x7c35f8` y `n = 0x7c35f4` en `0x7c35fc`. `n` apunta a `l`, y la celda siguiente (`n + 1`) es `m`, 4 bytes más allá.

> [!warning] No usar la aritmética entre variables sueltas
> En la figura, `*(n + 1)` da 13 porque el compilador dejó `m` justo después de `l`. Eso **no está garantizado**: el orden de las variables locales en el stack depende del compilador. La aritmética de punteros solo es válida **dentro de un mismo arreglo**. Fuera de él, se lee basura o algo peor.

## Un arreglo es su primer elemento

```c
int A[6] = {0, 5, 3, 2, 1, 7};   // definición con valores
int B[4];                        // solo declaración: 4 int sin inicializar
```

![Arreglo contiguo en el stack](adjuntos/Arreglo%20contiguo%20en%20el%20stack.png)

> [!example]- Transcripción de la imagen
> Marco de `(main)` con `A[0] = 0` en `0x8a71f0`, `A[1] = 5` en `0x8a71f4`, `A[2] = 3` en `0x8a71f8`, `A[3] = 2` en `0x8a71fc`, `A[4] = 1` en `0x8a7200` y `A[5] = 7` en `0x8a7204`: celdas seguidas, de 4 en 4 bytes.

En casi todas las expresiones, el nombre `A` se convierte en un puntero a `A[0]`. Por eso `A`, `&A` y `&A[0]` imprimen la misma dirección, y la indexación no es más que aritmética de punteros:

![Indexación como aritmética de punteros](adjuntos/Indexaci%C3%B3n%20como%20aritm%C3%A9tica%20de%20punteros.png)

> [!example]- Transcripción de la imagen
> "`type A[]`" y una flecha hacia "`A[i] = *(A + i)`".

![Dirección del tercer elemento](adjuntos/Direcci%C3%B3n%20del%20tercer%20elemento%20del%20arreglo.png)

> [!example]- Transcripción de la imagen
> La misma tabla del arreglo `A` con todo en gris salvo `0x8a71f8 → A[2] = 3`: `&A[2]` y `A + 2` son esa dirección y `A[2]` es su valor.

![La indexación conmuta](adjuntos/La%20indexaci%C3%B3n%20conmuta.png)

> [!example]- Transcripción de la imagen
> "`A[i] = i[A]`" junto a un emoji asustado. Como `A[i]` es `*(A + i)` y la suma conmuta, `i[A]` = `*(i + A)` también compila. Se puede, pero nunca se escribe así.

```c
printf("%d %d %d\n", A[2], *(A + 2), 2[A]);   // 3 3 3
printf("sizeof(A) = %zu\n", sizeof(A));       // 24: el arreglo completo, no un puntero
```

## Recorrer y pasar arreglos

No existe `for elem in array` ni `len()`: **hay que guardar el largo** y recorrer con índices. Como el arreglo "es" la dirección de su primer elemento, una función lo recibe como puntero, junto con su largo, y **puede modificarlo**:

```c
int sum(int* array, int n)
{
    int total = 0;
    for (int i = 0; i < n; i += 1) total += array[i];
    return total;
}

void multiply_by(int* array, int n, int x)
{
    for (int i = 0; i < n; i += 1) array[i] *= x;   // cambia el arreglo original
}
// int B[5] = {1, -2, 3, 4, 1};  sum(B, 5) = 7;  multiply_by(B, 5, 3) -> {3, -6, 9, 12, 3}
```

Las **matrices** (`int M[3][2] = {{1, 2}, {3, 4}, {5, 6}};`) también son contiguas, fila tras fila: `M[1][0]` está justo después de `M[0][1]`. Por eso todas las filas deben tener el mismo largo.

> [!warning] C no revisa los índices
> `A[-1]` o `A[100]` en un arreglo de 6 compilan sin problema: leen la memoria vecina y entregan basura. Escribir fuera del arreglo es peor, porque pisa otras variables. Si el sistema operativo lo detecta, aborta con *stack smashing detected* o *segmentation fault*, pero muchas veces no avisa.

## Preguntas de repaso

> [!question]- Si `int* p` vale `0x1000`, ¿cuánto vale `p + 3`?
> `0x100C`, porque cada paso avanza `sizeof(int)` = 4 bytes: $0x1000 + 3 \cdot 4$.

> [!question]- ¿Por qué acceder a `A[i]` cuesta $O(1)$ sin importar `i`?
> Porque la dirección se calcula directamente como `A + i * sizeof(type)`, gracias a que las celdas son contiguas y del mismo tamaño. No hay que recorrer nada.

> [!question]- ¿Por qué una función que recibe un arreglo necesita también su largo?
> Porque la función solo recibe la dirección del primer elemento. C no guarda el largo del arreglo en ningún lado, así que sin `n` no sabe dónde terminar.

> [!question]- ¿Qué ocurre al leer `A[3]` en un `int A[3]`?
> Se lee la memoria justo después del arreglo: C no revisa límites y entrega lo que haya ahí, normalmente basura. No hay error de compilación, y en ejecución tampoco suele haberlo.
