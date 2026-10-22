---
ramo: "Seguridad Computacional"
tema: "Arquitectura de seguridad de Google"
tags:
  - seguridad/arquitectura
  - origen/apuntes
prerrequisitos:
  - "[[03 - Defensa en profundidad y seguridad imperfecta]]"
---

# Arquitectura de seguridad y aislamiento

Una **arquitectura de seguridad** estructura el sistema completo para defender contra grandes clases de ataques conocidos, prevenir ataques aún desconocidos y contener el daño de los que tengan éxito, en vez de reaccionar parchando. El caso de estudio del curso es el paper de seguridad de la plataforma en la nube de Google.

## Qué se analiza y qué se usa
- **Modelo de amenaza:** qué se defiende (datos de clientes, claves), quién ataca (empleados, competidores) y qué poderes tiene.
- **Principio:** minimizar la confianza.
- **Técnicas:** aislamiento, autenticación, separación de privilegios y canales seguros.

Los objetivos de Google son evitar la divulgación de datos, mantener la disponibilidad, rastrear qué pasó tras un compromiso y ayudar a los ingenieros a construir aplicaciones seguras. Las amenazas incluyen errores de software, redes comprometidas, contraseñas de empleados robadas, ataques internos (sobornos), hardware malicioso y discos descartados.

## El entorno de servidor
Centros de datos con máquinas físicas, sobre ellas máquinas virtuales, dentro de ellas servicios y aplicaciones que se hablan por **RPC**; los servidores *front-end* (GFE) convierten HTTP/HTTPS en RPC.

![Entorno de servidor de Google](adjuntos/Entorno%20de%20servidor%20de%20Google.png)

> [!example]- Transcripción de la imagen
> Un recuadro "Platform DC" con tres servicios (Svc A, Svc B y GFE) sobre dos bloques KVM. Entra una solicitud HTTP a un KVM, y hay flechas entre el GFE y otros dos centros de datos (DC). El diagrama del profesor tiene un detalle impreciso: la solicitud HTTP no llega directamente al KVM sino al front-end.

## Aislamiento
> [!tip] Idea clave
> La actividad de X no debe afectar a la de Y, incluso si X es maliciosa o Y tiene errores. Sin aislamiento no hay esperanza para la seguridad; con él se puede permitir y controlar la interacción.

Se aplica en cada nivel: centros de datos separados, máquinas separadas, varias VM por máquina y varios servicios por VM, de modo que si algo cae el resto sigue. Google lo implementa con usuarios Linux separados, *sandboxes* de lenguaje y de kernel, VM y máquinas dedicadas para servicios sensibles.

Las **VM** cumplen dos papeles: mantienen *fuera* a atacantes de otras VM y mantienen *dentro* (confinan) al código comprometido, siempre que se controle con quién habla por la red. No son un aislamiento perfecto entre invitados (el VMM puede tener errores).

## Preguntas de repaso

> [!question]- ¿Qué dos funciones cumple una máquina virtual como mecanismo de aislamiento?
> Impide que atacantes de otras VM lleguen a la nuestra, y confina el código malicioso o con errores dentro de su propia VM.

> [!question]- ¿Por qué en una arquitectura de seguridad se parte del aislamiento?
> Porque sin una separación fuerte entre actividades no se puede controlar la interacción; el aislamiento es la base sobre la que se agregan autorización y compartición controlada.

> [!question]- ¿Cómo se diferencia una arquitectura de seguridad de simplemente parchar vulnerabilidades?
> Busca anticiparse: reducir clases enteras de ataques y limitar el daño aunque aparezcan ataques desconocidos, en vez de reaccionar a cada error.
