---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, origen/apuntes]
prerrequisitos: ["[[02 - Disco duro y páginas|Disco duro y páginas]]"]
---
# Disco, RAM y buffer pool

El DBMS trae las páginas que necesita desde el disco a un área de RAM llamada **buffer pool**. Si la página ya está ahí, no hace falta volver a leer del disco.

## Relación entre disco y RAM
- **Operación del DBMS:**
    - El sistema de gestión de bases de datos (DBMS) trabaja a nivel de página.
    - Utiliza la RAM para almacenar temporalmente las páginas cargadas desde el disco.
    - Implementa un buffer pool para gestionar estas páginas y optimizar el acceso a los datos.

> [!tip] Complemento — páginas, disco y buffer (slides "Clase 9: Almacenamiento y Índices")
> - Los registros de las tablas se guardan en **páginas de disco**. A medida que se necesitan, las páginas se traen a memoria principal (el **buffer**), que se divide en *frames* del tamaño de una página.
> - **Ejemplo:** la relación R ocupa las páginas R-1…R-4 (t1, t2 en R-1; t3, t4 en R-2, …) y S, las páginas S-1…S-3.
>   1. La BD necesita la tupla t3 de R → carga la **página R-2** completa (con t3 y t4) en un frame del buffer. **1 I/O**.
>   2. Luego necesita t4 de R → **¡ya la tenemos!** Está en R-2, que sigue en el buffer. **0 I/O**.
>
> ![Slide - páginas, disco y buffer](adjuntos/Slide%20-%20páginas,%20disco%20y%20buffer.png)
>
> - Cuando el buffer se llena, el Buffer Manager elige qué página **reemplazar** (políticas como LRU o *clock*). Si la página fue modificada (*dirty*), primero la escribe en disco. Esto se coordina con el log ([[02 - Log manager y registros de log|WAL]]).

> [!note]- Transcripción de la imagen
> DB: "Necesito tupla t4 de R" → "Cargar página con t4" → "¡Ya la tenemos!". En el buffer está la página R-2 (t3, t4). En disco: R-1 (t1, t2), R-2 (t3, t4), R-3 (t5, t6), R-4 (t7, t8), S-1 (tt1, tt2), S-2 (tt3, tt4), S-3 (tt5, tt6).

## Preguntas de repaso

1. ¿Qué es el buffer pool?
> [!question]- Respuesta
> Un área de la RAM, dividida en frames, donde el DBMS guarda las páginas que trae del disco para no tener que volver a leerlas.

2. Si la tupla t4 está en la misma página que t3 y t3 ya se leyó, ¿cuántos I/O cuesta leer t4?
> [!question]- Respuesta
> Cero, porque la página completa ya está en el buffer.

3. ¿Qué pasa cuando el buffer está lleno y se necesita otra página?
> [!question]- Respuesta
> El Buffer Manager reemplaza una página según su política (por ejemplo, LRU). Si la página reemplazada fue modificada, primero se escribe en disco.
