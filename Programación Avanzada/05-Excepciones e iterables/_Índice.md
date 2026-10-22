# Excepciones e iterables — índice

Manejo robusto de errores y el protocolo de iteración en Python: errores sintácticos vs excepciones en tiempo de ejecución, bloques de control defensivo `try`, `except`, `else` y `finally`, levantamiento explícito con `raise` y diseño de excepciones personalizadas de negocio, la distinción formal entre iterables e iteradores con `StopIteration`, evaluación perezosa y funciones generadoras con `yield`, y construcción de listas ligadas mediante nodos e integración al protocolo de iteración.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cuatro notebooks principales y el notebook bonus de la sexta semana del curso (introducción a excepciones, levantamiento y manejo, iterables y generadores, listas ligadas y excepciones personalizadas), complementado con las diapositivas de excepciones.

## Orden de estudio
1. [[01 - Excepciones: errores en tiempo de ejecución y tipos comunes|Excepciones: errores en tiempo de ejecución]]: errores sintácticos vs excepciones, lectura de tracebacks y catálogo de excepciones estándar comunes.
2. [[02 - Manejo de excepciones: bloques try, except, else y finally|Manejo de excepciones]]: control con `try` y `except`, captura de múltiples excepciones, flujos limpios con `else` y liberación garantizada de recursos con `finally`.
3. [[03 - Levantamiento y excepciones personalizadas|Levantamiento y excepciones personalizadas]]: lanzamiento de errores con `raise`, árbol genealógico de `BaseException` y creación de excepciones propias heredando de `Exception`.
4. [[04 - Protocolo de iteración: iterables, iteradores y StopIteration|Protocolo de iteración]]: el funcionamiento interno del bucle `for`, diferencias entre iterables e iteradores, y métodos `__iter__`, `__next__` y `StopIteration`.
5. [[05 - Generadores y la palabra clave yield|Generadores y la palabra clave yield]]: evaluación perezosa (*lazy evaluation*), suspensión de funciones con `yield`, secuencias infinitas y expresiones generadoras.
6. [[06 - Listas ligadas: nodos y operaciones fundamentales|Listas ligadas: nodos y operaciones]]: estructura encadenada en memoria, clase `Nodo`, puntero `head`, e inserción y obtención de elementos.
7. [[07 - Listas ligadas iterables: integrando __iter__ y generadores|Listas ligadas iterables]]: integración del método `__iter__` con `yield`, recorrido en tiempo $O(N)$ y compatibilidad con `in`, `for` y `list()`.
