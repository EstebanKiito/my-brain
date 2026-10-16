---
ramo: "Estructuras de Datos"
tema: "Análisis de algoritmos"
tags:
  - edd
  - correctitud
  - pseudocodigo
  - bubble-sort
  - origen/complemento
prerrequisitos:
  - "[[01 - Inducción simple, fuerte y estructural]]"
---

# Correctitud de algoritmos

Un **algoritmo** es una secuencia ordenada de pasos que resuelve un tipo de problema. Es independiente del lenguaje: puede escribirse en C, en Python, en lenguaje natural o en **pseudocódigo**, que es lo que usa el curso (control de flujo, notación matemática y lenguaje natural cuando es más claro). Antes de preguntarse si un algoritmo es rápido, hay que saber si es correcto.

> [!tip] Algoritmo correcto
> Un algoritmo es **correcto** si (1) **termina** en una cantidad finita de pasos y (2) **cumple su propósito**. Para ordenar, eso significa que entrega los datos ordenados después de finitos pasos.

Las dos partes se demuestran por separado. La finitud se justifica contando qué se consume en cada iteración. El propósito se demuestra por [[01 - Inducción simple, fuerte y estructural|inducción]] sobre los pasos del algoritmo.

## Ejemplo: ordenar extrayendo el menor

```
input : Lista L
output: Lista ordenada L'
Ordenar(L):
1   Iniciamos L' vacía
2   Encontrar el menor valor en L
3   Borrar el valor encontrado
4   Escribirlo al final de L'
5   Si quedan valores en L, volver a la línea 2
    return L'
```

**Finitud.** Sea $n$ la cantidad finita de valores de $L$. Cada iteración borra exactamente un valor de $L$. Después de $n$ iteraciones $L$ queda vacía y la línea 5 corta el ciclo.

![Demostración de finitud](adjuntos/Demostraci%C3%B3n%20de%20finitud%20de%20un%20algoritmo%20de%20ordenaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Demostración (finitud)". Sea $n$ la cantidad (finita) de valores en la lista original $L$. En cada iteración se borra un valor de $L$ y se escribe en la lista nueva $L'$. Luego de $n$ iteraciones todos los valores de $L$ fueron borrados; por la línea 5, que verifica si quedan valores en $L$, el algoritmo no sigue iterando. Por lo tanto termina en una cantidad finita de pasos.

**Propósito.** La propiedad que se demuestra es:

$$P(n) := \text{los primeros } n \text{ valores borrados de } L \text{ son los } n \text{ menores de } L \text{ y están ordenados en } L'.$$

- **CB ($n = 1$):** el primer valor borrado es el mínimo de $L$, y una lista de un elemento está ordenada.
- **HI:** después de $n$ pasos, $L'$ contiene los $n$ menores, en orden.
- **TI:** en el paso $n+1$ se borra el menor de lo que queda en $L$. Todo lo que queda es mayor o igual que lo que ya está en $L'$ (por HI, ahí están los menores), así que agregarlo **al final** mantiene $L'$ ordenada y con los $n+1$ menores.

Este algoritmo es la versión con lista auxiliar de *selection sort*.

## Ejemplo: bubble sort

1. Tomar el primer dato $x$ y compararlo con el siguiente $y$.
2. Si $y < x$, intercambiarlos.
3. Avanzar una posición y repetir hasta el penúltimo elemento.
4. Repetir pasadas completas hasta hacer una **sin intercambios**.

![Animación de bubble sort](adjuntos/Animaci%C3%B3n%20de%20bubble%20sort.gif)

> [!example]- Transcripción de la imagen
> Animación de barras con los valores 29, 10, 14, 37, 14, 2, 17, 41, 32, 5. En cada pasada se comparan barras vecinas y se intercambian si están desordenadas, de modo que la barra más alta "burbujea" hasta el final. La animación termina con las barras ordenadas de menor a mayor.

**Propósito, por inducción sobre el largo.** CB: un arreglo de 1 elemento ya está ordenado. HI: bubble sort ordena cualquier arreglo de largo $n$. TI: en un arreglo $A$ de largo $n+1$, la primera pasada lleva el **máximo** al final, porque gana todas sus comparaciones, y desde ahí nunca más se mueve. El resto $A'$ (sin el máximo) tiene largo $n$ y por HI queda ordenado. Entonces $A$ queda ordenado.

**Finitud.** Cada intercambio corrige exactamente un par desordenado (una *inversión*), y hay a lo más $\binom{n}{2}$. Por eso solo hay finitas pasadas con intercambios. La siguiente no tiene ninguno y el algoritmo se detiene.

> [!tip] Orden práctico
> A veces es más cómodo demostrar primero que el algoritmo hace lo pedido y después que termina. En bubble sort, saber que ordena asegura que se llega a una pasada sin intercambios, que es su condición de término.

```python
def bubble_sort(A):
    A = list(A)
    hubo_intercambio = True
    while hubo_intercambio:        # termina tras una pasada sin intercambios
        hubo_intercambio = False
        for k in range(len(A) - 1):
            if A[k + 1] < A[k]:
                A[k], A[k + 1] = A[k + 1], A[k]
                hubo_intercambio = True
    return A

print(bubble_sort([29, 10, 14, 37, 14, 2, 17, 41, 32, 5]))
# [2, 5, 10, 14, 14, 17, 29, 32, 37, 41]
```

## Preguntas de repaso

> [!question]- ¿Por qué no basta con demostrar que un algoritmo "hace lo pedido" para decir que es correcto?
> Porque un algoritmo que nunca termina no entrega resultado. La correctitud exige las dos cosas: que termine en finitos pasos y que el resultado cumpla el propósito.

> [!question]- En la demostración del algoritmo que extrae el menor, ¿qué parte de la hipótesis inductiva justifica escribir al final de L'?
> Que $L'$ ya contiene los $n$ menores de $L$. Por eso todo lo que queda en $L$ es mayor o igual, y el nuevo mínimo puede ir al final sin romper el orden.

> [!question]- ¿Por qué en bubble sort la inducción se hace "sacando el máximo"?
> Porque la primera pasada deja el máximo fijo en la última posición. Lo que queda es un arreglo de largo $n$ que bubble sort procesa igual, y a ese arreglo se le aplica la hipótesis inductiva.

> [!question]- ¿Cómo se justifica que bubble sort no hace infinitas pasadas?
> Cada intercambio elimina una inversión y nunca crea otra. Como el número de inversiones es finito, hay finitas pasadas con intercambios, y la siguiente pasada sin intercambios detiene el algoritmo.
