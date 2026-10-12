---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# Clases y objetos en Ruby

Una **clase** es el molde que define atributos y comportamiento; un **objeto** es una instancia concreta de esa clase. En Ruby **casi todo es un objeto**.

## En Ruby casi todo es objeto
- En Ruby casi todo es **objeto** → tienen **métodos** con los cuales interactuar.

```ruby
	s = String.new("Hola") # => "Hola"
	s.length
	a = Array.new # => []
	a.push(s)
	a.reverse
```

> [!tip] Complemento — definir una clase y crear objetos (slides "Ruby" y "Object Oriented Programming")
> ```ruby
> class BankAccount
>   def initialize(number)
>     @accountNumber = number
>   end
>
>   def deposit(amount)
>     @accountNumber = @accountNumber + amount
>   end
>
>   def withdraw(amount)
>     @accountNumber = @accountNumber - amount
>   end
> end
>
> account = BankAccount.new(1324)   # crea un objeto (instancia)
> account.deposit(200)              # le envía un mensaje: llama a un método
> account.withdraw(100)
> ```
> - `class Nombre … end` define la clase (en `PascalCase`).
> - `Nombre.new(...)` crea una instancia y llama a su [[04 - Constructor initialize en Ruby|constructor `initialize`]].
> - Llamar a un método es **enviarle un mensaje** al objeto. Las cadenas, los arreglos e incluso los enteros son objetos y responden a mensajes.

> [!example] Ejemplo extra
> ```ruby
> 5.class            # => Integer
> "hola".class       # => String
> Integer.class      # => Class   (las clases también son objetos)
> [1, 2].respond_to?(:push)  # => true
> ```

## Preguntas de repaso

1. ¿Qué diferencia hay entre una clase y un objeto?
> [!question]- Respuesta
> La clase define la estructura (atributos) y el comportamiento (métodos). El objeto es una instancia concreta creada a partir de la clase con `new`, con su propio estado.

2. ¿Qué significa "enviar un mensaje" a un objeto?
> [!question]- Respuesta
> Llamar a uno de sus métodos, por ejemplo `s.length`. El objeto busca el método y lo ejecuta (ver method lookup).

3. ¿Por qué se puede escribir `a.push(s)` si `a` es un arreglo?
> [!question]- Respuesta
> Porque el arreglo es un objeto de la clase `Array`, que define el método `push`.
