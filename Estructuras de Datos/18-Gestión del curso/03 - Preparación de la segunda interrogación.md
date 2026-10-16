---
ramo: "Estructuras de Datos"
tema: "Gestión del curso"
tags:
  - edd
  - gestion-del-curso
  - repaso
  - origen/complemento
prerrequisitos:
  - "[[03 - Factor de carga y rehashing]]"
  - "[[04 - Comparación de técnicas de diseño]]"
  - "[[05 - Componentes fuertemente conectadas y Kosaraju]]"
---

# Preparación de la segunda interrogación

La segunda interrogación cubre **diccionarios** (tablas de hash y árboles B+), las **estrategias algorítmicas** (backtracking, algoritmos codiciosos y programación dinámica) y **DFS** en grafos. En las técnicas, las preguntas suelen ser de **modelamiento**: reconocer qué estrategia pide un problema y plantearla bien.

## Diccionarios

- **Tablas de hash:** son una estructura **sin orden**. Hay que dominar la [[01 - Función de hash y tablas de hash|función de hash modular]] y sus propiedades deseables, el impacto en las colisiones, la [[02 - Resolución de colisiones|comparación entre encadenamiento y sondeo]] y el [[03 - Factor de carga y rehashing|factor de carga]].
  - Con $\lambda = 1$ y encadenamiento, las listas son cortas. La complejidad de las colisiones importa cuando $\lambda$ es alto.
  - Una pregunta difícil: **eliminar** en una tabla con sondeo lineal.
  - Las preguntas de diagnóstico ("la tabla dejó de comportarse bien") apuntan al **factor de carga**, y la solución suele ser rehashing o **combinar** estructuras. Por ejemplo: una tabla principal de pasajeros y otra secundaria de tickets que apunta a la primera, para buscar pasajeros por vuelo y equipaje por pasajero.
- **Árboles B+:** son la estructura para buscar en disco o en bases de datos (encontrar el bloque que tiene el dato). Con el orden $d$ se puede razonar sobre la altura: el árbol solo crece cuando se llena la raíz y siempre está balanceado. Puede haber preguntas que mezclen un B+ con consultas SQL o con dos índices distintos.

## Estrategias algorítmicas

| Técnica | Qué la caracteriza | Pregunta típica |
|---|---|---|
| [[02 - Algoritmo de backtracking\|Backtracking]] | Puede arrepentirse y cambiar de decisión | Identificar **variables, dominios y restricciones**; aplicar poda, propagación o heurística (puede bastar explicarlo en palabras) |
| [[01 - Estrategia codiciosa\|Codicioso]] | Toma la mejor decisión aparente y no se arrepiente | **Demostrar con un contraejemplo** que una estrategia no sirve (a veces basta con $n = 3$ o 5) |
| [[01 - Subproblemas solapados y subestructura óptima\|Programación dinámica]] | El problema se descompone en subproblemas que se solapan | **Plantear la ecuación de recurrencia** y el algoritmo; no confundir qué se optimiza (valor en las charlas, cantidad de monedas en el vuelto, cantidad de vehículos en la barcaza) |

> [!tip] Relaciones que se preguntan
> - **De backtracking a codicioso:** no retroceder y elegir con una heurística, es decir, la mejor variable con su mejor valor.
> - Si la estrategia codiciosa no es óptima, backtracking con esa heurística **igual** encuentra una solución.
> - Problemas típicos de backtracking: laberintos, carga de mochilas y barcazas, y **estibar carga** (que ambos lados de un camión pesen lo mismo). La pregunta suele ser larga y exige concentrarse en el modelamiento más que en el pseudocódigo.

## DFS

DFS es un tema flexible: detecta ciclos, construye el orden topológico y encuentra componentes fuertemente conectadas con Kosaraju. Las preguntas suelen pedir **modificar el recorrido**, para lo que hay que entender que [[03 - Tiempos de DFS y tipos de aristas|DFS genera árboles]] (varios en un mismo recorrido), que hay **distintos tipos de aristas** y que el orden de término da el [[04 - Orden topológico|orden topológico]]. Un ejemplo es identificar **atajos** (aristas hacia adelante) que permiten recorrer en menos pasos. El patrón general es reconocer el problema, modelarlo como grafo y aplicar DFS o Kosaraju.

## Preguntas de repaso

> [!question]- ¿Cuál es la forma estándar de demostrar que una estrategia codiciosa no es óptima?
> Dar un contraejemplo: una instancia pequeña en que la estrategia entrega una solución peor que otra que se puede mostrar.

> [!question]- Una tabla de hash que funcionaba bien empieza a responder de forma errática al crecer los datos. ¿Qué se diagnostica y qué se propone?
> Un factor de carga demasiado alto (muchas colisiones en algunas celdas). Se propone rehashing a una tabla más grande con una nueva función de hash.

> [!question]- ¿Qué tres elementos hay que identificar al modelar un problema para backtracking?
> Las variables, el dominio de cada una y las restricciones que deben cumplir las asignaciones.
