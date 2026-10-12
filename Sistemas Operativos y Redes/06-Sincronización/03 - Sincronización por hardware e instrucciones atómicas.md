---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - hardware
  - atomic-instructions
  - test-and-set
  - compare-and-swap
  - origen/complemento
prerrequisitos:
  - "[[02 - Soluciones por software y algoritmo de Peterson]]"
---

# Sincronización por hardware e instrucciones atómicas

El primer intento de [[02 - Soluciones por software y algoritmo de Peterson|solución por software]] fallaba por una razón simple: *revisar* si el lock está libre y *tomarlo* eran dos pasos, y entre ambos podía colarse otro thread. Si el hardware pudiera hacer esos dos pasos **en uno solo, sin interrupción posible**, el problema desaparecería. Eso es lo que ofrecen las **instrucciones atómicas**.

## La idea: instrucciones atómicas

Las soluciones por software dependen, en el fondo, de que existan instrucciones atómicas provistas por el hardware. Una instrucción **atómica** se ejecuta como una unidad indivisible: ningún otro thread ni núcleo puede ver un estado intermedio. Cada procesador trae algunas, y funcionan como **locks implementados en hardware**: permiten marcar una variable como bloqueada sin que otro thread pueda meterse entre la lectura y la escritura. Así, **un solo thread a la vez** logra tomar el lock, mientras que con el lock ingenuo por software podían entrar dos.

## `test_and_set()` (TSL)

`test_and_set` toma una variable booleana, **la cambia a `true` y devuelve el valor que tenía**, todo de forma atómica.

![Instrucción atómica hardware test and set](adjuntos/Instrucci%C3%B3n%20at%C3%B3mica%20hardware%20test%20and%20set.png)

> [!example]- Transcripción de la imagen
> "Sincronización por Hardware: *test_and_set*() (TSL)". "Algunas arquitecturas proveen instrucciones atómicas del tipo *test_and_set*. La instrucción, que se ejecuta atómicamente, es equivalente a este código:" `bool SOFTWARE_test_and_set(bool *target) { bool old_value = *target; *target = true; return old_value; }`. "¿Cómo usarlo?"

![Semántica equivalente de test and set](adjuntos/Sem%C3%A1ntica%20equivalente%20de%20test%20and%20set.png)

> [!example]- Transcripción de la imagen
> El mismo código equivalente: `bool SOFTWARE_test_and_set(bool *target) { bool old_value = *target; *target = true; return old_value; }`.

Con ella se puede implementar la versión "ingenua" del lock. Es ingenua porque es la más fácil, y ahora sí funciona:

![Implementación básica de lock con test and set](adjuntos/Implementaci%C3%B3n%20b%C3%A1sica%20de%20lock%20con%20test%20and%20set.png)

> [!example]- Transcripción de la imagen
> `bool lock = false; // false==free, true==busy`, y luego `while(true) { ... while (test_and_set(&lock)); /* SC */ lock = false; /* Out of SC */ }`.

> [!tip] Cómo leerlo
> El lock vacío es `false`. Si `test_and_set` devuelve `false`, el lock estaba libre y este thread lo acaba de tomar: entra. Si devuelve `true`, estaba ocupado, y el thread sigue en el `while` reintentando. Al salir, `lock = false` lo libera.

## `compare_and_swap()` (CAS, XCHG)

`compare_and_swap` (en x86, la instrucción `CMPXCHG`) es más general: **solo escribe el valor nuevo si el valor actual es el esperado**, y en ambos casos devuelve el valor previo.

![Semántica equivalente de compare and swap](adjuntos/Sem%C3%A1ntica%20equivalente%20de%20compare%20and%20swap.png)

> [!example]- Transcripción de la imagen
> `bool SOFTWARE_compare_and_swap(int *value, int expected, int new_value) { int previous = *value; if (*value == expected) *value = new_value; return previous; }`.

![Implementación de lock con compare and swap](adjuntos/Implementaci%C3%B3n%20de%20lock%20con%20compare%20and%20swap.png)

