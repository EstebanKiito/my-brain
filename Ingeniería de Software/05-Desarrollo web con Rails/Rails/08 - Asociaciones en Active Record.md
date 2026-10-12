---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/complemento]
prerrequisitos: ["[[05 - Migraciones en Rails|Migraciones en Rails]]"]
---
# Asociaciones en Active Record

> [!tip] Complemento — nota nueva (fuente: slides "RoR - Active Record")
> **Qué es:** las asociaciones declaran **relaciones entre modelos** (1 a 1, 1 a N, N a N). Active Record crea los métodos para navegarlas, como `author.books`.
>
> **Ejemplo 1 a N:** un autor tiene varios libros; un libro pertenece a un autor.
> ```bash
> rails generate model Author name:string
> rails generate model Book published_at:datetime
> ```
> ```ruby
> class Author < ApplicationRecord
>   has_many :books
> end
>
> class Book < ApplicationRecord
>   belongs_to :author
> end
>
> class CreateBooks < ActiveRecord::Migration[7.0]
>   def change
>     create_table :books do |t|
>       t.belongs_to :author          # agrega la columna author_id
>       t.datetime :published_at
>       t.timestamps
>     end
>   end
> end
> ```
> En la base de datos solo hace falta que **cada libro tenga el id de su autor** (`author_id`).
>
> ```ruby
> juan = Author.new(name: 'Juan'); juan.save
> book1 = Book.new(published_at: Time.now, author: juan); book1.save
> book2 = Book.new(published_at: Time.now, author: juan); book2.save
> juan.books
> # SELECT "books".* FROM "books" WHERE "books"."author_id" = 1
> # => [#<Book id: 1, author_id: 1, ...>, #<Book id: 2, author_id: 1, ...>]
> ```
>
> **Otras asociaciones:**
> | Tipo | Declaración | Ejemplo |
> |---|---|---|
> | 1 a 1 | `has_one` / `belongs_to` | un proveedor tiene una cuenta |
> | 1 a N | `has_many` / `belongs_to` | un autor tiene muchos libros |
> | N a N | `has_many :through` (con un modelo intermedio) | médicos ↔ pacientes a través de citas |
>
> ```mermaid
> erDiagram
>   AUTHOR ||--o{ BOOK : "has_many / belongs_to"
> ```
> Documentación: https://guides.rubyonrails.org/v6.1/association_basics.html

## Preguntas de repaso

1. En una relación 1 a N entre Author y Book, ¿qué tabla guarda la clave foránea?
> [!question]- Respuesta
> `books`, con la columna `author_id` (el lado `belongs_to`).

2. ¿Qué método se obtiene al declarar `has_many :books` en Author?
> [!question]- Respuesta
> `author.books`, que devuelve todos los libros cuyo `author_id` es el del autor (además de métodos como `author.books.create(...)`).

3. ¿Cómo se modela una relación N a N en Rails?
> [!question]- Respuesta
> Con un modelo o tabla intermedia y `has_many :through`. Por ejemplo, Doctor `has_many :patients, through: :appointments`.
