---
ramo: "Seguridad Computacional"
tema: "Separación de privilegios con OKWS"
tags:
  - seguridad/arquitectura
  - origen/complemento
prerrequisitos:
  - "[[02 - Monitor de referencia, autorización y canales seguros]]"
  - "[[01 - Buffer overflows y sus defensas]]"
---

# Separación de privilegios y OKWS

Encontrar y corregir bugs (plan A) no basta: seguirán apareciendo. El plan B es construir sistemas que **sigan siendo seguros aunque haya bugs**, dividiendo software y datos para limitar el daño. **OKWS**, el servidor web de OkCupid, es el caso de estudio.

## El problema de la configuración clásica
En un servidor tipo Apache, N procesos idénticos tienen todo el código de la aplicación y acceso a toda la base de datos: es "cáscara dura, interior blando". Un solo bug (desbordamiento, control de acceso faltante, recorrido de rutas con `../etc/passwd`, inyección SQL) expone todo.

> [!tip] Dos beneficios de separar
> Limitar el **daño** de un exploit (menor privilegio) y limitar el acceso del atacante al código con bugs (**superficie de ataque**). Dificultad: hay que aislar, permitir interacción controlada y no perder rendimiento. Se puede separar por servicio, por usuario, por cantidad de bugs, por exposición o por privilegio inherente.

## Arquitectura de OKWS
Principios: procesos en `chroot`, como usuarios sin privilegios, con mínimos privilegios de BD y funcionalidad independiente en procesos independientes.

![Arquitectura de OKWS](adjuntos/Arquitectura%20de%20OKWS.png)

> [!example]- Transcripción de la imagen
> Las conexiones HTTP externas (puerto 80) llegan a `okd`; la administración interna al puerto 11277. `okld` es "padre de" `okd`, `pubd`, `oklogd` y los servicios `svc1`, `svc2`, `svc3`. `okd` envía HTTP a los servicios y habla por RPC con `pubd`; los servicios escriben a `oklogd` y acceden a sus datos (`data1`, `data2`), y a la base de datos por SQL. Leyenda: RPC, HTTP, "Parent Of" y SQL; los procesos grises son ayudantes de OKWS y los blancos son del sitio.

| Componente | Función | Privilegio si se compromete | Superficie de ataque |
|---|---|---|---|
| `okld` | Lanza todo según la configuración; corre como root | Superusuario del servidor | Pequeña (casi sin entrada de usuario) |
| `okd` | Enruta solicitudes HTTP al servicio | Ver todas las solicitudes y robar contraseñas | Parsear la primera línea HTTP |
| `pubd` | Acceso a archivos (plantillas) | Corromper plantillas | Pedidos de `okd` |
| `oklogd` | Escribe logs | Borrar o alterar el log y cubrir huellas | Mensajes de log |
| Servicio | Lógica de la aplicación | Datos del servicio de cualquier usuario | Solicitudes HTTP y contenido de la BD |
| `dbproxy` | Intermediario con la BD | Todos los datos de esa BD | RPC de servicios autorizados |

La mayoría de los bugs estarán en los servicios (complejos, escritos por expertos en citas y no en seguridad); el código crítico lo escriben expertos y es pequeño. Un overflow en el editor de perfil no expone contraseñas, aunque sí puede dejar leer perfiles.

## `dbproxy` y los tokens
La BD acepta SQL general; `dbproxy` acepta **RPC** (no SQL) y genera él el SQL, así los servicios no sufren inyección SQL. Ahí vive la política: una matriz servicio/consulta. Como TCP no dice quién se conectó, cada servicio recibe de `okld` un **token secreto de 20 bytes** que envía en cada RPC.

## Cómo se hace cumplir el aislamiento
`okld` usa `setuid` (un UID distinto por servicio: no pueden hacerse `kill`, `ptrace` ni leer sus *core dumps*), `chroot` (solo ven sus archivos) y GID separados (el servicio puede ejecutar su binario pero no leerlo ni modificarlo), y pasa descriptores de archivo (el puerto 80 a `okd`). `okld` corre como root solo para esto, por eso debe hacer lo mínimo; `okd` no es root.

**Límites:** no hay aislamiento por usuario (arrancar procesos por usuario es caro), las herramientas UNIX (`chroot`, UIDs, espacios de nombres globales) son difíciles de usar y no hay "sin acceso por defecto". Por eso hoy se usan [[01 - Contenedores de Linux y capabilities|contenedores]], VM y *seccomp*; Chrome aísla cada *frame* y `ssh-agent` aísla las claves.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre "limitar el daño" y "reducir la superficie de ataque"?
> El daño es lo que logra el atacante si compromete un componente (sus privilegios); la superficie es por dónde puede alcanzar sus bugs (sus entradas). La separación reduce ambos.

> [!question]- ¿Por qué `dbproxy` impide la inyección SQL desde los servicios?
> Porque los servicios solo envían RPC con parámetros; el SQL lo genera `dbproxy`, que además solo permite las consultas autorizadas para el token de cada servicio.

> [!question]- ¿Por qué `okld` corre como root pero `okd` no?
> `okld` necesita root para `setuid` y para abrir el puerto 80; `okd` ve todo el tráfico HTTP, así que se le pasa el puerto ya abierto y se le quita todo privilegio posible.
