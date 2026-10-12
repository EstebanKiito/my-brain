---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/apuntes
prerrequisitos:
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
---

# Fundamentos de paginación, marcos y tabla de páginas

La paginación es un mecanismo arquitectónico de gestión de memoria que desacopla el espacio de direcciones virtuales de la memoria física mediante particiones de tamaño fijo idéntico, eliminando por completo la fragmentación externa.

## Paginación y traducción de direcciones (mis apuntes)

> [!note] Apuntes de clase
> **Clase 7**
> 4/09/2024
>
> **PAGINACION**
> Otra estrategia para localizacion de memoria.
> Lo que hace es dividir la memoria fisica → en framse
> Y la virtual en → Paginas
> |Paginas| = |Frame|
>
> Para hacer esto, necesitamos informacion extra → Necesitamos una TABLA DE PAGINAS:
> - Guarda las traducciones de memoria de pagina a frame
> - Basicamente es en que frame se encuentra guardada cada pagina de un proceso
>
> **TABLA DE PAGINAS: Ejemplo**
> Para este caso, notemos que tenemos 64b de direcciones de espacio virtual:
> - direcciones = 64 = 2**6 = 6 bits necesarios
> - Entre cada pagina hay 16 bits de desplazamiento: offset = 16 = 2**4 = 4 bits
> - y 64/16 = 4 = 2**2 = 2 bits de numero de pagina
> - Bits direccion virtual = b5 b4 b3 b2 b1 b0:
>   - b5 b4 = VPN (numero pagina) → virtual page number
>   - b3 b2 b1 b0 = OFFSET
>
> En el espacio fisico: 128b = 2**7 = 7 bits necesarios:
> - offset = 16 → 4 bits
> - Numero frame = 8 = 2**3 = 3 bits (PFN) → physical frame number
> - Bits direccion fisica = b6 b5 b4 b3 b2 b1 b0:
>   - b6 b5 b4 = PFN (numero frame)
>   - b3 b2 b1 b0 = OFFSET
>
> Ahora → Como traducir una direccion a la otra?
> TABLA DE PAGINA: Almacenara la traduccion de un numero de pagina a un numero de frame.
>
> **CONCLUSION (y pregunta de prueba probablemente):**
> TRADUCCION: conservar OFFSET y cambiar VPN por PFN.
>
> La tabla ademas de las traducciones tambien almacena otros valores: (Metadatos)
> - Bit de validez: indica si la entrada es valida (si la pagina ha sido asignada) → Importante para la tarea
> - Bit de presencia: si esta en la memoria primaria o secundaria
> - Bit de escritura: indica si se puede escribir
> - etc…. → Depende de cada OS
>
> PTE (page table entry) = PFN + Metadatos
> |Tabla de pagina| = | PTE | * Numero de paginas
> Esto porque la tabla de paginas se debe almacenar en la memoria principal, y esa cantidad de memoria es significativa → Hay que tratar de reducir el tamaño de la tabla.
>
> Ojo: Esto afecta al tiempo de acceso (al doble practicamente)
> Dado que siempre para buscar una variable, primero hay que cargar la tabla de paginas para traducir, y luego ir a buscar.
> Por lo tanto: CADA ACCESO A MEMORIA SE DUPLICA (a 2 accesos).

> [!warning] Posible error
> En los apuntes figura "framse" por frames. Asimismo, la notación "64b de direcciones" y "16 bits de desplazamiento" refiere en realidad a unidades de *bytes* (un espacio virtual de 64 Bytes con páginas de 16 Bytes), pues $2^6 = 64$ y $2^4 = 16$.

![División de memoria virtual en páginas y memoria física en marcos](adjuntos/Divisi%C3%B3n%20de%20memoria%20virtual%20en%20p%C3%A1ginas%20y%20memoria%20f%C3%ADsica%20en%20marcos.png)

