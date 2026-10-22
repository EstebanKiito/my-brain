---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/concurrencia
  - programacion/api
  - origen/complemento
prerrequisitos:
  - "[[03 - Concurrencia condiciones de carrera y locks]]"
  - "[[06 - Consumo de APIs web con requests en Python]]"
  - "[[07 - Creación de servicios web con Flask: rutas, parámetros y JSON]]"
---

# Concurrencia en servicios web: peticiones paralelas y condiciones de carrera

Al conectar múltiples clientes y servidores a través de internet, la concurrencia deja de ser un ejercicio teórico para convertirse en la norma. Cuando cientos de usuarios interactúan simultáneamente con una API o cuando un cliente lanza decenas de peticiones simultáneas, emergen condiciones de carrera y problemas de límites de tasa que requieren estrategias de sincronización robustas.

## Peticiones concurrentes con ThreadPoolExecutor

Realizar peticiones HTTP secuenciales en un bucle genera tiempos de espera elevados porque el programa pasa la mayor parte del tiempo esperando paquetes de red (I/O-bound). Para paralelizar peticiones del lado del cliente utilizamos **`ThreadPoolExecutor`** del módulo `concurrent.futures`:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def consultar_servicio(usuario_id: int):
    # Simula la latencia de una petición de red
    time.sleep(0.04)
    return f"Datos usuario {usuario_id}"

usuarios = [101, 102, 103, 104]

# Ejecución paralela con un grupo de hilos de trabajo
with ThreadPoolExecutor(max_workers=4) as executor:
    resultados = list(executor.map(consultar_servicio, usuarios))

print(f"Total procesados concurrentemente: {len(resultados)}")
```

## Condiciones de carrera desde el cliente

### 1. El problema del doble envío (Double Submit)
Ocurre cuando un usuario presiona dos veces seguidas el botón "Pagar" o cuando dos hilos de un cliente envían la misma orden simultáneamente. Si la red procesa ambas antes de que la primera termine, el servidor puede cobrar dos veces.
- **Solución:** Claves de idempotencia (*Idempotency Keys*) en las cabeceras HTTP para que el servidor ignore peticiones duplicadas.

### 2. Límite de tasa (Rate Limiting) y error 429
Las APIs comerciales limitan la cantidad de solicitudes por minuto para proteger su infraestructura. Al superarlo, responden con el código **`429 Too Many Requests`**. Para mitigar este problema se implementa el algoritmo de **retroceso exponencial** (*Exponential Backoff*):

```python
import time

def reintentar_con_backoff(max_intentos: int = 3):
    tiempo_espera = 0.1  # Espera inicial en segundos
    for intento in range(1, max_intentos + 1):
        # Simulación de respuesta 429
        respuesta_status = 429 if intento < 3 else 200

        if respuesta_status == 200:
            print(f"Éxito en el intento {intento}")
            return True
        elif respuesta_status == 429:
            print(f"Límite alcanzado. Esperando {tiempo_espera:.2f}s antes de reintentar...")
            time.sleep(tiempo_espera)
            tiempo_espera *= 2  # Duplicar el tiempo de espera (exponencial)
    return False

reintentar_con_backoff()
```

```
Límite alcanzado. Esperando 0.10s antes de reintentar...
Límite alcanzado. Esperando 0.20s antes de reintentar...
Éxito en el intento 3
```

## Condiciones de carrera en el servidor web

Los servidores web modernos atienden cada petición HTTP entrante en un hilo o proceso separado. Si el servidor almacena información en variables globales de memoria (por ejemplo un contador de asientos disponibles o saldo de compras), múltiples peticiones concurrentes pueden leer el mismo inventario y sobrevender el producto:

```python
import threading
from flask import Flask, jsonify

app = Flask(__name__)
stock_disponible = 10
cerrojo_stock = threading.Lock()

@app.route("/comprar", methods=["POST"])
def comprar_producto():
    global stock_disponible
    # Sección crítica protegida contra condiciones de carrera concurrentes
    with cerrojo_stock:
        if stock_disponible > 0:
            stock_disponible -= 1
            return jsonify({"mensaje": "Compra exitosa", "stock_restante": stock_disponible}), 200
        return jsonify({"error": "Stock agotado"}), 409
```

> [!tip] Backoff con dispersión aleatoria (Jitter)
> En sistemas masivos distribuidos, añadir una pequeña variación aleatoria (*jitter*) al tiempo de espera del backoff exponencial evita que miles de clientes despierten exactamente al mismo milisegundo y vuelvan a saturar al servidor al unísono (*thundering herd problem*).

## Preguntas de repaso

> [!question]- ¿Por qué `ThreadPoolExecutor` es especialmente eficaz para acelerar clientes que consultan múltiples APIs?
> Porque las peticiones HTTP son operaciones limitadas por Entrada/Salida (I/O-bound); mientras un hilo espera la respuesta del servidor remoto, el intérprete libera el GIL y permite que los demás hilos transmitan sus consultas.

> [!question]- ¿Qué significa el código de estado HTTP 429 y cómo debe reaccionar un cliente bien diseñado?
> Significa *Too Many Requests* (límite de tasa excedido); el cliente no debe saturar con reintentos inmediatos, sino pausar su ejecución y reintentar progresivamente usando retroceso exponencial (*exponential backoff*).

> [!question]- ¿Cómo se produce una condición de carrera dentro de un servidor web Flask?
> Cuando dos hilos del servidor atienden peticiones concurrentes distintas y ambos leen y modifican la misma variable de estado compartida en memoria sin sincronización previa con un cerrojo (`Lock`).

> [!question]- ¿Qué problema resuelve el uso de claves de idempotencia en peticiones POST críticas (como pagos)?
> Asegura que si una petición se envía dos veces debido a reintentos de red o clics repetidos, el servidor reconozca el identificador único y solo procese la transacción financiera una sola vez.

