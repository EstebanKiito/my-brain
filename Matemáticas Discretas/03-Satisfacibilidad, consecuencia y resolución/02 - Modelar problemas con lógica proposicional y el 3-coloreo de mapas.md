---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Satisfacibilidad de fórmulas y tautologías proposicionales]]"
---

# Modelar problemas con lógica proposicional y el 3-coloreo de mapas

Muchos problemas ajenos a la lógica se pueden resolver traduciéndolos a una fórmula $\varphi$ tal que **el problema tiene solución si y solo si $\varphi$ es satisfacible**. Esta nota muestra el método con el ejemplo clásico: colorear un mapa con tres colores.

## El problema

Un mapa de $n$ países es **3-coloreable** si se puede pintar cada país de rojo, azul o verde sin que dos países vecinos tengan el mismo color. Se pide construir $\varphi$ que sea satisfacible exactamente cuando el mapa es 3-coloreable.

## Estrategia en tres pasos

1. **Definir las variables.** Unas son datos del problema y otras son las incógnitas.
2. **Escribir las restricciones** como fórmulas y unirlas con $\land$.
3. **Demostrar las dos direcciones** del "si y solo si": una solución produce una valuación que satisface $\varphi$, y una valuación que satisface $\varphi$ produce una solución.

## Paso 1: variables

- $p_{ij}$ vale $1$ si los países $i$ y $j$ son adyacentes. Se conocen de antemano a partir del mapa.
- $r_i, b_i, g_i$ valen $1$ si el país $i$ se pinta rojo, azul o verde. Son las incógnitas: la valuación que las satisface será la coloración.

## Paso 2: restricciones

- **Un solo color por país:** $\varphi_C = \bigwedge_{i=1}^{n}\big[(r_i \lor b_i \lor g_i) \land (r_i \to \neg b_i \land \neg g_i) \land (b_i \to \neg r_i \land \neg g_i) \land (g_i \to \neg r_i \land \neg b_i)\big]$. La primera disyunción asegura al menos un color; las implicaciones, a lo más uno.
- **Vecinos con colores distintos:** $\varphi_D = \bigwedge_{i,j}\big[p_{ij} \to (r_i \to \neg r_j) \land (b_i \to \neg b_j) \land (g_i \to \neg g_j)\big]$.
- **Datos del mapa:** $\varphi_M = \bigwedge_{(i,j) \in A} p_{ij} \land \bigwedge_{(i,j) \notin A} \neg p_{ij}$, donde $A$ es la lista de pares adyacentes. Fija las variables conocidas.

La fórmula final es $\varphi = \varphi_C \land \varphi_D \land \varphi_M$.

## Paso 3: por qué funciona

($\Rightarrow$) Dada una coloración válida, se define $\sigma(r_i) = 1$ si $i$ es rojo (y análogo para $b_i, g_i$) y $\sigma(p_{ij}) = 1$ si son adyacentes. Cada país tiene exactamente un color, así que $\sigma(\varphi_C) = 1$; en $\varphi_D$ solo importan los pares adyacentes, y sus colores difieren, luego los consecuentes son verdaderos; $\varphi_M$ se cumple por construcción.

($\Leftarrow$) Si $\sigma(\varphi) = 1$, entonces $\sigma(\varphi_C) = 1$ da a cada país exactamente un color. Para países adyacentes $i, j$ (por $\varphi_M$, $\sigma(p_{ij}) = 1$), si $\sigma(r_i) = 1$ la implicación de $\varphi_D$ fuerza $\sigma(r_j) = 0$; lo mismo con los otros colores. Los vecinos no comparten color.

## Ejemplos chicos

Con tres países mutuamente vecinos (un triángulo) hay coloración: uno de cada color, y $\varphi$ es satisfacible. Con cuatro países mutuamente vecinos no hay coloración posible con tres colores, y $\varphi$ resulta insatisfacible (se comprobó revisando todas las valuaciones de las variables de color).

> [!warning] Las dos direcciones son obligatorias
> Mostrar solo que una solución satisface $\varphi$ no basta: también hay que mostrar que toda valuación que satisface $\varphi$ entrega una solución real, y por eso las restricciones "a lo más un color" son necesarias.

## Preguntas de repaso

> [!question]- ¿Para qué sirve $\varphi_M$ si las $p_{ij}$ ya se conocen?
> Una fórmula solo "sabe" lo que dice: sin $\varphi_M$, la valuación podría asignar a $p_{ij}$ cualquier valor y satisfacer $\varphi_D$ trivialmente. $\varphi_M$ las ata al mapa concreto.

> [!question]- ¿Qué pasaría si se omitieran las implicaciones de "a lo más un color"?
> Un país podría tener dos colores a la vez. Entonces la valuación satisfaría $\varphi$ sin producir una coloración, y la dirección ($\Leftarrow$) fallaría.

> [!question]- ¿Por qué en $\varphi_D$ solo importan los pares adyacentes?
> Si $p_{ij} = 0$ el antecedente es falso y la implicación vale $1$ sin imponer nada sobre los colores.
