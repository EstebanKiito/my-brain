---
ramo: "Sistemas Distribuidos"
tema: "Tolerancia a fallos"
tags:
  - sd/tolerancia-a-fallos
  - origen/complemento
prerrequisitos:
  - "[[02 - Fallo, error y fracaso]]"
---

# Detección de fallos y redundancia

Para tolerar una falla hay dos estrategias complementarias: **detectarla** (saber que un nodo cayó y reaccionar) o **enmascararla** (que el sistema siga dando la respuesta correcta sin necesidad de saber qué falló). La segunda se basa en una sola idea: tener más de lo estrictamente necesario, es decir, **redundancia**.

## Detección de fallos (*failure detection*)

| Mecanismo | Tipo | Cómo funciona |
|---|---|---|
| **Sondas** (*probes*) | Activo | Se envían mensajes "¿sigues vivo?" (como un *ping*); si no hay respuesta, se sospecha falla |
| **Latidos** (*heartbeats*) | Pasivo | Se esperan mensajes periódicos del otro nodo; funciona solo si el canal de comunicación es bueno |
| **Tiempos de espera** (*timeouts*) | – | Cada mensaje tiene un tiempo máximo de respuesta; si no se cumple, se sospecha falla. Aunque un mensaje no requiera respuesta, se puede exigir un `ACK` |

Estos mecanismos detectan **que** algo falló, pero no **qué tipo** de falla fue.

![Desafíos de la detección de fallos](adjuntos/Desaf%C3%ADos%20de%20la%20detecci%C3%B3n%20de%20fallos.png)

> [!example]- Transcripción de la imagen
> En sistemas sin límites en la velocidad de ejecución ni en el retraso de los mensajes, un timeout solo indica que un proceso no responde, pero no si se bloqueó, está lento o se perdió el mensaje. Esto puede generar falsos positivos (creer que el nodo falló cuando fue la red). Por eso existen mecanismos "eventualmente perfectos" que se adaptan al sistema: ajustar el timeout para cada nodo, o enviar más de una petición para asegurar que al menos un mensaje llegue o para contrastar respuestas.

> [!warning] Falsos positivos
> Un timeout no prueba que el nodo cayó. Declarar muerto a un nodo vivo puede ser tan dañino como no detectar uno caído: por ejemplo, dos nodos podrían creerse líderes.

## Enmascaramiento de fallos (*failure masking*)

Un sistema tolerante a fallos sigue ejecutando correctamente sus tareas en presencia de fallos de hardware o software; su objetivo es que los fallos **no generen un fracaso**. La herramienta es la **redundancia**: agregar información, recursos o tiempo más allá de lo necesario. Tiene costo: puede afectar el rendimiento, el tamaño, el peso y el consumo de energía.

### Redundancia de hardware

- **Enfoque pasivo:** se **ignora** la falla. Con **TMR** (*Triple Modular Redundancy*) se triplica el hardware y se **vota** la salida; el quórum elige, idealmente, la respuesta correcta sin averiguar qué módulo falló. Se extiende a $N$ módulos ($N$ impar) para tolerar más fallas simultáneas.
- **Enfoque activo:** se **detecta** el componente fallado y se repara o reemplaza. En *standby sparing* hay módulos de respaldo (*spares*): en **hot standby** operan en sincronía, listos para tomar el control de inmediato; en **cold standby** están apagados hasta que se necesitan.

```python
from collections import Counter
def tmr(*salidas):
    return Counter(salidas).most_common(1)[0][0]
tmr(42, 42, 17)   # → 42: el módulo que respondió 17 queda en minoría
```

### Redundancia de información

Se agrega información a los datos para **detectar** y/o **reconstruir** el dato:

- **Código duplicado:** toda la información se guarda $N$ veces.
- **Checksum:** un bloque con la suma de todos los bytes (hay distintas fórmulas para sumar). Detecta errores, pero no los corrige.
- **Código Hamming:** agrega bits de paridad que permiten detectar y **corregir** un bit erróneo. En Python, el código Hamming(7,4) de `[1,0,1,1]` con el bit 5 invertido se corrigió al dato original (el síndrome indicó la posición 5).
- **Reed-Solomon:** trata los datos como polinomios y agrega símbolos redundantes que permiten reconstruir los datos aunque se pierda o dañe una parte (lo usan los CD, los códigos QR y los sistemas RAID).

### Redundancia de tiempo

Ahorra hardware a cambio de **tiempo**: se repite la misma operación dos o más veces y se comparan los resultados; si difieren, se repite para ver si el error desaparece, y se puede votar entre ejecuciones. Sirve para fallos transitorios. Para detectar fallos permanentes se ejecutan operaciones de resultado conocido.

### Redundancia de software

El nodo ejecuta más programas o procesos para asegurar el funcionamiento correcto: pruebas que verifican el estado del sistema (memoria, ALU) o las mismas técnicas de hardware, pero con procesos: varios procesos concurrentes que votan la respuesta, o procesos de respaldo.

> [!tip] Resumen
> Hardware: más componentes. Información: más bits. Tiempo: más ejecuciones. Software: más procesos. Las cuatro cambian recursos por la capacidad de ocultar fallas.

## Preguntas de repaso

> [!question]- ¿Por qué TMR usa un número impar de módulos?
> Para que la votación nunca empate. Con 3 módulos, una falla queda en minoría 2 a 1; con un número par podría quedar 2 a 2.

> [!question]- ¿Puede la redundancia de información reparar un mensaje dañado?
> Sí, si se usa un código corrector como Hamming o Reed-Solomon. Un checksum, en cambio, solo detecta que el mensaje está dañado.

> [!question]- ¿Qué diferencia hay entre hot y cold standby sparing?
> En hot standby los repuestos funcionan en sincronía con los módulos activos y toman el control al instante. En cold standby están apagados: gastan menos energía, pero tardan más en reemplazar al módulo fallado.
