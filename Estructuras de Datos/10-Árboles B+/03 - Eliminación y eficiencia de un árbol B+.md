---
ramo: "Estructuras de Datos"
tema: "Árboles B+"
tags:
  - edd
  - arbol-b-plus
  - eliminacion
  - bulk-loading
  - origen/complemento
prerrequisitos:
  - "[[02 - Inserción en un árbol B+]]"
---

# Eliminación y eficiencia de un árbol B+

Eliminar es el espejo de insertar: si una hoja queda **con menos de $d$ llaves** (bajo el 50 %), hay que **redistribuir** con un hermano o, si no se puede, fusionar nodos (**unsplit**). La fusión puede propagarse hacia arriba igual que el split.

```
Eliminar(k):
    P <- BusquedaEnArbol(k, raiz)
    if |P| >= d + 1:
        eliminar k de P                   // sigue con al menos d llaves
    else:
        eliminar k de P y rebalancear [P - k]:
            si un hermano tiene más de d llaves -> redistribuir
            si no -> unsplit (fusionar con el hermano) y repetir en el padre
```

## Ejemplo con $d = 2$

![Eliminación - árbol inicial](adjuntos/Eliminaci%C3%B3n%20-%20%C3%A1rbol%20inicial.png)

> [!example]- Transcripción de la imagen
> "Para eliminar el elemento 19*": raíz 17; directorios 5, 13 y 24, 30; hojas 2* 3* | 5* 7* 8* | 14* 16* | 19* 20* 22* | 24* 27* 29* | 33* 34* 38* 39*.

![Eliminación de 19](adjuntos/Eliminaci%C3%B3n%20de%2019.png)

> [!example]- Transcripción de la imagen
> La hoja queda 20* 22* (resaltada). "Podemos eliminar 19* sin problemas (#-data entries > 2)".

**Eliminar 20** deja la hoja con un solo dato:

![Eliminación de 20 deja una hoja con poca ocupación](adjuntos/Eliminaci%C3%B3n%20de%2020%20deja%20una%20hoja%20con%20poca%20ocupaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> La hoja queda solo con 22* (resaltada). "Debemos hacer redistribución o 'unsplit' de los nodos".

![Eliminación de 20 - redistribución con el hermano](adjuntos/Eliminaci%C3%B3n%20de%2020%20-%20redistribuci%C3%B3n%20con%20el%20hermano.png)

> [!example]- Transcripción de la imagen
> El hermano 24* 27* 29* le presta el 24: las hojas quedan 22* 24* y 27* 29*, y en el directorio el separador pasa de 24 a 27 (resaltado). No hubo que subir nada más.

**Eliminar 22** deja otra vez una hoja con un dato, pero ahora el hermano tiene justo $d$ llaves y no puede prestar:

![Eliminación de 22 - hoja con poca ocupación](adjuntos/Eliminaci%C3%B3n%20de%2022%20-%20hoja%20con%20poca%20ocupaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> La hoja queda solo con 24* (resaltada), junto a 27* 29*. La raíz 17 aparece marcada. "Necesitamos hacer un 'unsplit' de los nodos".

![Eliminación de 22 - unsplit de hojas](adjuntos/Eliminaci%C3%B3n%20de%2022%20-%20unsplit%20de%20hojas.png)

> [!example]- Transcripción de la imagen
> Las dos hojas se fusionan en 24* 27* 29*. En el directorio 27, 30 sobra el separador 27 (resaltado). "Necesitamos hacer un 'unsplit' de los nodos".

![Eliminación de 22 - directorio con poca ocupación](adjuntos/Eliminaci%C3%B3n%20de%2022%20-%20directorio%20con%20poca%20ocupaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> El directorio derecho queda solo con 30: menos de $d = 2$ llaves.

![Eliminación de 22 - unsplit del directorio](adjuntos/Eliminaci%C3%B3n%20de%2022%20-%20unsplit%20del%20directorio.png)

> [!example]- Transcripción de la imagen
> Se fusionan los dos directorios bajando el 17 de la raíz: queda una sola raíz 5, 13, 17, 30 con las hojas 2* 3* | 5* 7* 8* | 14* 16* | 24* 27* 29* | 33* 34* 38* 39*. El árbol perdió un nivel.

> [!tip] Cuándo baja la altura
> La **única** forma de reducir la altura es que la raíz quede con un solo hijo después de un unsplit. Ese hijo pasa a ser la nueva raíz. Es el espejo exacto del split de la raíz al insertar.

## Eficiencia

![Costo de las operaciones en un árbol B+](adjuntos/Costo%20de%20las%20operaciones%20en%20un%20%C3%A1rbol%20B%2B.png)

> [!example]- Transcripción de la imagen
> Sean $n$ el número de nodos y $2d$ la cantidad máxima de datos en una hoja. El costo de cada operación, medido en I/O: búsqueda, inserción y eliminación son $\mathcal{O}(\log_{2d}(n))$. "Costo depende logarítmicamente en base $d$".

## Duplicados y optimizaciones

Si se permiten **llaves repetidas**, hay tres opciones: usar páginas de *overflow*, extender la llave a una compuesta $(k, \text{id})$ para que vuelva a ser única, o flexibilizar los intervalos del directorio de $k_i \le k < k_{i+1}$ a $k_i \le k \le k_{i+1}$.

- **Compresión de llaves del directorio:** basta con guardar un prefijo que separe, lo que permite más llaves por nodo y menos altura.
- **Bulk loading:** para cargar una tabla completa, insertar llave por llave provoca muchos splits. Es mejor **ordenar primero** los datos, armar las hojas llenas de izquierda a derecha y construir el directorio por encima, haciendo split solo cuando se llena el nodo directorio de más a la derecha.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre redistribuir y hacer unsplit al eliminar?
> Redistribuir toma una llave de un hermano con más de $d$ llaves y ajusta el separador del padre. Unsplit fusiona la hoja con su hermano (que tiene exactamente $d$) y elimina un separador del padre, lo que puede propagarse hacia arriba.

> [!question]- ¿Cuándo disminuye la altura de un árbol B+?
> Cuando un unsplit deja a la raíz con un solo hijo. Ese hijo pasa a ser la raíz y el árbol pierde un nivel.

> [!question]- ¿Por qué el bulk loading ordena los datos antes de construir el árbol?
> Porque así se pueden llenar las hojas en orden, de izquierda a derecha, y construir el directorio con splits mínimos, en vez de pagar una búsqueda y posibles splits por cada inserción.

> [!question]- ¿En qué unidad se mide el costo de las operaciones de un B+ y cuánto vale?
> En lecturas y escrituras de disco (I/O), y es $O(\log_{2d} n)$, porque cada nivel recorrido es una lectura de bloque.
