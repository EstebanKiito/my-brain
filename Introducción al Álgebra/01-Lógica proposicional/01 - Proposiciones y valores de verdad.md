---
ramo: "Introducción al Álgebra"
tema: "Lógica proposicional"
tags:
  - intro-algebra/logica-proposicional
  - origen/complemento
prerrequisitos: []
---

# Proposiciones y valores de verdad

La matemática se escribe en un lenguaje donde cada afirmación es verdadera o falsa, sin ambigüedad. Antes de resolver o demostrar, conviene fijar la unidad mínima de ese lenguaje: la **proposición**. Todo razonamiento —un teorema, una demostración, un "V o F"— se construye encadenando proposiciones, así que su definición es el punto de partida de la lógica proposicional.

## Qué es una proposición

Una proposición es una frase declarativa que es verdadera o falsa, pero no ambas cosas a la vez. Si es verdadera, su **valor de verdad** es V; si es falsa, F. Se denotan con letras minúsculas $p, q, r, s, \dots$

> [!tip] Proposición
> Una **proposición** es una frase o expresión declarativa (no necesariamente matemática) que es **verdadera o falsa, y no ambas**. Su valor de verdad es V si es verdadera y F si es falsa.

Lo importante es que el valor de verdad exista y esté bien definido. Son proposiciones $p$: "murió el roto Quezada", $q$: "estoy en medio de un triángulo", $r$: "$2+1=5$" (cuyo valor es F) y $s$: "$1 \ge 0$" (cuyo valor es V). Cada una es declarativa y se le puede asignar un único valor de verdad.

## Qué no es una proposición

No toda frase es proposición. Las órdenes, preguntas y exclamaciones no lo son porque no afirman algo que pueda ser V o F:

- "Siéntate" es una orden, no una proposición.
- "¿Está lloviendo?" es una pregunta.
- "¡Estudien!" es una exclamación.

> [!warning] Frases con variables libres
> "$x > 3$" no es una proposición mientras $x$ no esté fijado: no se puede decir si es V o F. Para que una frase con variables sea proposición hay que asignar un valor a cada variable, o bien cuantificarla (eso se estudia en el tema de cuantificadores).

## Preguntas de repaso

> [!question]- Dé un ejemplo de proposición verdadera, uno de falsa y uno de frase que no sea proposición.
> Verdadera: "$2$ es un número par". Falsa: "$2+1=5$". No proposición: "Cierra la puerta" (es una orden, no declara nada).

> [!question]- ¿Por qué "esta frase es falsa" no es una proposición?
> Porque si fuera verdadera entonces sería falsa, y si fuera falsa entonces sería verdadera. No tiene un valor de verdad único y bien definido: viola la condición "V o F, no ambas".

> [!question]- ¿"$n$ es par" es una proposición? ¿Y "existe un natural $n$ que es par"?
> La primera no: depende del valor de $n$ (variable libre). La segunda sí, y es verdadera, porque el cuantificador "existe" fija el alcance de $n$ y convierte la frase en una afirmación completa.
