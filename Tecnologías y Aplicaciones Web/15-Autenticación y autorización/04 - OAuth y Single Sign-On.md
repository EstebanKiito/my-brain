---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Autenticación y autorización"
tags:
  - web
  - seguridad
  - oauth
  - sso
  - origen/complemento
prerrequisitos:
  - "[[03 - JSON Web Tokens]]"
---

# OAuth y Single Sign-On

Hasta aquí, cada aplicación autentica a sus propios usuarios con su propia contraseña. Pero hay situaciones en que eso no basta: una aplicación que necesita acceder a datos del usuario en **otra** aplicación (sus contactos de Google, sus repositorios de GitHub), o una organización con muchos sitios que quiere un **solo** inicio de sesión. Para eso existen **OAuth** y el **Single Sign-On** (SSO).

## El problema que resuelve OAuth

Una aplicación quiere acceder a recursos del usuario que están en otra aplicación. Pero no tiene autorización para hacerlo ni puede autenticarse en nombre del usuario. La solución trivial sería darle la contraseña, y es pésima: la aplicación obtiene acceso total, para siempre, y si se filtra, se compromete la cuenta completa.

**OAuth 2.0** es el protocolo estándar de la industria para **autorización**, desarrollado en el grupo de trabajo OAuth del IETF. Coordina al usuario y a las aplicaciones para que una aplicación acceda a recursos en nombre del usuario **sin conocer su contraseña**, con permisos limitados (*scopes*) y revocables. Define flujos específicos para aplicaciones web, de escritorio, móviles y otros dispositivos.

## El flujo de código de autorización

![Flujo de autorización OAuth 2.0](adjuntos/Flujo%20de%20autorizaci%C3%B3n%20OAuth%202.0.png)

> [!example]- Transcripción de la imagen
> 1. Bob intenta acceder a su cuenta y sus pedidos en una aplicación.
> 2. La aplicación lo redirige a la pantalla de login del proveedor.
> 3. Bob inicia sesión y concede acceso a sus recursos o datos.
> 4. El proveedor devuelve un código de autorización (*auth code*) a la aplicación.
> 5. La aplicación envía ese código, junto con sus credenciales de cliente, al servidor de autorización.
> 6. El servidor de autorización entrega un *access token* (y un *refresh token*).
> 7. La aplicación usa el token del paso 6 para pedir los datos al servidor de recursos.

La contraseña de Bob solo la ve el proveedor (paso 3), nunca la aplicación. Esta recibe un **access token**, muchas veces un JWT, con permisos acotados y una expiración. Cuando el token vence, el *refresh token* permite pedir uno nuevo sin volver a molestar al usuario.

> [!warning] OAuth es autorización, no autenticación
> OAuth responde "¿puede esta aplicación acceder a estos recursos?", no "¿quién es este usuario?". El botón "Iniciar sesión con Google" usa **OpenID Connect**, una capa de autenticación construida sobre OAuth 2.0 que agrega un token de identidad.

## Single Sign-On

Con **Single Sign-On**, el usuario inicia sesión **una vez** y queda autenticado en varios sitios o aplicaciones. Es lo que ocurre al entrar a distintos servicios de una universidad con la misma cuenta.

![Login por dominio sin SSO](adjuntos/Login%20por%20dominio%20sin%20SSO.png)

> [!example]- Transcripción de la imagen
> "Non-SSO scenario": el usuario navega a `domain1.com` (1), que le pide sus credenciales y lo autentica (2) y guarda una cookie en el navegador (3). Luego navega a `domain2.com` (4), que **vuelve a pedirle** las credenciales (5) y guarda su propia cookie (6).

¿Podría `domain2.com` reutilizar la cookie de `domain1.com`?

![Same origin policy impide compartir la cookie](adjuntos/Same%20origin%20policy%20impide%20compartir%20la%20cookie.png)

> [!example]- Transcripción de la imagen
> "Same-origin-policy forbids this": después de que `domain1.com` guarda su cookie, `domain2.com` intenta leerla (5) y usarla para autenticar al usuario (6). Ambos pasos aparecen tachados con una X roja.

No: el navegador solo envía a cada dominio sus propias cookies (la *same-origin policy* y el atributo `Domain`). Por eso SSO usa un **proveedor de identidad central** (*identity provider*):

1. El usuario entra a `domain1.com`, que lo redirige al proveedor de identidad.
2. El usuario inicia sesión en el proveedor, que guarda su propia cookie de sesión.
3. El proveedor redirige de vuelta a `domain1.com` con un token o una aserción que prueba la identidad.
4. Cuando el usuario entra a `domain2.com`, este también lo redirige al proveedor. Como el proveedor ya tiene su cookie, responde de inmediato **sin pedir credenciales**.

Los estándares más usados para SSO son **SAML** (habitual en organizaciones) y **OpenID Connect**. Servicios como **Auth0** ofrecen autenticación y autorización listas para integrar.

## Preguntas de repaso

> [!question]- ¿Por qué darle la contraseña a una aplicación externa es peor que usar OAuth?
> Porque la aplicación obtendría acceso total e indefinido a la cuenta, y la única forma de quitárselo sería cambiar la contraseña. Con OAuth recibe un token con permisos limitados, que expira y que se puede revocar sin tocar la contraseña.

> [!question]- ¿Qué diferencia hay entre OAuth 2.0 y OpenID Connect?
> OAuth 2.0 es un protocolo de autorización: delega acceso a recursos. OpenID Connect agrega encima una capa de autenticación, con un token de identidad que dice quién es el usuario.

> [!question]- ¿Por qué SSO necesita un proveedor de identidad y no puede compartir una cookie entre dominios?
> Porque el navegador solo envía a cada dominio sus propias cookies. La sesión compartida vive en el proveedor de identidad, al que todos los sitios redirigen, y que reconoce al usuario por su cookie.
