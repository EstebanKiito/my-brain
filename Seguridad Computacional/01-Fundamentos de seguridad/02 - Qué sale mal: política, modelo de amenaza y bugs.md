---
ramo: "Seguridad Computacional"
tema: "Fundamentos de seguridad"
tags:
  - seguridad/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Objetivo, modelo de amenaza, política y mecanismo]]"
---

# Qué sale mal: política, modelo de amenaza y bugs

Los fallos de seguridad caen casi siempre en una de las tres piezas de la nota anterior: la política es inadecuada, el modelo de amenaza supone algo falso, o el mecanismo tiene un bug. Conocer ejemplos de cada tipo entrena a pensar como atacante.

## 1. Problemas con la política
El sistema cumple la política, pero la política es mala.
- **Boleto de clase ejecutiva:** se puede cambiar sin costo "en cualquier momento"; en algunos sistemas incluso después de embarcar, así que el adversario puede abordar y cambiar al vuelo siguiente indefinidamente. Se corrige con la regla "no se cambia tras embarcar".
- **Sistema escolar de Fairfax:** los profesores pueden agregar alumnos a su clase y cambiarles la contraseña. Un alumno con la clave de un profesor agrega al superintendente a su clase, le cambia la clave y entra a todo: la política equivale a "los profesores pueden hacer todo".
- **Cuentas de Mat Honan:** una cadena de políticas razonables por separado pero peligrosas juntas.

![Cadena de restablecimientos Amazon, Apple y Gmail](adjuntos/Cadena%20de%20restablecimientos%20Amazon,%20Apple%20y%20Gmail.png)

> [!example]- Transcripción de la imagen
> Tres círculos: Amazon → Apple → Gmail. Cada servicio sirve para obtener el dato que pide el siguiente: Amazon deja agregar una tarjeta sin autenticar y luego muestra los últimos 4 dígitos de todas; Apple los acepta como prueba de identidad; el restablecimiento de Gmail se envía a la cuenta de Apple.

- **Valores predeterminados inseguros:** contraseñas de fábrica en routers, buckets S3 públicos. Importan porque el operador puede olvidar configurar algo.
- **Sarah Palin:** se podía entrar con contraseña *o* con preguntas de seguridad (adivinables), así que la política era tan débil como la más débil de las dos.

## 2. Problemas con el modelo de amenaza
El diseñador asumió algo que no era cierto.

| Suposición errónea | Caso |
|---|---|
| El diseño o implementación es secreto | [Chip Clipper](https://en.wikipedia.org/wiki/Clipper_chip#:~:text=El%20chip%20Clipper%20fue%20un,estatales%20y%20locales%20decodificar%20las), criptografía propietaria rota |
| Los usuarios piensan en seguridad | Phishing: "haga clic aquí para renovar" |
| Nadie entrega su código 2FA | Engaño por teléfono o sitio falso |
| El atacante usará una solución concreta | CAPTCHA: se esperaba OCR, pero se pagaron humanos a una fracción de centavo |
| Se ejecuta el software esperado | XcodeGhost: espejos de Xcode en China que inyectaban malware; extensiones de Chrome compradas; paquete npm que roba bitcoin |
| Las suposiciones de cómputo no cambian | Claves DES de 56 bits en Kerberos: hoy se rompen por unos US$100 |
| Una máquina sin Internet es segura | Stuxnet se propagó por USB |

## 3. Problemas con el mecanismo (bugs)
Regla práctica: un error cada 1000 líneas de código, y todo error es una explotación potencial.
- **iCloud:** la API *Find my iPhone* olvidó limitar los intentos, permitiendo millones de pruebas de contraseña. Si se requieren muchas verificaciones, una faltará.
- **Citigroup:** cambiando el número en la URL se veían cuentas ajenas; el servidor no comprobaba que el usuario fuera el dueño.
- **Debian/OpenSSL:** al "arreglar" una advertencia se eliminó la siembra del generador pseudoaleatorio, dejando claves adivinables. Un PRNG es determinista una vez fijada la semilla.

## Preguntas de repaso

> [!question]- En el caso de Mat Honan, ¿por qué falla la política aunque cada servicio parezca razonable?
> Porque los servicios se combinan: lo que Amazon trata como dato no sensible (últimos 4 dígitos) lo usa Apple como prueba de identidad. Las políticas individuales están bien, la composición no.

> [!question]- ¿Por qué el caso del CAPTCHA es un error de modelo de amenaza y no de mecanismo?
> El CAPTCHA funcionaba como se diseñó; lo falso era suponer que el atacante intentaría resolverlo con OCR en vez de pagar a personas baratas.

> [!question]- ¿Qué enseña el bug de Debian sobre el código "que no parece de seguridad"?
> Que cualquier cambio puede degradar la seguridad: eliminar una línea para callar una advertencia dejó sin aleatoriedad a todas las claves generadas.
