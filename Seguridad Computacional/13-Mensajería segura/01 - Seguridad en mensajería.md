---
ramo: "Seguridad Computacional"
tema: "Mensajería segura"
tags:
  - seguridad/mensajeria
  - criptografia
  - origen/complemento
prerrequisitos:
  - "[[01 - TLS 1.3 y el canal seguro]]"
  - "[[02 - Certificados y autoridades certificadoras]]"
---

# Seguridad en mensajería

La seguridad de mensajería importa en la práctica y combina todas las técnicas del ramo. El escenario: Alice envía un mensaje `M` a Bob; se quiere **confidencialidad** (solo ellos lo leen) y **autenticidad** (Bob confirma que lo envió Alice), y a veces integridad o negabilidad.

## Hop-by-hop frente a extremo a extremo
El correo electrónico nació sin criptografía y su seguridad se agregó de a poco; un mensaje pasa por 10 o 20 saltos con DNS y varios servidores. Lo desplegado es **salto a salto**: STARTTLS (oportunista), POP/IMAP sobre TLS, DKIM (firma por organización de origen, útil contra suplantación y spam) y BIMI. Pero no compone: cada servidor ve y puede modificar el mensaje en claro, y la seguridad depende de muchos operadores.

La **seguridad extremo a extremo** depende solo de los usuarios y sus dispositivos: el remitente firma, el destinatario verifica y los intermediarios no importan (WhatsApp, iMessage, Signal). Tiene tres ejes: establecer confianza (claves), el protocolo de conversación y la privacidad de transporte (metadatos).

## Mensaje único y canal seguro
- **Mensaje único (tipo PGP):** `c = E(PK_Bob, m)` y `s = Sign(SK_Alice, c)`; Bob verifica y descifra. Preguntas abiertas: ¿firmar `c` o `m`? (conviene lo más cercano al original), y el replay.
- **Canal simplificado:** cada parte envía un aleatorio cifrado y firmado; comparten `randomA ‖ randomB`, derivan claves `Kx = Hash(randomA ‖ randomB ‖ x)` y usan `E(K1, M)` con `MAC(K2, M)`.

## Establecer confianza
Hay que ligar identidades con claves públicas:

| Enfoque | Idea | Límite |
|---|---|---|
| **Oportunista** | Cada parte envía su clave en claro | Resiste espías pasivos, no activos |
| **TOFU** | Se acepta la primera clave y se fija (SSH `known_hosts`) | Débil ante un adversario persistente; un cambio legítimo se ve como alerta |
| **Fuera de banda** | Verificar la clave en persona | Muy seguro pero poco práctico |
| **Servidor central de claves** | El servidor entrega la clave del contacto (iMessage: cada dispositivo registra su clave pública en Apple) | Un servidor deshonesto puede entregar la clave de Eve |
| **Key Transparency** | El servidor lleva un log público (solo se agrega) de cambios de claves; el dueño revisa el suyo y quien consulta verifica | Eficiencia, privacidad, evitar bifurcaciones |
| **Keybase (verificación social)** | Pruebas firmadas en otros servicios (`Sign(PK_Alice, "soy alice177 en twitter")`) que el cliente verifica y pregunta al usuario | Comprometer las cuentas de prueba; las claves se fijan y las actualizaciones las firma la clave anterior |

> [!tip] Tensión permanente
> La usabilidad es crítica: un sistema muy seguro pero impráctico no se usa, y recuperar claves o dispositivos perdidos es difícil.

## Seguridad de la conversación
- **Secreto hacia adelante:** Alice genera un par temporal, Bob cifra con `PK_temp`, y Alice borra `SK_temp`; las grabaciones antiguas no se pueden descifrar aunque luego se comprometan las claves largas.
- **Autenticidad negable:** convencer al destinatario sin prueba ante terceros. En vez de firmas, un MAC simétrico: Bob elige una clave `K`, la envía cifrada, Alice responde con `M` y `MAC(K, M)` y al final **publica `K`**, así cualquiera pudo haber producido el mismo MAC (OTR, Signal).
- Los grupos agregan complejidad; también hay tensión entre confidencialidad y denunciar abusos.

## Privacidad de transporte (metadatos)
Ocultar quién habla con quién y cuándo es costoso. Con un servidor central, TLS oculta el contenido pero no los patrones; **onion routing** (Tor) mejora, aunque un adversario global correlaciona tiempos; difusión o *mixnets* (lotes de mensajes) ocultan más pero con latencia y complejidad.

## Preguntas de repaso

> [!question]- ¿Por qué la seguridad salto a salto no basta para el correo?
> Porque cada servidor intermedio ve el mensaje en claro y puede modificarlo, y proteger todos los saltos exige configuración correcta y operadores confiables.

> [!question]- ¿Cómo ayuda Key Transparency contra un servidor de claves deshonesto?
> Lo obliga a publicar en un log público cada clave que entrega: si da la de Eve, Bob lo detecta al revisar su log, y si no la publica, Alice ve que no está en el log.

> [!question]- ¿Por qué se usa un MAC en vez de una firma para la negabilidad?
> Porque quien comparte la clave puede producir el mismo MAC; al publicar la clave después, nadie puede probar ante terceros que el mensaje lo escribió Alice.
