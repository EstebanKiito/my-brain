---
ramo: "Sistemas Operativos y Redes"
tema: "Algoritmos de ruteo"
tags:
  - sistemas-operativos
  - redes
  - sistemas-autonomos
  - intra-as
  - inter-as
  - bgp
  - ospf
prerrequisitos:
  - "[[Algoritmos de ruteo/02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito|02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito]]"
---

# Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS)

La escala global de Internet hace inviable un enrutamiento plano donde cada enrutador almacene entradas para los cientos de millones de destinos mundiales. Para resolver los desafíos de escalabilidad y autonomía administrativa, Internet se estructura jerárquicamente en **Sistemas Autónomos** (AS, *Autonomous Systems*). Cada AS gestiona su propia red interna mediante protocolos **Intra-AS** y se interconecta con otros sistemas autónomos mediante protocolos **Inter-AS** basados en políticas (BGP).

---

## Estructura jerárquica y enrutamiento interdominio (mis apuntes)

- No es factible almacenar Tablas para todos los Routers de Internet!!!
- Routers pertenecen a distintas organizaciones
- Router pertencientes al mismo dominio administrativo forman un SISTEMA AUTONOMO
Finalmente un conjunto de routers, lo veremos como un conjunto de sistemas autonomos
Cada sistema autonomo, esta administrado por una entidad → Por lo tanto habra un algoritmo Interno LiNK STATE → Es mas facil conseguir la topologia
Routers de salida (de Sistemas autonomos) son GATEWAY ROUTERS
Algoritmos inter-AS ayudan a determinar FORWARDING TABLES entre distintos AS
Algorimtos intra-AS resuelven ruteo interno
28 y 30 Clases de REPASO MIDTERM

> [!tip] Complemento de clase: Protocolos Intra-AS vs Inter-AS
> 1. **Enrutamiento Intra-AS (Interior Gateway Protocols, IGP)**:
>    - Se enfoca en optimizar el rendimiento y costo métrico dentro de una misma organización o ISP.
>    - Ejemplos: **OSPF** (Open Shortest Path First, basado en Link-State) y **RIP** (Routing Information Protocol, basado en Distance-Vector).
> 2. **Enrutamiento Inter-AS (Exterior Gateway Protocols, EGP)**:
>    - Se enfoca en acuerdos comerciales, soberanía administrativa y políticas de tránsito entre organizaciones.
>    - Protocolo estándar de Internet: **BGP** (*Border Gateway Protocol*, RFC 4271), un protocolo de vector de caminos (*Path-Vector*) que intercambia prefijos de red y secuencias completas de números de AS (AS-PATH).

> [!tip] Complemento de clase: Enrutamiento por patata caliente (Hot-Potato Routing)
> Cuando un router en un AS debe enviar tráfico hacia un destino externo accesible por múltiples routers de pasarela (*gateway routers*), la técnica de *Hot-Potato Routing* elige la pasarela interna que tenga el menor costo de transferencia intra-AS, deshaciéndose del paquete lo antes posible fuera de su propia red.

---

## Preguntas de repaso

> [!question]- ¿Por qué el enrutamiento inter-AS se basa en políticas en lugar de buscar únicamente el camino más corto?
> Porque los proveedores de Internet y corporaciones tienen acuerdos comerciales y geopolíticos (relaciones cliente-proveedor o acuerdos de peering) que determinan por qué enlaces están dispuestos a cursar tráfico y si aceptan transportar tráfico de terceros de forma gratuita.

> [!question]- ¿Qué rol cumplen los *Gateway Routers* en un Sistema Autónomo?
> Son los enrutadores situados en el borde perimetral del AS que tienen enlaces físicos directos hacia routers de otros sistemas autónomos, ejecutando sesiones BGP externas (eBGP) para anunciar y recibir prefijos de red.

> [!question]- ¿Cómo evita BGP los bucles de enrutamiento entre sistemas autónomos?
> Al ser un protocolo de vector de caminos (*Path-Vector*), cada anuncio incluye la lista ordenada de números de AS transitados (`AS-PATH`). Si un router recibe un anuncio que ya contiene su propio número de AS en la lista, lo descarta inmediatamente.
