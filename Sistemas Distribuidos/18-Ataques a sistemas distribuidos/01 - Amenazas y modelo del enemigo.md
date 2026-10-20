---
ramo: "Sistemas Distribuidos"
tema: "Ataques a sistemas distribuidos"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[04 - Objetivos de un sistema distribuido]]"
---

# Amenazas y modelo del enemigo

Además de replicar datos y tolerar fallas, un sistema distribuido debe protegerse de quien **quiere** hacerle daño. Una falla es accidental; un ataque es intencional y busca el punto más débil. Para diseñar defensas, primero hay que definir **qué** se protege y **de quién**.

## Los tres pilares

Un ataque busca comprometer al menos uno de estos pilares:

| Pilar | Garantiza | Ejemplo de ataque |
|---|---|---|
| **Confidencialidad** | Que la información privada no se divulgue | Filtración de contraseñas |
| **Integridad** | Que los datos se envíen y almacenen correctamente, sin alteraciones | Cambiar el rol de un usuario en la base de datos |
| **Disponibilidad** | Que el sistema esté disponible cuando corresponde | Un ataque DDoS |

Un mismo ataque puede afectar varios pilares: una inyección SQL puede leer datos privados y, a la vez, cambiar permisos.

## El modelo del enemigo

Para analizar las amenazas se postula un **enemigo** (o adversario): un atacante conceptual con estas capacidades:

- Puede **enviar** cualquier mensaje a cualquier proceso.
- Puede **leer o copiar** cualquier mensaje entre dos procesos.
- Puede **generar mensajes con una dirección de origen falsificada**; por eso no se puede confiar en la IP de origen.
- Puede atacar desde un computador **legítimamente conectado** a la red (ataque interno) o desde uno no autorizado.

> [!tip] Por qué un enemigo tan poderoso
> Suponer un adversario con todas estas capacidades permite **anticiparse** a lo que podría hacer y diseñar defensas más robustas. Si el sistema resiste a ese enemigo, resiste a uno más débil.

## Tipos de amenazas

- **Leakage (fuga de información):** receptores no autorizados obtienen información. Puede ser sutil: inferir datos a partir de la mera **existencia** de un mensaje o del patrón de tráfico.
- **Tampering (manipulación):** alteración no autorizada de la información, desde cambiar contenido para afectar la seguridad hasta impedir que el usuario haga su solicitud correctamente. Ejemplos: darle permisos altos a un usuario de bajo nivel; inyección SQL.
- **Denial of use (denegación de uso):** interferir con el funcionamiento del sistema sin que el atacante obtenga un beneficio directo; típicamente, ataques de denegación de servicio. Pueden botar solo una parte (por ejemplo, el backend) mientras el frontend sigue arriba.

> [!warning] El enemigo puede estar adentro
> El modelo no supone que el atacante viene solo desde fuera: un empleado o un equipo legítimo comprometido tiene acceso a la red interna. Por eso hacen falta también defensas internas, como el monitoreo.

La visión desde las redes (ataques en distintas capas y defensas) está en [[04 - Fundamentos de seguridad en redes: amenazas, ataques y defensas|Fundamentos de seguridad en redes]].

## Preguntas de repaso

> [!question]- ¿Qué pilar compromete un ataque DDoS y cuál una filtración de contraseñas?
> El DDoS compromete la disponibilidad; la filtración de contraseñas, la confidencialidad.

> [!question]- ¿Por qué el modelo del enemigo asume que puede falsificar la dirección de origen?
> Porque en una red real se pueden forjar paquetes con una IP falsa. Si el sistema confiara en la IP para identificar al emisor, sería fácil suplantar a otro.

> [!question]- ¿Cómo puede haber fuga de información sin leer el contenido de los mensajes?
> Infiriendo a partir de la existencia de los mensajes o del patrón de tráfico: quién se comunica con quién, cuándo y cuánto.
