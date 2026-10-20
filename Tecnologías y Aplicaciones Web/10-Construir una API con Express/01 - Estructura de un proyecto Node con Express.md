---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Construir una API con Express"
tags:
  - web
  - express
  - nodejs
  - npm
  - origen/complemento
prerrequisitos:
  - "[[04 - Middleware y acceso a datos en el servidor]]"
  - "[[05 - Un proyecto React con npm y Vite]]"
---

# Estructura de un proyecto Node con Express

Antes de escribir rutas o modelos hay que armar el proyecto: declarar las dependencias, instalar Express y dejar un servidor mínimo que se reinicie solo al guardar. Esta nota cubre ese punto de partida, que después crece con routers y Sequelize.

## `package.json` y `node_modules`

`package.json` es el archivo de configuración de npm, en la raíz del proyecto. Contiene la metadata del proyecto y cumple tres funciones:

- lista las **dependencias**;
- fija sus **versiones**;
- hace que la instalación y la ejecución sean **reproducibles** en cualquier máquina.

Debe tener al menos **nombre y versión** (son obligatorios). Además suele incluir autor, descripción, **scripts**, palabras clave, licencia y las URLs de bugs y de la página del proyecto.

Todo paquete instalado queda en la carpeta `node_modules`, con su contenido y sus propias dependencias. Esa carpeta se regenera con `npm install` o `yarn`, así que no se versiona: va en `.gitignore`.

Hay varias formas de iniciar un proyecto:

| Herramienta | Comando |
|---|---|
| npm | `npm init` (con `-y` acepta todos los valores por defecto) |
| yarn | `yarn init` (`-y`) |
| Vite (para frontend) | `npm create vite@latest` o `yarn create vite@latest` |

## El "Hello world" de Express

1. Crear el proyecto: `yarn init`.
2. Agregar Express: `yarn add express`.
3. Crear `src/app.js` con el código base.
4. Agregar nodemon como dependencia de desarrollo: `yarn add nodemon --dev`.
5. Agregar un script en `package.json`: `"dev": "nodemon src/app.js"`.
6. Levantar el servidor con `yarn dev` y abrir `localhost:3000`.

```javascript
// src/app.js
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello world!');
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
```

**nodemon** es una herramienta que vigila los archivos del servidor y lo **reinicia automáticamente** cuando cambian. Así no hay que detener y volver a levantar el proceso después de cada edición. Por eso va como dependencia de desarrollo: en producción no se usa.

```json
{
  "name": "primera-api",
  "version": "1.0.0",
  "scripts": {
    "dev": "nodemon src/app.js",
    "start": "node src/app.js"
  },
  "dependencies": { "express": "^5.0.0" },
  "devDependencies": { "nodemon": "^3.0.0" }
}
```

> [!tip] Leer el puerto desde el entorno
> `process.env.PORT || 3000` usa el puerto que entregue el entorno y, si no hay ninguno, el 3000. Así el mismo código corre en un servicio de hosting (que asigna el puerto) y en local. También evita chocar con otro proceso que ya ocupe el 3000: basta con `PORT=3005 yarn dev`.

## Hacia dónde crece la estructura

```text
primera-api/
├── package.json
├── .sequelizerc            ← dónde están los archivos de Sequelize
└── src/
    ├── app.js              ← crea la app y monta los routers
    ├── routes/             ← un router por recurso (movies.js, users.js…)
    ├── config/config.json  ← credenciales de la base de datos
    ├── models/             ← modelos de Sequelize
    ├── migrations/         ← cambios al esquema de la base
    └── seeders/            ← datos iniciales
```

> [!warning] Sin `express.json()` no hay body
> Por defecto Express no interpreta el cuerpo de las requests: `req.body` queda `undefined`. Para recibir JSON en un `POST` o `PUT` hay que registrar el middleware `app.use(express.json())`.

## Preguntas de repaso

> [!question]- ¿Por qué `node_modules` no se sube al repositorio pero `package.json` sí?
> `package.json` (junto con el archivo de bloqueo de versiones) basta para reconstruir `node_modules` con `npm install`. La carpeta es pesada y depende del sistema, así que versionarla solo agrega ruido.

> [!question]- ¿Qué aporta nodemon durante el desarrollo?
> Reinicia el servidor automáticamente cada vez que cambia un archivo, para que los cambios se vean sin detener y relanzar el proceso a mano.

> [!question]- ¿Qué diferencia hay entre `dependencies` y `devDependencies` en este proyecto?
> Express es necesario para que el servidor funcione, así que va en `dependencies`. Nodemon y la CLI de Sequelize solo se usan al desarrollar, así que van en `devDependencies`.
