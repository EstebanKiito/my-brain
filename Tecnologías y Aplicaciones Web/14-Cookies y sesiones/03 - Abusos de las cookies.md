---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Cookies y sesiones"
tags:
  - web
  - cookies
  - seguridad
  - privacidad
  - origen/complemento
prerrequisitos:
  - "[[02 - Sesiones de usuario]]"
---

# Abusos de las cookies

Que el navegador envíe las cookies **automáticamente** en cada request es lo que las hace útiles para las sesiones. Es también lo que permite abusar de ellas: seguir a un usuario por internet, falsificar acciones en su nombre o robarle la sesión. Conocer estos abusos explica los atributos de `Set-Cookie` y las leyes que regulan su uso.

## Tracking con cookies de terceros

Una **cookie de primera parte** la crea el sitio que se está visitando. Una **cookie de terceros** la crea otro dominio cuyo contenido está incrustado en la página: un anuncio, un botón de "me gusta", un script de analytics.

Si un mismo dominio de publicidad aparece en miles de sitios, su cookie viaja con cada visita a cualquiera de ellos. Así el anunciante arma un **perfil del historial de navegación** del usuario a través de sitios que no tienen relación entre sí, sin que este lo sepa.

> [!warning] El rastreo cruza sitios
> El usuario cree visitar un diario, una tienda y un blog por separado. Para el tercero que está incrustado en los tres, son tres visitas de la misma persona, unidas por la misma cookie.

Por eso los navegadores bloquean cada vez más las cookies de terceros, y leyes como la GDPR exigen **consentimiento** antes de usar cookies que no sean estrictamente necesarias (de ahí los banners de cookies).

## CSRF: actuar en nombre del usuario

En un ataque **CSRF** (*Cross-Site Request Forgery*), un sitio malicioso hace que el navegador de la víctima envíe una request a otro sitio donde la víctima tiene la sesión abierta. Como el navegador agrega las cookies automáticamente, la request llega **autenticada**:

```html
<!-- en sitio-malicioso.com -->
<form action="https://banco.example/transferir" method="POST">
  <input type="hidden" name="destino" value="atacante">
  <input type="hidden" name="monto" value="100000">
</form>
<script>document.forms[0].submit();</script>
```

Defensas:

- **`SameSite=Lax` o `Strict`**: el navegador no envía la cookie en requests que se originan en otro sitio (con `Lax`, solo en navegaciones normales con `GET`).
- **Tokens anti-CSRF**: un valor secreto que el formulario legítimo incluye y que el sitio atacante no puede conocer.

## Robo y fijación de sesión

- **Robo por XSS**: si un atacante logra ejecutar JavaScript en la página, puede leer `document.cookie` y enviarse la cookie de sesión. `HttpOnly` lo impide.
- **Robo en la red**: una cookie enviada por HTTP sin cifrar se puede leer en una red pública. `Secure` obliga a usar HTTPS.
- **Fijación de sesión**: el atacante le hace usar a la víctima un `session_id` que él ya conoce. La defensa es **generar un id nuevo al iniciar sesión**.

| Abuso | Defensa |
|---|---|
| Tracking entre sitios | Bloqueo de cookies de terceros, consentimiento (GDPR) |
| CSRF | `SameSite`, tokens anti-CSRF |
| Robo por XSS | `HttpOnly`, escapar el contenido |
| Robo en la red | `Secure`, HTTPS |
| Fijación de sesión | Regenerar el id al iniciar sesión |

> [!tip] Las cookies no son el problema
> Son un mecanismo neutral. El riesgo aparece cuando se configuran mal (sin `HttpOnly`, `Secure` ni `SameSite`) o cuando se usan para seguir a las personas sin su consentimiento.

## Preguntas de repaso

> [!question]- ¿Por qué un CSRF funciona aunque el atacante nunca vea la cookie de la víctima?
> Porque no necesita verla: el navegador de la víctima la adjunta automáticamente a la request falsificada. El servidor recibe una request autenticada y no distingue que no la originó el usuario.

> [!question]- ¿Cómo permite una cookie de terceros seguir a un usuario por distintos sitios?
> El mismo dominio de terceros está incrustado en muchos sitios, y su cookie viaja con cada visita a cualquiera de ellos. Ese dominio une las visitas en un solo perfil.

> [!question]- ¿Qué atributo de cookie mitiga cada uno de estos ataques: XSS, CSRF y espionaje en una red pública?
> `HttpOnly` contra el robo por XSS, `SameSite` contra CSRF y `Secure` contra el espionaje en la red.
