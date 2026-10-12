---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - peterson
  - turnos
  - exclusion-mutua
  - origen/complemento
prerrequisitos:
  - "[[01 - Condiciones de carrera y el problema de la sección crítica]]"
---

# Soluciones por software y algoritmo de Peterson

¿Se puede proteger una sección crítica usando solo variables compartidas, sin ayuda especial del hardware? Los primeros intentos muestran lo difícil que es cumplir a la vez los tres criterios (exclusión mutua, progreso y espera acotada), y el algoritmo de Peterson es la respuesta más simple para dos threads.

## Intento 1: una bandera de "ocupado"

La idea más directa es una variable *lock* que indique si la sección está siendo usada: un thread no entra si está en uso, y al entrar la marca. **Una sola variable no arregla el problema**: dos threads pueden leer "libre" al mismo tiempo y entrar ambos antes de que alguno la marque. Revisar y marcar son dos pasos, y entre ellos puede llegar una interrupción.

## Intento 2: alternancia estricta con `turn`

Una variable compartida `turn` determina quién puede entrar, y cada thread, al salir, le pasa el turno al otro.

![Solución con alternancia estricta de turnos](adjuntos/Soluci%C3%B3n%20con%20alternancia%20estricta%20de%20turnos.png)

> [!example]- Transcripción de la imagen
> "Solución con turn, para alternar entre dos threads. Variable compartida turn determina quién puede entrar." `int turn = 1; // o 0 ...`. El thread 0 hace `while(TRUE) { while(turn != 0); /* SC */ turn = 1; /* out of SC */ }` y el thread 1 lo mismo, pero espera `turn != 1` y deja `turn = 0`. "¿Cumple con las condiciones?" Exclusión mutua: **Sí**. Progreso: **No**, "porque hay un thread que puede entrar y no quiere. Y otro que quiere entrar y no puede."

![Código de alternancia estricta para dos hilos](adjuntos/C%C3%B3digo%20de%20alternancia%20estricta%20para%20dos%20hilos.png)

> [!example]- Transcripción de la imagen
> El mismo código para thread 0 y thread 1, con la misma evaluación: Exclusión mutua: Sí. Progreso: No. Hay un thread que puede entrar y no quiere, y otro que quiere entrar y no puede.

Hay **exclusión mutua**, porque `turn` vale 0 o 1, nunca ambos. Pero **no hay progreso**: si es el turno del thread 0 y este no necesita entrar, el thread 1 queda esperando aunque la sección crítica esté vacía. Entra quien tiene el turno, no quien lo necesita.

## Algoritmo de Peterson (1981)

Peterson combina las dos ideas: **dos tipos de variables**. Un arreglo `flag[2]` indica si cada thread **quiere** entrar, y `turn` indica **a quién se le cede el paso**. Para sincronizar threads por software bastan estas variables compartidas; por hardware, como se verá, hacen falta instrucciones atómicas.

![Algoritmo de Peterson con turno e interés](adjuntos/Algoritmo%20de%20Peterson%20con%20turno%20e%20inter%C3%A9s.png)

> [!example]- Transcripción de la imagen
> "Solución de G. L. Peterson, 1981 (no la primera, pero la más simple)". `int turn = 1;` e `int flag[2] = {false, false}; // indica t_i está interesado en entrar`. "Variable local me puede ser 0 ó 1": `int other = 1-me; while('o') { flag[me] = true; /* wants */ turn = other; while(flag[other] && turn == other); /* wait */ /* SC */ flag[me] = false; }`. "¿Cumple los requisitos? ¿Por qué? ¿Se puede demostrar?" Exclusión mutua: Sí. Progreso: Sí. Espera acotada: "Si un thread 1 quiere entrar va a estar bloqueado, y solo va a poder entrar cuando el thread 0 salga de SC. Si el thread 0 es muy rápido va a esperar infinito." "Turn == other hace la magia".

