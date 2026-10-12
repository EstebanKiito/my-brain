---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/modelos
  - redes/osi
  - redes/tcp-ip
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos\|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Modelos de capas: modelo de referencia OSI frente al stack TCP-IP

Para gestionar la complejidad del software y hardware de comunicaciones, las redes se estructuran modularmente en capas donde cada estrato implementa protocolos específicos y ofrece servicios bien definidos al nivel superior.

## Modelos en capas y arquitectura de protocolos (mis apuntes)

- Software de Redes
- Hardware soluciona mitad de la tarea
- Redes se organizan en base a un modelo de CAPAS
- Las Capas se comunican usando PROTOCOLOS
- Este modelo de capas se ven a partir de un medio fisico
- Cada capa atiende a un problema especifico
- Y cada capa funciona utilizando un protocolo específico
- Los mensajes pueden ser modificados en cada capa → Agregando headers o modificando todo el mensaje
- Cada capa entrega servicios a una Capa Superior
- Y solicita servicios a una capa inferior
- Modelo OSI (modelo de referencia)
- Define las reponsabilidades para cada capa
- No define estandares ni protocolos ni implementaciones
- A partir de esto, una implementacion practica es la STACK TCP/IP
- TCP/IP
- Con respecto al modelos OSI: es mas compactada, y tenemos solo 5 capas:
- Applicacion
- Transporte
- Network
- Link
- Physical
- CAPA APLICACION
- Funciona con los procesos, cuando vemos el tema de sockets, estamos hablando de la capa aplicacion, vamos a pedirle servicios a la capa de transporte
- Algunos de esto son los protocolos que intercambian MENSAJES
- ej:
- HTTP
- SMTP
- FTP
- DNS
- IMAP
- POP
- Capa presentacion y sesion (solo en modelo OSI) → Son compactadas en Applicacion (para modelo TCP/IP)
- Presentacion de mensajes y sesion → Es la logica en el envio
- Cada capa aplicacion es encargado de:
- Codificar
- Encriptar
- Autorizar
- etc

> [!tip] Complemento: Comparación arquitectónica de OSI frente a TCP/IP
> ![Comparación de modelos en capas OSI frente a TCP IP](adjuntos/Comparación%20de%20modelos%20en%20capas%20OSI%20frente%20a%20TCP%20IP.png)
>
> > [!example]- Transcripción de la imagen
> > **Mapeo entre el modelo de referencia OSI (7 capas) y el modelo de Internet TCP/IP (5 capas):**
> > - **Modelo OSI (ISO/IEC 7498-1):**
> >   - 7. **Aplicación:** interfaz directa con el usuario o aplicación.
> >   - 6. **Presentación:** sintaxis y semántica de datos (codificación, compresión, cifrado).
> >   - 5. **Sesión:** control de diálogo, sincronización y delimitación de sesión.
> >   - 4. **Transporte:** transferencia confiable de datos de proceso a proceso.
> >   - 3. **Red:** enrutamiento de paquetes de host a host a través de la subred.
> >   - 2. **Enlace de datos:** transferencia confiable de tramas sobre el enlace físico adyacente.
> >   - 1. **Física:** transmisión de flujo de bits brutos sobre el medio.
> > - **Stack TCP/IP:** fusiona las funciones de las capas 5, 6 y 7 de OSI dentro de una única capa superior (**Capa de Aplicación**). Si una aplicación necesita cifrado o control de sesión, lo implementa en su propio código o biblioteca de espacio de usuario (p. ej. mediante TLS/HTTPS).

## Preguntas de repaso

> [!question]- ¿Por qué el modelo OSI se considera un modelo de referencia teórico mientras que TCP/IP es la arquitectura práctica de Internet?
> Porque OSI definió una especificación conceptual formal de 7 capas antes de que existieran implementaciones masivas de mercado. En contraste, TCP/IP evolucionó de forma pragmática a partir de la implementación de ARPANET, guiada por el principio de desarrollo empírico de la IETF (*rough consensus and running code*).

> [!question]- ¿Dónde residen las responsabilidades de las capas de presentación y sesión de OSI dentro del modelo de Internet TCP/IP?
> Residen íntegramente dentro de la capa de aplicación o en bibliotecas auxiliares de espacio de usuario utilizadas por el desarrollador (como OpenSSL para cifrado TLS, o mecanismos de cookies/tokens para gestión de sesión en HTTP).

> [!question]- ¿Cuál es la unidad de datos de protocolo (PDU) intercambiada en la capa de aplicación?
> En la capa de aplicación, la unidad de datos intercambiada entre procesos se denomina formalmente **mensaje** (*message*).

