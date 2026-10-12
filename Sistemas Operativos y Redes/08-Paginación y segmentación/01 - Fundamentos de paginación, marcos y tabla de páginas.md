---
ramo: "Sistemas Operativos y Redes"
tema: "Paginación y segmentación"
tags:
  - so/memoria
  - so/paginacion
  - origen/complemento
prerrequisitos:
  - "[[03 - Relocalización, protección de memoria y registros base y límite]]"
  - "[[05 - Segmentación de memoria y prevención de segmentation fault]]"
---

# Fundamentos de paginación, marcos y tabla de páginas

La [[05 - Segmentación de memoria y prevención de segmentation fault|segmentación]] reduce el problema de los huecos, pero los segmentos siguen teniendo tamaños distintos y la fragmentación externa no desaparece. La **paginación** es otra estrategia para ubicar la memoria: corta todo en trozos **del mismo tamaño**, de modo que cualquier trozo libre sirve para cualquier pedazo de cualquier proceso.

## Páginas y marcos

- La memoria **física** se divide en **marcos** (*frames*).
- La memoria **virtual** de cada proceso se divide en **páginas**.
- **Página y marco tienen el mismo tamaño**: $|\text{página}| = |\text{frame}|$.

Cualquier página puede ir en cualquier marco libre, sin necesidad de que las páginas de un proceso queden contiguas. Como todos los marcos son iguales, no hay fragmentación externa.

Para saber dónde quedó cada página hace falta información extra: la **tabla de páginas**, una por proceso, que guarda la traducción de **número de página a número de frame**, es decir, en qué frame está guardada cada página del proceso.

## Ejemplo: 64 bytes virtuales, 128 físicos

![División de memoria virtual en páginas y memoria física en marcos](adjuntos/Divisi%C3%B3n%20de%20memoria%20virtual%20en%20p%C3%A1ginas%20y%20memoria%20f%C3%ADsica%20en%20marcos.png)

> [!example]- Transcripción de la imagen
> A la izquierda, el **Espacio virtual** de 0 a 64 con 4 páginas de 16 (*page 0 of the address space*, *page 1*, *page 2*, *page 3*). A la derecha, el **Espacio Físico** de 0 a 128 con **8 frames** de 16: frame 0 *reserved for OS*, frame 1 *unused*, frame 2 *page 3 of AS*, frame 3 *page 0 of AS*, frame 4 *unused*, frame 5 *page 2 of AS*, frame 6 *unused* y frame 7 *page 1 of AS*. Líneas de colores unen cada página con su frame, y una **X** a mano marca el mismo desplazamiento dentro de la página 2 y dentro del frame 5.

| | Espacio virtual | Espacio físico |
|---|---|---|
| Tamaño | 64 B $= 2^6$ → **6 bits** de dirección | 128 B $= 2^7$ → **7 bits** |
| Offset (página o frame de 16 B $= 2^4$) | **4 bits** | **4 bits** |
| Número de página o frame | $64/16 = 4 = 2^2$ → **2 bits de VPN** | $128/16 = 8 = 2^3$ → **3 bits de PFN** |
| Formato | `b5 b4` = VPN · `b3 b2 b1 b0` = offset | `b6 b5 b4` = PFN · `b3 b2 b1 b0` = offset |

VPN es el *virtual page number* y PFN el *physical frame number*. La tabla de páginas de este proceso:

![Traducción de VPN a PFN preservando el offset](adjuntos/Traducci%C3%B3n%20de%20VPN%20a%20PFN%20preservando%20el%20offset.png)

> [!example]- Transcripción de la imagen
> Tabla *Page (VPN) / Frame (PFN)*: 0 (`0b00`) → 3 (`0b011`); 1 (`0b01`) → 7 (`0b111`); 2 (`0b10`) → 5 (`0b101`); 3 (`0b11`) → 2 (`0b010`).

## Cómo se traduce

> [!tip] Regla de traducción
> **Se conserva el offset y se cambia el VPN por el PFN.** Esta traducción la hace la MMU en cada acceso. Como página y frame miden lo mismo, el byte $k$ de una página está en el byte $k$ del frame donde quedó.

