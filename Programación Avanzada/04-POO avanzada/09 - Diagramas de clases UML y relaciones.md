---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/uml
  - origen/complemento
prerrequisitos:
  - "[[01 - Herencia y especialización de clases]]"
  - "[[07 - Encapsulamiento y atributos privados]]"
---

# Diagramas de clases UML y relaciones

Al planificar un proyecto de software antes de escribir código, o al comunicar la arquitectura de un sistema a otros desarrolladores, se requiere un estándar visual universal que describa con precisión las clases existentes y los vínculos entre ellas.

## Qué es un diagrama de clases UML

Un **diagrama de clases UML** (*Unified Modeling Language*) es un esquema gráfico estático que representa las clases del sistema, sus atributos internos, sus operaciones o métodos, y las relaciones que las conectan.

### Anatomía de una clase en UML

Cada clase se representa como un rectángulo dividido horizontalmente en tres compartimentos:

![Estructura de clase en diagrama UML](adjuntos/Estructura%20de%20clase%20en%20diagrama%20UML.png)

> [!example]- Transcripción de la imagen
> - Rectángulo dividido en tres secciones:
>   1. **Superior:** Nombre de la clase (en negrita o centrado).
>   2. **Intermedia:** Lista de atributos con su visibilidad y tipo.
>   3. **Inferior:** Lista de métodos u operaciones con sus parámetros y tipo de retorno.

![Ejemplo de clase Auto en UML](adjuntos/Ejemplo%20de%20clase%20Auto%20en%20UML.png)

> [!example]- Transcripción de la imagen
> - Clase `Auto` con atributos como `- kilometraje: int` y métodos como `+ conducir(kms: int): void`.

### Modificadores de visibilidad

UML utiliza símbolos prefijados para expresar el nivel de acceso de cada miembro:

| Símbolo | Visibilidad | Significado en Python |
|---|---|---|
| **`+`** | Público | Accesible libremente (`self.nombre`) |
| **`-`** | Privado | Oculto mediante *mangling* (`self.__password`) |
| **`#`** | Protegido | Convención de uso interno o herencia (`self._saldo`) |
| **`~`** | Paquete | Accesible dentro del mismo módulo |

## Relaciones fundamentales entre clases

### 1. Herencia o Generalización
Modela la relación **"es un"** (*is-a*). Se dibuja como una línea continua que termina en una **flecha con punta triangular hueca** que apunta desde la subclase hacia la superclase:

![Relación de herencia en UML](adjuntos/Relaci%C3%B3n%20de%20herencia%20en%20UML.png)

> [!example]- Transcripción de la imagen
> - Superclase `Enemigo` arriba con flechas triangulares huecas apuntando a ella desde las subclases `Goomba` y `Koopa`.

### 2. Composición y Agregación (Contención)
Modela la relación **"tiene un"** (*has-a*), donde una clase contiene a otra como atributo:

- **Agregación (débil):** la parte puede existir de manera independiente al todo (se dibuja con un rombo blanco/hueco en la clase contenedora).
- **Composición (fuerte):** la parte depende exclusivamente del ciclo de vida del todo; si se destruye el contenedor, se destruyen sus componentes (se dibuja con un **rombo negro relleno**):

![Relación de contención o composición en UML](adjuntos/Relaci%C3%B3n%20de%20contenci%C3%B3n%20o%20composici%C3%B3n%20en%20UML.png)

> [!example]- Transcripción de la imagen
> - Clase `Nivel` que contiene objetos de tipo `Mario` y listas de `Enemigo`, unida mediante una línea con rombo relleno que indica composición.

## Caso de estudio: modelando el mundo de Mario

Antes de construir las clases en UML, se realiza el análisis conceptual de las entidades y personajes del videojuego:

![Modelo conceptual de objetos en Mario](adjuntos/Modelo%20conceptual%20de%20objetos%20en%20Mario.png)

> [!example]- Transcripción de la imagen
> - Ilustración del videojuego Mario con personajes como Mario, Goombas y Koopas en un escenario.
> - Ilustra el paso de abstracción desde el dominio visual del juego hacia las clases y objetos del software.

## Modelo integrado

Al combinar herencia y composición se obtiene el plano estructural completo del programa:

![Diagrama de clases UML completo de Mario](adjuntos/Diagrama%20de%20clases%20UML%20completo%20de%20Mario.png)

> [!example]- Transcripción de la imagen
> - Diagrama UML completo con la clase central `Juego` o `Nivel` que compone instancias de `Jugador` y colecciones de `Enemigo`, donde `Goomba` y `Koopa` heredan de `Enemigo`.

> [!tip] Clases e interfaces abstractas en UML
> En los diagramas UML, los nombres de clases abstractas y de métodos abstractos se escriben en letra **_cursiva_** o se etiquetan con el estereotipo `<<abstract>>`.

## Preguntas de repaso

> [!question]- ¿Qué representan los tres compartimentos de una caja de clase en UML?
> El compartimento superior contiene el nombre de la clase; el intermedio contiene los atributos y sus tipos; y el inferior lista los métodos, sus parámetros y tipos de retorno.

> [!question]- ¿Cómo se representa visualmente la visibilidad privada en un diagrama UML?
> Mediante el símbolo de signo menos (`-`) antes del nombre del atributo o método (por ejemplo `- clave_acceso: str`).

> [!question]- ¿Cuál es la diferencia gráfica y semántica entre agregación y composición en UML?
> La agregación usa un rombo hueco y modela una relación débil donde las partes pueden subsistir sin el contenedor; la composición usa un rombo relleno y modela una relación fuerte donde las partes mueren si el contenedor es destruido.

> [!question]- ¿Hacia dónde apunta la flecha triangular hueca en una relación de herencia en UML?
> Apunta siempre desde la **subclase** derivada hacia la **superclase** base o madre de la cual hereda.
