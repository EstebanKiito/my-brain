---
ramo: "Arquitectura de Sistemas de Software"
tema: "Medición de escalabilidad"
tags:
  - arquisis/escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Escalabilidad escenarios y cuellos de botella]]"
  - "[[02 - Medir performance experimental y teóricamente]]"
---

# Tipos de pruebas de carga y monitoreo

Para saber si un sistema escala hay que someterlo a cargas distintas y observar qué se rompe primero. Cada tipo de prueba responde una pregunta distinta, y elegir la equivocada da una falsa sensación de seguridad.

## Las cuatro pruebas

| Prueba | Pregunta que responde | Forma de la carga |
|---|---|---|
| **Test de carga** | ¿Resisto **este** nivel de carga esperado? | Sube hasta la carga objetivo y se mantiene |
| **Test de estrés** | ¿Cuánto resisto **antes de colapsar**? | Sube más allá de lo esperado hasta que falla |
| **Soak test** | ¿Sigo bien después de **horas o días**? | Carga normal sostenida mucho tiempo; es más precisa |
| **Spike test** | ¿Me adapto a un **pico repentino**? | Salto brusco de carga. Mide la **elasticidad** |

| Tiempo | t1 | t2 | t3 | t4 | t5 | t6 | t7 | t8 |
|---|---|---|---|---|---|---|---|---|
| Carga | 100 | 300 | 500 | 500 | 500 | 500 | 500 | 500 |
| Estrés | 100 | 400 | 800 | 1.200 | 1.600 | 2.000 | 2.400 | 2.800 |
| Spike | 100 | 100 | 100 | 2.000 | 2.000 | 100 | 100 | 100 |

La tabla muestra usuarios virtuales en el tiempo: el test de carga sube a 500 y se mantiene, el de estrés sube sin parar y el spike salta a 2.000 y vuelve. Un soak test sería la fila de carga mantenida durante horas.

**Qué detecta cada una:**
- **Carga:** si se cumple el escenario (por ejemplo, p95 < 500 ms con 10.000 usuarios).
- **Estrés:** el punto de quiebre y **cómo** falla. ¿Se degrada con gracia (responde `429`) o cae por completo?
- **Soak:** fugas de memoria, conexiones que no se liberan, logs que llenan el disco, el recolector de basura que se degrada con el tiempo.
- **Spike:** si el autoscaling reacciona a tiempo, o si las peticiones fallan mientras arrancan las nuevas instancias.

## Monitoreo

Las pruebas dan una foto; el monitoreo da la película en producción. Los proveedores se agrupan así:

| Tipo | Ejemplos | Característica |
|---|---|---|
| **PaaS / manejados** | Datadog, New Relic | Experiencia muy manejada, incluyendo el almacenamiento de los datos; tiene costo |
| **Open source** | Prometheus, Grafana, Nagios | Control total; hay que operarlo |
| **Ligados a la nube** | AWS CloudWatch | Integrados con los servicios del proveedor; dependen de él |

Para escalabilidad, conviene monitorear las mismas métricas de los escenarios (latencia en percentiles, RPS, saturación, lag de replicación y tasa de aciertos de la caché) y poner **alertas** antes del punto de quiebre que mostró el test de estrés.

> [!warning] Probar solo la carga promedio
> Un sistema que pasa el test de carga con el tráfico promedio puede caerse en la apertura de una venta o en un evento viral. Si el enunciado menciona picos ("cuando ocurra un evento particular"), la prueba relevante es el **spike test**, y la característica es la **elasticidad**.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un test de carga y un test de estrés?
> El de carga verifica que el sistema cumpla con la carga esperada. El de estrés lo lleva más allá de lo esperado para encontrar su punto de quiebre y ver cómo falla.

> [!question]- ¿Qué tipo de problemas solo aparece en un soak test?
> Los que se acumulan con el tiempo: fugas de memoria, conexiones o archivos que no se liberan, discos que se llenan de logs y degradación progresiva del recolector de basura. Un test corto no alcanza a mostrarlos.

> [!question]- ¿Qué atributo mide un spike test y qué falla típica detecta?
> La elasticidad. Detecta si el autoscaling reacciona a tiempo: por ejemplo, que las nuevas instancias tarden 3 minutos en arrancar y mientras tanto las peticiones fallen o expiren.

> [!question]- Mini caso: una app de noticias recibe un tráfico normal estable, pero con cada noticia de último minuto sube 20 veces en segundos. ¿Qué prueba prioriza y qué característica arquitectónica justifica?
> Un spike test, porque el riesgo está en los picos repentinos y no en la carga sostenida. La característica es la elasticidad: escalar rápido al subir y reducir después. Se complementa con caché o CDN para absorber las lecturas del pico.

> [!question]- Compare Prometheus con CloudWatch como herramientas de monitoreo.
> Prometheus es open source: da control total y no ata a un proveedor, pero hay que operarlo (almacenamiento, alta disponibilidad, Grafana para visualizar). CloudWatch está integrado a AWS y no hay que operarlo, pero solo es cómodo dentro de AWS y tiene costo por uso.

> [!question]- V o F: "Si el sistema pasa el test de carga, no es necesario hacer un test de estrés".
> Falso. El test de carga solo confirma que se cumple el nivel esperado. El de estrés muestra cuánto margen queda y cómo falla el sistema al superarlo, información necesaria para configurar alertas, rate limiting y autoscaling.
