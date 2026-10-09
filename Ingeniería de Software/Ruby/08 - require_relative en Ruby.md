---
ramo: Ingeniería de Software
tema: Ruby
tags: [ingsoft/ruby, origen/apuntes]
prerrequisitos: ["[[01 - Introducción a Ruby|Introducción a Ruby]]"]
---
# require_relative en Ruby

`require_relative` carga otro archivo `.rb` usando una **ruta relativa al archivo que está ejecutando el código**. Sirve para separar las clases en varios archivos.

## Mis apuntes
**`require_relative`** se utiliza para cargar archivos desde una ruta relativa al archivo que está ejecutando el código.

```
proyecto/
├── main.rb
└── lib/
    └── utilidades.rb
#ruby
require_relative 'lib/utilidades'  # Carga el archivo utilidades.rb relativo al archivo actual
```

> [!tip] Complemento — `require` vs `require_relative`
> | | `require` | `require_relative` |
> |---|---|---|
> | Busca en | el *load path* (gemas y librerías) | la carpeta del archivo actual |
> | Uso típico | `require 'json'`, `require 'simplecov'` | tus propios archivos: `require_relative 'item'` |
>
> - La extensión `.rb` se omite.
> - Cada archivo se carga **una sola vez**, aunque se pida varias veces.
> - En Rails casi no se usa, porque Rails carga automáticamente las clases de `app/` (*autoloading*).

> [!example] Ejemplo extra — el ShoppingCar de la clase de Diseño
> ```ruby
> # main.rb
> require_relative "shopping_car"
> require_relative "item"
>
> car = ShoppingCar.new
> car.add(Item.new("Pancito", 5, 200))
> car.print
> ```

## Preguntas de repaso

1. ¿Qué diferencia hay entre `require` y `require_relative`?
> [!question]- Respuesta
> `require` busca en el load path (gemas y librerías instaladas). `require_relative` busca a partir de la carpeta del archivo actual; se usa para tus propios archivos.

2. Si `main.rb` está en `proyecto/` y quiere cargar `proyecto/lib/utilidades.rb`, ¿qué escribe?
> [!question]- Respuesta
> `require_relative 'lib/utilidades'`.

3. ¿Por qué en un proyecto Rails casi no se escribe `require_relative`?
> [!question]- Respuesta
> Porque Rails carga automáticamente (autoloading) las clases de las carpetas de `app/` según sus nombres.
