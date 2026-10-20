---
ramo: "Sistemas Distribuidos"
tema: "Monitoreo de seguridad"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Objetivos, desafíos y ciclo del monitoreo]]"
---

# Mecanismos de monitoreo y consideraciones legales

El monitoreo se implementa con herramientas concretas que se diferencian en **dónde** miran (la red o un servidor), **cómo** analizan (firmas o anomalías) y **qué hacen** al detectar algo (alertar o bloquear). Y como vigilar implica registrar lo que hacen los usuarios, también está acotado por la ley.

## Mecanismos

### IDS (sistema de detección de intrusos)

Detecta actividades no autorizadas, **sin intervenir**: alerta. Se clasifica por tipo de análisis y por ubicación.

| Por análisis | Signature-based IDS | Anomaly-based IDS |
|---|---|---|
| Detecta | Ataques conocidos | Comportamientos anómalos, incluso desconocidos |
| Requiere | Una base de patrones | Entrenamiento con datos normales |
| Falsos positivos | Pocos | Puede tener muchos si el modelo está mal entrenado |
| Limitación | No detecta ataques nuevos (*zero-day*) | – |

| Por ubicación | HIDS (*host-based*) | NIDS (*network-based*) |
|---|---|---|
| Analiza | Un servidor: logs, llamadas al sistema, integridad de archivos | La comunicación: paquetes en tiempo real |
| Detecta | Ataques internos o posteriores a la intrusión | Ataques en tránsito o intentos de intrusión |

### CIDS (IDS colaborativo)

Una colección de IDS que **comparten** detecciones y análisis. Los dispositivos se agrupan en **comunidades**, cada una con un **líder** que reúne y analiza los datos de sus miembros; las comunidades pueden superponerse.

### IPS (sistema de prevención de intrusos)

Un IDS con capacidad de **intervenir**: detecta y bloquea. Se clasifica igual: NIPS (red), HIPS (servidor), por anomalías o por firmas. Actúa rápido, pero un falso positivo **bloquea** una acción legítima.

### Firewall

Hardware o software que **filtra el tráfico** entre zonas de red: permite o bloquea puertos, IPs y protocolos, de entrada y de salida. Es la **primera línea de defensa**.

- **Filtrado de paquetes:** opera a nivel de red (como un router) y decide según las direcciones de origen y destino del encabezado IP.
- **Pasarela de aplicación:** inspecciona el contenido de los mensajes, según el protocolo (HTTP, SQL, DNS).
- Por ubicación: **perimetral** (entre la LAN e Internet), **por servidor** (reglas locales, como Windows Defender Firewall) o **distribuido** (definido por software, con políticas por componente).

![Firewall frente a IDS e IPS](adjuntos/Firewall%20frente%20a%20IDS%20e%20IPS.png)

> [!example]- Transcripción de la imagen
> Tres diagramas de red entre un hacker, Internet y una red corporativa: el firewall se ubica en el borde; el IDS está conectado al costado, observando; el IPS está en línea, entre el firewall y el router. Resumen: **Firewall**, primera línea de defensa que filtra tráfico según reglas; **IDS**, detecta actividades sospechosas pero no interviene; **IPS**, detecta y bloquea amenazas en tiempo real.

> [!tip] Se combinan
> Nada obliga a elegir entre IDS e IPS: por ejemplo, un IPS por firmas bloquea lo conocido y un IDS por anomalías alerta sobre lo raro, sin el riesgo de bloquear acciones legítimas.

## Consideraciones legales

Monitorear implica registrar las acciones de los usuarios, que pueden sentir vulnerada su privacidad. Hace falta un marco regulatorio que defina cómo y hasta dónde se puede monitorear.

El **GDPR**, el Reglamento General de Protección de Datos de la Unión Europea, establece la privacidad como un **derecho fundamental**. Sus objetivos son proteger los datos personales contra accesos no autorizados, dar al usuario control (acceso, corrección y eliminación de sus datos) y transparencia en su uso. Ver [[Tecnologías y Aplicaciones Web/21-Privacidad y ética/_Índice|Privacidad y ética]].

Para cumplirlo, los sistemas de monitoreo suelen:

- guardar solo lo estrictamente necesario (**minimización**);
- anonimizar o seudonimizar los datos personales;
- registrar solo metadatos relevantes (hora, IP, tipo de evento, resultado, ubicación general, identificador anónimo, dispositivo y sistema operativo);
- documentar el consentimiento o el aviso previo (términos y condiciones);
- restringir el acceso a personal autorizado;
- conservar los datos solo el tiempo necesario y luego eliminarlos.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un IDS y un IPS?
> El IDS detecta y alerta, sin intervenir. El IPS además bloquea la actividad sospechosa en tiempo real, con el riesgo de bloquear acciones legítimas ante un falso positivo.

> [!question]- ¿Qué detecta un HIDS que un NIDS no ve?
> Lo que ocurre dentro de un servidor: cambios en archivos, llamadas al sistema o actividad de un atacante que ya entró, aunque el tráfico de red se vea normal.

> [!question]- ¿Cómo reconcilia un sistema de monitoreo la seguridad con el GDPR?
> Registrando solo metadatos necesarios, anonimizados cuando es posible, con aviso al usuario, acceso restringido y un plazo de conservación limitado.
