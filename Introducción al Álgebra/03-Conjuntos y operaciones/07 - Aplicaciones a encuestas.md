---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[06 - Álgebra de conjuntos y cardinalidad]]"
---

# Aplicaciones a encuestas

Los problemas de encuestas ("cuántos estudian X o Y") se resuelven traduciendo el enunciado a **regiones de un diagrama de Venn** con sus cardinalidades. Cada condición del problema da una ecuación sobre esas regiones, y resolverlas responde todas las preguntas de una vez.

## Plantear el diagrama de Venn

**Ejemplo.** Una delegación de $44$ deportistas participa en salto alto ($S$), $100$ metros planos ($P$) y salto con garrocha ($G$):

- $24$ participan en salto alto;
- $18$ en salto alto y/o $100$ m, pero no en garrocha;
- $25$ en garrocha;
- $7$ en las tres disciplinas;
- $9$ en $100$ m, pero no en garrocha;
- $12$ no participan ni en salto alto ni en $100$ m;
- $15$ en salto alto, pero no en garrocha.

Cada región del diagrama recibe una letra que representa su cardinalidad.

![Diagrama de Venn del problema de los deportistas](adjuntos/Diagrama%20de%20Venn%20del%20problema%20de%20los%20deportistas.png)

> [!example]- Transcripción de la imagen
> Dentro del universo $U$ hay tres círculos: $S$ (salto alto, arriba a la izquierda), $P$ (100 m, arriba a la derecha) y $G$ (garrocha, abajo). Las regiones muestran sus cardinalidades: $9$ (solo salto alto), $6$ (salto alto y 100 m), $3$ (solo 100 m), $2$ (salto alto y garrocha), $7$ (las tres, en el centro), $5$ (100 m y garrocha), $11$ (solo garrocha) y $1$ fuera de los círculos (no participa en ninguna).

## Traducir a ecuaciones

Cada dato es una ecuación sobre las regiones $a$ (solo $S$), $b$ ($S \cap P$ sin $G$), $c$ (solo $P$), $d$ ($S \cap G$ sin $P$), $e$ (las tres), $f$ ($P \cap G$ sin $S$), $g$ (solo $G$) y $h$ (ninguna):

$$
\begin{aligned}
a+b+c+d+e+f+g+h &= 44, & a+b+d+e &= 24, & a+b+c &= 18, \\
d+e+f+g &= 25, & e &= 7, & b+c &= 9, & g+h &= 12, & a+b &= 15.
\end{aligned}
$$

Sustituyendo: de $a+b=15$ y $a+b+c=18$ sale $c = 3$; de $b+c=9$ sale $b = 6$; de $a+b=15$ sale $a = 9$; de $a+b+d+e=24$ sale $d = 2$; de $a+b+c+d+e+f+g+h=44$ y $g+h=12$ sale $f = 5$; de $d+e+f+g=25$ sale $g = 11$; y de $g+h=12$ sale $h = 1$.

**Respuestas.** (i) No participa en ninguna disciplina: $h = 1$. (ii) Salto alto y garrocha: $d + e = 9$. (iii) Más de un deporte: $b + d + e + f = 20$.

> [!tip] Método de la región
> Asigne una letra a cada región del diagrama, traduzca cada dato a una ecuación sobre esas letras y resuelva. Con las regiones determinadas, cualquier pregunta ("solo $X$", "al menos uno", "ninguno") se responde sumando las letras correspondientes.

## Preguntas de repaso

> [!question]- ¿Qué representa la letra $e$ en el diagrama y cuánto vale?
> La triple intersección $S \cap P \cap G$: los que hacen las tres disciplinas. Vale $e = 7$ (dato directo del problema).

> [!question]- ¿Cómo se calcula cuántos participan en "salto alto y garrocha"?
> Sumando las regiones que están en $S$ y en $G$ a la vez: $d + e = 2 + 7 = 9$ (con o sin los 100 m).

> [!question]- ¿Qué región corresponde a "no participa en salto alto ni en 100 m"?
> La región fuera de $S$ y de $P$, que es $g + h$ (solo garrocha más ninguno). El problema da $g + h = 12$.

> [!question]- ¿Por qué "más de un deporte" suma $b + d + e + f$?
> Porque son las regiones en exactamente dos disciplinas ($b$, $d$, $f$) más la triple ($e$). Quedan fuera los que hacen una sola ($a$, $c$, $g$) y los que no hacen ninguna ($h$).
