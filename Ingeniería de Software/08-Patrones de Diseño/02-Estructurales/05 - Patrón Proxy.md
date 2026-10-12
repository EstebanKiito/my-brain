---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, patron/estructural, origen/apuntes]
prerrequisitos: ["[[01 - Qué es un patrón de diseño|Qué es un patrón de diseño]]"]
---
# Patrón Proxy 🥷🏻

Proxy es un **sustituto de otro objeto con su misma interfaz**: recibe las llamadas, puede hacer algo antes o después (controlar el acceso, registrar, usar caché, crear el objeto real recién cuando se necesita) y delega en el objeto real.

## Definición
- Proporciona un **sustituto o marcador de posición** para otro objeto.
- **Controla el acceso** al objeto original.
- Permite hacer algo **antes o después** de que la solicitud llegue al objeto principal.

## Problema
- Un objeto enorme que consume muchos recursos y se utiliza a veces, no siempre.
- Podemos crear el objeto solo cuando sea necesario → genera mucho código.

## Solución
- Crear la clase **"Proxy" con la misma interfaz** del objeto original.
- Se actualiza la app para **pasar el proxy** a todos los clientes del objeto original.
- Si necesitamos ejecutar algo entremedio, **no necesitamos cambiar la clase**.

![Proxy - proxy de base de datos](../adjuntos/Proxy%20-%20proxy%20de%20base%20de%20datos.png)

![Proxy - estructura](../adjuntos/Proxy%20-%20estructura.png)

> [!note]- Transcripción de las imágenes
> - *"El proxy se camufla como objeto de la base de datos. Puede gestionar la inicialización diferida y el caché de resultados sin que el cliente o el objeto real de la base de datos lo sepan."*
> - **Estructura:** `Client` → `«interface» ServiceInterface` (`+operation()`), implementada por `Service` (`+operation()`) y por `Proxy` (`-realService: Service`, `+Proxy(s: Service)`, `+checkAccess()`, `+operation()`, que hace `if (checkAccess()) { realService.operation() }`).

## Problema (log de login)
![Proxy - problema del log de login](../adjuntos/Proxy%20-%20problema%20del%20log%20de%20login.png)

## Solución
![Proxy - solución LoginProxy](../adjuntos/Proxy%20-%20solución%20LoginProxy.png)

> [!note]- Transcripción del ejemplo
> *¿Cómo añadir un mensaje en consola (log) cada vez que un cliente hace un login fallido? El requisito es no tocar ninguna de las dos clases (`ConsoleClient` y `LoginService`).*
> ```ruby
> class LoginProxy
>   def initialize(objetoOriginal)
>     @objetoOriginal = objetoOriginal
>   end
>   def login(rut,pass)
>     result = @objetoOriginal.login(rut,pass)
>     if result == false then
>       puts "failed login attempt #{rut}"
>     end
>     return result
>   end
> end
> # client = ConsoleClient.new(LoginProxy.new(LoginService.new))
> ```

Implementación genérica: [[06 - Proxy - implementación en Ruby|Proxy: implementación en Ruby]]. Comparación con patrones parecidos: [[03 - Adapter vs Proxy vs Decorator|Adapter vs Proxy vs Decorator]].

> [!tip] Complemento (slides "Patrones de Diseño": Adapter, Proxy, Singleton)
> - El proxy **tiene la referencia al objeto original**, y los clientes pueden usar el proxy o el original **de forma indistinta**. Para responder, el proxy siempre consulta al original.
> - **¿Para qué sirve entonces?** Puede hacer operaciones **antes y después** de llamar al original, e incluso **filtrar** llamadas.
> - **Tipos comunes:** proxy virtual (*lazy loading*: crear el objeto pesado solo cuando se usa), de protección (control de acceso), de caché, de registro (*logging*) y remoto.

## Preguntas de repaso

1. ¿Qué tiene en común el proxy con el objeto real?
> [!question]- Respuesta
> La misma interfaz, para que el cliente pueda usarlo en lugar del original sin darse cuenta.

2. Nombra tres usos típicos de un proxy.
> [!question]- Respuesta
> Carga diferida (lazy loading), control de acceso, caché y registro (logging) de las llamadas.

3. En el ejemplo de login, ¿cómo se agrega el log sin tocar `ConsoleClient` ni `LoginService`?
> [!question]- Respuesta
> Se crea `LoginProxy`, con el mismo `login`, que delega en el servicio real e imprime "failed login attempt" si el resultado es `false`. Al cliente se le pasa el proxy en vez del servicio.
