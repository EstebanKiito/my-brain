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

## Invocación remota
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - gRPC y Protocol Buffers\|gRPC y Protocol Buffers]] | Slide de Protocol Buffers: esquema `message Character { string username = ""; string phase = ""; }` e `import character_pb3` | En proto3 cada campo lleva un número de campo (`string username = 1;`); con `= ""` `protoc` falla con "Expected field number". Además, el módulo generado para Python se llama `character_pb2` aunque el esquema sea proto3. La nota usa la versión que compila (y `phrase` en vez de `phase`). |

## Consenso
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Casos borde y garantías de Paxos\|Casos borde y garantías de Paxos]] | Slide "Ejemplo 2. Sobreescribir acción que tenía consenso" | Lo que tuvo consenso fue el `prepare(1)` (los tres aceptantes prometieron), pero la operación $A_1$ solo la aceptó un nodo y nunca alcanzó mayoría. La nota lo explica así, en línea con la observación de las slides: un prepare con consenso no asegura que su operación sea la final. |

## Elección de líder
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Casos de votación en Raft\|Casos de votación en Raft]] | Imágenes de los casos 2 y 4: el votante dice "Tu term actual es menor al mío. ¡Rechazado!" | Tras postularse, el candidato sube su term: en el caso 4 queda en 2, igual al del votante, así que la regla 1 no aplica. El rechazo se justifica por la regla 3c (el último log del candidato es de un term menor). En el caso 2 pasa lo mismo con el votante de term 1. El resultado no cambia; la nota explica ambas reglas. |

## Exclusión mutua distribuida
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Multicast de Ricart y Agrawala\|Multicast de Ricart y Agrawala]] | Apuntes, bajo "Algoritmo 3: Ricart y Agrawala": "Todavia no se creaban los relojes logicos" | Los relojes lógicos de Lamport son de 1978 y el algoritmo de Ricart y Agrawala, de 1981; además, las slides indican que usa relojes lógicos para el orden total. La nota sigue a las slides. |

## Replicación y modelos de consistencia
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[02 - Consistencia secuencial\|Consistencia secuencial]] | Apuntes: "Propuesta por Chandy Lamport (otra vez xD)" | La consistencia secuencial la definió Leslie Lamport en 1979, como indican las slides; Chandy no participó (con Lamport firmó el algoritmo de snapshots). La nota dice Lamport, 1979. |

## Transacciones distribuidas
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Commit de tres fases\|Commit de tres fases]] | Pregunta de las slides: "IV. El protocolo 3PC garantiza la atomicidad" marcada como correcta | Es cierto bajo los supuestos del protocolo (fallas por caída, red sin particiones). En la literatura se señala que, con particiones de red, 3PC puede dejar a dos grupos con decisiones distintas. La nota respeta la respuesta del curso y menciona la limitación. |

## Control de concurrencia distribuido
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[02 - Control pesimista y optimista\|Control pesimista y optimista]] | Ejemplo de control pesimista, paso 5: "T2 hace commit y 'Lock' Z" | Por el paso siguiente (T3 puede tomar Z), al hacer commit T2 **libera** el lock de Z. La transcripción y la nota dicen "libera". |

## Teoremas CAP y PACELC
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - Teorema PACELC\|Teorema PACELC]] | Pregunta del banco global: la slide marca **PC/EC** | El enunciado dice que, sin partición, la réplica local responde con saldos posiblemente atrasados por la sincronización periódica: eso prioriza la latencia (EL), no la consistencia. La respuesta coherente parece PC/EL. La nota explica ambas y menciona la discrepancia. Conviene confirmarlo con el material o el equipo docente. |
