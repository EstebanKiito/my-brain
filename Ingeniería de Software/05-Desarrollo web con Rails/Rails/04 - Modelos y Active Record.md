---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[03 - Patrón MVC en Rails|Patrón MVC en Rails]]"]
---
# Modelos y Active Record

Un **modelo** en Rails es una clase que hereda de `ApplicationRecord` y representa una tabla de la base de datos. **Active Record** es el ORM que traduce objetos Ruby a filas SQL y al revés.

## Mis apuntes
- **Models** → permiten interactuar con la **BASE DE DATOS**.
- El modelo `Persona` generado en `app/models/persona.rb`:

```ruby
class Persona < ApplicationRecord
  validates :nombre, presence: true
  validates :edad, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
end
```
*(Las validaciones se explican en [[07 - Validaciones en Active Record|Validaciones en Active Record]].)*

> [!tip] Complemento — Active Record como ORM (libro del curso, cap. 11, y slides "RoR - First API")
> - **ORM** (*Object-Relational Mapping*): enlaza los objetos de la aplicación con tablas de una base de datos relacional. No hace falta escribir SQL a mano.
> - "Active Record" es también el nombre de un **patrón arquitectónico** descrito por Martin Fowler (*Patterns of Enterprise Application Architecture*): cada objeto envuelve una fila y sabe guardarse, buscarse y borrarse.
> - Funciona con distintos gestores: PostgreSQL, MySQL o SQLite.
>
> **Convenciones:** clase `Student` (singular, `PascalCase`) ↔ tabla `students` (plural, `snake_case`). Los atributos no se declaran en la clase: salen de las columnas de la tabla.
>
> ```bash
> rails generate model Student name score
> # crea app/models/student.rb, la migración db/migrate/XXXX_create_students.rb,
> # test/models/student_test.rb y test/fixtures/students.yml
> ```
> ```ruby
> class Student < ApplicationRecord
> end
> ```
>
> **Operaciones básicas:**
> ```ruby
> student = Student.new(name: "Juan Pablo", score: 100)
> result = student.save            # INSERT; devuelve true/false
> student = Student.find(1)        # busca por id (si no existe, lanza error)
> all_students = Student.all       # todos
> Student.where("score = ?", 100)  # filtro (el ? evita inyección SQL)
> Student.find_by(name: "Ana")     # primero que cumpla, o nil
> student.update(score: 90)        # UPDATE
> student.destroy                  # DELETE
> ```
> Cada registro tiene además `id` (autoincremental, empieza en 1) y `created_at` / `updated_at` (por `t.timestamps`).

## Preguntas de repaso

1. ¿Qué es un ORM y qué ventaja da?
> [!question]- Respuesta
> Un mapeo objeto-relacional: permite trabajar con objetos Ruby (`Student.find(1)`) en vez de escribir SQL. Active Record traduce las operaciones a consultas SQL.

2. Si el modelo se llama `Persona`, ¿cómo se llama la tabla?
> [!question]- Respuesta
> `personas` (plural, en minúscula).

3. ¿Qué diferencia hay entre `find(id)` y `find_by(...)`?
> [!question]- Respuesta
> `find(id)` busca por id y lanza `ActiveRecord::RecordNotFound` si no existe. `find_by(...)` busca por cualquier condición y devuelve `nil` si no encuentra.

4. ¿Qué devuelve `student.save`?
> [!question]- Respuesta
> `true` si se guardó; `false` si no, por ejemplo porque falló una validación.
