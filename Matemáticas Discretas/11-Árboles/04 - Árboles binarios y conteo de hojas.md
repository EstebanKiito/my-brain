---
ramo: "Matemáticas Discretas"
tema: "Árboles"
tags:
  - discretas/grafos
  - discretas/arboles
  - origen/complemento
prerrequisitos:
  - "[[02 - Hojas, poda y número de aristas de un árbol]]"
  - "[[03 - Árboles con raíz y su terminología]]"
---

# Árboles binarios y conteo de hojas

Los **árboles binarios** son la forma de árbol más usada en computación (búsqueda, ordenamiento, torneos, expresiones). Su restricción es simple, y de ella sale una relación exacta entre hojas y vértices con dos hijos que responde preguntas de conteo sin dibujar nada.

## Definición

Un árbol con raíz es **binario** si todo vértice tiene a lo más dos hijos (equivalentemente, grado a lo más $3$). Se distingue el hijo **izquierdo** del **derecho**, y el árbol cuya raíz es el hijo izquierdo de $v$ con todos sus descendientes es el **subárbol izquierdo** de $v$ (análogo el derecho).

![Árbol binario con subárboles izquierdo y derecho](adjuntos/%C3%81rbol%20binario%20con%20sub%C3%A1rboles%20izquierdo%20y%20derecho.png)

> [!example]- Transcripción de la imagen
> Un árbol binario con la raíz arriba y dos hijos, $u$ (izquierdo) y $w$ (derecho). Se indica que $v$ es el hijo izquierdo de $u$ y que $x$ es el hijo derecho de $w$. Dos regiones encerradas con línea punteada marcan el subárbol izquierdo de $w$ y el subárbol derecho de $w$.

Quitar una hoja a un árbol binario da otro árbol binario: ningún vértice gana hijos.

## Hojas frente a vértices con dos hijos

> [!tip] Teorema
> En un árbol binario, la cantidad de hojas es la cantidad de vértices con exactamente dos hijos más $1$.

**Demostración por inducción en el número de vértices.**
- *Base:* un solo vértice es una hoja y no hay vértices con dos hijos: $1 = 0 + 1$.
- *HI:* un árbol binario con $n$ vértices tiene una hoja más que vértices con dos hijos.
- *TI:* sea $T$ binario con $n + 1$ vértices y $v$ una hoja. $T - v$ tiene $n$ vértices; sea $k$ su cantidad de vértices con dos hijos, y por HI tiene $k + 1$ hojas. Hay dos casos:
  - *$v$ tiene hermano.* El padre de $v$ tenía dos hijos en $T$ y uno en $T - v$. Entonces $T$ tiene $k + 1$ vértices con dos hijos y una hoja más que $T - v$: $k + 2$ hojas. Se cumple $k + 2 = (k + 1) + 1$.
  - *$v$ no tiene hermano.* El padre tenía un hijo en $T$ y pasa a ser hoja en $T - v$ (la hoja $v$ desaparece y el padre aparece): las hojas siguen siendo $k + 1$ y los vértices con dos hijos siguen siendo $k$. Se cumple $k + 1 = k + 1$.

## Aplicación: torneos de eliminación

En un torneo de eliminación simple cada partido enfrenta a dos participantes y el perdedor sale. Se modela como árbol binario: las hojas son los participantes, el padre de dos vértices es el ganador de su partido y la raíz es el campeón. Cada vértice con dos hijos corresponde a un partido; por el teorema hay $n - 1$ partidos con $n$ participantes, sin importar cómo se arme el cuadro.

> [!example]- Ejemplo
> Con $100$ equipos se juegan $99$ partidos. Es coherente con el sentido común: cada partido elimina exactamente a un equipo y deben quedar $99$ eliminados para que haya campeón.

> [!warning] Trampa
> El teorema cuenta vértices con **exactamente** dos hijos. Los vértices con un solo hijo no cambian la diferencia: aportan $0$ a ambos lados.

## Preguntas de repaso

> [!question]- ¿Por qué la prueba separa el caso en que $v$ tiene hermano y el caso en que no?
> Porque quitar $v$ afecta distinto al padre: si había hermano, el padre pasa de dos hijos a uno (y deja de contar); si no, el padre pasa de uno a cero hijos y se vuelve hoja.

> [!question]- ¿Cuántas hojas tiene un árbol binario con $5$ vértices de dos hijos?
> $6$, por el teorema.

> [!question]- ¿Cómo se ve el resultado de los torneos en el árbol?
> Cada partido es un vértice con dos hijos, así que partidos $=$ hojas $- 1 = n - 1$.

> [!question]- ¿Sirve el teorema si algún vértice tiene tres hijos?
> No: la demostración (y el enunciado) suponen a lo más dos hijos. Con tres hijos la relación cambia.
