---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/complemento]
prerrequisitos: ["[[05 - Jerarquía y creación de procesos con fork|Jerarquía y creación de procesos con fork]]", "[[06 - Control de procesos con wait, exec y terminación|Control de procesos con wait, exec y terminación]]"]
---
# Programación de procesos en C y prevención de fork bombs

Crear procesos en C se reduce a combinar tres llamadas al sistema: `fork()` crea, `exec()` reemplaza y `wait()` espera. Bien estructuradas permiten que un programa principal (el padre) reparta trabajo entre hijos. Mal estructuradas, los procesos se multiplican sin control hasta botar la máquina: una **fork bomb**.

## Herramientas de C que se usan

- **`double`** para números reales: tiene más precisión y rango que `float`.
- **Punteros:** variables que guardan direcciones de memoria.
- **`struct`:** agrupa datos relacionados, por ejemplo la descripción de un proceso.
- **`enum`:** define constantes enteras con nombre, útil para estados.
- **`argc` / `argv`:** cuántos argumentos llegaron por línea de comandos y cuáles son (`argv` es el arreglo de strings).
- **`clock()`** de `<time.h>`: mide el tiempo de CPU consumido por el proceso.
- **Encabezados:** `<unistd.h>` (`fork`, `exec*`, `getpid`), `<sys/types.h>` (`pid_t`) y `<sys/wait.h>` (`wait`, `waitpid`, `WEXITSTATUS`).

## El patrón fork → exit → wait

`fork()` crea un hijo como **copia del padre**. Ambos continúan ejecutando desde la misma instrucción, el retorno de `fork()`, y solo se distinguen por el valor que reciben: el padre obtiene el **PID del hijo** y el hijo obtiene **0** (un valor negativo indica error). Lo típico es que el padre sea el programa principal y los hijos ejecuten funcionalidades concretas.

![Uso de fork en lenguaje C](adjuntos/Uso%20de%20fork%20en%20lenguaje%20C.png)

> [!example]- Transcripción de la imagen
> Dos copias del mismo programa, una por proceso. Ambas ejecutan `pid = fork(); if (pid == 0) ChildProcess(); else ParentProcess();`. En el padre, `pid = 3456` (el PID del hijo) y entra a `ParentProcess()`. En el hijo, `pid = 0` y entra a `ChildProcess()`.

El hijo hace su trabajo y termina con `exit(código)`. El padre, mientras tanto, llama a `wait()` para esperarlo y recoger ese código de retorno (0 = terminó bien).

![Ciclo de sincronización fork y wait](adjuntos/Ciclo%20de%20sincronización%20fork%20y%20wait.png)

> [!example]- Transcripción de la imagen
> Desde `fork` salen dos ramas. La rama *child* va a *child program* y luego a `exit`. La rama *parent* va a *main program* y luego a `wait`. Una flecha une `exit` con `wait`, y desde `wait` el padre sigue (`continue`).

Ejemplo completo: un padre crea tres hijos, nunca nietos, y espera a cada uno.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

enum State { RUNNING, WAITING, FINISHED };

struct Process {
    pid_t pid;
    char *name;
    enum State state;
};

int main(void) {
    struct Process hijos[3];
    for (int i = 0; i < 3; i++) {
        pid_t pid = fork();
        if (pid < 0) { perror("fork"); exit(1); }
        if (pid == 0) {              /* hijo: trabaja y termina */
            printf("hijo %d (pid %d)\n", i, getpid());
            exit(i);                 /* sin exit, el hijo seguiría el for y crearía nietos */
        }
        hijos[i] = (struct Process){ pid, "worker", RUNNING };
    }
    for (int i = 0; i < 3; i++) {    /* padre: espera a cada hijo */
        int status;
        waitpid(hijos[i].pid, &status, 0);
        hijos[i].state = FINISHED;
        printf("hijo %d terminó con código %d\n", hijos[i].pid, WEXITSTATUS(status));
    }
    return 0;
}
```

## exec: el hijo deja de ser el mismo código

`exec()` es distinto de `fork()`: no crea un proceso, sino que **reemplaza** el programa del proceso actual por el ejecutable de la ruta indicada, manteniendo el PID. Hay varias variantes (`execl`, `execlp`, `execv`, `execvp`…), cada una con su forma de recibir los argumentos. Tras un `exec` exitoso el hijo ya no ejecuta el código del padre, sino el otro programa, por ejemplo uno que multiplica números:

```c
if (fork() == 0) {
    execlp("expr", "expr", "6", "*", "7", (char *)NULL);  /* imprime 42 */
    perror("exec");                  /* solo se llega aquí si exec falla */
    exit(1);
}
wait(NULL);
```

## Fork bombs: crecimiento exponencial

Si los hijos también ejecutan `fork()`, el número de procesos se duplica en cada vuelta. Con `for (i = 0; i < 3; i++) fork();` terminan existiendo $2^3 = 8$ procesos. El riesgo típico es un `fork()` dentro de un ciclo (un `for` dentro de un `while`) sin que el hijo salga del ciclo: la tabla de procesos del kernel se llena y el computador puede colgarse. Usar `fork` dentro de un ciclo no es un error en sí. Es seguro mientras sea ordenado, es decir, mientras cada hijo termine (`exit`) y el ciclo tenga fin.

> [!warning] Fork bomb canónica (no ejecutar)
> En Bash, `:(){ :|:& };:` define una función `:` que se llama dos veces a sí misma en segundo plano: 2, 4, 8, 16… procesos. Para defender el sistema se limita la cantidad de procesos por usuario con `ulimit -u <máximo>` o en `/etc/security/limits.conf`.

## Preguntas de repaso

> [!question]- Tras un `fork()`, ¿cómo sabe el código si corre en el padre o en el hijo?
> Por el valor de retorno: 0 en el hijo, el PID del hijo (mayor que 0) en el padre y negativo si falló.

> [!question]- ¿Por qué el hijo debe llamar a `exit()` dentro del ciclo que crea hijos?
> Porque el hijo continúa desde el retorno de `fork()` con una copia del estado del padre, incluido el contador del ciclo. Si no termina, sigue iterando y crea sus propios hijos (nietos del padre), y el número de procesos crece de forma exponencial.

> [!question]- ¿Qué diferencia hay entre `fork()` y `exec()`?
> `fork()` crea un proceso nuevo, copia del llamador, con otro PID. `exec()` no crea procesos: reemplaza el programa del proceso actual por otro ejecutable y conserva el PID.

> [!question]- ¿Para qué sirve `wait()` y qué entrega?
> Bloquea al padre hasta que un hijo termine y le entrega su estado: `WIFEXITED` indica si terminó normalmente y `WEXITSTATUS` extrae el código pasado a `exit()`. Así el padre sabe cuándo y cómo terminó cada hijo.

> [!question]- ¿Qué hace una fork bomb al sistema y cómo se mitiga?
> Crea procesos en forma exponencial hasta agotar la tabla de procesos, y entonces no se pueden lanzar comandos nuevos. Se mitiga limitando los procesos por usuario (`ulimit -u`, `limits.conf`).
