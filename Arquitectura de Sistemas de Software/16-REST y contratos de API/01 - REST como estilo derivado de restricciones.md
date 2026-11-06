---
ramo: "Arquitectura de Sistemas de Software"
tema: "REST y contratos de API"
tags:
  - arquisis/integracion
  - arquisis/rest
  - origen/complemento
prerrequisitos:
  - "[[06 - Tácticas básicas de integración encapsulamiento middleware y estándares]]"
  - "[[01 - Invocación remota y REST]]"
---

# REST como estilo derivado de restricciones

Si dos sistemas tienen que comunicarse, la primera idea es usar los protocolos de la web: petición y respuesta sobre HTTP. Para que eso sea reusable hace falta un estándar común, y ahí aparece **REST**. Casi cualquier sistema que expone algo en la web usa algo de REST, pero REST **no es un formato de API**: es un **estilo arquitectónico** que se obtiene sumando restricciones, cada una con un beneficio y un costo.

## Origen

**REST** (*Representational State Transfer*) fue definido por **Roy Fielding en su tesis del año 2000**. Fielding fue autor principal de HTTP/1.1 (1999) y coautor de la sintaxis de URI (1998). REST es el **conjunto de restricciones arquitectónicas que subyacen a la Web**: explica por qué la web escaló como escaló.

El método de Fielding es el mismo que se usa en todo el curso para diseñar:
1. **Enumerar las propiedades** que se necesitan.
2. **Elegir las restricciones** que producen esas propiedades.
3. **Aceptar lo que cada restricción cuesta.**

Las propiedades que la web debía mantener eran una barrera de entrada baja (para autores, editores y lectores), extensibilidad, hipermedia distribuida, **escalabilidad masiva y anárquica** (nadie controla la web completa) y despliegue independiente de cada parte.

## El árbol de derivación

![Árbol de derivación de REST a partir de estilos más simples](adjuntos/Árbol%20de%20derivación%20de%20REST.png)

> [!example]- Transcripción de la imagen
> - Desde una raíz salen cinco restricciones: *replicated* → **RR**, *separated* → **CS**, *layered* → **LS**, *programmable* → **VM** y *uniform interface* → **U**.
> - RR + *on-demand* → **\$** (caché). CS + *stateless* → **CSS**. CS + LS + *intermediate processing* → **LCS**. VM + *mobile* → **COD**.
> - \$ + CSS (*reliable*, *cacheable*) → **C\$SS**. C\$SS + LCS (*scalable*, *shared*) → **LC\$SS**. LC\$SS + COD (*extensible*) → **LCODC\$SS**.
> - LCODC\$SS + U (*simple*, *visible*, *reusable*, *multi-org*) → **REST**.

Cada nodo es un estilo que hereda las restricciones de sus padres:

| Sigla | Estilo | Restricción que agrega | Qué compra |
|---|---|---|---|
| CS | Cliente-servidor | Separar interfaz de datos | Evolución independiente de cada lado |
| LCS | Cliente-servidor en capas | Intermediarios (proxy, gateway) | Escalabilidad, seguridad, balanceo |
| CSS | Cliente - servidor *stateless* | El servidor no guarda la conversación | Escalabilidad y confiabilidad |
| C\$SS | Cliente con caché - servidor *stateless* | Respuestas marcadas como cacheables | Eficiencia de red y latencia percibida |
| LC\$SS | Cliente con caché en capas - servidor *stateless* | Todo lo anterior, con proxies y gateways (DNS, por ejemplo) | Escala masiva |
| RR / \$ | Repositorio replicado / caché | Copias de los datos cerca del cliente | Disponibilidad y menos tráfico |
| VM / COD | Máquina virtual / **código bajo demanda** | El cliente descarga código y lo ejecuta localmente (JavaScript) | Extensibilidad del cliente |
| LCODC\$SS | En capas, código bajo demanda, cliente con caché - servidor *stateless* | Suma de todo | Extensible y escalable |
| REST | LCODC\$SS + **interfaz uniforme** | Una interfaz genérica entre componentes | Simplicidad, visibilidad y reuso |

