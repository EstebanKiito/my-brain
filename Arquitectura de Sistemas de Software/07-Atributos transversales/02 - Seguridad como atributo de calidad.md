---
ramo: "Arquitectura de Sistemas de Software"
tema: "Atributos transversales"
tags:
  - arquisis/atributos
  - arquisis/seguridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Elasticidad frente a escalabilidad]]"
---

# Seguridad como atributo de calidad

La seguridad es el atributo transversal por excelencia: está en los algoritmos y herramientas que se programan, pero también en el monitoreo de la operación, porque un atacante no llega cuando se escribe el código, sino cuando el sistema está funcionando. Casi siempre aparece en los enunciados de prueba, y hay que saber justificarla y nombrar principios concretos.

## Definición

> [!tip] Seguridad
> **Grado en que el software protege la información y el acceso a los datos.** Es **completamente transversal** e involucra a diversos actores y sistemas.

Un sistema totalmente bloqueado no es seguro: es inútil. Si un cliente no puede leer su propia información, se perdió la capacidad funcional. **La seguridad debe convivir con la disponibilidad.**

**Conceptos clave:**
- **Autenticación** (quién eres) y **autorización** (qué puedes hacer).
- **Control de acceso (AC)**: RBAC, basado en roles; CBAC o ABAC, basado en contexto o atributos.
- **IAM** (*Identity and Access Management*): gestión centralizada de identidades y permisos, como IAM de AWS.

## Principios

| Principio | Qué significa | Ejemplo |
|---|---|---|
| **Mínimo privilegio** | Cada sistema o usuario solo tiene acceso a lo que necesita para su tarea | El worker de reportes tiene permiso de solo lectura en la base |
| **Defensa en profundidad** | Múltiples capas de defensa: si una falla, quedan otras | WAF + API Gateway con autenticación + autorización en el servicio + cifrado en la base |
| **Fail-safe** | Si el sistema falla, debe quedar en un **estado seguro** | Si roban un reloj inteligente, se bloquea completo; si falla el servicio de permisos, se deniega el acceso en vez de permitirlo |
| **Separación de responsabilidades** | Cada sistema se enfoca en una tarea, así un atacante no compromete todo | El servicio de pagos está aislado del de catálogo |
| **Diseño abierto** | La seguridad no depende de que el diseño sea secreto; se usan algoritmos públicos y probados | Usar AES o bcrypt en vez de un cifrado propio |

## En la práctica

- Usualmente **está presente, pero no es la máxima prioridad**, salvo en dominios sensibles (salud, finanzas, identidad).
- **Compliance:** normas y estándares que el sistema debe cumplir (por ejemplo, de datos personales o de la industria de tarjetas).
- **Data safety:** protección y respaldo de los datos.
- **Debe ser manejada por expertos.** Si no, los resultados pueden ser catastróficos.
- **Requiere testeo constante:**
  - **Pentest** (pruebas de penetración, de distintos "sombreros" según el conocimiento del atacante simulado);
  - **escaneos de vulnerabilidades**;
  - **protección y educación de usuarios** (phishing, contraseñas).

> [!example]- Respuesta modelo: datos faciales en un supermercado sin cajeros
> **Problema:** el sistema autentica clientes por reconocimiento facial y se teme que un intermediario obtenga esos datos, desde el sistema o desde la base, y los use en otro lado.
> **Respuesta:** a diferencia de un token, **el rostro no se puede cambiar** si se filtra. Por eso no se guardan los datos faciales en claro: se guarda un **hash o un cifrado** de los puntos característicos, y la comparación se hace en el backend contra esa versión protegida. Las comunicaciones van con **TLS**.

> [!warning] "Agregar seguridad" no es una respuesta
> En las pautas se espera una **medida concreta** (cifrado o hashing de qué dato, OAuth2 para delegar acceso, mínimo privilegio en qué componente, WAF delante de qué) y **por qué** ataca la amenaza del enunciado. Nombrar "seguridad" en abstracto no suma.

## Preguntas de repaso

> [!question]- ¿Por qué la seguridad es un atributo transversal?
> Porque depende tanto de lo que se programa (algoritmos, validaciones, control de acceso) como de la operación (monitoreo, detección de ataques, parches). Los ataques ocurren con el sistema funcionando.

> [!question]- ¿Por qué un sistema totalmente bloqueado no se considera seguro?
> Porque pierde su capacidad funcional: si ni los usuarios legítimos pueden acceder, el sistema no cumple su propósito. La seguridad debe proteger sin eliminar la disponibilidad.

> [!question]- Explique fail-safe con un ejemplo de software.
> Ante una falla, el sistema debe quedar en un estado seguro. Si el servicio que verifica permisos no responde, la API debe denegar el acceso en vez de permitirlo por defecto.

> [!question]- ¿Qué es defensa en profundidad y cómo se vería en una API web?
> Tener varias capas de protección independientes: un WAF que filtra tráfico malicioso, una API Gateway que autentica, autorización por recurso en cada servicio y cifrado de los datos en la base. Si una capa falla, las demás siguen protegiendo.

> [!question]- ¿Por qué el principio de diseño abierto recomienda algoritmos públicos?
> Porque su seguridad fue revisada por muchos expertos y no depende de que el diseño sea secreto. Un algoritmo propio "secreto" suele tener fallas que nadie revisó y, si se filtra, queda expuesto.

> [!question]- Mini caso: un worker que genera reportes usa las mismas credenciales de administrador que la API. ¿Qué principio se viola y cómo se corrige?
> Mínimo privilegio. Si comprometen el worker, el atacante obtiene acceso de administrador. Hay que darle credenciales propias con permisos de solo lectura sobre las tablas que necesita.

> [!question]- ¿Por qué los datos biométricos requieren más protección que una contraseña?
> Porque no se pueden cambiar si se filtran: una contraseña se reemplaza, un rostro no. Por eso se guardan hasheados o cifrados y nunca en claro, y se transmiten por canales cifrados.
