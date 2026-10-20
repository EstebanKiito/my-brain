---
ramo: "Sistemas Distribuidos"
tema: "Gestión del curso"
tags:
  - sd/gestion
  - origen/complemento
prerrequisitos:
  - "[[01 - Confiabilidad y sus propiedades]]"
  - "[[05 - Consistencia eventual]]"
  - "[[03 - Replicación primaria y replicación activa]]"
---

# Síntesis de fiabilidad y seguridad

Repaso integrado de la segunda unidad: tolerancia a fallos, consistencia, replicación, transacciones, concurrencia, CAP y PACELC, y la introducción a la seguridad y el cifrado. Cada punto remite a su nota, donde está el detalle.

## Qué entra

Tolerancia a fallos; consistencia centrada en los datos y en el cliente; protocolos de replicación; transacciones distribuidas; control de concurrencia; teoremas CAP y PACELC; introducción a la seguridad y cifrado de mensajes.

## Tolerancia a fallos

- Confiabilidad = disponibilidad + fiabilidad + seguridad + mantenibilidad ([[01 - Confiabilidad y sus propiedades|Confiabilidad]]).
- **Falla → error → fracaso:** un string donde se esperaba un int (falla) provoca una excepción (error) y la operación no se completa (fracaso) ([[02 - Fallo, error y fracaso|Fallo, error y fracaso]]).
- Detección: sondas (activo), latidos (pasivo) y timeouts. Enmascaramiento con redundancia de hardware, información, tiempo y software ([[03 - Detección de fallos y redundancia|Detección y redundancia]]).

## Consistencia

![Síntesis de consistencia secuencial](adjuntos/S%C3%ADntesis%20de%20consistencia%20secuencial.png)

> [!example]- Transcripción de la imagen
> A escribe $x=2$ y F escribe $x=5$. Izquierda: H y S leen 5 y luego 2. Derecha: H y S leen 2 y luego 5. Ambas son secuenciales: todos ven el mismo orden.

**Secuencial:** todos ven la misma secuencia; solo se evalúa lo visible. Ver [[02 - Consistencia secuencial|Consistencia secuencial]].

![Síntesis de consistencia fuerte](adjuntos/S%C3%ADntesis%20de%20consistencia%20fuerte.png)

> [!example]- Transcripción de la imagen
> A: $W_A(x)=1$, $W_A(y)=1$, $R_A(x)$; F: $W_F(y)=2$, $W_F(x)=2$, $R_F(y)$. Como $W_A(x)=1$ y $W_F(y)=2$ se superponen, solo hay 2 secuencias válidas: partir con $W_A(x)=1$ o con $W_F(y)=2$.

**Fuerte:** además respeta el tiempo real, con propagación inmediata. Ver [[03 - Consistencia fuerte o linealizable|Consistencia fuerte]].

![Síntesis de consistencia causal](adjuntos/S%C3%ADntesis%20de%20consistencia%20causal.png)

> [!example]- Transcripción de la imagen
> A escribe $x=2$ y luego $x=5$. F lee 2 y escribe 9. H lee 2, 5, 9 y S lee 2, 9, 5. "Nodo F escribe 9 después de leer 2: ningún nodo puede leer 9 antes de 2."

**Causal:** si se lee $x$ y luego se escribe $y$, nadie puede ver $y$ antes que $x$. Ver [[04 - Consistencia causal|Consistencia causal]].

![Síntesis de consistencia eventual](adjuntos/S%C3%ADntesis%20de%20consistencia%20eventual.png)

> [!example]- Transcripción de la imagen
> A escribe 2, lee 9 y escribe 5. F lee 2, escribe 9 y lee 5. H lee 2, 9 y 5; S lee 9, 2 y 5. "Todos los nodos tienen finalmente el mismo valor (x=5)."

**Eventual:** todos terminan con el mismo valor. Si algún nodo ve un valor final distinto, o no hay una lectura final que lo demuestre, no se puede afirmar. Ver [[05 - Consistencia eventual|Consistencia eventual]].

