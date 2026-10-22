---
ramo: "Seguridad Computacional"
tema: "Seguridad web"
tags:
  - seguridad/web
  - origen/complemento
prerrequisitos:
  - "[[02 - Ataques web: CSRF, XSS y clickjacking]]"
---

# OWASP Top 10

**OWASP** (*Open Web Application Security Project*) publica las diez categorías de riesgo más comunes en aplicaciones web, basadas en las **CWE** (*Common Weakness Enumerations*). Cada una resume qué falla y cómo prevenirla.

| Categoría | Qué es | Ejemplo | Prevención clave |
|---|---|---|---|
| **Control de acceso roto** | Se rompe el privilegio mínimo: se manipula la URL o un identificador para ver datos ajenos | `accountInfo?acct=notmyacct`; API sin control en POST/PUT/DELETE | Denegar por defecto; implementar el control una vez y reutilizarlo; limitar la tasa |
| **Fallo criptográfico** | Datos en claro, algoritmos o claves débiles, certificados sin validar | Contraseñas con hash simple y sin sal | Cifrar en reposo y en tránsito; hash adaptativos (Argon2, scrypt, bcrypt, PBKDF2); no guardar lo innecesario |
| **Inyección** | Datos del usuario concatenados en una consulta o comando | `"SELECT * FROM accounts WHERE custID='" + id + "'"` | Consultas **parametrizadas** o ORM; validar y escapar |
| **Diseño inseguro** | Falta o es ineficaz un control en el diseño (distinto de un bug de implementación) | Reservas grupales sin límite, sin protección contra bots revendedores | Modelado de amenazas, ciclo de desarrollo seguro |
| **Configuración insegura** | Valores por defecto, cuentas de fábrica, errores con *stack traces*, funciones innecesarias | Consola de administración con credenciales por defecto | Plataforma mínima; entornos configurados igual; segmentar |
| **Componentes vulnerables o desactualizados** | Dependencias sin parchear o sin inventario | Struts 2 (CVE-2017-5638); Heartbleed | Gestión de parches, inventario, fuentes oficiales y firmadas |
| **Fallos de identificación y autenticación** | Credential stuffing, contraseñas débiles, sesión en la URL, sin MFA | Contraseñas como único factor | MFA, sin credenciales por defecto, limitar intentos, ID de sesión nuevo y aleatorio |
| **Fallos de integridad de software y datos** | Actualizaciones, CI/CD o datos serializados sin verificar | SolarWinds; deserialización insegura de Java | Firmas digitales, repositorios confiables, revisión de cambios |
| **Fallos de logs y monitoreo** | No se registran ni vigilan eventos | Una brecha de siete años sin detectar | Registrar fallos con contexto, monitorear y tener plan de incidentes |

(La lista oficial incluye también falsificación de solicitudes del lado del servidor; en clase se vieron las nueve anteriores y quedaron "casi" calidad de código, DDoS y manejo de memoria.)

## Inyección SQL

![Tira Exploits of a Mom sobre inyección SQL](adjuntos/Tira%20Exploits%20of%20a%20Mom%20sobre%20inyecci%C3%B3n%20SQL.png)

> [!example]- Transcripción de la imagen
> Tira de cuatro viñetas: la escuela llama a una madre por "problemas informáticos" y pregunta si de verdad llamó a su hijo `Robert'); DROP TABLE Students;--`. Ella responde "Sí, lo llamamos Bobby Tables". La escuela perdió los registros del año y ella espera que "hayan aprendido a sanear sus entradas de base de datos".

El nombre cierra la cadena, termina la consulta y agrega `DROP TABLE`; la solución es no concatenar nunca y usar consultas parametrizadas. Ver [[Bases de Datos/_Índice|Bases de Datos]].

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre diseño inseguro e implementación insegura?
> El diseño inseguro es un control que falta o no existe en el diseño; la implementación insegura es un bug en un diseño correcto. Tienen causas y remedios distintos.

> [!question]- ¿Por qué una consulta parametrizada evita la inyección?
> Porque separa la estructura de la consulta de los datos: el intérprete trata la entrada solo como dato, aunque contenga comillas o comandos.

> [!question]- ¿Qué tienen en común "componentes vulnerables" y "fallos de integridad"?
> Que se confía en código o actualizaciones de terceros sin verificarlos: un componente desactualizado o una actualización alterada compromete a toda la aplicación.