![Detalle de ejecución del algoritmo de Peterson](adjuntos/Detalle%20de%20ejecuci%C3%B3n%20del%20algoritmo%20de%20Peterson.png)

> [!example]- Transcripción de la imagen
> La misma diapositiva sin el título: las variables `turn` y `flag[2]`, el código con `me` y `other`, y la misma evaluación de los tres requisitos.

Cada thread **declara su interés** (`flag[me] = true`) y **cede cortésmente el turno** (`turn = other`). Espera solo si el otro *quiere* entrar **y** tiene el turno. Si ambos llegan a la vez, `turn` guarda un solo valor (el último que se escribió), así que exactamente uno de los dos pasa: "`turn == other` hace la magia". Y si el otro no quiere entrar, `flag[other]` es falso y se entra sin esperar, con lo que se cumple el progreso que le faltaba a la alternancia.

Sobre la **espera acotada**, el material del curso plantea el caso borde: un thread sale de la SC y, por ser muy rápido, vuelve a pedir la entrada antes de que el otro, que estaba esperando, alcance a entrar. Según el material, si el thread 0 es muy rápido, el thread 1 podría esperar indefinidamente.

```c
#include <pthread.h>
#include <stdatomic.h>
#include <stdbool.h>
#include <stdio.h>

#define VECES 1000000
atomic_bool flag[2];                 /* flag[i]: el thread i quiere entrar */
atomic_int turn;                     /* a quién se le cede el paso */
long contador = 0;

void *trabajo(void *arg) {
    int me = *(int *)arg, other = 1 - me;
    for (int i = 0; i < VECES; i++) {
        atomic_store(&flag[me], true);                              /* quiero entrar */
        atomic_store(&turn, other);                                 /* cedo el turno */
        while (atomic_load(&flag[other]) && atomic_load(&turn) == other)
            ;                                                       /* espera activa */
        contador++;                                                 /* sección crítica */
        atomic_store(&flag[me], false);                             /* salgo */
    }
    return NULL;
}

int main(void) {
    pthread_t t0, t1;
    int id0 = 0, id1 = 1;
    pthread_create(&t0, NULL, trabajo, &id0);
    pthread_create(&t1, NULL, trabajo, &id1);
    pthread_join(t0, NULL);
    pthread_join(t1, NULL);
    printf("esperado %d, obtenido %ld\n", 2 * VECES, contador);   /* 2000000 */
    return 0;
}
```

> [!warning] Peterson en hardware moderno
> Con variables `int` comunes, este código **puede fallar** en un procesador multicore: la CPU y el compilador pueden reordenar las escrituras a `flag` y `turn`, y entonces ambos threads ven el camino libre. Por eso el ejemplo usa variables atómicas de C11, que imponen el orden. Sin ellas, al probarlo, a veces se pierden incrementos.

## Preguntas de repaso

> [!question]- ¿Por qué una sola variable de "ocupado" no resuelve la sección crítica?
> Porque revisar si está libre y marcarla como ocupada son dos pasos separados. Dos threads pueden revisar a la vez, ver "libre" y entrar ambos.

> [!question]- ¿Qué criterio viola la alternancia estricta con `turn` y por qué?
> Viola el progreso: si el thread que tiene el turno no quiere entrar, el otro queda bloqueado aunque la sección crítica esté vacía.

> [!question]- ¿Cómo garantiza Peterson la exclusión mutua cuando ambos threads quieren entrar a la vez?
> Ambos levantan su `flag` y ceden el turno, pero `turn` solo puede quedar con un valor, el del último que escribió. El thread al que le quedó cedido el turno pasa y el otro espera.

> [!question]- ¿Por qué Peterson no se usa tal cual en procesadores modernos?
> Porque el hardware y el compilador pueden reordenar las lecturas y escrituras de `flag` y `turn`, y sin barreras de memoria o variables atómicas se rompe la exclusión mutua.
