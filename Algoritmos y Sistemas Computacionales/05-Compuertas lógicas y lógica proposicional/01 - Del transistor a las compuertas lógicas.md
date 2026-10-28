---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Compuertas lógicas y lógica proposicional"
tags:
  - algoritmos/compuertas-logicas
  - algoritmos/logica
  - origen/complemento
prerrequisitos:
  - "[[04 - Hexadecimal|Hexadecimal]]"
---

# Del transistor a las compuertas lógicas

Ya sabemos cómo se representan los números y los caracteres. Falta responder una pregunta: ¿cómo hace el computador para operar con ellos? La respuesta pasa por el **transistor**, el **álgebra booleana** y las **compuertas lógicas**, que conectan la física con la lógica.

## La parte física: el transistor

Un **transistor** es un dispositivo semiconductor con tres terminales. Un voltaje aplicado a una entrada permite controlar el voltaje de la salida. Si hay cierto nivel de voltaje, se interpreta como "hay señal" (1); si no hay, "no hay señal" (0).

Esa es la razón física por la que el computador usa binario: un transistor puede estar encendido o apagado, y encadenando millones de ellos se construyen operaciones complejas.

## La parte teórica: Boole y Shannon

En el siglo XIX, **George Boole** desarrolló un sistema formal para analizar proposiciones lógicas. Las proposiciones tienen dos valores de verdad, verdadero (V) o falso (F), y se combinan con las operaciones **not**, **and** y **or**. Ese conjunto de reglas se conoce como **álgebra booleana**.

En 1937, **Claude Shannon** mostró que el álgebra booleana puede usarse para representar valores binarios: verdadero es 1 y falso es 0. Así, las proposiciones lógicas se pueden implementar con circuitos electrónicos.

> [!tip] La idea central
> Un bit es a la vez una señal física (voltaje) y un valor lógico (verdadero/falso). Las compuertas lógicas son el puente entre ambos mundos.

## La parte práctica: las compuertas

Una **compuerta lógica** es un componente electrónico que implementa una operación de Boole. Recibe uno o más bits de entrada y entrega uno o más bits de salida según una tabla.

| Compuerta | Operación | Significado |
|---|---|---|
| NOT | $\neg A$ | Niega la entrada |
| AND | $A \land B$ | Verdadero solo si ambas son verdaderas |
| OR | $A \lor B$ | Verdadero si al menos una es verdadera |
| XOR | $A \oplus B$ | Verdadero si exactamente una es verdadera |

Combinando compuertas se construyen circuitos que suman, comparan, seleccionan y, en última instancia, ejecutan instrucciones.

> [!warning] No confundir OR con XOR
> El OR es inclusivo: $1 \lor 1 = 1$. El XOR es exclusivo: $1 \oplus 1 = 0$, porque no es cierto que *exactamente una* sea verdadera.

## Preguntas de repaso

> [!question]- ¿Por qué el transistor permite representar bits?
> Porque puede estar en dos estados: con voltaje (señal, 1) o sin voltaje (sin señal, 0). Esos dos estados son fáciles de distinguir.

> [!question]- ¿Qué aportó Shannon a la lógica de Boole?
> Mostrar que el álgebra booleana puede representar valores binarios (verdadero = 1, falso = 0) y, por lo tanto, implementarse con circuitos eléctricos.

> [!question]- ¿Qué es una compuerta lógica?
> Un componente electrónico que recibe bits de entrada y produce bits de salida según una operación lógica y su tabla de verdad.

> [!question]- ¿Cuál es la diferencia entre la parte física y la parte lógica de un bit?
> La parte física es el voltaje del transistor; la parte lógica es la interpretación de ese voltaje como verdadero o falso, 1 o 0.

> [!question]- ¿Por qué se dice que estos circuitos son digitales?
> Porque trabajan con valores discretos (0 y 1), no con un rango continuo de voltajes. Cada señal se interpreta como uno de esos dos valores.
