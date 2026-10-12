---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[03 - Niveles de testing en Rails|Niveles de testing en Rails]]", "[[07 - Validaciones en Active Record|Validaciones en Active Record]]"]
---
# Unit tests en Rails

Un unit test de Rails verifica **un modelo de forma aislada**. Tiene tres partes: preparar los datos, ejecutar la acción y verificar el resultado con un *assert*.

## Unit test
![Unit test - modelo Book y su test](adjuntos/Unit%20test%20-%20modelo%20Book%20y%20su%20test.png)

> [!note]- Transcripción de la imagen
> ```ruby
> # Modelo
> class Book < ApplicationRecord
>   validates :title, presence: true
>   validates :author, presence: true
>   validates :year, presence: true
> end
>
> # Test
> class BookTest < ActiveSupport::TestCase
>   test "should not save without title" do
>     @book = Book.new(title:"",author:"Juan P.", year:2023)
>     result = @book.save
>     assert_not result,"saved the title without title"
>   end
> end
> ```

```ruby
class BookTest < ActiveSupport::TestCase
	test "No deberia guardarse sin titulo" do
		# Donde se crean objetos y datos necesarios
		@book = Book.new(title:"", author:"Juan P.", year:2023)
		# donde se realiza la accion a evaluar
		result = @book.save
		# verificacion, donde se evalua si el resultado esperado
		# assert o assert_not
		assert_not result, "saved the book without title"
	end
end

# EJECUCIÓN
rails test test/models/book_test.rb
```

## Consideraciones
- Rails tiene **3 bases de datos**:
  - una para **pruebas**,
  - otra de **producción**,
  - y otra para **desarrollo** (esto se puede ver en `config/database.yml`).
- Rails inicializará una **base de datos dedicada** para ejecutar cada prueba; de esta forma cada test se ejecuta de forma **separada y aislada**.

> [!tip] Complemento — estructura y ejecución (slides "Testing")
> Las tres partes del test (conocidas como *Arrange–Act–Assert*):
> 1. **Inicialización:** se crean los objetos y datos necesarios.
> 2. **Estímulo:** se realiza la acción a evaluar.
> 3. **Verificación:** se evalúa si el resultado es el esperado.
>
> Salida al ejecutar:
> ```
> > rails test test/models/book_test.rb
> Running 1 tests in a single process (parallelization threshold is 50)
> Run options: --seed 53778
> # Running:
> .
> Finished in 0.008640s, 115.7407 runs/s, 115.7407 assertions/s.
> 1 runs, 1 assertions, 0 failures, 0 errors, 0 skips
> ```
> Cada `.` es un test que pasó; `F` es una falla y `E` un error.
>
> Más precisamente, Rails ejecuta cada test dentro de una **transacción** que se deshace al final, así los datos de un test no afectan a otro.

## Preguntas de repaso

1. ¿Cuáles son las tres partes de un unit test?
> [!question]- Respuesta
> Inicialización (crear objetos y datos), estímulo (ejecutar la acción a evaluar) y verificación (assert sobre el resultado).

2. ¿Por qué el test usa `assert_not result`?
> [!question]- Respuesta
> Porque se espera que `save` devuelva `false` cuando el libro no tiene título (falla la validación `presence`). Si devolviera `true`, el test fallaría con el mensaje "saved the book without title".

3. ¿Cuántas bases de datos tiene Rails y dónde se configuran?
> [!question]- Respuesta
> Tres: test, development y production, configuradas en `config/database.yml`.

4. ¿Cómo se ejecuta solo el test del modelo Book?
> [!question]- Respuesta
> `rails test test/models/book_test.rb`.
