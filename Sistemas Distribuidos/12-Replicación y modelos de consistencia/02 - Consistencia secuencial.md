---
ramo: "Sistemas Distribuidos"
tema: "Replicación y modelos de consistencia"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Replicación de datos y modelos de consistencia]]"
---

# Consistencia secuencial

La **consistencia secuencial** (Lamport, 1979) pide que el sistema distribuido se comporte **como si** hubiera un solo procesador que ejecuta las operaciones de todos, una por una. No importa en qué orden se intercalen los procesos, siempre que **todos los nodos vean la misma intercalación** y se respete el orden interno de cada proceso.

## Definición

> [!tip] Regla
> El resultado de cualquier ejecución es el mismo que si las operaciones de todos los procesos se ejecutaran en **algún orden secuencial**, y cada proceso individual respeta ese orden. Cualquier intercalación válida es aceptable, pero **todos ven la misma**.

No se exige que el orden coincida con el tiempo real: basta con que **exista** una secuencia compatible con lo que vio cada nodo.

## Ejemplos

![Dos ejecuciones secuencialmente consistentes](adjuntos/Dos%20ejecuciones%20secuencialmente%20consistentes.png)

> [!example]- Transcripción de la imagen
> A escribe $W_A(x)=2$ y F escribe $W_F(x)=5$. En la primera ejecución, H y S leen $x \rightarrow 5$ y luego $x \rightarrow 2$; en la segunda, ambos leen 2 y luego 5. Las dos son secuencialmente consistentes.

En la primera, la secuencia es $W_F(x)=5, R, R, W_A(x)=2, R, R$; en la segunda, al revés. Lo importante es que H y S coinciden.

![Ejecución no consistente secuencialmente](adjuntos/Ejecuci%C3%B3n%20no%20consistente%20secuencialmente.png)

> [!example]- Transcripción de la imagen
> Las mismas escrituras, pero H lee 2 y luego 5, mientras S lee 5 y luego 2 (recuadro naranjo). "No es consistente secuencialmente. ¿Cuál fue primero, $W_A(x)=2$ o $W_F(x)=5$?"

H cree que la última escritura fue la de F y S cree que fue la de A: no existe un orden único que explique ambas lecturas.

## El problema: muchas opciones válidas

![Seis órdenes válidos de escrituras](adjuntos/Seis%20%C3%B3rdenes%20v%C3%A1lidos%20de%20escrituras.png)

> [!example]- Transcripción de la imagen
> A hace $W_A(x)=1$, $W_A(y)=1$ y $R_A(x)$; F hace $W_F(y)=2$, $W_F(x)=2$ y $R_F(y)$. "Existen 6 formas de ordenar $W_A(x)=1$, $W_A(y)=1$, $W_F(y)=2$, $W_F(x)=2$ que serán secuencialmente consistentes."

Con dos escrituras por nodo y el orden interno fijo, hay $\binom{4}{2} = 6$ intercalaciones, y todas son secuencialmente consistentes. Cada una da lecturas finales distintas: el modelo no dice **cuál** ocurrirá, solo que todos verán la misma.

## Verificación por fuerza bruta

Para saber si una ejecución es secuencialmente consistente, basta buscar una intercalación que respete el orden de cada nodo y en que cada lectura devuelva la última escritura anterior. Un programa en Python que prueba todas las intercalaciones confirmó los ejemplos: la primera ejecución sí lo es, la de H y S en órdenes distintos no, y con dos escrituras por nodo hay exactamente 6 órdenes.

```python
def secuencial(procesos):
    for orden in intercalaciones(procesos):          # respetan el orden de cada nodo
        mem, ok = {}, True
        for op, var, val in orden:
            if op == "W": mem[var] = val
            elif mem.get(var, 0) != val: ok = False; break
        if ok: return orden                           # existe una secuencia válida
    return None
```

> [!warning] Secuencial no es "en orden de tiempo"
> Una escritura que ocurrió antes en el reloj puede quedar después en la secuencia. Si se exige respetar el tiempo real, el modelo es la [[03 - Consistencia fuerte o linealizable|consistencia fuerte]].

## Preguntas de repaso

> [!question]- ¿Qué tienen que ver todos los nodos para que haya consistencia secuencial?
> La misma intercalación de las operaciones, que además respete el orden en que cada proceso emitió las suyas.

> [!question]- ¿Por qué H leyendo 2→5 y S leyendo 5→2 rompe la consistencia secuencial?
> Porque cada uno implica un orden distinto de las dos escrituras. No hay una única secuencia que explique ambas lecturas.

> [!question]- ¿Cuántos órdenes válidos hay para tres escrituras de A y una de F?
> $\binom{4}{1} = 4$: la escritura de F puede ir en cualquiera de las 4 posiciones, y las de A mantienen su orden.
