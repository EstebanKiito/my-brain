---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - dns
  - resolucion-nombres
  - resource-records
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/02 - Concepto de socket e identificación por IP y puerto|02 - Concepto de socket e identificación por IP y puerto]]"
---

# Sistema de nombres de dominio (DNS) y resolución de consultas

Para conectarse a un servidor se necesita su dirección IP, pero las personas recuerdan nombres como `www.google.com`. El **DNS** (*Domain Name System*) es el sistema que **traduce un dominio a su dirección IP**: una base de datos distribuida y jerárquica que el navegador consulta antes de cada conexión. Las consultas viajan normalmente por **UDP**, al **puerto 53**, porque caben en un solo mensaje y así se evita el *handshake* de TCP.

## Antes de cada conexión HTTP

Para abrir `http://iic2333.ing.puc.cl/slides/5-disk.html`:

1. El cliente ejecuta el proceso **cliente DNS**.
2. El navegador extrae el dominio (`iic2333.ing.puc.cl`) y se lo pasa al cliente DNS.
3. El cliente DNS envía una **query** por ese dominio a un **servidor DNS** (normalmente el servidor local que entrega el ISP o la red).
4. Recibe la respuesta, que incluye la IP.
5. Le pasa la respuesta al navegador.
6. El cliente HTTP inicia la **conexión TCP** a esa IP.

## Una base de datos jerárquica

![Jerarquía distribuida del sistema de nombres de dominio DNS](adjuntos/Jerarqu%C3%ADa%20distribuida%20del%20sistema%20de%20nombres%20de%20dominio%20DNS.png)

> [!example]- Transcripción de la imagen
> "Base de datos distribuida y jerárquica". Arriba, los **Root DNS servers**. Debajo, los servidores de dominio de nivel superior: *com*, *org* y *edu DNS servers*. Más abajo, los servidores de cada organización: *yahoo.com* y *amazon.com* bajo com, *pbs.org* bajo org, *poly.edu* y *umass.edu* bajo edu.

- **Servidores raíz** (*root*): **13 en el mundo**, nombrados de la A a la M, cada uno con muchas réplicas (cuatro de ellos replicados en Chile).
- **Servidores TLD** (*top-level domain*): los de `.com`, `.org`, `.edu`, `.cl`…
- **Servidores de cada dominio**.

Los servidores **almacenan mappings** (nombre → IP). Si uno no conoce un mapping, lo consulta a un servidor de mayor jerarquía, y eventualmente se puede llegar a la raíz.

| Tipo de servidor | Qué hace |
|---|---|
| **Autoritativo** | **Administra** el mapping de su institución: **tiene** las direcciones |
| **No autoritativo** | **Mantiene temporalmente** el mapping (en caché): las tiene que buscar |

## Consultas iterativas y recursivas

Según el material: las **consultas iterativas** **retornan la respuesta**, completa o parcial, al que preguntó (en la figura del material, los servidores de los pasos 1 y 2); las **consultas recursivas** **reenvían la consulta** cuando el servidor no tiene la respuesta (los pasos 4 y 6). En la recursiva el trabajo se delega por completo, y el servidor local espera la respuesta final de una cadena de servidores: cliente → servidor local → raíz → TLD → …

![Resolución iterativa de consultas en el sistema DNS](adjuntos/Resoluci%C3%B3n%20iterativa%20de%20consultas%20en%20el%20sistema%20DNS.png)

> [!example]- Transcripción de la imagen
> El *Requesting host* `cis.poly.edu` pregunta (1) a su *Local DNS server* `dns.poly.edu`. El servidor local consulta a su vez al *Root DNS server* (2, respuesta 3), al *TLD DNS server* (4, respuesta 5) y al *Authoritative DNS server* `dns.umass.edu` (6, respuesta 7), y finalmente responde al host (8). El nombre buscado es `gaia.cs.umass.edu`.

![Resolución recursiva de consultas en el sistema DNS](adjuntos/Resoluci%C3%B3n%20recursiva%20de%20consultas%20en%20el%20sistema%20DNS.png)

