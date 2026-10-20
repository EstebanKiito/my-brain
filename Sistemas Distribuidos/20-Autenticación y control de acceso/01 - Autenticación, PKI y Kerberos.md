---
ramo: "Sistemas Distribuidos"
tema: "Autenticación y control de acceso"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[02 - Cifrado asimétrico, hash y firmas digitales]]"
---

# Autenticación, PKI y Kerberos

Cifrar no basta si no se sabe **con quién** se habla: el man-in-the-middle de Diffie-Hellman lo demostró. La **autenticación** verifica la identidad declarada de una entidad. En un sistema distribuido hay que hacerlo a escala, en ambos sentidos y sin repartir secretos a mano; para eso existen **PKI** y **Kerberos**.

## Formas de autenticarse

- **Firmas digitales:** con la llave privada (o firmando el hash del mensaje), cualquiera con la pública verifica que el mensaje lo creó su dueño y que no fue alterado.
- **Comparación de hash:** el servidor guarda el hash de la contraseña de cada usuario; al iniciar sesión, calcula el hash de la contraseña recibida y lo compara. Ver [[02 - Hashing de contraseñas con bcrypt|hashing de contraseñas]].
- **Desafío-respuesta** (*challenge-response*): el verificador presenta un desafío, la otra parte elabora una respuesta y el verificador evalúa si es correcta.

![Desafío-respuesta con llave simétrica](adjuntos/Desaf%C3%ADo-respuesta%20con%20llave%20sim%C3%A9trica.png)

> [!example]- Transcripción de la imagen
> El nodo M pide autenticarse. El verificador genera `X = mensaje_aleatorio` y le pide "Cifrar X". M responde con X cifrado con la llave compartida $K_{AB}$. El verificador comprueba `Desencriptar(X, K_AB) == X` y lo autentica ✅. La versión asimétrica es igual, pero M cifra con su llave privada y el verificador descifra con la pública.

Como el desafío es aleatorio cada vez, capturar una respuesta antigua no sirve para un ataque de *replay*.

## Desafíos

- **Autenticación en ambos sentidos:** el servidor autentica al cliente, pero el cliente también debe asegurarse de la identidad del servidor.
- **Escalabilidad:** administrar claves crece con la cantidad de nodos.
- **Delegación de credenciales:** a veces un usuario quiere delegar su identidad o permisos a otro agente sin exponer sus credenciales.
- **Expiración:** hay que decidir cada cuánto volver a verificar una identidad.

## PKI: infraestructura de clave pública

- Cada entidad genera su par de llaves pública y privada.
- Una **autoridad certificadora** (CA) firma digitalmente un **certificado** que vincula una llave pública con la identidad de su dueño.

**Emitir:** el servidor genera sus llaves y envía a la CA una solicitud de firma (**CSR**) con su llave pública y su información. La CA verifica la solicitud, firma el contenido con su llave privada y emite el certificado.

**Verificar:** el cliente recibe el certificado; comprueba que lo firmó una CA de confianza, que está vigente y que sus datos coinciden; luego extrae la llave pública y reconoce al servidor.

![Cliente verifica un certificado de la CA](adjuntos/Cliente%20verifica%20un%20certificado%20de%20la%20CA.png)

> [!example]- Transcripción de la imagen
> "Extrae llave pública y reconoce la autenticidad del servidor": el cliente, con la llave pública del servidor (Juego) obtenida del certificado (con una lupa y un ✓), lo reconoce ✅. A la derecha, la CA con su llave.

> [!tip] Ventaja de PKI
> Escala a muchos nodos: no hace falta que cada par de entidades comparta una clave secreta, y se autentica al servidor sin contacto previo, solo con un certificado firmado por una CA de confianza.

## Kerberos

Protocolo de autenticación del **MIT** que usa criptografía **simétrica** y un servidor central de confianza, el **KDC** (*Key Distribution Center*), que emite **tickets** temporales.

![Flujo completo de Kerberos](adjuntos/Flujo%20completo%20de%20Kerberos.png)

> [!example]- Transcripción de la imagen
> 1: el usuario se autentica ante el *Authentication Server*. 2: el AS busca en su base la llave del usuario y la del TGS. 3: devuelve al usuario un *Ticket-Granting Ticket*. Dentro del KDC están el AS, el *Ticket Granting Server* (TGS) y la base de llaves; aparte está el *Service Server*.

1. **Authentication Server (AS):** el usuario se autentica; el AS busca la llave secreta del usuario y la del TGS, y envía un **TGT** (*Ticket-Granting Ticket*) cifrado con la llave del TGS y luego con la del usuario.
2. **Ticket Granting Server (TGS):** el usuario descifra el TGT con su llave y lo envía al TGS junto con el servicio que quiere; el TGS lo descifra con su llave, verifica y responde con un **ticket de servicio**.
3. **Service Server (SS):** el usuario presenta el ticket al servidor del servicio, que lo verifica y le entrega el servicio.

| | PKI | Kerberos |
|---|---|---|
| Criptografía | Asimétrica | Simétrica |
| Escalabilidad | Muy alta | Moderada (centralizada) |
| Autoridad | CA | KDC |
| Credencial | Certificados | Tickets |

## Preguntas de repaso

> [!question]- ¿Por qué un desafío-respuesta resiste un ataque de replay?
> Porque el desafío es aleatorio y distinto cada vez: una respuesta capturada antes no sirve para un desafío nuevo.

> [!question]- ¿Qué comprueba un cliente al recibir un certificado?
> Que lo firmó una CA de confianza, que está vigente y que la identidad coincide con el servidor al que se conecta. Si todo calza, confía en la llave pública que contiene.

> [!question]- ¿Para qué sirve el TGT en Kerberos?
> Para pedir tickets de servicio al TGS sin tener que volver a autenticarse con la contraseña cada vez.
