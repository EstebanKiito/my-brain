---
ramo: "Seguridad Computacional"
tema: "Buffer overflows y baggy bounds"
tags:
  - seguridad/memoria
  - c
  - origen/complemento
prerrequisitos:
  - "[[03 - Defensa en profundidad y seguridad imperfecta]]"
---

# Buffer overflows y sus defensas

En C un arreglo no sabe su tamaño: nada impide escribir más allá de su final. Si ese exceso pisa datos de control (como la dirección de retorno), un atacante puede tomar el control del programa. Siguen siendo una vía de ataque popular, y su historia es el ejemplo clásico de ataque y defensa que evolucionan juntos.

## Lo que hay que saber de memoria en C
Cada proceso tiene `text` (código), `data`, `bss`, `heap` (crece hacia arriba, con `malloc`) y `stack` (crece hacia abajo, un marco por llamada a función). Los parámetros se pasan por valor: para modificar el original se pasa un puntero (`&x`).

![Layout de un programa en memoria](adjuntos/Layout%20de%20un%20programa%20en%20memoria.png)

> [!example]- Transcripción de la imagen
> De la dirección alta a la baja: `stack` (crece hacia abajo), espacio libre, `heap` (crece hacia arriba), `bss` (inicializado en 0 al arrancar), `data` y `text` (código); estos dos últimos se leen del disco.

## El ataque clásico en el stack
Con `char buf[128]; gets(buf);`, si la entrada pasa de 128 bytes, `gets` sigue escribiendo hacia direcciones altas: pisa `i`, el `%rbp` guardado y la **dirección de retorno**. Al ejecutar `ret`, el procesador salta a donde diga esa dirección. El ataque tiene dos partes: (1) meter instrucciones en el búfer y (2) sobrescribir la dirección de retorno para que apunte a ellas. Entonces el atacante puede hacer lo que pueda la aplicación (si corre como root, todo).

![Stack de read_req con buf, i y dirección de retorno](adjuntos/Stack%20de%20read_req%20con%20buf,%20i%20y%20dirección%20de%20retorno.png)

> [!example]- Transcripción de la imagen
> De arriba abajo: marco de `main()`, dirección de retorno, `%rbp` guardado (donde apunta `%rbp`), `i`, `...`, `buf[127]` … `buf[0]` (donde apunta `%rsp`). El desborde de `buf` avanza hacia arriba.

En el laboratorio se ve con `gdb`: al meter 190 letras "A" (0x41), el `rbp` guardado y el retorno quedan como `0x41414141` y el programa cae con *segmentation fault*.

## Defensas

| Defensa | Qué hace | Cómo se esquiva |
|---|---|---|
| Lenguaje con verificación de límites (Python, Java) | Evita el error de raíz | Demasiado código C existente |
| No usar funciones inseguras (`gets`) | Quita la causa típica | Otros errores de límites |
| **NX** (*No eXecute*) | El SO marca el stack como no ejecutable: lo inyectado no corre | Saltar a código que ya existe (por ejemplo, un puntero a función) |
| **Stack canary** | El compilador pone un valor aleatorio entre variables y dirección de retorno y lo comprueba antes de `ret` | Leer o adivinar el canario; pisar variables o punteros a función antes de él |
| **ASLR** | Direcciones aleatorias de stack, heap y código: el atacante no sabe dónde saltar | Filtrar direcciones |

![Stack con canario entre buf y dirección de retorno](adjuntos/Stack%20con%20canario%20entre%20buf%20y%20dirección%20de%20retorno.png)

> [!example]- Transcripción de la imagen
> Igual al stack anterior, pero entre `buf[127]` y el `%rbp` guardado hay una caja `CANARY`. Una flecha indica "el overflow va en este sentido": para llegar a la dirección de retorno debe pisar el canario, y se detecta.

> [!tip] NX no es perfecto, pero no es inútil
> Ninguna defensa sola basta; cada una sube el costo del atacante (defensa en profundidad). El canario se llama así por los canarios de las minas: si muere, hay peligro.

## Buffer overflow en el heap
Los bloques libres de `malloc` forman una lista doblemente enlazada. Si el atacante desborda un bloque, puede alterar `next` y `prev` del siguiente. Cuando `malloc` lo elija, ejecuta `b->next->prev = b->prev; b->prev->next = b->next;`, que con valores elegidos equivale a *escribir un valor arbitrario en una dirección arbitraria*. El ataque es más difícil que en el stack (memoria poco estructurada) pero real.

![Ataque al heap con la lista de bloques libres](adjuntos/Ataque%20al%20heap%20con%20la%20lista%20de%20bloques%20libres.png)

> [!example]- Transcripción de la imagen
> Diapositiva "Ataques de heap": malloc mantiene los bloques libres en una lista doblemente enlazada ordenada por dirección (para fusionar bloques adyacentes); al asignar un bloque `b` hace `b->next->prev = b->prev` y `b->prev->next = b->next`; si el atacante desborda un bloque, puede modificar `next` y `prev` del bloque siguiente.

## Preguntas de repaso

> [!question]- ¿Por qué sobrescribir la dirección de retorno da control al atacante?
> Porque al terminar la función `ret` carga esa dirección en el contador de programa; si el atacante la eligió, el procesador ejecuta lo que él quiera (por ejemplo, el código que dejó en el búfer).

> [!question]- Si el stack es no ejecutable (NX), ¿ya no hay que preocuparse?
> No: el atacante puede reutilizar código existente o pisar punteros a función y variables de control. NX solo elimina la inyección directa de instrucciones en el stack.

> [!question]- ¿Por qué el canario debe ser aleatorio?
> Si fuera fijo, el atacante lo incluiría en su entrada y la comprobación pasaría; al ser aleatorio por ejecución no puede conocerlo sin una filtración.
