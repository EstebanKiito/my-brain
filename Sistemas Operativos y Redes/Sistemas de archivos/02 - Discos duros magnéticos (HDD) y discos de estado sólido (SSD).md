---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Sistemas de archivos/01 - Capas de abstracción de entrada-salida y mecanismos de buffering\|01 - Capas de abstracción de entrada-salida y mecanismos de buffering]]"
---

# Discos duros magnéticos (HDD) y discos de estado sólido (SSD)

La memoria secundaria provee persistencia no volátil y gran capacidad, implementándose principalmente mediante discos mecánicos magnéticos (HDD) o unidades de estado sólido basadas en semiconductores (SSD).

## Memoria secundaria, HDD y SSD (mis apuntes)

- Lo que nos interesa realmente de esta materia → MEMORIA SECUNDARIA
- Memoira Secundaria
- Almacenamiento de Alta capacidad
- Memoria No volatil
- Mas lento (y barato) que la memoria principal
- DISCO DURO
- DISCO DURO: Esta armado a traves de brazos,
- ROTAR
- Esto implica tiempos de demora distintos
- tiene que ejecutar movimientos para trabajar
- Latencia de Rotacion
- Seek Time (mover el brazo lector (para leer los discos))
- Hay ciertas formas
- Defragmentar → Posicionar memoria util, para evitar tener que hacer tantos movimientos al leer la información
- Latencias:
- DISCO ESTADO SOLIDO (SSD)
- Mejor que el Disco Duro → No tiene brazos
- Dado que eliminamos la latencia de rotacion y Seek Time
- Son mas rapidos
- Mas costosos por MB
- Menor consumo electrico
- CELDAS LIMITADAS de reescrituras
- Usan celdas para descargar informacion

> [!warning] Posible error
> En los apuntes aparece `Memoira Secundaria` (error tipográfico por Memoria Secundaria).

> [!tip] Complemento: Geometría mecánica y características físicas
> ![Geometría de un disco duro magnético HDD](adjuntos/Geometría%20de%20un%20disco%20duro%20magnético%20HDD.png)
>
> > [!example]- Transcripción de la imagen
> > **Diagrama de arquitectura interna de un disco duro magnético (HDD):**
> > - **Spindle:** eje central de rotación que gira a velocidad constante ($5400$, $7200$, $10000$, $15000\text{ RPM}$).
> > - **Platters:** platos circulares magnéticos apilados. Cada plato posee dos superficies de grabación.
> > - **Tracks:** pistas circulares concéntricas trazadas en la superficie del plato.
> > - **Sectores:** divisiones angulares de una pista (típicamente $512\text{ bytes}$ o $4\text{ KB}$).
> > - **Cilindro:** conjunto de todas las pistas que comparten el mismo radio vertical entre todos los platos.
> > - **Cabezas lectoras/escritoras (heads):** una por superficie, unidas a brazos mecánicos rígidos (*arm assembly*) que se desplazan solidariamente.
>
> 1. **Componentes del tiempo de acceso en HDD:**
>    $$\text{Tiempo de I/O} = \text{Seek Time} + \text{Latencia Rotacional} + \text{Tiempo de Transferencia}$$
>    - **Seek Time:** tiempo físico para acelerar, mover y estabilizar el brazo sobre el cilindro destino ($3\text{ a }10\text{ ms}$).
>    - **Latencia rotacional:** tiempo de giro hasta que el sector deseado pasa bajo la cabeza lectora. En promedio:
>      $$\text{Latencia promedio} = \frac{1}{2 \times \text{RPM}} \times 60\text{ s}$$
>      Para $7200\text{ RPM}$, equivale aproximadamente a $4.17\text{ ms}$.
>    - **Desfragmentación:** reorganiza los archivos para que sus bloques residan en sectores contiguos de un mismo cilindro o cilindros adyacentes, minimizando saltos del cabezal.
> 2. **Arquitectura y funcionamiento de SSD:**
>    - Basado en memoria flash NAND. Sin partes mecánicas: latencia rotacional y seek time iguales a cero.
>    - Lecturas y escrituras a nivel de páginas ($4\text{ KB} - 16\text{ KB}$), pero borrado únicamente por bloques completos ($128\text{ a }512\text{ páginas}$, $2\text{ a }8\text{ MB}$).
>    - Ciclos de escritura/borrado limitados por desgaste de las compuertas flotantes (endurance). Los controladores implementan algoritmos de nivelación de desgaste (*wear leveling*) y comandos TRIM para maximizar su vida útil.

## Preguntas de repaso

> [!question]- ¿Por qué la fragmentación de archivos perjudica gravemente el rendimiento de un disco HDD pero casi no afecta a un SSD?
> Porque en un HDD cada fragmento no contiguo obliga al brazo a realizar una operación mecánica de búsqueda (*seek*) y esperar una latencia rotacional ($4\text{–}10\text{ ms}$ por salto). En un SSD el acceso a cualquier dirección flash toma un tiempo prácticamente idéntico de microsegundos mediante direccionamiento puramente electrónico.

> [!question]- ¿Cómo se calcula la latencia rotacional promedio de un disco que gira a $10000\text{ RPM}$?
> Un disco a $10000\text{ RPM}$ da una vuelta completa en $\frac{60}{10000}\text{ s} = 6\text{ ms}$. En promedio, el sector deseado se encuentra a media vuelta de distancia, por lo que la latencia rotacional media es de $3\text{ ms}$.

> [!question]- ¿Qué es la nivelación de desgaste (*wear leveling*) en unidades SSD y qué problema resuelve?
> Es un algoritmo del controlador del SSD que distribuye las escrituras de manera uniforme entre todos los bloques físicos de la memoria flash NAND para evitar que celdas frecuentemente reescritas se degraden prematuramente antes que el resto.
