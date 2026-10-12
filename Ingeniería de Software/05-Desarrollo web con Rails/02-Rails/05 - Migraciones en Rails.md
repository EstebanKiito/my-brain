---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[04 - Modelos y Active Record|Modelos y Active Record]]"]
---
# Migraciones en Rails

Una migración es un **script de Ruby que modifica el esquema de la base de datos** (crear tablas, agregar columnas…) de forma versionada, para que la base de datos evolucione junto con el código.

## Mis apuntes
- **`db:migrate`** → se guardan migraciones: modificar la BDD **consistentemente e iterativamente**.
- `rails generate model Pokemon name:string`
- `create_pokemons.rb`
- `rails generate migration CreatePokemon` → atributos opcionales (tiene que ser en singular)

```ruby
create_table: pokemons do |t|
	t.string :name
	t.string :pokemon_type
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> - **Sintaxis:** es `create_table :pokemons do |t|` (el símbolo va después de un espacio, no con `:` pegado al método), y faltan los `end`. Versión completa:
> ```ruby
> class CreatePokemons < ActiveRecord::Migration[7.0]
>   def change
>     create_table :pokemons do |t|
>       t.string :name
>       t.string :pokemon_type
>       t.timestamps
>     end
>   end
> end
> ```
> - **"(tiene que ser en singular)":** lo que va en **singular es el nombre del modelo** (`rails generate model Pokemon`), y Rails crea la tabla en **plural** (`pokemons`). Una migración suelta suele nombrarse como acción: `rails generate migration CreatePokemons` o `AddTypeToPokemons`.

> [!tip] Complemento (slides "RoR - First API" y "RoR - Active Record", libro cap. 11)
> - `rails generate model Student name score` crea el modelo **y** su migración. Se puede indicar el tipo: `name:text score:integer`; si no se indica, es `string`.
> - El archivo se llama con un timestamp: `db/migrate/20230312193956_create_students.rb`.
> - `rails db:migrate` ejecuta las migraciones pendientes:
> ```
> == 20230312193956 CreateStudents: migrating ===========
> -- create_table(:students)
>    -> 0.0007s
> == 20230312193956 CreateStudents: migrated (0.0007s) ==
> ```
> - El estado completo del esquema queda en **`db/schema.rb`** (el libro dice `db/migrate/schema.rb`, pero el archivo está en `db/`).
> - La tabla tiene `id` (agregado por defecto y autoincremental), las columnas de los atributos y `created_at`/`updated_at` (por `t.timestamps`).
> - Otros comandos útiles: `rails db:rollback` (deshace la última migración), `rails db:create`, `rails db:seed`.
> - Documentación: https://guides.rubyonrails.org/active_record_migrations.html

## Preguntas de repaso

1. ¿Qué es una migración y por qué se usan?
> [!question]- Respuesta
> Un script versionado que cambia el esquema de la base de datos. Permite modificar la BDD de forma consistente e iterativa, que todo el equipo tenga el mismo esquema y poder deshacer cambios.

2. ¿Qué comando ejecuta las migraciones pendientes?
> [!question]- Respuesta
> `rails db:migrate`.

3. Si genero `rails generate model Pokemon name:string`, ¿cómo se llama la tabla y qué columnas tiene?
> [!question]- Respuesta
> `pokemons`, con las columnas `id`, `name` (string), `created_at` y `updated_at`.

4. ¿Dónde se ve el esquema completo y actual de la base de datos?
> [!question]- Respuesta
> En `db/schema.rb`.
