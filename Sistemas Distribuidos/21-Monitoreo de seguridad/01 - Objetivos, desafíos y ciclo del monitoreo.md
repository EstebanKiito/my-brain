---
ramo: "Sistemas Distribuidos"
tema: "Monitoreo de seguridad"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[02 - Control de acceso, OAuth y canales seguros]]"
---

# Objetivos, desafíos y ciclo del monitoreo

Si ya se cifra, se autentica y se autoriza, ¿para qué vigilar? Porque esas defensas no sirven cuando un atacante usa **credenciales válidas** robadas, o cuando el ataque viene de adentro. El **monitoreo** observa lo que los otros mecanismos no previenen, y en un sistema distribuido enfrenta los mismos problemas de siempre: relojes desfasados, eventos dispersos y volumen enorme.

## Objetivos

- **Detectar** actividades maliciosas.
- **Reaccionar** ante incidentes.
- **Recolectar evidencia.**
- Vigilar **sin incumplir la ley**.
- **Mejorar** la postura de seguridad.

## Desafíos en un sistema distribuido

| Desafío | Problema | Qué se hace |
|---|---|---|
| **Latencia y asincronía** | Los eventos llegan desordenados y los relojes no coinciden: se pierde la causalidad | Sincronizar relojes ([[05 - Protocolo NTP\|NTP]] o [[02 - Relojes vectoriales\|vectoriales]]); correlación tolerante al desorden, con ventanas de tiempo o un buffer que reordena; IDs explícitos de petición, flujo o transacción en los logs |
| **Volumen de eventos** | Demasiados logs, métricas y trazas para guardar o analizar en tiempo real | Filtrar localmente lo irrelevante; muestrear o agregar (por ejemplo, el promedio de CPU cada 10 s en vez de cada 1 s); procesar en paralelo con Elasticsearch, Loki, Fluentd o Kafka |
| **Visibilidad fragmentada** | Cada nodo ve solo su contexto, y los ataques distribuidos no se notan localmente | Un **SIEM** que correlaciona de forma centralizada; IDs de flujo y usuario en los logs; dashboards globales (Prometheus, Grafana Loki); política **Zero Trust**: pedir identidad en cada solicitud, incluso dentro del sistema |
| **Puntos ciegos** | El propio monitoreo puede fallar o ser comprometido | **Watchdogs** que vigilan al monitoreo; logs **inmutables** (almacenamiento WORM) y firmados; aislar el canal de monitoreo del de control |
| **Privacidad y normativa** | Lo recolectado puede violar la privacidad o regulaciones | Anonimizar (sin IP ni ID de usuario asociados); consentimiento o control del usuario; logs por nivel de sensibilidad |

> [!warning] El desafío principal
> Para identificar patrones maliciosos, lo más difícil es la **asincronía y desincronización de los relojes**: sin un orden confiable de los eventos no se puede reconstruir qué causó qué. El volumen se maneja con filtros y herramientas; el orden perdido no.

## Ciclo de vida

![Ciclo de vida del monitoreo](adjuntos/Ciclo%20de%20vida%20del%20monitoreo.png)

> [!example]- Transcripción de la imagen
> Una pirámide de cuatro niveles: (1) recolección de eventos; (2) análisis: verificar reglas, patrones y anomalías; (3) respuesta: permitir, bloquear o alertar; (4) registro para auditoría.

## Tipos de análisis

| Tipo | Cómo detecta | Ejemplo | Ventaja | Desventaja |
|---|---|---|---|---|
| **Firmas** | Compara contra patrones de ataques conocidos | Una petición con `../../../etc/passwd`; el hash de un virus conocido | Alta precisión ante amenazas conocidas | No detecta amenazas nuevas |
| **Anomalías** | Desviaciones del perfil "normal" | root inicia sesión a las 3 a. m. desde una IP inusual; tráfico 10 veces mayor que el promedio | Detecta amenazas desconocidas | Muchos falsos positivos |
| **Reglas o políticas** | Condiciones definidas a mano | Bloquear SSH desde fuera de la subred; alertar si un usuario entra desde dos países en menos de 5 minutos | Fácil de entender y controlar | Difícil de mantener y escalar |
| **Correlación** | Une eventos dispersos en tiempo o espacio | Tres logins fallidos desde IPs distintas y luego uno exitoso: fuerza bruta distribuida | Aporta contexto y reduce falsas alarmas | Requiere mucho procesamiento y logs normalizados |
| **Machine learning o IA** | Aprende patrones normales, agrupa y detecta outliers (Elastic ML, Microsoft Sentinel) | Clasificar logs por severidad con NLP; ataques que cambian de firma | Se adapta a amenazas nuevas | Requiere entrenamiento y datos |

## Preguntas de repaso

> [!question]- ¿Por qué hace falta monitorear si ya hay cifrado y autenticación?
> Porque un atacante con credenciales válidas, o uno interno, pasa esas defensas. El monitoreo detecta comportamientos sospechosos aunque el acceso sea "legítimo".

> [!question]- ¿Por qué la correlación de eventos necesita relojes sincronizados o IDs de causalidad?
> Porque une eventos de distintos nodos para reconstruir un ataque. Si el orden de los eventos es incorrecto, la cadena causa-efecto se pierde.

> [!question]- ¿Qué gana y qué pierde el análisis por anomalías frente al basado en firmas?
> Gana la capacidad de detectar ataques nuevos que no tienen firma conocida; pierde precisión, porque genera más falsos positivos.
