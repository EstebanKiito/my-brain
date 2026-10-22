# POO avanzada — índice

Técnicas avanzadas del paradigma orientado a objetos en Python: relaciones de herencia y especialización, sobrescritura y delegación con `super()`, polimorfismo y tipado dinámico (*duck typing*), sobrecarga de operadores y métodos dunder, multiherencia y el problema del diamante, contratos de interfaz con clases abstractas (`abc`), decoradores y propiedades (`@property`), diagramas de clases UML, el algoritmo de linearización MRO y metaclases con `type`.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los seis notebooks principales y dos notebooks bonus de la cuarta semana del curso (herencia, polimorfismo, multiherencia, clases abstractas, decoradores, diagramas de clases, metaclases y multiherencia en Python), complementado con las diapositivas de repaso de POO.

## Orden de estudio
1. [[01 - Herencia y especialización de clases|Herencia y especialización de clases]]: relación "es un", superclases y subclases, y extensión de tipos built-in.
2. [[02 - Sobrescritura de métodos y la función super|Sobrescritura de métodos y la función super]]: method overriding, delegación desacoplada con `super()` y extensión de constructores.
3. [[03 - Polimorfismo y duck typing|Polimorfismo y duck typing]]: interfaces uniformes, ausencia de sobrecarga por firma en Python y la filosofía de tipado duck typing.
4. [[04 - Sobrecarga de operadores y métodos dunder|Sobrecarga de operadores y métodos dunder]]: métodos mágicos aritméticos y relacionales, y diferencias clave entre `__str__` y `__repr__`.
5. [[05 - Multiherencia y el problema del diamante|Multiherencia y el problema del diamante]]: clases base múltiples, colisiones por orden de declaración y el riesgo de inicialización duplicada en rombo.
6. [[06 - Clases abstractas y el módulo abc|Clases abstractas y el módulo abc]]: contratos de interfaz obligatorios con `ABC` y `@abstractmethod` y validación en tiempo de instanciación.
7. [[07 - Decoradores: funciones de primera clase y sintaxis arroba|Decoradores: funciones de primera clase]]: funciones como objetos de primera clase, funciones de envoltura (*wrappers*) y sintaxis `@`.
8. [[08 - Properties y métodos estáticos: classmethod y staticmethod|Properties y métodos estáticos]]: encapsulamiento limpio con `@property`, setters de validación, y métodos `@classmethod` frente a `@staticmethod`.
9. [[09 - Diagramas de clases UML y relaciones|Diagramas de clases UML y relaciones]]: compartimentos de clase, visibilidad (`+`, `-`, `#`), relaciones de asociación, composición y generalización.
10. [[10 - MRO y multiherencia cooperativa en Python|MRO y multiherencia cooperativa en Python]]: algoritmo C3 Linearization, orden de resolución de métodos, `super()` cooperativo y propagación de argumentos con `*args` y `**kwargs`.
11. [[11 - Metaclases: la clase de una clase y el comando type|Metaclases: la clase de una clase y el comando type]]: creación dinámica de clases con `type(name, bases, dict)`, intercepción en `__new__` y patrón Singleton.