![Varios clientes, algunos con caché, frente a un servidor](adjuntos/Cliente%20con%20caché%20frente%20a%20servidor%20stateless.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, tres óvalos de clientes: dos llevan el símbolo **\$** (tienen caché) y el del medio no. Un rótulo dice "Client" y otro "Client + Cache".
> - Todos se conectan a un único **Server**, dibujado como una caja con carpetas (los recursos).

## Propiedades de calidad y qué restricciones las compran

| Propiedad | Qué significa | La compran |
|---|---|---|
| **Network performance** | Throughput, overhead, ancho de banda total y útil | Caché, stateless, mensajes autodescriptivos, capas |
| **Network efficiency** | Minimizar el uso de la red (caché, datos replicados, uso offline) | Igual que la anterior |
| **User-perceived performance** | Latencia que percibe el usuario | Igual que la anterior |
| **Confiabilidad** | Redundancia, sin puntos únicos de falla, monitoreo | Igual que la anterior |
| **Escalabilidad** | Distribuir servicios entre componentes y simplificarlos | Stateless, interfaz uniforme, mensajes autodescriptivos, cliente-servidor, código bajo demanda |
| **Simplicidad** | Separación de responsabilidades | Igual que la anterior |
| **Visibilidad** | Un intermediario puede entender cada interacción | Igual que la anterior |
| **Portabilidad** | Incluye mover código | Igual que la anterior |
| **Modificabilidad** | Evolución, extensibilidad, personalización, configurabilidad y reusabilidad | Cliente-servidor, hipermedia, capas, código bajo demanda, interfaz uniforme |

Dentro de la modificabilidad: **evolución** es cambiar sin afectar al sistema. **Extensibilidad** es añadir funcionalidad con el sistema ya desplegado. **Personalización** es especializar temporalmente un elemento, por ejemplo para un cliente. **Configurabilidad** es modificar componentes después del despliegue.

> [!warning] REST es un estilo, no "APIs que devuelven JSON"
> Como reúne tantas propiedades deseables, REST se considera un **estilo arquitectónico** en sí mismo, igual que capas o cliente-servidor. Una API que devuelve JSON por HTTP pero guarda la sesión en el servidor o ignora los verbos no cumple las restricciones, aunque la llamen "REST".

## Preguntas de repaso

> [!question]- Describa el método con el que Fielding derivó REST.
> Primero enumeró las propiedades que la web necesitaba (escalabilidad masiva, baja barrera de entrada, extensibilidad, despliegue independiente). Luego eligió restricciones que producen esas propiedades (cliente-servidor, stateless, caché, capas, código bajo demanda, interfaz uniforme). Por último aceptó el costo de cada una. Es diseñar arquitectura por tradeoffs.

> [!question]- ¿Qué agrega la restricción stateless y qué cuesta?
> El servidor no guarda el estado de la conversación: cada petición trae todo lo necesario. Compra escalabilidad (cualquier servidor atiende cualquier petición, así que basta agregar réplicas) y confiabilidad (si un servidor cae, no se pierden sesiones). Cuesta más datos por mensaje y que el cliente cargue con el estado de la sesión.

> [!question]- ¿Qué significa la sigla LC\$SS y por qué fue clave para la escala de la web?
> Layered Client-Cached Stateless Server: cliente-servidor sin estado, con caché del lado del cliente y con capas intermedias como proxies y gateways. La caché evita viajes repetidos, el stateless permite replicar servidores y las capas permiten balancear, proteger y cachear en el camino. Con eso la web pudo escalar sin coordinación central.

> [!question]- ¿Qué es "code on demand" y en qué rama del árbol aparece?
> El cliente descarga código del servidor y lo ejecuta localmente, como JavaScript en el navegador. Viene de la rama de máquina virtual (VM → COD). Compra extensibilidad del cliente sin redistribuirlo. Es la única restricción opcional de REST.

> [!question]- V o F: "La interfaz uniforme es lo que distingue a REST de LCODC\$SS".
> Verdadero. Según el árbol de derivación, REST es LCODC\$SS más la interfaz uniforme, que aporta simplicidad, visibilidad y reusabilidad entre organizaciones.

> [!question]- ¿Qué restricciones de REST compran escalabilidad y por qué?
> Stateless (cualquier servidor atiende cualquier petición), interfaz uniforme y mensajes autodescriptivos (los intermediarios pueden cachear y balancear sin conocer la aplicación), cliente-servidor (cada lado escala por separado) y código bajo demanda (traslada trabajo al cliente).

> [!question]- Alternativas: ¿cuál NO es una propiedad que REST busca? a) Visibilidad · b) Escalabilidad masiva y anárquica · c) Consistencia fuerte entre réplicas · d) Despliegue independiente
> c). REST favorece la caché y la replicación, que pueden servir datos desactualizados. La consistencia fuerte no es uno de sus objetivos: prioriza escala, visibilidad y evolución independiente.
