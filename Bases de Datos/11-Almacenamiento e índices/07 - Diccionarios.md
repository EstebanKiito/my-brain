---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, bd/edd, origen/apuntes]
prerrequisitos: ["[[06 - Arreglos y listas ligadas|Arreglos y listas ligadas]]"]
---
# Diccionarios

Un diccionario es una estructura que guarda pares **llave → valor** y permite insertar, actualizar, buscar y borrar por llave de forma eficiente, sin importar el orden de las llaves. Es lo que hace un índice de una base de datos.

## Diccionarios
- Es una estructura de datos que permite:
    - asociar un valor a una llave;
    - actualizar el valor asociado a una llave;
    - obtener el valor asociado a una llave;
    - eliminar de la estructura la asociación llave-valor.
- Es eficiente al buscar por llave.
- El orden de las llaves **no** es relevante.

### Ejemplo

![Ejemplo - 25.000 estudiantes en un arreglo](adjuntos/Ejemplo%20-%2025.000%20estudiantes%20en%20un%20arreglo.png)

> [!note]- Transcripción de la imagen
> **Ejemplo:** En la universidad hay aproximadamente 25.000 estudiantes este año. Asignamos un k ∈ {0, …, 24.999} a cada estudiante y usamos cada natural como índice del arreglo A.

- Rango de RUT: hasta 25.000.000.
- Cantidad de estudiantes: 25.000, muchos menos.
- Problema: en un arreglo indexado por RUT, solo 1 de cada 1000 celdas estaría ocupada.
- Las [[08 - Tablas de hash|tablas de hash]] reducen el espacio de llaves a un tamaño razonable.

> [!tip] Complemento — por qué no basta un arreglo
> - Si la llave fuera un número pequeño y denso (0…24.999), un arreglo sería un diccionario perfecto: buscar = `A[k]`, en $O(1)$.
> - Pero la llave natural es el **RUT**, que llega a 25.000.000. Un arreglo indexado por RUT necesitaría 25 millones de celdas para 25.000 estudiantes: $25.000 / 25.000.000 = 1/1000$ de ocupación, un desperdicio enorme.
> - La solución es una función que lleve el RUT a un rango pequeño: la **función de hash** ([[08 - Tablas de hash|Tablas de hash]]).
>
> | Operación | Ejemplo en Python |
> |---|---|
> | asociar / actualizar | `d[rut] = "Ana"` |
> | obtener | `d[rut]` |
> | eliminar | `del d[rut]` |
>
> Los `dict` de Python son tablas de hash, igual que los Hash de [[05 - Arreglos y hashes en Ruby|Ruby]].

## Preguntas de repaso

1. ¿Qué operaciones ofrece un diccionario?
> [!question]- Respuesta
> Asociar un valor a una llave, actualizarlo, obtenerlo y eliminar la asociación llave-valor, todo de forma eficiente por llave.

2. ¿Por qué es mala idea un arreglo indexado por RUT para 25.000 estudiantes?
> [!question]- Respuesta
> Porque el rango de RUT llega a 25.000.000: el arreglo tendría 25 millones de celdas y solo 1 de cada 1000 estaría ocupada.

3. ¿Qué estructura resuelve ese problema?
> [!question]- Respuesta
> Una tabla de hash, que lleva las llaves a un rango pequeño de casilleros mediante una función de hash.
