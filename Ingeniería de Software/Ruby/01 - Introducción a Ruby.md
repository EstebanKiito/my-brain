---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/apuntes]
prerrequisitos: []
---
# Introducción a Ruby

Ruby es el lenguaje que se usa en el curso (con el framework Rails). Es interpretado y orientado a objetos: **todo es un objeto**, y se puede probar línea a línea en su consola **irb**.

## Lo esencial (mis apuntes)
- **Método → todo es un objeto**: incluso los números y los strings tienen métodos.
- **irb** → consola de Ruby.
- En clase también se vieron: comparaciones, strings y otros (ver [[07 - Strings y comparaciones en Ruby|Strings y comparaciones en Ruby]]).

> [!tip] Complemento — primeros pasos (slides "Ruby" y libro del curso, cap. 10)
> ```ruby
> puts "Hello World!"
> ```
> ```bash
> ruby -e 'puts "Hello Ruby!\n"'   # ejecutar una línea
> ruby hello.rb                    # ejecutar un archivo
> irb                              # consola interactiva
> ```
>
> **Comentarios:**
> ```ruby
> # Comentario de una línea
> puts "Welcome to Ruby!" # comentario al final de la línea
> =begin
> Comentario de múltiples líneas.
> El código aquí dentro no se interpreta.
> =end
> ```
>
> **Variables y constantes:** no se declara el tipo, y una variable puede cambiar de tipo.
> ```ruby
> MYCONSTANT = "hello"   # constante: en mayúsculas
> var1 = Person.new
> var2 = 230
> var3 = "hola"
> var2 = Array.new       # var2 ahora es un arreglo
> ```

> [!example] Ejemplo extra — "todo es un objeto"
> ```ruby
> 5.class          # => Integer
> 5.even?          # => false
> 3.times { print "hola " }
> "hola".upcase    # => "HOLA"
> nil.to_a         # => []
> ```
> Hasta `nil` es un objeto (de la clase `NilClass`).

## Preguntas de repaso

1. ¿Qué significa que en Ruby "todo es un objeto"?
> [!question]- Respuesta
> Que todos los valores, incluidos números, strings, `nil` y las clases, son objetos con métodos. Por ejemplo, `5.even?` o `"hola".length`.

2. ¿Para qué sirve irb?
> [!question]- Respuesta
> Es la consola interactiva de Ruby: permite ejecutar código línea a línea y ver el resultado al instante.

3. ¿Cómo se escribe un comentario de varias líneas?
> [!question]- Respuesta
> Entre `=begin` y `=end`, cada uno al inicio de su línea.
