---
ramo: "Sistemas Distribuidos"
tema: "Procesos e hilos en Python"
tags:
  - sd/procesos-e-hilos
  - origen/complemento
prerrequisitos:
  - "[[05 - Mecanismos de sincronización entre threads]]"
---

# Algoritmo de la panadería y deadlock

¿Se puede garantizar exclusión mutua sin un lock que tenga dueño? Leslie Lamport (figura central de los sistemas distribuidos y desarrollador inicial de LaTeX) lo mostró en 1974 con el **algoritmo de la panadería**, que solo usa números de turno. Su idea de ordenar por (número, identificador) reaparece más adelante en los relojes lógicos y en la exclusión mutua distribuida. La nota cierra con el peligro opuesto a la falta de sincronización: el **deadlock**.

## La analogía

Cada thread es un **cliente** y el **mostrador** de la panadería es la sección crítica.

![Reglas del algoritmo de la panadería](adjuntos/Reglas%20del%20algoritmo%20de%20la%20panader%C3%ADa.png)

> [!example]- Transcripción de la imagen
> Algoritmo para asegurar exclusión mediante un contador global. Cada thread es un cliente y el mostrador de la panadería, la sección crítica:
> 1. Cada cliente pide un número del contador y luego se aumenta el contador global.
> 2. El mostrador atiende por orden de los números.
> 3. Si dos o más clientes piden número al mismo tiempo, se desempata por el identificador, que es único por entidad (por ejemplo, el PID).
> 4. Cuando el cliente está siendo atendido, no puede sacar otro número.
> 5. Cuando el cliente termina, deja libre el mostrador para llamar al siguiente número.
>
> Si el sistema operativo habilita memoria compartida entre procesos, el algoritmo también sirve para procesos.

## Pseudocódigo

```text
Entrando: array[NUM_CLIENT] of bool = {false};
Número:   array[NUM_CLIENT] of integer = {0};

# Código del cliente i
Entrando[i] = true;
Número[i] = 1 + max(Número);
Entrando[i] = false;
for j in 0 .. NUM_CLIENT - 1:
    # Si j está sacando número, esperar para comparar con su valor final
    while Entrando[j]: nada
    # Esperar a todo cliente con menor turno que esté en la zona crítica
    while Número[j] != 0 and (Número[j], j) < (Número[i], i): nada
# sección crítica
Número[i] = 0;
# sección no crítica
```

- La comparación `(Número[j], j) < (Número[i], i)` es **lexicográfica**: primero el número; si empatan, gana el identificador menor. Así dos clientes nunca tienen el mismo turno efectivo.
- `Entrando[j]` evita leer el número de un cliente que todavía lo está calculando.
- Cada cliente busca a quienes tienen un número menor y **depende de ellos** para que le toque.

Se probó en Python con tres threads que entran 2000 veces cada uno a una sección crítica que incrementa un contador: el resultado fue exactamente 6000.

> [!tip] Por qué no hay deadlock
> Los turnos forman un **orden total**, así que no hay esperas cíclicas: el cliente con menor (número, id) siempre puede avanzar, pide su pan y se va.

> [!warning] Sus límites
> Si el cliente atendido no termina, todos los demás se atrasan. Además usa **espera activa** (los `while` consumen CPU) y los números crecen sin límite. Hoy no se usa en la práctica, pero su idea de ordenar por (contador, id) es la base de los algoritmos distribuidos que vienen.

La familia de soluciones por software (como el algoritmo de Peterson) está en [[02 - Soluciones por software y algoritmo de Peterson|Soluciones por software]].

## Deadlock

Esperar mucho no es necesariamente un deadlock. Si un thread espera indefinidamente sin que nadie lo atienda, se habla de **inanición** (*starvation*). El **deadlock** (interbloqueo) es más específico; según Coulouris, Dollimore y Kindberg:

> [!tip] Definición
> Hay deadlock cuando cada proceso de un grupo espera que otro proceso del grupo le envíe un mensaje y existe un **ciclo** en el grafo de la relación "espera a".

Lo típico es que aparezca por un **mal uso de locks**, aunque puede ocurrir con cualquier mecanismo de sincronización. El caso clásico son dos threads que toman dos locks en orden inverso:

```python
def tarea(primero, segundo, nombre):
    with primero:
        time.sleep(0.1)                 # da tiempo al otro thread a tomar su lock
        if segundo.acquire(timeout=1):  # sin timeout esperaría para siempre
            segundo.release()
        else:
            print(nombre, "no pudo tomar el segundo lock: deadlock")

# T1 toma a y luego b; T2 toma b y luego a
```

Al ejecutarlo, ambos threads se rinden tras el timeout: cada uno tiene el lock que el otro necesita. Tomar los locks **siempre en el mismo orden** rompe el ciclo. Ver [[09 - Problema de los filósofos comelones y deadlocks|Filósofos comelones y deadlocks]] y [[09 - Deadlocks|Deadlocks en bases de datos]].

## Preguntas de repaso

> [!question]- ¿Para qué sirve el arreglo `Entrando` en el algoritmo de la panadería?
> Para no comparar contra el número de un cliente que todavía lo está calculando. Sin esa espera, un cliente podría ver un número antiguo (0) del otro y entrar a la vez que él.

> [!question]- ¿Qué distingue un deadlock de la inanición?
> En el deadlock hay un ciclo de esperas: nadie del grupo puede avanzar porque todos esperan a otro del grupo. En la inanición un proceso espera indefinidamente, pero los demás sí avanzan.

> [!question]- ¿Por qué tomar los locks siempre en el mismo orden evita el deadlock?
> Porque ningún thread puede tener un lock "posterior" mientras espera uno "anterior", así que el grafo de esperas no puede formar un ciclo.
