---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Codificación de caracteres"
tags:
  - algoritmos/ascii
  - algoritmos/codificacion
  - origen/complemento
prerrequisitos:
  - "[[03 - Complemento a dos|Complemento a dos]]"
---

# ASCII

Un computador solo guarda números. Para que pueda mostrar letras, hay que ponerse de acuerdo en qué número representa cada carácter. **ASCII** (*American Standard Code for Information Interchange*) es esa tabla: asigna un número de 7 bits a cada letra, dígito y símbolo básico.

## La idea

Cada carácter tiene un código entre 0 y 127. Como son 128 valores, alcanzan justo para 7 bits ($2^7 = 128$). Al escribir un texto, el computador guarda la secuencia de códigos; al mostrarlo, busca cada código en la tabla y dibuja el carácter correspondiente.

> [!tip] La idea central
> ASCII no guarda letras: guarda números. La letra es solo la interpretación que hace el programa al leer ese número.

## Los códigos que más se usan

| Carácter | Decimal | Binario |
|---|---:|---|
| `0` | 48 | 00110000 |
| `9` | 57 | 00111001 |
| `A` | 65 | 01000001 |
| `B` | 66 | 01000010 |
| `Z` | 90 | 01011010 |
| `a` | 97 | 01100001 |
| `z` | 122 | 01111010 |
| espacio | 32 | 00100000 |

Los dígitos van del 48 al 57, las mayúsculas del 65 al 90 y las minúsculas del 97 al 122. Los códigos 0 a 31 son caracteres de control que no se ven: el salto de línea, el tabulador, el retorno de carro, etc.

> [!example]- Un patrón útil
> La `A` mayúscula es 65 y la `a` minúscula es 97. La diferencia es 32, que en binario es $2^5$: cambiar el bit 5 convierte una mayúscula en minúscula (y viceversa) cuando la letra es la misma.

## Convertir un carácter a binario

El procedimiento es el mismo de los temas anteriores: se busca el código decimal del carácter y se convierte a binario.

Convertir `A`:

1. `A` = 65.
2. $65 = 64 + 1 = 2^6 + 2^0$.
3. En 8 bits: `01000001`.

Convertir `01100001` a carácter:

1. $01100001_2 = 64 + 32 + 1 = 97$.
2. El código 97 corresponde a `a`.

## Decodificar un mensaje

Para leer `01001000 01101001`:

- $01001000_2 = 72$, que es `H`.
- $01101001_2 = 105$, que es `i`.

El mensaje es `Hi`.

## La tabla completa

![Tabla ASCII con los códigos decimal, hexadecimal, HTML y el carácter correspondiente](adjuntos/Tabla%20ASCII.png)

> [!example]- Transcripción de la imagen
> - La tabla tiene cuatro bloques de columnas, uno por rango de códigos.
> - Cada fila muestra el valor decimal, el hexadecimal, el código HTML y el carácter.
> - Los primeros códigos (0 a 31) son caracteres de control: `NUL`, `SOH`, `STX`, `ETX`, salto de línea (`LF`), tabulador (`HT`), etc.
> - Desde el 32 aparece el espacio; luego los signos, los dígitos (48-57), las mayúsculas (65-90), los corchetes y las minúsculas (97-122).

> [!warning] ASCII se queda corto
> ASCII solo tiene 128 caracteres y no incluye la ñ, las tildes, el euro ni los emojis. Para escribir en español o en otros idiomas hace falta una codificación más amplia: UTF-8.

## Preguntas de repaso

> [!question]- ¿Por qué ASCII usa 7 bits y no 8?
> Porque con 7 bits alcanzan $2^7 = 128$ códigos, suficientes para las letras, dígitos y signos básicos del inglés. El octavo bit se usaba para control de errores o se dejaba en 0.

> [!question]- ¿Qué número corresponde a la letra `A` y cómo se escribe en binario?
> 65, que en binario es `01000001`.

> [!question]- ¿Cómo se decodifica `01000010`?
> $01000010_2 = 66$, que corresponde a la letra `B`.

> [!question]- ¿Por qué un texto en español puede ocupar más espacio en UTF-8 que en ASCII?
> Porque caracteres como la ñ o las vocales con tilde no existen en ASCII y en UTF-8 necesitan 2 bytes en vez de 1.
