---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[03 - Patrón MVC en Rails|Patrón MVC en Rails]]", "[[04 - Modelos y Active Record|Modelos y Active Record]]"]
---
# Controladores en Rails

Un controlador es una clase que **recibe los requests** (vía las rutas), usa los modelos y decide **qué responder**: renderizar una vista, redirigir o devolver JSON. Cada método público es una **acción**.

## Mis apuntes
- **Controllers** → clase que controla las interacciones con el usuario, la vista y el modelo.
- El controlador en `app/controllers/personas_controller.rb` define las **acciones CRUD**:

```ruby
class PersonasController < ApplicationController
  before_action :set_persona, only: %i[show edit update destroy]

  def index
    @personas = Persona.all
  end

  def show
  end

  def new
    @persona = Persona.new
  end

  def edit
  end

  def create
    @persona = Persona.new(persona_params)
    if @persona.save
      redirect_to @persona, notice: 'Persona fue creada exitosamente.'
    else
      render :new
    end
  end

  def update
    if @persona.update(persona_params)
      redirect_to @persona, notice: 'Persona fue actualizada exitosamente.'
    else
      render :edit
    end
  end

  def destroy
    @persona.destroy
    redirect_to personas_url, notice: 'Persona fue eliminada exitosamente.'
  end

  private

  def set_persona
    @persona = Persona.find(params[:id])
  end

  def persona_params
    params.require(:persona).permit(:nombre, :edad)
  end
end
```

> [!tip] Complemento — las piezas del controlador
> - **`before_action :set_persona, only: %i[show edit update destroy]`** ejecuta `set_persona` antes de esas 4 acciones, que necesitan cargar la persona por `params[:id]`. Así se evita repetir código. `%i[...]` es un arreglo de símbolos.
> - **Variables de instancia (`@personas`)**: son las que la vista puede usar.
> - **`params`**: hash con los datos del request (de la ruta `:id`, de la query string y del formulario).
> - **Strong parameters**, `params.require(:persona).permit(:nombre, :edad)`: solo deja pasar los atributos permitidos. Evita que alguien envíe campos extra (por ejemplo, `admin: true`) y los asigne (*mass assignment*).
> - `show` y `edit` están vacíos porque `before_action` ya cargó `@persona` y Rails renderiza su vista por defecto.
> - Si `save`/`update` falla, se hace `render :new`/`render :edit` para mostrar el formulario con los errores. Si funciona, se hace `redirect_to` (ver [[14 - render vs redirect_to|render vs redirect_to]]).
> - **Generar un controlador** (slides "RoR - First API"): `rails generate controller Hello` crea `app/controllers/hello_controller.rb`.

## Preguntas de repaso

1. ¿Qué hace `before_action :set_persona, only: %i[show edit update destroy]`?
> [!question]- Respuesta
> Ejecuta `set_persona` (que busca la persona por `params[:id]`) antes de esas cuatro acciones, para no repetir el `find` en cada una.

2. ¿Para qué sirve `persona_params` (strong parameters)?
> [!question]- Respuesta
> Filtra los parámetros del request: exige la clave `:persona` y solo permite `:nombre` y `:edad`, para evitar asignación masiva de atributos no permitidos.

3. ¿Por qué `create` hace `render :new` cuando `save` falla?
> [!question]- Respuesta
> Para volver a mostrar el formulario con los datos ingresados y los errores de validación, sin perder lo escrito ni hacer un nuevo request.
