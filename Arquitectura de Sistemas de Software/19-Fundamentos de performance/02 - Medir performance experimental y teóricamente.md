---
ramo: "Arquitectura de Sistemas de Software"
tema: "Fundamentos de performance"
tags:
  - arquisis/performance
  - origen/complemento
prerrequisitos:
  - "[[01 - Performance como atributo y sus métricas]]"
---

# Medir performance experimental y teóricamente

Optimizar sin medir es adivinar. La performance se mide de dos formas complementarias: **experimentalmente**, cargando el sistema real y observando qué pasa, o **teóricamente**, modelando la llegada de peticiones para predecir cuellos de botella antes de construir.

## Medición experimental

Se basa en herramientas, en ensayo y error, y en medir implementaciones concretas: throughput, latencia y nivel de servicio.

| Tipo | Herramientas | Para qué |
|---|---|---|
| **Carga** | JMeter, Locust, k6, Vegeta, AWS Distributed Load Testing | Generar tráfico sintético y medir cómo responde el sistema |
| **Monitoreo** | New Relic, Datadog, Prometheus | Observar métricas reales en producción a lo largo del tiempo |
| **Red** | Herramientas del navegador, Wireshark, ping, iperf | Ver latencia, paquetes y ancho de banda |
| **Sistema** | htop/top, `time`, monitores de procesos | Ver CPU, memoria y procesos de una máquina |

Un test de carga típico sube los usuarios virtuales por etapas y observa en qué punto la latencia se dispara o empiezan los errores:

```python
# locustfile.py — prueba de carga con Locust
from locust import HttpUser, task, between

class Comprador(HttpUser):
    wait_time = between(1, 3)          # segundos entre acciones de cada usuario virtual

    @task(3)
    def ver_catalogo(self):
        self.client.get("/productos")

    @task(1)
    def ver_producto(self):
        self.client.get("/productos/42")
```

![Panel de monitoreo con operaciones de base de datos, throughput y tiempo de respuesta](adjuntos/Panel%20de%20monitoreo%20de%20métricas%20de%20base%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, una lista de operaciones ordenadas por tiempo consumido, con barras de porcentaje.
> - Arriba, un gráfico de áreas apiladas con las 5 operaciones de base de datos que más tiempo de reloj consumen.
> - Al centro, *Database throughput* (barras parejas) y *Database response time* (una línea con variaciones).
> - Abajo, *Slow SQL traces*: consultas `SELECT` lentas con su tiempo de respuesta y número de muestras.

Un panel así permite ubicar el cuello de botella: si la mayor parte del tiempo se va en unas pocas consultas SQL, la táctica correcta es optimizar esas consultas o cachearlas, no agregar servidores web.

## Medición teórica

- **Teoría de colas:** análisis estadístico de la llegada y la atención de peticiones. Las llegadas se modelan típicamente como un **proceso de Poisson** (tiempo entre llegadas con distribución **exponencial**).
- **Cadenas de Markov:** modelan los **estados más probables** del sistema (vivo, al límite, caído) y las **transiciones más probables** entre ellos. Sirven para análisis de capacidad y para encontrar cuellos de botella, aunque el modelamiento es complejo.
- **Simulaciones** con distintas tasas de llegada.

### Ejemplo: una cola con un servidor (M/M/1)

Un servicio atiende **μ = 100 req/s** y recibe **λ = 80 req/s**:
- Utilización: $\rho = \lambda / \mu = 0{,}8$.
- Tiempo promedio en el sistema: $W = \frac{1}{\mu - \lambda} = \frac{1}{20} = 0{,}05$ s, es decir, **50 ms**.
- Peticiones promedio en el sistema: $L = \frac{\rho}{1-\rho} = 4$. Esto cumple la ley de Little: $L = \lambda W = 80 \cdot 0{,}05 = 4$.

Si la carga sube a **λ = 95 req/s** ($\rho = 0{,}95$), entonces $W = 1/5 = 0{,}2$ s = **200 ms**: un 19% más de carga **cuadruplica** la latencia.

> [!warning] Cerca del 100% de utilización la latencia explota
> En una cola, el tiempo de espera crece como $1/(\mu - \lambda)$: no es lineal. Por eso un servidor al 95% de CPU no está "casi bien", está a punto de colapsar. Se diseña para operar con holgura (por ejemplo, ρ ≤ 0,7) y se escala antes de llegar al límite.

| | Experimental | Teórico |
|---|---|---|
| Cuándo | Con el sistema construido | Antes de construir o para dimensionar |
| Ventaja | Mide la realidad, con todos sus efectos | Barato; explica por qué ocurre algo |
| Límite | Caro; el ambiente de prueba puede diferir de producción | Supuestos simplificados (Poisson, servidor único) |

## Preguntas de repaso

> [!question]- Nombre una herramienta de cada tipo (carga, monitoreo, red y sistema) y para qué sirve.
> Carga: k6 o Locust, para generar tráfico sintético. Monitoreo: Datadog o Prometheus, para observar métricas en producción. Red: Wireshark o iperf, para inspeccionar paquetes o medir ancho de banda. Sistema: htop, para ver CPU y memoria de una máquina.

> [!question]- Un servicio atiende 50 req/s y recibe 40 req/s (M/M/1). Calcule la utilización y el tiempo promedio en el sistema.
> $\rho = 40/50 = 0{,}8$ y $W = 1/(50-40) = 0{,}1$ s, es decir, 100 ms. Además $L = \lambda W = 40 \cdot 0{,}1 = 4$ peticiones en el sistema.

> [!question]- ¿Por qué no conviene operar un servidor cerca del 100% de utilización?
> Porque en una cola la espera crece como $1/(\mu-\lambda)$, que se dispara al acercarse λ a μ. Un pequeño aumento de carga produce un gran aumento de latencia. Hay que dejar holgura y escalar antes.

> [!question]- ¿Qué aporta modelar el sistema con cadenas de Markov?
> Permite estimar en qué estados pasa más tiempo el sistema (normal, degradado, caído) y cuáles son las transiciones más probables entre ellos. Así se identifica capacidad y cuellos de botella antes de que ocurran, aunque construir el modelo es complejo.

> [!question]- Un panel muestra que el 70% del tiempo de respuesta se va en tres consultas SQL. ¿Qué táctica conviene y cuál no?
> Conviene optimizar esas consultas (índices, reescritura) o cachear sus resultados. No conviene agregar servidores de aplicación, porque el cuello de botella está en la base de datos y más servidores solo le mandarían más consultas.

> [!question]- V o F: "La medición teórica reemplaza a las pruebas de carga".
> Falso. Son complementarias. La teoría sirve para dimensionar y explicar comportamientos con supuestos simplificados, y las pruebas de carga miden el sistema real con todos sus efectos (red, base de datos, recolector de basura).

> [!question]- ¿Qué es un proceso de Poisson y por qué se usa para modelar llegadas?
> Es un modelo donde las llegadas son independientes entre sí y ocurren a una tasa promedio λ, con tiempos entre llegadas de distribución exponencial. Describe bien muchos usuarios que actúan sin coordinarse, como las peticiones a una web.
