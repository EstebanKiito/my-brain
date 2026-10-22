---
ramo: "Introducción a la Programación"
tema: "Primeros pasos en Python"
tags:
  - programacion/python
  - origen/complemento
prerrequisitos:
  - "[[02 - Variables, input y conversión de tipos]]"
---

# Operadores aritméticos

Con variables numéricas se puede calcular. Python tiene los operadores de la calculadora y dos muy útiles que no son tan conocidos: la **división entera** (`//`) y el **resto** (`%`). Aparecen en muchísimos ejercicios del curso.

## La tabla de operadores

| Operador | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `7 + 2` | `9` |
| `-` | Resta | `7 - 2` | `5` |
| `*` | Multiplicación | `7 * 2` | `14` |
| `/` | División (siempre da `float`) | `7 / 2` | `3.5` |
| `//` | División entera (descarta los decimales) | `7 // 2` | `3` |
| `%` | Resto (módulo) de la división | `7 % 2` | `1` |
| `**` | Potencia | `7 ** 2` | `49` |

Ojo: `/` **siempre** entrega un decimal, incluso si la división es exacta: `6 / 2` da `3.0`.

## `//` y `%`: repartir en partes iguales

Hay 25 chocolates para 4 personas. Cada una recibe `25 // 4 = 6` y sobra `25 % 4 = 1`. Es la división "con resto" del colegio: 25 = 4 · 6 + 1.

```python
chocolates = int(input("Cuantos chocolates hay? "))
personas = int(input("Cuantas personas hay? "))
print(f"Repartir {chocolates // personas} a cada uno, sobran {chocolates % personas}")
```

```
Cuantos chocolates hay? 25
Cuantas personas hay? 4
Repartir 6 a cada uno, sobran 1
```

> [!tip] Usos típicos de `%` y `//`
> - `n % 2 == 0` dice si `n` es **par**.
> - `n % 10` entrega el **último dígito** de `n` (`347 % 10` es `7`).
> - `n // 10` **quita** el último dígito (`347 // 10` es `34`).
> - `segundos // 60` y `segundos % 60` separan minutos y segundos.

## Prioridad de los operadores

Igual que en matemáticas, no todo se calcula de izquierda a derecha:

| Prioridad | Operadores |
|---|---|
| 1 (primero) | Paréntesis `( )` |
| 2 | Potencia `**` |
| 3 | `*`, `/`, `//`, `%` |
| 4 (último) | `+`, `-` |

Operadores con la misma prioridad se evalúan de izquierda a derecha (excepto la potencia, que va de derecha a izquierda).

```python
print(2 + 3 * 4)     # 14, primero 3 * 4
print((2 + 3) * 4)   # 20, el paréntesis manda
print(10 - 4 - 3)    # 3, de izquierda a derecha: (10 - 4) - 3
```

> [!warning] Ante la duda, paréntesis
> Para convertir Fahrenheit a Celsius, `c = f - 32 * 5 / 9` está **mal**: multiplica antes de restar. Lo correcto es `c = (f - 32) * 5 / 9`. Los paréntesis extra nunca hacen daño y hacen el código más claro.

## Dos sorpresas con los decimales

**1. `0.1 + 0.2` no da exactamente `0.3`.**

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

El computador guarda los `float` en binario, y números como 0,1 no tienen representación binaria exacta (igual que 1/3 no tiene representación decimal exacta: 0,333…). Por eso aparecen pequeños errores. No es un bug de Python; pasa en casi todos los lenguajes. Por eso no conviene comparar decimales con `==`.

**2. `round` redondea "al par" en los casos justo a la mitad.**

```python
print(round(2.5))   # 2
print(round(3.5))   # 4
```

Desde Python 3, cuando un número está exactamente a la mitad, `round` elige el entero **par** más cercano (el llamado "redondeo del banquero"). Así, en promedio, los redondeos hacia arriba y hacia abajo se compensan.

## Preguntas de repaso

> [!question]- ¿Cuánto vale `17 // 5` y `17 % 5`? ¿Qué relación tienen con 17?
> `17 // 5` es `3` y `17 % 5` es `2`. Se cumple `17 = 5 * 3 + 2`: el cociente por el divisor más el resto da el número original.

> [!question]- ¿Cómo se sabe si un número es par usando operadores?
> Se calcula el resto de dividirlo por 2: si `n % 2` es `0`, es par; si es `1`, es impar.

> [!question]- ¿Por qué `(f - 32) * 5 / 9` y `f - 32 * 5 / 9` dan resultados distintos?
> Porque la multiplicación y la división tienen más prioridad que la resta. Sin paréntesis, Python calcula primero `32 * 5 / 9` y luego lo resta de `f`.

> [!question]- ¿Por qué no es buena idea preguntar si `0.1 + 0.2 == 0.3`?
> Porque los decimales se guardan de forma aproximada y la suma da `0.30000000000000004`, así que la comparación resulta `False`.
