---
ramo: "Tecnologías y Aplicaciones Web"
tema: "APIs web y REST"
tags:
  - web
  - api
  - autenticacion
  - origen/complemento
prerrequisitos:
  - "[[02 - CRUD y principios REST]]"
---

# Autenticación con tokens en APIs

REST exige que cada request sea independiente: el servidor no recuerda la anterior. Eso choca con algo que toda aplicación necesita. Si una request no sabe nada de la siguiente, ¿cómo se inicia sesión y se identifica al usuario en cada llamada a la API? La respuesta más común es un **token** que el cliente envía en cada request.

## Access token

Un **access token** es un string de caracteres aleatorios (o de apariencia aleatoria, como en los JWT) que funciona como **credencial**: identifica a un usuario, su grupo, sus permisos o una aplicación. Sirve para **autenticar** al usuario sin que envíe su contraseña en cada request.

## El flujo

```mermaid
sequenceDiagram
    participant C as Cliente
    participant S as Servidor
    C->>S: POST /login {email, password}
    Note over S: Verifica las credenciales
    S-->>C: Respuesta con el token del usuario
    Note over C: Guarda el token
    C->>S: GET /profile (incluye el token)
    Note over S: Identifica al usuario a partir del token
    S-->>C: ¡Hola @aaossa!
```

1. El cliente envía email y contraseña **una sola vez**, a un endpoint de login.
2. El servidor los verifica y responde con un token.
3. El cliente guarda el token de alguna manera.
4. En cada request siguiente, el cliente incluye el token y el servidor identifica al usuario con él.

El token viaja en un **header** de la request, normalmente `Authorization`:

```http
GET /profile HTTP/1.1
Host: api.example.com
Authorization: Bearer token_que_parece_random
```

`Bearer` ("portador") significa que quien porte el token tiene acceso: el servidor no verifica nada más.

> [!warning] Quien tiene el token es el usuario
> Por eso el token nunca debe viajar por HTTP sin cifrar ni quedar expuesto (en la URL, en logs o en código subido a un repositorio). Si alguien lo roba, puede hacer todo lo que el usuario puede hacer, sin conocer su contraseña.

## ¿Y el cierre de sesión?

Si el servidor no guarda estado, "cerrar sesión" no es tan simple: hay que **revocar** el token, para que deje de servir aunque el cliente lo siga enviando. Hay varias estrategias:

- mantener en el servidor una lista de tokens válidos o una de tokens revocados;
- recordar en el servidor cuándo expira cada token;
- **codificar la validez dentro del propio token** (por ejemplo, una fecha de expiración firmada, como en los JWT);
- y otros mecanismos.

Cada estrategia tiene un costo. Las listas obligan al servidor a guardar estado, que es justo lo que REST quería evitar. La expiración dentro del token no permite invalidarlo antes de tiempo. Este equilibrio se retoma al ver cookies, sesiones y JWT.

> [!tip] Autenticación en la API frente a sesión en el navegador
> Con tokens, el cliente decide dónde guardar la credencial y la envía explícitamente en cada request. Con cookies, el navegador la guarda y la envía solo. Ambos enfoques resuelven el mismo problema: que HTTP no tiene estado.

## Preguntas de repaso

> [!question]- ¿Por qué no basta con enviar el email y la contraseña en cada request?
> Porque expondría la contraseña constantemente y obligaría a verificarla (una operación costosa, con hash) en cada llamada. El token se obtiene una vez, se puede revocar o dejar expirar, y puede tener permisos limitados.

> [!question]- ¿En qué parte de la request viaja el token y por qué no en la URL?
> En un header, normalmente `Authorization: Bearer …`. En la URL quedaría registrado en el historial, en los logs del servidor y en las cachés, exponiendo la credencial.

> [!question]- ¿Por qué cerrar sesión es un problema en una API stateless?
> Porque el servidor no recuerda qué tokens entregó. Para invalidar uno antes de tiempo necesita guardar alguna información (una lista de revocados o vigentes), o bien aceptar que el token siga sirviendo hasta que expire.
