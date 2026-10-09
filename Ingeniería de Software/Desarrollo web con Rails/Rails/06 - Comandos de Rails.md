---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[01 - Instalar Ruby on Rails en Mac M1|Instalar Ruby on Rails en Mac M1]]"]
---
# Comandos de Rails

Resumen de los comandos de consola de Rails (y de PostgreSQL) que se usan en el curso.

## Mis apuntes
- `rails s` = `rails server` = `bin/rails server` → inicializa el servidor
- `rails generate model Pokemon name:string`
- `rails generate migration CreatePokemon` → atributos opcionales
- `db:migrate` → aplica las migraciones a la BDD
- `rails console`
- `sudo service postgresql start` → inicia postgres

> [!tip] Complemento — tabla de comandos
> | Comando | Qué hace |
> |---|---|
> | `rails new app` / `rails new app --api` | crea un proyecto (normal o solo API) |
> | `rails s` | levanta el servidor en http://localhost:3000 |
> | `rails c` / `rails console` | consola irb con la app cargada (para probar modelos) |
> | `rails g model Nombre attr:tipo` | modelo + migración + test + fixture |
> | `rails g controller Nombre` | controlador (y carpeta de vistas) |
> | `rails g scaffold Nombre attr:tipo` | modelo, migración, controlador CRUD completo, vistas y rutas |
> | `rails g migration NombreMigracion` | migración vacía (o con columnas) |
> | `rails db:migrate` / `rails db:rollback` | aplica / deshace migraciones |
> | `rails routes` | lista todas las rutas |
> | `rails test` | corre los tests |
>
> - `sudo service postgresql start` es para **Linux/WSL**. En Mac con Homebrew se usa `brew services start postgresql` (ver [[01 - Instalar Ruby on Rails en Mac M1|instalación]]).
> - `g` es abreviatura de `generate`, `s` de `server` y `c` de `console`.

## Preguntas de repaso

1. ¿Qué comando levanta el servidor y en qué puerto queda por defecto?
> [!question]- Respuesta
> `rails s` (o `rails server`), en http://localhost:3000.

2. ¿Para qué sirve `rails console`?
> [!question]- Respuesta
> Para abrir una consola interactiva con la aplicación cargada y probar modelos y consultas, por ejemplo `Student.all`.

3. ¿Qué genera `rails generate model Pokemon name:string`?
> [!question]- Respuesta
> El modelo `app/models/pokemon.rb`, la migración `create_pokemons`, el test del modelo y el fixture.
