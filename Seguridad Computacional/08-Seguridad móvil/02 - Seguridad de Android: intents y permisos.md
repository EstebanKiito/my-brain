---
ramo: "Seguridad Computacional"
tema: "Seguridad móvil"
tags:
  - seguridad/movil
  - android
  - origen/complemento
prerrequisitos:
  - "[[01 - Seguridad de iOS: arranque seguro y enclave]]"
---

# Seguridad de Android: intents y permisos

En Android cualquiera puede publicar una app y el usuario puede ejecutar la que quiera, aun siendo maliciosa. Esto exige resolver el **control de acceso app contra app**: qué apps pueden usar contactos, ubicación o SMS, y cómo interactúan entre sí. En escritorio, cada app tiene todos los privilegios del usuario (un ransomware puede todo); las VM aíslan bien pero casi no permiten compartir; los sitios web se aíslan pero comparten poco.

## Aislamiento y comunicación
Una app es un proceso Linux con almacenamiento privado (`/data/data/app`), un **manifiesto** con sus permisos y la firma de su desarrollador. Se aísla con un UID por app, más SELinux y seccomp. La interacción es solo por **intents**: mensajes (como RPC) que pasan por un único **monitor de referencia** confiable.

Los componentes son: *Activity* (pantalla), *Service* (segundo plano o RPC), *Content provider* (base de datos) y *Broadcast receiver* (anuncios). Un intent lleva `Component` (destino), `Action` (el opcode, como `DIAL`) y `Data` (un URI). Puede ser **implícito**: sin destino, el monitor elige según la acción, lo que da flexibilidad (cambiar de app de contactos sin romper nada).

## Permisos
Una **etiqueta de permiso** es un string (por ejemplo `com.android.phone.DIALPERM`). Cada app tiene un conjunto de etiquetas autorizadas y cada componente está protegido por una (los content providers, dos: leer y escribir); el monitor deja pasar un intent solo si el emisor tiene la etiqueta. El manifiesto pide permisos (el desarrollador puede pedir cualquiera) y no cambia sin reinstalar.

| Tipo | Ejemplos | Comportamiento |
|---|---|---|
| **Normal** | Cambiar fondo, volumen | No se pregunta al usuario (privilegio mínimo igual) |
| **Peligroso** | SMS, contactos, cámara, ubicación, calendario, teléfono | Se pregunta al usuario (hoy, al usarlo por primera vez) |
| **Firma** | Configuración de red | Solo apps del mismo desarrollador |

> [!tip] Control de acceso obligatorio (MAC)
> Los permisos se declaran fuera del código y el sistema los hace cumplir, así que se analizan sin leer la app y funcionan aunque el programador olvide verificar. Es lo opuesto al DAC de UNIX, donde cada programa fija los permisos de sus archivos.

No es un MAC puro: un servicio con varias funciones RPC puede verificar por su cuenta, y los *broadcast* privados (como `SMS_RECEIVED`) requieren una etiqueta extra para el receptor. Delegar permisos temporales: **URI delegado** (App1 pasa a App2 acceso a un URI; hay que revocarlo) e **intents pendientes** (App2 envía luego con los permisos de App1).

## Debilidades
- Si dos apps definen el mismo permiso, gana la primera: una app maliciosa puede registrarlo como "normal".
- El usuario decide mal: el malware común envía SMS a números premium; los permisos peligrosos son tantos que insensibilizan, se piden "por si acaso" y no se puede aceptar solo algunos.
- Mejoras: pedir al usar, desactivar permisos sueltos, análisis de Google Play (clones, ejecución de prueba) y desinstalación remota.

## Preguntas de repaso

> [!question]- ¿Por qué Android usa un manifiesto y un monitor de referencia y no deja que cada componente verifique?
> Porque los programadores olvidan verificaciones; así la política se aplica por defecto, se puede analizar sin entender el código y ayuda al usuario y a la tienda a ver qué pide cada app.

> [!question]- ¿Qué diferencia hay entre un permiso "normal" y uno "peligroso"?
> El normal no preocupa a la seguridad y no se pregunta al usuario; el peligroso (SMS, contactos) sí se consulta porque podría causar daño.

> [!question]- ¿Cómo puede una app maliciosa quedarse con un permiso importante?
> Declarándolo primero con ese nombre como "normal": como la primera definición gana, las demás apps pueden obtenerlo sin preguntar.
