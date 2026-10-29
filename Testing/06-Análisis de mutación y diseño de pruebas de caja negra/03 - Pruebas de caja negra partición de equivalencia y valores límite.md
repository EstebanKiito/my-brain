---
ramo: "Testing"
tema: "Análisis de mutación y diseño de pruebas de caja negra"
tags:
  - testing/analisis-de-mutacion-y-diseno-de-pruebas-de-caja-negra
  - origen/complemento
prerrequisitos:
  - "[[Testing/01-Fundamentos del testing de software/03 - Los siete principios del testing de software|Los siete principios del testing de software]]"
---

# Pruebas de caja negra, partición de equivalencia y valores límite

## De la caja blanca a la caja negra (*Black-Box Testing*)

Hasta aquí diseñamos pruebas mirando el interior del código fuente (caja blanca). En el **testing de caja negra** cerramos el código y nos ponemos en los zapatos del usuario final o del analista de calidad: **solo conocemos la especificación de requerimientos y observamos las entradas y salidas externas**.

¿Por qué es indispensable combinar caja negra con caja blanca? Porque si un desarrollador olvidó programar una regla de negocio o malinterpretó un rango de la especificación, el código tendrá un defecto que las pruebas guiadas por cobertura jamás notarán, pero que un caso de prueba derivado directamente del documento de requerimientos destapará de inmediato.

---

## 1. Partición de Equivalencia (*Equivalence Partitioning*, EP)

Como el principio 2 del testing nos recuerda que probar todas las entradas es imposible, la **Partición de Equivalencia (PE)** divide el dominio de entrada en subconjuntos disjuntos llamados **clases o particiones de equivalencia** tales que **el sistema debería tratar a todos los valores dentro de una misma partición exactamente de la misma manera**.

* **Supuesto clave:** si un valor representante de una partición funciona correctamente, asumimos que todos los demás valores de esa partición también funcionarán; y si falla, asumimos que toda la partición falla.
* **Particiones válidas vs. inválidas:**
  * **Clases válidas:** rangos o grupos de entradas que el sistema debe aceptar y procesar normalmente. Pueden combinarse varias en un mismo caso de prueba.
  * **Clases inválidas:** entradas fuera de rango, negativas o de tipo incorrecto que el sistema debe rechazar. **Deben probarse siempre de forma individual** (una sola entrada inválida por test) para que el rechazo de una condición no enmascare un defecto en otra.

---

## 2. Análisis de Valores Límite (*Boundary Value Analysis*, BVA)

Los programadores cometemos la gran mayoría de los errores en las **fronteras** entre particiones (por ejemplo, escribir `<` en vez de `<=`, o equivocarse por una unidad —errores *off-by-one*). El **Análisis de Valores Límite (AVL / BVA)** extiende la partición de equivalencia exigiendo probar explícitamente los extremos de cada partición ordenada.

En el curso distinguimos dos niveles de rigor para cada límite propio (inferior y superior) de cada partición:

| Variante de BVA | ¿Qué puntos genera por cada límite de una partición? | Detección de *off-by-one* y costo |
| :--- | :--- | :--- |
| **Two-Point BVA** (2 puntos) | **`[valor en el límite, valor justo fuera de la partición]`** (un punto a cada lado de la frontera). | Costo bajo; recomendado para sistemas de riesgo normal junto con EP. |
| **Three-Point BVA** (3 puntos) | **`[justo antes, valor en el límite, justo después]`** para el mínimo y el máximo propios de cada partición. | Más casos de prueba, pero máxima detección en sistemas críticos (y descubre *gaps* cuando una partición termina en $100$ y la siguiente empieza en $101$). |

---

## Ejercicios resueltos paso a paso

### Caso 1: Cuenta bancaria con decimales (Two-Point vs. Three-Point)

