---
ramo: "Seguridad Computacional"
tema: "Autenticación de usuarios"
tags:
  - seguridad/autenticacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Objetivo, modelo de amenaza, política y mecanismo]]"
---

# Autenticación con contraseñas

Casi toda política de seguridad depende de saber **quién** hace una solicitud. En el modelo del guardia, el servidor tiene un guardia que revisa cada solicitud (mediación completa: el recurso solo es accesible a través de él) y debe decidir qué *principal* la originó. Es un problema fácil de hacer mal porque no es solo técnico: los usuarios eligen contraseñas malas.

## Las tres partes
- **Registro:** establecer el secreto entre usuario y guardia (primero en llegar, verificación por email, o creado por un administrador).
- **Verificación:** el usuario envía (usuario, secreto) y el guardia lo compara con su copia.
- **Recuperación:** qué pasa si se pierde el secreto. Suele pasarse por alto y es el talón de Aquiles (preguntas de seguridad, email, llamar a soporte: vulnerable a ingeniería social).

Además, la solicitud pasa por **principales intermedios** (dispositivo, balanceador, servidor de aplicaciones) que "hablan por" el usuario: si el dispositivo tiene un *keylogger*, el atacante captura la clave. Y normalmente solo se garantiza que quien inicia sesión tiene el secreto del registro, no su identidad real.

## Por qué fallan las contraseñas
Son fáciles de usar e implementar, pero el factor humano las debilita:
- Un 20 % de las cuentas usa el mismo conjunto de unas 5000 contraseñas populares.
- Los requisitos de caracteres ayudan poco ("1Password!" es común): lo que importa es la **entropía** (una contraseña con 16 bits requiere $2^{16}$ intentos).
- Se reutilizan entre sitios.
- Cambiarlas con frecuencia no tiene un efecto claro: invalida filtraciones viejas, pero lleva a elegir claves más débiles o anotarlas.

**Defensas:** usarlas lo menos posible (tras autenticar, usar cookies o claves criptográficas), un **gestor de contraseñas** (genera y guarda claves fuertes y distintas por sitio; hay que confiar en él y protegerlo con una clave fuerte) y la autenticación de dos factores.

## Limitar los intentos
Los atacantes conocen las distribuciones de contraseñas (por filtraciones). Hay que limitar la tasa de intentos (esperas tras fallos), pero por usuario no basta: se puede probar `123456` en todas las cuentas. Los CAPTCHA ayudan poco porque resolverlos es barato. Si los datos están cifrados con una contraseña, la adivinación es *offline* y sin servidor que limite.

## Cómo almacenar contraseñas

| Esquema | Se guarda | Problema o mejora |
|---|---|---|
| Ingenuo | `(usuario, contraseña)` | Un compromiso del servidor revela todas, incluso las usadas en otros sitios |
| Hash | `(usuario, H(contraseña))` | El hash es unidireccional, pero se precalculan *rainbow tables* de contraseñas comunes |
| **Salt** | `(usuario, salt, H(salt ‖ contraseña))` | Un salt aleatorio por usuario hace costosa la tabla precalculada |
| Hash costoso | Igual, con **KDF** (bcrypt, scrypt, PBKDF2) | Los hashes normales son rápidos; un KDF lento limita la tasa de adivinación |

> [!tip] Regla
> Nunca guardar la contraseña: guardar `salt` y un hash lento (KDF) de `salt ‖ contraseña`. Ver también [[02 - Cifrado asimétrico, hash y firmas digitales|hash y firmas]].

## Preguntas de repaso

> [!question]- ¿Por qué el salt no impide el ataque de fuerza bruta pero sí las rainbow tables?
> Porque el atacante aún puede probar contraseñas contra cada hash, pero no puede reutilizar una tabla precalculada: cada usuario tiene un salt distinto y habría que construir una tabla por salt.

> [!question]- ¿Por qué usar un hash "costoso" en vez de SHA-256 simple?
> Si se filtran los hashes, el atacante adivina offline sin límite de tasa; un KDF lento multiplica el costo de cada intento.

> [!question]- ¿Por qué limitar intentos por usuario no es suficiente?
> Porque el atacante puede probar una contraseña común en todas las cuentas, con pocos intentos por cuenta, sin activar el límite.
