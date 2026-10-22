---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/serializacion
  - programacion/pickle
  - programacion/seguridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Serialización con JSON: dumps, loads y personalización]]"
---

# Serialización binaria con pickle y riesgos de seguridad

Mientras que JSON es un estándar universal interoperable limitado a tipos de datos básicos, muchas aplicaciones en Python necesitan congelar y restaurar objetos complejos completos —con sus clases, atributos privados y referencias circulares— sin escribir manualmente codificadores y decodificadores. Para este propósito Python incluye el módulo nativo **`pickle`**.

## El módulo pickle: serialización binaria nativa

El proceso de serializar con `pickle` se denomina coloquialmente emcurtido (*pickling*) y su inverso descurtido (*unpickling*). A diferencia de JSON, `pickle` transforma los objetos en una secuencia de **bytes binarios** propios del entorno de Python:

- **En memoria (bytes):**
  - `pickle.dumps(obj)`: serializa cualquier objeto de Python a un flujo de `bytes`.
  - `pickle.loads(datos_bytes)`: reconstruye el objeto original a partir de los bytes recibidos.
- **En archivos:**
  - `pickle.dump(obj, archivo)`: escribe en un archivo binario abierto en modo `"wb"`.
  - `pickle.load(archivo)`: lee y reconstruye desde un archivo abierto en modo `"rb"`.

### Comparativa técnica: JSON frente a Pickle

```
+--------------------+-----------------------+-----------------------+
| Característica     | JSON                  | Pickle                |
+--------------------+-----------------------+-----------------------+
| Formato resultante | Texto plano legible   | Binario opaco         |
| Interoperabilidad  | Universal (cualquier  | Exclusivo de Python   |
|                    | lenguaje o sistema)   |                       |
| Tipos soportados   | Primitivos básicos    | Prácticamente todo    |
|                    | (dict, list, str, num)| objeto de Python      |
| Clases propias     | Requiere encoders     | Automático por defecto|
| Seguridad          | Seguro (solo datos)   | **Altamente inseguro**|
+--------------------+-----------------------+-----------------------+
```

## Personalización con `__getstate__` y `__setstate__`

Cuando un objeto contiene atributos que no tienen sentido persistir (como conexiones a bases de datos, sockets de red abiertos o contraseñas en memoria), se pueden interceptar el guardado y la carga mediante métodos mágicos:

```python
import pickle

class SesionUsuario:
    def __init__(self, usuario: str, token: str):
        self.usuario = usuario
        self.token = token
        self.conexion_activa = "socket_en_vivo"

    def __getstate__(self):
        # Excluir recursos efímeros del volcado
        estado = self.__dict__.copy()
        estado.pop("conexion_activa", None)
        return estado

    def __setstate__(self, estado):
        # Restaurar estado y reiniciar variables
        self.__dict__.update(estado)
        self.conexion_activa = None

sesion = SesionUsuario("valdivieso", "token_secreto_123")
datos = pickle.dumps(sesion)

recuperado = pickle.loads(datos)
print(f"Usuario: {recuperado.usuario}, Conexión: {recuperado.conexion_activa}")
```

```
Usuario: valdivieso, Conexión: None
```

> [!warning] Peligro crítico de seguridad: ejecución arbitraria de código
> **NUNCA** utilices `pickle.loads()` sobre datos recibidos desde la red o de fuentes en las que no confíes plenamente. La deserialización de `pickle` puede ejecutar cualquier instrucción de Python durante la reconstrucción del objeto. Un atacante puede construir un payload malicioso que ejecute código arbitrario o borre el disco con solo deserializar el paquete.

> [!tip] Cuándo usar pickle
> Utiliza `pickle` únicamente para almacenamiento temporal interno (por ejemplo memoria caché local en disco o comunicación entre procesos del mismo servidor confiable). Para APIs, clientes web y redes externas, usa siempre **JSON**.

## Preguntas de repaso

> [!question]- ¿Por qué es peligroso usar `pickle` para recibir información de clientes en un servidor público?
> Porque la deserialización de `pickle` reconstruye código ejecutable de Python; un atacante puede alterar los bytes para ejecutar comandos del sistema operativo (*Remote Code Execution*) en el servidor.

> [!question]- ¿Cuál es la diferencia en el modo de apertura de archivo para `json.dump()` versus `pickle.dump()`?
> `json.dump()` escribe texto plano (`"w"` o `"wt"`), mientras que `pickle.dump()` escribe bytes binarios y exige abrir el archivo en modo binario (`"wb"`).

> [!question]- ¿Para qué sirve el método `__getstate__()` en una clase serializable con `pickle`?
> Permite personalizar qué atributos formarán parte del estado serializado, excluyendo datos sensibles o recursos del sistema (como sockets de red) que no se pueden persistir.

> [!question]- ¿Qué ocurre si intentas abrir y deserializar con `pickle` un archivo generado en un programa que utiliza Java o C++?
> Fallará; el formato binario de `pickle` es un protocolo interno dependiente de la implementación del intérprete de Python y no es interoperable con otros lenguajes.
