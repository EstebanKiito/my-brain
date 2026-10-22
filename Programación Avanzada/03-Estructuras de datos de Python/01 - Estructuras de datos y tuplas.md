---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/tuplas
  - origen/complemento
prerrequisitos:
  - "[[02 - Listas: creación y comprensión]]"
  - "[[03 - Listas: slicing y orden]]"
---

# Estructuras de datos y tuplas

Al escribir programas reales rara vez trabajamos con valores aislados. Necesitamos agrupar colecciones de datos, organizarlas de manera lógica y acceder a ellas con la mayor rapidez posible según la tarea requerida.

## Clasificación de las estructuras de datos

Una **estructura de datos** es un formato especializado para organizar, almacenar y manipular conjuntos de datos relacionados. En Python se dividen en dos familias según su organización interna:

- **Secuenciales:** mantienen un orden posicional estricto determinado por cómo ingresaron los elementos. Permiten acceso directo mediante un índice numérico correlativo. Ejemplos: listas, tuplas y colas de doble extremo (*deques*).
- **No secuenciales:** no garantizan un orden posicional entre sus elementos. Están optimizadas para comprobar pertenencia o buscar por una clave en tiempo constante. Ejemplos: conjuntos (*sets*) y diccionarios.

## Tuplas: secuencias ordenadas e inmutables

Una **tupla** (`tuple`) es una colección secuencial ordenada e **inmutable**. Una vez creada, su longitud y las referencias que contiene no pueden modificarse: no es posible agregar, reemplazar ni eliminar elementos.

```python
# Creación de tuplas
vacia = tuple()
coordenadas = (10, 20)
un_elemento = (42,)  # La coma final es obligatoria
sin_parentesis = 1, "dos", 3.0

print(f"Coordenadas: {coordenadas}, tipo: {type(coordenadas)}")
print(f"Un elemento: {un_elemento}, tamaño: {len(un_elemento)}")
```

```
Coordenadas: (10, 20), tipo: <class 'tuple'>
Un elemento: (42,), tamaño: 1
```

> [!warning] La coma hace a la tupla de un elemento
> Escribir `(42)` en Python no crea una tupla, sino un entero dentro de paréntesis aritméticos. Para definir una tupla de un solo elemento es obligatorio incluir la coma final: `(42,)`.

### Índices y slicing

Cada elemento posee un índice entero que comienza en 0 desde la izquierda y en -1 desde la derecha:

![Índices en una tupla o secuencia](adjuntos/Índices%20en%20una%20tupla%20o%20secuencia.png)

> [!example]- Transcripción de la imagen
> - Diagrama con una secuencia de cuatro celdas con valores `['a', 'b', 'c', 'd']`.
> - Índices positivos en la fila superior: van de 0 a 3 de izquierda a derecha.
> - Índices negativos en la fila inferior: van de -4 a -1 de izquierda a derecha.

El particionamiento (*slicing*) genera una nueva tupla sin alterar la original:

```python
numeros = (10, 20, 30, 40, 50, 60)
subtupla = numeros[1:4]
saltados = numeros[::2]

print(f"subtupla [1:4]: {subtupla}")
print(f"saltados [::2]: {saltados}")
```

```
subtupla [1:4]: (20, 30, 40)
saltados [::2]: (10, 30, 50)
```

### Mutabilidad interna vs inmutabilidad de la tupla

La inmutabilidad de una tupla significa que las referencias a sus objetos no pueden cambiar. Si uno de sus elementos es un objeto mutable (como una lista), el contenido interno de ese objeto sí puede modificarse:

```python
registro = ("IIC2233", ["Ana", "Pedro"])
# registro[0] = "IIC1103"  # TypeError: 'tuple' object does not support item assignment
registro[1].append("Clara")  # Válido: muta la lista interna
print(registro)
```

```
('IIC2233', ['Ana', 'Pedro', 'Clara'])
```

## Desempaquetado y el operador asterisco

El **desempaquetado** (*unpacking*) permite extraer los valores de una tupla directamente en variables individuales. El operador asterisco (`*`) permite capturar múltiples elementos sobrantes en una lista:

```python
datos = ("Diego", 21, "Ingeniería", "UC", "Santiago")
nombre, edad, *resto = datos
primero, *medio, ultimo = (1, 2, 3, 4, 5)

print(f"Nombre: {nombre}, Edad: {edad}, Resto: {resto}")
print(f"Primero: {primero}, Medio: {medio}, Último: {ultimo}")
```

```
Nombre: Diego, Edad: 21, Resto: ['Ingeniería', 'UC', 'Santiago']
Primero: 1, Medio: [2, 3, 4], Último: 5
```

> [!tip] Retorno múltiple en funciones
> Cuando una función en Python retorna múltiples valores separados por coma (`return a, b`), en realidad está empaquetando los valores en una tupla. El código receptor puede desempaquetarlos inmediatamente: `x, y = calcular()`.

## Preguntas de repaso

> [!question]- ¿Por qué una tupla es preferible a una lista para representar coordenadas geográficas fijas?
> Porque su inmutabilidad garantiza que los valores no se modifiquen accidentalmente a lo largo de la ejecución y permite usarlas como llaves en diccionarios o elementos en conjuntos, cosa que una lista mutable no permite.

> [!question]- ¿Qué ocurre si intentamos reasignar `t[0] = 5` en una tupla `t = (1, [2, 3])`, y qué ocurre si ejecutamos `t[1].append(4)`?
> La reasignación `t[0] = 5` lanza un `TypeError` porque la tupla no admite cambiar sus referencias. En cambio, `t[1].append(4)` tiene éxito porque no cambia la referencia que la tupla guarda hacia la lista, sino que modifica el contenido interno del objeto lista al que apunta.

> [!question]- ¿Qué función cumple el operador `*` en la instrucción `inicio, *cuerpo, final = secuencia`?
> Desempaqueta la secuencia asignando el primer elemento a `inicio`, el último a `final` y empaqueta todos los elementos intermedios en una lista asignada a `cuerpo`, sin importar cuántos elementos contenga la secuencia.

> [!question]- ¿Cuál es la diferencia entre una estructura secuencial y una no secuencial en Python?
> Las estructuras secuenciales conservan un orden posicional estricto accesible por índice numérico (como listas y tuplas), mientras que las no secuenciales no garantizan un orden posicional y optimizan la búsqueda directa mediante tablas de *hash* (como diccionarios y conjuntos).
