---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/apuntes
prerrequisitos:
  - "[[02 - Memoria principal y el desafío de la multiprogramación]]"
  - "[[01 - Concepto de proceso y espacio de memoria]]"
---

# Relocalización, protección de memoria y registros base y límite

Para permitir la multiprogramación segura, el sistema operativo y el hardware resuelven dos problemas fundamentales: la relocalización dinámica (ubicar variables en posiciones variables de la memoria física) y la protección de memoria (aislar los espacios para evitar que un proceso acceda o modifique regiones ajenas).

## Relocalización, protección y MMU (mis apuntes)

> [!note] Apuntes de clase
> **PROBLEMA 1: Relocalización de memoria**
> → Problema con intentar acceder a memoria realocalizada, las variables no siempre estan en la misma ubicacion.
>
> **PROBLEMA 2: Proteccion de memoria → Segmentation Fault**
> Por ejemplo leer/escribir memoria que no correspondia al programa.
> En lugar de usar direcciones absolutas, usaremos Virtuales.
>
> **DIRECCIONES:**
> - Direcciones Absoultas: Relacionadas a la memoria Ram/principal
> - Direcciones Virtuales: Las que “ve” el proceso, y entiende en el universo del proceso
> - Espacio de direccion para los procesos
>
> Lo que haremos al final: Usaremos Direcciones virtuales en vez de absolutas.
> Instrucciones codigo variables se van a encontrar en la misma lugar desde el punto de vista del proceso.
>
> **TRADUCCION VIRTUAL → ABSOLUTA:**
> Antiguamente: 2 registros, uno base y uno limit, para saber donde empieza y termina el espacio.
> El espacio de memoria de un proceso se DIVIDE en SEGMENTOS.
> Tienen cierta interpretacion:
> → Code Heap y stack, memoria dinamica va creciendo en funcion del programa.
> - Heap Crece
> - Stack Decrece
>
> Al codigo base de la direccion, se le suma la direccion virtual, y esa se entrega como direccion Fisica.
> La MMU: Memory Managment Unit → Es quien realiza esos calculos.
> Los tipicos problemas como segmentation fault, son que nos salimos de la dirección que tenemos para el programa.
> Ahora bien, ese calculo no es tan eficiente, existen mejores estrategias.

> [!warning] Posible error
> En los apuntes aparecen erratas tipográficas: "realocalizada" por relocalizada, "Direcciones Absoultas" por Absolutas, y "Memory Managment Unit" por *Memory Management Unit*.

![Traducción de direcciones con registros base y límite en MMU](adjuntos/Traducci%C3%B3n%20de%20direcciones%20con%20registros%20base%20y%20l%C3%ADmite%20en%20MMU.png)

> [!example]- Transcripción de la imagen
> Arquitectura de hardware para traducción con registros Base y Límite:
> 1. La CPU genera una dirección lógica (virtual).
> 2. Se compara la dirección lógica contra el **Registro Límite** (*Limit Register*).
>    - Si $\text{dirección lógica} \ge \text{límite}$, se genera una trampa por violación de memoria (*Segmentation Fault* o *Trap* al SO).
>    - Si $\text{dirección lógica} < \text{límite}$, prosigue la operación.
> 3. Se suma la dirección lógica al **Registro Base** (*Relocation/Base Register*):
>    $$\text{Dirección Física} = \text{Registro Base} + \text{Dirección Lógica}$$
> 4. La dirección física resultante se envía al bus de memoria RAM.

> [!tip] Complemento: Rol de la MMU y aislamiento
> La unidad de hardware encargada de este proceso es la **MMU** (*Memory Management Unit*). Los registros base y límite son cargados por el sistema operativo en cada cambio de contexto con instrucciones privilegiadas (modo kernel). El proceso de usuario jamás puede modificar estos registros; de esta forma, cualquier intento de acceder más allá del límite genera una interrupción de hardware (*general protection fault*), abortando el proceso sin comprometer al resto del sistema.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia conceptual entre una dirección virtual (lógica) y una dirección física?
> Una dirección virtual es la que referencia la CPU desde el espacio lineal y continuo del proceso, comenzando habitualmente en 0. Una dirección física es la posición real y tangible en las celdas de la memoria RAM donde residen los datos, calculada por la MMU.

> [!question]- ¿Cómo detecta la MMU un intento ilegal de acceso a memoria (*Segmentation Fault*) bajo el esquema de base y límite?
> Antes de realizar la suma con el registro base, la MMU compara la dirección lógica generada contra el registro límite. Si la dirección lógica es mayor o igual que el límite, el hardware bloquea el acceso a memoria y dispara una trampa (*trap*) de excepción al kernel, el cual envía `SIGSEGV` al proceso infractor.

> [!question]- ¿En qué direcciones crecen el Heap y el Stack en el espacio virtual tradicional de un proceso?
> El Heap crece hacia direcciones de memoria más altas (hacia arriba) a medida que se asigna memoria dinámica con `malloc`, mientras que el Stack crece hacia direcciones más bajas (hacia abajo) al apilar marcos de activación de funciones.
