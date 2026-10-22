# Seguridad Computacional (IIC2531) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto de forma breve**: basta con buscar el concepto, sin saber en qué clase se vio. El curso es de amplitud, así que las notas son cortas y se quedan con lo necesario para entender cada caso. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` y `prerrequisitos` (notas que conviene leer antes).
- **Cuerpo:** explicación breve que parte por el problema que resuelve cada mecanismo, con tablas y algún diagrama.
- **Otros ramos:** lo que está en otro ramo se enlaza en vez de repetirse: criptografía y Kerberos en [[Sistemas Distribuidos/_Índice|Sistemas Distribuidos]]; HTTP, XSS y autenticación web en [[Tecnologías y Aplicaciones Web/_Índice|Tecnologías y Aplicaciones Web]]; inyección SQL en [[Bases de Datos/_Índice|Bases de Datos]]; TCP, DNS, contenedores y memoria en [[Sistemas Operativos y Redes/_Índice|Sistemas Operativos y Redes]].
- **Imágenes:** figuras de apuntes y de clase en PNG, con su transcripción en un callout plegable.
- **Cierre:** cada nota termina con tres preguntas de repaso con la respuesta oculta.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Seguridad Computacional/01-Fundamentos de seguridad/_Índice\|Fundamentos de seguridad]] | Objetivo, modelo de amenaza, política y mecanismo; tríada CIA; fallos típicos y defensa en profundidad |
| [[Seguridad Computacional/02-Buffer overflows y baggy bounds/_Índice\|Buffer overflows y baggy bounds]] | Desbordes en stack y heap, NX, canarios, ASLR y verificación de límites |
| [[Seguridad Computacional/03-Autenticación de usuarios/_Índice\|Autenticación de usuarios]] | Contraseñas, salt, KDF, 2FA, TOTP y U2F |
| [[Seguridad Computacional/04-Arquitectura de seguridad de Google/_Índice\|Arquitectura de seguridad de Google]] | Aislamiento, monitor de referencia, ACL y capacidades, canales seguros y arranque seguro |
| [[Seguridad Computacional/05-Separación de privilegios con OKWS/_Índice\|Separación de privilegios con OKWS]] | Partición de un servidor web, `dbproxy` y aislamiento con UNIX |
| [[Seguridad Computacional/06-Contenedores y microVMs/_Índice\|Contenedores y microVMs]] | Namespaces, cgroups, capabilities, seccomp, Firecracker y gVisor |
| [[Seguridad Computacional/07-Sandboxing de software/_Índice\|Sandboxing de software]] | WebAssembly, aislamiento de fallas de software y RLBox |
| [[Seguridad Computacional/08-Seguridad móvil/_Índice\|Seguridad móvil]] | iOS (arranque seguro, enclave, cifrado) y Android (intents y permisos) |
| [[Seguridad Computacional/09-Ejecución simbólica/_Índice\|Ejecución simbólica]] | Fuzzing, EXE, restricciones de camino y ejecución concólica |
| [[Seguridad Computacional/10-Seguridad web/_Índice\|Seguridad web]] | Política del mismo origen, cookies, CSRF, XSS, clickjacking y OWASP Top 10 |
| [[Seguridad Computacional/11-Seguridad TCP-IP/_Índice\|Seguridad TCP-IP]] | Números de secuencia, IP falsificada, DNS, SYN flooding, amplificación, ARP, DHCP y BGP |
| [[Seguridad Computacional/12-TLS y certificados/_Índice\|TLS y certificados]] | Canal seguro, handshake, ataques a SSL, CA, Certificate Transparency y revocación |
| [[Seguridad Computacional/13-Mensajería segura/_Índice\|Mensajería segura]] | Extremo a extremo, confianza en claves, secreto hacia adelante, negabilidad y metadatos |
| [[Seguridad Computacional/14-DDoS y cadena de suministro/_Índice\|DDoS y cadena de suministro]] | Reflexión y amplificación, defensas, y ataques a dependencias npm |
| [[Seguridad Computacional/15-SDLC seguro/_Índice\|SDLC seguro]] | Shift left, DevSecOps, STRIDE, respuesta a incidentes y metodologías |
| [[Seguridad Computacional/16-Gestión del curso/_Índice\|Gestión del curso]] | Contenidos, evaluaciones y materia por evaluación |

## Ruta de estudio sugerida
1. **Fundamentos → Buffer overflows → Autenticación:** el vocabulario de amenazas y los primeros mecanismos.
2. **Arquitectura de Google → OKWS → Contenedores → Sandboxing:** aislamiento y separación de privilegios, de procesos a microVMs y WebAssembly.
3. **Seguridad móvil → Ejecución simbólica:** diseños completos y cómo encontrar bugs.
4. **Seguridad web → TCP-IP → TLS → Mensajería:** de la web a la red y a la criptografía aplicada.
5. **DDoS y cadena de suministro → SDLC seguro:** disponibilidad, dependencias y seguridad en el ciclo de desarrollo.
6. **Gestión del curso:** evaluaciones y materia de cada una.
