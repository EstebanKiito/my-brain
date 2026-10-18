---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[09 - Controladores en Rails|Controladores en Rails]]", "[[02 - HTML|HTML]]"]
---
# Vistas ERB

Las vistas de Rails son archivos `.html.erb`: **HTML con código Ruby incrustado**. Se guardan en `app/views/<recurso>/` y usan las variables `@...` del controlador.

## Render implícito
Si una acción del controlador **no llama a `render`**, Rails **busca una vista con el mismo nombre de la acción** (por ejemplo, `index`) en `app/views/<recurso>/`, genera el HTML y lo envía como respuesta.

```ruby
# app/controllers/pokemons_controller.rb
class PokemonsController < ApplicationController
  def index
    @pokemons = Pokemon.all
  end
end
```

```erb
<%# app/views/pokemons/index.html.erb %>
<% @pokemons.each do |pokemon| %>
  <tr>
    <td><%= pokemon.name %></td>
    <td><%= pokemon.pokemon_type %></td>
  </tr>
<% end %>
```

El controlador se llama `PokemonsController`, en plural, para que Rails encuentre la carpeta `app/views/pokemons/`.

## Ejemplo completo: vistas de Persona
Las vistas del recurso `Persona`, que usan las variables que prepara [[09 - Controladores en Rails|su controlador]]:

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
> - **Importante:** el nombre del controlador y de la acción deben calzar exactamente con la carpeta y el archivo: `BooksController#index` → `app/views/books/index.html.erb`.
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
