---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[05 - Atributos y accesores en Ruby|Atributos y accesores en Ruby]]"]
---
# Herencia en Ruby

La herencia permite que una **clase hija** reciba los atributos y métodos de una **clase padre** y agregue o cambie los suyos. En Ruby se escribe `class Hija < Padre`.

## Herencia
La clase hija hereda de la clase padre con `<`, y suma sus propios atributos a los heredados:

```ruby
class Figura
  attr_accessor :stroke, :fill
end

class Circulo < Figura
  attr_accessor :radius  # además de stroke y fill
end

c1 = Circulo.new
c1.fill = "red"          # fill viene de Figura
```

## Jerarquía de clases
La herencia puede tener varios niveles; cada clase acumula lo de todas sus ancestras:

```ruby
# 3 niveles de jerarquía
class Figure
  attr_accessor :stroke, :fill
end

class Circle < Figure
  attr_accessor :radius        # tiene stroke, fill y radius
end

class Cylinder < Circle
  attr_accessor :length        # tiene stroke, fill, radius y length
end
```

> [!tip] Complemento (slides "Object Oriented Programming" y "Ruby")
> - El objeto de la clase `Circle` tiene el atributo `radius` y, **por herencia**, `stroke` y `fill`.
> - Ruby tiene **herencia simple**: una clase tiene un solo padre directo. Para compartir comportamiento entre clases no relacionadas se usan **módulos** (*mixins*).
> - Todas las clases heredan, en última instancia, de **`Object`**. Por eso todo objeto tiene `to_s`, `class`, `==`, etc.
> - En la herencia se apoyan [[08 - super en Ruby|super]], la [[09 - Sobrescritura de métodos (override)|sobrescritura]], las [[10 - Clases abstractas en Ruby|clases abstractas]] y el [[12 - Method lookup en Ruby|method lookup]].
>
> ```mermaid
> classDiagram
>   Figure <|-- Circle
>   Circle <|-- Cylinder
>   class Figure { +stroke +fill }
>   class Circle { +radius }
>   class Cylinder { +length }
> ```

## Preguntas de repaso

1. ¿Qué atributos tiene un objeto `Cylinder` en la jerarquía Figure → Circle → Cylinder?
> [!question]- Respuesta
> `stroke` y `fill` (de Figure), `radius` (de Circle) y `length` (propio).

2. ¿Cómo se indica en Ruby que una clase hereda de otra?
> [!question]- Respuesta
> Con `<`: `class Circle < Figure`.

3. ¿De qué clase heredan todas las clases de Ruby si no se indica otra?
> [!question]- Respuesta
> De `Object`.
