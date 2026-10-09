---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[03 - Niveles de testing en Rails|Niveles de testing en Rails]]", "[[10 - Rutas en Rails|Rutas en Rails]]"]
---
# Integration tests en Rails

Un integration test de Rails **envía requests HTTP a la aplicación** (GET, POST, DELETE…) y verifica la respuesta. Así se prueba que los controladores y las rutas funcionan.

## Integration test
![Integration test - index y new](adjuntos/Integration%20test%20-%20index%20y%20new.png)

![Integration test - show](adjuntos/Integration%20test%20-%20show.png)

> [!note]- Transcripción de las imágenes
> ```ruby
> class BooksControllerTest < ActionDispatch::IntegrationTest
>   test "should get index" do
>     get books_url              # envía un GET a "/books"
>     assert_response :success   # y verifica que el response sea success
>   end
>
>   test "should get new" do
>     get new_book_url           # GET a "/books/new"
>     assert_response :success
>   end
> end
>
> class BooksControllerTest < ActionDispatch::IntegrationTest
>   test "should show book" do
>     @book = Book.new(title:"Ing. Software",author:"Juan P.", year:2023)
>     @book.save
>     get book_url(@book)
>     assert_response :success
>   end
> end
> ```
> - Creamos un objeto libro en la base de datos.
> - Hacemos un GET request a `/books/id`, donde id es el del libro recién creado.
> - Se verifica que el HTTP response sea success.

- También se puede **armar la ruta a mano** → `get "/books/#{@book.id}"`

> [!tip] Complemento — crear y borrar (slides "Testing")
> ```ruby
> test "should create book" do
>   assert_difference("Book.count") do          # verifica que el contador aumente en uno
>     post books_url, params: { book: { author: "Juan P.", title: "Ing. Software", year: 2022 } }
>   end
>   assert_redirected_to book_url(Book.last)    # redirige a "/books/id" del último libro
> end
>
> test "should destroy book" do
>   @book = Book.new(title:"Ing. Software", author:"Juan P.", year:2023)
>   @book.save
>   assert_difference("Book.count", -1) do      # verifica que disminuya en uno
>     delete book_url(@book)
>   end
>   assert_redirected_to books_url              # al borrar, redirige a "/books"
> end
> ```
> Armar la URL a mano sirve si uno se confunde con los path helpers.

## Preguntas de repaso

1. ¿Qué hace `get books_url` seguido de `assert_response :success`?
> [!question]- Respuesta
> Envía un GET a `/books` y verifica que la respuesta tenga un código 2xx.

2. ¿Cómo se verifica que un POST creó un registro?
> [!question]- Respuesta
> Envolviendo el `post` en `assert_difference("Book.count") do … end`, que comprueba que la cantidad aumentó en uno.

3. Escribe la ruta a mano equivalente a `book_url(@book)`.
> [!question]- Respuesta
> `"/books/#{@book.id}"`.
