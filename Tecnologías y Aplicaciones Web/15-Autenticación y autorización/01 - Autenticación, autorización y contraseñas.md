---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Autenticación y autorización"
tags:
  - web
  - seguridad
  - autenticacion
  - origen/complemento
prerrequisitos:
  - "[[02 - Sesiones de usuario]]"
---

# Autenticación, autorización y contraseñas

Cuando un usuario se identifica, el servidor le asigna un string (un token, un `session_id` u otro) para reconocerlo en cada request. Pero hay dos preguntas distintas que suelen confundirse: **quién es** el usuario y **qué puede hacer**. Además, la identificación puede venir de su contraseña o de un tercero confiable, como su cuenta de Google. Esos mecanismos se construyen sobre estándares (SAML, OAuth, OpenID Connect).

## Autenticación frente a autorización

| | **Autenticación** | **Autorización** |
|---|---|---|
| Pregunta | ¿Es el usuario quien dice ser? | ¿Puede este usuario acceder a este recurso? |
| Ejemplos | Formulario de login, autenticación vía HTTP | Control de acceso a URLs, verificación de permisos o roles |
| Error HTTP típico | `401 Unauthorized` | `403 Forbidden` |

> [!tip] Primero quién, después qué
> Sin autenticación no se puede decidir la autorización: para saber si alguien puede borrar un post, primero hay que saber quién es.

> [!warning] El nombre del 401 confunde
> `401 Unauthorized` en realidad significa "no autenticado" (no se sabe quién eres). `403 Forbidden` es el verdadero "no autorizado" (se sabe quién eres, pero no tienes permiso).

## Factores de autenticación

Se suelen usar uno o dos de estos tres factores:

1. **Algo que el usuario sabe**: una contraseña o un PIN.
2. **Algo que el usuario tiene**: un celular o una llave criptográfica.
3. **Algo que el usuario es**: la huella digital u otro dato biométrico.

Mientras más factores se combinan, más seguro es que el usuario es quien dice ser. Por eso existe la **autenticación multifactor** (MFA): aunque roben la contraseña, falta el segundo factor.

## Consejos de implementación

- Guardar los nombres de usuario **sin distinguir mayúsculas**: `aaossa` es lo mismo que `AAossa` o `AaOssa`.
- Los nombres de usuario deben ser **únicos**.
- Exigir requisitos mínimos **razonables** a las contraseñas, como un largo mínimo y caracteres especiales.
- El factor principal de una contraseña segura es su **largo**: las contraseñas muy cortas se adivinan fácil.
- **No forzar cambios periódicos** de contraseña: llevan a contraseñas más débiles (`Clave1`, `Clave2`…).

## ¿Qué es una contraseña débil?

El conjunto de caracteres posibles es finito, así que cada contraseña es una **aguja en un pajar**. La pregunta correcta no es si "parece" complicada, sino cuántos intentos haría falta para encontrarla. Si cada carácter tiene $k$ opciones y la contraseña tiene $n$ caracteres, hay $k^n$ posibilidades. El largo está en el exponente, así que crece mucho más rápido que agregar símbolos:

$$
\underbrace{94^{8}}_{\text{8 caracteres cualesquiera}} \approx 6 \times 10^{15}
\qquad
\underbrace{26^{20}}_{\text{20 letras minúsculas}} \approx 2 \times 10^{28}
$$

Es la idea del cómic de xkcd *Password Strength*: cuatro palabras comunes al azar son más difíciles de adivinar que una palabra corta con símbolos, y más fáciles de recordar.

> [!warning] Las contraseñas filtradas no sirven
> Una contraseña larga que apareció en una filtración de datos se prueba primero en cualquier ataque. Sitios como **Have I Been Pwned** (de Troy Hunt) y **Mozilla Monitor** permiten revisar si un correo o una contraseña aparecen en brechas conocidas, y algunos servicios los consultan para rechazar contraseñas comprometidas.

## Preguntas de repaso

> [!question]- Un usuario autenticado intenta borrar el post de otro. ¿Es un problema de autenticación o de autorización?
> De autorización: se sabe quién es (está autenticado), pero no tiene permiso para ese recurso. La respuesta adecuada es un `403 Forbidden`.

> [!question]- ¿Por qué MFA protege aunque roben la contraseña?
> Porque el atacante también necesita otro factor de distinta naturaleza, como el celular o la huella del usuario, que no se obtiene con la misma filtración.

> [!question]- ¿Por qué el largo importa más que los símbolos en una contraseña?
> Porque el número de combinaciones es $k^n$: agregar símbolos solo aumenta un poco la base $k$, mientras que alargar la contraseña aumenta el exponente $n$, lo que multiplica las posibilidades mucho más rápido.
