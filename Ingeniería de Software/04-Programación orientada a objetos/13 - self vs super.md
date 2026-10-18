---
ramo: Ingeniería de Software
tema: Programación orientada a objetos
tags: [ingsoft/poo, ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[12 - Method lookup en Ruby|Method lookup en Ruby]]", "[[08 - super en Ruby|super en Ruby]]"]
---
# self vs super

`self` y `super` cambian **desde dónde empieza el method lookup**. `self` parte desde la clase **del objeto real**; `super` parte desde la clase **padre de donde está escrito el código**.

## Definición
- **`self`:** la búsqueda del método parte desde la **clase del objeto** que recibe el mensaje.
- **`super`:** la búsqueda parte desde la **clase padre** de la clase donde está escrita la llamada a `super`.

## Ejemplo 1
```ruby
class A
  def foo
    1
  end

  def bar
    3
  end
end

class B < A
  def bar
    foo + super
  end
end

puts B.new.bar  # 4
```

**Traza:**
1. Se crea un `B` y se llama a `bar`; `B` tiene su propio `bar`, así que se usa ese.
2. `foo` no está en `B`, así que la búsqueda sube a la clase padre: `A#foo` devuelve 1.
3. `super` ejecuta el `bar` de la clase padre: `A#bar` devuelve 3.
4. Resultado: 1 + 3 = **4**.

## Ejemplo 2
```ruby
class S
  def foo
    self.bar
    puts "S>>foo"
  end

  def bar
    puts "S>>bar"
  end
end

class A < S
  def foo
    super
    puts "A>>foo"
  end
end

class B < S
  def bar
    puts "B>>bar"
  end
end

class C < S
  def foo
    puts "C>>foo"
  end
end

S.new.foo  # S>>bar, S>>foo
A.new.foo  # S>>bar, S>>foo, A>>foo
B.new.foo  # B>>bar, S>>foo
C.new.foo  # C>>foo
```

> [!tip] Complemento — traza paso a paso del ejemplo 2
> | Llamada | Traza | Salida |
> |---|---|---|
> | `S.new.foo` | `S#foo` → `self.bar` (self es un S) → `S#bar` | S>>bar, S>>foo |
> | `A.new.foo` | `A#foo` → `super` → `S#foo` → `self.bar`: self es **un A**; A no tiene `bar` → `S#bar` | S>>bar, S>>foo, A>>foo |
> | `B.new.foo` | B no tiene `foo` → `S#foo` → `self.bar`: self es **un B** → **`B#bar`** | B>>bar, S>>foo |
> | `C.new.foo` | `C#foo` lo sobrescribe y no llama a super | C>>foo |
>
> **La clave es B:** aunque `self.bar` está escrito dentro de la clase `S`, la búsqueda parte desde la clase del objeto real (`B`), por eso imprime `B>>bar`. Con `super` pasa lo contrario: siempre parte del padre de la clase donde está escrito, sin importar el objeto.

## Preguntas de repaso

1. ¿Desde dónde empieza a buscar el método `self.metodo` y desde dónde `super`?
> [!question]- Respuesta
> `self.metodo` empieza en la clase del objeto que recibe el mensaje (su clase real). `super` empieza en la clase padre de la clase donde está escrita la llamada.

2. ¿Qué imprime `puts B.new.bar` en el ejemplo 1 y por qué?
> [!question]- Respuesta
> 4. `foo` no está en B y se encuentra en A (1). `super` ejecuta `A#bar` (3). 1 + 3 = 4.

3. En el ejemplo 2, ¿por qué `B.new.foo` imprime "B>>bar" y no "S>>bar"?
> [!question]- Respuesta
> Porque `self.bar` se busca desde la clase del objeto, que es B, y B sobrescribe `bar`. Que `foo` esté definido en S no importa.

4. ¿Qué imprimiría `A.new.bar`?
> [!question]- Respuesta
> "S>>bar": A no define `bar`, así que el lookup sube a S.