**En el cliente:** monotonic reads, read your writes, monotonic writes y writes follow reads. Ayuda pensar las réplicas como el celular y el computador con la misma cuenta. Ver [[02 - Garantías de sesión|Garantías de sesión]].

## Replicación

![Síntesis de gossip](adjuntos/S%C3%ADntesis%20de%20gossip.png)

> [!example]- Transcripción de la imagen
> Una red de nodos; `Write(A) = 5` entra por un extremo y se propaga de vecino en vecino; `Read(A)` se hace en otro extremo.

**Gossip:** cada nodo propaga cuando puede; no sirve para consistencia fuerte, pero todos terminan con la misma información. **Quórum:** se pregunta a varios para dar con el más actualizado.

![Síntesis de replicación con primario](adjuntos/S%C3%ADntesis%20de%20replicaci%C3%B3n%20con%20primario.png)

> [!example]- Transcripción de la imagen
> `Write(A) = 5` y `Read(A)` llegan a un nodo central que replica hacia cinco respaldos.

**Basado en primario:** el servidor central procesa y propaga a los respaldos, uno por uno o solo el estado final; las lecturas pueden ir directo a los respaldos para repartir la carga.

![Síntesis de replicación activa](adjuntos/S%C3%ADntesis%20de%20replicaci%C3%B3n%20activa.png)

> [!example]- Transcripción de la imagen
> Seis nodos conectados todos con todos; `Write(A) = 5` entra por uno y `Read(A)` por otro.

**Replicación activa (TOM):** cualquier nodo recibe las operaciones, que se ordenan globalmente; puede empaquetar varias acciones. Ver [[03 - Replicación primaria y replicación activa|Replicación primaria y activa]].

## Transacciones y concurrencia

- **ACID:** todos aceptan o todos rechazan; de un estado válido a otro (sin saldos negativos); cada transacción vive aislada; tras el commit no se puede revertir, solo compensar con otra transacción. Ver [[02 - Propiedades ACID en transacciones distribuidas|ACID distribuido]].
- **2PC:** primero se reservan los recursos y luego se consolida; si cae quien coordina, los participantes quedan bloqueados. **3PC:** agrega un pre-aviso para que los participantes decidan entre ellos. Ver [[03 - Commit de dos fases|2PC]] y [[04 - Commit de tres fases|3PC]].

![Síntesis de validación forward y backward](adjuntos/S%C3%ADntesis%20de%20validaci%C3%B3n%20forward%20y%20backward.png)

> [!example]- Transcripción de la imagen
> Tabla: forward validation valida $T_v$ contra las transacciones **activas**, revisando sus **escrituras**, para no invalidar lecturas futuras; backward validation valida contra las **ya consolidadas**, revisando sus **lecturas**, para asegurar que fueron válidas.

**Optimista:** forward mira las transacciones que van a hacer commit; backward mira el pasado y aborta si un commit ya lo afectó. Ver [[02 - Control pesimista y optimista|Control pesimista y optimista]].

## CAP, PACELC y seguridad

- Ante una partición: consistencia o disponibilidad; sin partición: latencia o consistencia ([[02 - Teorema PACELC|PACELC]]).
- Pilares (confidencialidad, integridad y disponibilidad), modelo del enemigo y ataques ([[02 - Métodos de ataque y medidas de seguridad|Ataques y medidas]]); cifrado simétrico, asimétrico y firmas ([[02 - Cifrado asimétrico, hash y firmas digitales|Cifrado asimétrico y firmas]]).

## Preguntas de repaso

> [!question]- ¿Qué distingue a la consistencia fuerte de la secuencial en una frase?
> La fuerte además respeta el orden de tiempo real; la secuencial solo exige que todos vean el mismo orden.

> [!question]- ¿Qué problema de 2PC resuelve 3PC?
> El bloqueo de los participantes cuando el coordinador cae después de la votación: con el pre-commit pueden decidir entre ellos.

> [!question]- ¿Por qué gossip no garantiza consistencia fuerte?
> Porque las escrituras se propagan perezosamente y en orden arbitrario: una lectura puede ver un valor antiguo hasta que la novedad llegue.
