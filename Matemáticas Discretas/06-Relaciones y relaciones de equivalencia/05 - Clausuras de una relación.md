---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[04 - Propiedades de las relaciones]]"
---

# Clausuras de una relación

Con frecuencia una relación casi tiene una propiedad: la tabla de vuelos directos no es transitiva, pero interesa saber a qué ciudades se llega con escalas. La **clausura** repara la relación agregando lo mínimo necesario para que cumpla la propiedad, sin inventar pares de más.

## Definición

Sea $\varphi$ una propiedad de relaciones (refleja, simétrica o transitiva). La **clausura $\varphi$** de $R$ es la menor relación que contiene a $R$ y cumple $\varphi$. Es decir, una relación $R^\varphi$ tal que:

1. $R \subseteq R^\varphi$,
2. $R^\varphi$ cumple $\varphi$,
3. si $S$ cumple $\varphi$ y $R \subseteq S$, entonces $R^\varphi \subseteq S$.

La condición 3 es la que garantiza que no sobra nada: cualquier otra relación que repare $R$ contiene a la clausura.

> [!tip] Cómo se calculan
> - Clausura refleja: $R \cup D$ (se agregan los bucles que faltan).
> - Clausura simétrica: $R \cup R^{-1}$ (se agrega la vuelta de cada flecha).
> - Clausura transitiva: $R^t = \bigcup_{i \ge 1} R^i = R \cup R^2 \cup R^3 \cup \cdots$ (todos los pares unidos por un camino).

Con $A = \{1, 2, 3, 4\}$ y $R = \{(1,2), (2,3), (3,4)\}$:
- la clausura refleja agrega $(1,1), (2,2), (3,3), (4,4)$;
- la simétrica agrega $(2,1), (3,2), (4,3)$;
- la transitiva agrega $(1,3), (2,4), (1,4)$ y queda $\{(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)\}$.

## Clausura transitiva paso a paso

![Clausura transitiva paso 1 pares originales](adjuntos/Clausura%20transitiva%20paso%201%20pares%20originales.png)

> [!example]- Transcripción de la imagen
> Cuatro puntos $0, 1, 2, 3$ con tres flechas: de $0$ a $1$, de $1$ a $2$ y de $2$ a $3$. Es la relación $R = \{(0,1), (1,2), (2,3)\}$.

Como hay flechas $0 \to 1 \to 2$, la clausura debe contener $(0, 2)$; de $0 \to 2 \to 3$ sale $(0, 3)$ y de $1 \to 2 \to 3$ sale $(1, 3)$. Nada más hace falta, porque la relación resultante ya es transitiva.

![Clausura transitiva paso 2 relación completada](adjuntos/Clausura%20transitiva%20paso%202%20relaci%C3%B3n%20completada.png)

> [!example]- Transcripción de la imagen
> Los mismos cuatro puntos, ahora con seis flechas: las tres originales más $0 \to 2$, $0 \to 3$ y $1 \to 3$. Cada punto alcanza a todos los que están más adelante en la cadena $0, 1, 2, 3$.

## Por qué la unión de potencias es la menor

$R^t$ contiene a $R$ ($i = 1$). Es transitiva: si $(x, y) \in R^j$ y $(y, z) \in R^k$, entonces $(x, z) \in R^{j+k}$. Y es mínima: si $S$ es transitiva y $R \subseteq S$, por inducción en $i$ se cumple $R^i \subseteq S$, porque $(x, z) \in R^{i+1}$ significa $(x, y) \in R^i \subseteq S$ y $(y, z) \in R \subseteq S$, y la transitividad de $S$ da $(x, z) \in S$. Si $A$ es finito con $n$ elementos basta tomar hasta $R^n$, porque un camino más largo repite un punto y se puede acortar. En matrices, $M_{R^t} = M_R \vee M_R^2 \vee \cdots \vee M_R^n$.

## Combinar clausuras: la menor equivalencia

Para hacer una relación de equivalencia hay que combinar las tres reparaciones. La menor equivalencia que contiene a $R$ es

$$(R \cup R^{-1} \cup D)^t,$$

y sus pares son los que están unidos por un camino de flechas recorridas en cualquier sentido. Para $R = \{(1,2), (2,3)\}$ sobre $\{1,2,3\}$ resulta $A^2$ completo: los tres elementos quedan en una sola clase.

> [!warning] El orden importa
> La transitiva debe ir **al final**. Con $R = \{(1,2), (1,3)\}$, la clausura transitiva es $R$ misma y al hacerla simétrica queda $2 \to 1 \to 3$ sin el par $(2, 3)$: el resultado no es transitivo. En cambio la refleja y la simétrica no se estorban entre sí.

## Preguntas de repaso

> [!question]- ¿Qué condición de la definición de clausura impide agregar pares innecesarios?
> La minimalidad: toda relación que contenga a $R$ y cumpla la propiedad debe contener a la clausura. Si se agregara un par de más, otra relación más chica la violaría.

> [!question]- ¿Para qué sirve la clausura transitiva de la relación «hay un vuelo directo»?
> Para obtener la relación «se puede llegar con escalas»: contiene todos los pares unidos por un camino de vuelos de cualquier largo.

> [!question]- ¿Cuántas potencias de $R$ hay que unir en un conjunto de $n$ elementos?
> Hasta $R^n$: un camino de largo mayor que $n$ pasa dos veces por un mismo punto, y al quitar ese ciclo queda un camino más corto con los mismos extremos.

> [!question]- ¿Por qué la menor equivalencia usa $R \cup R^{-1}$ antes de la clausura transitiva?
> Porque la unión ya es simétrica, y una clausura transitiva de una relación simétrica sigue siendo simétrica (el camino invertido es otro camino). Si se invierte el orden, la simetría puede destruir la transitividad.
