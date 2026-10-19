# Cookies y sesiones — índice

Cómo un servidor distingue entre clientes si HTTP no tiene estado: qué son las cookies y cómo viajan en los headers `Set-Cookie` y `Cookie`, por qué una cookie con el id del usuario no basta y cómo lo resuelven las sesiones, y cómo se abusa de las cookies (tracking, CSRF, robo de sesión) y cómo se previene.

Volver al [[Tecnologías y Aplicaciones Web/_Índice|mapa del ramo]].

> [!note] Origen
> Construido con las slides de la clase de cookies y sesiones (almacenamiento client-side, qué son las cookies, headers, directivas, flujo de autenticación con cookies, sesiones, cookies frente a session, Express y la discusión sobre abusos). La discusión final se desarrolló con conocimiento general de seguridad web. El manejo de sesiones se probó con Express y cookie-parser.

## Orden de estudio
1. [[01 - Cookies y el header Set-Cookie|Cookies y el header Set-Cookie]]: almacenamiento en el cliente, usos, headers y atributos.
2. [[02 - Sesiones de usuario|Sesiones de usuario]]: session id, flujo con base de datos, cookies frente a sesiones y Express.
3. [[03 - Abusos de las cookies|Abusos de las cookies]]: cookies de terceros, CSRF, robo y fijación de sesión, y sus defensas.
