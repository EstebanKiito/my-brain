---
ramo: "Seguridad Computacional"
tema: "TLS y certificados"
tags:
  - seguridad/redes
  - criptografia
  - origen/complemento
prerrequisitos:
  - "[[01 - TLS 1.3 y el canal seguro]]"
---

# Certificados y autoridades certificadoras

Sin certificado, TLS da una conexión privada y autenticada, pero **¿con quién?** Cifrar vale poco si no se sabe con quién se habla: el cliente debe verificar que `PK_S` es realmente de `amazon.com`. Los certificados web nacieron a mediados de los 90 para generar confianza en el comercio electrónico.

## Qué es y qué contiene
Un **certificado** liga un nombre (normalmente DNS) a una clave pública: incluye el **sujeto** (`amazon.com`), su **clave pública**, la **fecha de expiración** (uno o dos años), el identificador de la **CA** emisora y la **firma** de la CA sobre todo.

Una **autoridad certificadora** (CA) es una organización confiable que valida la relación DNS → clave pública: el sitio genera su par de claves, envía la clave pública y una prueba de propiedad, y la CA firma el certificado (o rechaza). Los navegadores traen preinstaladas las claves públicas de decenas de CAs raíz.

Al conectarse, el navegador comprueba que: el nombre coincida con el URL, la CA sea reconocida, la firma sea válida, no haya expirado ni esté revocado, y el servidor demuestre poseer la clave privada. Si algo falla, bloquea la página. No se consulta a la CA en línea porque sería lento, frágil y la CA podría registrar tu navegación.

## Tipos
- **DV** (*Domain Validated*): la CA solo verifica el control del dominio con chequeos técnicos (un archivo o un registro DNS); automatizado, rápido y barato (Let's Encrypt, protocolo ACME). Depende de que DNS y el enrutamiento funcionen.
- **EV** (*Extended Validation*): certifica a la organización; caro y poco útil, porque los usuarios no distinguen la diferencia.

## Qué garantiza el candado
Un certificado válido para `amazon.com` impide que alguien que redirige tus paquetes (WiFi, DNS) se haga pasar por el sitio: el atacante puede mostrar el certificado real, pero no tiene la clave privada; con un certificado propio, el navegador lo rechaza.

> [!warning] Lo que el candado no dice
> No dice "esta página es segura": solo que hablas con el dueño del nombre DNS mostrado. Si no revisas el URL, el phishing (`g00gle.com`) funciona igual. Los usuarios son el eslabón débil.

## Cuando las CAs fallan
Cualquier CA puede emitir un certificado para **cualquier** nombre, y el navegador confía en cientos. Si una CA es engañada, hackeada o coaccionada, un atacante con un certificado válido para `gmail.com` y control de la red hace un MitM perfecto, con candado. En 2011 dos CAs emitieron certificados falsos (por ejemplo para google.com) usados para interceptar Gmail.

### Defensas
| Mecanismo | Idea |
|---|---|
| **Key pinning** | Detectar cambios de clave respecto de visitas previas (TOFU) o una lista de CAs permitidas por dominio; HPKP por cabecera es potente pero peligroso si se configura mal |
| **Registros CAA** | El dueño del dominio dice a qué CAs permite emitir |
| **Certificate Transparency** | Registro público de todos los certificados; las CAs deben registrarlos, los navegadores rechazan los no registrados y los dueños monitorean falsos |

## Revocación
Si se roba una clave, el certificado sigue pareciendo válido hasta expirar. Las **CRL** (listas firmadas de revocados) son grandes y el navegador suele aceptar el certificado si no las alcanza; **OCSP** pregunta en línea (lento, poco fiable, filtra privacidad); **OCSP stapling** adjunta en el handshake la respuesta firmada, que funciona como un certificado de corta vida (bandera *must staple*). La revocación sigue siendo un punto débil.

## Preguntas de repaso

> [!question]- ¿Por qué un atacante que intercepta el tráfico no puede usar el certificado real de Amazon?
> Porque el certificado liga el nombre a la clave pública de Amazon; sin la clave privada, el atacante no puede completar el handshake ni descifrar la clave de sesión.

> [!question]- ¿Qué problema resuelve Certificate Transparency?
> Que una CA emita en secreto un certificado falso: al obligar a registrarlos públicamente, el dueño del dominio puede detectarlo, y los navegadores rechazan los no registrados.

> [!question]- ¿Qué diferencia hay entre validar un dominio y validar una organización?
> DV solo prueba el control técnico del dominio; EV intenta certificar quién es la organización, aunque en la práctica los usuarios no lo notan.
