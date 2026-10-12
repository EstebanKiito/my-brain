---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[04 - Unit tests en Rails|Unit tests en Rails]]"]
---
# Fixtures en Rails

Los fixtures son **datos de ejemplo** definidos en archivos YAML que Rails carga en la base de datos de pruebas, para crear objetos del modelo fácilmente en los tests.

## Fixture
- Nos permite hacer **ejemplos de datos**.
- En Rails nos ayuda a **crear objetos del modelo de manera fácil**.
- `app/test/fixtures/nombre_del_modelo.yml`

![Fixtures - books.yml](adjuntos/Fixtures%20-%20books.yml.png)

> [!note]- Transcripción de la imagen
> ```yaml
> jp1:
>   author: Juan P. Sandoval
>   title: Ingenieria de Software
>   year: 2023
>
> jp2:
>   author: Juan P. Sandoval
>   title: Testing
>   year: 2022
> ```

## Unit test con fixtures
![Unit test con fixtures](adjuntos/Unit%20test%20con%20fixtures.png)

> [!note]- Transcripción de la imagen
> ```ruby
> class Book < ApplicationRecord
>   validates :title, presence: true
>   validates :author, presence: true
>   validates :year, presence: true
> end
>
> class BookTest < ActiveSupport::TestCase
>   test "should not save without title" do
>     @book = books(:jp1)
>     result = @book.save
>     assert_not result,"saved the title without title"
>   end
> end
> ```

> [!warning] Posible error en el ejemplo (viene de la slide; registrado en `_meta/DUDAS.md`)
> El fixture `jp1` **sí tiene título**, así que `@book.save` devuelve `true` y el `assert_not` **falla**. Para probar "sin título" con fixtures hay que quitarle el título primero:
> ```ruby
> test "should not save without title" do
>   @book = books(:jp1)
>   @book.title = ""
>   assert_not @book.save, "saved the book without title"
> end
> ```

> [!tip] Complemento
> - La ruta real en un proyecto es `test/fixtures/books.yml` (dentro de `test/`, no de `app/`).
> - El archivo se llama como la **tabla** (plural) y cada entrada (`jp1`, `jp2`) es un registro que se accede con `books(:jp1)`.
> - Los fixtures se cargan en la base de datos de **test** antes de cada test.

## Preguntas de repaso

1. ¿Qué es un fixture y dónde se define?
> [!question]- Respuesta
> Datos de ejemplo en YAML (`test/fixtures/<tabla>.yml`) que Rails carga en la base de datos de pruebas.

2. ¿Cómo se obtiene en un test el libro definido como `jp2`?
> [!question]- Respuesta
> Con `books(:jp2)`.

3. ¿Por qué el test con `books(:jp1)` de la slide fallaría?
> [!question]- Respuesta
> Porque `jp1` tiene título: `save` devuelve `true` y `assert_not` espera `false`. Hay que vaciar el título antes de guardar.
