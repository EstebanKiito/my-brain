---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/complemento]
prerrequisitos: ["[[07 - Integration tests en Rails|Integration tests en Rails]]"]
---
# Setup y teardown en tests

> [!tip] Complemento — nota nueva (fuente: slides "Testing")
> **Qué es:** `setup` y `teardown` son bloques que Minitest ejecuta **antes** y **después** de **cada** test de la clase. Sirven para preparar datos comunes y limpiar al final.
>
> ```ruby
> class BooksControllerTest < ActionDispatch::IntegrationTest
>   # código ejecutado antes de cada test
>   setup do
>     @book = books(:jp1)
>   end
>
>   # código ejecutado después de cada test
>   teardown do
>     # normalmente es buena idea resetear el cache
>     Rails.cache.clear
>   end
>
>   test "should show book" do
>     get book_url(@book)          # @book ya viene del setup
>     assert_response :success
>   end
> end
> ```
> - Evita repetir la inicialización en cada test (menos código duplicado).
> - Más información: https://guides.rubyonrails.org/testing.html

## Preguntas de repaso

1. ¿Cuándo se ejecutan `setup` y `teardown`?
> [!question]- Respuesta
> `setup` antes de cada test de la clase y `teardown` después de cada test.

2. ¿Para qué se usa típicamente `teardown`?
> [!question]- Respuesta
> Para limpiar después de cada test, por ejemplo vaciar la caché con `Rails.cache.clear`, para que un test no afecte a otro.

3. ¿Qué ventaja de diseño da `setup`?
> [!question]- Respuesta
> Evita duplicar el código de inicialización en cada test.
