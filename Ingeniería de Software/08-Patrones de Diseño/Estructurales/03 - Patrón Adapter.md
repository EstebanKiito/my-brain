---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, patron/estructural, origen/apuntes]
prerrequisitos: ["[[01 - Qué es un patrón de diseño|Qué es un patrón de diseño]]"]
---
# Patrón Adapter 🔌

Adapter permite que **colaboren objetos con interfaces incompatibles**: una clase intermedia (el adaptador) traduce las llamadas de uno al formato que espera el otro.

## Definición
- Permite la **colaboración entre objetos con interfaces incompatibles**.

![Adapter - enchufe británico](../adjuntos/Adapter%20-%20enchufe%20británico.png)

## Problemas
- **Incompatibilidad de formatos.**
- Ej.: app de monitoreo que descarga información en **XML**.
- V2: integración con una biblioteca que solo funciona con **JSON**.

## Solución
- Crear un **adaptador** para convertir la interfaz de un objeto → así otro podrá entenderla.

![Adapter - de XML a JSON](../adjuntos/Adapter%20-%20de%20XML%20a%20JSON.png)

- El adaptador obtiene una **interfaz compatible** con uno de los objetos existentes.
- El objeto existente puede invocar con esa interfaz los métodos del adaptador.
- Al recibir una llamada, el adaptador pasa la solicitud al segundo objeto, pero **en el formato que este objeto espera**.

![Adapter - estructura](../adjuntos/Adapter%20-%20estructura.png)

> [!note]- Transcripción de las imágenes
> - **Enchufe:** el enchufe británico expone una interfaz; el laptop de EE. UU. espera otra. El adaptador AC convierte una interfaz en la otra.
> - **XML a JSON:** el "Proveedor de información de bolsa" entrega XML a las "Clases centrales" de la aplicación; un "Adaptador XML a JSON" lo convierte para la "Biblioteca de análisis", que solo entiende JSON.
> - **Estructura (variante de clase):** `Client` → `Existing Class` (`+method(data)`) y `Service` (`+serviceMethod(specialData)`); `Adapter` hereda de ambas y su `method(data)` hace `specialData = convertToServiceFormat(data); return serviceMethod(specialData)`. *"La clase adaptadora no necesita envolver objetos porque hereda comportamientos tanto de la clase cliente como de la clase de servicio."*

## Problema ejemplo (RUT)
![Adapter - problema del RUT](../adjuntos/Adapter%20-%20problema%20del%20RUT.png)

## Solución ejemplo
![Adapter - solución del RUT](../adjuntos/Adapter%20-%20solución%20del%20RUT.png)

> [!note]- Transcripción del ejemplo del RUT
> ```ruby
> class ConsoleClient
>   def initialize(service)
>     @service = service
>   end
>   def run
>     rut = "22.456.456-2"
>     clave = "secreta"
>     if @service.login(rut,clave) then
>       puts "autenticacion exitosa"
>     else
>       puts "autenticacion fallida"
>     end
>   end
> end
>
> class LoginService
>   def initialize()
>     @users = { "22456456-2" => "secreta",
>                "11789789-3" => "password",
>                "33456123-4" => "clave" }
>   end
>   def login_user(rut, pass)
>     return @users[rut.strip] == pass.strip
>   end
> end
>
> # Solución: el adaptador tiene el método que espera el cliente (login)
> class LoginServiceAdapter
>   def initialize(originalService)
>     @originalService = originalService
>   end
>   def login(rut, pass)
>     adaptedrut = rut.gsub(".", "")
>     return @originalService.login_user(adaptedrut, pass)
>   end
> end
>
> service = LoginService.new
> adaptador = LoginServiceAdapter.new(service)
> client = ConsoleClient.new(adaptador)
> client.run
> ```
> Hay dos incompatibilidades: el cliente llama a `login` y el servicio tiene `login_user`; el cliente manda el RUT **con puntos** y el servicio lo espera **sin puntos**.

Implementación genérica: [[04 - Adapter - implementación en Ruby|Adapter: implementación en Ruby]]. Ejercicio: [[04 - Ejercicio - Proxy y Adapter en mensajería|Proxy y Adapter en mensajería]].

> [!tip] Complemento (slides "Patrones de Diseño": Adapter, Proxy, Singleton)
> - Hay dos clases, A y B. A espera que B tenga un método particular, pero B no lo tiene (aunque tenga uno parecido), o A manda un dato en otro formato: son **incompatibles**. Se crea una tercera clase C, **el adaptador**, con el método que A espera, que internamente usa los métodos de B. **No se modifica ni A ni B.**
> - Al cliente se le pasa el adaptador. Como tiene los métodos tal como los necesita el cliente, el cliente no distingue si está usando el adaptador o el servicio original.
> - En Ruby se usa casi siempre la variante **de objeto** (el adaptador *contiene* el servicio), porque Ruby no tiene herencia múltiple.

## Preguntas de repaso

1. ¿Qué problema resuelve Adapter?
> [!question]- Respuesta
> Hacer colaborar dos clases con interfaces incompatibles (nombres de métodos o formatos de datos distintos) sin modificar ninguna de las dos.

2. En el ejemplo del RUT, ¿qué dos incompatibilidades resuelve el adaptador?
> [!question]- Respuesta
> El nombre del método (`login` vs `login_user`) y el formato del RUT (con puntos vs sin puntos, que corrige con `gsub(".", "")`).

3. ¿Por qué el cliente no nota la diferencia?
> [!question]- Respuesta
> Porque el adaptador expone exactamente la interfaz que el cliente espera (`login(rut, pass)`).
