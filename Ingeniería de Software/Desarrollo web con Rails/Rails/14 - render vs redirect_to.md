---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[09 - Controladores en Rails|Controladores en Rails]]", "[[11 - Vistas ERB|Vistas ERB]]"]
---
# render vs redirect_to

`render` genera **una vista en el mismo request**, con las variables que ya existen. `redirect_to` le dice al navegador que **haga un nuevo request** a otra URL.

## Render
```ruby
def update
	if @pokemon.update(pokemon_params)
		redirect_to @pokemon, notice: 'Pokemon was succesfully update'
	else
		render :edit
	end
end
```
- **Renderizar a otra vista** (diferente del nombre del método) → `render :vista`.
- **`redirect_to`:** no solo renderiza la vista "show", ya que para renderizarla necesitará probablemente la variable `@pokemon`.
- **`redirect_to`:** hace **REFRESH del browser** en la página "show" usando `@pokemon`, por lo que **se envía otro HTTPRequest**.

Otras formas de usar render:
- `render: edit`
- `render action: edit`
- `render "edit"`
- `render "books/edit"`
- `render template: "books/edit"`

**Todas son equivalentes.**

Más información:
- https://guides.rubyonrails.org/routing.html
- https://guides.rubyonrails.org/layouts_and_rendering.html

> [!tip] Complemento (slides "Rails MVC")
> ```ruby
> def show
>   @book = Book.find_by(id: params[:id])
>   if @book.nil?
>     redirect_to action: :index
>   end
> end
> ```
> `redirect_to` no solo renderiza "index.html.erb", que probablemente necesite `@books` (no definido en `show`): hace que el navegador pida de nuevo `index`, y esa acción carga sus propios datos.
>
> | | `render` | `redirect_to` |
> |---|---|---|
> | Requests | el mismo | uno nuevo (código 302) |
> | Variables `@` | se conservan | se pierden (la nueva acción carga las suyas) |
> | URL del navegador | no cambia | cambia |
> | Uso típico | mostrar el formulario con errores tras un `save` fallido | después de crear, actualizar o borrar con éxito |
>
> - En la lista de los apuntes, `render: edit` se escribe en realidad `render :edit` (con el símbolo `:edit`); las formas exactas de las slides son `render :edit`, `render action: :edit`, `render "edit"`, `render action: "edit"`, `render "books/edit"` y `render template: "books/edit"`.
> - El patrón **"redirect after POST"** evita que, al recargar la página, el navegador reenvíe el formulario.
> - Detalle: el `notice` dice "succesfully update"; lo correcto es "successfully updated".

## Preguntas de repaso

1. ¿Qué diferencia hay entre `render :edit` y `redirect_to @pokemon`?
> [!question]- Respuesta
> `render :edit` genera la vista `edit` en el mismo request, usando las variables actuales (por ejemplo, con los errores). `redirect_to @pokemon` responde con una redirección: el navegador hace un nuevo request GET a la página `show` del pokémon.

2. ¿Por qué después de un `update` exitoso se usa `redirect_to` y no `render :show`?
> [!question]- Respuesta
> Porque así el navegador queda en la URL de `show` con un request nuevo: recargar la página no reenvía el formulario, y la acción `show` carga sus propios datos.

3. Nombra tres formas equivalentes de renderizar la vista `edit`.
> [!question]- Respuesta
> `render :edit`, `render action: :edit` y `render "edit"` (también `render "books/edit"` o `render template: "books/edit"` si es de otro controlador).
