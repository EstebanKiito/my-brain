---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Autenticación y autorización"
tags:
  - web
  - seguridad
  - hashing
  - bcrypt
  - origen/complemento
prerrequisitos:
  - "[[01 - Autenticación, autorización y contraseñas]]"
---

# Hashing de contraseñas con bcrypt

Una base de datos puede filtrarse. Si guarda las contraseñas tal cual, el atacante obtiene las credenciales de todos los usuarios, y como la gente reutiliza contraseñas, también sus cuentas en otros sitios. Por eso las contraseñas nunca se guardan: se guarda un **hash**, y para eso hay funciones diseñadas específicamente, como **bcrypt**.

## Encriptación frente a hashing

Ambas protegen información, pero de formas distintas:

| | **Encriptación** | **Hashing** |
|---|---|---|
| ¿Se puede revertir? | Sí, con la clave correcta | No (es *one-way*) |
| Objetivo | Que un receptor autorizado lea los datos | Probar la autenticidad o integridad de un dato |
| Cuándo se usa | Para **enviar** información | Para **almacenar** información que solo hay que comparar |
| Ejemplo | HTTPS | Contraseñas, identificadores de commits de Git (SHA-1) |

Una **función de hash** transforma cualquier string en otro string de largo fijo y aparentemente aleatorio, y no hay proceso inverso. Para verificar una contraseña en el login no hace falta recuperarla: se calcula el hash de lo que escribió el usuario y se compara con el hash guardado.

## El problema: la misma contraseña da el mismo hash

![Mismo hash para la misma contraseña sin salt](adjuntos/Mismo%20hash%20para%20la%20misma%20contrase%C3%B1a%20sin%20salt.png)

> [!example]- Transcripción de la imagen
> Dos usuarios con la misma contraseña, `strawberry`, pasan por la misma función de hash (SHA-256) y obtienen exactamente el mismo resultado, `5e737f891db1175442a39fd…`. Flechas con la palabra *same* unen la contraseña, la función y el hash de ambos lados.

Esto tiene dos consecuencias:

- Si dos usuarios comparten contraseña, se nota en la base de datos.
- Un atacante puede usar **rainbow tables**: tablas precalculadas con el hash de millones de contraseñas comunes, y buscar ahí cada hash filtrado.

La solución es el **salt**: un valor aleatorio distinto para cada usuario, que se combina con la contraseña antes de calcular el hash. Así la misma contraseña produce hashes distintos, y las tablas precalculadas dejan de servir.

## bcrypt

**bcrypt** es una función de hash para contraseñas creada en 1999 por Niels Provos y David Mazières. Sus medidas de seguridad:

- **Salt incorporado**, que protege contra las rainbow tables.
- **Factor de costo**, que fija la cantidad de rondas de hashing: con costo $c$ se hacen $2^c$ rondas.
- **Lentitud intencional**, para encarecer los ataques de fuerza bruta.
- **Adaptabilidad en el tiempo**: el costo se puede subir a medida que el hardware mejora.

El hash resultante guarda todo lo necesario para verificarlo:

```text
$2a$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUW
\__/\/ \____________________/\_____________________________/
Alg Cost       Salt                      Hash
```

- `$2a$`: el identificador del algoritmo (bcrypt).
- `12`: el costo, es decir, $2^{12} = 4096$ rondas.
- `R9h/cIPz0gi.URNNX3kh2O`: el salt aleatorio (16 bytes) en base 64.
- `PST9/PgBkqquzi.Ss7KIUgO2t0jWMUW`: los primeros 23 bytes del hash de 24 bytes, en base 64.

La entrada es la contraseña (hasta 72 bytes), el costo y el salt. Este ejemplo corresponde a la contraseña `abc123xyz`.

```javascript
const bcrypt = require('bcrypt');

const hash = await bcrypt.hash('abc123xyz', 12);   // genera un salt nuevo cada vez
// '$2b$12$…'  (60 caracteres, distinto en cada llamada)

await bcrypt.compare('abc123xyz', hash);   // true
await bcrypt.compare('abc123xy', hash);    // false
```

> [!tip] La lentitud es la defensa
> Calcular un hash de bcrypt toma del orden de cientos de milisegundos. Para un login es imperceptible, pero para un atacante que quiere probar miles de millones de contraseñas es un costo enorme. Un hash rápido como SHA-256 es mala elección para contraseñas justamente por ser rápido.

> [!warning] Nunca inventar el propio esquema
> Ni encriptar las contraseñas (si se roba la clave, se recuperan todas), ni usar un hash rápido sin salt. Hay que usar una función diseñada para contraseñas, como bcrypt, scrypt o Argon2, mediante una librería probada.

## Preguntas de repaso

> [!question]- ¿Por qué las contraseñas se hashean y no se encriptan?
> Porque el servidor nunca necesita recuperar la contraseña original, solo verificarla. Encriptarla implica guardar una clave que, si se roba, permite descifrar todas las contraseñas; un hash no se puede revertir.

> [!question]- ¿Qué problema resuelve el salt?
> Que la misma contraseña produzca el mismo hash. Con un salt aleatorio por usuario, los hashes son distintos, no se ve quién comparte contraseña y las rainbow tables no sirven.

> [!question]- ¿Qué significa el `12` en un hash `$2a$12$…` y por qué se puede aumentar con los años?
> Es el factor de costo: $2^{12}$ rondas de hashing. Como el hardware se vuelve más rápido, subir el costo mantiene el tiempo de cálculo alto para un atacante.
