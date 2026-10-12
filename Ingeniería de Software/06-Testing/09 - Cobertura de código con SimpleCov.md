---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[04 - Unit tests en Rails|Unit tests en Rails]]", "[[07 - Integration tests en Rails|Integration tests en Rails]]"]
---
# Cobertura de código con SimpleCov

La **cobertura** mide qué porcentaje del código ejecutan los tests. **SimpleCov** es la gema que la calcula en Ruby/Rails y muestra qué líneas quedaron sin probar.

## SimpleCov
- Es una **gema** que nos permite ver **cuántas líneas hemos testeado, y cuántas no**.
- Para instalarlo hay que agregar la gema al archivo **Gemfile** y ejecutar **`bundle install`** para que se instale:
- `gem 'simplecov', require: false, group: :test`

![SimpleCov - líneas no cubiertas](adjuntos/SimpleCov%20-%20líneas%20no%20cubiertas.png)

> [!note]- Transcripción de la imagen
> "Líneas de código no cubiertas": en el método `create` del controlador (`# POST /books`), las líneas del caso exitoso (`if @book.save` … `redirect_to book_url(@book), notice: "Book was successfully created."`) están en **verde** (cubiertas). La línea `render :new, status: :unprocessable_entity` está en **rojo**: no se ejecutó.
>
> *"Creamos un test para la creación exitosa de un libro, pero no consideramos cuando un libro no puede ser creado."*

Documentación: https://guides.rubyonrails.org/

> [!tip] Complemento — configuración completa (slides "Testing")
> 1. En el `Gemfile`: `gem 'simplecov', require: false, group: :test` y luego `bundle install`.
> 2. Al **inicio** de `test/test_helper.rb` (o `spec_helper.rb`), antes de todo lo demás:
> ```ruby
> require 'simplecov'
> SimpleCov.start
> # el contenido anterior del archivo debe ir aquí abajo
> ```
> 3. Correr `rails test`. SimpleCov crea una carpeta **`coverage/`** con HTML: se abre `coverage/index.html` en el navegador.
>
> - Para cubrir la línea roja del ejemplo, falta un test que intente crear un libro **inválido** y verifique que no se creó, por ejemplo con `assert_no_difference("Book.count")`.
> - **Ojo:** 100% de cobertura no significa que no haya bugs. Solo dice que cada línea se ejecutó al menos una vez, no que se verificó bien su resultado.
> - Los apuntes escriben la gema con comillas tipográficas (`‘simplecov’`) y `group :test`. En el `Gemfile` van comillas rectas y `group: :test`.

## Preguntas de repaso

1. ¿Qué mide la cobertura de código?
> [!question]- Respuesta
> El porcentaje de líneas (o ramas) del código que se ejecutan al correr los tests.

2. ¿Qué pasos hay para usar SimpleCov en Rails?
> [!question]- Respuesta
> Agregar la gema al Gemfile (grupo test) y hacer `bundle install`; poner `require 'simplecov'` y `SimpleCov.start` al inicio de `test/test_helper.rb`; correr los tests y abrir `coverage/index.html`.

3. ¿Qué test falta en el ejemplo de la imagen?
> [!question]- Respuesta
> Uno que intente crear un libro inválido (que no pasa las validaciones) y verifique que no se crea y que se renderiza `new` con status 422.

4. ¿Una cobertura del 100% garantiza que no hay bugs?
> [!question]- Respuesta
> No. Solo indica que todas las líneas se ejecutaron, no que los asserts verifiquen todos los comportamientos ni todos los casos de datos.
