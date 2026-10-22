---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/seguridad
  - origen/complemento
prerrequisitos:
  - "[[04 - Protocolo HTTP: estructura de mensajes, métodos y códigos de estado]]"
---

# Seguridad en la web: TLS, HTTPS y certificados digitales

El protocolo HTTP original transmite toda la información en texto plano sin cifrar. Si un usuario se conecta a una red Wi-Fi abierta en una cafetería y envía su contraseña o datos bancarios por HTTP, cualquier atacante en la misma red puede interceptar los paquetes y leerlos de inmediato. Para proteger la comunicación se desarrolló HTTPS.

## Amenazas sobre HTTP plano

Cuando el tráfico viaja sin protección criptográfica queda expuesto a dos ataques críticos:

- **Espionaje (*Eavesdropping / Packet Sniffing*):** actores intermedios (proveedores de internet, routers intervenidos) leen contraseñas, tokens y datos confidenciales.
- **Ataque de intermediario (*Man-in-the-Middle / MITM*):** un atacante se interpone silenciosamente en el canal, alterando el contenido de las respuestas del servidor o inyectando código malicioso sin que el cliente lo note.

## ¿Qué es HTTPS y TLS?

**HTTPS** (*Hypertext Transfer Protocol Secure*) es la combinación del protocolo HTTP tradicional ejecutándose sobre un túnel seguro provisto por **TLS** (*Transport Layer Security*, el estándar moderno sucesor del antiguo SSL). Por convención, HTTPS utiliza el puerto TCP **443** (mientras HTTP usa el puerto 80).

TLS garantiza tres pilares de seguridad fundamentales:

1. **Privacidad y confidencialidad:** todo el tráfico viaja fuertemente cifrado; solo el cliente y el servidor pueden leerlo.
2. **Integridad de datos:** incorpora códigos de autenticación que garantizan que ningún dato fue alterado, truncado o corrompido en el tránsito.
3. **Autenticación de identidad:** asegura al usuario que está conectado al servidor legítimo y no a un sitio impostor clonado.

## El modelo criptográfico híbrido y el saludo TLS

El protocolo TLS combina dos ramas de la criptografía para balancear seguridad matemática y alto rendimiento:

$$\text{Criptografía Asimétrica (Autenticación)} \longrightarrow \text{Criptografía Simétrica (Transferencia masiva)}$$

1. **Fase asimétrica (El saludo o *TLS Handshake*):**
   - El cliente contacta al servidor y este le presenta su **Certificado Digital**.
   - El cliente valida que el certificado esté firmado por una **Autoridad Certificadora** (**CA**, *Certificate Authority*) de confianza global.
   - Mediante la clave pública del servidor, ambos acuerdan de forma matemáticamente segura una **clave secreta compartida de sesión**, sin que ningún espía pueda descifrarla.
2. **Fase simétrica (Cifrado de datos en bloque):**
   - Una vez acordada la clave secreta de sesión, el resto de la comunicación HTTP (cabeceras, URLs completas, cuerpo JSON) se cifra con algoritmos simétricos rápidos (como AES), permitiendo un rendimiento de red casi instantáneo.

> [!tip] Lo que oculta HTTPS
> Cuando navegas por HTTPS, un observador intermedio solo puede ver la dirección IP y el nombre de dominio del servidor al que te conectas. La ruta específica (`/cuenta/saldo`), los parámetros de consulta, las contraseñas, las cookies de sesión y el cuerpo del mensaje viajan completamente blindados.

## Preguntas de repaso

> [!question]- ¿Por qué no se utiliza criptografía asimétrica durante toda la sesión de navegación en HTTPS?
> Porque los cálculos matemáticos de la criptografía asimétrica son cientos de veces más lentos y costosos en CPU que los algoritmos simétricos; por ello solo se usa al inicio para negociar una clave de sesión rápida.

> [!question]- ¿Qué rol cumplen las Autoridades Certificadoras (CA) en la seguridad de la web?
> Actúan como terceros de confianza que verifican la identidad del propietario del dominio y firman digitalmente su certificado, evitando que un atacante suplante al servidor original.

> [!question]- ¿Qué información viaja cifrada bajo HTTPS y qué datos quedan visibles para un intermediario de red?
> Quedan visibles únicamente la IP de destino y el dominio (mediante SNI); la ruta de la URL, las cabeceras, los parámetros y el cuerpo del mensaje viajan completamente cifrados.

> [!question]- ¿En qué consiste un ataque de Hombre en el Medio (*Man-in-the-Middle*) y cómo lo previene TLS?
> Consiste en un atacante que intercepta y altera los mensajes entre cliente y servidor sin que lo noten; TLS lo previene exigiendo certificados digitales autenticados y firmas de integridad criptográfica por paquete.