> [!example]- Transcripción de la imagen
> El host pregunta (1) al servidor local, este (2) a la raíz, la raíz (3) al TLD, el TLD (4) al servidor autoritativo; las respuestas vuelven por la misma cadena (5, 6, 7) y el servidor local responde al host (8).

**En la práctica**, los servidores raíz no se consultan tanto, porque las respuestas ya están **cacheadas** en servidores más abajo en la jerarquía. El caché reduce el tráfico, y cada respuesta guardada tiene un **timeout**. Si la respuesta no está en caché, la consulta demora más.

## Registros DNS

Las respuestas DNS tienen la forma **(nombre, valor, tipo, ttl)**:

![Caché DNS y balanceo de carga entre múltiples servidores](adjuntos/Cach%C3%A9%20DNS%20y%20balanceo%20de%20carga%20entre%20m%C3%BAltiples%20servidores.png)

> [!example]- Transcripción de la imagen
> "(nombre, valor, tipo, ttl)". **Tipo A**: nombre es nombre del host; valor es dirección IP. **Tipo NS**: nombre es dominio; valor es IP de host autoritativo. **Tipo CNAME**: alias, nombre es alias; valor es nombre real. **Tipo MX**: valor es el nombre de un *mail server*.

| Tipo | Para qué sirve | Ejemplo |
|---|---|---|
| **A** | Dominio → **IP** | ([relay1.bar.foo.com](http://relay1.bar.foo.com), 145.37.93.126, A) |
| **NS** | Encontrar el **servidor autoritativo** de un dominio | (foo.com, dns.foo.com, NS) |
| **CNAME** | **Alias**: valor es el nombre real | (foo.com, relay1.bar.foo.com, CNAME) |
| **MX** | Saber a qué **servidor de correo** van los mails del dominio | (foo.com, mail.bar.foo.com, MX) |

El **TTL** indica cuánto tiempo se puede guardar el registro en caché.

![Registros de recursos DNS Resource Records tipo A NS CNAME y MX](adjuntos/Registros%20de%20recursos%20DNS%20Resource%20Records%20tipo%20A%20NS%20CNAME%20y%20MX.png)

> [!example]- Transcripción de la imagen
> Formato de un mensaje DNS: una cabecera de **12 bytes** con *Identification*, *Flags*, *Number of questions*, *Number of answer RRs*, *Number of authority RRs* y *Number of additional RRs*; luego las secciones *Questions* (nombre y tipo de la consulta), *Answers* (RRs de respuesta), *Authority* (registros de servidores autoritativos) y *Additional information* (información adicional útil).

> [!tip] ¿Y si un sitio tiene varios servidores?
> Un sitio grande no se aloja en una sola máquina. Lo habitual es conectarse a un servidor que deriva a otros, o a un *proxy* o réplica cercana con copia del contenido original, de modo que no todos los usuarios llegan al mismo servidor.

## Preguntas de repaso

> [!question]- ¿Qué pasos ocurren antes de que el navegador abra la conexión TCP de un sitio?
> El navegador extrae el dominio de la URL y se lo pasa al cliente DNS, que consulta a un servidor DNS, recibe la IP y se la entrega al navegador. Recién entonces el cliente HTTP abre la conexión TCP a esa IP.

> [!question]- ¿Qué diferencia hay entre un servidor autoritativo y uno no autoritativo?
> El autoritativo administra el mapping de su dominio y tiene las direcciones. El no autoritativo solo guarda temporalmente en caché respuestas que obtuvo de otros.

> [!question]- ¿Por qué los servidores raíz no reciben tantas consultas?
> Porque las respuestas quedan cacheadas en servidores más abajo en la jerarquía, que responden sin subir hasta la raíz mientras no expire su timeout.

> [!question]- ¿Para qué sirven los registros A, NS, CNAME y MX?
> A traduce un nombre a una IP; NS indica el servidor autoritativo de un dominio; CNAME asocia un alias con el nombre real; MX indica el servidor de correo del dominio.
