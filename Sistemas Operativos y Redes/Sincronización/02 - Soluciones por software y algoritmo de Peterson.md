---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - peterson
  - turnos
  - exclusion-mutua
prerrequisitos:
  - "[[01 - Condiciones de carrera y el problema de la sección crítica]]"
---

# Soluciones por software y algoritmo de Peterson

Históricamente se propusieron diversas soluciones algorítmicas por software puro (sin instrucciones de hardware especializadas) para coordinar el acceso a la sección crítica entre dos procesos o hilos.

---

## Intentos iniciales y alternancia estricta (mis apuntes)

> SOLUCION: Flag → Que indique si la seccion esta siendo usada
> Sirve para que el Thread no entré si esta siendo usada
> Una variable sola no arregla el problema → Podria ser que ya no necesite entrar, deberia haber otra flag para saber si se quiere entrar (ademas si esta disponible)
> Puede ser que entre, cuando no quería entrar, y otra que queria entrar no pueda entre → ese thread sufrira de Inanicion
> 
> SOLUCION CON TURNOS
> 
> ![Solución con alternancia estricta de turnos](adjuntos/Soluci%C3%B3n%20con%20alternancia%20estricta%20de%20turnos.png)
> 
> Tiene problema? → SI
> - Esto genera inanicion de threads, que quieran entrar y no puedan, porque alguno que no necesitaba entrar, entro porque tenia turno
> 
> Turno → Exclusion mutua si → Pero no cumple con progreso → Y por lo tanto con cumple con inanicion
> Solucion inicial:
> 
> ![Código de alternancia estricta para dos hilos](adjuntos/C%C3%B3digo%20de%20alternancia%20estricta%20para%20dos%20hilos.png)

## Algoritmo de Peterson (mis apuntes)

> SOLUCION SIMPLE (PETERSON)
> Variable turn → Para saber si puedo entrar
> Variable extra → Saber si quiero entrar
> 
> ![Algoritmo de Peterson con turno e interés](adjuntos/Algoritmo%20de%20Peterson%20con%20turno%20e%20inter%C3%A9s.png)
> 
> ¿Que pasa si entre, y soy tan rapido que me pongo denuevo en la cola, y entro denuevo, mas rapido que otro que estaba esperando? → UNICO CASO BORDE
> Para sincronizar Threads por Software → Necesito 2 Variable
> Para sincronizar Threads por Hardware → Necesito Instrucciones Atomicas
> Solucion Final: Peterson
> 
> ![Detalle de ejecución del algoritmo de Peterson](adjuntos/Detalle%20de%20ejecuci%C3%B3n%20del%20algoritmo%20de%20Peterson.png)

> [!warning] Posible error en apuntes
> * *"Y por lo tanto con cumple con inanicion"*: errata evidente por "por lo tanto **no cumple con ausencia de inanición**" (es decir, viola espera acotada).
> * *"Para sincronizar Threads por Software → Necesito 2 Variable"*: en el algoritmo de Peterson para 2 hilos se necesitan en realidad dos tipos de variables: un arreglo de banderas booleanas `flag[2]` (deseo de entrar) y una variable escalar `turn` (turno asignado).

---

> [!example]- Transcripción de la imagen: Solución con alternancia estricta de turnos.png y Código de alternancia estricta para dos hilos.png
> **Alternancia estricta (Variable turn):**
> * Hilo 0 espera mientras `turn != 0`; al salir de su sección crítica, asigna `turn = 1`.
> * Hilo 1 espera mientras `turn != 1`; al salir de su sección crítica, asigna `turn = 0`.
> * **Falla de Progreso:** Si el Hilo 0 no desea entrar a la sección crítica pero `turn == 0`, el Hilo 1 queda bloqueado indefinidamente aunque la sección crítica esté vacía. Se produce violación de progreso e inanición.

> [!example]- Transcripción de la imagen: Algoritmo de Peterson con turno e interés.png y Detalle de ejecución del algoritmo de Peterson.png
> **Estructura del Algoritmo de Peterson (1981):**
> ```c
> int turn;
> bool flag[2] = {false, false};
> 
> // Código para el proceso i (con j = 1 - i):
> flag[i] = true;             // Manifiesto mi intención de entrar
> turn = j;                   // Cedo cortésmente el turno al otro proceso
> while (flag[j] && turn == j); // Espera activa si el otro quiere y tiene el turno
> 
> // SECCIÓN CRÍTICA
> 
> flag[i] = false;            // Salgo de la sección crítica
> ```
> * Cumple simultáneamente con: 1) **Exclusión mutua**, 2) **Progreso** y 3) **Espera acotada**.

---

## Preguntas de repaso

> [!question]- ¿Por qué la solución de alternancia estricta (turn) viola el criterio de progreso?
> Porque obliga a los procesos a intercalar estrictamente sus accesos. Si el proceso 0 no necesita entrar a la sección crítica durante un período prolongado, el proceso 1 quedará eternamente bloqueado en su bucle de espera, a pesar de que la sección crítica se encuentra desocupada.

> [!question]- ¿Cómo garantiza el algoritmo de Peterson la exclusión mutua entre dos procesos?
> Ambos procesos indican su interés levantando su bandera (`flag[i] = true`), pero cada uno le cede el turno al contrario (`turn = j`). Al llegar al `while`, la variable `turn` solo puede retener un valor escalar (0 o 1); el proceso al que le fue concedido el turno avanzará de inmediato a la sección crítica mientras el otro espera.

> [!question]- ¿Por qué el algoritmo de Peterson no se utiliza directamente en procesadores modernos multicore?
> Porque las arquitecturas modernas ejecutan instrucciones fuera de orden (*out-of-order execution*) y emplean cachés con consistencia relajada; sin barreras de memoria explícitas (*memory barriers*), el hardware puede reordenar las escrituras en `flag` y `turn`, rompiendo la exclusión mutua.
