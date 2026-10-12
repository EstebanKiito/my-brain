---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[11 - Vistas ERB|Vistas ERB]]", "[[07 - Validaciones en Active Record|Validaciones en Active Record]]"]
---
# Parciales en ERB

Un **parcial** es un fragmento de vista reutilizable (archivo que empieza con `_`). En el ejemplo de Persona, `new` y `edit` comparten el mismo formulario `_form.html.erb`.

## new.html.erb y edit.html.erb
Ambos formularios son similares, así que puedes usar un **parcial** para el formulario.

### _form.html.erb
```erb
<%= form_with(model: persona, local: true) do |form| %>
  <% if persona.errors.any? %>
    <div id="error_explanation">
      <h2><%= pluralize(persona.errors.count, "error") %> prohibited this persona from being saved:</h2>
      <ul>
        <% persona.errors.full_messages.each do |message| %>
          <li><%= message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :nombre %>
    <%= form.text_field :nombre %>
  </div>

  <div class="field">
    <%= form.label :edad %>
    <%= form.number_field :edad %>
  </div>

  <div class="actions">
    <%= form.submit %>
  </div>
<% end %>
```

### new.html.erb
```erb
<h1>Nueva Persona</h1>
<%= render 'form', persona: @persona %>
<%= link_to 'Volver', personas_path %>
```

### edit.html.erb
```erb
<h1>Editar Persona</h1>
<%= render 'form', persona: @persona %>
<%= link_to 'Volver', personas_path %>
```

> [!tip] Complemento
> - Los parciales empiezan con `_` (`_form.html.erb`), pero se invocan **sin** el guion bajo: `render 'form', persona: @persona`. El hash final le pasa la **variable local** `persona` al parcial.
> - El parcial usa `persona` (local) y no `@persona`, para no depender de la acción que lo llama.
> - `form_with(model: persona)` decide solo la URL y el método: si `persona` es nueva va a `POST /personas` (create); si ya existe, a `PATCH /personas/:id` (update).
> - `pluralize(persona.errors.count, "error")` da "1 error" o "2 errors".
> - Los campos se generan con form helpers: ver [[13 - Form helpers de Rails|Form helpers de Rails]].

## Preguntas de repaso

1. ¿Cómo se llama el archivo de un parcial y cómo se incluye?
> [!question]- Respuesta
> Empieza con `_` (por ejemplo `_form.html.erb`) y se incluye con `<%= render 'form', persona: @persona %>`.

2. ¿Por qué `new` y `edit` pueden compartir el mismo formulario?
> [!question]- Respuesta
> Porque `form_with(model: persona)` detecta si el objeto es nuevo o existente y genera la URL y el método correctos (POST para crear, PATCH para actualizar).

3. ¿Cómo muestra el formulario los errores de validación?
> [!question]- Respuesta
> Si `persona.errors.any?`, recorre `persona.errors.full_messages` y muestra cada mensaje en una lista.
