---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Operaciones binarias y complemento a dos"
tags:
  - algoritmos/binario
  - algoritmos/aritmetica
  - origen/complemento
prerrequisitos:
  - "[[04 - Hexadecimal|Hexadecimal]]"
---

# Suma binaria

El computador guarda los datos en bytes, es decir, en binario, y necesita operar con ellos. Sumar en base 2 funciona igual que en base 10, pero con una diferencia clave: cuando una columna llega a 2, se escribe 0 y se lleva 1 a la siguiente. Esa idea de **acarreo** (*carry*) es la base de toda la aritmética del computador.

## Las cuatro reglas

| Suma | Resultado | Acarreo |
|---|---|---|
| $0 + 0$ | 0 | 0 |
| $0 + 1$ | 1 | 0 |
| $1 + 0$ | 1 | 0 |
| $1 + 1$ | 0 | 1 |

La última regla es la única que genera acarreo: $1 + 1 = 10_2$, que se escribe como 0 en la columna y un 1 que se suma a la columna siguiente.

> [!tip] La idea central
> Se suma columna por columna, de derecha a izquierda, arrastrando el acarreo. Es exactamente lo que se hace en decimal cuando $7 + 5 = 12$: se escribe 2 y se lleva 1.

## Ejemplo paso a paso

Sumar $1011_2 + 0110_2$:

```
  1 1 1 1   ← acarreos
    1 0 1 1
+   0 1 1 0
-----------
  1 0 0 0 1
```

De derecha a izquierda:
1. $1 + 0 = 1$.
2. $1 + 1 = 0$ y llevo 1.
3. $0 + 1 + 1 = 0$ y llevo 1.
4. $1 + 0 + 1 = 0$ y llevo 1.
5. Se baja el acarreo final: 1.

El resultado es $10001_2 = 17_{10}$. Comprobación: $11 + 6 = 17$.

## Más ejemplos

| Suma | Resultado binario | Comprobación decimal |
|---|---|---:|
| $1101_2 + 0011_2$ | $10000_2$ | $13 + 3 = 16$ |
| $1010_2 + 1010_2$ | $10100_2$ | $10 + 10 = 20$ |
| $1111_2 + 0001_2$ | $10000_2$ | $15 + 1 = 16$ |

> [!warning] El resultado puede tener un bit más
> Al sumar dos números de $n$ bits, el resultado puede necesitar $n+1$ bits. Ese bit extra se llama **acarreo de salida** (*carry out*). Si el registro solo tiene $n$ bits, el acarreo se pierde o se usa para detectar desbordamiento.

## Preguntas de repaso

> [!question]- ¿Por qué $1 + 1$ da 0 con acarreo 1?
> Porque en base 2 no existe el dígito 2. El valor 2 se escribe como $10_2$: un 0 en la columna actual y un 1 en la siguiente.

> [!question]- ¿En qué se parece la suma binaria a la suma decimal?
> En que ambas suman columna por columna de derecha a izquierda y arrastran un acarreo cuando la suma de una columna supera la base.

> [!question]- Suma $1011_2 + 0001_2$.
> $1011 + 0001 = 1100_2$, que es $11 + 1 = 12$. Solo se propaga un acarreo.

> [!question]- ¿Qué es el acarreo de salida y cuándo aparece?
> Es el bit extra que se genera cuando la suma de los bits más significativos produce un acarreo. Aparece cuando el resultado no cabe en la misma cantidad de bits que los operandos.
