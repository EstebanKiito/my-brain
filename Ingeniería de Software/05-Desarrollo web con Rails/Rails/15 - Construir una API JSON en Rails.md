---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/complemento]
prerrequisitos: ["[[09 - Controladores en Rails|Controladores en Rails]]", "[[10 - Rutas en Rails|Rutas en Rails]]"]
---
# Construir una API JSON en Rails

> [!tip] Complemento — nota nueva (fuente: slides "RoR - First API" y "RoR - Active Record", libro cap. 12; la tarea del curso era "API simple en Ruby on Rails")
> **Qué es:** una API responde **datos en JSON** en vez de páginas HTML. Se prueba con **Postman** enviando requests HTTP.
>
> **1. Hello World API**
> ```bash
> rails new hello --api
> cd hello
> rails generate controller Hello
> ```
> ```ruby
> # app/controllers/hello_controller.rb
> class HelloController < ApplicationController
>   def sayHi
>     render json: 'Hello World!!'
>   end
> end
>
> # config/routes.rb
> Rails.application.routes.draw do
>   get 'hi', to: 'hello#sayHi'          # http://localhost:3000/hi
> end
> ```
>
> **2. API de estudiantes (CRUD)**
> ```ruby
> class StudentController < ApplicationController
>   def index                                  # GET /index
>     @all_students = Student.all
>     render json: @all_students
>   end
>
>   def show                                   # GET /student/:id
>     @student = Student.find(params[:id])
>     render json: @student
>   end
>
>   def create                                 # POST /student
>     @student = Student.new(student_params)
>     if @student.save
>       render json: @student
>     else
>       render json: @student.errors, status: :unprocessable_entity
>     end
>   end
>
>   def update                                 # PATCH /student/:id
>     @student = Student.find(params[:id])
>     if @student.update(student_params)
>       render json: @student
>     else
>       render json: @student.errors, status: :unprocessable_entity
>     end
>   end
>
>   def destroy                                # DELETE /student/:id
>     @student = Student.find(params[:id])
>     @student.destroy
>   end
>
>   def filter                                 # GET /filter/:score
>     @students = Student.where("score = ?", params[:score])
>     render json: @students
>   end
>
>   private
>
>   def student_params
>     params.require(:student).permit(:name, :score)
>   end
> end
> ```
> Las rutas correspondientes están en [[10 - Rutas en Rails|Rutas en Rails]] (ejemplo de rutas a mano).
>
> **Body JSON para crear (en Postman):**
> ```json
> { "student": { "name": "Juan Pablo", "score": 100 } }
> ```
> - `status: :unprocessable_entity` es el código **422**: la validación falló.
> - Más: https://guides.rubyonrails.org/active_record_basics.html

## Preguntas de repaso

1. ¿Qué cambia entre una acción que devuelve HTML y una de API?
> [!question]- Respuesta
> En la API se responde con `render json: objeto` en vez de renderizar una vista ERB o hacer `redirect_to`.

2. ¿Qué código de estado se devuelve cuando falla la validación al crear y cómo se indica en Rails?
> [!question]- Respuesta
> 422 Unprocessable Entity, con `render json: @student.errors, status: :unprocessable_entity`.

3. Escribe la ruta y la acción para filtrar estudiantes por puntaje.
> [!question]- Respuesta
> Ruta: `get 'filter/:score', to: 'student#filter'`. Acción: `@students = Student.where("score = ?", params[:score]); render json: @students`.
