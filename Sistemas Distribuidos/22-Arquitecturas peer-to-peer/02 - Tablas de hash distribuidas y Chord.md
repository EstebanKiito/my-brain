---
ramo: "Sistemas Distribuidos"
tema: "Arquitecturas peer-to-peer"
tags:
  - sd/p2p
  - python
  - origen/complemento
prerrequisitos:
  - "[[01 - Redes P2P, búsqueda y ataques]]"
  - "[[01 - Función de hash y tablas de hash]]"
---

# Tablas de hash distribuidas y Chord

Buscar a ciegas en una red P2P es caro. Las redes **estructuradas** resuelven la búsqueda con una regla: la posición de cada dato la decide una función de hash, así que cualquier nodo sabe **dónde** debe estar. Es una **tabla de hash distribuida** (DHT), y **Chord** es su versión clásica en forma de anillo.

## DHT

- Estructura de datos distribuida para almacenar y buscar eficientemente sin servidor central.
- Una **función de hash consistente** asigna una key a cada dato y a cada nodo. La key del nodo suele ser el hash de algo que lo identifica (su IP, por ejemplo).
- La key decide la **posición** del dato y qué nodo es **responsable** de él: el más próximo según alguna métrica (XOR, prefijo común o distancia circular).
- Cada nodo tiene una **tabla de ruteo** con punteros a otros nodos, elegidos para llegar al responsable en pocos saltos.

La versión local de las tablas de hash está en [[01 - Función de hash y tablas de hash|Función de hash y tablas de hash]].

## Hash consistente

Con un hash "normal", el nodo de $X$ sería $hash(X) \bmod 5$. Si un nodo sale, pasa a ser $hash(X) \bmod 4$ y **casi todos** los datos cambian de dueño. Con un **hash consistente**, el rango de valores es fijo e independiente del tamaño de la red: cada nodo ocupa una posición en ese rango, y si un nodo sale, solo se afectan su sucesor y su predecesor.

Ejemplo: los hashes van de 0 a 9 y hay nodos en 0, 4 y 8. El nodo 0 se encarga de las keys 9 y 0; el 4, de 1 a 4; el 8, de 5 a 8. Si sale el 8, el nodo 0 absorbe sus keys (5 a 9 y 0) y el 4 no cambia.

En Python, con 1000 claves y un nodo que sale de 5: con módulo cambiaron de dueño **800** claves; con hash consistente, solo **200** (las del nodo que salió).

## Seguridad de una DHT

1. **Es difícil secuestrar rutas:** las posiciones y los vecinos los fija el hash, y las búsquedas siguen reglas. No basta con insertar unos pocos nodos maliciosos; habría que ocupar posiciones precisas en muchas rutas. Mitiga los ataques Eclipse.
2. **Los nodos no eligen qué datos guardan:** el responsable lo decide el hash, así que un atacante no puede elegir quedarse con claves críticas sin "vencer" al hash.
3. **La red se adapta:** si un nodo desaparece, sus datos se replican o redistribuyen y las tablas se actualizan; resiste denegaciones parciales y permite expulsar nodos sospechosos.

En resumen, atacar una DHT exige ataques masivos y coordinados, mucho más caros que en una red no estructurada.

## Chord

- Los nodos se organizan en un **anillo**.
- El dato con clave $k$ va al nodo con el menor identificador tal que $hash(id) \geq k$: el **sucesor** de $k$.
- Cada nodo tiene una **finger table** (tabla de ruteo) que permite llegar a cualquier nodo en $O(\log N)$ saltos.

![Búsquedas en el anillo de Chord](adjuntos/B%C3%BAsquedas%20en%20el%20anillo%20de%20Chord.png)

> [!example]- Transcripción de la imagen
> Anillo de 0 a 31 con nodos en 1, 4, 9, 11, 14, 18, 20, 21 y 28, cada uno con su finger table (el 28 tiene 1, 4 y 14; el 1 tiene 4, 9 y 18). "28 busca 12": la clave 12 no existe como nodo, así que el 14 se hace responsable. "1 busca 26": el 26 no existe, así que el 28 es el responsable.

Una búsqueda avanza hacia el nodo más cercano que no supere la clave; si el nodo actual ya está "pasado", se da la vuelta al anillo. En Python, con ese anillo: $sucesor(12) = 14$, $sucesor(26) = 28$ y $sucesor(30) = 1$ (se da la vuelta).

### Churn: nodos que entran y salen

![Llegada de un nodo en Chord](adjuntos/Llegada%20de%20un%20nodo%20en%20Chord.png)

> [!example]- Transcripción de la imagen
> El archivo `uwu.py` tiene hash 5. Como no hay nodo 5, lo guardaba el 9 (responsable de las keys 5 a 9). Llega el nodo 7: ahora es responsable de 5, 6 y 7, y el 9 de 8 y 9. El archivo se envía al nuevo nodo; luego se actualiza la finger table del nodo 4 para que sepa del 7.

- **Entrada:** el nodo nuevo obtiene de su sucesor lo necesario para construir su finger table, se ubica según su hash y recibe los datos de los que pasa a ser responsable.
- **Salida o falla:** el predecesor detecta la ausencia y reconfigura su tabla.

Chord hereda la seguridad de las DHT: las rutas de las finger tables se pueden verificar preguntando a varios nodos; nadie elige ser $sucesor(k)$ sin romper el hash; y las claves se replican en $sucesor(k)$, $sucesor(sucesor(k))$, etc., así que expulsar a un nodo malicioso no pierde datos.

> [!tip] Otras DHT
> **Pastry** enruta por prefijos: cada salto comparte más dígitos iniciales con el destino (4XXX → 44XX → 444X → 4444). **Kademlia** mide la distancia con XOR: cada salto comparte más dígitos en cualquier posición (4XX4 → 44X4 → 4444).

## Preguntas de repaso

> [!question]- ¿Por qué el hash consistente mueve menos datos que el módulo cuando cambia la cantidad de nodos?
> Porque las posiciones dependen de un rango fijo y no del número de nodos. Al salir un nodo, solo sus claves pasan al sucesor; las demás no cambian de dueño.

> [!question]- En el anillo del ejemplo, ¿quién guarda la clave 10?
> El nodo 11, el sucesor de 10 (el menor identificador mayor o igual a 10).

> [!question]- ¿Por qué un nodo malicioso no puede elegir guardar una clave crítica en una DHT?
> Porque el responsable de cada clave lo determina el hash de los identificadores. Para quedarse con una clave específica, tendría que fabricar un ID con un hash elegido, lo que equivale a romper la función de hash.
