---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[09 - Controladores en Rails|Controladores en Rails]]", "[[02 - HTML|HTML]]"]
---
# Vistas ERB

Las vistas de Rails son archivos `.html.erb`: **HTML con código Ruby incrustado**. Se guardan en `app/views/<recurso>/` y usan las variables `@...` del controlador.

## Render implícito
Crea las vistas en `app/views/personas/`:
- Si en el controlador **no usamos el método "render"** para devolver un HTTPResponse,
- Rails **buscará un archivo `.erb` con el mismo nombre de la acción** (ej: `index`), generará el HTML y enviará el HTTPResponse.

`app/views/pokemons/index.html.erb`
```erb
# --- Controlador ---
class PokemonController < ApplicationController
	def index
		@pokemons = Pokemon.all
	end
end

# --- index.html.erb ---
<% @pokemons.each do |pokemon| %>
	<tr>
		<td><%= pokemon.name %></td>
		<td><%= pokemon.pokemon_tupe %></td>
	<tr>
<& end %>
```

> [!warning] Posible error (registrado en `_meta/DUDAS.md`)
> - `pokemon_tupe` → `pokemon_type`.
> - El segundo `<tr>` debe ser `</tr>`.
> - `<& end %>` → `<% end %>`.
> - El controlador debería llamarse `PokemonsController` (plural) para que Rails encuentre `app/views/pokemons/index.html.erb`.

## Ejemplo completo: vistas de Persona
Volviendo al ejemplo de la clase Persona:

### index.html.erb
```erb
<h1>Personas</h1>

<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Edad</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @personas.each do |persona| %>
      <tr>
        <td><%= persona.nombre %></td>
        <td><%= persona.edad %></td>
        <td><%= link_to 'Mostrar', persona %></td>
        <td><%= link_to 'Editar', edit_persona_path(persona) %></td>
        <td><%= link_to 'Eliminar', persona, method: :delete, data: { confirm: '¿Estás seguro?' } %></td>
      </tr>
    <% end %>
  </tbody>
</table>

<%= link_to 'Nueva Persona', new_persona_path %>
```

### show.html.erb
```erb
<h1><%= @persona.nombre %></h1>
<p>
  <strong>Edad:</strong>
  <%= @persona.edad %>
</p>
<%= link_to 'Editar', edit_persona_path(@persona) %> |
<%= link_to 'Volver', personas_path %>
```

Los formularios `new` y `edit` usan un parcial: ver [[12 - Parciales en ERB|Parciales en ERB]].

> [!tip] Complemento — sintaxis ERB (slides "Rails MVC")
> | Etiqueta | Qué hace |
> |---|---|
> | `<%= … %>` | ejecuta Ruby e **inserta el resultado** en el HTML |
> | `<% … %>` | ejecuta Ruby **sin imprimir** (if, each, end) |
>
> - Todo lo que está fuera de las etiquetas es HTML. Por ejemplo, `<h1> Hello <%= name %>! </h1>` con `name = "Juan Pablo"` genera `<h1> Hello Juan Pablo! </h1>`.
> - ERB solo genera la rama del `if` que corresponde.
> - **Ojo:** el nombre del controlador y de la acción deben calzar exactamente con la carpeta y el archivo: `BooksController#index` → `app/views/books/index.html.erb`.
> - Más: https://guides.rubyonrails.org/layouts_and_rendering.html

## Preguntas de repaso

1. ¿Qué diferencia hay entre `<%= %>` y `<% %>`?
> [!question]- Respuesta
> `<%= %>` ejecuta e imprime el resultado en el HTML; `<% %>` ejecuta sin imprimir (para if, each, end).

2. Si la acción `index` de `PersonasController` no llama a `render`, ¿qué archivo se muestra?
> [!question]- Respuesta
> `app/views/personas/index.html.erb`.

3. ¿Qué genera `<td><%= link_to 'Editar', edit_persona_path(persona) %></td>`?
> [!question]- Respuesta
> Una celda con un enlace `<a href="/personas/ID/edit">Editar</a>`, donde ID es el id de esa persona.
