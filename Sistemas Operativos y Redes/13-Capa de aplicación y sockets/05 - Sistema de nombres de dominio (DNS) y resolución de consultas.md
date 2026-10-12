---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - dns
  - resolucion-nombres
  - resource-records
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/02 - Concepto de socket e identificación por IP y puerto|02 - Concepto de socket e identificación por IP y puerto]]"
---

# Sistema de nombres de dominio (DNS) y resolución de consultas

El Sistema de Nombres de Dominio (DNS, *Domain Name System*) es una base de datos distribuida y jerárquica que mapea nombres de host mnemónicos legibles por humanos a direcciones IP numéricas utilizadas por los protocolos de red. Opera sobre UDP y TCP en el puerto 53.

---

## Estructura, consultas y registros de DNS (mis apuntes)

### Clase 4
16/10/24

DNS
Sistema que permite Traducir un Dominio con Direcciones

EJ
- Cliente ejecuta PROCESO Cliente DNS
- Browser extrae la URL: [www.google.com](http://www.google.com) y lo pasa al CLIENTE DNS
- Cliente DNS manda QUERY por el dominio [www.google](http://www.google) a SERVIDOR DNS
- Cliente DNS recibe respuesta con la IP del dominio pedido
- Cliente le pasa respuesta al browser
- Cliente HTTP inicia CONEXION TCP a la IP www.google.com

DNS utiliza una estructura de jerarquias y dominios
- Root Servers
- TLD Servers
- Domain Servers → .com .org. edu …

![Jerarquía distribuida del sistema de nombres de dominio DNS](adjuntos/Jerarquía%20distribuida%20del%20sistema%20de%20nombres%20de%20dominio%20DNS.png)

> [!example]- Transcripción de la imagen
> Estructura jerárquica de DNS:
> 1. Servidores Raíz (Root): 13 identidades lógicas distribuidas globalmente mediante Anycast.
> 2. Servidores de Dominio de Nivel Superior (TLD): Gestionan extensiones `.com`, `.org`, `.edu`, `.cl`, etc.
> 3. Servidores Autoritativos: Pertenecen a organizaciones y contienen los registros definitivos de sus dominios.
> 4. Servidor DNS Local (Default Name Server): Proporcionado por el ISP o red local; actúa como proxy de resolución y caché.

Jerarquia:
Servidores DNS, almacenan MAPPINGS
- Lo consulta a un servidor de Mayor jerarquía
- Si no conoce mapping:
- Eventualmente pueden llegar a la RAIZ

Tipos:
- Autoritativos → administran el mapping → POSEEN LAS DIRECCIONES
- No autoritativos → manientienen temporalmente el mapping → TIENEN QUE BUSCARLAS

1. Servidores DNS: Son los encargados de almacenar y proporcionar la información necesaria para la traducción de dominios a direcciones IP.
2. Resolvidores DNS: Son los intermediarios que consultan los servidores DNS en nombre del usuario y devuelven la IP correspondiente.
3. Zonas DNS: Se refieren a divisiones en el espacio de nombres, cada una administrada por un servidor específico.

TIPOS DE CONSULTAS
- Ejemplo el servidor (1,2) de la imagen envían respuesta (completa o parcial) al origen
- Consultas iterativas: retornan la respuesta.

![Resolución iterativa de consultas en el sistema DNS](adjuntos/Resolución%20iterativa%20de%20consultas%20en%20el%20sistema%20DNS.png)

> [!example]- Transcripción de la imagen
> Consulta iterativa: el servidor consultado responde directamente con la mejor respuesta que conoce o con una referencia al siguiente servidor DNS de la jerarquía. El servidor DNS local es el que realiza sucesivamente las peticiones a la raíz, al TLD y al autoritativo.

- Entonces reenvían la consulta.
- Ejemplo (4,6) reenvían la consulta.
- Consulta Recursiva: no tienen la respuesta

![Resolución recursiva de consultas en el sistema DNS](adjuntos/Resolución%20recursiva%20de%20consultas%20en%20el%20sistema%20DNS.png)

> [!example]- Transcripción de la imagen
> Consulta recursiva: el servidor al que se le consulta asume la responsabilidad completa de obtener la respuesta final, delegando la petición en cadena a los servidores superiores y esperando su retorno antes de responder al cliente.

La iterativa no delega completamente el trabajo
La recursiva si, el servidor local espera que llegue la respuesta completa de una lista de servidores
Ej: COMPUTADOR (Cliente) → LocalServer → RootServer → TLD Server → ….

IMPORTANTE
- Algunas veces preferiremos las consultas iterativas por sobre las recursivas
- Los servidores raiz (root), no suelen ser tan consultadas dado que mas abajo, ya hay respuestas cacheadas (en servidores mas abajo en jerarquia)
- Si las respuestas no estan cacheadas - > Se demora el tiempo de respuesta

ARGUMENTOS (Records)

![Registros de recursos DNS Resource Records tipo A NS CNAME y MX](adjuntos/Registros%20de%20recursos%20DNS%20Resource%20Records%20tipo%20A%20NS%20CNAME%20y%20MX.png)

> [!example]- Transcripción de la imagen
> Formato de un Resource Record (RR): `(Name, Value, Type, TTL)`:
> - `Type=A`: Name es nombre de host, Value es dirección IPv4.
> - `Type=NS`: Name es dominio, Value es el nombre de host del servidor de nombres autoritativo.
> - `Type=CNAME`: Name es alias, Value es el nombre canónico real del host.
> - `Type=MX`: Name es dominio, Value es el nombre del servidor de correo asociado (ej. `http://relay1.bar.foo.com`).

LAS RESPUESTAS TIENEN LA SIGUIENTE FORMA
(nombre, valor, tipo, ttl)
- ej: ( relay1.bar.foo.com , 145.37.93.126, A)
- A: Domain → IP :
- ej: ( foo.com, dns.foo.com, NS )
- NS: Sirve para buscar servidor autoritativo
- ej : ( foo.com, relay1.bar.foo.com, CNAME )
- CNAME: Para nombres alias
- MX: para saber a donde va a parar los mail de cierto dominios

![Caché DNS y balanceo de carga entre múltiples servidores](adjuntos/Caché%20DNS%20y%20balanceo%20de%20carga%20entre%20múltiples%20servidores.png)

> [!example]- Transcripción de la imagen
> Mecanismo de caché DNS y balanceo de carga:
> - Una vez que un servidor DNS aprende una correspondencia, la almacena en caché durante el tiempo indicado por el TTL (Time To Live), respondiendo de inmediato a futuras consultas sin acudir a los servidores superiores.
> - Balanceo de carga (DNS Round Robin): cuando un dominio tiene múltiples réplicas con distintas IPs, el servidor devuelve la lista rotada de IPs en cada respuesta.

De pregunta en clases → ¿que pasa cuando tengo mas de un servidor (por la ip)?
Si tiene mas de un servior para hostear pagina web → Probablemente nos conectemos a un solo servidor, y ese nos deriva a otros servidores
Tambien generalmente nos conectamos a un PROXY → servidor mas cercano (con replicas de la info original de la pagina)

---

## Preguntas de repaso

> [!question]- ¿Por qué DNS utiliza primordialmente UDP en lugar de TCP para consultas habituales?
> Por velocidad y baja sobrecarga: las consultas caben en un único datagrama y no requieren el retardo de ida y vuelta (RTT) del *handshake* de conexión de TCP ni conservar estado en el servidor. TCP se reserva para respuestas que superan los 512 bytes o para transferencias de zona entre servidores.

> [!question]- ¿Cuál es la diferencia entre una consulta DNS iterativa y una recursiva?
> En la consulta recursiva, la entidad consultada asume la carga de resolver todo el nombre hasta devolver la IP definitiva. En la iterativa, si el servidor no conoce el registro final, devuelve la dirección del siguiente servidor en la jerarquía para que el cliente continúe la búsqueda por sí mismo.

> [!question]- ¿Qué función cumple el campo TTL (*Time-To-Live*) en un registro de recurso DNS?
> Especifica el número de segundos durante los cuales los servidores intermedios y resolvidores pueden almacenar el registro en caché local antes de considerarlo expirado y consultar nuevamente al servidor autoritativo.

