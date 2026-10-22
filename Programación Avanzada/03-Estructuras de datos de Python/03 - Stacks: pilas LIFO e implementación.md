---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/stacks
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructuras de datos y tuplas]]"
---

# Stacks: pilas LIFO e implementación

Al diseñar sistemas de control de versiones, botones de deshacer en editores o el historial de un navegador web, el orden en que se deshacen o procesan las acciones debe ser exactamente el inverso al orden en que ocurrieron: la última acción realizada debe ser la primera en revertirse.

## Principio LIFO y concepto de Stack

Un **stack** (o **pila**) es una estructura de datos secuencial que opera bajo la disciplina **LIFO** (*Last-In, First-Out*): el último elemento en ingresar es siempre el primer elemento en salir.

La analogía habitual es una pila de platos para lavar: cada plato nuevo se apila en la parte superior (tope) y, al momento de lavar, se retira siempre el plato del tope.

![Operaciones en un stack o pila](adjuntos/Operaciones%20en%20un%20stack%20o%20pila.png)

> [!example]- Transcripción de la imagen
> - Diagrama de una pila con elementos ordenados verticalmente.
> - Operación **Push**: ingresa un nuevo elemento situándose sobre el tope de la pila.
> - Operación **Pop**: extrae y remueve el elemento situado en el tope.
> - Indicador de **Top**: señala la posición del último elemento ingresado.

## Operaciones básicas e implementación en Python

En Python, la forma más directa y eficiente de implementar un *stack* es mediante una **lista** convencional (`list`), aprovechando que agregar y extraer al final de una lista tiene costo temporal $O(1)$ amortizado:

| Operación abstracta | Equivalente en Python | Descripción | Costo |
|---|---|---|---|
| **Push** | `stack.append(x)` | Agrega el elemento `x` al tope de la pila | $O(1)$ |
| **Pop** | `stack.pop()` | Extrae y retorna el elemento del tope | $O(1)$ |
| **Peek** | `stack[-1]` | Observa el elemento del tope sin removerlo | $O(1)$ |
| **Is Empty** | `len(stack) == 0` | Comprueba si la pila carece de elementos | $O(1)$ |
| **Length** | `len(stack)` | Cuenta cuántos elementos residen en la pila | $O(1)$ |

```python
pila = []

# Push
pila.append("página_inicio")
pila.append("noticias")
pila.append("articulo_python")

# Peek
print(f"Elemento en el tope: {pila[-1]}")

# Pop
ultimo = pila.pop()
print(f"Elemento extraído: {ultimo}")
print(f"Pila tras pop: {pila}")
```

```
Elemento en el tope: articulo_python
Elemento extraído: articulo_python
Pila tras pop: ['página_inicio', 'noticias']
```

> [!warning] Nunca usar pop(0) para simular pilas
> El método `pop()` sin argumentos remueve el último elemento en tiempo constante $O(1)$. Si se utiliza `pop(0)`, Python debe desplazar todos los elementos restantes a la izquierda, degradando la operación a tiempo lineal $O(N)$.

## Aplicación real: el botón volver de un navegador

Los navegadores web utilizan un *stack* para almacenar las direcciones visitadas. Al navegar hacia un sitio nuevo la URL previa se apila; al pulsar el botón "Volver", la URL del tope se desapila para regresar a ella:

![Historial de navegación con stack](adjuntos/Historial%20de%20navegaci%C3%B3n%20con%20stack.png)

> [!example]- Transcripción de la imagen
> - Flujo secuencial de tres pantallas de navegador:
>   1. Inicialmente se visita `google.cl`.
>   2. Luego se visita `wikipedia.org`, apilando la página anterior.
>   3. Se visita `python.org`, dejando `wikipedia.org` en el tope de la pila.
> - Al presionar el botón *Atrás*, se extrae `wikipedia.org` de la pila y el navegador regresa a ella.

```python
class Navegador:
    def __init__(self, url_inicial: str):
        self.historial = []
        self.url_actual = url_inicial

    def ir(self, nueva_url: str):
        self.historial.append(self.url_actual)
        self.url_actual = nueva_url
        print(f"Navegando a: {self.url_actual}")

    def volver(self):
        if not self.historial:
            print("No hay páginas previas en el historial.")
            return
        self.url_actual = self.historial.pop()
        print(f"Regresando a: {self.url_actual}")

nav = Navegador("https://uc.cl")
nav.ir("https://canvas.uc.cl")
nav.ir("https://github.com")
nav.volver()
nav.volver()
```

```
Navegando a: https://canvas.uc.cl
Navegando a: https://github.com
Regresando a: https://canvas.uc.cl
Regresando a: https://uc.cl
```

> [!tip] Invertir secuencias de manera natural
> Dado que la pila extrae los datos en orden inverso a su ingreso, apilar los elementos de una secuencia y desapilarlos uno a uno hasta vaciarla revierte la secuencia completa de forma sencilla.

## Preguntas de repaso

> [!question]- ¿Qué significa la sigla LIFO y cómo se refleja en el comportamiento de una pila?
> Significa *Last-In, First-Out* (el último en entrar es el primero en salir). Refleja que cualquier extracción siempre retira el elemento más reciente agregado al tope, dejando los anteriores en espera.

> [!question]- ¿Por qué una lista de Python es adecuada para representar un stack cuando se usa `append()` y `pop()`?
> Porque agregar y quitar elementos por el extremo derecho de una lista opera en tiempo constante amortizado $O(1)$, sin necesidad de reordenar o desplazar el resto de los elementos en memoria.

> [!question]- ¿Qué riesgo existe al llamar a `pop()` o acceder a `stack[-1]` sin comprobar previamente si la pila está vacía?
> Si la pila está vacía, `stack.pop()` levanta una excepción `IndexError: pop from empty list`, y `stack[-1]` levanta `IndexError: list index out of range`. Siempre debe verificarse `if stack:` antes.

> [!question]- ¿En qué otras aplicaciones informáticas se utiliza internamente la estructura de stack?
> En el seguimiento de llamadas a funciones en el sistema de ejecución (*call stack* para recursión y seguimiento de excepciones) y en la evaluación o balanceo de paréntesis y expresiones matemáticas.
