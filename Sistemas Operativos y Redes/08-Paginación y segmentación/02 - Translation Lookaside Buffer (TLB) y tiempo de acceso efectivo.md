---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/tlb
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de paginación, marcos y tabla de páginas]]"
---

# Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo

Con [[01 - Fundamentos de paginación, marcos y tabla de páginas|paginación]], cada acceso a memoria se vuelve dos: uno para leer la tabla de páginas y otro para el dato. La solución es guardar las traducciones recientes en una memoria muy rápida dentro de la MMU, la **TLB**, para no tener que ir a la tabla cada vez.

## Qué es la TLB

La **TLB** (*Translation Lookaside Buffer*) es una **caché totalmente asociativa** (*fully associative*) de traducciones, dentro de la MMU:

- Guarda traducciones **VPN → PFN**.
- Está en la CPU, no en la memoria principal, así que consultarla es muchísimo más rápido.
- **TLB hit**: la traducción está en la caché y se responde directamente.
- **TLB miss**: la traducción no está, así que se lee la tabla de páginas desde memoria y se **actualiza la TLB**.

![Arquitectura de TLB y flujo de aciertos y fallos](adjuntos/Arquitectura%20de%20TLB%20y%20flujo%20de%20aciertos%20y%20fallos.png)

> [!example]- Transcripción de la imagen
> La CPU emite una *logical address* `p | d`. El número de página `p` se compara a la vez con todas las entradas de la **TLB** (*page number / frame number*). En un **TLB hit**, la TLB entrega `f` directamente. En un **TLB miss** (flecha roja a mano), se consulta la *page table* con `p` para obtener `f`. En ambos casos la *physical address* es `f | d`, que va a la *physical memory*.

Un miss cuesta un poco **más** que no tener TLB, porque además de la tabla y el dato se perdió tiempo buscando en la TLB. Pero ese extra es pequeño, porque la TLB es muy rápida, y cada hit **se ahorra el acceso a la tabla**.

## Ejemplo: recorrer un arreglo

```c
int sum = 0;
for (i = 0; i < 10; i++) {
    sum += a[i];
}
```

Con un espacio virtual de 8 bits y páginas de 16 B (4 bits de offset, 4 de página, 16 páginas), y un arreglo de 10 `int` de 4 B, la memoria queda así: `sum`, `a[0]`, `a[1]` y `a[2]` llenan los primeros 16 B (una página); `a[3]` a `a[6]` caen en la siguiente; y `a[7]` a `a[9]` en la tercera.

![Distribución de un arreglo en páginas virtuales](adjuntos/Distribuci%C3%B3n%20de%20un%20arreglo%20en%20p%C3%A1ginas%20virtuales.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano de la memoria del programa: `sum = 0`, `a[0]`, `a[1]` y `a[2]` en la primera página (flechas sobre `a[0]`, `a[1]` y `a[2]`); una línea roja separa `a[3]` a `a[6]` (segunda página) y otra separa `a[7]` a `a[9]` (tercera página).

![Cálculo de tasa de aciertos de TLB en bucle secuencial](adjuntos/C%C3%A1lculo%20de%20tasa%20de%20aciertos%20de%20TLB%20en%20bucle%20secuencial.png)

> [!example]- Transcripción de la imagen
> El mismo dibujo con anotaciones: `a[0]` **Miss**, `a[1]` **Hit**, `a[2]` **Hit**; `a[3]` **Miss** y luego **Hit × 3**; `a[7]` **Miss** y luego **Hit × 2**.

Contando solo los accesos a `a`:

| | Accesos a memoria | Detalle |
|---|---|---|
| Sin TLB | **20** | 10 × (tabla de páginas + `a[i]`) |
| Con TLB | **13** | miss, hit, hit, miss, hit, hit, hit, miss, hit, hit: 10 a `a[i]` + 3 a la tabla |

Cada vez que se accede por primera vez a una página es un miss, y los siguientes accesos a esa página ya están en la TLB y son hits. Resultado: **3 misses y 7 hits, 70% de TLB hit rate** (7 de 10 accesos a la tabla ahorrados). **Con páginas más grandes, el hit rate aumenta**: con páginas de 32 B solo habría 2 misses (80%).

## ¿Es bueno un 70%? Tiempo de acceso promedio

Con un acceso a memoria física de ≈100 ns y uno a TLB de 1 ns:

- **TLB hit** ≈ 1 + 100 = **101 ns** (TLB + dato);
- **TLB miss** ≈ 1 + 100 + 100 = **201 ns** (TLB + tabla + dato).

$$T_{\text{promedio}} = T_{\text{hit}} \cdot \text{hit rate} + T_{\text{miss}} \cdot (1 - \text{hit rate}) = 101 \cdot 0{,}7 + 201 \cdot 0{,}3 = 131 \text{ ns}$$

Este promedio también se llama **tiempo de acceso efectivo** (EAT, *effective access time*). Con un hit rate realista de 99%, queda en $101 \cdot 0{,}99 + 201 \cdot 0{,}01 = 102$ ns, casi lo mismo que un acceso sin paginación.

En el ejemplo, sin TLB son 20 accesos (2000 ns); con TLB, 13 accesos a memoria y 10 a la TLB (1310 ns): **≈1,52 veces más rápido**. Funciona tan bien porque los programas suelen acceder a direcciones cercanas y repetidas, lo que se llama [[03 - Localidad de referencia y gestión de TLB con ASID en cambios de contexto|localidad de referencia]].

```python
def accesos_tlb(tam_pagina, n=10, base=4, tam_int=4):
    """a[i] está en la dirección base + 4*i (sum ocupa los bytes 0-3)."""
    tlb, resultado = set(), []
    for i in range(n):
        pagina = (base + tam_int * i) // tam_pagina
        resultado.append("hit" if pagina in tlb else "miss")
        tlb.add(pagina)                       # tras un miss, la PTE queda en la TLB
    return resultado

print(accesos_tlb(16))   # miss, hit, hit, miss, hit, hit, hit, miss, hit, hit -> 70%
print(accesos_tlb(32))   # 2 misses -> 80%
```

## Preguntas de repaso

> [!question]- ¿Qué pasa en un TLB hit y en un TLB miss?
> En un hit, la TLB entrega el PFN y se accede directo al dato: un acceso a memoria. En un miss, se lee la PTE en la tabla de páginas, se guarda en la TLB y luego se accede al dato: dos accesos.

> [!question]- ¿Por qué en el ejemplo del arreglo hay 3 misses?
> Porque los 10 elementos ocupan 3 páginas, y solo el primer acceso a cada página falla. Los siguientes accesos a la misma página encuentran la traducción en la TLB.

> [!question]- Calcula el tiempo promedio con hit rate de 70%, hit de 101 ns y miss de 201 ns.
> $101 \cdot 0{,}7 + 201 \cdot 0{,}3 = 70{,}7 + 60{,}3 = 131$ ns.

> [!question]- ¿Por qué páginas más grandes aumentan el hit rate?
> Porque caben más datos consecutivos en cada página, así que el miss inicial de cada página se reparte entre más accesos que después son hits.
