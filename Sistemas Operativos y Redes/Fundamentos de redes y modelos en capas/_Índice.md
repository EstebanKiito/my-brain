# Fundamentos de redes y modelos en capas — índice

Principios teóricos y arquitectónicos de las redes de computadores e Internet. Estudio de la estructura de red: sistemas terminales (*hosts* clientes y servidores en el borde de la red), enlaces de comunicación y dispositivos de interconexión (switches y routers). Redes de acceso y medios físicos de transmisión guiados (par trenzado de cobre UTP, cable coaxial y fibra óptica hasta el hogar / FTTH) y no guiados (Wi-Fi 802.11 y banda ancha móvil 3G/4G/LTE) junto a los fenómenos de atenuación e interferencia por propagación multicamino. Análisis del núcleo de la red: cálculo del retardo de transmisión ($d_{\text{trans}} = L/R$), principios de la conmutación de paquetes (*Packet Switching*, colas en routers, tablas de reenvío y descarte por congestión) frente a la conmutación de circuitos (*Circuit Switching*, multiplexación FDM/TDM y retardo de establecimiento). Modelos de arquitectura en capas: comparación entre el modelo de referencia teórico OSI de 7 capas y el estándar empírico de Internet TCP/IP de 5 capas. Caracterización de las unidades de datos (PDU) y responsabilidades de las capas de transporte, red, enlace y física. Detalle exhaustivo del proceso de encapsulamiento y flujo de datos a través de switches (Capa 2) y routers (Capa 3).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 1 y Clase 2 de los apuntes originales de Redes, complementadas exhaustivamente con las diapositivas oficiales de `Contenido_8_Redes.pdf` y la literatura estándar de redes de computadores (Kurose & Ross, Tanenbaum).

## Orden de estudio

1. [[01 - Arquitectura de Internet, nodos, enlaces y protocolos|Arquitectura de Internet, nodos, enlaces y protocolos]]: conceptos fundamentales de interconexión, definición formal de protocolo, hosts, módems, direccionamiento IP público frente a privado y conmutación de paquetes.
2. [[02 - Redes de acceso y medios físicos de transmisión|Redes de acceso y medios físicos de transmisión]]: tecnologías de acceso al borde (DSL, cable HFC compartido, FTTH, Ethernet LAN y Wi-Fi), medios guiados frente a no guiados y propagación multicamino.
3. [[03 - Conmutación de paquetes frente a conmutación de circuitos|Conmutación de paquetes frente a conmutación de circuitos]]: cálculo de retardo de transmisión ($L/R$), conmutación de paquetes con colas de routers frente a reserva dedicada en conmutación de circuitos con FDM y TDM.
4. [[04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP|Modelos de capas: modelo de referencia OSI frente al stack TCP-IP]]: justificación de la modularidad en capas, modelo OSI de 7 estratos y consolidación en el stack TCP/IP de 5 capas con foco en la capa de aplicación.
5. [[05 - Capas de transporte, red, enlace y física|Capas de transporte, red, enlace y física]]: unidades de datos (segmentos, datagramas, tramas y bits), servicios connection-oriented (TCP) y connection-less (UDP), y funciones de enrutamiento y enlace.
6. [[06 - Proceso de encapsulamiento y flujo de datos en la red|Proceso de encapsulamiento y flujo de datos en la red]]: agregación sucesiva de cabeceras ($H_t, H_n, H_l$), niveles de procesamiento en switches de capa 2 y routers de capa 3, y ciclo de desencapsulamiento en el host receptor.

