# Progreso de la migración — Seguridad Computacional (IIC2531)

Rama: `migrar/seguridad-computacional`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Seguridad Computacional" --tema "<Tema>"` revisando el código de salida. Pausas de revisión: después del tema 1 (piloto), del 8 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + clases) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Seguridad Computacional/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de seguridad | `01-Fundamentos de seguridad/` | ✅ hecho | 3 + índice | 0 + 1 |
| 2 | Buffer overflows y baggy bounds | `02-Buffer overflows y baggy bounds/` | ✅ hecho | 2 + índice | 3 + 1 |
| 3 | Autenticación de usuarios | `03-Autenticación de usuarios/` | ✅ hecho | 2 + índice | 0 + 0 |
| 4 | Arquitectura de seguridad de Google | `04-Arquitectura de seguridad de Google/` | ⏳ pendiente | – | – |
| 5 | Separación de privilegios con OKWS | `05-Separación de privilegios con OKWS/` | ⏳ pendiente | – | – |
| 6 | Contenedores y microVMs | `06-Contenedores y microVMs/` | ⏳ pendiente | – | – |
| 7 | Sandboxing de software | `07-Sandboxing de software/` | ⏳ pendiente | – | – |
| 8 | Seguridad móvil | `08-Seguridad móvil/` | ⏳ pendiente | – | – |
| 9 | Ejecución simbólica | `09-Ejecución simbólica/` | ⏳ pendiente | – | – |
| 10 | Seguridad web | `10-Seguridad web/` | ⏳ pendiente | – | – |
| 11 | Seguridad TCP-IP | `11-Seguridad TCP-IP/` | ⏳ pendiente | – | – |
| 12 | TLS y certificados | `12-TLS y certificados/` | ⏳ pendiente | – | – |
| 13 | Mensajería segura | `13-Mensajería segura/` | ⏳ pendiente | – | – |
| 14 | DDoS y cadena de suministro | `14-DDoS y cadena de suministro/` | ⏳ pendiente | – | – |
| 15 | SDLC seguro | `15-SDLC seguro/` | ⏳ pendiente | – | – |
| 16 | Gestión del curso | `16-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md), pero **cortas y concisas** por pedido del usuario: de 30 a 70 líneas, solo lo necesario para entender cada concepto, con 3 preguntas de repaso plegables.
- Los apuntes propios casi no existen; las notas mezclan lo poco que hay (clases 1-6 en `apuntes_i1`) con los textos de `Classes/` y se guían por los resúmenes de `Skibidi-Seguridad/` (`Resumen-I1.pdf`: clases 1-6 y SDLC seguro; `Resumen-I2.pdf`: Firecracker, WebAssembly, RLBox, iOS, Android, EXE, seguridad web, OWASP, TCP/IP y TLS). Las clases 17-20 (certificados, mensajería, DDoS, npm) no están en los resúmenes: se tratan como contenido del examen y quedan más breves.
- Los PDF y textos de clase no se suben al repo: solo las figuras útiles, como PNG en `adjuntos/` y registradas con `tipo: "clase"`.
- Otros ramos: se enlaza en vez de duplicar (criptografía, TLS y Kerberos en Sistemas Distribuidos; HTTP, XSS, CSRF y SQL injection en Tecnologías y Aplicaciones Web y Bases de Datos; TCP, DNS, contenedores y VM en Sistemas Operativos y Redes).

## Registro
- **2026-10-21 · Fundamentos de seguridad.** Fuentes: `apuntes_i1` clase 1 completa y `resumen_i1` (objetivo, amenaza, política, mecanismo, CIA, defensa en profundidad, ejemplos de política, modelo y bugs) complementados con el texto de la clase 1 (`I01-intro-es.md`): Fairfax, Mat Honan, Palin, CAPTCHA, XcodeGhost, DES en Kerberos, iCloud, Citigroup y Debian. Se omitieron las presentaciones del equipo docente. 3 notas; 1 figura de clase. Sin dudas.
- **2026-10-21 · Buffer overflows y baggy bounds.** Fuentes: `apuntes_i1` clases 2 y 6 (recordatorios de C, stack y heap, gdb, NX, canarios, ASLR, ataque al heap) con el texto de la clase 2 (`I02-baggy-es.md`) para baggy bounds y punteros gordos. Se resumió el recorrido con gdb. 2 notas; 3 imágenes de apuntes y 1 figura de clase. Sin dudas.
- **2026-10-21 · Autenticación de usuarios.** Sin apuntes propios (solo menciones en la clase 1). Construido con el texto de la clase de autenticación (`I03-aut-es.md`): guardia, tres partes, contraseñas y entropía, gestores, límite de intentos, hash, salt, KDF, SMS, TOTP y U2F con sus dos problemas. Se omitió la lista de referencias. 2 notas; sin imágenes. Sin dudas.
