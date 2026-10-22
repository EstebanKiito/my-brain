---
ramo: "Seguridad Computacional"
tema: "Seguridad web"
tags:
  - seguridad/web
  - origen/complemento
prerrequisitos:
  - "[[01 - Política del mismo origen y cookies]]"
---

# Ataques web: CSRF, XSS y clickjacking

Los ataques web aprovechan las excepciones a la SOP y el envío automático de cookies. Los tres clásicos son CSRF, XSS y clickjacking.

## CSRF (*Cross-Site Request Forgery*)
Una página de `attacker.com` incluye `<IMG SRC="https://bank.com/xfer?amount=500&to=attacker">`. El usuario solo ve una imagen rota, pero si tiene sesión en `bank.com`, el navegador envía la cookie y el banco ve una transferencia legítima. Es un caso de *confused deputy*: el navegador actúa con la autoridad del usuario por orden del atacante.

> [!tip] Defensa
> El servidor incluye un **token aleatorio anti-CSRF** en cada URL o formulario que genera y solo acepta solicitudes con un token legítimo, no usado y asociado al usuario; el atacante no puede predecirlo ni leerlo (por la SOP). `SameSite` también ayuda.

## XSS (*Cross-Site Scripting*)
Un sitio que muestra comentarios de usuarios sin filtrar permite publicar `<SCRIPT>...</SCRIPT>`. El problema no es que corra JS, sino que corre **con el origen del sitio** (por ejemplo `facebook.com`): puede leer la cookie de sesión, actuar como la víctima o enviarla al atacante. Es el tema del laboratorio 4.

Defensas (ninguna sola basta):
- Cookies **HttpOnly**: ocultan la cookie al JS, pero el script aún puede hacer solicitudes como el usuario.
- Quitar o escapar el HTML de las entradas (con una buena biblioteca; los usuarios quieren formato y enlaces).
- Cabecera **Content-Security-Policy**: el servidor prohíbe *scripts* en línea, sin tener que adivinar cómo el navegador interpreta el HTML.
- Cuidado con las subidas de archivos: una "foto" puede ser JavaScript.

## Clickjacking
El navegador trata un clic como autoridad total, y el usuario se guía por pistas visuales. `attacker.com` incrusta un `iframe` de Amazon (con "compra en un clic") **transparente** (`opacity:0`) y pinta encima "¡Haz clic para un iPad gratis!": el clic compra el artículo. Defensa: `X-Frame-Options: DENY` o `Content-Security-Policy: frame-ancestors 'none'`.

## Resumen de la lección
La SOP evita muchos ataques, pero se diseñó por partes y por compatibilidad; un diseño mejor separaría las credenciales de las cookies, indicaría explícitamente qué principal usa cada solicitud (sin autoridad implícita), mezclaría menos JS y HTML y mostraría más claramente a qué se hace clic. Los *frameworks* como Django automatizan escapes y protecciones.

## Preguntas de repaso

> [!question]- ¿Por qué CSRF funciona aunque la SOP impida leer la respuesta?
> Porque al atacante no le importa leer la respuesta, solo causar el efecto (una transferencia), y el navegador envía la cookie de sesión automáticamente.

> [!question]- ¿Por qué XSS es grave aunque JS esté en un sandbox?
> Porque el script inyectado corre con el origen del sitio vulnerable, por lo que la SOP lo trata como código legítimo y puede leer cookies y actuar como el usuario.

> [!question]- ¿Cómo se evita que una página sea usada para clickjacking?
> Prohibiendo que se cargue dentro de un `iframe` ajeno con `X-Frame-Options: DENY` o `frame-ancestors 'none'`.
