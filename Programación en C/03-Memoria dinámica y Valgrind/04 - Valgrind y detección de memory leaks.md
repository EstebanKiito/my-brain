---
ramo: "Programación en C"
tema: "Memoria dinámica y Valgrind"
tags:
  - c
  - valgrind
  - memcheck
  - memory-leak
  - origen/complemento
prerrequisitos:
  - "[[03 - Errores de memoria y memory leaks]]"
---

# Valgrind y detección de memory leaks

**Valgrind** es un conjunto de herramientas que ejecuta el programa en una máquina virtual y **monitorea cada instrucción**. Su herramienta por defecto, **memcheck**, detecta en el **heap** los errores que C no reporta: leaks, accesos inválidos y uso de memoria no inicializada. En el stack no los detecta.

## Cómo correrlo

```bash
gcc main.c -g -o main     # -g: guarda la información de líneas para los reportes
valgrind ./main
```

El flag `-g` agrega la información de depuración (qué instrucción corresponde a qué línea del `.c`), para que Valgrind pueda decir **en qué línea** está el problema. Conviene compilar sin optimizaciones, porque el optimizador reordena y elimina código, y las líneas reportadas dejan de calzar.

El precio es la velocidad: el programa corre **del orden de 40 veces más lento**, así que Valgrind sirve para revisar la memoria, no para medir el tiempo.

![Tiempo de ejecución con y sin Valgrind](adjuntos/Tiempo%20de%20ejecuci%C3%B3n%20con%20y%20sin%20Valgrind.png)

> [!example]- Transcripción de la imagen
> `gcc main.c -g -o main` y `time ./main` da real 0m2.630s, user 0m1.938s y sys 0m0.203s. Con `time valgrind ./main` da real 1m14.508s, user 1m10.641s y sys 0m2.500s, junto a un emoji preocupado.

La salida ideal termina sin bloques en uso y con 0 errores:

![Valgrind sobre un programa sin errores](adjuntos/Valgrind%20sobre%20un%20programa%20sin%20errores.png)

> [!example]- Transcripción de la imagen
> `valgrind ./main` sobre un programa vacío. Cada línea parte con `==150==`, el identificador del proceso. Muestra el encabezado de Memcheck y luego "HEAP SUMMARY: in use at exit: 0 bytes in 0 blocks; total heap usage: 0 allocs, 0 frees, 0 bytes allocated. All heap blocks were freed -- no leaks are possible. ERROR SUMMARY: 0 errors from 0 contexts".

## Leer un leak: directo e indirecto

```c
#include <stdlib.h>

int main()
{
    int** B = malloc(10 * sizeof(int*));   // línea 5: 80 bytes
    for (int i = 0; i < 10; i += 1)
    {
        B[i] = malloc(10 * sizeof(int));   // línea 8: 40 bytes x 10
    }
    return 0;                              // no hay ningún free
}
```

![Resumen de un leak directo e indirecto](adjuntos/Valgrind%20-%20resumen%20de%20un%20leak%20directo%20e%20indirecto.png)

> [!example]- Transcripción de la imagen
> `valgrind ./leak`: "in use at exit: 480 bytes in 11 blocks; total heap usage: 11 allocs, 0 frees, 480 bytes allocated". LEAK SUMMARY: "definitely lost: 80 bytes in 1 blocks", "indirectly lost: 400 bytes in 10 blocks", "possibly lost: 0", "still reachable: 0". Sugiere "Rerun with --leak-check=full to see details of leaked memory".

- **Definitely lost** (directo): bloques cuya última referencia se perdió. Aquí es `B`.
- **Indirectly lost**: bloques que solo eran alcanzables **a través** de un bloque perdido. Las 10 filas solo se podían alcanzar por `B`.

Con `--leak-check=full`, Valgrind indica **en qué línea** se pidió cada bloque perdido:

![leak-check full apunta a la línea del malloc](adjuntos/Valgrind%20-%20leak-check%20full%20apunta%20a%20la%20l%C3%ADnea%20del%20malloc.png)

> [!example]- Transcripción de la imagen
> "480 (80 direct, 400 indirect) bytes in 1 blocks are definitely lost in loss record 2 of 2, at malloc, by main (leak_ind.c:5)". Al lado, el código con la línea 5 resaltada: `int** B = malloc(10 * sizeof(int*));`.

Si se agrega solo `free(B)`, las filas pasan a ser el leak principal:

![Leak restante tras liberar B](adjuntos/Valgrind%20-%20leak%20restante%20tras%20liberar%20B.png)

> [!example]- Transcripción de la imagen
> "400 bytes in 10 blocks are definitely lost in loss record 1 of 1, at malloc, by main (leak_ind.c:8)". LEAK SUMMARY: "definitely lost: 400 bytes in 10 blocks", "indirectly lost: 0 bytes in 0 blocks". En el código, la línea 8 (`B[i] = malloc(10 * sizeof(int));`) está resaltada y la línea 10 tiene el `free(B);` agregado.

La corrección es liberar cada `B[i]` en un ciclo **antes** de `free(B)`.

## El stack trace del reporte

Cuando el `malloc` está dentro de funciones anidadas, Valgrind muestra la **cadena de llamadas** completa hasta el punto de origen:

![Stack trace de un leak en funciones anidadas](adjuntos/Valgrind%20-%20stack%20trace%20de%20un%20leak%20en%20funciones%20anidadas.png)

> [!example]- Transcripción de la imagen
> `stack_trace.c`: `p()` retorna `malloc(sizeof(int))` (línea 4), `q()` retorna `p()` (línea 8) y `main` hace `int* H = q();` (línea 12) sin liberar. `valgrind --leak-check=full ./stack_trace` informa "4 bytes in 1 blocks are definitely lost", con el camino "at malloc, by p (stack_trace.c:4), by q (stack_trace.c:8), by main (stack_trace.c:12)".

> [!tip] Comando completo para depurar tareas
> `valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes --log-file=valgrind-out.txt ./programa input.txt output.txt` muestra todos los tipos de leak, el origen de los valores no inicializados y guarda todo en un archivo. Valgrind no corre de forma nativa en macOS; el curso propone usarlo dentro de un contenedor Docker.

## Preguntas de repaso

> [!question]- ¿Por qué hay que compilar con `-g` antes de usar Valgrind?
> Porque `-g` guarda la correspondencia entre las instrucciones de máquina y las líneas del código fuente. Sin ella, Valgrind solo puede mostrar direcciones y no dice en qué línea está el problema.

> [!question]- En el ejemplo de la matriz `B`, ¿por qué las filas aparecen como *indirectly lost* y no como *definitely lost*?
> Porque sus direcciones estaban guardadas dentro del bloque `B`, que es el que se perdió directamente. Solo eran alcanzables a través de él.

> [!question]- ¿Por qué no sirve Valgrind para medir el rendimiento de un programa?
> Porque simula cada instrucción y hace que el programa corra del orden de 40 veces más lento. Los tiempos medidos no representan la ejecución real.

> [!question]- Al liberar solo `B`, ¿cómo cambia el reporte de leaks?
> Desaparecen los 80 bytes directos de `B` y los 400 bytes de las filas pasan de *indirectly lost* a *definitely lost*, ahora atribuidos a la línea del `malloc` de cada fila.
