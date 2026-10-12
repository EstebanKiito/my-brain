---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - race-condition
  - seccion-critica
  - origen/complemento
prerrequisitos:
  - "[[01 - Concepto de hilo y recursos compartidos versus privados]]"
---

# Condiciones de carrera y el problema de la sección crítica

Los threads de un proceso comparten memoria y archivos, compiten por la CPU y, en un multicore, pueden ejecutar en paralelo. Esa combinación es poderosa, pero tiene un costo: si dos threads tocan el mismo dato sin coordinarse, el resultado puede cambiar de una ejecución a otra. Este capítulo trata de cómo evitarlo, y empieza por darle nombre al problema.

## Condición de carrera

> [!tip] Definición
> Una **condición de carrera** (*race condition*) es una situación en que **el resultado de una operación depende del orden** temporal en que se ejecutan las operaciones de los threads, un orden que **no está bajo control del programador**. El resultado depende de cómo se entremezclan (*interleaving*) los threads.

Son muy comunes en computación, y se vuelven más probables a medida que crecen los datos y la cantidad de threads. Por ejemplo, si muchos threads escriben en un mismo archivo sin respetar un orden, el contenido final no tiene sentido. Lo mismo pasa con una variable compartida que cada thread va sobrescribiendo con lo que trae: "gana" el último que escribe, y el valor final varía según el orden de los threads. Los sistemas empresariales que paralelizan mucho, con muchos threads que leen y actualizan los mismos datos, son terreno fértil para estos errores.

Un ejemplo mínimo: dos threads incrementan un millón de veces cada uno el mismo contador.

```c
#include <pthread.h>
#include <stdio.h>

#define VECES 1000000
long contador = 0;                       /* recurso compartido */

void *incrementar(void *arg) {
    for (int i = 0; i < VECES; i++)
        contador++;                      /* sección crítica sin protección */
    return NULL;
}

int main(void) {
    pthread_t a, b;
    pthread_create(&a, NULL, incrementar, NULL);
    pthread_create(&b, NULL, incrementar, NULL);
    pthread_join(a, NULL);
    pthread_join(b, NULL);
    printf("esperado %d, obtenido %ld\n", 2 * VECES, contador);
    return 0;
}
```

Al ejecutarlo se obtiene casi siempre **menos de 2.000.000**, y un número distinto cada vez. La razón es que `contador++` no es una sola operación: es *leer, sumar 1, escribir*. Si los dos threads leen el mismo valor antes de que alguno escriba, uno de los incrementos se pierde.

> [!warning] Solo leer no es problema
> Si todos los threads solo **leen** un dato compartido, no hay carrera, porque nadie lo cambia. El conflicto aparece cuando al menos uno **escribe**.

## La sección crítica

El segmento de código en que un thread accede a recursos compartidos se llama **sección crítica** (SC). Es el "bien preciado" que hay que proteger: necesitamos un **protocolo** que no permita que dos o más threads estén en su sección crítica al mismo tiempo. La estructura de cualquier solución es la misma:

```c
void mess_with_shared_things() {
    entry();     /* protocolo de entrada: pedir permiso */
    /* sección crítica */
    leave();     /* protocolo de salida: liberar */
}
```

![Exclusión mutua ideal en región crítica](adjuntos/Exclusi%C3%B3n%20mutua%20ideal%20en%20regi%C3%B3n%20cr%C3%ADtica.png)

> [!example]- Transcripción de la imagen
> Dos líneas de tiempo, Process A y Process B. En $T_1$, *A enters critical region*. En $T_2$, *B attempts to enter critical region* y queda bloqueado (*B blocked*, línea punteada). En $T_3$, *A leaves critical region* y en ese mismo instante *B enters critical region*. En $T_4$, *B leaves critical region*. En ningún momento están los dos dentro a la vez.

Esta es la **situación ideal**: mediante software o hardware, lograr que los threads entren a la SC de a uno, sin afectar los resultados.

## Los tres criterios de una solución

| Criterio | Qué exige | Qué lo viola |
|---|---|---|
| **Exclusión mutua** | A lo más un thread está en su SC | Dos threads dentro a la vez |
| **Progreso** | Si nadie está en la SC y hay threads que quieren entrar, los que quieren entrar deciden quién entra, en un tiempo acotado | Que la SC quede vacía y nadie pueda entrar; por ejemplo, porque un thread que no quiere entrar bloquea la decisión |
| **Espera acotada** (ausencia de inanición) | Si un thread quiere entrar a su SC, podrá hacerlo luego de una cantidad finita de tiempo | Que un thread espere para siempre mientras otros entran una y otra vez |

> [!tip] Para recordar
> **E-P-E: Exclusión, Progreso, Espera acotada.** La primera dice "no más de uno", la segunda "no se queda vacía si hay interesados" y la tercera "a nadie le toca esperar para siempre".

Las soluciones posibles se ven en las notas siguientes: [[02 - Soluciones por software y algoritmo de Peterson|soluciones por software]] y [[03 - Sincronización por hardware e instrucciones atómicas|por hardware]].

## Preguntas de repaso

> [!question]- ¿Qué es una condición de carrera?
> Es una situación en que el resultado depende del orden en que se intercalan las operaciones de los threads, que el programador no controla. El mismo programa puede dar resultados distintos en cada ejecución.

> [!question]- ¿Por qué dos threads que hacen `contador++` un millón de veces pueden no llegar a dos millones?
> Porque `contador++` es leer, sumar y escribir. Si ambos leen el mismo valor antes de que alguno escriba, los dos escriben el mismo resultado y se pierde un incremento.

> [!question]- ¿Cuáles son los tres criterios de una solución correcta a la sección crítica?
> Exclusión mutua (a lo más uno dentro), progreso (si está libre y hay interesados, alguien entra en tiempo acotado) y espera acotada (quien quiere entrar lo logra en tiempo finito, sin inanición).

> [!question]- ¿Hay condición de carrera si diez threads solo leen un mismo archivo?
> No. Si nadie modifica el recurso, el orden de las lecturas no cambia el resultado. El problema aparece cuando al menos uno escribe.
