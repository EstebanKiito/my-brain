---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/complemento]
prerrequisitos: ["[[04 - Modelos y Active Record|Modelos y Active Record]]"]
---
# Validaciones en Active Record

> [!tip] Complemento — nota nueva (fuente: slides "RoR - Active Record"; ejemplo `Persona` de mis apuntes)
> **Qué es:** las validaciones son reglas declaradas en el modelo que se revisan **antes de guardar** en la base de datos. Si alguna falla, `save` devuelve `false` y los errores quedan en `errors`.
>
> ```ruby
> class Student < ApplicationRecord
>   validates :name, presence: true      # un estudiante sí o sí debe tener nombre
> end
> ```
> ```
> > rails console
> irb> student = Student.new(score: 100)
> irb> student.save
> => false                               # no se guarda: falta name
> irb> student.errors
> => #<ActiveModel::Errors [#<ActiveModel::Error attribute=name, type=blank, options={}>]>
> irb> student.valid?
> => false
> ```
>
> **Más ejemplos (slides):**
> ```ruby
> class Person < ApplicationRecord
>   validates :name, length: { minimum: 2 }
>   validates :bio, length: { maximum: 500 }
>   validates :password, length: { in: 6..20 }
>   validates :registration_number, length: { is: 6 }
> end
>
> class Account < ApplicationRecord
>   validates :email, uniqueness: true
> end
> ```
>
> **Ejemplo de mis apuntes (modelo `Persona`):** `nombre` obligatorio y `edad` entera mayor o igual a 0.
> ```ruby
> validates :nombre, presence: true
> validates :edad, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
> ```
>
> - `obj.valid?` ejecuta las validaciones sin guardar.
> - `obj.errors.full_messages` da los mensajes legibles, por ejemplo `["Name can't be blank"]`. Se muestran en el formulario (ver [[11 - Vistas ERB|Vistas ERB]]).
> - Documentación: https://guides.rubyonrails.org/active_record_validations.html

## Preguntas de repaso

1. ¿Qué devuelve `save` si falla una validación y dónde quedan los errores?
> [!question]- Respuesta
> Devuelve `false`, y los errores quedan en `obj.errors` (por ejemplo, `obj.errors.full_messages`).

2. Escribe una validación para que `email` sea obligatorio y único.
> [!question]- Respuesta
> `validates :email, presence: true, uniqueness: true`.

3. ¿Para qué sirve `valid?`?
> [!question]- Respuesta
> Para ejecutar las validaciones y saber si el objeto está en un estado válido, sin intentar guardarlo.
