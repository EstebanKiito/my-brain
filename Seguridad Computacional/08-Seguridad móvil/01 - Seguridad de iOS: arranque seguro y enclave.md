---
ramo: "Seguridad Computacional"
tema: "Seguridad móvil"
tags:
  - seguridad/movil
  - ios
  - origen/complemento
prerrequisitos:
  - "[[02 - Monitor de referencia, autorización y canales seguros]]"
---

# Seguridad de iOS: arranque seguro y enclave

El diseño de iOS busca que un iPhone **robado y bloqueado** no entregue sus datos, aun si el atacante lo desarma o explota el sistema operativo. Importa a clientes que guardan secretos (periodistas, gobiernos) y es ventaja competitiva. Supone que el dispositivo tiene código de acceso y estaba bloqueado al robarlo.

## Ataques contemplados
Probar todos los códigos (a menudo solo cuatro dígitos), suplantar la huella o el rostro, extraer los chips *flash* o leer la RAM, explotar el kernel por USB/WiFi/radio (activos aunque esté bloqueado), instalar un SO hackeado o **degradar** a uno antiguo con un error conocido.

## Hardware
CPU principal, RAM, almacenamiento flash, un **motor AES** entre la CPU/DRAM y el flash, una CPU de **enclave seguro** con una clave `UID` grabada en el hardware (el enclave puede cifrar y descifrar con ella, pero nunca leerla) y sensores (huella, Face ID).

![Arquitectura del enclave seguro de iOS](adjuntos/Arquitectura%20del%20enclave%20seguro%20de%20iOS.png)

> [!example]- Transcripción de la imagen
> Un *system on chip* con el procesador de aplicaciones, el controlador de memoria (hacia la DRAM), el controlador de NAND flash y el motor AES, conectados por un bus. En un recuadro azul, el **Secure Enclave**: su procesador, un TRNG (generador aleatorio verdadero), su propio motor AES, PKA (aceleración de clave pública), un bus I2C hacia el almacenamiento no volátil seguro, y un motor de protección de memoria que cifra y autentica su memoria en la DRAM. Una flecha punteada con una llave va del enclave al motor AES.

## Arranque seguro
Cadena de confianza: **Boot ROM** (solo lectura, fijada en fábrica) → iBoot → kernel → apps; cada etapa verifica la **firma de Apple** de la siguiente (las apps, la de un desarrollador aprobado).

**Ataque de degradación:** instalar un kernel antiguo, firmado por Apple pero con un bug conocido. Guardar un número de versión no sirve (¿dónde, y quién impide modificarlo?). La solución es el **ECID**, un identificador de chip único y de solo lectura: los servidores de Apple firman cada actualización para un ECID concreto y el arranque verifica que la firma corresponda a ese teléfono; Apple no firmará un kernel obsoleto.

## Enclave seguro
Una CPU separada con su propio arranque seguro, que comparte DRAM pero cifra y autentica su memoria. Evita que la CPU principal (y un kernel comprometido) vea claves, datos biométricos o salte los límites de intentos del código. Los sensores se comunican con el enclave con una clave AES compartida de fábrica (y un nonce) para impedir repeticiones y sensores falsos. Face ID proyecta puntos infrarrojos para distinguir un rostro 3D de una foto.

## Cifrado de datos
Todo el flash está cifrado. La clave no se guarda: se calcula como aproximadamente $E_{UID}(E_{UID}(\dots(\text{código})))$, cifrando muchas veces con el UID dentro del enclave. Así: depende del código (no existe tras reiniciar), el enclave limita los intentos, es lenta (frena la fuerza bruta) y depende del UID (no se puede atacar fuera del teléfono).

El **envoltorio de claves** $E_{k1}(k2)$ permite delegar: quien conoce `k1` obtiene `k2`. Se usa una clave por archivo `Kf`, envuelta con una clave de clase de protección, y los metadatos con `Kfs`, protegida por el UID (borrar `E_UID(Kfs)` borra todo rápido y los chips no sirven en otro teléfono). El kernel solo ve claves envueltas; el motor AES hace el cifrado.

| Clase de protección | Se puede descifrar |
|---|---|
| Completa | Solo con el teléfono desbloqueado |
| Completa salvo abiertos | Se puede escribir bloqueado (adjuntos en segundo plano) |
| Hasta la primera autenticación | Tras el primer desbloqueo desde el reinicio (por defecto en apps de terceros) |
| Sin protección | Siempre (clave solo desde UID); permite borrado rápido |

Touch ID/Face ID no sirven tras reiniciar: primero se exige el código, y el enclave guarda claves cifradas para usarlas luego. El borrado seguro (tras 10 intentos) usa "almacenamiento borrable" con acceso directo a la NAND.

**Costos y debilidades:** hardware caro, código incómodo, actividades en segundo plano difíciles y datos perdidos si se olvida el código. Quedan bugs de kernel, de USB/WiFi, claves de Apple y la extracción del UID.

## Preguntas de repaso

> [!question]- ¿Por qué firmar para un ECID específico evita la degradación?
> Porque el adversario no tiene un kernel antiguo firmado para el ECID de la víctima y Apple no firmará versiones obsoletas, de modo que no hace falta guardar un contador manipulable.

> [!question]- ¿Por qué la clave de datos se deriva del código y del UID?
> Del código, para que no exista en el dispositivo cuando está bloqueado; del UID, para que no pueda probarse todos los códigos en otra máquina con los chips extraídos.

> [!question]- ¿Para qué sirve el envoltorio de claves?
> Para delegar acceso sin entregar la clave original (por ejemplo, permitir a una app escribir en segundo plano) y para borrar datos rápidamente eliminando solo la clave envuelta.
