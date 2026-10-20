---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Privacidad y ética"
tags:
  - web
  - privacidad
  - regulacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Privacidad en la web]]"
---

# GDPR, CCPA y la ley chilena de datos

Las regulaciones de privacidad buscan devolverles a las personas el poder sobre su información personal, regulando a las organizaciones que la recolectan y la usan. Para quien desarrolla no son solo un tema de abogados: varios derechos se traducen directamente en funcionalidades que hay que implementar, como descargar los propios datos o borrar la cuenta.

## GDPR y CCPA

| | **GDPR** (Unión Europea) | **CCPA** (California) |
|---|---|---|
| Vigencia | Adoptada en 2016, aplicada desde 2018 | Activa desde 2018 |
| A quién protege | Residentes de la UE (*data subjects*) | Consumidores residentes en California |
| Qué datos | Cualquier información personal; solo se excluyen los datos anonimizados | Información que identifique, se relacione, describa o se vincule con un consumidor u hogar |
| A quién regula | Controladores y procesadores de datos de personas de la UE | Negocios que operan en California (según condiciones financieras) y quienes procesan sus datos |

## GDPR

| Elemento | Qué exige |
|---|---|
| **Notificación de brechas** (art. 33-34) | Avisar a las personas afectadas por una brecha de sus datos **dentro de 72 horas**. Cuentan como brecha el acceso de un tercero no autorizado, una acción deliberada o accidental del responsable, enviar datos al destinatario equivocado, perder o que roben dispositivos con datos, alterar datos sin permiso y perder su disponibilidad |
| **Derecho de acceso** (art. 15) | Que cada persona pueda ver la información que la empresa tiene sobre ella. De ahí las opciones de "descargar tus datos" de Google o Spotify |
| **Derecho al olvido** (art. 17) | Que la persona pueda pedir que se **borren** sus datos. Hizo visible la diferencia entre "desactivar" y "eliminar" una cuenta |
| **Oficiales de protección de datos** (art. 37-39) | Las empresas que procesan datos de forma sistemática y a gran escala deben tener un DPO, que monitorea el cumplimiento, asesora y es el punto de contacto |
| **Privacidad desde el diseño** (art. 25) | Incluir la privacidad en los productos **desde el inicio**, con medidas técnicas y organizacionales |

Las **sanciones** pueden llegar al **4% de los ingresos mundiales anuales** de la empresa. Sitios como Have I Been Pwned (de Troy Hunt) y Mozilla Monitor avisan si un correo aparece en una brecha conocida.

## Qué significa para el código

GDPR es relevante si personas de la UE usan la aplicación, si hay suscripciones, si hay secciones de comentarios o si se puede iniciar sesión con cuentas de terceros. Algunas prácticas:

- Preguntarse si realmente se necesita cada dato (¿hace falta guardar la IP?).
- Cifrar los datos personales cuando sea posible y usar HTTPS.
- No usar formularios con casillas **pre-marcadas**; pedir consentimiento **granular** para cada tipo de comunicación.
- Separar la aceptación de términos y condiciones del consentimiento sobre los datos personales, y que los términos estén visibles.
- Informar si se comparten datos con terceros, y con quiénes.
- Facilitar el retiro del consentimiento (un enlace de "unsubscribe" en cada correo).
- Evitar preguntas de seguridad basadas en información personal.
- Informar si los logs guardan la IP, y eliminar los datos de usuarios no registrados.
- Permitir rechazar el tracking y **ser razonable con las cookies**.

> [!warning] Los banners de cookies no los exige la ley así
> Bajo GDPR, las cookies que identifican usuarios están reguladas. Se pueden usar por obligación legal, por interés legítimo, para ejecutar un contrato (como un pago) o con consentimiento. Pero si una cookie es **estrictamente necesaria** para el servicio que el usuario pidió, no requiere consentimiento. El "spam" de banners lo generan sobre todo organizaciones que usan los datos de más, y que así hacen parecer que la molestia es culpa de la regulación.

En Estados Unidos, la regla "click-to-cancel" de la FTC buscaba que cancelar una suscripción fuera tan fácil como contratarla. Se anunció en 2024, su aplicación se postergó y un tribunal la anuló en 2025.

## CCPA

La CCPA da a los consumidores de California varios derechos:

- **saber** qué información personal se recolecta;
- **borrar** la información personal recolectada;
- **opt-out**: negarse a que sus datos se vendan o compartan;
- **no discriminación** por ejercer estos derechos;
- **corregir** la información incorrecta;
- **limitar** el uso y la divulgación de la información sensible.

## Chile: la nueva Ley de Protección de Datos

Aprobada en 2024 (Ley 21.719), alinea a Chile con estándares internacionales como GDPR y entra en vigencia en 2026. Establece deberes para los responsables de datos y derechos para los titulares:

| Derecho | Qué permite |
|---|---|
| **Acceso** | Saber si se tratan sus datos, cuáles, su origen, finalidad, destinatarios y por cuánto tiempo |
| **Rectificación** | Corregir datos inexactos, desactualizados o incompletos |
| **Supresión** | Pedir que se eliminen sus datos personales |
| **Oposición** | Oponerse a un tratamiento específico, como marketing directo, datos obtenidos de fuentes públicas o decisiones automatizadas |
| **Portabilidad** | Pedir una copia de sus datos |
| **Bloqueo** | Suspender temporalmente el tratamiento |

Las sanciones van de 5 mil a 10 mil y hasta 20 mil UTM, según la gravedad.

> [!tip] La pregunta de fondo
> ¿Por qué hacen falta estas leyes y por qué se siguen cometiendo infracciones, pese a multas millonarias? Porque los datos son un negocio muy rentable. Por eso quien desarrolla debe considerar las implicancias de su trabajo antes de aceptarlo: los problemas de privacidad y ética son difíciles de remediar una vez construido el sistema.

## Preguntas de repaso

> [!question]- ¿Qué funcionalidades concretas exigen el derecho de acceso y el derecho al olvido?
> Una forma de que el usuario vea y descargue todos sus datos (acceso) y una forma real de eliminar su cuenta y sus datos, no solo desactivarla (olvido).

> [!question]- ¿Toda cookie requiere un banner de consentimiento bajo GDPR?
> No. Las estrictamente necesarias para el servicio que el usuario pidió (como la cookie de sesión) no requieren consentimiento. Sí lo requieren las de tracking o publicidad, entre otras.

> [!question]- ¿Qué tiene en común la ley chilena con GDPR?
> Ambas dan derechos al titular de los datos (acceso, rectificación, supresión, oposición y portabilidad), imponen deberes a quienes tratan datos y contemplan sanciones según la gravedad.
