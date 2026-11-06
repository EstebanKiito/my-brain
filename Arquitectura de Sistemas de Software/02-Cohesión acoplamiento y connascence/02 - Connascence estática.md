---
ramo: "Arquitectura de Sistemas de Software"
tema: "Cohesión acoplamiento y connascence"
tags:
  - arquisis/fundamentos
  - arquisis/connascence
  - origen/complemento
prerrequisitos:
  - "[[01 - Cohesión y acoplamiento entre módulos]]"
---

# Connascence estática

"Acoplamiento alto o bajo" es una medida gruesa. La **connascence** la afina: no solo dice que dos componentes dependen entre sí, sino **en qué tienen que ponerse de acuerdo** y qué tan difícil es cambiar ese acuerdo. No es buena ni mala en sí: indica qué tan fácil o difícil será modificar el sistema.

## Definición

> [!tip] Connascence (Meilir Page-Jones)
> "Dos componentes son connascentes si un cambio en uno requeriría modificar el otro para mantener la correctitud general del sistema."

- Si un cambio en A obliga a cambiar B, comparten connascence. Si son muchos y difíciles los cambios, la connascence es de **grado alto**.
- Si tienen al menos un punto de conexión, tienen algún grado de connascence.
- Si no interactúan en absoluto, su connascence es **cero**: están completamente separados.

![Escala de tipos de connascence, estáticos y dinámicos](adjuntos/Tipos%20de%20connascence%20de%20menor%20a%20mayor%20fuerza.png)

> [!example]- Transcripción de la imagen
> - Una lista de tipos ordenada por fuerza, de verde a rojo.
> - **Static**: Name, Type, Meaning, Position, Algorithm.
> - **Dynamic**: Execution, Timing, Value, Identity.
> - A la derecha, una flecha **Strength** que va de **Low (good)** arriba a **High (bad)** abajo.

La connascence **estática** es **observable en el código**, sin ejecutarlo. Hay cinco tipos, de más débil a más fuerte.

## Name (nombre)

Deben ponerse de acuerdo en **el nombre** de una entidad. Es la más simple de ver y la más débil.

```python
# módulo A                 # módulo B
def fun_a(): ...           import A
                           A.fun_a()
```

Si A renombra `fun_a`, B debe cambiar. Pero un IDE lo detecta y lo refactoriza automáticamente.

## Type (tipo)

Deben ponerse de acuerdo en **el tipo** de una entidad, sobre todo en lenguajes tipados.

```python
# A espera un objeto date       # B le pasa un string
def fun_a(fecha: date): ...     A.fun_a("2026-08-11")   # se rompe: debía construir date(2026, 8, 11)
```

## Meaning (significado)

Deben ponerse de acuerdo en **el significado de valores particulares**, los llamados "valores mágicos".

```python
# A: éxito es 0            # B: éxito es 1
TRUE, FALSE = 0, 1         TRUE, FALSE = 1, 0
return TRUE                if A.fun_a() == TRUE: ...   # interpreta al revés
```

Si A cambia qué significa un código de estado, B interpreta mal sin que nada falle visiblemente. **Solución:** constantes o enums compartidos con nombre, que convierten la connascence de significado en una de nombre.

## Position (posición)

Deben ponerse de acuerdo en **el orden** de los valores.

```python
def fun_a(fecha, num): ...
A.fun_a(1, fecha)            # orden equivocado: difícil de encontrar
A.fun_a(num=1, fecha=fecha)  # solución: argumentos con nombre
```

Lo mismo pasa en las APIs: si un endpoint espera los parámetros en cierto orden y se mueve uno, el cliente debe moverse también.

## Algorithm (algoritmo)

Deben ponerse de acuerdo en **un algoritmo particular**. Ejemplos:
- A y B usan el mismo `code`/`decode`: si A cambia el algoritmo, B ya no puede decodificar.
- Cifrado o hashing: A guarda `123 = ENC("DATE", secreto)` y B compara con `ENC(DATE, secreto)`. Ambos deben usar exactamente el mismo algoritmo y la misma configuración.

![Componentes A y B que dependen de un mismo componente C](adjuntos/Connascence%20de%20algoritmo%20con%20un%20componente%20común.png)

> [!example]- Transcripción de la imagen
> - Croquis: el componente **A** se conecta con **B** mediante una interfaz.
> - Ambos se conectan también a un tercer componente **C**, que representa la librería o el algoritmo común que usan.

**Mitigación:** poner el algoritmo en un solo componente o librería compartida (C), para que haya una única implementación.

| Tipo | Acuerdo sobre | Mitigación típica |
|---|---|---|
| Name | Nombres | Refactoring automático del IDE |
| Type | Tipos | Tipado estático, contratos (OpenAPI, protobuf) |
| Meaning | Valores mágicos | Enums o constantes con nombre |
| Position | Orden de los parámetros | Argumentos con nombre, objetos en vez de listas |
| Algorithm | El mismo algoritmo | Una librería o un servicio único |

## Preguntas de repaso

> [!question]- Defina connascence y explique cuándo es cero.
> Dos componentes son connascentes si un cambio en uno obliga a modificar el otro para que el sistema siga correcto. Es cero cuando no interactúan en absoluto: ningún cambio en uno afecta al otro.

> [!question]- Ordene de más débil a más fuerte los cinco tipos estáticos.
> Name < Type < Meaning < Position < Algorithm.

> [!question]- Una función se llama `procesar(1, fecha)` cuando la firma es `procesar(fecha, num)`. ¿Qué tipo de connascence hay y cómo se reduce?
> Connascence de posición: ambos lados deben acordar el orden de los argumentos. Se reduce usando argumentos con nombre (`procesar(num=1, fecha=fecha)`), que la convierten en connascence de nombre, más débil.

> [!question]- ¿Por qué la connascence de significado es peligrosa y cómo se corrige?
> Porque el error no falla visiblemente: B interpreta un valor con otro significado y produce resultados incorrectos en silencio. Se corrige con enums o constantes compartidas con nombre (`Estado.EXITO`), que la transforman en connascence de nombre.

> [!question]- Dos servicios validan contraseñas aplicando el mismo hash. ¿Qué connascence tienen y qué riesgo hay?
> Connascence de algoritmo: ambos deben usar exactamente el mismo algoritmo y la misma configuración. Si uno cambia (por ejemplo, de SHA-1 a bcrypt) y el otro no, las validaciones fallan. Conviene centralizar el hashing en un solo componente o librería.

> [!question]- V o F: "La connascence de nombre es la más problemática porque está en todo el código".
> Falso. Es la más débil y la más fácil de manejar: los IDE renombran automáticamente y los errores aparecen al compilar o al importar. Las más fuertes, como las dinámicas, son más difíciles de detectar.

> [!question]- ¿Qué significa que la connascence estática sea "observable en el código"?
> Que se puede detectar leyendo o analizando el código fuente sin ejecutarlo: nombres, tipos, valores, orden de argumentos y algoritmos compartidos. La dinámica, en cambio, solo aparece al ejecutar el sistema.
