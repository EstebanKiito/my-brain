---
ramo: Ingeniería de Software
tema: UML
tags: [ingsoft/uml, origen/apuntes]
prerrequisitos: ["[[01 - Diagrama de clases UML|Diagrama de clases UML]]"]
---
# Visibilidad en UML

En UML, cada atributo y operación lleva un símbolo que indica **desde dónde se puede acceder**: `+` público, `-` privado, `#` protegido (y `~` de paquete).

![Diagrama de clases - visibilidad](../adjuntos/Diagrama%20de%20clases%20-%20visibilidad.png)

> [!note]- Transcripción de la imagen
> En `MyClassName`: `+attribute : int` es un **atributo público**, `-attribute2 : float` es un **atributo privado** y `#attribute3 : Circle` es un **atributo protegido**.

- **Público (`+`):** puede ser accedido desde **cualquier clase** del sistema.
- **Protegido (`#`):** solo puede ser accedido desde la **misma clase y clases hijas**.
- **Privado (`-`):** solo puede ser accedido desde la **misma clase**.

> [!tip] Complemento (libro del curso, cap. 8.9)
> | Símbolo | Visibilidad | Accesible desde |
> |---|---|---|
> | `+` | pública | todas las clases |
> | `-` | privada | solo la misma clase |
> | `#` | protegida | la misma clase y sus subclases |
> | `~` | de paquete | clases del mismo paquete |
>
> - Lo habitual: **atributos privados** (encapsulamiento) y **métodos públicos**, salvo los auxiliares.
> - En Ruby los atributos (`@x`) son siempre privados; un `+nombre` en el diagrama de una clase Ruby suele significar que hay un accesor (`attr_reader`/`attr_accessor`). Ver [[05 - Atributos y accesores en Ruby|Atributos y accesores en Ruby]] y [[03 - Visibilidad de métodos en Ruby|Visibilidad de métodos en Ruby]].

## Preguntas de repaso

1. ¿Qué significan `+`, `-` y `#` delante de un atributo?
> [!question]- Respuesta
> `+` público (accesible desde cualquier clase), `-` privado (solo la misma clase) y `#` protegido (la misma clase y sus hijas).

2. ¿Qué visibilidad suelen tener los atributos y por qué?
> [!question]- Respuesta
> Privada, por encapsulamiento: así otras clases no dependen de los datos internos y se reduce el acoplamiento.

3. ¿Qué indica `~`?
> [!question]- Respuesta
> Visibilidad de paquete: accesible por las clases del mismo paquete.
