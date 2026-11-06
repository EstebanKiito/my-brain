---
ramo: "Arquitectura de Sistemas de Software"
tema: "gRPC GraphQL y MCP"
tags:
  - arquisis/integracion
  - arquisis/graphql
  - origen/complemento
prerrequisitos:
  - "[[05 - OpenAPI y límites de REST]]"
---

# GraphQL y consultas definidas por el cliente

En REST, el **servidor** decide qué trae cada endpoint. Si una pantalla necesita dos campos de un recurso, recibe todos. Si necesita datos de tres recursos, hace tres peticiones. **GraphQL** invierte la responsabilidad: es un **lenguaje de consultas para APIs** en el que **el cliente define exactamente qué datos quiere**, en una sola llamada y a un único endpoint.

## Origen y problemas que ataca

GraphQL fue creado en Facebook en 2015 y está en la GraphQL Foundation desde 2019. Nace para prevenir problemas comunes de REST y SOAP:
- **Overfetching:** recibir más datos de los que se necesitan.
- **Underfetching:** no recibir todo lo necesario en una petición y tener que hacer más.
- **Exceso de peticiones** para armar una sola vista.
- **Exceso de endpoints**: uno por cada combinación de datos que pide alguna pantalla.

## El schema: el contrato

El **schema** define **todas las interacciones de datos posibles** con el servidor, igual que el contrato entre un ORM y la base de datos. Básicamente es un contrato tipado, y es **federable**: varios servicios pueden aportar partes de un schema unificado. Tiene tres tipos de operaciones:
- **Queries:** lecturas.
- **Mutaciones:** escrituras.
- **Suscripciones:** el servidor empuja datos cuando cambian, lo que sirve para aplicaciones en tiempo real.

```graphql
query {
  continents {
    code
    name
    countries {
      name
      capital
      languages { name native }
    }
  }
}
```

Con **una sola llamada a un único endpoint**, el cliente obtiene continentes, sus países, las capitales y los idiomas, solo con los campos pedidos. También podría filtrar por continente o pedir solo los nombres. En REST serían varios endpoints y varias peticiones, o una respuesta enorme.

En un diagrama de componentes, GraphQL se ve igual que REST o gRPC: un servidor que provee una interfaz y un cliente que la requiere. La diferencia está en el flujo: el cliente envía la forma de la respuesta que quiere y, con suscripciones, el servidor también puede enviar datos sin que se los pidan.

## Pros y contras

| Pros | Contras |
|---|---|
| **Fetching mejorado**: un solo endpoint, normalmente una o dos peticiones por vista | **Mayor costo de desarrollo** para definir los schemas, aunque después se paga bien |
| **Suscripciones** para aplicaciones en tiempo real | **Curva de aprendizaje** |
| **Mejor experiencia de desarrollo en el frontend** | **Caché poco intuitiva**: todo va por `POST` a un endpoint, así que se pierde el apoyo de la caché HTTP |
| **Tipado** | **Difícil de optimizar**: el cliente puede pedir cualquier combinación, y la performance depende de la capacidad del servidor |
| | Clientes mal configurados o maliciosos pueden pedir datos muy complejos y extensos en una sola petición |

En resumen: para el frontend es excelente, para el backend es más difícil.

> [!warning] Seguridad: un endpoint que expone todo el grafo
> Si el endpoint de GraphQL queda accesible sin autenticación ni autorización por campo, se expone **toda la data** del schema, porque el cliente puede explorar y pedir cualquier relación. Además, una consulta profundamente anidada puede funcionar como denegación de servicio. Se mitiga con autenticación, autorización por campo, límites de profundidad y costo de las consultas, y consultas persistidas (*persisted queries*).

## Cuándo elegirlo

- Un **frontend** (web o móvil) arma vistas con datos de muchos recursos y cambia seguido.
- Hay **muchos clientes con necesidades distintas** (app, web, partners) sobre los mismos datos.
- Se necesitan **actualizaciones en tiempo real** hacia la interfaz (suscripciones).

No conviene para comunicación entre servicios de alta velocidad (ahí va gRPC) ni para APIs públicas simples que se benefician de la caché HTTP (ahí va REST).

## Preguntas de repaso

> [!question]- ¿Qué invierte GraphQL respecto de REST?
> Quién define la forma de la respuesta. En REST, el servidor fija qué devuelve cada endpoint. En GraphQL, el cliente envía una consulta con exactamente los campos y las relaciones que necesita, a un único endpoint.

> [!question]- Nombre los tres tipos de operaciones de un schema GraphQL y para qué sirve cada uno.
> Queries para leer, mutaciones para escribir y suscripciones para que el servidor empuje cambios en tiempo real al cliente.

> [!question]- ¿Por qué la caché es más difícil en GraphQL que en REST?
> En REST, cada recurso tiene su URI y los `GET` son cacheables por navegadores, proxies y CDN. En GraphQL todas las consultas van normalmente por `POST` a un mismo endpoint, con cuerpos distintos, así que se pierde la caché HTTP estándar y hay que cachear en la aplicación.

> [!question]- ¿Por qué GraphQL es "difícil de optimizar" del lado del servidor?
> Porque el cliente puede pedir cualquier combinación de campos y relaciones. El servidor no conoce de antemano las consultas, así que pueden aparecer consultas anidadas que disparan muchas lecturas a la base de datos (el problema N+1), y la performance depende de cómo se resuelva cada campo.

> [!question]- Mini caso: una app móvil con mala conexión hace 6 peticiones REST para mostrar el perfil de un usuario. ¿Qué propone?
> GraphQL: una sola consulta trae el usuario, sus pedidos y sus direcciones con solo los campos necesarios. Así bajan el número de viajes y los bytes transferidos, que es lo que más pesa con mala conexión. Hay que mencionar el costo de definir el schema y de proteger el endpoint (autorización y límites de profundidad).

> [!question]- V o F: "GraphQL solo permite operaciones de lectura".
> Falso. Tiene mutaciones para escribir y suscripciones para recibir cambios en tiempo real, además de las queries de lectura.

> [!question]- ¿Qué riesgo de seguridad específico tiene GraphQL y cómo se mitiga?
> Un endpoint sin autenticación ni autorización por campo expone todo el grafo de datos, y las consultas muy anidadas pueden saturar el servidor. Se mitiga con autenticación, autorización por campo, límites de profundidad y de costo, y consultas persistidas.
