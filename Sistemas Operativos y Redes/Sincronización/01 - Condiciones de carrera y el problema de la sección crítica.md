---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - race-condition
  - seccion-critica
prerrequisitos:
  - "[[01 - Concepto de hilo y recursos compartidos versus privados]]"
---

# Condiciones de carrera y el problema de la sección crítica

Cuando múltiples hilos o procesos acceden concurrentemente a recursos compartidos (como memoria global o archivos en disco) y al menos uno de ellos realiza escrituras, el resultado final puede depender del orden arbitrario en que el planificador intercala su ejecución. Esta anomalía se conoce como **condición de carrera** (*race condition*).

---

## CONTENIDO 5: SINCRONIZACIÓN (mis apuntes)

> Los Threads compiten por el uso de la CPU/ARCHIVOS → ¿Si se comparten archivos? A quien leemos primero?
> - En computacion hay un monton en condiciones de Carrera
> - Ejemplo: Si tuviera que escribir muchas cosas en un archivo, y cada thread escribiera, no tendría sentido → Race Condition (Respetar su orden)
> - CONDICION DE CARRERA: Situacion donde el valor de salida, depende del ORDEN, de los Threads
> 
> Es muy común, en el mundo empresarial
> - Cuando el archivo era mas grande,
> - Tenemos un bien preciado → SECCION CRITICA como variable, se va sobreescribiendo, segun lo que traiga cada Thread, y gana el que cierra el archivo al final, por lo que los valores no se mantienen, y varian segun el orden de sus Threads
> - Amazon → Tuvo problemas por paralelización (hacian muchos threads) y cada uno tomaba los datos y lo bajaba
> 
> SECCION CRITICA: Seccion critica donde solo 1 Thread accede a la vez
> 
> ```c
> void mess_with_shared_things(){
> 	entry();
> 	// Seccion critica
> 	leave();
> }
> ```
> 
> Archivos de una variable Global → Solo debe leerse 1 a la vez
> IMPORTANTE
> ¿Como nos aseguramos de solucionar secciones criticas?
> Si o si esto es pregunta de prueba
> 3 CRITERIOS (Condiciones)
> - Exclusion Mutua: A lo mas uno este en la seccion
> - No habria progreso por ejemplo, si un Thread se queda pegado sin liberar el acceso a la SC (Seccion Critica)
> - Progreso: Al menos un thread puede entrar, si ninguno entra, y hay threads esperando
> - Espera Agotada: (Ausencia de inanicion) → si un proceso quiere entrar, podrá hacerlo (luego de un tiempo finito)

## CLASE 5 (mis apuntes)

> 28/08/2024
> Cerrando lo de la clase pasada
> 3 Condiciones de Seccion Critica → Importantes de aprenderselas
> - Exclusion Mutua
> - Progreso
> - Espera Actodada
> 
> SITUACION IDEAL
> 
> ![Exclusión mutua ideal en región crítica](adjuntos/Exclusi%C3%B3n%20mutua%20ideal%20en%20regi%C3%B3n%20cr%C3%ADtica.png)
> 
> Tenemos que mediante software o hardware, que los Threads entren separados, y no se afecten los resultados

> [!warning] Posible error en apuntes
> * *"Espera Agotada / Espera Actodada"*: errata evidente por **Espera Acotada** (*Bounded Waiting*).
> * *"Archivos de una variable Global → Solo debe leerse 1 a la vez"*: imprecisión conceptual; si todos los hilos solo *leen*, no hay condición de carrera ni conflicto. El problema surge cuando al menos un hilo *modifica o escribe*.

---

> [!example]- Transcripción de la imagen: Exclusión mutua ideal en región crítica.png
> **Región crítica temporal entre dos procesos/hilos (A y B):**
> * Proceso A entra en la región crítica en $t_1$.
> * Proceso B intenta ingresar en $t_2$, pero la región está ocupada por A; B queda bloqueado o suspendido.
> * Proceso A sale de la región crítica en $t_3$, liberando el acceso.
> * Proceso B es admitido y entra finalmente a la región crítica en $t_3$, saliendo en $t_4$.
> * **Propiedad fundamental:** En ningún instante de tiempo coexisten A y B simultáneamente dentro de la región crítica.

---

> [!tip] Complemento: Los 3 Criterios Formales para Resolver la Sección Crítica
> Una solución válida al problema de la sección crítica debe satisfacer obligatoriamente tres condiciones fundamentales (Silberschatz / Dijkstra):
> 1. **Exclusión Mutua (*Mutual Exclusion*):** Si un proceso o hilo está ejecutando en su sección crítica, ningún otro proceso puede entrar a ejecutar en la suya.
> 2. **Progreso (*Progress*):** Si ningún proceso está en la sección crítica y hay procesos que desean ingresar, solo aquellos procesos que no estén en su sección remanente pueden participar en la decisión de quién entra, y esta decisión no puede postergarse indefinidamente.
> 3. **Espera Acotada (*Bounded Waiting*):** Debe existir un límite en la cantidad de veces que otros procesos pueden ingresar a sus secciones críticas después de que un proceso haya solicitado ingresar y antes de que se le conceda la entrada, previniendo la **inanición** (*starvation*).

---

## Preguntas de repaso

> [!question]- ¿Qué es una condición de carrera (race condition)?
> Es una situación en la que múltiples hilos acceden y manipulan concurrentemente datos compartidos, de modo que el resultado final de la ejecución depende del orden o temporización exacta en que las instrucciones fueron ejecutadas por el planificador de la CPU.

> [!question]- ¿Cuáles son los tres requisitos necesarios para una solución correcta al problema de la sección crítica?
> Son: 1) **Exclusión mutua** (a lo más un proceso a la vez en la sección crítica), 2) **Progreso** (si está libre y hay procesos esperando, alguno debe poder entrar sin bloqueos eternos), y 3) **Espera acotada** (garantía de que ningún proceso esperará indefinidamente sufriendo inanición).

> [!question]- ¿Ocurre una condición de carrera si diez hilos leen simultáneamente un mismo archivo compartido sin escribir?
> No. La concurrencia de solo lectura (*read-only*) es intrínsecamente segura y no produce condiciones de carrera, ya que el estado del recurso compartido no se altera. El conflicto surge en cuanto al menos un hilo ejecuta operaciones de modificación (*write*).
