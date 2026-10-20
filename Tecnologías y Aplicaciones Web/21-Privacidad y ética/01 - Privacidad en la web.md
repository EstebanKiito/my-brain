---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Privacidad y ética"
tags:
  - web
  - privacidad
  - origen/complemento
prerrequisitos:
  - "[[03 - Abusos de las cookies]]"
---

# Privacidad en la web

Cada aplicación web recolecta datos: correos, contraseñas, direcciones, historiales de compra, ubicación. Quien desarrolla decide qué se guarda, cuánto tiempo y quién lo ve. La privacidad no es solo un tema legal: es una decisión técnica que se toma al diseñar las tablas, las cookies y los formularios. Esta nota define los conceptos básicos.

## Privacidad frente a seguridad

| | **Privacidad** | **Seguridad** |
|---|---|---|
| Qué es | Darle a los usuarios el **derecho a controlar** cómo se recolectan, almacenan y usan sus datos, y no usarlos irresponsablemente | **Proteger** los datos y sistemas privados contra accesos no autorizados (datos internos, de usuarios y externos) |
| Pregunta | ¿Debería tener y usar este dato? | ¿Está protegido este dato? |

> [!tip] Se necesitan ambas
> Un sistema puede ser muy seguro y no respetar la privacidad (guarda perfectamente protegido todo lo que el usuario hace, y lo vende). Y una política de privacidad impecable no sirve si la base de datos se filtra.

## Conceptos clave

- **Información personal**: cualquier información que describa a un usuario, como atributos físicos, dirección, identificadores, historial médico, credenciales o datos biométricos.
- **Información personal identificable** (PII): información que, completa o en parte, sirve para **identificar** o seguir a una persona específica.
- **Tracking**: un tercero registra la actividad de un usuario **a través de distintos sitios**, y arma un perfil con sus intereses (para anuncios, venta de datos, etc.). Las cookies de terceros son su herramienta clásica.
- **Fingerprinting**: identificar a un usuario **sin cookies**, combinando datos que su navegador entrega al conectarse: las fuentes instaladas, la resolución, el idioma, la zona horaria, los tiempos de carga.

> [!warning] Borrar las cookies no basta contra el fingerprinting
> La combinación de muchos datos aparentemente inofensivos puede ser única para cada navegador. Por eso el fingerprinting sigue identificando al usuario aunque borre sus cookies o use modo incógnito.

## Qué puede hacer quien desarrolla

Las regulaciones, que se ven en la nota siguiente, traducen la privacidad en obligaciones. Pero el criterio de fondo es anterior a cualquier ley:

- **Minimizar**: guardar solo los datos que realmente se necesitan. Un dato que no se guarda no se puede filtrar.
- **Ser transparente**: decir qué se recolecta, para qué y con quién se comparte.
- **Dar control**: permitir ver, corregir, descargar y borrar los propios datos, y rechazar el tracking.
- **Proteger**: cifrar en tránsito (HTTPS) y en reposo, y hashear las contraseñas.

Para profundizar están el artículo de MDN *Privacy on the web*, el curso de buenas prácticas de privacidad de web.dev, y las extensiones de privacidad y seguridad para Firefox y Chrome.

La privacidad desde la perspectiva de bases de datos (anonimización, k-anonimato y privacidad diferencial) está en [[01 - Privacidad vs seguridad|Privacidad vs seguridad]].

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre privacidad y seguridad?
> La privacidad trata del derecho del usuario a controlar cómo se usan sus datos. La seguridad trata de proteger los datos y sistemas contra el acceso no autorizado. Un sistema puede tener una sin la otra.

> [!question]- ¿Cómo puede un sitio reconocer a un usuario que bloquea todas las cookies?
> Con fingerprinting: combina características del navegador y del dispositivo (fuentes, resolución, idioma, zona horaria) que juntas forman una huella casi única.

> [!question]- ¿Por qué "minimizar los datos" es una buena práctica de privacidad y también de seguridad?
> Porque los datos que no se recolectan no se pueden usar mal ni filtrar. Reducir lo que se guarda reduce a la vez el riesgo para los usuarios y el daño de una eventual brecha.
