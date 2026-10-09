---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, patron/estructural, origen/apuntes]
prerrequisitos: ["[[03 - Patrón Adapter|Patrón Adapter]]"]
---
# Adapter: implementación en Ruby

Implementación genérica de [[03 - Patrón Adapter|Adapter]]: un `Adaptador` hace que la interfaz rara del `Adaptado` se vea como la del `Objetivo` que espera el cliente.

```ruby
# La clase Objetivo define la interfaz usada por el cliente.
class Objetivo
  def solicitud
    'Objetivo: El comportamiento por defecto del objetivo.'
  end
end

# La clase Adaptado contiene una funcionalidad útil, pero su interfaz es incompatible con el cliente.
class Adaptado
  def solicitud_especifica
    '.eetpadA eht fo roivaheb laicepS'
  end
end

# El Adaptador hace que la interfaz del Adaptado sea compatible con la del Objetivo.
class Adaptador < Objetivo
  def initialize(adaptado)
    @adaptado = adaptado
  end

  def solicitud
    "Adaptador: (TRADUCIDO) #{@adaptado.solicitud_especifica.reverse!}"
  end
end

# El código del cliente soporta todas las clases que siguen la interfaz del Objetivo.
def codigo_cliente(objetivo)
  puts objetivo.solicitud
end

puts 'Cliente: Puedo trabajar bien con los objetos del Objetivo:'
objetivo = Objetivo.new
codigo_cliente(objetivo)

adaptado = Adaptado.new
puts 'Cliente: La clase Adaptado tiene una interfaz extraña. Mira, no la entiendo:'
puts "Adaptado: #{adaptado.solicitud_especifica}"

puts 'Cliente: Pero puedo trabajar con ella a través del Adaptador:'
adaptador = Adaptador.new(adaptado)
codigo_cliente(adaptador)
```

> [!tip] Complemento — lectura del código
> | Rol | Clase | Qué hace |
> |---|---|---|
> | Objetivo (*Target*) | `Objetivo` | la interfaz que entiende el cliente: `solicitud` |
> | Adaptado (*Adaptee*) | `Adaptado` | funcionalidad útil con interfaz incompatible: `solicitud_especifica`, que devuelve el texto al revés |
> | Adaptador | `Adaptador < Objetivo` | contiene un `Adaptado` y traduce: llama a `solicitud_especifica` y lo invierte con `reverse!` |
> | Cliente | `codigo_cliente` | solo conoce `solicitud` |
>
> La última línea imprime `Adaptador: (TRADUCIDO) Special behavior of the Adaptee.`
>
> El adaptador hereda de `Objetivo` (para tener su interfaz) y **contiene** al adaptado: es la variante **de objeto**.

## Preguntas de repaso

1. ¿Por qué `Adaptador` hereda de `Objetivo`?
> [!question]- Respuesta
> Para tener la misma interfaz que espera el cliente (`solicitud`) y poder pasarse donde se espera un `Objetivo`.

2. ¿Qué hace `@adaptado.solicitud_especifica.reverse!`?
> [!question]- Respuesta
> Obtiene el string invertido del adaptado y lo da vuelta, traduciéndolo a un formato legible ("Special behavior of the Adaptee.").

3. ¿Se modificó la clase `Adaptado` para que el cliente pudiera usarla?
> [!question]- Respuesta
> No. Esa es la idea del patrón: el adaptador hace la traducción y ninguna de las dos clases originales cambia.
