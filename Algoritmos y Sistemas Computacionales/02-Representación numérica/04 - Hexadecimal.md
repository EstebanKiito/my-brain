---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Representación numérica"
tags:
  - algoritmos/hexadecimal
  - algoritmos/conversiones
  - origen/complemento
prerrequisitos:
  - "[[02 - De binario a decimal|De binario a decimal]]"
---

# Hexadecimal

Escribir binario es incómodo: un número de 16 bits ocupa 16 símbolos. El **hexadecimal** (base 16) agrupa esos bits de cuatro en cuatro y los resume en un solo dígito. Por eso se usa para direcciones de memoria, colores y volcados de datos.

## Base 16

En base 16 hacen falta 16 dígitos. Como solo conocemos los diez decimales, se agregan las letras A, B, C, D, E y F para los valores 10 a 15:

| Decimal | Hexadecimal | Binario |
|---:|---|---|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

> [!tip] La idea central
> Un dígito hexadecimal equivale exactamente a 4 bits. Esa correspondencia perfecta es lo que hace tan fácil convertir entre ambas bases.

## De hexadecimal a binario

Cada dígito hexadecimal se reemplaza por sus 4 bits, en el mismo orden. Por ejemplo:

$$(2A)_{16} = 0010\ 1010_2$$

$$(7C)_{16} = 0111\ 1100_2$$

$$(958)_{16} = 1001\ 0101\ 1000_2$$

No hay que hacer cuentas: basta con mirar la tabla.

## De binario a hexadecimal

Se agrupan los bits de **derecha a izquierda** en bloques de 4. Si el último bloque queda incompleto, se rellena con ceros a la izquierda. Luego cada bloque se convierte a su dígito hexadecimal.

$$(101010)_2 \rightarrow (0010\ 1010)_2 \rightarrow (2A)_{16}$$

$$(1010101111001101)_2 \rightarrow (1010\ 1011\ 1100\ 1101)_2 \rightarrow (ABCD)_{16}$$

> [!warning] Agrupar desde la izquierda
> Si se agrupa desde la izquierda, los bloques quedan corridos y el resultado es otro número. Siempre se agrupa desde la derecha, porque el bit menos significativo debe quedar en el primer bloque.

## Por qué se usa

- Un byte (8 bits) se escribe con dos dígitos hexadecimales, por ejemplo `FF`.
- Las direcciones de memoria y los colores en pantalla suelen expresarse en hexadecimal.
- Al leer un volcado de memoria, el hexadecimal es mucho más compacto que el binario.

> [!example]- Ejemplo de ida y vuelta
> $(1010)_2 = A_{16}$ porque $1010_2 = 10_{10}$. Y $(00011110)_2 = 1E_{16}$ porque $0001 = 1$ y $1110 = E$. La ida y la vuelta usan la misma tabla.

## Preguntas de repaso

> [!question]- ¿Por qué un dígito hexadecimal equivale a 4 bits?
> Porque $2^4 = 16$: con 4 bits se pueden representar exactamente los 16 valores de un dígito hexadecimal.

> [!question]- ¿Cuántos dígitos hexadecimales necesita un byte?
> Dos, porque un byte tiene 8 bits y cada dígito hexadecimal cubre 4 bits.

> [!question]- Convierte $(10110111)_2$ a hexadecimal.
> Se agrupa en 1011 y 0111, que son B y 7. Entonces $(10110111)_2 = (B7)_{16}$.

> [!question]- ¿Por qué se rellena con ceros a la izquierda y no a la derecha?
> Porque los ceros a la izquierda no cambian el valor del número. A la derecha cambiarían su magnitud, sería como multiplicar por una potencia de 2.