> [!example]- Transcripción de la imagen
> "Código equivalente a *compare_and_swap*() (XCHG, CAS)", con el mismo código de arriba. "Otra implementación simple, gracias a una instrucción atómica": `int lock = 0; // 0==free, 1==busy` y `while(true) { ... while (compare_and_swap(&lock, 0, 1)); /* SC */ lock = 0; /* Out of SC */ }`.

`compare_and_swap(&lock, 0, 1)` significa "si el lock vale 0 (libre), ponlo en 1 (ocupado)". Devuelve 0 solo al thread que lo logró; los demás reciben 1 y siguen esperando.

## En C real

C11 expone estas instrucciones en `<stdatomic.h>`, y otros lenguajes tienen equivalentes, como `std::atomic` en C++. Los dos locks de arriba, con dos threads cada uno:

```c
#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>

#define VECES 1000000
atomic_flag lock_tas = ATOMIC_FLAG_INIT;    /* para test_and_set: limpio == libre */
atomic_int lock_cas = 0;                    /* para compare_and_swap: 0 == libre */
long c1 = 0, c2 = 0;

void *con_tas(void *arg) {
    for (int i = 0; i < VECES; i++) {
        while (atomic_flag_test_and_set(&lock_tas))
            ;                                 /* devolvió true: estaba ocupado, reintentar */
        c1++;                                 /* sección crítica */
        atomic_flag_clear(&lock_tas);         /* lock = false */
    }
    return NULL;
}

void *con_cas(void *arg) {
    for (int i = 0; i < VECES; i++) {
        int esperado = 0;
        while (!atomic_compare_exchange_strong(&lock_cas, &esperado, 1))
            esperado = 0;                     /* falló: lock no era 0; reintentar */
        c2++;                                 /* sección crítica */
        atomic_store(&lock_cas, 0);           /* lock = 0 */
    }
    return NULL;
}

int main(void) {
    pthread_t t[4];
    pthread_create(&t[0], NULL, con_tas, NULL);
    pthread_create(&t[1], NULL, con_tas, NULL);
    pthread_create(&t[2], NULL, con_cas, NULL);
    pthread_create(&t[3], NULL, con_cas, NULL);
    for (int k = 0; k < 4; k++) pthread_join(t[k], NULL);
    printf("test_and_set: %ld   compare_and_swap: %ld\n", c1, c2);   /* 2000000 y 2000000 */
    return 0;
}
```

> [!warning] No se usan directamente
> En general **no se usan las instrucciones atómicas directamente** en los programas: sobre ellas se construyen **primitivas de software**, como [[04 - Mutex locks y el dilema de busy waiting versus dormir|mutex locks]] y semáforos, que son las que usa el programador. Además, estos locks hacen **espera activa** (*busy waiting*): el thread que espera gira en el `while` gastando CPU.

## Preguntas de repaso

> [!question]- ¿Qué significa que una instrucción sea atómica y por qué resuelve el problema del lock ingenuo?
> Que se ejecuta como una unidad indivisible: nadie puede intercalarse a mitad de camino. El lock ingenuo fallaba porque revisar y tomar eran dos pasos; con `test_and_set` son uno solo.

> [!question]- Con `test_and_set`, ¿cómo sabe un thread si consiguió el lock?
> Por el valor devuelto: si es `false`, el lock estaba libre y ahora es suyo. Si es `true`, estaba ocupado y debe seguir intentando.

> [!question]- ¿Qué hace `compare_and_swap(&lock, 0, 1)`?
> Si `lock` vale 0 (libre), lo pone en 1 (ocupado). Siempre devuelve el valor anterior, así que solo el thread que recibe 0 tomó el lock.

> [!question]- ¿Por qué los programas no suelen usar estas instrucciones directamente?
> Porque sobre ellas se construyen primitivas más cómodas y eficientes, como mutex y semáforos, que además evitan gastar CPU en espera activa.
