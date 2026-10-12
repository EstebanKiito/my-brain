---
ramo: "Sistemas Operativos y Redes"
tema: "Señales e IPC"
tags:
  - ssoo
  - senales
  - sigterm
  - sigkill
  - sigint
  - sigstop
  - origen/complemento
prerrequisitos:
  - "[[01 - Concepto de señal y ciclo de vida de señales POSIX]]"
---

# Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT

Varias señales sirven para "parar" un proceso, pero no hacen lo mismo. La diferencia clave es **si el proceso tiene voz**: algunas señales le *preguntan* al proceso si puede terminar o detenerse, y él decide cómo reaccionar; otras actúan sin preguntar.

## Preguntar o imponer

| Señal | Qué hace | ¿El proceso puede capturarla? |
|---|---|---|
| `SIGTERM` (15) | **Le avisa que debe terminar**: es la forma educada de pedirlo, y la que envía `kill <pid>` | Sí: puede cerrar archivos y liberar recursos antes de salir |
| `SIGKILL` (9) | **Mata el proceso sin preguntar**: el kernel lo elimina de la tabla de procesos | **No** |
| `SIGINT` (2) | **Interrumpe** el proceso; es la que envía `Ctrl+C` en la terminal. Por defecto termina | Sí: el programa puede, por ejemplo, preguntar "¿seguro que quieres salir?" |
| `SIGSTOP` / `SIGTSTP` | **Detiene** el proceso sin terminarlo: su estado queda guardado para continuar después. `SIGTSTP` es la de `Ctrl+Z` | `SIGSTOP` no; `SIGTSTP` sí |
| `SIGCONT` | **Continúa** un proceso detenido | Sí |
| `SIGSEGV` (11) | Acceso inválido a memoria (*segmentation fault*); por defecto termina con *core dump* | Sí |
| `SIGCHLD` | Avisa al padre que un hijo cambió de estado (por ejemplo, terminó y debe recogerlo con `wait()`); por defecto se ignora | Sí |

Los números de 2, 9, 11 y 15 son los mismos en todos los sistemas tipo UNIX. Los de las demás varían según el sistema, así que conviene usar siempre los nombres.

> [!tip] Mnemotecnia
> **TERM pregunta, KILL impone.** Con `SIGTERM` el proceso alcanza a ordenar sus cosas; con `SIGKILL` no alcanza a nada. Lo mismo vale para detenerse: `SIGTSTP` pide y `SIGSTOP` impone.

## Por qué SIGKILL y SIGSTOP no se pueden capturar

Si un proceso pudiera ignorar todas las señales, un programa colgado o malicioso sería imposible de detener. El SO reserva estas dos para garantizar que **siempre exista una forma infalible** de terminar o pausar cualquier proceso. Intentar registrarles un manejador falla:

```c
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

volatile sig_atomic_t terminar = 0;

void al_terminar(int sig) { terminar = 1; }      /* solo marca; el trabajo se hace afuera */

int main(void) {
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = al_terminar;
    sigaction(SIGTERM, &sa, NULL);                /* SIGTERM: se puede capturar */
    sigaction(SIGINT, &sa, NULL);                 /* SIGINT (Ctrl+C): también */
    if (sigaction(SIGKILL, &sa, NULL) == -1)      /* SIGKILL: el kernel lo rechaza */
        perror("sigaction(SIGKILL)");             /* Invalid argument */

    kill(getpid(), SIGTERM);                      /* simulamos un "kill <pid>" */
    while (!terminar) pause();
    printf("cerrando archivos y saliendo ordenadamente\n");
    return 0;
}
```

## Buenas prácticas: primero TERM, después KILL

1. Enviar **`SIGTERM`** y esperar un tiempo prudente, para dar al proceso la oportunidad de un **apagado ordenado** (*graceful shutdown*).
2. Solo si sigue colgado, enviar **`SIGKILL`** (`kill -9 <pid>`).

Usar `kill -9` de entrada es riesgoso: el proceso no ejecuta sus manejadores ni las rutinas de salida registradas con `atexit()`, y puede dejar archivos a medio escribir, bases de datos inconsistentes o *locks* sin liberar.

Para pausar y reanudar: `Ctrl+Z` (o `kill -STOP <pid>`) detiene el proceso, y `fg`, `bg` o `kill -CONT <pid>` lo reanudan con `SIGCONT`.

## Preguntas de repaso

> [!question]- ¿Por qué `SIGKILL` no se puede capturar ni ignorar?
> Para que siempre exista una forma garantizada de eliminar un proceso, aunque esté colgado, sea malicioso o ignore las demás señales.

> [!question]- ¿En qué se diferencian `SIGINT` y `SIGTERM`?
> `SIGINT` la genera el usuario con `Ctrl+C` para interrumpir el programa que está usando en la terminal. `SIGTERM` es la petición estándar de terminación que envían `kill` y las herramientas de administración. Ambas se pueden capturar y, por defecto, terminan el proceso.

> [!question]- ¿Por qué se recomienda enviar `SIGTERM` antes que `SIGKILL`?
> Porque `SIGTERM` permite que el proceso cierre archivos, libere *locks* y deje sus datos consistentes. `SIGKILL` lo corta en seco y puede dejar todo eso a medias.

> [!question]- ¿Qué pasa con un proceso que recibe `SIGSTOP` y cómo se reanuda?
> Queda detenido, sin terminar: conserva su estado en memoria. Con `SIGCONT` continúa desde donde estaba.
