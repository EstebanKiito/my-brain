---
ramo: "Seguridad Computacional"
tema: "Arquitectura de seguridad de Google"
tags:
  - seguridad/arquitectura
  - origen/apuntes
prerrequisitos:
  - "[[01 - Arquitectura de seguridad y aislamiento]]"
  - "[[01 - Autenticación con contraseñas]]"
---

# Monitor de referencia, autorización y canales seguros

El aislamiento total no sirve: los servicios deben compartir datos de forma controlada. El **monitor de referencia** es el modelo para hacerlo, y Google lo aplica entre cada par de servicios, apoyado en criptografía y en un arranque seguro.

## El modelo
Un **principal** (persona, dispositivo, programa, servicio) envía una **solicitud**; un **guardia** la revisa según una **política** y, si procede, deja pasar al **recurso** (un servicio o un elemento dentro de él). El guardia hace tres cosas: **autenticar** (¿quién pide?), **autorizar** (¿se permite?) y **auditar** (registrar en un *audit log*, guardado fuera de la caja del recurso para que quien comprometa el recurso no lo pueda borrar).

![Modelo de referencia para compartir](adjuntos/Modelo%20de%20referencia%20para%20compartir.png)

> [!example]- Transcripción de la imagen
> "Sharing: reference model". Un Principal envía un Request al Guard, que recibe la Policy desde arriba, escribe en un Audit log (caja inferior) y, si autoriza, deja pasar a Resource.

## Autorizar
La política es una función `permisos = POLÍTICA(principal, recurso)`, o su matriz de acceso. Se almacena de dos formas:

| | ACL | Capacidades |
|---|---|---|
| Corte de la matriz | Una fila (por recurso) | Una columna (por principal) |
| Dónde se guarda | Con el objeto protegido | Con el principal |
| Responde bien | ¿Quién puede acceder a esto? | Qué puede hacer este principal |
| Plazo | Política de largo plazo (permisos de archivo) | Corto plazo (descriptores, tokens) |
| Debilidad | – | No responde "¿quién tiene acceso?"; revocar es difícil |

En Google, entre servicios se usa una **ACL** (un administrador autoriza qué servicios pueden llamar a otro, aplicada por la infraestructura RPC) y para actuar por un usuario final, una **capacidad**: un *ticket de permiso de usuario final*, de corta duración para limitar el daño si se roba. La granularidad va del centro de datos (firewall: se confía en lo de adentro), al servicio (mínimo privilegio) y al usuario.

> [!tip] Por qué un monitor separado
> Separa la política de la implementación del recurso: es más fácil razonar y cambiar la política, y se evita incrustar chequeos de seguridad en el código del recurso. Depende del aislamiento: no debe haber otro camino al recurso.

**Límites:** no sirve cuando la decisión depende de datos del recurso (ver una oferta solo tras hacer una mayor) ni contra ataques que no son de acceso (DoS).

## Defensa perimetral frente a monitor por servicio
Un firewall perimetral confía en todo lo de adentro: si alguien entra, no hay segunda línea de defensa. Google aplica un monitor por servicio (Gmail puede llamar a Contactos, otros servicios no): **privilegio mínimo**, dividir y dar a cada actividad solo lo que necesita. Los tickets lo refuerzan: además de un servicio aprobado, el usuario debe estar realmente conectado, lo que limita a servicios con errores y a internos.

## Canales seguros y claves
Un servicio autentica a otro con criptografía: las **firmas** prueban quién envió y que no se alteró (integridad) y el **cifrado** asegura que solo lo lea el destinatario. Los RPC se firman y se cifran entre centros de datos, y conviene cifrarlos incluso dentro (un atacante dentro de una máquina podría espiarlos). Esto traslada el problema a la gestión de claves: hace falta un servicio de nombres que asocie servicio y clave pública. Ver [[02 - Cifrado asimétrico, hash y firmas digitales|firmas digitales]].

## Arranque seguro y DoS
Google debe confiar en el hardware: un atacante podría cambiar el servidor, el SO o el BIOS. Para eso usa placas y un **chip de seguridad** propios que, al arrancar, verifica que BIOS y SO estén firmados por Google y puede firmar una declaración con el hash de lo arrancado; los servicios exigen esa declaración y la contrastan con una base de claves de chips y de hashes aceptados.

Contra **DoS** (botnets que saturan ancho de banda, CPU, memoria o estado de protocolo; es difícil distinguir ataque de tráfico real) se usan recursos masivos con balanceo, autenticar lo antes posible, gastar poco antes de autenticar, aislar los componentes que atienden solicitudes no autenticadas (GFE, login) y priorizar a los usuarios autenticados.

## Preguntas de repaso

> [!question]- ¿Por qué el audit log va fuera del recurso?
> Para que un atacante que comprometa el recurso no pueda borrar el rastro de lo que hizo.

> [!question]- ¿Cuándo conviene una ACL y cuándo una capacidad?
> La ACL para política duradera y para saber quién accede a un recurso; la capacidad para permisos temporales y delegables, como un ticket de corta duración, a costa de difícil revocación.

> [!question]- ¿Qué debilidad de la defensa perimetral corrige el enfoque de Google?
> Que dentro del perímetro todo se confía y no hay segunda línea de defensa; con un monitor por servicio, comprometer una máquina no da acceso a todo.
