---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Programabilidad de circuitos digitales"
tags:
  - algoritmos/arquitectura
  - algoritmos/memoria
  - origen/complemento
prerrequisitos:
  - "[[01 - Calculadora con registros y señales de carga|Calculadora con registros y señales de carga]]"
---

# Memoria de instrucciones y PC

Una calculadora necesita que alguien apriete los botones en cada operación. Un computador, en cambio, lee las instrucciones desde una **memoria** y las ejecuta en orden. Esa memoria y el **Program Counter** (PC) son las piezas que permiten almacenar un programa completo.

## El programa como lista de instrucciones

Cada instrucción de la calculadora ocupa 5 bits: la operación `S` y las señales `La`, `Lb`. Un programa es una secuencia de esas instrucciones:

| Dirección | Instrucción (S, La, Lb) | Operación |
|---|---|---|
| 0000 | 000 1 0 | Suma y guarda en A |
| 0001 | 111 0 1 | Shift right y guarda en B |
| 0010 | 001 1 0 | Resta y guarda en A |

La **memoria de instrucciones** guarda esas filas. Cada fila tiene una **dirección** (un número secuencial) y un **contenido** (los bits de la instrucción).

## Direcciones y tamaño

Si la dirección tiene 4 bits, se pueden direccionar $2^4 = 16$ instrucciones. En cada dirección se guardan los 5 bits de la instrucción. El tamaño de la memoria depende de ambos: cantidad de instrucciones y ancho de cada una.

> [!tip] La idea central
> Un programa es un dato más: se guarda en memoria como una secuencia de bits. Ejecutarlo es leer esas instrucciones una por una.

## El Program Counter

El **Program Counter** (PC) es un registro que guarda la dirección de la instrucción que se va a ejecutar. El ciclo es:

1. El PC indica una dirección.
2. La memoria entrega la instrucción guardada en esa dirección.
3. La instrucción se ejecuta.
4. El PC se incrementa en 1 para apuntar a la siguiente.

El PC se inicializa en 0000, así que la primera instrucción es la de la dirección 0. Al final de cada ciclo avanza solo, sin intervención humana.

![Computador con memoria de instrucciones: el PC entrega la dirección y la memoria devuelve la instrucción](adjuntos/Memoria%20de%20instrucciones.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, `RegA` y `RegB` conectados a la ALU.
> - Arriba a la derecha, la `Instruction Memory`, con una entrada de `Address` y una salida de `Data out`.
> - La salida de datos lleva los bits de control a los registros y a la ALU.
> - El resultado de la ALU vuelve a los registros.

> [!warning] El PC no guarda el resultado
> El PC solo guarda una dirección: en qué instrucción vamos. El resultado de las operaciones vive en los registros, no en el PC.

## Preguntas de repaso

> [!question]- ¿Qué guarda la memoria de instrucciones?
> Las instrucciones del programa, cada una en una dirección. Cada instrucción contiene los bits de control que indican la operación y qué registros se cargan.

> [!question]- ¿Qué pasa con el PC al final de cada ciclo?
> Se incrementa en 1 para apuntar a la instrucción siguiente, salvo que una instrucción de salto lo modifique.

> [!question]- ¿Cuántas instrucciones se pueden direccionar con 4 bits de dirección?
> $2^4 = 16$ instrucciones.

> [!question]- ¿Por qué se dice que el programa es un dato?
> Porque se almacena en memoria como una secuencia de bits, igual que los números. El computador lo lee y lo ejecuta.
