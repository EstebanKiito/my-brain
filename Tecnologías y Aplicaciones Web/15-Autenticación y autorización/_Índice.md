# Autenticación y autorización — índice

Cómo saber quién es el usuario y qué puede hacer: la diferencia entre autenticar y autorizar, los factores de autenticación y qué hace segura una contraseña, cómo guardarlas con hashing y bcrypt, qué son los JWT y cuándo no usarlos, y cómo delegar el acceso con OAuth o iniciar sesión una sola vez con SSO.

Volver al [[Tecnologías y Aplicaciones Web/_Índice|mapa del ramo]].

> [!note] Origen
> Construido con las slides de la clase de autenticación y autorización (factores, consejos de implementación, contraseñas débiles, encriptación frente a hashing, bcrypt y su formato, JWT y su estructura, Express con jsonwebtoken y express-jwt, JWT frente a sesiones, OAuth 2.0 y SSO). bcrypt y JWT se probaron con Node.js, incluido el hash de ejemplo de la clase.

## Orden de estudio
1. [[01 - Autenticación, autorización y contraseñas|Autenticación, autorización y contraseñas]]: 401 frente a 403, factores, MFA, consejos y fuerza de las contraseñas.
2. [[02 - Hashing de contraseñas con bcrypt|Hashing de contraseñas con bcrypt]]: encriptación frente a hashing, salt, rainbow tables, costo y formato del hash.
3. [[03 - JSON Web Tokens|JSON Web Tokens]]: estructura, firma, uso en Express, revocación y por qué no usarlos como sesión.
4. [[04 - OAuth y Single Sign-On|OAuth y Single Sign-On]]: delegar acceso sin contraseña, flujo de código, OpenID Connect y proveedor de identidad.

Las imágenes de esta carpeta están en `adjuntos/`.
