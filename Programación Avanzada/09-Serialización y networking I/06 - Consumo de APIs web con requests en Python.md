---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/requests
  - programacion/api
  - origen/complemento
prerrequisitos:
  - "[[01 - Serialización con JSON: dumps, loads y personalización]]"
  - "[[04 - Protocolo HTTP: estructura de mensajes, métodos y códigos de estado]]"
---

# Consumo de APIs web con requests en Python

Para integrar nuestras aplicaciones con servicios del mundo real —como consultar el pronóstico del tiempo, obtener precios de divisas o interactuar con la API de GitHub—, no escribimos sockets en crudo. En su lugar, utilizamos la biblioteca estándar de facto **`requests`**, diseñada para realizar peticiones HTTP de forma intuitiva e idiomática.

## Peticiones GET y consulta de recursos

Para solicitar información de un servicio web utilizamos `requests.get()`. Si la consulta requiere parámetros en la URL (*query string*), se entregan de forma limpia mediante un diccionario en el parámetro `params`:

```python
import requests

url = "https://api.ejemplo.com/usuarios"
parametros = {"rol": "estudiante", "limite": 10}

# Equivale a: https://api.ejemplo.com/usuarios?rol=estudiante&limite=10
respuesta = requests.get(url, params=parametros, timeout=5.0)

print(f"Código de estado: {respuesta.status_code}")
```

### Inspección del objeto Response
El objeto retornado contiene toda la información de la respuesta del servidor:

- **`respuesta.status_code`:** entero con el código de respuesta (ejemplo `200`, `404`).
- **`respuesta.ok`:** valor booleano (`True` si el código es menor a 400).
- **`respuesta.json()`:** deserializa automáticamente el cuerpo JSON recibido a un diccionario o lista nativa de Python (equivalente a `json.loads(respuesta.text)`).
- **`respuesta.text`:** cuerpo de la respuesta decodificado como string de texto.
- **`respuesta.content`:** bytes crudos de la respuesta (esencial para descargar imágenes o archivos PDF).
- **`respuesta.headers`:** diccionario con las cabeceras HTTP emitidas por el servidor.

## Peticiones POST y envío de información

Para crear recursos o enviar datos estructurados al servidor utilizamos `requests.post()`:

```python
import requests

url = "https://api.ejemplo.com/usuarios"
datos_nuevo_usuario = {"nombre": "Francisca", "correo": "fran@ejemplo.cl"}

# Al usar json=..., requests serializa automáticamente y añade Content-Type: application/json
respuesta = requests.post(url, json=datos_nuevo_usuario, timeout=5.0)

if respuesta.status_code == 201:
    print("Usuario creado con éxito en la API.")
```

## Autenticación y cabeceras personalizadas

La gran mayoría de las APIs comerciales requieren autenticar al usuario para controlar cuotas de uso. Esto se hace agregando cabeceras de autorización en el parámetro `headers`:

```python
headers = {
    "Authorization": "Bearer TOKEN_SECRETO_XYZ",
    "User-Agent": "MiAppPython/1.0"
}
respuesta = requests.get("https://api.github.com/user", headers=headers)
```

> [!warning] Define siempre un timeout explícito
> Si invocas `requests.get(url)` sin especificar el parámetro `timeout`, la llamada puede quedar **bloqueada indefinidamente** si el servidor remoto deja de responder o la red colapsa, congelando tu programa por completo. Usa siempre `timeout=5.0` (en segundos).

> [!tip] Control automático de errores con raise_for_status()
> En lugar de escribir comprobaciones manuales `if respuesta.status_code != 200`, invoca **`respuesta.raise_for_status()`**. Este método levantará una excepción `HTTPError` automática si el servidor respondió con cualquier código 4xx o 5xx.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre usar `json=datos` versus `data=datos` en una petición `requests.post()`?
> `json=datos` convierte el diccionario a un string JSON y añade la cabecera `Content-Type: application/json`; `data=datos` envía los datos codificados como formulario URL estándar (*form-urlencoded*) o como bytes en crudo.

> [!question]- ¿Qué ventaja ofrece el método `respuesta.json()` por sobre llamar a `json.loads(respuesta.text)`?
> Es una abstracción directa integrada en `requests` que detecta y aplica automáticamente la codificación de caracteres declarada en las cabeceras HTTP del servidor.

> [!question]- ¿Qué ocurre si un servidor remoto se congela y no responde cuando realizas una petición sin el parámetro `timeout`?
> El hilo de ejecución de Python se queda esperando para siempre en el socket de red, bloqueando el resto de la aplicación sin arrojar ninguna excepción.

> [!question]- ¿Cómo se entregan parámetros de búsqueda para que se añadan automáticamente a la URL con el formato `?clave=valor`?
> Se entregan en un diccionario de Python pasado al argumento `params` de la función `requests.get()`.

