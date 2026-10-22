---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/redes
  - origen/complemento
prerrequisitos:
  - "[[01 - Serialización con JSON: dumps, loads y personalización]]"
---

# Fundamentos de redes: arquitectura cliente-servidor, sockets y puertos

Para que aplicaciones distribuidas colaboren entre sí —ya sea una aplicación móvil consultando un servidor o dos computadores jugando en línea—, es necesario establecer canales de comunicación digital sobre redes de datos. Dominar cómo se identifican los equipos y cómo se diferencian los programas en ejecución es la base del *networking*.

## Arquitectura Cliente-Servidor

El modelo predominante en los sistemas distribuidos es la arquitectura **cliente-servidor** (*client-server*), donde los roles están claramente definidos:

- **Servidor (*Server*):** es un programa o computador que ofrece un servicio o recurso compartido (como páginas web o bases de datos). Permanece a la escucha pasiva en un puerto determinado, esperando solicitudes entrantes para procesarlas y retornar una respuesta.
- **Cliente (*Client*):** es el programa que inicia activamente la comunicación enviando una solicitud (*request*) al servidor y esperando el resultado (*response*).

![Arquitectura cliente-servidor](adjuntos/Arquitectura%20cliente-servidor%20en%20redes%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - Esquema de red cliente-servidor:
>   - Múltiples clientes independientes (computadores personales y dispositivos) envían peticiones a través de internet hacia un servidor centralizado que responde a cada uno.

## Identificación en la red: direcciones IP y DNS

Para que los datos lleguen al destinatario correcto, cada dispositivo conectado a una red requiere un identificador único:

- **Dirección IP (*Internet Protocol address*):** es la dirección lógica asignada a cada interfaz de red. En **IPv4** está compuesta por 4 octetos numéricos separados por puntos (ejemplo `192.168.0.10`). La dirección especial **`127.0.0.1`** (denominada **localhost** o interfaz de *loopback*) permite que un programa cliente y un programa servidor se comuniquen dentro de la **misma máquina física** sin salir a la red externa.
- **DNS (*Domain Name System*):** es el directorio telefónico distribuido de internet que traduce nombres amigables para los humanos (como `www.ing.puc.cl`) a su dirección IP numérica correspondiente.

## Puertos y Sockets: identificando programas específicos

Un computador no ejecuta una sola aplicación de red, sino decenas al mismo tiempo (navegador, base de datos, cliente de mensajería). Una dirección IP solo llega hasta el computador físico, pero no sabe a qué programa entregar el mensaje:

- **Puerto (*Port*):** es un identificador numérico de 16 bits (con valores de $0$ a $65535$) que permite multiplexar la comunicación y asociar el tráfico con un proceso o aplicación concreta del sistema operativo.
  - **Puertos bien conocidos (*Well-known ports*, 0 a 1023):** reservados para servicios estándar del sistema (HTTP en el puerto 80, HTTPS en el 443, SSH en el 22).
  - **Puertos registrados (1024 a 49151):** usados por servicios y bases de datos comunes (ej. PostgreSQL 5432, Flask 5000).
  - **Puertos dinámicos o efímeros (49152 a 65535):** asignados temporalmente por el sistema operativo al cliente para recibir la respuesta.

![Distribución de puertos y sockets](adjuntos/Distribuci%C3%B3n%20de%20puertos%20y%20sockets%20en%20un%20host.png)

> [!example]- Transcripción de la imagen
> - Diagrama de puertos en un host:
>   - Un computador con una única dirección IP distribuye el tráfico entrante hacia distintos procesos según el número de puerto asignado.

Un **socket** es el punto final de comunicación bidireccional (*endpoint*) formado por la combinación indisociable de una dirección IP y un número de puerto: $(\text{IP}, \text{Puerto})$.

> [!tip] La analogía del edificio
> Piensa en la **dirección IP** como la dirección de la calle del edificio (identifica el inmueble en la ciudad), y en el **número de puerto** como el número de departamento u oficina dentro del edificio (identifica a la persona o proceso específico que recibirá la correspondencia).

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre el comportamiento de un cliente y un servidor al iniciar la comunicación?
> El servidor permanece en estado pasivo esperando conexiones en una dirección conocida, mientras que el cliente toma la iniciativa activa de contactar al servidor.

> [!question]- ¿Para qué se utiliza la dirección IP `127.0.0.1` (localhost)?
> Para establecer comunicaciones de red entre procesos que corren dentro de la misma máquina física, permitiendo probar aplicaciones cliente y servidor localmente sin requerir conexión a internet.

> [!question]- ¿Por qué una dirección IP por sí sola no es suficiente para entregar un mensaje de red a una aplicación?
> Porque la IP solo identifica a la máquina destino; el sistema operativo necesita el número de puerto para dirigir los paquetes al proceso específico que abrió dicho canal.

> [!question]- ¿Qué elementos constituyen formalmente un socket de red?
> La combinación única de una dirección IP (que identifica al host) y un número de puerto (que identifica al proceso de software dentro del host).

