---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[04 - Unit tests en Rails|Unit tests en Rails]]"]
---
# Asserts en Minitest

Los *asserts* son las verificaciones de un test: si la condición no se cumple, el test falla con el mensaje opcional `[msg]`. Rails usa el framework **Minitest**.

## Tipos de asserts
| Assert | Verifica |
|---|---|
| `assert( test, [msg] )` | Ensures that test is true. |
| `assert_not( test, [msg] )` | Ensures that test is false. |
| `assert_equal( expected, actual, [msg] )` | Ensures that expected == actual is true. |
| `assert_not_equal( expected, actual, [msg] )` | Ensures that expected != actual is true. |
| `assert_same( expected, actual, [msg] )` | Ensures that expected.equal?(actual) is true. |
| `assert_not_same( expected, actual, [msg] )` | Ensures that expected.equal?(actual) is false. |
| `assert_nil( obj, [msg] )` | Ensures that obj.nil? is true. |
| `assert_not_nil( obj, [msg] )` | Ensures that obj.nil? is false. |
| `assert_empty( obj, [msg] )` | Ensures that obj is empty?. |

> [!tip] Complemento — asserts específicos de Rails (slides "Testing")
> | Assert | Verifica |
> |---|---|
> | `assert_response :success` | que el código HTTP sea 2xx |
> | `assert_redirected_to url` | que la respuesta redirija a esa URL |
> | `assert_difference("Book.count") { … }` | que la expresión aumente en 1 tras ejecutar el bloque (con `-1`, que disminuya) |
>
> - `assert_equal` compara con `==` (igual valor); `assert_same` compara con `equal?` (mismo objeto). Ver [[07 - Strings y comparaciones en Ruby|Strings y comparaciones en Ruby]].
> - **Orden de argumentos:** primero el **esperado** y después el **real**: `assert_equal 4, suma(2, 2)`. Si se invierten, el mensaje de error confunde.

## Preguntas de repaso

1. ¿Qué diferencia hay entre `assert_equal` y `assert_same`?
> [!question]- Respuesta
> `assert_equal` verifica igualdad de valor (`==`); `assert_same` verifica que sean el mismo objeto (`equal?`).

2. ¿Qué assert usarías para verificar que un objeto no es nil?
> [!question]- Respuesta
> `assert_not_nil(obj)`.

3. ¿Qué verifica `assert_difference("Book.count", -1) { delete book_url(@book) }`?
> [!question]- Respuesta
> Que después del request DELETE haya un libro menos en la base de datos.
