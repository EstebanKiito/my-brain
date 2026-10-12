---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - dhcp
  - nat
  - upnp
  - redes-locales
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR|03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR]]"
---

# Configuración dinámica con DHCP y traducción de direcciones NAT

La incorporación automática de dispositivos a una red local y la mitigación de la escasez de direcciones IPv4 descansan en dos tecnologías clave de borde: **DHCP** (*Dynamic Host Configuration Protocol*), que asigna dinámicamente direcciones IP, máscaras, gateways y servidores DNS a nuevos clientes, y **NAT** (*Network Address Translation* / NAPT), que traduce múltiples direcciones privadas hacia una única IP pública modificando cabeceras de red y puertos de transporte.

---

## DHCP y Traducción NAT (mis apuntes)

DHCP : DYNAMIC HOST CONFIG PROTOCOL
DHCP es un protocolo plug and play, que nos configura nuestra IP
Cuando detecta que alguien se contecta, le entrega los parametros para la conexion

4 Etapas del protocolo
- Destino → 255.255.255.255:
- Cuando el cliente llega (enchufa a la red) → Cliente DHCP discover message
- Destino → 255.255.255.255 : Sigue siendo braodcast (le llega a todos)
- El Servidor Responde: DHCP offer Message
- Cliente envía un DHCP Request Message
- Server envía DHCP ACK Message

![Flujo de cuatro pasos del protocolo DHCP: Discover, Offer, Request y ACK](adjuntos/Flujo%20de%20cuatro%20pasos%20del%20protocolo%20DHCP:%20Discover,%20Offer,%20Request%20y%20ACK.png)

> [!example]- Transcripción de la imagen
> El intercambio DORA de DHCP (puerto UDP 67 servidor, 68 cliente):
> 1. **Discover**: Cliente sin IP envía broadcast `255.255.255.255` con `src 0.0.0.0`.
> 2. **Offer**: Servidor DHCP reserva una IP y envía broadcast ofreciendo la IP, máscara, lease time y gateway.
> 3. **Request**: Cliente confirma la elección de la IP ofrecida mediante broadcast.
> 4. **ACK**: Servidor confirma definitivamente la asignación de la dirección IP.

NAT
Network Addres Translation
ISP provee ctd limitada de IPs, y aveces solo una por Casas o oficinas que formen una LAN
- Esto es posible gracias a que la NAT utiliza direcciones IP privadas de forma interna en la red doméstica.
- 1 Direccion Publica
- Varias Direcciones Internas → Usando NAT
- Resumen:
NAT: Es una tecnología que permite que varios dispositivos se conecten a Internet usando 1 sola dirección IP pública.

![Arquitectura de traducción de direcciones de red NAT en red local](adjuntos/Arquitectura%20de%20traducción%20de%20direcciones%20de%20red%20NAT%20en%20red%20local.png)

> [!example]- Transcripción de la imagen
> Funcionamiento del router NAT: Todo el tráfico que sale de la red local (10.0.0.0/24 o 192.168.1.0/24) se reescribe con la única dirección IP pública asignada por el ISP, diferenciando las conexiones mediante números de puerto asignados dinámicamente.

EJEMPLO DE USO COTIDIANO
- La ip destino no vive dentro de la Misma Subred
- Gateway : Puerta de enlace
- Consecuencia: Comunicarse con el ROUTER (gateway)
- Mi ip interna es 192.168.1.86 y por el puerto 8120 me quiero conectar a Youtube.com, lo hare con ip destinatario: 64.233.186.90 por el puerto 443(https),
El router que implementa NAT: va a recibir el paquete, cuando reciba eso, va a ver, que alguien interno quiere conectarse a alguien externo
El Router lo que hace será : CAMBIAR EL PAQUETE (header)
- Para cambiarle la direccion de Origen, ya no sera 192.168.1.86, si no sera que la que proveyo el ISP ej: 138.76.29.7 por el puerto 6010
- Luego va el paquete al servidor, se devuelve con origen 64.233.186.90 puerto 443, hacia el destino 128.76.29.7 puerto 6010
- Y el PROPIO ROUTER NAT, traduce a quien le llega el paquete → Que es 192.168.1.86

![Tabla de traducción NAT con puertos y direcciones IP públicas y privadas](adjuntos/Tabla%20de%20traducción%20NAT%20con%20puertos%20y%20direcciones%20IP%20públicas%20y%20privadas.png)

> [!example]- Transcripción de la imagen
> Tabla de traducción NAT: Mapea tuplas `(IP privada, Puerto privado)` $\leftrightarrow$ `(IP pública NAT, Puerto público NAT)`. Al recibir una respuesta externa, consulta la tabla para revertir la traducción y reenviar el datagrama al host interno.

Eso desde el lado del cliente → COMO FUNCIONA PARA UN SERVIDOR?
Conectar un Servicio detras de NAT
El Cliente no sabe con quien contactarse (es una IP PRIVADA)
El Cliente para conectarse al servidor, tiene que conectarse con la direccion del Router
El Router del servidor debe tener un protocolo llamado: UPNP (Universal plug-play)
- Esto le permite que los serviodres se registren dentro del ROUTER NAT

![Traversal de NAT y reenvío de puertos mediante UPnP para servidores internos](adjuntos/Traversal%20de%20NAT%20y%20reenvío%20de%20puertos%20mediante%20UPnP%20para%20servidores%20internos.png)

> [!example]- Transcripción de la imagen
> Apertura y reenvío de puertos (*Port Forwarding* y UPnP): Permite a un host interno solicitar al router NAT la creación estática o automática de una entrada en la tabla para recibir conexiones entrantes desde el exterior en un puerto específico.

El Router poseera el registro de que puertos dirigen a que direcciones
- Se registra a travez de un PUERTO
Los Clientes deben conocer esto → El servidor debe anunciarse, o en algun DNS , para que el Cliente sepa a que puerto debe conectarse!

ANTI NATS
NAT tiene distractores, dado que Viola el principio de Extremo-Extremo
- Son de CAPA DE TRANSPORTE!!!
- Router son de Capa 3 → NAT requiere que modifiquen puertos, y Puertos no son de capa 3
- Comunicacion Sin Modificacion Intermedia
- NAT es un parche, con ipv6 ya nunca deberiamos necesitar NAT

> [!warning] Posible error en apuntes: "distractores" de NAT y errata en IP
> En los apuntes se menciona "NAT tiene distractores"; la palabra adecuada es **detractores**. Asimismo, en el flujo de retorno se menciona la IP 128.76.29.7 como destino, cuando la IP pública original del ejemplo era 138.76.29.7.

---

## Preguntas de repaso

> [!question]- ¿Por qué el mensaje DHCP Discover utiliza la dirección de destino 255.255.255.255?
> Porque el nuevo cliente recién conectado aún no tiene asignada una dirección IP ni conoce la dirección IP del servidor DHCP local; el broadcast a nivel de subred asegura que cualquier servidor DHCP activo reciba la solicitud.

> [!question]- ¿Por qué los puristas de la arquitectura de redes critican el uso de NAT?
> Porque viola el principio de extremo a extremo (*End-to-End principle*): los routers (Capa 3) inspeccionan y modifican números de puerto (Capa 4), impiden que hosts externos inicien conexiones directas con hosts internos y complican protocolos P2P y de telefonía IP.

> [!question]- ¿Cómo resuelve UPnP (*Universal Plug and Play*) la dificultad de alojar servidores detrás de NAT?
> Proporciona un protocolo automatizado para que una aplicación interna descubra el router NAT y le solicite abrir y mapear automáticamente un puerto público externo hacia su IP y puerto privado sin intervención manual del usuario.

