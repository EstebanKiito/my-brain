---
ramo: "Introducción a la Programación"
tema: "Funciones y módulos"
tags:
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Definir funciones propias: def y return]]"
---

# Return versus print y funciones booleanas

Una confusión muy común al empezar es creer que `print` y `return` hacen lo mismo, porque "ambos muestran el resultado". No es así, y entender la diferencia es clave para escribir funciones útiles. Esta nota también muestra las **funciones booleanas**, que responden preguntas de sí o no.

## `return` entrega, `print` muestra

Compárense dos versiones del factorial (n! = 1 · 2 · … · n):

```python
def factorial(n):          # retorna
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    return producto

def factorialp(n):         # imprime
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    print(producto)
```

| | `factorial` (con `return`) | `factorialp` (con `print`) |
|---|---|---|
| ¿Muestra algo en pantalla? | No, por sí sola | Sí |
| ¿Entrega el valor a quien la llama? | Sí | No (entrega `None`) |
| ¿Se puede usar en un cálculo? | `factorial(5) * 2` → 240 | `factorialp(5) * 2` → error |
| Para mostrarla | `print(factorial(5))` | `factorialp(5)` |

```python
def factorial(n):
    producto = 1
    for i in range(1, n + 1):
        producto *= i
    return producto

for i in range(1, 5):
    print(f"factorial({i}) = {factorial(i)}")
combinaciones = factorial(5) // (factorial(2) * factorial(3))
print(combinaciones)
```

```
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
10
```

Con `factorialp` el cálculo de `combinaciones` sería imposible: el número se mostraría en pantalla y se perdería.

> [!tip] Regla
> `print` es para comunicarse con **la persona** que usa el programa. `return` es para comunicarse con **el resto del programa**. Si el enunciado dice "una función que *entregue* / *retorne*…", va `return`.

## `return` termina la función

Al ejecutar `return`, la función **termina inmediatamente** y vuelve al lugar donde fue llamada, aunque haya un ciclo a medio camino. Esto se aprovecha para responder apenas se sabe la respuesta.

## Funciones booleanas

Una **función booleana** retorna `True` o `False`. Por ejemplo, ¿es `num` un número primo? Se busca un divisor entre 2 y `num - 1`; si aparece uno, ya se sabe que no es primo:

```python
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False      # encontró un divisor: sale de inmediato
    return True               # terminó el ciclo sin divisores

for n in range(1, 20):
    if es_primo(n):
        print(n, end=" ")
print()
```

```
2 3 5 7 11 13 17 19
```

Como retorna un `bool`, se usa directo en un `if`: `if es_primo(n):` se lee casi como en español.

> [!warning] El `return True` va fuera del ciclo
> Si se escribe `return True` dentro del `for` (en un `else`), la función respondería después de probar solo el primer divisor. Solo se puede afirmar que es primo **después** de revisar todos los candidatos.

## Dividir para conquistar: primos relativos

Dos números son **primos relativos** si no tienen ningún divisor común mayor que 1. Para mostrar todos los pares entre 2 y 10, primero se escribe el programa principal **suponiendo** que ya existe la función `primos_relativos(x, y)`, y después se escribe la función:

```python
def primos_relativos(x, y):
    for d in range(2, min(x, y) + 1):
        if x % d == 0 and y % d == 0:
            return False
    return True

for i in range(2, 6):
    for j in range(i + 1, 7):
        if primos_relativos(i, j):
            print(i, j)
```

Separar el problema así permite pensar una cosa a la vez: primero cómo recorrer los pares, después cómo saber si un par sirve.

## Una función que no retorna nada

Una función sin `return` (o con un `return` solo, sin valor) también es válida: sirve para realizar una acción, como mostrar un menú. `return` sin valor se usa para **salir antes** de la función.

## Preguntas de repaso

> [!question]- ¿Qué muestra `x = factorialp(3)` seguido de `print(x)`?
> Primero muestra `6` (lo imprime la función) y después `None`, porque `factorialp` no retorna nada y `x` queda vacía.

> [!question]- ¿Por qué `es_primo` puede retornar `False` dentro del ciclo pero `True` solo al final?
> Para decir que no es primo basta encontrar un divisor. Para decir que sí lo es, hay que haber revisado todos los candidatos sin encontrar ninguno.

> [!question]- Si el enunciado pide "una función que muestre en pantalla un saludo", ¿usarías `print` o `return`?
> `print`, porque el objetivo es mostrar algo a la persona, no entregar un valor al programa.
