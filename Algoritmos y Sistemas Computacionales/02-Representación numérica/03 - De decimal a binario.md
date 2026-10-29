---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Representación numérica"
tags:
  - algoritmos/binario
  - algoritmos/conversiones
  - origen/complemento
prerrequisitos:
  - "[[02 - De binario a decimal|De binario a decimal]]"
---

# De decimal a binario

El camino inverso —pasar de decimal a binario— se resuelve dividiendo el número por 2 una y otra vez y mirando los restos. Es el método que usa el curso y el que conviene dominar antes de operar con complemento a dos y hexadecimal.

## El método de las divisiones sucesivas

Se divide el número por 2, se anota el resto (0 o 1) y se continúa con el cuociente hasta llegar a 0. Los restos, leídos **de abajo hacia arriba**, forman el número binario.

> [!tip] Regla práctica
> El primer resto que se obtiene es el **bit menos significativo** (el de la derecha). Por eso se escribe al final. El último resto es el bit más significativo (el de la izquierda).

## Ejemplo paso a paso

Convertir $12_{10}$ a binario:

| División | Cuociente | Resto |
|---|---:|---:|
| $12 \div 2$ | 6 | 0 |
| $6 \div 2$ | 3 | 0 |
| $3 \div 2$ | 1 | 1 |
| $1 \div 2$ | 0 | 1 |

Los restos son 0, 0, 1, 1. Leídos de abajo hacia arriba: $1100_2$. Verificación: $8 + 4 = 12$.

## Un ejemplo más largo

Convertir $999_{10}$ a binario. Las divisiones son:

| División | Cuociente | Resto |
|---|---:|---:|
| $999 \div 2$ | 499 | 1 |
| $499 \div 2$ | 249 | 1 |
| $249 \div 2$ | 124 | 1 |
| $124 \div 2$ | 62 | 0 |
| $62 \div 2$ | 31 | 0 |
| $31 \div 2$ | 15 | 1 |
| $15 \div 2$ | 7 | 1 |
| $7 \div 2$ | 3 | 1 |
| $3 \div 2$ | 1 | 1 |
| $1 \div 2$ | 0 | 1 |

Leídos de abajo hacia arriba: $1111100111_2$. La verificación suma $512 + 256 + 128 + 64 + 32 + 4 + 2 + 1 = 999$.

## Atajos útiles

- Si el número es una potencia de 2, el binario es un 1 seguido de tantos ceros como el exponente: $16 = 2^4 = 10000_2$.
- Si el número es impar, el último bit es 1; si es par, es 0.
- Para números grandes conviene restar la potencia de 2 más grande que cabe y repetir con lo que sobra.

> [!warning] El error típico
> Leer los restos en el orden en que se obtienen. Ese orden da el número al revés. Siempre se leen de abajo hacia arriba, porque el primer resto es el bit de la derecha.

## Preguntas de repaso

> [!question]- ¿Por qué el primer resto es el bit menos significativo?
> Porque la división por 2 separa el número en dos partes: el cuociente (los bits de las potencias mayores) y el resto (el bit de $2^0$). Ese resto es el que queda a la derecha.

> [!question]- ¿Cómo se sabe cuándo terminar las divisiones?
> Cuando el cuociente llega a 0. El último resto distinto de cero es el bit más significativo.

> [!question]- Convierte $20_{10}$ a binario.
> $20 \div 2 = 10$ r0; $10 \div 2 = 5$ r0; $5 \div 2 = 2$ r1; $2 \div 2 = 1$ r0; $1 \div 2 = 0$ r1. Leído de abajo hacia arriba: $10100_2$.

> [!question]- ¿Qué tienen en común los binarios de los números pares?
> Terminan en 0, porque el resto de dividir un par por 2 es 0. Los impares terminan en 1.
