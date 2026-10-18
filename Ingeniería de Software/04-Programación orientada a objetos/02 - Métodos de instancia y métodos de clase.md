---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Clases y objetos en Ruby|Clases y objetos en Ruby]]"]
---
# Métodos de instancia y métodos de clase

Los métodos definen el **comportamiento** de una clase. Los **de instancia** se llaman sobre un objeto; los **de clase** (`def self.nombre`) se llaman sobre la clase misma, sin crear una instancia.

## Métodos de instancia
Los métodos permiten **definir el comportamiento** de una clase. Un método de instancia se llama sobre un objeto:

```ruby
class Person
  def greet
    "Hola"
  end
end

p1 = Person.new
puts p1.greet          # imprime Hola

# Sin guardar el objeto en una variable:
puts Person.new.greet  # también imprime Hola
```

## Métodos de clase
Un método definido con `self.` pertenece a la **clase**, así que se llama **sin crear una instancia**. Un método de instancia, en cambio, no se puede llamar sobre la clase:

```ruby
class Developer
  def self.backend
    "I am a backend developer"
  end

  def frontend
    "I am a frontend developer"
  end
end

puts Developer.backend   # imprime "I am a backend developer"
puts Developer.frontend  # NoMethodError: frontend es de instancia (no tiene self.)
puts Developer.new.frontend  # así sí funciona
```

> [!tip] Complemento (slides "Object Oriented Programming")
> - `greet` es un **método de instancia**: se ejecuta sobre una instancia de la clase.
> - `backend` es un **método de clase**: se ejecuta sobre la clase misma y no hace falta crear una instancia.
> - `Developer.frontend` da `NoMethodError` porque `frontend` es de instancia: hay que llamarlo como `Developer.new.frontend`.
>
> **¿Para qué sirven los métodos de clase?** Por ejemplo, para "facilitar" la creación de objetos (métodos *fábrica*):
> ```ruby
> class Person
>   def initialize(name, gender)
>     ...
>   end
>
>   def self.create_female(name)
>     Person.new(name, :female)
>   end
>
>   def self.create_male(name)
>     Person.new(name, :male)
>   end
> end
>
> pedro = Person.create_male("Pedro")
> maria = Person.create_female("Maria")
> ```
> Otros usos típicos: contadores compartidos (ver [[06 - Variables de clase en Ruby|Variables de clase]]) y consultas en Rails como `Student.all` o `Student.find(1)`.

## Preguntas de repaso

1. ¿Cómo se define un método de clase en Ruby?
> [!question]- Respuesta
> Anteponiendo `self.` al nombre: `def self.backend ... end`. Se llama como `Developer.backend`.

2. ¿Por qué `Developer.frontend` da error?
> [!question]- Respuesta
> Porque `frontend` es un método de instancia: existe en los objetos `Developer`, no en la clase. Hay que hacer `Developer.new.frontend`.

3. Da un ejemplo de uso de un método de clase.
> [!question]- Respuesta
> Un método fábrica como `Person.create_male("Pedro")`, que construye objetos con ciertos valores, o en Rails `Student.all`.
