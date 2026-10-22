---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/funcional
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Repaso de Python: tipos, funciones y módulos]]"
  - "[[07 - Decoradores: funciones de primera clase y sintaxis arroba]]"
---

# Paradigma funcional y funciones puras

En los programas imperativos tradicionales indicamos a la computadora *cómo* hacer las cosas paso a paso, modificando variables globales y alterando el estado en cada línea. La programación funcional propone un enfoque alternativo: describir *qué* queremos transformar mediante funciones matemáticas predecibles y sin efectos colaterales.

## Qué es la Programación Funcional

La **programación funcional** es un paradigma de programación declarativo donde el cómputo se modela como la evaluación de funciones matemáticas, evitando el cambio de estado mutable y la alteración de datos fuera del ámbito local.

Python es un lenguaje multiparadigma: no es puramente funcional (como Haskell), pero provee herramientas nativas que permiten aplicar este estilo de forma limpia y eficiente.

## Funciones puras y efectos colaterales

Una **función pura** (*pure function*) cumple dos propiedades innegociables:

1. **Determinismo:** dados los mismos argumentos de entrada, retorna **siempre el mismo resultado**, sin depender de variables externas que puedan cambiar en el tiempo.
2. **Sin efectos colaterales (*side effects*):** no modifica ninguna variable fuera de su cuerpo, no muta los objetos recibidos por parámetro, no modifica variables globales y no realiza operaciones de I/O ocultas (como imprimir en consola o escribir en un archivo).

![Funciones puras y efectos colaterales](adjuntos/Funciones%20puras%20y%20efectos%20colaterales.png)

> [!example]- Transcripción de la imagen
> - Comparación conceptual de pureza:
>   - **Función impura:** interactúa con el mundo exterior leyendo o modificando variables globales y estado del sistema.
>   - **Función pura:** caja negra aislada que solo toma entradas por sus parámetros y produce salidas mediante su valor de retorno, sin tocar el entorno exterior.

```python
# Función impura: depende de una variable global y produce efecto colateral
impuesto_global = 0.19

def calcular_total_impuro(precio: float) -> float:
    return precio * (1 + impuesto_global)

# Función pura: solo depende de sus argumentos explícitos
def calcular_total_puro(precio: float, impuesto: float) -> float:
    return precio * (1 + impuesto)

print(f"Total puro: ${calcular_total_puro(1000.0, 0.19):.2f}")
```

```
Total puro: $1190.00
```

## Flujo de datos y tuberías (pipelines)

Al trabajar con funciones puras, los programas se construyen conectando funciones en serie como tuberías (*data flow*): la salida de una función es la entrada directa de la siguiente, transformando los datos sin alterar las estructuras originales:

![Flujo de datos en programación funcional](adjuntos/Flujo%20de%20datos%20en%20programaci%C3%B3n%20funcional.png)

> [!example]- Transcripción de la imagen
> - Diagrama de tubería de datos: los datos fluyen secuencialmente a través de etapas de transformación independientes (`f(x)`, luego `g(x)`, luego `h(x)`) produciendo el resultado final sin modificar el origen.

```python
def limpiar_texto(texto: str) -> str:
    return texto.strip().lower()

def eliminar_puntuacion(texto: str) -> str:
    return "".join(c for c in texto if c.isalnum() or c.isspace())

def contar_palabras(texto: str) -> int:
    return len(texto.split())

# Composición funcional en cadena
frase_cruda = "  ¡Hola, mundo de la Programación Avanzada!  "
palabras = contar_palabras(eliminar_puntuacion(limpiar_texto(frase_cruda)))
print(f"Total de palabras procesadas: {palabras}")
```

```
Total de palabras procesadas: 6
```

> [!tip] Facilidad de pruebas unitarias y concurrencia
> Las funciones puras son triviales de probar mediante tests automatizados: al no depender de base de datos ni de estado global, basta con entregar entradas y verificar salidas. Además, son inherentemente seguras en entornos multihilo porque nunca entran en colisión por memoria compartida.

> [!warning] Mudar listas recibidas por parámetro es un efecto colateral
> Si una función ejecuta `lista.append(x)` o `lista.sort()` sobre un argumento recibido, está mutando el objeto original del invocador. Para mantener la pureza, debe retornar una nueva lista o una copia: `sorted(lista)`.

## Preguntas de repaso

> [!question]- ¿Qué dos condiciones debe cumplir estrictamente una función para ser clasificada como función pura?
> Debe ser determinista (mismas entradas siempre producen las mismas salidas) y carecer por completo de efectos colaterales (no alterar estado global, variables mutables externas ni realizar I/O no declarado).

> [!question]- ¿Por qué una función que llama a `random.random()` o a `datetime.now()` no es considerada una función pura?
> Porque viola la regla del determinismo: cada vez que se invoca entrega un resultado distinto sin que hayan variado sus argumentos de entrada.

> [!question]- ¿Cuál es la ventaja de diseñar pipelines de funciones puras frente a modificar un objeto acumulador mutable?
> Cada etapa de transformación es independiente, componible y fácil de razonar; además, la estructura de datos original permanece inalterada para otros consumidores.

> [!question]- ¿Por qué las funciones puras eliminan las condiciones de carrera (*race conditions*) en entornos concurrentes?
> Porque al no modificar memoria ni variables compartidas y basarse en datos inmutables, múltiples hilos pueden ejecutarlas en paralelo sin riesgo de sobrescribir el estado de otro hilo.
