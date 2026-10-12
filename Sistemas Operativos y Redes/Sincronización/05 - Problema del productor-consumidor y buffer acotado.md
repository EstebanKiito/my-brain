---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - productor-consumidor
  - bounded-buffer
  - mutex
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
---

# Problema del productor-consumidor y buffer acotado

El **problema del productor-consumidor** (o del búfer limitado / *bounded buffer*) es uno de los problemas clásicos de sincronización en sistemas operativos, donde uno o más procesos generan datos y los depositan en un almacén temporal mientras otros procesos los extraen y procesan concurrentemente.

---

## PRODUCTO-CONSUMIDOR (mis apuntes)

> Problema concurrente: Si se esta vendiendo y comprando en el momento
> Este problema ese llama de PRODUCTO-CONSUMIDOR
> 
> ![Problema del productor consumidor y buffer circular](adjuntos/Problema%20del%20productor%20consumidor%20y%20buffer%20circular.png)
> 
> - El buffer es la lista donde se va guardando cosas
> - El espacio se va guardando por el que va produciendo, y sacando el que va consumiendo
> - Un buffer circular de tamaño limitado N
> - Dos threads: productor (agrega) y consumidor (consume)
> - Todos los elementos producidos deben ser consumidos en orden
> 
> EJEMPLO DE USO
> 
> ![Condición de carrera en variable stock compartida](adjuntos/Condici%C3%B3n%20de%20carrera%20en%20variable%20stock%20compartida.png)
> 
> Y ahora agregar LOCKS al stock, porque esa es nuestra seccion critica
> 
> ![Protección de variable stock con locks](adjuntos/Protecci%C3%B3n%20de%20variable%20stock%20con%20locks.png)

> [!warning] Posible error en apuntes
> * *"PRODUCTO-CONSUMIDOR"*: errata por "Productor-Consumidor" (*Producer-Consumer*).
> * *"ese llama"*: errata por "se llama".

---

> [!example]- Transcripción de la imagen: Problema del productor consumidor y buffer circular.png
> **Esquema del Búfer Circular de tamaño $N$:**
> * Arreglo circular compartido con punteros `in` (dónde inserta el productor) y `out` (dónde retira el consumidor).
> * **Condiciones límite:**
>   - Si el búfer está lleno ($N$ elementos), el productor debe detenerse y no puede insertar.
>   - Si el búfer está vacío ($0$ elementos), el consumidor debe detenerse y no puede retirar.

> [!example]- Transcripción de la imagen: Condición de carrera en variable stock compartida.png y Protección de variable stock con locks.png
> **Condición de carrera al actualizar inventario compartido:**
> ```c
> // Sin sincronización (INCORRECTO):
> // Productor:               // Consumidor:
> stock = stock + 1;           stock = stock - 1;
> // A nivel de ensamblador cada instrucción involucra 3 pasos:
> // 1. REG = stock
> // 2. REG = REG +/- 1
> // 3. stock = REG
> // Si el planificador intercala estos pasos, el valor final de stock se corrompe.
> 
> // Con protección de sección crítica mediante Cerrojos (CORRECTO):
> lock.acquire();
> stock = stock + 1;
> lock.release();
> ```

---

> [!tip] Complemento: Las dos dimensiones del problema
> El problema del productor-consumidor exige resolver **dos necesidades de sincronización simultáneas**:
> 1. **Exclusión mutua:** Evitar que dos hilos modifiquen los punteros del búfer o la variable de conteo al mismo tiempo (resuelto con un Mutex).
> 2. **Sincronización por condición:** Evitar que el productor intente escribir cuando el búfer no tiene espacio libre, y evitar que el consumidor intente leer cuando no hay elementos disponibles (resuelto con Semáforos o Variables de Condición).

---

## Preguntas de repaso

> [!question]- ¿Por qué la operación stock = stock + 1 no es atómica a nivel de hardware?
> Porque en lenguaje máquina se traduce en tres instrucciones separadas: cargar el valor de memoria a un registro de CPU (`MOV EAX, [stock]`), incrementar el registro (`ADD EAX, 1`), y reescribir el resultado en memoria (`MOV [stock], EAX`). Un cambio de contexto entre cualquiera de estas instrucciones produce una condición de carrera.

> [!question]- ¿Qué ocurre si un consumidor intenta extraer un elemento de un búfer vacío sin sincronización condicional?
> Ocurre una falla de subdesbordamiento (*underflow*), leyendo basura en memoria o índices negativos en el arreglo, a menos que se implemente una espera (activa o suspendida) hasta que el productor genere un nuevo dato.

> [!question]- ¿Basta un simple Mutex para resolver completamente el problema del búfer limitado?
> No. El Mutex solo asegura exclusión mutua para que no escriban a la vez; no resuelve de forma eficiente la coordinación cuando el búfer está completamente lleno o vacío (requiriendo semáforos o variables de condición para suspender y despertar hilos).

