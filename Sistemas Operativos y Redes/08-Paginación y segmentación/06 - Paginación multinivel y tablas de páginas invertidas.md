---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/apuntes
prerrequisitos:
  - "[[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna]]"
  - "[[05 - Arquitectura de segmentos paginados]]"
---

# Paginación multinivel y tablas de páginas invertidas

Para gestionar espacios de direcciones dispersos en arquitecturas modernas sin requerir memoria contigua para las tablas de páginas, los sistemas operativos emplean estructuras jerárquicas de paginación multinivel o esquemas globales de paginación invertida.

## Paginación multinivel e invertida (mis apuntes)

> [!note] Apuntes de clase
> **OTRA ESTRATEGIA: PAGINACION MULTI-NIVEL**
> Es lo mismo que la estrategia anterior → Pero mas generica!
> Esta es la que utilizan los sitemas modernos.
> En vez de segmentar, PAGINAR la tabla de paginas.
>
> A grandes Rasgos:
> - Toma el VPN y lo divide en la cantidad de niveles que necesitemos
> - Si queremos 2 niveles, dividimos en 2 el vpn (no necesaraimente tiene que ser igual cantidad de bits las mitades)
> Por cada seccion grande, tendre una tabla de paginas, luego si hay alguna seccion que no este utilizando, no tengo porque tener guardada dentro de la memoria su tabla → (ahorro espacio).
>
> **EJEMPLO:**
> Dirección Virtual de 14 bit, paginas de 64 B:
> - Esquemas de 1 Nivel: 2**14 / 2**6 = 2**8 paginas posibles → 256 PTE´s
> - 4 bits para vpn0: 16 PTE en tabla Principal
> - 4 bits para vpn1: 16 PTE en la tablas de 2o Nivel
> - Esquemas de 2 Nivel: Como vimos en el ejemplo de arriba (de los 14 bit: 8 son de vpn0, vpn1)
>
> Graficamente se ve como que una tabla (principal), lleva a una seccion (1er nivel), y dentro de ese nivel, la 2da tabla (del vpn1), nos indica la direccion dentro de la 2da.
> Ahora bien, el AHORRO, solo es significativo, cuando no estoy usando toda la memoria, → No tendria ahorro alguno:
> - si por ejemplo tuviera que usar toda: Es dificil que un proceso utilice TODA su memoria virtual. A la larga, usaría mas por tener mas tablas.
> - Sin embargo, si hay tablas que no estoy contando, estoy ahorrando espacio!!
> - Redujimos los 256 PTES de usar todo el nivel cargado (tabla) → A 32 PTEs.
>
> **A 3 NIVELES:**
> Se vería algo asi:
> En memoria, se necesita la tabla de paginas del 1er NIVEL
> Y una tabla de cada Nivel para poder Resolver una Direccion Fisica
> - PAGE TABLE: La tabla de ultimo nivel guarda las traducciones a (VPN → PFN)
> - LA otras tablas: Guardan Punteros a Tablas
>
> **PAGINACION INVERTIDA:**
> En lugar de guardar una tabla por proceso, mantener una tabla única para todo el sistema!
> Una unica tabla de pagiunas indexada por frames → Busqueda es mas costosa!
> - Lo mas importante de aprender de memoria talvez, sea PAGINACION, no todo!
>
> **Resumen:**
> Vimos las estrategias para usar la memoria de manera eficiente:
> - Segmentacion
> - Paginacion
> - Segmento Paginado
> - Paginacion Multi-nivel
> - Paginacion Inversa

> [!warning] Posible error
> En los apuntes se aprecian erratas de tipeo: "sitemas" por sistemas, "necesaraimente" por necesariamente, y "pagiunas" por páginas.

![Paginación multinivel con división jerárquica de VPN](adjuntos/Paginaci%C3%B3n%20multinivel%20con%20divisi%C3%B3n%20jer%C3%A1rquica%20de%20VPN.png)

> [!example]- Transcripción de la imagen
> Partición jerárquica de la dirección virtual:
> El VPN se descompone en índices para cada nivel del árbol: $VPN_0$ indexa el Directorio de Páginas (*Page Directory*), y $VPN_1$ indexa la Tabla de Páginas (*Page Table*) correspondiente.

![Estructura de árbol de directorios y tablas de páginas](adjuntos/Estructura%20de%20%C3%A1rbol%20de%20directorios%20y%20tablas%20de%20p%C3%A1ginas.png)

> [!example]- Transcripción de la imagen
> Jerarquía de dos niveles:
> - Nivel 1: *Page Directory* (guarda direcciones físicas a tablas de segundo nivel y bits de presencia/validez).
> - Nivel 2: *Page Tables* (guardan los PFN y metadatos reales).

