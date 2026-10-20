---
ramo: "Sistemas Distribuidos"
tema: "Fundamentos de sistemas distribuidos"
tags:
  - sd/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[04 - Objetivos de un sistema distribuido]]"
---

# Tipos de sistemas distribuidos

No todos los sistemas distribuidos se reparten por el mismo motivo. El curso los clasifica según el **uso principal de la red**: calcular rápido, integrar sistemas o rodear al usuario de dispositivos. Los límites no son estrictos y las combinaciones son comunes; lo importante es reconocer qué uso domina.

| Tipo | Uso principal | Subtipos |
|---|---|---|
| **Computación distribuida de alto rendimiento** (HPC) | Procesar mucha información en un tiempo acotado | Clúster, grid |
| **Sistemas de información distribuidos** | Interoperar entre sistemas distintos | Integración de aplicaciones, transacciones distribuidas |
| **Sistemas pervasivos** | Integrarse de forma natural en el entorno | Ubicuos, móviles, redes de sensores |

## Computación de alto rendimiento

### Clúster

Un **clúster** es una colección de nodos de cómputo **similares**, en un mismo lugar e interconectados por una red de alta velocidad. Se usa para **programación paralela**: un programa intensivo en cómputo se ejecuta en paralelo en muchas máquinas. Un nodo responsable recolecta los trabajos de los usuarios y reparte las tareas entre los nodos de cómputo; **Slurm** es el programa más usado para esto. Si un nodo de ejecución se cae, los demás siguen computando.

![Clúster con scheduler y nodos de ejecución](adjuntos/Cl%C3%BAster%20con%20scheduler%20y%20nodos%20de%20ejecuci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Dos usuarios envían *user requests* a un *Scheduler*, que guarda los trabajos en una cola (*queued jobs*) y los reparte a *Exec node 1* … *Exec node n*. Los nodos de ejecución y el *Storage* están unidos por una *high speed network*.

### Grid

Un **grid** es un sistema distribuido **de clústeres**: varios clústeres separados (en distintos lugares y servidores) que se organizan para actuar como una única entidad. Sobre los responsables de cada clúster se agrega una **capa adicional** que se comunica con todos y unifica la información. Se usa para aumentar el rendimiento al entrenar modelos y repartir carga, y también para garantizar privacidad, porque cada clúster puede quedarse con sus datos.

![Grid como capa sobre varios clústeres](adjuntos/Grid%20como%20capa%20sobre%20varios%20cl%C3%BAsteres.png)

> [!example]- Transcripción de la imagen
> Cuatro pasos con un *model-server* y tres *workers* (a, b y c):
> 1. El servidor tiene el modelo y los workers están vacíos.
> 2. *Model Sync*: el servidor envía una copia del modelo a cada worker.
> 3. Cada worker ajusta su copia con sus propios datos (puntos distintos en cada uno).
> 4. *Upload*: los workers suben sus modelos y el servidor los promedia (*Average*).

> [!tip] Clúster frente a grid
> **Clúster:** muchos computadores parecidos en un mismo lugar. **Grid:** muchos clústeres en lugares distintos, coordinados por una capa superior.

## Sistemas de información distribuidos

Se centran en la **operabilidad** entre sistemas distintos dentro de organizaciones con muchas aplicaciones en red. Tienen dos usos no excluyentes:

- **Integración de aplicaciones empresariales:** un intermediario (*middleware*) conecta aplicaciones que no fueron hechas para hablar entre sí.
- **Procesamiento de transacciones distribuidas:** se garantiza que todas las solicitudes de una operación se ejecuten, o ninguna (la misma idea de atomicidad de [[02 - Propiedades ACID|ACID]], pero entre varias máquinas).

El correo electrónico ilustra ambos usos:

- **Integración:** la comunicación es asíncrona y persistente gracias a una cola. Se puede enviar desde cualquier gestor y el destinatario no necesita estar conectado para recibir el mensaje.
- **Transacción:** enviar un correo (solicitud 1) y que llegue al destinatario (solicitud 2) forman una unidad. Si no ocurren ambas, el envío "rebota".

![Gestores de correo que interoperan](adjuntos/Gestores%20de%20correo%20que%20interoperan.png)

> [!example]- Transcripción de la imagen
> Logos de diez gestores de correo: Gmail, Outlook, Yahoo!, ProtonMail, AOL Mail, Zoho, GMX, iCloud, Yandex y mail.com. Todos intercambian correos entre sí aunque sean sistemas distintos.

## Sistemas pervasivos

Están formados por dispositivos variados que se integran de forma natural en el entorno. La literatura distingue tres grupos no excluyentes:

- **Computación ubicua:** el sistema está siempre presente y el usuario interactúa con él de forma implícita, a menudo sin darse cuenta. Ejemplos: Smart TV, asistentes de voz como Alexa o Google Home.
- **Computación móvil:** dispositivos que se mueven y usan comunicación inalámbrica para acceder a servicios remotos; su desafío es mantener la conectividad. Ejemplos: celulares, tarjetas inteligentes.
- **Redes de sensores:** muchos nodos sensores que colaboran y procesan los datos **lo más cerca posible de la fuente**, para reducir tráfico de red y consumo de energía. Ejemplos: alarmas de humo, sensores de temperatura, sistemas de riego.

Sea cual sea su tipo, se espera que el sistema cumpla con los seis [[04 - Objetivos de un sistema distribuido|objetivos de un sistema distribuido]].

## Preguntas de repaso

> [!question]- ¿Por qué un grid puede ayudar a la privacidad y un clúster no tanto?
> En un grid cada clúster puede quedarse con sus datos y compartir solo resultados (como modelos entrenados), que la capa superior combina. En un clúster todos los nodos están en un mismo lugar bajo un mismo responsable, que reparte también los datos.

> [!question]- ¿Por qué una red de sensores procesa los datos cerca de la fuente?
> Porque enviar todas las lecturas a un servidor central consume ancho de banda y energía, que son escasos en sensores. Filtrar o agregar localmente reduce lo que viaja por la red.

> [!question]- ¿Qué parte del envío de un correo corresponde a integración y cuál a transacción?
> La integración es que gestores distintos se entiendan y que el mensaje espere en una cola aunque el destinatario no esté conectado. La transacción es que el envío y la recepción ocurran ambos o ninguno; si falla la entrega, el correo rebota.
