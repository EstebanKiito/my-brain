---
ramo: Ingeniería de Software
tema: Patrones creacionales
tags: [ingsoft/patrones, patron/creacional, origen/apuntes]
prerrequisitos: ["[[01 - Qué es un patrón de diseño|Qué es un patrón de diseño]]", "[[02 - Métodos de instancia y métodos de clase|Métodos de instancia y métodos de clase]]"]
---
# Patrón Singleton

Singleton **asegura que una clase tenga una sola instancia** y da un **punto de acceso global** a ella. Para eso oculta el constructor y ofrece un método de clase que siempre devuelve la misma instancia.

## Singleton (YO)
- Nos permite **ASEGURAR que una clase solo tenga 1 instancia**.
- Proporciona un **punto de acceso global** a dicha instancia.
- Ej.: solo queremos **1 pelota en un partido de fútbol** → no permitir una segunda.

![Singleton - estructura](../adjuntos/Singleton%20-%20estructura.png)

> [!note]- Transcripción de la imagen
> `Singleton` (`-instance: Singleton` subrayado, es decir, estático; `-Singleton()` con constructor privado; `+getInstance(): Singleton` estático). El `Client` usa `getInstance()`, que hace: `if (instance == null) { instance = new Singleton() } return instance` (*nota: en aplicaciones multihilo hay que poner un bloqueo aquí*).

*"El constructor de la clase está oculto para prevenir la creación de más instancias."*

```ruby
class Singleton
  @instance = new

  private_class_method :new

  def self.instance
    @instance
  end
end

# Codigo del Cliente
singleton1 = Singleton.instance
singleton2 = Singleton.instance

if singleton1.equal?(singleton2)
  puts 'Singleton funciona, ambas variables contienen la misma instancia.'
else
  puts 'Singleton falló, las variables contienen diferentes instancias.'
end
```

> [!warning] Duda: ¿qué significa "(YO)" en el título?
> No queda claro en los apuntes (quizá "este lo hice yo"). Registrado en `_meta/DUDAS.md`.

> [!tip] Complemento — ejemplo de las slides (carpeta raíz)
> ```ruby
> class MainFolder
>   private_class_method :new
>   def initialize
>     @name = "root"
>   end
>   def self.instance
>     if @instance == nil
>       @instance = new
>     end
>     return @instance
>   end
> end
> folder = MainFolder.instance
> ```
> - `private_class_method :new` hace que **no se pueda llamar `MainFolder.new` desde fuera**. Dentro de la clase sí se puede, y por eso `self.instance` puede hacer `new`.
> - El método de clase `instance` es público y **controla que no se cree más de una instancia**: la crea la primera vez (*lazy*) y después devuelve siempre la misma.
> - En tus apuntes, la instancia se crea **al cargar la clase** (`@instance = new` antes de hacer privado `new`, *eager*). Las dos variantes son válidas.
> - `@instance` aquí es una variable de instancia **de la clase** (la clase también es un objeto), no de sus objetos.
> - Ruby trae el módulo `Singleton` (`require 'singleton'; include Singleton`), que hace lo mismo y además es seguro con hilos.
> - **Cuidado:** es un estado global y aumenta el acoplamiento (y dificulta los tests). Úsalo solo cuando de verdad debe haber una única instancia: configuración, logger, conexión compartida.

## Preguntas de repaso

1. ¿Cómo impide Singleton que se creen más instancias en Ruby?
> [!question]- Respuesta
> Haciendo privado el constructor con `private_class_method :new`. Así solo la propia clase puede crear la instancia, y la expone con un método de clase (`instance`).

2. ¿Qué diferencia hay entre la versión de tus apuntes y la de la slide?
> [!question]- Respuesta
> En tus apuntes, la instancia se crea al definir la clase (eager). En la slide, se crea la primera vez que se llama a `instance` (lazy). En ambas, `instance` devuelve siempre el mismo objeto.

3. ¿Qué verifica `singleton1.equal?(singleton2)`?
> [!question]- Respuesta
> Que las dos variables apuntan exactamente al mismo objeto (identidad), no solo a objetos iguales.

4. Da una desventaja del Singleton.
> [!question]- Respuesta
> Introduce estado global: aumenta el acoplamiento y complica los tests, porque todos comparten la misma instancia.