![Ejemplo numérico de traducción en paginación de dos niveles](adjuntos/Ejemplo%20num%C3%A9rico%20de%20traducci%C3%B3n%20en%20paginaci%C3%B3n%20de%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> Dirección virtual de 14 bits con páginas de 64 bytes (6 bits offset):
> - 8 bits para VPN: dividido en $VPN_0$ (4 bits, 16 entradas en directorio) y $VPN_1$ (4 bits, 16 entradas por tabla de segundo nivel).

![Ahorro de memoria por tablas no asignadas en dos niveles](adjuntos/Ahorro%20de%20memoria%20por%20tablas%20no%20asignadas%20en%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> Ahorro de espacio en memoria:
> Si un proceso solo utiliza páginas en el rango inicial y final de su espacio, solo se asignan 2 tablas de segundo nivel. Las 14 entradas restantes del directorio apuntan a `NULL`, ahorrando el 87% de la memoria de traducción.

![Comparación de espacio entre tabla lineal y dos niveles](adjuntos/Comparaci%C3%B3n%20de%20espacio%20entre%20tabla%20lineal%20y%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> Comparativa de sobrecarga:
> En la tabla lineal, se requieren obligatoriamente 256 PTEs en memoria contigua. En dos niveles, con dos rangos activos, bastan 16 entradas de directorio + 32 PTEs de segundo nivel = 48 entradas en total.

![Estructura jerárquica de paginación a tres niveles](adjuntos/Estructura%20jer%C3%A1rquica%20de%20paginaci%C3%B3n%20a%20tres%20niveles.png)

> [!example]- Transcripción de la imagen
> Extensión a 3 niveles:
> Raíz (Nivel 1) $\to$ Directorio intermedio (Nivel 2) $\to$ Tabla de páginas (Nivel 3) $\to$ Marco físico (RAM).

![Descomposición de dirección virtual para tres niveles](adjuntos/Descomposici%C3%B3n%20de%20direcci%C3%B3n%20virtual%20para%20tres%20niveles.png)

> [!example]- Transcripción de la imagen
> Formato de dirección con 3 niveles:
> `[ VPN_0 | VPN_1 | VPN_2 | Offset ]`.

![Recorrido jerárquico hasta la tabla de último nivel](adjuntos/Recorrido%20jer%C3%A1rquico%20hasta%20la%20tabla%20de%20%C3%BAltimo%20nivel.png)

> [!example]- Transcripción de la imagen
> Navegación en el árbol por el Page Table Walker de hardware:
> Cada nivel intermedio almacena punteros a la base física de la siguiente tabla; únicamente la tabla de hojas (último nivel) contiene el PFN final de datos.

![Concepto y estructura de tabla de páginas invertida](adjuntos/Concepto%20y%20estructura%20de%20tabla%20de%20p%C3%A1ginas%20invertida.png)

> [!example]- Transcripción de la imagen
> Tabla de Páginas Invertida (*Inverted Page Table*):
> La tabla posee exactamente una entrada por cada marco físico real en RAM (indexada por PFN). Cada entrada contiene `[PID, VPN]`, registrando qué proceso y qué página ocupan dicho marco físico.

![Búsqueda y sobrecarga en tabla de páginas invertida](adjuntos/B%C3%BAsqueda%20y%20sobrecarga%20en%20tabla%20de%20p%C3%A1ginas%20invertida.png)

> [!example]- Transcripción de la imagen
> Búsqueda con Hash Anchor Table:
> Para encontrar el marco físico dado un par `(PID, VPN)`, se aplica una función de hash sobre `(PID, VPN)` para indexar una tabla hash y resolver colisiones por encadenamiento, evitando el costo de un escaneo secuencial exhaustivo sobre toda la RAM.

> [!tip] Complemento: Arquitecturas de 64 bits y paginación a 4 y 5 niveles
> En procesadores x86-64 modernos, el espacio virtual utiliza 48 bits direccionables descompuestos en 4 niveles de 9 bits cada uno ($4 \times 9 = 36$ bits de VPN) más 12 bits de offset ($2^{12} = 4\text{ KB}$): PML4 $\to$ PDPT $\to$ PD $\to$ PT. La extensión moderna de Intel con paginación de 5 niveles (*5-level paging*) expande el espacio a 57 bits.

## Preguntas de repaso

> [!question]- ¿Por qué una estructura de paginación multinivel ahorra memoria si en el peor caso consume más espacio que una lineal?
> Porque en la práctica los procesos tienen espacios de memoria muy dispersos (*sparse*): reservan código al inicio y stack al final, dejando un enorme vacío intermedio. En multinivel, las entradas del directorio para regiones no reservadas se marcan como no válidas y no se asignan sus tablas de páginas hijas en RAM.

> [!question]- ¿Qué desventaja temporal introduce la paginación multinivel en caso de un TLB Miss?
> Cada nivel adicional añade una lectura obligatoria a memoria RAM física antes de encontrar el dato. En un esquema de 4 niveles, un fallo de TLB requiere 4 accesos a memoria para descender por el árbol más 1 acceso final para el dato (5 accesos en total), haciendo que la tasa de aciertos de la TLB sea crítica.

> [!question]- ¿Cuál es la principal ventaja y la principal desventaja de una tabla de páginas invertida?
> Ventaja: El consumo de memoria es fijo y proporcional únicamente al tamaño de la RAM física instalada, independientemente de cuántos cientos de procesos se estén ejecutando. Desventaja: La traducción de VPN a PFN no es directa por indexación, requiriendo búsquedas con funciones hash o cadenas de colisión que aumentan la latencia.

