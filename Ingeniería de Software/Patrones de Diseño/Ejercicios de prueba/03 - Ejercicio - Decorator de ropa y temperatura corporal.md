---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, ingsoft/ejercicio, patron/estructural, origen/apuntes]
prerrequisitos: ["[[01 - Patrón Decorator|Patrón Decorator]]"]
---
# Ejercicio: Decorator de ropa y temperatura corporal

Problema de prueba (Pregunta 5): modelar con el patrón Decorator a una persona que se pone abrigos uno encima de otro y calcular su temperatura corporal.

## Ejercicio prueba
![Ejercicio Decorator - enunciado abrigos](../adjuntos/Ejercicio%20Decorator%20-%20enunciado%20abrigos.png)

> [!note]- Transcripción del enunciado
> *Pregunta 5.* En este ejercicio usted debe implementar el patrón Decorator para modelar una persona que puede tener diferentes tipos de abrigos que se pueden poner uno encima de otro. En la primera imagen se ve una persona sin ningún abrigo; en la segunda, una persona con un suéter; y en la última, una persona con un suéter y una parca. El modelo de clases debe permitir instanciar personas con diferentes combinaciones de abrigos.
> - **(5 pts)** Implemente el patrón Decorator que permita modelar personas con diferentes tipos de abrigos. Debe escribir el código de cada clase.
> - **(5 pts)** Agregue una operación llamada `temperatura_corporal`, que devuelva la temperatura esperada del cuerpo de la persona que tiene N abrigos:
>   - una persona tiene una temperatura corporal de 37 grados;
>   - un suéter aumenta la temperatura de la persona en 2 grados;
>   - una parca la aumenta en 5 grados;
>   - por ejemplo, una persona con dos suéteres y una parca debe tener 47 grados (37 + 2 + 2 + 5).

## Solución (mis apuntes)
```ruby
class PersonInterface
	def temperatura_corporal
		raise NotImplementedError
	end
end

class Person < PersonInterface
	def temperatura_corporal
		37
	end
end

# Aqui Estamos entregando el Objeto Decorado al Decorador
class PersonDecorator < PersonInterface
	def initialize(person)
		@person = person
	end

	def temperatura_corporal
		@person.temperatura_corporal
	end
end

class Sweater < PersonDecorator
	def temperatura_corporal
		super + 2
	end
end

class Coat < PersonDecorator
	def temperatura_corporal
		super + 5
	end
end
```

> [!tip] Complemento — cómo se usa y por qué funciona
> ```ruby
> persona = Coat.new(Sweater.new(Sweater.new(Person.new)))
> persona.temperatura_corporal   # => 47  (37 + 2 + 2 + 5)
> ```
> - `PersonInterface` es la **interfaz común** (abstracta).
> - `Person` es el **componente concreto** (37).
> - `PersonDecorator` es el **decorador base**: guarda la persona envuelta y delega.
> - `Sweater` y `Coat` son **decoradores concretos**: `super` llama al `temperatura_corporal` del decorador base, que delega en la persona envuelta, y luego suman lo suyo.
> - La llamada recorre la "cebolla" de afuera hacia adentro y suma al volver: Coat → Sweater → Sweater → Person (37) → +2 → +2 → +5.
>
> ```mermaid
> classDiagram
>   class PersonInterface { <<abstract>> +temperatura_corporal() }
>   PersonInterface <|-- Person
>   PersonInterface <|-- PersonDecorator
>   PersonDecorator o--> PersonInterface : person
>   PersonDecorator <|-- Sweater
>   PersonDecorator <|-- Coat
> ```

## Preguntas de repaso

1. ¿Qué devuelve `Sweater.new(Person.new).temperatura_corporal`?
> [!question]- Respuesta
> 39 (37 + 2).

2. ¿Qué hace `super` dentro de `Sweater#temperatura_corporal`?
> [!question]- Respuesta
> Llama a `PersonDecorator#temperatura_corporal`, que devuelve la temperatura de la persona envuelta (`@person.temperatura_corporal`); después se le suma 2.

3. ¿Cómo agregarías una bufanda que sube 1 grado?
> [!question]- Respuesta
> `class Bufanda < PersonDecorator; def temperatura_corporal; super + 1; end; end`. No se modifica ninguna clase existente.
