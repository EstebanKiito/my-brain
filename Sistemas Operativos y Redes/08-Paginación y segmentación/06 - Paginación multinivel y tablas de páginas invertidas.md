---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/complemento
prerrequisitos:
  - "[[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna]]"
  - "[[05 - Arquitectura de segmentos paginados]]"
---

# Paginación multinivel y tablas de páginas invertidas

Los [[05 - Arquitectura de segmentos paginados|segmentos paginados]] achicaban la tabla, pero traían de vuelta la fragmentación externa. La **paginación multinivel** es la misma idea, pero más genérica, y es la que usan los sistemas modernos: en vez de segmentar la tabla de páginas, **se pagina la tabla de páginas**. La **tabla invertida** toma el camino opuesto: una sola tabla para todo el sistema.

## Paginación multinivel

Se toma el VPN y se divide en tantas partes como niveles se quieran; las partes no tienen por qué tener la misma cantidad de bits. Con 2 niveles:

- **VPN0** indexa la **tabla principal** (*page directory*), cuyas entradas apuntan a tablas de segundo nivel;
- **VPN1** indexa una **tabla de segundo nivel**, que tiene las traducciones a PFN.

Si una sección grande del espacio virtual no se usa, **su tabla de segundo nivel no existe en memoria**, y ahí está el ahorro.

![Paginación multinivel con división jerárquica de VPN](adjuntos/Paginaci%C3%B3n%20multinivel%20con%20divisi%C3%B3n%20jer%C3%A1rquica%20de%20VPN.png)

> [!example]- Transcripción de la imagen
> Dirección de 14 bits: el VPN (bits 13-6) se divide en **VPN0** = bits 13-10 (*Page Directory Index*) y **VPN1** = bits 9-6 (*Page Table Index*); el offset son los bits 5-0.

### Ejemplo: 14 bits, páginas de 64 B

Con páginas de $64 = 2^6$ B hay 6 bits de offset y $14 - 6 = 8$ de VPN:

| Esquema | Entradas en memoria |
|---|---|
| 1 nivel | $2^8 = $ **256 PTE**, siempre |
| 2 niveles (VPN0 de 4 bits, VPN1 de 4 bits) | tabla principal de **16** + una tabla de 2.º nivel de **16** por cada sección usada |

Si el proceso solo usa una sección, basta la tabla principal y una secundaria: $16 + 16 = $ **32 PTE**, es decir, $16 \times 4\text{ B} + 16 \times 4\text{ B} = 128$ B en vez de 1 KB. Pasamos de 256 PTE a 32.

