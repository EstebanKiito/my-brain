---
ramo: "Sistemas Operativos y Redes"
tema: "Hilos"
tags:
  - ssoo
  - threads
  - pthreads
  - c
  - posix
prerrequisitos:
  - "[[01 - Concepto de hilo y recursos compartidos versus privados]]"
---

# Programación con POSIX Threads y ciclo de vida

La API estándar para la gestión de hilos en sistemas tipo UNIX es **POSIX Threads** (definida en el estándar IEEE 1003.1c y conocida comúnmente como `pthreads`). Proporciona funciones de biblioteca para la creación, sincronización y finalización controlada de hilos.

---

## Funciones (Mas Usadas en Threads) (mis apuntes)

> - pthread_create: Crea un nuevo Thread
> - pthread_join: Espera un Thread
> - pthread_yield: Le pasa a la CPU o otro Thread → Pasarle el turno a otro Thread
> 
> OPERACIONES → FUNCIONES
> 
> ![Funciones principales de la biblioteca POSIX Threads](adjuntos/Funciones%20principales%20de%20la%20biblioteca%20POSIX%20Threads.png)

---

> [!example]- Transcripción de la imagen: Funciones principales de la biblioteca POSIX Threads.png
> **Llamadas del estándar POSIX Threads (IEEE 1003.1c):**
> 
> | Llamada (*Thread call*) | Descripción formal |
> | :--- | :--- |
> | **`pthread_create`** | Crea y pone en marcha un nuevo hilo (*Create a new thread*). |
> | **`pthread_exit`** | Termina la ejecución del hilo invocador (*Terminate the calling thread*). |
> | **`pthread_join`** | Bloquea al llamador hasta que un hilo específico finaliza (*Wait for a specific thread to exit*). |
> | **`pthread_yield`** | Cede voluntariamente la CPU para permitir la ejecución de otro hilo listo (*Release the CPU to let another thread run*). |
> | **`pthread_attr_init`** | Crea e inicializa la estructura de atributos del hilo (*Create and initialize a thread's attribute structure*). |
> | **`pthread_attr_destroy`** | Elimina la estructura de atributos de un hilo (*Remove a thread's attribute structure*). |

---

> [!tip] Complemento: Ejemplo clásico de hilos en lenguaje C
> Para compilar código que utiliza POSIX Threads en GCC o Clang se requiere la bandera `-pthread`:
> 
> ```c
> #include <stdio.h>
> #include <stdlib.h>
> #include <pthread.h>
> 
> void* tarea_hilo(void* arg) {
>     int id = *(int*)arg;
>     printf("Hilo %d ejecutando de forma concurrente\n", id);
>     pthread_exit(NULL); // Termina el hilo devolviendo un puntero de retorno
> }
> 
> int main() {
>     pthread_t hilo1, hilo2;
>     int id1 = 1, id2 = 2;
> 
>     // Crear hilos pasando la función de entrada y su argumento
>     pthread_create(&hilo1, NULL, tarea_hilo, &id1);
>     pthread_create(&hilo2, NULL, tarea_hilo, &id2);
> 
>     // Esperar a que ambos hilos concluyan (análogo a wait en procesos)
>     pthread_join(hilo1, NULL);
>     pthread_join(hilo2, NULL);
> 
>     printf("Ambos hilos finalizaron exitosamente.\n");
>     return 0;
> }
> ```
> 
> * **Similitud funcional:** `pthread_create()` cumple un rol similar a `fork()`, mientras que `pthread_join()` opera de forma análoga a `wait()`, evitando que un hilo termine sin entregar su código de salida.

---

## Preguntas de repaso

> [!question]- ¿Qué rol cumple la función pthread_join() y qué sucedería si el hilo principal (main) termina sin invocarla?
> `pthread_join()` bloquea la ejecución del hilo llamador hasta que el hilo objetivo especificado finalice, permitiendo recolectar su valor de retorno. Si la función `main()` termina con `exit()` o `return 0` sin esperar a sus hilos con `pthread_join()`, todo el proceso es destruido por el kernel y todos los hilos secundarios mueren de inmediato.

> [!question]- ¿Por qué pthread_create() recibe funciones con firma void* (*)(void*)?
> Porque utiliza punteros genéricos `void*` tanto para recibir cualquier tipo de estructura de datos como parámetro de entrada, como para devolver cualquier resultado o estructura de retorno a través de `pthread_join()`.

> [!question]- ¿Cuál es la diferencia entre pthread_exit() y exit()?
> `pthread_exit()` termina únicamente el hilo que invoca la función, permitiendo que los demás hilos del proceso continúen ejecutando normalmente. Por el contrario, la llamada a `exit()` finaliza el proceso completo en el sistema operativo, cancelando forzosamente todos los hilos en ejecución.

