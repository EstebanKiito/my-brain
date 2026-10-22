---
ramo: "Seguridad Computacional"
tema: "Seguridad web"
tags:
  - seguridad/web
  - origen/complemento
prerrequisitos:
  - "[[01 - WebAssembly y aislamiento de fallas de software]]"
---

# Política del mismo origen y cookies

El navegador ejecuta HTML y JavaScript de cualquier sitio que visites, incluidos los maliciosos. Aunque JavaScript corre en un *sandbox* sin acceso a tus archivos, lo relacionado con la web puede ser dañino: leer tu correo, actuar como tú en el banco, mirar sitios de la red interna. La **política del mismo origen** (SOP) es el aislamiento que lo evita.

## Modelo de amenaza
El atacante controla `attacker.com` y lo visitas mientras usas email o banco en otras pestañas. Se supone que el navegador es confiable y sin bugs de implementación y que la red es segura (HTTPS aparte).

## La regla
Un **origen** es protocolo + host + puerto (el de `https://foo.com/x/y` es `https://foo.com:443`). El navegador etiqueta scripts y recursos (páginas, variables JS, servidores) con un origen.

> [!tip] Regla SOP
> Un script solo puede acceder a un recurso si ambos tienen el mismo origen. La unidad de aislamiento es el *frame* (ventana, pestaña o `iframe`).

Así `attacker.com` no puede usar `XMLHttpRequest` contra Gmail, ni leer o cambiar otras ventanas. Se preserva sobre Internet con TLS y certificados (¿los datos vienen de verdad de `gmail.com`?) y con **cookies** (¿la petición viene de mi navegador?).

## Cookies
Permiten a un servidor guardar estado en el navegador: `Set-Cookie: key=value`; el navegador las devuelve en cada solicitud al sitio (el dominio debe ser un sufijo del nombre DNS: `google.com` vale para `mail.google.com`). Típico: al iniciar sesión, el servidor entrega un ID de sesión aleatorio y largo (secreto), que busca en su base de datos.
- Se envían **automáticamente**, lo que causa CSRF. `SameSite=Strict` no las manda en solicitudes de otro origen (pero un enlace desde otra página parece "sin sesión"); `SameSite=Lax` sí las manda con enlaces (Chrome lo usa por defecto).
- Sobrescribirlas: un sitio no debe fijar cookies de otro; la regla del sufijo ayuda y el navegador mantiene una lista de dominios públicos (`.com`, `co.uk`).

## Excepciones a la SOP (por compatibilidad y mashups)
| Excepción | Qué permite | Riesgo |
|---|---|---|
| **Enlaces** | Navegar a otro origen | Se envían cookies: efectos secundarios con tu sesión |
| **`IMG`** | Mostrar imágenes de otros sitios (los píxeles no son legibles) | Se envían cookies: base de CSRF |
| **`SCRIPT`** | Cargar y ejecutar JS de otro origen, **con el origen de la página que lo carga** | Hay que confiar en el script |
| **`IFRAME`** | Mostrar otra página; SOP sigue aislando marco y página | Clickjacking |
| **CORS** | El servidor autoriza explícitamente solicitudes de otros orígenes | Seguro: por defecto es "no" y decide el servidor |

## Preguntas de repaso

> [!question]- ¿Por qué un script cargado con `<script src>` de otro dominio corre con el origen de la página?
> Se trata como código de biblioteca propio de la app; por eso se debe ser cuidadoso con los scripts de terceros, pues tienen acceso total a la página.

> [!question]- ¿Por qué CORS es una excepción segura a la SOP?
> Porque la SOP protege al servidor; si el propio servidor autoriza explícitamente el acceso cruzado, no hay nadie que proteger, y por defecto se niega.

> [!question]- ¿Qué pasa con `SameSite=Strict` al seguir un enlace a un sitio donde ya iniciaste sesión?
> La cookie no se envía porque la solicitud viene de otro origen, así que el sitio te muestra la página de inicio de sesión, aunque estés conectado.
