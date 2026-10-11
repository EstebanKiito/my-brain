---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/fundamentos
  - redes/arquitectura
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Estructura de sistemas operativos/01 - Qué es un sistema operativo\|01 - Qué es un sistema operativo]]"
---

# Arquitectura de Internet, nodos, enlaces y protocolos

Internet constituye una red global de redes interconectadas que permite la comunicación entre procesos distribuidos mediante la conmutación de paquetes y un conjunto riguroso de protocolos.

## Elementos de una red y protocolos (mis apuntes)

- CLASE 1
- 7 / 10 / 2024
- Preguntas concurrentes
- ¿Porque las redes de datos? → Permitir que un proceso se comunique con otro
- ¿Donde se encuentra el otro proceso?
- ¿Por que medio? → Cable, aire?
- Como se transmite? por el aire?
- etc etc etc
- La red mas grande: Internet
- red como interconexion de redes mas pequeñas
- hay estructuras de red distintas
- Ejemplo de redes distintas:
- Elementos de las redes
- Ej: Puede ser un dispositivo inalambrico, cableado etc (celular computador)
- NODOS (HOST): Elemenots de origen y destinto de mensajes
- Cada enlace varia en velocidad, calidad etc
- ENLACES: por donde se transmiten, enlaces por cables o inalambricas (datos moviles, wifi)
- Router: Para darle conexion a varios dispositivos → Lo que hace es conectarse al Switch
- Switch: Comparte la conexion a varios dispositivos (es como una zapatilla)
- DISPOSITIVOS INTERCAMBIOS: Routers, Switches, son el medio donde se deciden encaminar la red, para hacer llegar el mensaje donde deba llegar
- El modem lo que puede hacer es transformar una señal enviada atravez de los cables (una señal analogica) a una digital → esto Permite ser compartida con los elementos de una red en una casa por ejemplo
- Modem = MOdulador - DEModulador → Dispositivo que permite transforma una señal de un tipo a otro, investigar
- Puede hacer la transformacion inversa, para enviar a los cables la señal (digital → Analoga)
- PUNTOS ACCESO: Modem, Access point(inalambricos), Cell tower (conexion celular) → Esta ultima, es conectada desde el router para compartir conexion a varios dispositivos
- PROVEDORES DE ACCESO: ISP (internet Service Provider) → Empresa que vende servicio
- ENTONCES?
- En una casa, se envia informacion a la ISP (proveedor de internet), el modem transforma la señal digital a analoga para pasarla por los cables (cableado, fibra optica coaxial etc), y en ISP se hace el trabajo inverso, transforma la señal de los cables a digital para poder compartirla entre la estructura de red definida por isp
- COMO SE TRANSMITE?
- No se transmite la informacion byte a byte → Se transmiten unidades llamadas paquetes
- Internet es una RED DE PAQUETES
- Mediante routers, se envían paquetes a distintas direcciones
- Existen 2:
- TCP: Transport control protocol
- IP: Internet protocol
- Reglas para intercambiar : PROTOCOLOS
- El protocolo TCP, lo que busca es la integridad del mensaje, que el mensaje enviado llegue correctamente a su destino, ya que como se envian paquetes, quizas un mensaje puede estar siendo enviado particionado, por caminos distintos, afectando el tiempo de llegada a destino
- Ejemplo ilustrativo
- Finalmente, se busca con una direccion, y por ejemplo el computador con ip: 146.155.13.75 que esta levantando un servidor, (un proceso que espera, esta escuchando), a que le llegue algo, le enviamos a traves de los routers, un paquete
- En nuestro caso: 192.168.1.10 seria nuestra ip local, de la conexion en nuestro hogar, y 180.106.50.27 seria la direccion publica con la que se identifica mi dispositivo
- Los procesos finalmente, utilizan un API (application Programming Interface) de internet, que permite que el proceso interactue con una infraestructura (otros procesos en otra parte de la red!!!)
- COMO COMUNICARSE?
- Al igual que una conversacion humana (+hola -hola +¿tienes la hora? -2.00 )
- Las computadoras deben interactuar, de tal forma que se avise y se responda, quiero enviar algo, ok solicitud permitida,
- +Tcp connection request -Tcp connection reply + get http://awl.com/kurose-ross - file

> [!warning] Posible error
> En los apuntes aparecen erratas en `PROVEDORES` (proveedores), `Elemenots` (elementos) y `atravez` (a través). Además, `TCP` corresponde a *Transmission Control Protocol* (no Transport Control Protocol).

> [!tip] Complemento: Infraestructura de red y semántica de protocolos
> ![Estructura general de interconexión de redes e Internet](adjuntos/Estructura%20general%20de%20interconexión%20de%20redes%20e%20Internet.png)
> ![Comunicación entre procesos clientes y servidores en la red](adjuntos/Comunicación%20entre%20procesos%20clientes%20y%20servidores%20en%20la%20red.png)
>
> > [!example]- Transcripción de las imágenes
> > **Componentes de la red e interacción de protocolos:**
> > - **Borde de la red (*Network Edge*):** sistemas terminales o hosts (clientes y servidores en centros de datos) que ejecutan procesos de aplicación de usuario.
> > - **Núcleo de la red (*Network Core*):** malla de routers y conmutadores interconectados que transfieren paquetes de datos.
> > - **Redes de acceso (*Access Networks*):** enlaces que conectan los hosts al primer router (*edge router*) a través de ISPs locales, regionales y de nivel 1 (*Tier-1*).
> > - **Definición de protocolo:** un protocolo define el formato, el orden de los mensajes transmitidos y recibidos entre entidades de red, y las acciones ejecutadas ante la transmisión o recepción de un mensaje o evento.
> > - **Direccionamiento privado vs público:** un host dentro de una red doméstica usa una dirección privada (p. ej. `192.168.1.10`, RFC 1918), la cual es traducida por un router mediante NAT (*Network Address Translation*) a una IP pública única global (`180.106.50.27`).

## Preguntas de repaso

> [!question]- ¿Qué es un protocolo de red y qué tres elementos fundamentales define?
> Un protocolo es un conjunto de reglas que gobierna la comunicación entre dos o más entidades remotas. Define formalmente la **sintaxis** (formato y estructura de los paquetes), la **semántica** (significado de cada campo y código de control) y la **temporización o secuencia** (orden de intercambio y acciones ante eventos).

> [!question]- ¿Cuál es la diferencia de función entre un Switch y un Router en una red de área local?
> Un switch opera a nivel de enlace (Capa 2), interconectando dispositivos dentro de la misma red local mediante direcciones físicas MAC. Un router opera a nivel de red (Capa 3), interconectando diferentes subredes lógicas y determinando la mejor ruta para enviar paquetes IP entre ellas.

> [!question]- ¿Qué función realiza un módem (Modulador-Demodulador) en una red doméstica?
> Modula las señales digitales producidas por los dispositivos computacionales en ondas analógicas compatibles con el medio de transmisión físico del proveedor (hilo de cobre, cable coaxial), y demodula las señales analógicas entrantes para convertirlas de nuevo en bits digitales comprensibles por el router.

