---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/encapsulamiento
  - origen/complemento
prerrequisitos:
  - "[[06 - Clases, objetos y variables de clase]]"
---

# Encapsulamiento y atributos privados

Un objeto tiene datos y métodos, pero no todos deberían ser tocados desde afuera. El **encapsulamiento** esconde los detalles internos de un objeto para que los demás solo usen lo que el programador quiso ofrecer. Así hay menos errores y el código es más limpio.

## La idea: ocultar lo interno

Piensa en un `Auto`. Tiene `color` y `modelo`, que interesan a quien interactúa con él, pero también `disco_de_embrague` y `palanca_de_cambios`, que son internos a su funcionamiento. Esos últimos están **encapsulados**: nadie los toca directamente, solo a través de métodos como `conducir`.

> [!tip] Regla
> Los atributos internos solo deben cambiar mediante los métodos que define la clase. Así la clase controla que sus datos siempre queden en un estado válido.

### Interfaz y abstracción

La **interfaz** de una clase es la fachada que protege su implementación: el conjunto de atributos y métodos que se ofrecen a los demás objetos. Cada tipo de interlocutor puede ver una interfaz distinta. Un `Conductor` ve `marca`, `modelo` y `año`, y puede `conducir`, `vender` o `pintar`, pero no modifica `kilometraje` directamente: solo lo hace al conducir. Un `Mecánico` vería otra interfaz (`nivel_de_aceite`, `abrir_capot`, `cambiar_aceite`).

El nivel de detalle que se muestra en una interfaz se llama **abstracción**.

![Clase Auto completa y la interfaz que ve el conductor](adjuntos/Interfaz%20de%20la%20clase%20Auto.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, la clase `Auto` con atributos `marca`, `modelo`, `año`, `color`, `kilometraje`, `ubicación`, `dueño` y métodos `conducir(kms)`, `vender(persona)`, `pintar(color)`, `leer_odómetro()`, `cambiar_neumático()`, `encontrar_auto()`.
> - A la derecha, «Interfaz <<Auto>>» con solo `marca`, `modelo`, `año` y los mismos métodos.
> - Texto: «Interfaz. Solo es posible acceder a estos atributos y métodos. Los demás están ocultos».

## Encapsulamiento en Python

En lenguajes como Java o C# se puede declarar un atributo **privado** y el lenguaje prohíbe usarlo desde afuera. En Python **todo es público**. Lo que existe es una **convención**: un nombre que empieza con guion bajo (`_`) significa «uso interno, no lo toques».

```python
class Televisor:
    def __init__(self, pulgadas, marca):
        self.pulgadas = pulgadas
        self.marca = marca
        self.encendido = False
        self.canal_actual = 0
        self._clave = "tv123"          # interno por convención

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def cambiar_canal(self, nuevo_canal):
        self._decodificar_imagen()
        self.canal_actual = nuevo_canal

    def _decodificar_imagen(self):     # método interno
        print("Estoy convirtiendo una señal eléctrica en la imagen que estás viendo.")

tv = Televisor(55, "Samsung")
tv.encender()
tv.cambiar_canal(5)
print(f"Televisor {tv.marca} en canal {tv.canal_actual}")
```

```
Estoy convirtiendo una señal eléctrica en la imagen que estás viendo.
Televisor Samsung en canal 5
```

Quien usa el televisor solo necesita `encender`, `apagar` y `cambiar_canal`. La decodificación ocurre sola al cambiar de canal, así que `_decodificar_imagen` no es parte de la interfaz.

> [!warning] Es solo una convención
> Python no lo impide: `tv._decodificar_imagen()` y `tv._clave` funcionan igual. El guion bajo es un aviso a otros programadores (y a tu yo futuro), no un candado.

## Doble guion bajo y *name mangling*

Si el nombre empieza con **dos** guiones bajos (`__clavesecreta`), Python lo hace más difícil de alcanzar:

```python
class Televisor:
    def __init__(self):
        self.__clavesecreta = "tv456"

    def __mostrar_canal_prohibido(self):
        print("Canal prohibido")

tv = Televisor()
# print(tv.__clavesecreta)              # AttributeError
# tv.__mostrar_canal_prohibido()        # AttributeError
tv._Televisor__mostrar_canal_prohibido()
print(tv._Televisor__clavesecreta)
```

```
Canal prohibido
tv456
```

No es un candado real, sino un truco llamado ***name mangling***: Python cambia internamente el nombre a `_NombreDeLaClase__atributo`, así que desde afuera con el nombre original «no existe», pero con el nombre completo se puede usar. No ocurre cuando el nombre **también termina** en doble guion bajo, por eso se puede llamar `tv.__str__()`. Su objetivo es reducir errores accidentales, no impedir el acceso.

> [!tip] Para controlar el acceso de verdad
> Más adelante se verán las *properties* (`@property`), que permiten leer y modificar un atributo a través de métodos.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que en Python no existen los atributos privados de verdad?
> Porque el lenguaje no impide acceder a ningún atributo. El guion bajo es solo una convención entre programadores, y el doble guion bajo solo cambia el nombre interno.

> [!question]- ¿Qué problema evita el encapsulamiento?
> Evita que otros objetos cambien datos internos y dejen al objeto en un estado inconsistente (por ejemplo, alterar el `kilometraje` sin conducir). Toda interacción pasa por métodos que controla el programador.

> [!question]- ¿Cómo se puede llamar un método `__secreto` de la clase `Caja` desde afuera?
> Con su nombre real transformado: `objeto._Caja__secreto()`. Esto muestra que *name mangling* no es una protección sino un cambio de nombre.
