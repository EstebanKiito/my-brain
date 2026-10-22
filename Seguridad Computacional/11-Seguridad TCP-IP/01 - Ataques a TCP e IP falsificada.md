---
ramo: "Seguridad Computacional"
tema: "Seguridad TCP-IP"
tags:
  - seguridad/redes
  - origen/complemento
prerrequisitos:
  - "[[03 - OWASP Top 10]]"
---

# Ataques a TCP e IP falsificada

La Internet es una red abierta y descentralizada, y el modelo de amenaza supone un adversario que puede **mirar** tus datos, **enviar paquetes arbitrarios** y **modificar** paquetes en tránsito. El núcleo de la red solo se preocupa de que lleguen los datos (*liveness*); la seguridad se pone en los extremos (SSH, TLS, Kerberos, gracias a la criptografía). Aun así, los ataques antiguos siguen vigentes en versiones nuevas.

## Por qué fallaba el login remoto de 1980
`telnet` abre una conexión TCP sin cifrar: se puede robar la contraseña espiando, modificar datos o inyectar. `rlogin` no envía contraseña: confía en una lista de hosts (`.rhosts`) según la **IP de origen** (y el nombre obtenido por DNS inverso, que el dueño del dominio inverso controla). La defensa aparente era que, si el atacante miente en la IP de origen, las respuestas no le llegan y no podría completar TCP.

## Handshake TCP y ataque de número de secuencia
```
C → S: SYN(SNc)
S → C: SYN(SNs), ACK(SNc+1)
C → S: ACK(SNs+1)
```
Solo el verdadero C debería recibir el segundo mensaje y saber `SNs`. Pero si el atacante A puede **adivinar** `SNs`, puede enviar los paquetes 1 y 3 con la IP de C y nunca ver el 2. Los hosts incrementaban el número inicial (ISN) en pasos fijos (128 por segundo, 64 por conexión): A abre una conexión legítima, ve el ISN y suma 64 para predecir el siguiente (el RST que C envía puede evitarse suprimiendo a C).

Consecuencias de predecir números de secuencia:
1. **Falsificar la IP de origen** para entrar a servicios que autentican por IP (`rlogin`): la capa TCP nunca prometió esa autenticación.
2. **Reset de conexión** (DoS): un `RST` con un número dentro de la ventana corta la conexión (afectó sesiones BGP entre enrutadores, que pueden perturbar el tráfico por minutos).
3. **Secuestro de conexiones:** inyectar datos en una conexión ya establecida (esperar a que alguien inicie sesión y tomar el control).

> [!tip] Defensas
> **No autenticar por IP**; usar autenticación criptográfica extremo a extremo (SSH, TLS, Kerberos); que los ISP filtren IP de origen obviamente falsas; y ISN impredecibles: `ISN = ISN_antiguo + hash(IPs, puertos, secreto)`, un desfase aleatorio por par origen/destino, sin estado extra (hoy con SipHash).

## El mismo problema en DNS
DNS usa UDP, sin números de secuencia, con puerto de destino fijo (53): si el atacante sabe que el cliente consulta, solo necesita adivinar el puerto de origen (a menudo predecible) y el ID de 16 bits. Ataque popular desde 2008. Mitigaciones: aleatorizar ID y puerto, y **DNSSEC** (registros firmados), de adopción lenta por costos de rendimiento y de gestión de claves, y por el problema de enumeración de nombres (NSEC3).

## Preguntas de repaso

> [!question]- ¿Por qué `rlogin` parecía seguro y por qué no lo era?
> Porque suponía que una conexión TCP desde una IP venía realmente de ese host, ya que las respuestas volverían a esa IP; pero si el atacante adivina el número de secuencia no necesita ver las respuestas.

> [!question]- ¿Por qué no se pueden elegir los ISN completamente al azar?
> Porque TCP debe evitar números usados hace poco para el mismo par host/puerto; por eso se usa un desfase aleatorio por par origen/destino sobre el contador normal.

> [!question]- ¿Por qué DNS es más fácil de falsificar que TCP?
> Porque va sobre UDP: no hay handshake ni números de secuencia, solo puertos e ID de consulta, así que basta adivinar unos 16 bits de puerto y 16 de ID.
