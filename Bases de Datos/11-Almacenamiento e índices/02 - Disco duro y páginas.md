---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, origen/apuntes]
prerrequisitos: ["[[01 - Arquitectura de un DBMS|Arquitectura de un DBMS]]"]
---
# Disco duro y páginas

Las tablas viven en disco, que se lee por **páginas** (bloques de varios KB). Leer del disco es órdenes de magnitud más lento que leer de RAM, así que todo el diseño del almacenamiento busca minimizar las páginas leídas.

## Almacenamiento y jerarquía de memoria
### Disco duro
- **Sector:** Es la unidad física mínima de almacenamiento en un disco duro, generalmente de 512 bytes o 4096 bytes en discos más modernos.
- **Página:** Unidad lógica mínima de almacenamiento que el sistema operativo gestiona, generalmente de 4 KB.
- **Clúster:** Conjunto de sectores agrupados para mejorar la eficiencia de la gestión de archivos.
- **Estructura del disco:**
    - **Pistas:** Anillos concéntricos en el disco.
    - **Sectores:** Divisiones de las pistas.
    - **Cilindros:** Conjunto de pistas alineadas verticalmente a través de los platos del disco.

### Rendimiento del disco duro
- **Tiempo de búsqueda:** El tiempo que tarda la cabeza de lectura/escritura en posicionarse sobre la pista correcta.
- **Retraso rotacional:** El tiempo de espera hasta que el sector deseado se posiciona bajo la cabeza de lectura/escritura.
- **Tiempo de transferencia:** El tiempo necesario para transferir los datos desde el disco a la memoria principal.

> [!tip] Complemento — jerarquía de memoria (slides "Clase 9: Almacenamiento y Índices")
> ![Slide - jerarquía de memoria](adjuntos/Slide%20-%20jerarquía%20de%20memoria.png)
>
> - **Sector:** unidad física mínima del disco (definida por el hardware). **Página:** unidad lógica mínima del sistema de archivos (definida por el SO o el **DBMS**). **¡Un DBMS trabaja al nivel de página!** En PostgreSQL la página mide 8 KB.
> - La base de datos necesita hacer **persistentes** los datos en memoria secundaria.
> - "La diferencia de tiempo entre tener un dato en RAM versus traerlo de disco es comparable a la de tomar el sacapuntas del escritorio donde estoy sentado versus tomarme un avión a Punta Arenas para ir a buscarlo y regresar."
> - Tiempo de acceso a disco ≈ búsqueda + retraso rotacional + transferencia. Por eso conviene leer páginas **contiguas** (secuenciales): se paga la búsqueda una vez.

> [!note]- Transcripción de la imagen
> **Almacenamiento — jerarquía de memoria**, de arriba abajo: CPU → Cache → RAM (memoria principal) → Disco sólido → Disco duro (magnético) → Cintas. Hacia abajo es más barato y de más capacidad; hacia arriba, más rápido.

## Preguntas de repaso

1. ¿Qué diferencia hay entre un sector y una página?
> [!question]- Respuesta
> El sector es la unidad física mínima del disco (512 B o 4096 B), definida por el hardware. La página es la unidad lógica mínima que maneja el SO o el DBMS (varios KB) y es con la que trabaja el DBMS.

2. ¿Qué tres tiempos componen un acceso a disco?
> [!question]- Respuesta
> El tiempo de búsqueda (mover la cabeza a la pista), el retraso rotacional (esperar que pase el sector) y el tiempo de transferencia.

3. ¿Por qué el DBMS trata de minimizar las lecturas a disco?
> [!question]- Respuesta
> Porque leer de disco es muchísimo más lento que leer de RAM. Es el costo dominante de una consulta.
