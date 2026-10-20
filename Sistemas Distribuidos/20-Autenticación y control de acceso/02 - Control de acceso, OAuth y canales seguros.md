---
ramo: "Sistemas Distribuidos"
tema: "Autenticación y control de acceso"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Autenticación, PKI y Kerberos]]"
---

# Control de acceso, OAuth y canales seguros

Saber **quién** es alguien (autenticación) no dice **qué puede hacer** (autorización). Este tema cierra el ciclo con las políticas de control de acceso, la delegación de permisos con OAuth y los canales seguros que combinan todo lo anterior para proteger una conversación.

## Políticas de control de acceso

Una política define **quién puede hacer qué acción sobre qué recurso**.

| Política | Cómo funciona | Ejemplo |
|---|---|---|
| **MAC** (control obligatorio) | Una autoridad central define la política; los datos tienen etiquetas (público, secreto…) y los usuarios no pueden cambiar permisos | Clasificación militar |
| **DAC** (control discrecional) | El **dueño** del recurso decide y puede cambiar los permisos | Permisos de archivos en UNIX |
| **RBAC** (basado en roles) | Los permisos se asignan a **roles**, y cada usuario obtiene los de su rol | Rol "profesor" en Canvas |
| **ABAC** (basado en atributos) | Reglas sobre atributos (rol, curso, contexto, país…); permite reglas complejas y dinámicas | "Los profesores del curso X pueden leer las notas de sus estudiantes" |

## OAuth: delegar sin compartir la contraseña

La **delegación** permite que una entidad actúe con la autoridad de otra. **OAuth** (versión 1.0 en 2006; la 2.0 es la más usada y la 2.1, la más actual y estricta) deja que una aplicación acceda a recursos en nombre de un usuario **sin recibir sus credenciales**: "Iniciar sesión con Google" o "con GitHub".

![Flujo de OAuth](adjuntos/Flujo%20de%20OAuth.png)

> [!example]- Transcripción de la imagen
> Pasos 3 a 5 del flujo: el cliente envía una *Request* junto con un token al *Servidor de Servicio* (la aplicación) (3); el servidor valida el token (4) y devuelve la *Response* (5). Arriba está el *Authorization Server* (Google), donde ocurrieron los pasos 1 y 2: el usuario se autentica y recibe el token.

El usuario se autentica **solo** ante el servidor de autorización, que entrega un token; la aplicación recibe ese token y lo valida, nunca la contraseña. Ver también [[04 - OAuth y Single Sign-On|OAuth y Single Sign-On]].

## Canales seguros

Un **canal seguro** es una capa sobre un canal de comunicación que garantiza propiedades de seguridad para los datos entre dos procesos. Combina criptografía simétrica, asimétrica y funciones hash.

| Propiedad | Significado |
|---|---|
| **Autenticación** | Identidad confiable de ambas partes |
| **Privacidad** | Cifrado de extremo a extremo |
| **Integridad** | Protección contra modificaciones |
| **Anti-replay** | Impide retransmitir mensajes viejos |

**Fases típicas:**

1. **Negociación (handshake):** intercambio de claves (usualmente asimétrico) y verificación de identidad (certificados).
2. **Establecimiento del canal:** derivación de una clave simétrica compartida y selección de algoritmos.
3. **Comunicación segura:** cada mensaje se cifra y se firma, con timestamps o números de secuencia contra el replay.

| Tecnología | Uso |
|---|---|
| HTTPS (TLS) | Web y APIs REST |
| SSH | Administración remota de servidores |
| IPsec | VPN a nivel de red |
| gRPC + TLS | Comunicación entre microservicios |
| SMTP + TLS | Correo seguro |

## Pregunta de aplicación

CineTV permite iniciar sesión con la cuenta de Spotify, para no ingresar credenciales en el sitio. Los usuarios se quejan de que, al cambiar el país desde el que se conectan, dejan de ver videos que empezaron en su país de origen. Lo correcto: CineTV **usa OAuth** (Spotify autoriza sin entregar la contraseña) y una política **ABAC** para la autorización (el país es un atributo del contexto). Spotify no es una CA ni un TGS, y la restricción no depende de un rol.

> [!warning] Autenticación no es autorización
> Iniciar sesión con Spotify autentica al usuario; lo que puede ver lo decide la política de acceso de CineTV.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre DAC y MAC?
> En DAC el dueño del recurso decide y cambia los permisos; en MAC una autoridad central define la política y los usuarios no pueden modificarla.

> [!question]- ¿Por qué OAuth es más seguro que dar la contraseña de Google a una aplicación?
> Porque la aplicación solo recibe un token con permisos acotados, que se puede revocar. La contraseña queda solo en el servidor de autorización.

> [!question]- ¿Cómo evita un canal seguro los ataques de replay?
> Incluyendo timestamps o números de secuencia en cada mensaje: un mensaje repetido o viejo se detecta y se descarta.
