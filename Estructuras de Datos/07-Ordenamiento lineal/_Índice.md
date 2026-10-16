# Ordenamiento lineal — índice

Cómo bajar de $O(n \log n)$ cuando se sabe algo de los datos: ordenar categorizando en vez de comparar, con counting sort, y ordenar por dígitos con radix sort, en sus variantes LSD y MSD.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de ordenación lineal y radix sort (counting sort, estabilidad, LSD, MSD, ejemplo de IPs; 5 imágenes y una animación). Se agregó la cota inferior $\Omega(n \log n)$ para algoritmos por comparación, que es conocimiento general. El código se verificó en Python, y la pasada por unidades coincide con la figura.

## Orden de estudio
1. [[01 - Ordenar sin comparar y counting sort|Ordenar sin comparar y counting sort]]: la cota de los algoritmos por comparación, counting sort, su estabilidad y $\Theta(n + k)$.
2. [[02 - Radix sort LSD y MSD|Radix sort LSD y MSD]]: ordenar por dígitos, por qué hace falta estabilidad, $\Theta(d(n + k))$ y strings de largo variable.

Las imágenes de esta carpeta están en `adjuntos/`.
