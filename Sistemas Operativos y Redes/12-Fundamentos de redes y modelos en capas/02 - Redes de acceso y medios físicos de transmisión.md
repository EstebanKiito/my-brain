---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/acceso
  - redes/medios-fisicos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos\|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Redes de acceso y medios físicos de transmisión

Las redes de acceso conectan los sistemas terminales al primer router de la red troncal mediante tecnologías de enlace guiadas por cable o inalámbricas no guiadas.

## Tecnologías de acceso y medios físicos (mis apuntes)

- CLASE 2
- 9/10/24
- Supuesto de que la clase 2 se vio la clase:
- https://www.youtube.com/watch?v=_pyWVod9dzE&list=PLVTkEjeczcER2aOMHPIfaHCpTx61iKsoV&index=51
- COMUNICACION END-To-END
- Hosts: Dispositivos que ejecutan programas
- Unos host acutan como clientes
- Otro como servidores
- Comuncacion entre HOSTS:
- Clientes: Dispositivo liviano que solicita un servicio
- Servidores: En dispositivos poderosos que poseen servicios (data centers)
- INFRAESTRUCTURAS DE COMUNCACIONES
- DSL
- CABLE
- FTTH
- ETHERNET
- FIBRA OPTICA
- Wi-Fi
- etc
- DSL: utiliza la via telefónica para comunicarse
- Transforma la señal digital, y la envia mediante via telefónica tradicional, transformando frecuencias de transmision
- CABLE: Coaxial por ejemplo, cables de cobre con recubrimiento, esta es un medio compartido, a diferencia de dsl
- Ventaja: Instalación mas facil → Extensión de cables
- Desventaja: Medio es compartido, si varios usarios se conectan, provoca congestiones
- CABLE FIBRA OPTICA (FTTH):
- Se basa en cables de fibra optica que tienen una altísima tasa de transmisión
- Estándares: desde 1Mbps a 1Gbps
- ETHERNET: Cables de red, pares de trenzados de cobre, protocolo IEEE 802.3
- Velocidad de transmision: 10Mbs 100Mbps 1Gbps 10 Gbps
- Implementan la famosa LAN (LOCAL AREA NETWORK)
- Router → Switch (comparte conexion) → → → Varios dispositivos (cada uno con su ancho de banda estandarizado)
- WIFI: simil al ethernet pero inalambcrica, de corto alcance
- IEE 802.11 Velocidades: 54Mbps, 150Mbps
- Implementan WLAN (wirless LAN)
- Similar a esta BANDA ANCHA MOVIL → Wide Area: 3G, 4G, LTE
- MEDIOS FISICOS
- Transmitir bits atravez de un enlace fisico o inalambrico
- Los medios pueden ser guiados o cableados: solidos
- los no guiados son los de tipo broadcast: inalambricos, satelital
- Solidos:
- Par trenzado de cobre UTP RECUBIERTO → (cable que no este recubierto puede tener interferencias y afectar los bits)
- Cable Coaxial de Cobre → Un unico cable protegido (asilado del ruido electromagnetico)
- FIBRA OPTICA → Usa haz de luz
- Medio inalambricos → Al ser emitida, esta expuesto a las interferencias que atenuen
- Porpagacion multicamino: Señales que llegan por multiples caminos

> [!warning] Posible error
> En los apuntes aparecen erratas en `acutan` (actúan), `Comuncacion` (comunicación), `wirless` (wireless), `IEE` (IEEE) y `Porpagacion` (propagación).

> [!tip] Complemento: Tecnologías de acceso al borde y medios de transmisión
> ![Red de acceso mediante línea telefónica DSL](adjuntos/Red%20de%20acceso%20mediante%20línea%20telefónica%20DSL.png)
> ![Red de acceso mediante cable coaxial y medio compartido](adjuntos/Red%20de%20acceso%20mediante%20cable%20coaxial%20y%20medio%20compartido.png)
> ![Red de área local cableada Ethernet con switches y routers](adjuntos/Red%20de%20área%20local%20cableada%20Ethernet%20con%20switches%20y%20routers.png)
> ![Red de acceso inalámbrico Wi-Fi y banda ancha móvil](adjuntos/Red%20de%20acceso%20inalámbrico%20Wi-Fi%20y%20banda%20ancha%20móvil.png)
>
> > [!example]- Transcripción de las imágenes
> > **Comparación de redes de acceso y medios físicos:**
> > - **DSL (*Digital Subscriber Line*):** línea telefónica punto a punto dedicada desde el hogar hasta el DSLAM de la central telefónica; no comparte el enlace físico con vecinos.
> > - **Cable (HFC - *Hybrid Fiber-Coaxial*):** red coaxial compartida entre múltiples hogares de un vecindario; la capacidad se divide concurrentemente entre usuarios activos.
> > - **FTTH (*Fiber To The Home*):** red óptica pasiva (PON) que entrega pulsos de luz láser directamente al hogar con tasas de transmisión simétricas superiores a $1\text{ Gbps}$.
> > - **Ethernet (IEEE 802.3):** LAN cableada con pares trenzados UTP/STP y conmutación en estrella mediante switches.
> > - **Wi-Fi (IEEE 802.11) y telefonía celular:** medios no guiados sujetos a pérdida de trayectoria (*path loss*), atenuación por obstáculos y desvanecimiento por propagación multicamino (*multipath fading*).

## Preguntas de repaso

> [!question]- ¿Por qué la velocidad efectiva en una red de acceso por cable (HFC) puede degradarse durante horas punta mientras que en DSL se mantiene más estable?
> Porque en la arquitectura de cable coaxial HFC el medio físico de transmisión es compartido (*shared medium*) por todos los hogares conectados al mismo nodo vecinal; si múltiples vecinos descargan simultáneamente, el ancho de banda del canal se divide. En DSL la línea de cobre es un enlace dedicado punto a punto entre el hogar y la central (DSLAM).

> [!question]- ¿Cuál es la diferencia física de propagación entre un cable de par trenzado de cobre y un cable de fibra óptica?
> El par trenzado transmite señales como pulsos de voltaje eléctrico a través de conductores de cobre, estando expuesto a interferencias electromagnéticas (EMI) y atenuación resistiva. La fibra óptica transmite pulsos de luz (fotones) a través de filamentos de vidrio de sílice, siendo completamente inmune al ruido electromagnético y sufriendo una atenuación drásticamente inferior en largas distancias.

> [!question]- ¿Qué es la propagación multicamino (*multipath propagation*) en enlaces inalámbricos y cómo afecta la señal?
> Es el fenómeno donde la onda electromagnética transmitida se refleja y dispersa en obstáculos físicos (muros, edificios, suelo), llegando al receptor por múltiples trayectorias con diferentes retardos de tiempo y fases, lo que genera interferencia constructiva o destructiva (desvanecimiento o *fading*) y distorsión de la señal.

