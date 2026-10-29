---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Operaciones binarias y complemento a dos"
tags:
  - algoritmos/binario
  - algoritmos/complemento-a-dos
  - origen/complemento
prerrequisitos:
  - "[[01 - Suma binaria|Suma binaria]]"
---

# Representación de números negativos

Los bits solo tienen dos valores, 0 y 1, así que no hay un signo menos que escribir. Para representar números negativos existen varias convenciones; la que usan casi todos los computadores es el **complemento a dos**, porque permite sumar y restar con el mismo circuito.

## El problema

Si en 4 bits se escribe $0101_2 = 5$, ¿cómo se escribe $-5$? Se podría reservar un bit para el signo, o inventar una regla para invertir los bits. Cada idea tiene ventajas y costos, y conviene conocer las tres más comunes.

## Signo y magnitud

Se reserva el bit de la izquierda para el signo: 0 significa positivo y 1 negativo. Los bits restantes guardan la magnitud.

- $+5$ en 4 bits: $0101_2$.
- $-5$ en 4 bits: $1101_2$ (el primer 1 indica negativo; 101 es la magnitud 5).

> [!warning] Dos ceros y aritmética incómoda
> Esta representación tiene dos ceros: $0000$ (+0) y $1000$ (-0). Además, sumar un positivo y un negativo requiere revisar el signo y decidir si se suma o se resta la magnitud, así que no sirve un sumador único.

## Complemento de uno

Se invierten todos los bits: los 0 pasan a 1 y los 1 a 0.

- $+5$ en 4 bits: $0101_2$.
- $-5$ en 4 bits: $1010_2$.

> [!warning] El problema del doble cero
> También tiene dos ceros: $0000$ (+0) y $1111$ (-0). Y para sumar hay que devolver el acarreo al bit menos significativo (*end-around carry*), lo que complica el circuito.

## Complemento a dos

Se invierten los bits y se suma 1 al resultado. Es la convención que se usa en la práctica.

- $+5$ en 4 bits: $0101_2$.
- $-5$ en 4 bits: $0101 \rightarrow 1010 \rightarrow 1011_2$.

Con esta regla hay un solo cero ($0000$), y la suma y la resta se hacen con el mismo sumador: restar es sumar el negativo.

## Comparación

| Decimal | Signo y magnitud | Complemento de uno | Complemento a dos |
|---:|---|---|---|
| 5 | 0101 | 0101 | 0101 |
| -5 | 1101 | 1010 | 1011 |
| 0 | 0000 | 0000 | 0000 |
| -0 | 1000 | 1111 | no existe |

> [!tip] La idea central
> En complemento a dos, el bit de la izquierda sigue indicando el signo (0 positivo, 1 negativo), pero el valor no se lee como signo y magnitud: se interpreta con la regla del complemento. Por eso $1011$ no es "menos 3", sino $-5$.

## Preguntas de repaso

> [!question]- ¿Por qué el complemento a dos es la representación más usada?
> Porque tiene un solo cero y permite hacer sumas y restas con el mismo circuito, sin revisar signos ni devolver acarreos especiales.

> [!question]- ¿Qué diferencia hay entre complemento de uno y complemento a dos?
> El complemento de uno solo invierte los bits. El complemento a dos invierte los bits y luego suma 1. Esa suma elimina el doble cero.

> [!question]- En signo y magnitud, ¿qué representa $1000$ en 4 bits?
> El cero negativo (-0). Es uno de los dos ceros que tiene esa representación.

> [!question]- ¿El bit de la izquierda siempre indica el signo?
> En las tres convenciones de esta nota, sí: 0 es positivo y 1 es negativo. Pero en complemento a dos el valor completo se interpreta con la regla del complemento, no como signo y magnitud.
