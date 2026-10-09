---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[02 - Métodos de instancia y métodos de clase|Métodos de instancia y métodos de clase]]"]
---
# Visibilidad de métodos en Ruby

La visibilidad define **desde dónde se puede llamar** a un método: `public` (desde cualquier lado), `protected` y `private` (solo desde dentro de la clase).

## Visibilidad de métodos
- **Privados:** solo se acceden desde la misma clase.
- **Public:** - - -
- **Protected:** - - -

> [!warning] Apunte incompleto (registrado en `_meta/DUDAS.md`)
> "Public" y "Protected" quedaron sin descripción. Se completan abajo.

> [!tip] Complemento — los tres niveles (slides "Object Oriented Programming" y conocimiento general de Ruby)
> | Visibilidad | ¿Desde dónde se puede llamar? |
> |---|---|
> | `public` | Desde cualquier lugar. **Es la visibilidad por defecto de los métodos** en Ruby. |
> | `protected` | Desde dentro de la clase y sus subclases, también sobre **otra instancia** de la misma familia (por ejemplo, `otro.saldo` dentro de un método para comparar). |
> | `private` | Solo desde dentro del propio objeto, **sin receptor explícito**: `metodo`, no `otro.metodo`. Las subclases también pueden llamarlos. |
>
> ```ruby
> class Person
>   ...
>
>   private
>     def secret_method
>       puts "Este es el método secreto"
>     end
>
>     def another_secret_method
>       puts "Este es otro método secreto"
>     end
> end
>
> p1 = Person.new("Pedro")
> p1.secret_method # genera un error!
> ```
> Todo lo que va después de la palabra `private` es privado. Por eso la última línea lanza `NoMethodError`.

> [!example] Ejemplo extra — `protected` para comparar
> ```ruby
> class Cuenta
>   def initialize(saldo)
>     @saldo = saldo
>   end
>
>   def mas_rica_que?(otra)
>     saldo > otra.saldo     # válido: saldo es protected
>   end
>
>   protected
>
>   def saldo
>     @saldo
>   end
> end
>
> Cuenta.new(10).mas_rica_que?(Cuenta.new(5))  # => true
> Cuenta.new(10).saldo                          # NoMethodError (protected)
> ```

## Preguntas de repaso

1. ¿Cuál es la visibilidad por defecto de un método en Ruby?
> [!question]- Respuesta
> Pública.

2. ¿Qué pasa si se llama a un método privado desde fuera del objeto?
> [!question]- Respuesta
> Se lanza `NoMethodError`: los métodos privados solo se pueden llamar desde dentro del objeto.

3. ¿Qué diferencia hay entre `private` y `protected`?
> [!question]- Respuesta
> Ambos impiden llamarlos desde afuera. `protected` permite llamarlo sobre otra instancia de la misma clase o subclase (`otro.metodo`) desde dentro de un método; `private` no permite receptor explícito.
