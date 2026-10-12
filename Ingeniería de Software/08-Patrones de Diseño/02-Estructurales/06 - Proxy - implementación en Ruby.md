---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, patron/estructural, origen/apuntes]
prerrequisitos: ["[[05 - Patrón Proxy|Patrón Proxy]]"]
---
# Proxy: implementación en Ruby

Implementación genérica de [[05 - Patrón Proxy|Proxy]]: un `Proxy` con la misma interfaz que `SujetoReal`, que verifica el acceso antes y registra después.

```ruby
class Sujeto
  # @abstract
  def solicitud
    raise NotImplementedError
  end
end

class SujetoReal < Sujeto
  def solicitud
    puts 'SujetoReal: Manejando solicitud.'
  end
end

# El Proxy tiene una interfaz idéntica al SujetoReal.
class Proxy < Sujeto
  # @param [SujetoReal] sujeto_real
  def initialize(sujeto_real)
    @sujeto_real = sujeto_real
  end

  # Las aplicaciones más comunes del patrón Proxy son la carga diferida, el caching,
  # el control de acceso, el registro, etc.
  # Un Proxy puede realizar una de estas
  # cosas y luego, dependiendo del resultado, pasar la ejecución al mismo
  # método en un objeto SujetoReal vinculado.
  def solicitud
    return unless verificar_acceso

    @sujeto_real.solicitud
    registrar_acceso
  end

  def verificar_acceso
    puts 'Proxy: Verificando acceso antes de realizar una solicitud real.'
    true
  end

  def registrar_acceso
    print 'Proxy: Registrando la hora de la solicitud.'
  end
end

# El código del cliente se supone que debe funcionar con todos los objetos (tanto sujetos como
# proxies) a través de la interfaz Sujeto para soportar tanto sujetos reales como
# proxies. En la vida real, sin embargo, los clientes trabajan mayormente con sus sujetos reales
# directamente. En este caso, para implementar el patrón más fácilmente, puedes extender
# tu proxy de la clase del sujeto real.
def codigo_cliente(sujeto)
  # ...

  sujeto.solicitud

  # ...
end

puts 'Cliente: Ejecutando el código del cliente con un sujeto real:'
sujeto_real = SujetoReal.new
codigo_cliente(sujeto_real)

puts "\n"

puts 'Cliente: Ejecutando el mismo código del cliente con un proxy:'
proxy = Proxy.new(sujeto_real)
codigo_cliente(proxy)
```

> [!tip] Complemento — salida
> ```
> Cliente: Ejecutando el código del cliente con un sujeto real:
> SujetoReal: Manejando solicitud.
>
> Cliente: Ejecutando el mismo código del cliente con un proxy:
> Proxy: Verificando acceso antes de realizar una solicitud real.
> SujetoReal: Manejando solicitud.
> Proxy: Registrando la hora de la solicitud.
> ```
> `return unless verificar_acceso` corta la llamada si no hay acceso: así el proxy **filtra** llamadas. Como `verificar_acceso` devuelve `true`, aquí siempre pasa.

## Preguntas de repaso

1. ¿Qué hace el proxy antes y después de llamar al sujeto real?
> [!question]- Respuesta
> Antes verifica el acceso (`verificar_acceso`) y después registra la hora de la solicitud (`registrar_acceso`).

2. ¿Qué pasaría si `verificar_acceso` devolviera `false`?
> [!question]- Respuesta
> `return unless verificar_acceso` saldría del método: el sujeto real nunca recibiría la solicitud y no se registraría nada.

3. ¿Por qué `codigo_cliente` funciona igual con el sujeto real y con el proxy?
> [!question]- Respuesta
> Porque ambos heredan de `Sujeto` y responden a `solicitud`: el cliente depende solo de esa interfaz.
