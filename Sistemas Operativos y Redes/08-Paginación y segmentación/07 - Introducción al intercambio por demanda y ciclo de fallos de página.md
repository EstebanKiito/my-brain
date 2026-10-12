---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/apuntes
prerrequisitos:
  - "[[01 - Fundamentos de paginación, marcos y tabla de páginas]]"
  - "[[04 - Swapping, fragmentación externa y algoritmos de asignación libre]]"
---

# Introducción al intercambio por demanda y ciclo de fallos de página

En sistemas reales, la suma de los espacios virtuales de todos los procesos excede por amplio margen la memoria RAM física instalada. El sistema operativo proporciona la ilusión de memoria ilimitada combinando la RAM con el espacio de intercambio (*swap space*) en disco mediante paginación por demanda.

## Mecanismo de fallo de página y espacio swap (mis apuntes)

> [!note] Apuntes de clase
> **Ahora veremos REEMPLAZO DE PAGINAS:**
> Suponemos que la suma de todos los espacios virtuales caben en la memoria fisica → La realidad no es así.
> Habiamos visto que cierto espacio de disco, la ibamos a usar como “memoria principal” fake (SWAP SPACE).
> Usamos el Disco (grande y lento) entonces, para proveer la ilusion que todo espacio virtual está en memoria.
> Procesos deben seguir creyendo que pueden acceder a todo el rango de direcciones virtuales.
> lo que nos queda por hacer, es llevar y traer paginas.
>
> **SWAP SPACE:**
> Paginas borradas de memoria principal, van a espacio de SWAP:
> - Representan parte del espacio de memoria de un proceso en ejecución
> - Tenemos un metadato de bit de presente (PRESENT BIT) → Para saber si la pagina esta en FRAME o no (mem fisica)
> - Page Fault: Activa el mecanismo de recuperación de una pagina desde disco a memoria fisica
> - 0 si solo tengo una copia en el espacio SWAP, y no esta cargada en la memoria principal: esto generá la INTERRUPCION:
>
> Ante el Page Fault → El SO va a buscar la pagina:
> - Estoy intentando cargar una direccion de memoria
> - Me voy a la tabla de pagina → Pero me dice que el bit de presencia esta en 0
> - Genera una interrupcion (Page Fault)
> - Le avisa al sistema operativo
> - El OS tendra que ejecutar una rutina, para tener que hacer un intercambio de pagina
> - El sistema operativo va a buscar la pagina
> - La cargamos en el espacio libre (free frame)
> - Reseteamos la info en la tabla paginas
> - Re ejecutar la instruccion que genero la interrupcion
>
> **¿Que pagina Reemplazar?**
> Ahora bien, necesitamos encontrar algun ALGORITMO que permita cada vez que no tengamos espacio libre, sacar de la memoria principal aquella pagina que sea la mejor opción (aquella que no vaya a utilizar en un futuro cercano).
> recordar : La memoria principal tiene las paginas a utilizar, las que no se utilicen tanto, mejor dejarlas en swap space, asi simulamos tener mas espacio del que realmente te

> [!warning] Posible error
> En los apuntes figura la errata "generá" por genera, y la frase final queda truncada: "realmente te" en lugar de "realmente tenemos".

![Ciclo de atención de interrupción por fallo de página](adjuntos/Ciclo%20de%20atenci%C3%B3n%20de%20interrupci%C3%B3n%20por%20fallo%20de%20p%C3%A1gina.png)

> [!example]- Transcripción de la imagen
> Secuencia de 6 pasos en la atención de un Page Fault:
> 1. La CPU genera una referencia a una página virtual.
> 2. La MMU consulta la tabla de páginas y detecta que el **Present Bit = 0** (página no residente en RAM).
> 3. La MMU dispara una trampa de interrupción (*trap*) al sistema operativo: **Page Fault**.
> 4. El manejador de fallos de página del kernel localiza la página requerida en el espacio swap del disco.
> 5. El kernel lee la página de disco y la escribe en un marco libre (*free frame*) en la RAM.
> 6. El kernel actualiza la PTE fijando el PFN y el Present Bit = 1, y reinicia la instrucción de CPU que causó la trampa.

> [!tip] Complemento: Reinicio de instrucción (*Instruction Restart*)
> A diferencia de una llamada al sistema (*syscall*), donde la CPU avanza a la siguiente instrucción tras el retorno, una interrupción por Page Fault debe devolver el control exactamente a la misma instrucción que falló (por ejemplo, el `LOAD` o `STORE` interrumpido a mitad de camino), ejecutándola ahora con éxito gracias a que la página ya está cargada en RAM física.

## Preguntas de repaso

> [!question]- ¿Qué rol cumple el bit de presencia (*Present Bit*) en la entrada de la tabla de páginas?
> Indica si la página virtual reside actualmente en un marco físico de la memoria RAM principal (valor 1) o si está guardada en el almacenamiento secundario / espacio swap (valor 0).

> [!question]- ¿Por qué un fallo de página (*Page Fault*) suspende temporalmente el proceso solicitante?
> Porque la lectura de una página desde disco (o SSD) involucra operaciones de entrada/salida (I/O) que tardan millones de ciclos de CPU. El kernel pone el proceso en estado `WAITING`/`BLOCKED` y conmuta la CPU a otro proceso listo mediante el scheduler mientras concluye la transferencia DMA.

> [!question]- Si no existen marcos físicos libres en la memoria RAM al producirse un Page Fault, ¿qué acción debe tomar el sistema operativo?
> Debe ejecutar un algoritmo de reemplazo de páginas para seleccionar una página víctima residente, escribirla a disco si fue modificada (*dirty bit = 1*), invalidar su bit de presencia y reutilizar su marco para cargar la nueva página requerida.

