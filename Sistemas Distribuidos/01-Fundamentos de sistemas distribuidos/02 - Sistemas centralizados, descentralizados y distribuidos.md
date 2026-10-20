---
ramo: "Sistemas Distribuidos"
tema: "Fundamentos de sistemas distribuidos"
tags:
  - sd/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un sistema distribuido]]"
---

# Sistemas centralizados, descentralizados y distribuidos

Si un sistema tiene varios servidores, ¿es distribuido o descentralizado? No hay consenso universal sobre la diferencia, y el curso adopta un criterio concreto. Conocer los enfoques clásicos sirve para entender por qué ese criterio es el elegido y para no confundir la topología de un sistema con su clasificación.

## Tres topologías

![Topologías centralizada, descentralizada y distribuida](adjuntos/Topolog%C3%ADas%20centralizada%2C%20descentralizada%20y%20distribuida.png)

> [!example]- Transcripción de la imagen
> Leyenda: nodos azules son clientes y nodos amarillos son servidores.
> - *Centralized*: un único servidor en el centro con todos los clientes conectados a él.
> - *Decentralized*: tres servidores, cada uno con su grupo de clientes, conectados entre sí.
> - *Distributed*: solo servidores, conectados en malla, sin un centro.

| Topología | Autoridad | Qué pasa si fallan nodos |
|---|---|---|
| **Centralizada** | Un solo jefe | Basta **1 falla** (la del centro) para que caiga todo |
| **Descentralizada** | Varios jefes con sus grupos | Si muere un jefe, muere su grupo completo |
| **Distribuida** | Cualquiera puede ser jefe | Con $N$ nodos, el sistema puede tolerar hasta $N-1$ fallas |

## Enfoques clásicos para distinguirlos

- **Según la autoridad:** en el descentralizado la autoridad se reparte entre varios nodos fijos; en el distribuido, cualquier nodo puede asumirla.
- **Según la robustez:** el descentralizado todavía depende de nodos clave; el distribuido puede eliminar por completo los **puntos únicos de falla**.

Ninguno de los dos es definitivo, porque un sistema distribuido real puede tener distintos tipos de autoridad, repartir algunas responsabilidades y ser más o menos robusto según cómo esté implementado.

![Nodo con autoridad dentro de un sistema distribuido](adjuntos/Nodo%20con%20autoridad%20dentro%20de%20un%20sistema%20distribuido.png)

> [!example]- Transcripción de la imagen
> Una red de servidores (amarillos) con sus clientes (azules), donde uno de los servidores lleva una corona: aunque el sistema sea distribuido, un nodo puede concentrar la autoridad. La clasificación no la decide la forma del grafo.

## El criterio del curso: la necesidad

El libro guía distingue por **el motivo** que llevó a repartir los servidores.

**Descentralizado:** una necesidad externa obliga a tener múltiples servidores repartidos.
- *Administrativa:* el **aprendizaje federado** (*federated learning*), donde cada institución entrena con sus datos privados y solo comparte el modelo.
- *De confianza:* **blockchain**, donde ningún participante confía en un servidor central.
- *Geográfica:* el monitoreo de plantas energéticas ubicadas lejos unas de otras.

![Aprendizaje federado entre hospitales](adjuntos/Aprendizaje%20federado%20entre%20hospitales.png)

> [!example]- Transcripción de la imagen
> Un *Federated Server* con un modelo global intercambia actualizaciones con tres hospitales (*Community Hospital*, *Research Medical Center*, *Cancer Treatment Center*). Cada hospital entrena un modelo local con sus *Private Data*, que nunca salen de la institución (*Privacy Preserving*). Fuente: blog de NVIDIA.

**Distribuido:** una **decisión de diseño** del propio creador, para cumplir requisitos de rendimiento y fiabilidad. Google podría haber centralizado todo en Estados Unidos y ser lento para el resto del mundo; en cambio, decidió repartir data centers y nodos cercanos a los usuarios para reducir la latencia.

![Data centers de Google en el mundo](adjuntos/Data%20centers%20de%20Google%20en%20el%20mundo.png)

> [!example]- Transcripción de la imagen
> Mapa mundial con los data centers de Google marcados: la mayoría en Norteamérica y Europa, algunos en Asia y uno en Sudamérica (Chile).

> [!tip] Diferencia final
> **Descentralizado = necesidad** (algo obliga a repartir y no se puede permitir que si cae uno caiga todo). **Distribuido = decisión de diseño** (se reparte para dar un mejor servicio).

## Consecuencias del criterio

- La autoridad y la robustez dependen de **cómo se orquesta** el sistema, no de su clasificación.
- Un sistema distribuido puede incluir servidores y clientes, y un cliente puede depender de uno o varios servidores.
- Todo lo que se estudia en el ramo aplica por igual a sistemas distribuidos y descentralizados.

## Preguntas de repaso

> [!question]- ¿Por qué el aprendizaje federado se clasifica como descentralizado y no como distribuido?
> Porque los servidores están repartidos por obligación: la privacidad impide juntar los datos de los hospitales en un solo lugar. No es una decisión de diseño para rendir más, sino una necesidad administrativa.

> [!question]- ¿Por qué el criterio de "autoridad" no basta para distinguir los dos tipos?
> Porque un sistema distribuido también puede tener un nodo con más autoridad (por ejemplo, un líder elegido) o repartir responsabilidades entre algunos nodos. La autoridad depende de la implementación, no de la categoría.

> [!question]- En una topología centralizada, ¿cuántas fallas bastan para botar el sistema, y por qué una distribuida tolera más?
> Basta una, la del nodo central. En una distribuida cualquier nodo puede asumir el rol de los demás, así que con $N$ nodos el servicio puede seguir mientras quede al menos uno.
