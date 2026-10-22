---
ramo: "Introducción a la Programación"
tema: "Condicionales"
tags:
  - programacion/control-de-flujo
  - origen/complemento
prerrequisitos:
  - "[[01 - If, else e indentación]]"
  - "[[02 - Condiciones compuestas: and, or y not]]"
---

# Elif, ifs anidados y orden de las condiciones

`if`/`else` sirve cuando hay dos caminos. Pero muchos problemas tienen **varios** casos: clasificar la calidad del aire, poner un concepto según la nota, decidir el precio según la edad. Esta nota muestra tres formas de escribirlo y por qué `elif` suele ser la mejor.

## El problema: calidad del aire

Una estación de monitoreo entrega un valor y hay que clasificarlo:

| Valor | Clasificación |
|---|---|
| 0 a 99 | bueno |
| 100 a 199 | regular |
| 200 a 299 | alerta |
| 300 a 499 | preemergencia |
| 500 o más | emergencia |
| negativo | fuera de rango |

## Forma 1: ifs anidados

Un `if` puede ir **dentro** del bloque de otro (anidado). Cada `else` abre una nueva pregunta:

```python
valor = int(input("Ingresar valor estacion: "))
if 0 <= valor <= 99:
    print("bueno")
else:
    if 100 <= valor <= 199:
        print("regular")
    else:
        print("alerta, preemergencia, ...")  # y así sigue anidando
```

Funciona, pero con cinco casos el código se va corriendo hacia la derecha y se vuelve difícil de leer.

## Forma 2: solo ifs sueltos

Otra opción es escribir cinco `if` independientes, uno por rango, sin `else`. Python **evalúa todos**, aunque ya haya encontrado el caso correcto. Funciona solo si los rangos no se pisan; si dos condiciones se cumplieran a la vez se mostrarían dos mensajes, y no hay forma cómoda de escribir "en cualquier otro caso".

## Forma 3: `elif` (la recomendada)

`elif` significa "si no, y si…". Encadena las preguntas y **se detiene en la primera que se cumple**:

```python
valor = int(input("Ingresar valor estacion: "))
if 0 <= valor <= 99:
    print("bueno")
elif 100 <= valor <= 199:
    print("regular")
elif 200 <= valor <= 299:
    print("alerta")
elif 300 <= valor <= 499:
    print("preemergencia")
elif valor >= 500:
    print("emergencia")
else:
    print("fuera de rango")
print("fin")
```

> [!tip] Regla de `elif`
> En una cadena `if` / `elif` / `else` se ejecuta **exactamente un** bloque: el de la primera condición verdadera, o el `else` si ninguna se cumple.

## El orden de las condiciones importa

Como `elif` ya sabe que las condiciones anteriores fallaron, se pueden escribir condiciones más cortas si se ordenan bien, de mayor a menor:

```python
valor = 250
if valor >= 500:
    print("emergencia")
elif valor >= 300:     # aquí ya se sabe que valor < 500
    print("preemergencia")
elif valor >= 200:     # y aquí, que valor < 300
    print("alerta")
elif valor >= 100:
    print("regular")
elif valor >= 0:
    print("bueno")
else:
    print("fuera de rango")
```

```
alerta
```

> [!warning] Una condición amplia puede tapar a las demás
> Si se escribe primero `if valor >= 0:` y después `elif valor >= 500:`, un valor de 600 entra al primer caso ("bueno") y nunca llega al de emergencia. Las condiciones más específicas o más exigentes van primero.

## Ejemplo: año bisiesto

Un año es bisiesto si es divisible por 4, salvo que sea divisible por 100; pero si es divisible por 400, sí es bisiesto. Ordenando del caso más específico al más general:

```python
anio = 1996
if anio % 400 == 0:
    print("Es bisiesto")
elif anio % 100 == 0:
    print("No es bisiesto")
elif anio % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
```

El año 2000 es bisiesto (divisible por 400), 1900 no lo es (divisible por 100 pero no por 400) y 1996 sí (divisible por 4).

## Combinar con condiciones compuestas

Con tres estaciones, se decreta un estado si **al menos dos** estaciones superan el umbral. Cada `elif` combina `and` y `or`:

```python
e1, e2, e3 = 124, 333, 201   # muestra: Alerta
if (e1 >= 500 and e2 >= 500) or (e1 >= 500 and e3 >= 500) or (e2 >= 500 and e3 >= 500):
    print("EMERGENCIA")
elif (e1 >= 300 and e2 >= 300) or (e1 >= 300 and e3 >= 300) or (e2 >= 300 and e3 >= 300):
    print("Preemergencia")
elif (e1 >= 200 and e2 >= 200) or (e1 >= 200 and e3 >= 200) or (e2 >= 200 and e3 >= 200):
    print("Alerta")
else:
    print("No hay situacion de excepcion")
```

Gracias al orden, si hay emergencia no se revisa la preemergencia.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre escribir varios `if` seguidos y una cadena con `elif`?
> Con varios `if`, Python revisa todas las condiciones y puede ejecutar más de un bloque. Con `elif`, se detiene en la primera verdadera y ejecuta solo un bloque.

> [!question]- ¿Por qué en la versión ordenada de mayor a menor basta con `valor >= 300` para preemergencia?
> Porque a ese `elif` solo se llega si `valor >= 500` fue falso; o sea, ya se sabe que el valor es menor que 500.

> [!question]- ¿Qué pasaría con el año bisiesto si se revisa primero `anio % 4 == 0`?
> El año 1900 (divisible por 4) se declararía bisiesto sin llegar a revisar la excepción del 100. Los casos más específicos deben ir primero.