> [!example]- Transcripción de la imagen
> Esquema de correspondencia entre páginas y marcos:
> - Espacio de direcciones virtual particionado en páginas fijas ($P_0, P_1, P_2, P_3$).
> - Memoria física particionada en marcos de página (*page frames*) del mismo tamaño ($f_0, f_1, \dots, f_7$).
> - Una página virtual puede ubicarse en cualquier marco físico disponible, sin necesidad de contigüidad.

![Traducción de VPN a PFN preservando el offset](adjuntos/Traducci%C3%B3n%20de%20VPN%20a%20PFN%20preservando%20el%20offset.png)

> [!example]- Transcripción de la imagen
> Regla de traducción de direcciones:
> - Dirección virtual: dividida en VPN (*Virtual Page Number*) y Offset.
> - El VPN indexa la Tabla de Páginas para obtener el PFN (*Physical Frame Number*).
> - Dirección física = $\text{PFN concatenated with Offset}$. El desplazamiento interno permanece idéntico.

![Estructura de la entrada de tabla de páginas y metadatos](adjuntos/Estructura%20de%20la%20entrada%20de%20tabla%20de%20p%C3%A1ginas%20y%20metadatos.png)

> [!example]- Transcripción de la imagen
> Formato de una PTE (*Page Table Entry*):
> - PFN: bits que identifican el marco físico asignado.
> - Bit de validez ($V$): 1 si la página pertenece al espacio del proceso, 0 si no está mapeada.
> - Bit de presencia ($P$): 1 si reside en RAM física, 0 si está en el espacio de intercambio (*swap*).
> - Bits de protección: permisos $R$ (lectura), $W$ (escritura), $X$ (ejecución).
> - Bit de referencia / modificado (*dirty bit*): registra accesos y modificaciones.

![Duplicación de accesos a memoria por consulta a tabla de páginas](adjuntos/Duplicaci%C3%B3n%20de%20accesos%20a%20memoria%20por%20consulta%20a%20tabla%20de%20p%C3%A1ginas.png)

> [!example]- Transcripción de la imagen
> Sobrecarga temporal de la paginación pura:
> Para ejecutar una sola instrucción que lee una variable (e.g. `MOV EAX, [addr]`):
> 1. Primer acceso a memoria RAM: leer la PTE correspondiente en la tabla de páginas del proceso.
> 2. Segundo acceso a memoria RAM: leer el byte solicitado en la dirección física traducida.
> Todo acceso se duplica, reduciendo la velocidad a la mitad.

> [!tip] Complemento: Eliminación de la fragmentación externa
> Dado que todos los marcos físicos tienen exactamente el mismo tamaño que las páginas virtuales, cualquier marco libre en RAM puede satisfacer la solicitud de cualquier página. Como consecuencia directa, la paginación elimina completamente la fragmentación externa.

## Preguntas de repaso

> [!question]- ¿Por qué el desplazamiento (*offset*) permanece invariante al traducir una dirección virtual a una dirección física?
> Porque tanto la página virtual como el marco físico tienen idéntico tamaño. El offset representa la distancia en bytes relativa al inicio del bloque, por lo que el byte $k$ de la página virtual se ubica exactamente en el byte $k$ del marco físico asignado.

> [!question]- ¿Qué ocurre si un proceso intenta acceder a una dirección virtual cuyo bit de validez en la PTE es 0?
> La MMU detecta que la entrada no es válida, bloquea el acceso físico a la memoria y genera una excepción de trampa (*trap*) al kernel, provocando que el sistema operativo envíe una señal `SIGSEGV` (*Segmentation Fault*) al proceso.

> [!question]- Si un sistema posee páginas de 4 KB y direcciones virtuales de 32 bits, ¿cuántos bits se destinan al offset y cuántos al VPN?
> Como $4\text{ KB} = 2^{12}\text{ bytes}$, el offset requiere 12 bits para direccionar dentro de la página. Los restantes $32 - 12 = 20\text{ bits}$ identifican el número de página virtual (VPN).

