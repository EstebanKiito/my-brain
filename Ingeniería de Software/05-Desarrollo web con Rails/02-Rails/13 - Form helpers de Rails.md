---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[11 - Vistas ERB|Vistas ERB]]", "[[04 - Formularios HTML|Formularios HTML]]"]
---
# Form helpers de Rails

Los *form helpers* son métodos de Rails (`form_with`, `form.text_field`…) que **generan el HTML de los formularios**, con los nombres de campos, la URL y la protección CSRF que Rails espera.

## Formularios Rails
![Rails form_with - código ERB](../adjuntos/Rails%20form_with%20-%20código%20ERB.png)

equivalente en HTML a:

![Rails form_with - HTML generado](../adjuntos/Rails%20form_with%20-%20HTML%20generado.png)

![Rails form_with - formulario renderizado](../adjuntos/Rails%20form_with%20-%20formulario%20renderizado.png)

> [!note]- Transcripción de las imágenes
> ```erb
> <%= form_with url: "/search", method: :get do |form| %>
>   <%= form.label :query, "Search for:" %>
>   <%= form.text_field :query %>
>   <%= form.submit "Search" %>
> <% end %>
> ```
> ```html
> <form action="/search" method="get" accept-charset="UTF-8" >
>   <label for="query">Search for:</label>
>   <input id="query" name="query" type="text" />
>   <input name="commit" type="submit"
>   value="Search" data-disable-with="Search" />
> </form>
> ```
> Resultado en el navegador: el texto "Search for:", un campo de texto y un botón "Search".

## Rails Form Helpers
```erb
<%= form.text_area :message, size: "70x5" %>
<%= form.hidden_field :parent_id, value: "foo" %>
<%= form.password_field :password %>
<%= form.number_field :price, in: 1.0..20.0, step: 0.5 %>
<%= form.range_field :discount, in: 1..100 %>
<%= form.date_field :born_on %>
<%= form.time_field :started_at %>
<%= form.datetime_local_field :graduation_day %>
<%= form.month_field :birthday_month %>
<%= form.week_field :birthday_week %>
<%= form.search_field :name %>
<%= form.email_field :address %>
<%= form.telephone_field :phone %>
<%= form.url_field :homepage %>
<%= form.color_field :favorite_color %>
```

> [!tip] Complemento (slides "Rails MVC")
> - **Checkbox:**
> ```erb
> <%= form.check_box :pet_dog %>
> <%= form.label :pet_dog, "I own a dog" %>
> ```
> genera `<input type="checkbox" id="pet_dog" name="pet_dog" value="1" />` y `<label for="pet_dog">I own a dog</label>`.
> - `form_with url: …` crea un formulario **libre** (por ejemplo, de búsqueda). `form_with model: @persona` crea uno **ligado a un modelo**: deduce la URL y el método (POST para nuevo, PATCH para existente) y nombra los campos `persona[nombre]`, que luego lee `params.require(:persona)`.
> - Cada helper corresponde a un `<input type="…">` de HTML (ver [[04 - Formularios HTML|Formularios HTML]]).
> - Documentación: https://guides.rubyonrails.org/form_helpers.html

## Preguntas de repaso

1. ¿Qué HTML genera `form.text_field :query`?
> [!question]- Respuesta
> `<input id="query" name="query" type="text" />`.

2. ¿Qué diferencia hay entre `form_with url:` y `form_with model:`?
> [!question]- Respuesta
> `url:` es un formulario libre hacia esa URL. `model:` se liga a un objeto: deduce la ruta y el método (crear o actualizar) y nombra los campos como `modelo[atributo]` para los strong parameters.

3. ¿Qué helper usarías para un campo de contraseña y cuál para una fecha?
> [!question]- Respuesta
> `form.password_field` y `form.date_field`.
