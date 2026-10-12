---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[09 - Controladores en Rails|Controladores en Rails]]", "[[01 - Protocolo HTTP|Protocolo HTTP]]"]
---
# Rutas en Rails

Las rutas, en `config/routes.rb`, **conectan una URL y un método HTTP con una acción de un controlador**. `resources` genera de una vez las 7 rutas CRUD.

## Rutas (Pt. 1)
- **Routes** → rutas para ser usadas por el usuario; se conectan con el controlador.

```ruby
post “/pokemon”, to: “pokemons#create”)

“/pokemons” → endpoint // pokemons → controlador // create → metodo
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> Sobra el `)` final, las comillas deben ser rectas (`"`) y el endpoint aparece como `/pokemon` en el código y `/pokemons` en la explicación. Versión correcta:
> ```ruby
> post "/pokemons", to: "pokemons#create"
> # "/pokemons" → endpoint · pokemons → controlador · create → método (acción)
> ```

## Routing
```ruby
Rails.application.routes.draw do
	resources :photos
end
```
- **Resources:** genera las rutas de las fotos de manera automática.
- Siguen el estándar de la web y de Ruby.

![Rails resources - rutas generadas](../adjuntos/Rails%20resources%20-%20rutas%20generadas.png)

> [!note]- Transcripción de la imagen
> | HTTP Verb | Path | Controller#Action | Used for |
> |---|---|---|---|
> | GET | /photos | photos#index | display a list of all photos |
> | GET | /photos/new | photos#new | return an HTML form for creating a new photo |
> | POST | /photos | photos#create | create a new photo |
> | GET | /photos/:id | photos#show | display a specific photo |
> | GET | /photos/:id/edit | photos#edit | return an HTML form for editing a photo |
> | PATCH/PUT | /photos/:id | photos#update | update a specific photo |
> | DELETE | /photos/:id | photos#destroy | delete a specific photo |

Más información: https://guides.rubyonrails.org/routing.html

> [!tip] Complemento — path helpers (slides "Rails MVC")
> `resources :photos` también crea métodos que generan las URLs:
> | Helper | Genera |
> |---|---|
> | `photos_path` | `"/photos"` |
> | `new_photo_path` | `"/photos/new"` |
> | `edit_photo_path(:id)` | `"/photos/:id/edit"` |
> | `photo_path(id)` | `"/photos/:id"` |
>
> Las versiones `_url` (por ejemplo `photos_url`) generan la URL completa con dominio. Se usan en vistas (`link_to`), en `redirect_to` y en tests.

> [!example] Ejemplo extra — rutas a mano (slides "RoR - First API" y "Active Record")
> ```ruby
> Rails.application.routes.draw do
>   get 'hi', to: 'hello#sayHi'
>   get 'index', to: 'student#index'
>   get '/student/:id', to: 'student#show'       # :id llega en params[:id]
>   post '/student', to: 'student#create'
>   patch 'student/:id', to: 'student#update'
>   delete 'student/:id', to: 'student#destroy'
>   get 'filter/:score', to: 'student#filter'
> end
> ```
> `rails routes` lista todas las rutas de la app.

## Preguntas de repaso

1. ¿Qué significa `post "/pokemons", to: "pokemons#create"`?
> [!question]- Respuesta
> Que un request POST a `/pokemons` lo atiende la acción `create` del controlador `PokemonsController`.

2. ¿Cuántas rutas genera `resources :photos` y cuáles usan el mismo path `/photos/:id`?
> [!question]- Respuesta
> 7 rutas. `/photos/:id` lo usan `show` (GET), `update` (PATCH/PUT) y `destroy` (DELETE): las distingue el método HTTP.

3. ¿Qué devuelve `edit_photo_path(3)`?
> [!question]- Respuesta
> El string `"/photos/3/edit"`.