![Estructura de la entrada de tabla de páginas y metadatos](adjuntos/Estructura%20de%20la%20entrada%20de%20tabla%20de%20p%C3%A1ginas%20y%20metadatos.png)

> [!example]- Transcripción de la imagen
> *Virtual Address* `0 1 | 0 1 0 1` (VPN | offset). Los bits del VPN entran a *Address Translation*, que produce el PFN `1 1 1`; los 4 bits del offset bajan sin cambios. *Physical Address* `1 1 1 | 0 1 0 1` (PFN | offset).

La dirección virtual 21 = `01 0101` está en la página 1 con offset 5. La página 1 está en el frame 7, así que la física es `111 0101` = 117.

![Duplicación de accesos a memoria por consulta a tabla de páginas](adjuntos/Duplicaci%C3%B3n%20de%20accesos%20a%20memoria%20por%20consulta%20a%20tabla%20de%20p%C3%A1ginas.png)

> [!example]- Transcripción de la imagen
> Hardware de paginación: la CPU emite una *logical address* `p | d`. Con `p` se indexa la *page table*, que entrega `f`. La *physical address* es `f | d`, que apunta dentro del frame `f` de la *physical memory* (direcciones `f0000…0000` a `f1111…1111`).

```python
OFFSET_BITS = 4                       # páginas de 16 bytes
TABLA = {0: 3, 1: 7, 2: 5, 3: 2}      # VPN -> PFN

def traducir(virtual):
    vpn = virtual >> OFFSET_BITS                   # bits altos: número de página
    offset = virtual & ((1 << OFFSET_BITS) - 1)    # bits bajos: se conservan
    pfn = TABLA[vpn]
    fisica = (pfn << OFFSET_BITS) | offset         # cambiar VPN por PFN
    return fisica

print(traducir(21))   # 117
```

## Qué guarda cada entrada

Además de la traducción, la tabla guarda **metadatos**, que dependen de cada SO:

- **Bit de validez**: si la entrada es válida, es decir, si la página fue asignada al proceso. Si la MMU encuentra una entrada inválida, genera una excepción y el SO envía `SIGSEGV`;
- **Bit de presencia**: si la página está en memoria principal o en la secundaria (swap);
- **Bit de escritura**: si la página se puede escribir.

Cada entrada es una **PTE** (*page table entry*): $\text{PTE} = \text{PFN} + \text{metadatos}$, y el tamaño de la tabla es $|\text{tabla}| = |\text{PTE}| \times \text{número de páginas}$. Como la tabla vive en la memoria principal, ocupa una cantidad significativa de ella, y hay que tratar de reducirla (ver [[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna|sobrecarga de las tablas]]).

> [!warning] Cada acceso a memoria se duplica
> Para leer una variable, primero hay que leer la tabla de páginas en memoria para traducir, y recién después ir a buscar el dato: **dos accesos en vez de uno**, lo que casi duplica el tiempo de acceso. La solución es la [[02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo|TLB]].

## Preguntas de repaso

> [!question]- ¿Cuál es la regla para traducir una dirección virtual a física con paginación?
> Se conserva el offset y se reemplaza el VPN por el PFN que indica la tabla de páginas.

> [!question]- Con 64 B virtuales, 128 B físicos y páginas de 16 B, ¿cuántos bits tienen el VPN, el PFN y el offset?
> El offset tiene 4 bits ($16 = 2^4$), el VPN 2 bits (4 páginas) y el PFN 3 bits (8 frames). La dirección virtual tiene 6 bits y la física 7.

> [!question]- ¿Qué indican los bits de validez y de presencia de una PTE?
> El de validez indica si la página fue asignada al proceso. El de presencia indica si la página está en RAM o en el disco (swap).

> [!question]- ¿Por qué la paginación pura duplica el costo de cada acceso a memoria?
> Porque antes de leer el dato hay que leer la PTE en la tabla de páginas, que también está en memoria. Son dos accesos por cada uno que pide el programa.

> [!question]- Con páginas de 4 KB y direcciones virtuales de 32 bits, ¿cuántos bits son de offset y cuántos de VPN?
> $4\text{ KB} = 2^{12}$, así que el offset tiene 12 bits y el VPN los $32 - 12 = 20$ restantes.
