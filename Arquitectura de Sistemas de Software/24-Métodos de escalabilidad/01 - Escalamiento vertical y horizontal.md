---
ramo: "Arquitectura de Sistemas de Software"
tema: "Métodos de escalabilidad"
tags:
  - arquisis/escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[03 - Leyes de Little Amdahl y Gustafson]]"
---

# Escalamiento vertical y horizontal

Una vez medido el problema, hay tres familias de soluciones: **agregar recursos** (métodos dimensionales), **diseñar el sistema para crecer** (modelación de sistemas) y **organizar los datos para crecer** (métodos en datos). Esta nota cubre la primera, que es la más directa y la que más trampas tiene en las pruebas.

## Las tres familias

| Método | Descripción |
|---|---|
| **Dimensionales** | Añadir recursos (servidores, discos, memoria) para manejar cargas mayores sin reducir el rendimiento ni la disponibilidad |
| **Modelación de sistemas** | Diseñar una arquitectura modular y flexible que se adapte a cambios en la demanda, usando patrones y prácticas que permitan expandirla y mantenerla fácilmente |
| **Estructuras y bases de datos** | Diseñar el almacenamiento para manejar grandes volúmenes: partición de datos, replicación, asignación dinámica de recursos, índices y optimización de consultas |

## Vertical y horizontal

- **Vertical (*scale up*):** mejorar las características de los computadores existentes: más CPU, RAM o disco.
- **Horizontal (*scale out*):** añadir más instancias de cómputo (máquinas físicas, máquinas virtuales o peers) y **mejorar la red**, tanto en ancho de banda como en latencia (Ethernet 10GbE, InfiniBand hasta 600 Gb/s, Myrinet).

| | Vertical | Horizontal |
|---|---|---|
| Cambio en la arquitectura | Ninguno | Necesita servicios sin estado y coordinación |
| Techo | Físico y de costo | Prácticamente ninguno |
| Redundancia | No: sigue siendo un solo nodo | Sí: si cae uno, siguen los otros |
| Costo de crecer | Crece más que linealmente en las máquinas grandes | Lineal, con hardware *commodity* |
| Complejidad | Baja | Alta: balanceo, concurrencia, consistencia |

### Lo que exige el escalamiento horizontal

![Responsabilidades del balanceo de carga: API Gateway, load balancer, servidores y CDN](adjuntos/Responsabilidades%20del%20balanceo%20de%20carga.png)

> [!example]- Transcripción de la imagen
> - Título **LOAD BALANCING**, con cuatro piezas.
> - **API Gateway:** validación de entradas, autenticación y autorización, rate limiting y throttling, listas blancas y negras, control de flujo, OAuth 2.0, terminación TLS, deduplicación de peticiones, medición de uso y despacho de peticiones.
> - **Load Balancer** (#MultiPrimary): algoritmos round robin, round robin ponderado, menos conexiones e IP hash; lleva registro de logs, códigos de estado, número de peticiones y conexiones activas.
> - **Frontend Servers** (#InMemoryConnections, para streaming y chat en vivo).
> - **CDN / Edge Servers** (#Global, #Regional, #Static): contenido estático y streaming.

![Balanceador de aplicaciones de AWS con grupos blue y green en dos zonas de disponibilidad](adjuntos/Balanceador%20de%20AWS%20con%20grupos%20blue%20y%20green%20en%20dos%20zonas.png)

> [!example]- Transcripción de la imagen
> - Usuarios (computador y celular) entran a la **AWS Cloud**, dentro de una **VPC**.
> - Un **Application Load Balancer** reparte el tráfico entre instancias en **Availability Zone 1** y **Availability Zone 2**.
> - Las instancias forman dos grupos: **Blue Target Group** y **Green Target Group** (uno con la versión actual y otro con la nueva).

El balanceador reparte la carga entre réplicas en zonas distintas, lo que da escalabilidad y también disponibilidad. Los dos grupos permiten despliegues *blue/green*: se prepara la versión nueva en el grupo verde y se cambia el tráfico de golpe. En Kubernetes, un **Service** cumple ese mismo rol de balanceador delante de los **pods** de cada nodo.

## Consideraciones

- **Vertical: no siempre añade performance.** Si el cuello de botella es un lock, la red o un algoritmo, una máquina más grande no ayuda.
- **Horizontal:**
  - **requiere intermediarios de coordinación**: load balancers, NATs y redes;
  - **añade complejidad**: asincronía, concurrencia y paralelismo;
  - **añade latencia por la distribución**, sobre todo en SOA y microservicios;
  - sufre la **ley de los retornos decrecientes**: por Amdahl, cada servidor extra aporta menos que el anterior.

> [!warning] Escalar horizontalmente un servicio con estado
> Si la sesión del usuario vive en la memoria de una instancia, el balanceador debe mandar siempre a ese usuario a la misma instancia (*sticky sessions*), y si la instancia cae, se pierde la sesión. Para escalar horizontalmente, el estado se saca a un almacén compartido (Redis, la base de datos) o al cliente (un token): es la restricción stateless de REST.

## Preguntas de repaso

> [!question]- Nombre las tres familias de métodos de escalabilidad.
> Métodos dimensionales (agregar recursos), métodos de modelación de sistemas (diseñar componentes, conectores y configuraciones para crecer) y métodos en datos (particionar, replicar, cachear, indexar).

> [!question]- Compare escalar vertical y horizontalmente en techo, redundancia y complejidad.
> Vertical: tiene un techo físico y de costo, no da redundancia (sigue siendo un nodo) y es simple. Horizontal: casi no tiene techo, da redundancia porque hay varias réplicas, y es complejo porque requiere balanceo, servicios sin estado y coordinación.

> [!question]- ¿Por qué el escalamiento horizontal tiene "retornos decrecientes"?
> Porque la parte secuencial del trabajo y la coordinación entre nodos no se reparten (Amdahl). Cada servidor extra acelera menos que el anterior, y en algún punto el costo de coordinar supera la ganancia.

> [!question]- ¿Qué hace un load balancer y qué algoritmos de reparto usa?
> Reparte las peticiones entre varias réplicas para que ninguna se sature, y saca de la rotación a las que fallan. Algoritmos típicos: round robin, round robin ponderado, menos conexiones e IP hash.

> [!question]- ¿Por qué un servicio con sesión en memoria es difícil de escalar horizontalmente y cómo se corrige?
> Porque cada usuario queda atado a la instancia que tiene su sesión: se necesitan sticky sessions, la carga se reparte mal y si esa instancia cae se pierde la sesión. Se corrige sacando el estado a un almacén compartido o a un token del cliente, para que cualquier réplica pueda atender cualquier petición.

> [!question]- V o F: "Escalar verticalmente siempre mejora la performance".
> Falso. Si el cuello de botella es un lock, la red, una dependencia externa o un mal algoritmo, más CPU o RAM no lo resuelve. Hay que medir dónde está el cuello antes de escalar.

> [!question]- ¿Qué aporta tener instancias en dos zonas de disponibilidad detrás de un balanceador?
> Escalabilidad, porque hay más instancias para repartir la carga, y disponibilidad, porque si falla una zona completa el balanceador envía el tráfico a la otra.
