---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/01 - Capas de abstracción de entrada-salida y mecanismos de buffering\|01 - Capas de abstracción de entrada-salida y mecanismos de buffering]]"
---

# Discos duros magnéticos (HDD) y discos de estado sólido (SSD)

Lo que realmente interesa en esta parte de la materia es la **memoria secundaria**: almacenamiento de **alta capacidad** y **no volátil** (no se borra al apagar), pero **más lento** (y más barato) que la memoria principal. Cómo está construido el disco explica por qué cuesta lo que cuesta acceder a él, y por qué el SO se esfuerza tanto en ordenar esos accesos.

## El disco duro magnético (HDD)

![Geometría de un disco duro magnético HDD](adjuntos/Geometr%C3%ADa%20de%20un%20disco%20duro%20magn%C3%A9tico%20HDD.png)

> [!example]- Transcripción de la imagen
> "Sistemas de Disco – Memoria Secundaria". Diagrama de un disco con varios *platters* apilados sobre un *spindle* que gira (*rotation*); en cada plato se marcan un *track t* y un *sector s*; las pistas alineadas de todos los platos forman el *cylinder c*; un *arm assembly* mueve varios *arms*, cada uno con su *read-write head*. Texto: **Brazos (arms)** se mueven juntos. **Brazos** poseen cabezas lectoras (*heads*). **Platos (platter)** divididos en tracks circulares. **Tracks** divididos en sectores: bloques de 512 byte. **Conjunto de tracks** entre varios platos forman un cilindro. **Velocidades de rotación**: 5400, 7200, 10000, 15000 RPM (rotaciones por minuto).

| Componente | Qué es |
|---|---|
| **Plato** (*platter*) | Disco magnético; está dividido en **pistas** (*tracks*) circulares |
| **Sector** | División de una pista; un bloque de **512 bytes** |
| **Cilindro** | El conjunto de pistas a la misma distancia del centro en todos los platos |
| **Brazos y cabezas** | Los brazos tienen las cabezas lectoras y **se mueven todos juntos** |

Como el disco funciona con partes que **rotan** y brazos que **se mueven**, cada acceso tiene demoras mecánicas distintas según dónde esté el dato.

## Tiempo de acceso

$$T_{\text{acceso}} = \underbrace{\text{seek time} + \text{latencia rotacional}}_{\text{posicionamiento}} + \text{tiempo de transferencia}$$

- **Seek time:** cambiar de pista, es decir, mover el brazo hasta el cilindro buscado.
- **Latencia rotacional:** esperar dentro de la pista hasta que el sector quede debajo de la cabeza. En promedio es media vuelta.
- **Transferencia:** leer los datos. **Leer sectores consecutivos es más rápido**, porque no hay que reposicionar.

| RPM | Una vuelta | Latencia rotacional promedio (½ vuelta) |
|---|---|---|
| 5400 | 11,1 ms | 5,6 ms |
| 7200 | 8,3 ms | 4,2 ms |
| 10000 | 6 ms | 3 ms |
| 15000 | 4 ms | 2 ms |

> [!tip] Desfragmentar
> Como leer sectores contiguos es mucho más rápido, **desfragmentar** reubica los bloques de cada archivo para que queden juntos, y así el brazo hace menos movimientos al leer. Por la misma razón el SO ordena los pedidos al disco (ver [[04 - Algoritmos de planificación de disco (Disk Scheduling)|scheduling de disco]]).

## El disco de estado sólido (SSD)

El SSD **no tiene brazos ni platos**: guarda la información en **celdas** de memoria flash (NAND).

| | HDD | SSD |
|---|---|---|
| Seek time y latencia rotacional | Sí | **No existen** |
| Velocidad | Más lento | **Más rápido** |
| Costo por MB | Más barato | **Más costoso** |
| Consumo eléctrico | Mayor | **Menor** |
| Desgaste | Mecánico | Las **celdas tienen una cantidad limitada de reescrituras** |

Para que las celdas se desgasten parejo, el controlador del SSD reparte las escrituras entre todas (*wear leveling*), y el SO le avisa con el comando TRIM qué bloques ya no se usan. Como no hay movimiento mecánico, la fragmentación casi no afecta su rendimiento.

## Preguntas de repaso

> [!question]- ¿Qué componentes tiene el tiempo de acceso de un HDD?
> El seek time (mover el brazo al cilindro), la latencia rotacional (esperar que el sector pase bajo la cabeza) y el tiempo de transferencia.

> [!question]- ¿Cuál es la latencia rotacional promedio de un disco de 7200 RPM?
> Una vuelta toma $60\,000/7200 \approx 8{,}33$ ms; en promedio se espera media vuelta, unos 4,17 ms.

> [!question]- ¿Por qué desfragmentar mejora un HDD pero casi no cambia un SSD?
> En el HDD cada salto entre bloques no contiguos cuesta seek y latencia rotacional; juntar los bloques los elimina. El SSD no tiene partes mecánicas, así que acceder a un bloque cuesta casi lo mismo esté donde esté.

> [!question]- ¿Qué ventajas y desventajas tiene un SSD frente a un HDD?
> Es más rápido y consume menos energía, porque no tiene seek ni latencia rotacional. Pero es más caro por MB y sus celdas soportan un número limitado de reescrituras.
