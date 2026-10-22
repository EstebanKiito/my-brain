---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/flask
  - programacion/api
  - origen/complemento
prerrequisitos:
  - "[[04 - Protocolo HTTP: estructura de mensajes, métodos y códigos de estado]]"
  - "[[06 - Consumo de APIs web con requests en Python]]"
---

# Creación de servicios web con Flask: rutas, parámetros y JSON

Así como podemos consumir servicios web mediante peticiones de cliente, también podemos construir nuestros propios servidores HTTP para procesar peticiones, consultar bases de datos y exponer recursos mediante una API REST. En Python, el microframework más popular y pedagógico para este propósito es **Flask**.

## Fundamentos de Flask y enrutamiento

Flask es un marco de trabajo minimalista (*microframework*) que permite mapear direcciones URL a funciones de Python usando el decorador **`@app.route()`**:

```python
from flask import Flask, jsonify

# Instanciar la aplicación
app = Flask(__name__)

@app.route("/")
def inicio():
    # Retorna un mensaje y código 200 por defecto
    return jsonify({"mensaje": "Bienvenido a la API del curso"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

Por defecto, las rutas solo escuchan peticiones `GET`. Para admitir otros métodos HTTP se debe especificar la lista en `methods=["GET", "POST"]`.

## Patrones esenciales de endpoints en Flask

### 1. Rutas con parámetros dinámicos
Permiten capturar valores directamente desde la ruta de la URL especificando su convertidor de tipo (`<int:id>`, `<string:nombre>`):

```python
@app.route("/productos/<int:producto_id>", methods=["GET"])
def detalle_producto(producto_id: int):
    # producto_id se recibe tipado como entero
    return jsonify({"id": producto_id, "estado": "disponible"}), 200
```

### 2. Parámetros de consulta (Query Parameters)
Para leer valores enviados en el *query string* (ejemplo `/buscar?termino=python&orden=asc`) se utiliza el objeto global **`request.args`**:

```python
from flask import request

@app.route("/buscar", methods=["GET"])
def buscar():
    termino = request.args.get("termino", default="")
    limite = request.args.get("limite", default=10, type=int)
    return jsonify({"resultado": f"Buscando '{termino}'", "limite": limite})
```

### 3. Recepción de datos JSON en el cuerpo (Body)
Al recibir peticiones `POST` o `PUT` con contenido JSON, utilizamos **`request.get_json()`** para deserializar la información automáticamente a un diccionario:

```python
@app.route("/productos", methods=["POST"])
def registrar_producto():
    datos = request.get_json()
    if not datos or "nombre" not in datos or "precio" not in datos:
        # Validación de entrada: error 400 Bad Request
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # Procesar y retornar código 201 Created
    return jsonify({"mensaje": "Producto guardado", "datos": datos}), 201
```

### 4. Control explícito de respuestas y códigos de estado
En Flask, una función manejadora puede retornar una tupla con dos elementos: `(cuerpo_respuesta, codigo_estado)`. La función **`jsonify()`** emite el string JSON correspondiente y fija automáticamente la cabecera `Content-Type: application/json`.

> [!warning] request.get_json() retorna None ante cabeceras faltantes
> Si el cliente envía datos en el cuerpo pero olvida incluir la cabecera `Content-Type: application/json`, `request.get_json()` retornará `None`. Valida siempre que el resultado no sea nulo antes de acceder a sus claves.

> [!tip] Desactivar debug en producción
> El parámetro `debug=True` en `app.run()` recarga el código automáticamente ante cambios y muestra un depurador interactivo en el navegador. Por motivos de seguridad estricta, jamás debe dejarse activo en servidores accesibles públicamente.

## Preguntas de repaso

> [!question]- ¿Cómo se define un endpoint en Flask que acepte únicamente peticiones POST?
> Indicando el parámetro de métodos en el decorador: `@app.route("/ruta", methods=["POST"])`.

> [!question]- ¿Cuál es la diferencia entre obtener datos con `request.args` versus `request.get_json()`?
> `request.args` extrae parámetros de consulta pasados en la URL (`?clave=valor`), mientras que `request.get_json()` decodifica el cuerpo del mensaje (*payload*) enviado en la petición HTTP.

> [!question]- ¿Qué ventaja aporta la función `jsonify()` sobre un retorno tradicional de string?
> Convierte automáticamente estructuras de Python a JSON y configura la cabecera HTTP `Content-Type: application/json`, asegurando que el cliente interprete la respuesta como datos estructurados.

> [!question]- ¿Cómo se retorna un código de error 404 personalizado desde una función de Flask?
> Retornando una tupla con la respuesta y el número de código entero: `return jsonify({"error": "No encontrado"}), 404`.

