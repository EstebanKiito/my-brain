---
ramo: Ingeniería de Software
tema: Patrones estructurales
tags: [ingsoft/patrones, ingsoft/ejercicio, patron/estructural, origen/apuntes]
prerrequisitos: ["[[05 - Patrón Proxy|Patrón Proxy]]", "[[03 - Patrón Adapter|Patrón Adapter]]"]
---
# Ejercicio: Proxy y Adapter en mensajería

Ejemplo de prueba (Pregunta 4): sobre un código de mensajería (WeChat), implementar un **Proxy** que vigila los mensajes y un **Adapter** que los transforma.

## Ejemplo de prueba (Adapter + Proxy)
![Ejercicio Proxy y Adapter - enunciado WeChat](../adjuntos/Ejercicio%20Proxy%20y%20Adapter%20-%20enunciado%20WeChat.png)

> [!note]- Transcripción del enunciado
> *Pregunta 4.* Considere el siguiente segmento de código, extraído de la aplicación WeChat (la versión china de WhatsApp).
> ```ruby
> class Contact
>   def receiveMessage(msg)
>     puts "you receive this message #{msg}"
>   end
> end
> class MessageSender
>   def initialize(cnt)
>     @contact = cnt
>   end
>   def sendMessage(msg)
>     @contact.receiveMessage(msg)
>   end
> end
> secretContact = Contact.new
> sender = MessageSender.new(secretContact)
> sender.sendMessage('saludos desde marte')
> ```
> - **(5 pts)** Implementar el **patrón proxy** de forma que el objeto proxy imprima en consola "Potencial Capitalista" cuando un mensaje enviado tenga la palabra *Trump*.
> - **(5 pts)** Implementar el **patrón adapter** para que, cuando alguien envíe la palabra "F", adapte el mensaje enviando el texto "@#@$" en su lugar.

## Solución
![Ejercicio Proxy y Adapter - solución WeChat](../adjuntos/Ejercicio%20Proxy%20y%20Adapter%20-%20solución%20WeChat.png)

> [!note]- Transcripción de la solución
> *Para cada inciso bastaba con escribir la clase Proxy y la clase Adapter.*
> ```ruby
> class ProxyContact
>   def initialize(originalContact)
>     @originalContact = originalContact
>   end
>   def receiveMessage(msg)
>     if msg.include? "Trump"
>       puts "Potencial Capitalista"
>     end
>     @originalContact.receiveMessage(msg)
>   end
> end
>
> class AdapterContact
>   def initialize(originalContact)
>     @originalContact = originalContact
>   end
>   def receiveMessage(msg)
>     newMsg = msg.replace("F","@#@$")
>     @originalContact.receiveMessage(newMsg)
>   end
> end
> ```
> Criterios de corrección: la parte que busca "Trump" o reemplaza "F" puede variar (por ejemplo, con un igual). La idea es que el código dé a entender esa búsqueda o reemplazo. **No importa si no se recuerda el nombre exacto de la función.** También es válido comparar mensajes iguales a "F" (`msg == "F"`).

> [!warning] Detalle de Ruby (registrado en `_meta/DUDAS.md`)
> `String#replace` **reemplaza todo el contenido** del string y recibe **un solo argumento**: `msg.replace("F","@#@$")` lanza `ArgumentError`. Lo correcto es `msg.gsub("F", '@#@$')`. Conviene usar comillas simples para que `#@` no se confunda con una interpolación. La pauta acepta el error porque no exige el nombre exacto de la función.

> [!tip] Complemento — uso
> ```ruby
> secretContact = Contact.new
> sender = MessageSender.new(ProxyContact.new(secretContact))
> sender.sendMessage('Trump dijo hola')   # Potencial Capitalista / you receive this message Trump dijo hola
>
> sender = MessageSender.new(AdapterContact.new(secretContact))
> sender.sendMessage('F')                  # you receive this message @#@$
> ```
> Ninguna de las clases originales (`Contact` y `MessageSender`) se modifica: solo se le pasa a `MessageSender` el envoltorio en vez del contacto. Diferencias entre ambos: [[03 - Adapter vs Proxy vs Decorator|Adapter vs Proxy vs Decorator]].

## Preguntas de repaso

1. ¿Qué interfaz deben tener `ProxyContact` y `AdapterContact`, y por qué?
> [!question]- Respuesta
> La misma que `Contact`, el método `receiveMessage(msg)`, para que `MessageSender` los use sin cambios.

2. ¿Por qué `ProxyContact` es un proxy y no un decorador?
> [!question]- Respuesta
> Porque su intención es vigilar o controlar el acceso (detectar "Trump") antes de delegar, sin cambiar el mensaje que recibe el contacto real.

3. Corrige la línea `newMsg = msg.replace("F","@#@$")`.
> [!question]- Respuesta
> `newMsg = msg.gsub("F", '@#@$')`.