Una cuenta de ahorros paga $3\%$ de interés para saldos de $\$0.00$ a $\$100.00$, $5\%$ de $\$100.01$ a $\$999.99$, y $7\%$ de $\$1000.00$ en adelante (con paso mínimo de $\$0.01$):
* **Particiones ($4$ en total):** Inválida ($< \$0.00$, rep. `-50`), Válida $3\%$ ($[0.00, 100.00]$, rep. `50`), Válida $5\%$ ($[100.01, 999.99]$, rep. `500`) y Válida $7\%$ ($\ge 1000.00$, rep. `1500`).
* **Two-Point BVA (eliminando duplicados):** **`{-0.01, 0.00, 100.00, 100.01, 999.99, 1000.00}`** ($6$ casos de prueba).
* **Three-Point BVA (eliminando duplicados):** para cada borde generamos `[antes, lím, después]`, obteniendo **`{-0.02, -0.01, 0.00, 0.01, 99.99, 100.00, 100.01, 100.02, 999.98, 999.99, 1000.00, 1000.01}`** ($12$ casos de prueba).

### Caso 2: Plataforma de streaming por edad (Ejercicio de Interrogación)

Una plataforma clasifica según la edad entera en años: $< 13 \to$ familiar; $13\text{–}17 \to$ junior; $18\text{–}64 \to$ estándar; $\ge 65 \to$ senior.

| Clase de equivalencia | Rango / Condición | Representante (EP) | Límites propios | Puntos generados (Two-Point BVA) |
| :--- | :---: | :---: | :---: | :---: |
| **Inválida 1** (edad negativa) | $(-\infty, -1]$ | `-2` | sup: `-1` | `-1, 0` |
| **Inválida 2** (tipo no entero) | Decimales, texto, `None` | `"abc"` | No aplica | — |
| **Válida 1** (familiar) | $[0, 12]$ | `7` | inf: `0`, sup: `12` | `-1, 0` y `12, 13` |
| **Válida 2** (junior) | $[13, 17]$ | `15` | inf: `13`, sup: `17` | `12, 13` y `17, 18` |
| **Válida 3** (estándar) | $[18, 64]$ | `30` | inf: `18`, sup: `64` | `17, 18` y `64, 65` |
| **Válida 4** (senior) | $[65, +\infty)$ | `70` | inf: `65` | `64, 65` |

Al unir y eliminar duplicados, el conjunto final de **Two-Point BVA** consta exactamente de **$8$ valores**: **`{-1, 0, 12, 13, 17, 18, 64, 65}`**.

---

## Preguntas de repaso

> [!question]- Si al aplicar Análisis de Valores Límite (AVL) ya estamos probando extremos que pertenecen a cada partición, ¿por qué se recomienda probar igualmente un representante central de cada Partición de Equivalencia (PE) por separado?
> Por dos razones prácticas: (1) si solo probamos el borde y falla, no sabemos si toda la partición está rota (ej. falta el bloque `if` completo) o si es únicamente un error *off-by-one* en el signo `<=`; y (2) los valores centrales representan el uso típico de los usuarios reales, dando confianza sobre el comportamiento normal del sistema.

> [!question]- ¿Por qué las particiones inválidas deben probarse siempre de forma individual (una sola entrada inválida por caso de prueba) en lugar de combinar varias entradas inválidas en un mismo test?
> Para evitar el **enmascaramiento de defectos**: si enviamos en un mismo formulario `edad = -5` y `correo = "sin_arroba"`, el sistema probablemente abortará en la primera validación (`edad inválida`) y nunca ejecutará la validación del correo. Si el validador de correo estaba roto, el test pasaría igual sin detectar el bug.

> [!question]- Un requisito de trenes dice: «Se cobra tarifa completa antes de las 9:30 AM y entre las 4:00 PM y las 7:30 PM; el boleto *saver* está disponible entre las 9:30 AM y las 4:00 PM, y después de las 7:30 PM». ¿Qué ambigüedad de borde revela aplicar BVA sobre este enunciado?
> Revela que los bordes exactos **$4:00\text{ PM}$** y **$7:30\text{ PM}$** están mal especificados o solapados: a las $4:00\text{ PM}$ («entre 9:30 AM y 4:00 PM» vs. «después de las 4:00 PM») y a las $7:30\text{ PM}$ («hasta las 7:30 PM» vs. «después de las 7:30 PM») no queda claro en el lenguaje natural si el minuto exacto incluye o excluye la tarifa *saver*. Aplicar BVA obliga a aclarar la especificación antes de programar.

