---
ramo: "Introducción a la Programación"
tema: "Ciclos"
tags:
  - programacion/ciclos
  - origen/complemento
prerrequisitos:
  - "[[03 - Centinela, banderas y break]]"
  - "[[03 - Operadores aritméticos]]"
---

# Patrones con ciclos: máximo, mínimo y dígitos

Hay ciclos que aparecen una y otra vez con pocas variaciones. Reconocer estos **patrones** ahorra mucho trabajo: en vez de inventar la solución desde cero, se adapta una que ya se conoce. Esta nota presenta dos muy frecuentes: buscar el mejor valor y recorrer los dígitos de un número.

## Patrón 1: buscar el máximo o el mínimo

Idea: llevar una variable con **el mejor valor visto hasta ahora** y compararla con cada dato nuevo. Si el nuevo es mejor, se reemplaza.

```python
mejor = 0          # menor que cualquier nota posible
nota = float(input("nota? "))
while nota != -1:
    if nota > mejor:
        mejor = nota
    nota = float(input("nota? "))
print("mejor =", mejor)
```

```
nota? 5.0
nota? 4.0
nota? -1
mejor = 5.0
```

> [!warning] El valor inicial
> Para el **máximo**, se parte con un valor más chico que cualquier dato posible (0 para notas de 1 a 7). Para el **mínimo**, con uno más grande que cualquier dato. Otra opción, que funciona siempre, es partir con el **primer dato** leído.

### Ejemplo: el ganador de una carrera
Se ingresan horas de llegada en formato `hhmmss` (por ejemplo `103015` = 10:30:15) hasta escribir -1. Gana quien llega antes, así que se busca el **mínimo** y además se recuerda **quién** lo tenía:

```python
menor_tiempo = 240000    # más tarde que cualquier hora del día
ganador = 0
numero = 1
llegada = int(input(f"Hora de llegada #{numero}? "))
while llegada != -1:
    if llegada < menor_tiempo:
        menor_tiempo = llegada
        ganador = numero
    numero += 1
    llegada = int(input(f"Hora de llegada #{numero}? "))
print(f"Gana el #{ganador} con hora {menor_tiempo}")
```

Para calcular cuánto tardó el último respecto del primero, cada hora se pasa a segundos con `//` y `%`: segundos = `t % 100`, minutos = `(t // 100) % 100`, horas = `t // 10000`. Ese cálculo se repite para cada hora, y es justo la motivación para escribir **funciones propias** (siguiente tema).

## Patrón 2: recorrer los dígitos de un número

`n % 10` da el **último dígito** y `n // 10` lo **quita**. Repitiendo ambos pasos hasta que el número llegue a 0 se recorren todos los dígitos, de derecha a izquierda:

```python
n = 347
while n > 0:
    print(n % 10)
    n = n // 10
```

```
7
4
3
```

### Ejemplo: dígito verificador del RUT
El dígito verificador del RUT chileno se calcula así:
1. Multiplicar cada dígito, **de derecha a izquierda**, por 2, 3, 4, 5, 6, 7, y volver a empezar en 2.
2. Sumar los productos.
3. Calcular el resto de dividir esa suma por 11.
4. El dígito es `11 - resto`; si da 10 es `K`, y si da 11 es `0`.

Con el RUT 11.222.333: los productos suman 68, 68 % 11 = 2, y 11 − 2 = **9**.

```python
rut = 11222333
mult = 2
suma = 0
while rut > 0:
    ultimo = rut % 10
    suma += ultimo * mult
    rut = rut // 10
    mult += 1
    if mult == 8:        # después del 7 vuelve al 2
        mult = 2
dv = 11 - suma % 11
if dv == 10:
    print("K")
elif dv == 11:
    print("0")
else:
    print(dv)
```

```
9
```

El ciclo combina tres cosas ya vistas: un acumulador (`suma`), una variable que cambia en cada vuelta (`mult`, que "da la vuelta" del 7 al 2) y el patrón de dígitos.

## Ciclos dentro de ciclos

Un ciclo puede ir dentro de otro. En el juego del **cerdo** (*pig*), dos jugadores se turnan hasta que uno llega a 100 puntos (ciclo externo); en cada turno, el jugador lanza un dado las veces que quiera, acumulando puntos, pero si saca un 1 pierde los puntos del turno (ciclo interno). El ciclo interno se ejecuta completo en cada vuelta del externo.

## Preguntas de repaso

> [!question]- ¿Por qué el mínimo de la carrera parte en 240000 y no en 0?
> Porque se busca el valor más chico: si se partiera en 0, ninguna hora sería menor y el mínimo quedaría en 0. 240000 es mayor que cualquier hora válida, así que la primera llegada siempre lo reemplaza.

> [!question]- ¿Qué hacen `n % 10` y `n // 10` con `n = 2024`?
> `2024 % 10` da 4 (el último dígito) y `2024 // 10` da 202 (el número sin ese dígito).

> [!question]- En el RUT, ¿para qué sirve `if mult == 8: mult = 2`?
> Para que los multiplicadores sigan la secuencia 2, 3, 4, 5, 6, 7 y luego vuelvan a 2, como exige el algoritmo.
