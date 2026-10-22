---
ramo: "Introducción a la Programación"
tema: "Funciones y módulos"
tags:
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones existentes y el módulo math]]"
  - "[[04 - Patrones con ciclos: máximo, mínimo y dígitos]]"
---

# Definir funciones propias: def y return

En el problema de la carrera, para calcular cuánto tardó el último respecto del primero había que pasar **dos** horas `hhmmss` a segundos. El mismo cálculo de tres líneas se escribía dos veces, cambiando solo el nombre de la variable. Cuando un cálculo se repite, lo correcto es convertirlo en una **función propia**: escribirlo una vez, ponerle nombre y usarlo las veces que haga falta.

## Anatomía de una función

```python
def segundos(hora):
    s = hora % 100
    m = (hora // 100) % 100
    h = hora // 10000
    return s + m * 60 + h * 60 * 60
```

| Parte | En el ejemplo | Qué significa |
|---|---|---|
| `def` | `def` | "Voy a definir una función" |
| Nombre | `segundos` | Cómo se llamará; mismas reglas que las variables |
| Parámetros | `(hora)` | Los datos que recibe; dentro de la función se usan como variables |
| Cuerpo | Las líneas con sangría | Lo que hace la función |
| `return` | `return s + m*60 + h*3600` | El resultado que entrega a quien la llamó |

Definir la función **no ejecuta nada**: solo le enseña a Python qué hacer cuando alguien la **llame**. Llamarla es escribir su nombre con los argumentos entre paréntesis:

```python
def segundos(hora):
    s = hora % 100
    m = (hora // 100) % 100
    h = hora // 10000
    return s + m * 60 + h * 60 * 60

primero = 135949     # 13:59:49
ultimo = 140301      # 14:03:01
print(segundos(ultimo) - segundos(primero))
```

```
192
```

Al llamar `segundos(ultimo)`, el parámetro `hora` toma el valor `140301`, se ejecuta el cuerpo y el `return` entrega `50581`. Ese valor reemplaza a la llamada en la expresión, igual que con `int("42")`.

## Cómo se ordena un programa con funciones

```python
import math                               # 1. imports

def area_circulo(r):                      # 2. definiciones de funciones
    return math.pi * r * r

def area_triangulo(a, b, c):              # fórmula de Herón
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

a, b, c = 3, 4, 5                         # 3. programa principal
radio = max(a, b, c) / 2
print(round(area_circulo(radio) - area_triangulo(a, b, c), 2))
```

```
13.63
```

Las funciones se definen **antes** de usarse; si el programa principal llama a una función que todavía no se ha definido más arriba, Python da `NameError`.

## Ejemplo: sumatoria

Una función `sumatoria(n)` que entregue 1 + 2 + … + n, y 0 si `n` es negativo:

```python
def sumatoria(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(sumatoria(4))    # 10
print(sumatoria(-4))   # 0: range(1, -3) no genera números
```

## Variables locales

Las variables creadas dentro de una función (`s`, `m`, `h` en `segundos`) son **locales**: existen solo mientras la función se ejecuta y no se ven desde fuera. Por eso dos funciones distintas pueden tener cada una su propia `s` sin pisarse.

```text
def doble(x):
    resultado = x * 2
    return resultado

doble(5)
print(resultado)   # NameError: resultado no existe fuera de la función
```

> [!warning] El resultado hay que guardarlo
> Llamar `doble(5)` sola en una línea calcula 10 y lo pierde. Para usarlo hay que guardarlo (`r = doble(5)`) o usarlo directamente (`print(doble(5))`).

## ¿Por qué usar funciones?

- **Dividir para conquistar:** un problema grande se parte en problemas chicos, cada uno resuelto por una función.
- **Eliminar código repetido:** si hay que corregir algo, se corrige en un solo lugar.
- **Legibilidad:** `segundos(ultimo) - segundos(primero)` se entiende sin leer los cálculos.
- **Reutilización:** una función bien hecha sirve en otros programas.

> [!tip] Regla
> Una función recibe datos por sus **parámetros** y entrega su resultado con **`return`**. Por eso, en general, dentro de una función no se usa `input` para obtener los datos ni `print` para entregar el resultado.

## Preguntas de repaso

> [!question]- ¿Qué pasa al ejecutar un archivo que solo contiene la definición `def segundos(hora): ...`?
> Nada visible: definir una función solo la deja disponible. Su código recién corre cuando alguien la llama.

> [!question]- Al llamar `segundos(140301)`, ¿qué valor toma `hora`?
> `140301`. El argumento de la llamada se copia en el parámetro de la función.

> [!question]- ¿Por qué no se puede usar `s` de la función `segundos` en el programa principal?
> Porque es una variable local: solo existe mientras la función se está ejecutando.

> [!question]- ¿Por qué conviene que `sumatoria` reciba `n` como parámetro en vez de pedirlo con `input`?
> Porque así sirve en cualquier situación: con un número escrito por el usuario, leído de un archivo o calculado por otra parte del programa.
