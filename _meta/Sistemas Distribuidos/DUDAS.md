# Dudas y posibles errores en los apuntes originales — Sistemas Distribuidos (IIC2523)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Procesos e hilos en Python
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[05 - Mecanismos de sincronización entre threads\|Mecanismos de sincronización entre threads]] | Imagen de join de los apuntes: `T1.join()` y `T2.join(timeout=N)` | Thread 1 espera a Thread 2 y luego a Thread 3, así que las llamadas son `T2.join()` y `T3.join(timeout=N)`, como en la versión corregida de las slides. La nota usa esa versión. |

## Comunicación directa y sockets
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Protocolos de transporte TCP y UDP\|Protocolos de transporte TCP y UDP]] | Apuntes y slides: UDP "manda paquetes de máximo 64Kb" | El límite es de 64 KB (kilobytes: 65 535 bytes de datagrama, unos 65 507 de datos), no de 64 kilobits. La nota dice 64 KB. |
| ℹ️ | [[04 - Protocolos de aplicación DNS y HTTP\|Protocolos de aplicación DNS y HTTP]] | Petición HTTP de ejemplo con la línea `Remote Address: 185.178.208.140:443` | `Remote Address` lo muestran las herramientas del navegador, pero no es una cabecera HTTP: es la IP y el puerto de la conexión TCP. La nota lo saca del mensaje y lo explica aparte. |
