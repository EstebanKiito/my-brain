---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/serializacion
  - programacion/json
  - origen/complemento
prerrequisitos:
  - "[[08 - Archivos, encoding y bytes]]"
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
---

# Serialización con JSON: dumps, loads y personalización

Los objetos instanciados en Python residen en la memoria RAM del proceso bajo estructuras de punteros y tablas de símbolos que desaparecen al apagar el programa. Para guardar el estado de un programa en disco o transmitir datos a través de una red hacia computadores con otros lenguajes o arquitecturas, es imprescindible serializar la información.

## El concepto de serialización y el estándar JSON

La **serialización** (*serialization* o *marshalling*) es el proceso de transformar una estructura de datos u objeto en memoria en una secuencia lineal de bytes o texto plano estandarizado. La **deserialización** realiza el camino inverso: reconstruye el objeto original en memoria a partir del flujo recibido.

**JSON** (*JavaScript Object Notation*) es el formato de texto estándar de la industria web gracias a su legibilidad humana y su amplia interoperabilidad:

```
+--------------------+-----------------------+
| Tipo en Python     | Equivalente en JSON   |
+--------------------+-----------------------+
| dict               | object ({})           |
| list, tuple        | array ([])            |
| str                | string ("")           |
| int, float         | number                |
| True, False        | true, false           |
| None               | null                  |
+--------------------+-----------------------+
```

## El módulo json de la biblioteca estándar

Python provee el módulo nativo **`json`** con cuatro funciones esenciales:

- **Operaciones en memoria (strings):**
  - `json.dumps(obj)`: serializa un objeto de Python a un string con formato JSON (*dump string*).
  - `json.loads(texto_json)`: deserializa un string JSON a tipos nativos de Python (*load string*).
- **Operaciones con archivos:**
  - `json.dump(obj, archivo)`: serializa y escribe directamente en un archivo de texto abierto.
  - `json.load(archivo)`: lee y deserializa el contenido JSON desde un archivo.

## Serialización de clases personalizadas

Por defecto, JSON solo comprende tipos primitivos. Intentar serializar una instancia de una clase propia arroja `TypeError: Object of type X is not JSON serializable`. Para solucionarlo, extendemos **`json.JSONEncoder`** sobrescribiendo el método **`default(self, obj)`**, y para deserializar utilizamos el parámetro **`object_hook`**:

```python
import json

class Mascota:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

class MascotaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Mascota):
            # Convertir el objeto en un diccionario con metadata de tipo
            return {"__tipo__": "Mascota", "nombre": obj.nombre, "edad": obj.edad}
        return super().default(obj)

def mascota_hook(dicc: dict):
    if dicc.get("__tipo__") == "Mascota":
        return Mascota(dicc["nombre"], dicc["edad"])
    return dicc

gato = Mascota("Michi", 3)

# 1. Serialización con clase codificadora personalizada
texto_json = json.dumps(gato, cls=MascotaEncoder)
print(texto_json)

# 2. Deserialización reconstructiva con object_hook
objeto_recuperado = json.loads(texto_json, object_hook=mascota_hook)
print(f"Tipo: {type(objeto_recuperado).__name__}, Nombre: {objeto_recuperado.nombre}")
```

```
{"__tipo__": "Mascota", "nombre": "Michi", "edad": 3}
Tipo: Mascota, Nombre: Michi
```

> [!warning] Limitación de tipos no soportados
> Estructuras como conjuntos (`set`), tuplas (que se transforman en listas `[]` al serializarse y pierden su inmutabilidad), números complejos o funciones no se serializan automáticamente en JSON; requieren codificadores personalizados explícitos.

> [!tip] Formateo legible con indent
> Para inspeccionar archivos JSON grandes durante la depuración, usa el parámetro `indent=4` en `json.dumps()` para generar saltos de línea y sangrías automáticas legibles.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre los métodos `json.dump()` y `json.dumps()`?
> `json.dump()` escribe el resultado serializado directamente en un descriptor de archivo abierto, mientras que `json.dumps()` retorna el resultado como una cadena de texto (`str`) en memoria.

> [!question]- ¿Por qué una tupla de Python cambia de tipo al pasar por un ciclo de serialización y deserialización estándar con JSON?
> Porque la especificación JSON no distingue entre listas y tuplas; solo posee el concepto general de arreglo (*array* `[]`), por lo que `json.loads()` siempre reconstruye un `list`.

> [!question]- ¿Qué rol cumple el método `super().default(obj)` al implementar un `JSONEncoder` personalizado?
> Delega la serialización de cualquier objeto que no sea de nuestra clase a la implementación base de Qt/Python, arrojando el error estándar correspondiente si el tipo es desconocido.

> [!question]- ¿Cómo opera el parámetro `object_hook` en la función `json.loads()`?
> Es una función callback que se ejecuta sobre cada diccionario decodificado del JSON antes de devolverlo, permitiendo interceptarlo e instanciar la clase original si detecta las claves esperadas.

