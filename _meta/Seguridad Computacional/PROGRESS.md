# Progreso de la migración — Seguridad Computacional (IIC2531)

Rama: `migrar/seguridad-computacional`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Seguridad Computacional" --tema "<Tema>"` revisando el código de salida. Pausas de revisión: después del tema 1 (piloto), del 8 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + clases) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Seguridad Computacional/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos de seguridad | `01-Fundamentos de seguridad/` | ✅ hecho | 3 + índice | 0 + 1 |
| 2 | Buffer overflows y baggy bounds | `02-Buffer overflows y baggy bounds/` | ✅ hecho | 2 + índice | 3 + 1 |
| 3 | Autenticación de usuarios | `03-Autenticación de usuarios/` | ✅ hecho | 2 + índice | 0 + 0 |
| 4 | Arquitectura de seguridad de Google | `04-Arquitectura de seguridad de Google/` | ✅ hecho | 2 + índice | 2 + 0 |
| 5 | Separación de privilegios con OKWS | `05-Separación de privilegios con OKWS/` | ✅ hecho | 1 + índice | 0 + 1 |
| 6 | Contenedores y microVMs | `06-Contenedores y microVMs/` | ✅ hecho | 2 + índice | 0 + 1 |
| 7 | Sandboxing de software | `07-Sandboxing de software/` | ✅ hecho | 2 + índice | 0 + 1 |
| 8 | Seguridad móvil | `08-Seguridad móvil/` | ✅ hecho | 2 + índice | 0 + 1 |
| 9 | Ejecución simbólica | `09-Ejecución simbólica/` | ✅ hecho | 1 + índice | 0 + 1 |
| 10 | Seguridad web | `10-Seguridad web/` | ✅ hecho | 3 + índice | 0 + 1 |
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
- **2026-10-21 · Arquitectura de seguridad de Google.** Fuentes: `apuntes_i1` clases 3 y 4 (arquitectura de seguridad, aislamiento, VM, guardia, ACL y capacidades, monitor de referencia, canales seguros) y el texto de la clase 3 (`l02-google-es.md`) para el arranque seguro, DoS y defensa perimetral. Se mantuvo la observación del profesor sobre el detalle del diagrama del entorno. 2 notas; 2 imágenes de apuntes. Sin dudas.
- **2026-10-21 · Separación de privilegios con OKWS.** Sin apuntes propios. Construido con el texto de la clase de OKWS (`I05-okws-es.md`): plan B, componentes, daño y superficie de ataque, `dbproxy` con tokens, aislamiento con UID, GID y `chroot`, límites de UNIX y vigencia. Se dejaron fuera los detalles de la tabla de chroot y el orquestado por usuario. 1 nota; 1 figura de clase. Sin dudas.
- **2026-10-21 · Contenedores y microVMs.** Sin apuntes propios. Construido con los textos de las clases de contenedores Linux (`I06-linux-containers.md`) y Firecracker (`I06-firecracker-es.md`): VM frente a contenedor, namespaces, cgroups, capabilities con el ejemplo de `ping`, seccomp-bpf, Lambda, diseño de Firecracker, resultados y gVisor. 2 notas; 1 figura de clase. Sin dudas.
- **2026-10-21 · Sandboxing de software.** Sin apuntes propios. Construido con los textos de WebAssembly (`I07-wasm-es.md`) y RLBox (`I08-rlbox-es.md`). La figura `sfi.png` es una versión parcial de `sfi_wasm.png` y no se usa. 2 notas; 1 figura de clase. Sin dudas.
- **2026-10-21 · Seguridad móvil.** Sin apuntes propios. Construido con los textos de iOS (`I09-ios-es.md`) y Android (`I10-android-es.md`). Se resumieron las clases de protección, los permisos y las delegaciones. 2 notas; 1 figura de clase. Sin dudas.
- **2026-10-21 · Ejecución simbólica.** Sin apuntes propios. Construido con el texto de la clase de bugs y ejecución simbólica (`I11-exe-es.md`). 1 nota; 1 figura de clase. Sin dudas.
- **2026-10-21 · Seguridad web.** Sin apuntes propios. Construido con los textos de seguridad web (`l12-web-security-es.md`) y ataques web más comunes (`l13-top-web-attacks-es.md`). Se resumieron las categorías de OWASP en una tabla. 3 notas; 1 figura de clase. Sin dudas.
