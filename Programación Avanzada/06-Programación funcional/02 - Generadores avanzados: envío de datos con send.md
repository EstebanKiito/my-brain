---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/generadores
  - programacion/iteradores
  - origen/complemento
prerrequisitos:
  - "[[05 - Generadores y la palabra clave yield]]"
---

# Generadores avanzados: envío de datos con send

Hasta ahora hemos utilizado las funciones generadoras como emisores unidireccionales de datos: el generador produce valores hacia el exterior mediante `yield` y el programa los consume con `next()`. Sin embargo, en Python los generadores son canales de comunicación **bidireccionales**.

## La expresión yield como punto de entrada

En Python, `yield` no es solo una sentencia: es una **expresión** que puede recibir valores desde el exterior y asignarlos a una variable local dentro de la función generadora mediante la sintaxis: `valor_recibido = yield valor_enviado`.

Cuando el generador alcanza esa línea:
1. Emite `valor_enviado` hacia quien lo invocó.
2. Suspende su ejecución en ese punto exacto.
3. Al reanudarse, la expresión `yield` se evalúa al dato inyectado desde afuera, guardándolo en `valor_recibido`.

## El método send() y el cebado inicial

Para enviar información hacia el interior de un generador pausado se utiliza el método **`generador.send(valor)`**:

```python
def acumulador_interactivo():
    total = 0
    print("Acumulador iniciado.")
    while True:
        # Entrega 'total' hacia afuera y recibe 'monto' desde send()
        monto = yield total
        if monto is not None:
            total += monto


# 1. Instanciamos el generador
acc = acumulador_interactivo()

# 2. Cebado (priming): avanzar hasta el primer yield
primer_total = next(acc)  # o acc.send(None)
print(f"Total inicial: {primer_total}")

# 3. Enviar datos hacia el generador con .send()
print(f"Tras enviar 50:  {acc.send(50)}")
print(f"Tras enviar 100: {acc.send(100)}")
print(f"Tras enviar 25:  {acc.send(25)}")
```

```
Acumulador iniciado.
Total inicial: 0
Tras enviar 50:  50
Tras enviar 100: 150
Tras enviar 25:  175
```

> [!warning] El primer paso debe ser siempre next() o send(None)
> Un generador recién creado aún no ha iniciado su ejecución: no se encuentra detenido en ningún `yield`. Si intentas enviar un valor con `acc.send(50)` inmediatamente tras crearlo, Python lanzará una excepción: `TypeError: can't send non-None value to a just-started generator`. Siempre debes **cebar** el generador con `next(gen)` primero.

## Métodos de control: close() y throw()

Además de `.send()`, los generadores poseen dos métodos para gestionar su ciclo de vida:

- **`generador.close()`:** levanta una excepción interna de tipo `GeneratorExit` en el punto del `yield`, deteniendo el generador de forma controlada y liberando recursos.
- **`generador.throw(tipo_excepcion, mensaje)`:** inyecta una excepción en el punto pausado del generador, permitiendo que el generador la capture con un bloque `try-except` interno o aborte la ejecución:

```python
def monitor():
    try:
        while True:
            dato = yield "Esperando datos..."
            print(f"Procesando: {dato}")
    except GeneratorExit:
        print("Cerrando monitor limpiamente.")


m = monitor()
next(m)  # Cebado
m.send("Paquete #1")
m.close()
```

```
Procesando: Paquete #1
Cerrando monitor limpiamente.
```

> [!tip] La base de las corrutinas
> La capacidad de pausar la ejecución y transferir datos bidireccionalmente con `yield` y `.send()` constituye el fundamento teórico sobre el cual se construyó la programación asíncrona (`asyncio`) en Python.

## Preguntas de repaso

> [!question]- ¿Qué ocurre sintáctica y operativamente cuando se ejecuta `x = yield valor` dentro de un generador?
> El generador produce `valor` hacia el invocador y suspende su ejecución; cuando el invocador envía un dato con `.send(dato)`, el generador se reactiva y asigna ese `dato` a la variable `x`.

> [!question]- ¿Por qué falla la instrucción `gen.send(10)` si se llama inmediatamente después de instanciar el generador?
> Porque el generador aún no ha comenzado a ejecutarse ni ha alcanzado su primera expresión `yield`; por regla de lenguaje, solo se puede enviar `None` (o llamar a `next()`) para iniciar su ejecución.

> [!question]- ¿Qué excepción se levanta internamente dentro de un generador cuando se invoca el método `.close()`?
> Se levanta la excepción `GeneratorExit`, lo que permite ejecutar bloques `finally` o de limpieza antes de que el generador finalice definitivamente.

> [!question]- ¿Cuál es la diferencia entre reanudar un generador con `next(gen)` y hacerlo con `gen.send(valor)`?
> `next(gen)` equivale a ejecutar `gen.send(None)`, reanudando la función sin inyectar ningún valor específico (la expresión `yield` evalúa a `None`); mientras que `gen.send(valor)` inyecta un dato concreto en la expresión `yield`.