![Estructura de árbol de directorios y tablas de páginas](adjuntos/Estructura%20de%20%C3%A1rbol%20de%20directorios%20y%20tablas%20de%20p%C3%A1ginas.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano de una tabla de páginas lineal cortada en dos mitades (llaves moradas). La mitad de arriba, marcada **VPN0**, tiene dos entradas usadas (rayadas); una flecha roja marca **VPN1** dentro de ella. La mitad de abajo está vacía.

![Ejemplo numérico de traducción en paginación de dos niveles](adjuntos/Ejemplo%20num%C3%A9rico%20de%20traducci%C3%B3n%20en%20paginaci%C3%B3n%20de%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> "Paginación multinivel": la mitad usada (VPN0) se convierte en una tabla pequeña. La mitad vacía apunta a una tabla tachada con una cruz roja: no se crea.

![Ahorro de memoria por tablas no asignadas en dos niveles](adjuntos/Ahorro%20de%20memoria%20por%20tablas%20no%20asignadas%20en%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> Lo mismo con las secciones llamadas **S0** y **S1**, y abajo la tabla de primer nivel **T. lvl 1** con entradas S0, S1, S2…: la entrada S0 apunta a su tabla de segundo nivel y la de S1 apunta a la tabla tachada.

![Estructura jerárquica de paginación a tres niveles](adjuntos/Estructura%20jer%C3%A1rquica%20de%20paginaci%C3%B3n%20a%20tres%20niveles.png)

> [!example]- Transcripción de la imagen
> El mismo dibujo con la tabla de segundo nivel **T2** (la de S0), la de S1 tachada y **T. lvl 1** con la anotación $2^4 = 16$. Abajo: $|T_1| + |T_2| = 32$ PTE.

> [!warning] El ahorro depende de no usar todo
> Si el proceso usara **toda** su memoria virtual, tendría todas las tablas de segundo nivel y además la principal: usaría **más** espacio que una tabla lineal. El ahorro existe porque es difícil que un proceso use toda su memoria virtual: las secciones que no usa no tienen tabla.

![Comparación de espacio entre tabla lineal y dos niveles](adjuntos/Comparaci%C3%B3n%20de%20espacio%20entre%20tabla%20lineal%20y%20dos%20niveles.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano del caso sin ahorro: la tabla completa, con las secciones S0 y S1 enteras rayadas (todas sus entradas usadas).

### Tres o más niveles

El esquema se extiende a más niveles, y cada división puede tener distinto tamaño. En memoria se necesita **la tabla de primer nivel completa** y **una tabla de cada nivel** para poder resolver una dirección. Las tablas intermedias guardan **punteros a tablas**; solo la de último nivel guarda las traducciones VPN → PFN.

![Descomposición de dirección virtual para tres niveles](adjuntos/Descomposici%C3%B3n%20de%20direcci%C3%B3n%20virtual%20para%20tres%20niveles.png)

> [!example]- Transcripción de la imagen
> Dirección de 30 bits: el VPN (bits 29-9) se divide en **PD Index 0** (29-23), **PD Index 1** (22-16) y **Page Table Index** (15-9); el offset son los bits 8-0.

![Recorrido jerárquico hasta la tabla de último nivel](adjuntos/Recorrido%20jer%C3%A1rquico%20hasta%20la%20tabla%20de%20%C3%BAltimo%20nivel.png)

> [!example]- Transcripción de la imagen
> Traducción en x86 con 3 niveles: el registro **CR3** apunta a la *Page directory pointer table*. Los bits 31-30 eligen un *PDPTE*, que lleva a un *Page directory*. *Directory (9 bits)*, bits 29-21, elige un *PDE*, que lleva a una *Page Table*. *Page table (9 bits)*, bits 20-12, elige un *PTE*, que da la base de 40 bits de una *4 KB page*. El *Offset (12 bits)*, bits 11-0, ubica la *Physical address* dentro de la página.

En x86-64 se usan 4 niveles (la raíz se llama PML4) de 9 bits cada uno más 12 bits de offset: $4 \times 9 + 12 = 48$ bits de dirección virtual. Hay una extensión a 5 niveles, con 57 bits.

El costo: en un TLB miss, cada nivel es un acceso más a memoria antes de llegar al dato, así que una buena TLB se vuelve aún más importante.

## Tabla de páginas invertida

En lugar de guardar una tabla por proceso, se mantiene **una tabla única para todo el sistema**, con **una entrada por frame** físico. Cada entrada dice qué **(PID, página)** está en ese frame.

- **Consume menos memoria**: su tamaño depende de la RAM, no de la cantidad de procesos.
- Pero **la búsqueda es lenta**: para traducir hay que buscar la clave (PID, página) y, en principio, recorrer la tabla secuencialmente. La alternativa es usar *hashing*.

![Concepto y estructura de tabla de páginas invertida](adjuntos/Concepto%20y%20estructura%20de%20tabla%20de%20p%C3%A1ginas%20invertida.png)

> [!example]- Transcripción de la imagen
> La CPU emite una *logical address* `pid | p | d`. Se busca (*search*) en la *page table* la entrada `pid | p`. Su posición `i` es el número de frame, y la *physical address* es `i | d`.

![Búsqueda y sobrecarga en tabla de páginas invertida](adjuntos/B%C3%BAsqueda%20y%20sobrecarga%20en%20tabla%20de%20p%C3%A1ginas%20invertida.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano de la tabla invertida: filas numeradas 0, 1, 2, …, N (una por frame) y columnas **VPN** y **PID**.

## Resumen de estrategias de memoria

| Estrategia | Idea | Problema que deja |
|---|---|---|
| Segmentación | Un bloque por segmento | Fragmentación externa |
| Paginación | Bloques de tamaño fijo | Tablas grandes, fragmentación interna |
| Segmentos paginados | Una tabla por segmento | Vuelve la fragmentación externa (de tablas) |
| Multinivel | Paginar la tabla de páginas | Más accesos por TLB miss |
| Invertida | Una tabla por frame, global | Búsqueda lenta |

## Preguntas de repaso

> [!question]- ¿Cuántas PTE necesita una dirección de 14 bits con páginas de 64 B con 1 nivel y con 2 niveles (4+4 bits), si el proceso usa una sola sección?
> Con 1 nivel, $2^8 = 256$. Con 2 niveles, la tabla principal (16) más una secundaria (16): 32 PTE.

> [!question]- ¿Cuándo la paginación multinivel no ahorra memoria?
> Cuando el proceso usa todo su espacio virtual: existen todas las tablas de segundo nivel y además la principal, lo que suma más que una tabla lineal.

> [!question]- ¿Qué guardan las tablas intermedias y qué guarda la de último nivel?
> Las intermedias guardan punteros a la tabla del nivel siguiente; la de último nivel guarda las traducciones VPN → PFN.

> [!question]- ¿Qué ventaja y qué desventaja tiene la tabla de páginas invertida?
> Ventaja: una sola tabla para todo el sistema, cuyo tamaño depende de la RAM y no de los procesos. Desventaja: la traducción requiere buscar (PID, página), lo que es lento si es secuencial, así que se usa hashing.
