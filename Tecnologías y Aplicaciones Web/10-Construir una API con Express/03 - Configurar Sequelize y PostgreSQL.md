---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Construir una API con Express"
tags:
  - web
  - sequelize
  - postgresql
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructura de un proyecto Node con Express]]"
  - "[[04 - Middleware y acceso a datos en el servidor]]"
---

# Configurar Sequelize y PostgreSQL

Para que Express guarde datos hacen falta tres cosas: un motor de base de datos corriendo (PostgreSQL), un usuario y una base para la aplicación, y Sequelize configurado para conectarse a ellos. Esta nota recorre esa configuración, incluida la diferencia que aparece al instalar Postgres con Homebrew en macOS.

## Instalar Sequelize

1. Agregar Sequelize y el driver de Postgres: `yarn add sequelize pg pg-hstore`.
2. Agregar la CLI como dependencia de desarrollo: `yarn add sequelize-cli --dev`.
3. Crear las carpetas base: `yarn sequelize-cli init`, que genera `config`, `migrations`, `models` y `seeders`.
4. Mover esas carpetas dentro de `src/`.
5. Crear un archivo `.sequelizerc` en la raíz para indicarle a la CLI su nueva ubicación:

```javascript
// .sequelizerc
const path = require('path');

module.exports = {
  config: path.resolve('src', 'config', 'config.json'),
  'models-path': path.resolve('src', 'models'),
  'seeders-path': path.resolve('src', 'seeders'),
  'migrations-path': path.resolve('src', 'migrations'),
};
```

## Preparar PostgreSQL

En Linux, Postgres corre como servicio y se administra con el usuario `postgres` del sistema:

```bash
sudo service postgresql start     # iniciar el servicio
sudo -i -u postgres               # entrar como el usuario postgres
createdb demo_dev                 # crear la base (lo opuesto: dropdb)
createuser demo_user              # crear el usuario (lo opuesto: dropuser)
psql                              # abrir la consola de Postgres
```

Dentro de `psql`, se le da contraseña y permisos al usuario:

```sql
ALTER USER demo_user WITH ENCRYPTED PASSWORD 'pwd';
GRANT ALL PRIVILEGES ON DATABASE demo_dev TO demo_user;
ALTER USER demo_user CREATEDB;    -- para que la CLI pueda crear bases
```

Luego `exit` cierra `psql` y otro `exit` sale del usuario `postgres`.

> [!warning] En macOS con Homebrew no hay usuario `postgres`
> Con Homebrew, el servicio se inicia con `brew services start postgresql` y el **superusuario es el propio usuario de macOS**. Por eso `psql` a secas falla con `database "<tu-usuario>" does not exist`: intenta conectarse a una base con el nombre del usuario, que no existe. La solución es conectarse a la base por defecto con `psql postgres`, y desde ahí crear el usuario y la base de la aplicación. Conviene dejarlo anotado en el README del proyecto.

## Conectar Sequelize

Las credenciales van en `src/config/config.json`, con una entrada por ambiente:

```json
{
  "development": {
    "username": "demo_user",
    "password": "pwd",
    "database": "demo_dev",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

Si la base aún no existe, la CLI la crea con `yarn sequelize-cli db:create` (da error si ya existe).

> [!tip] Credenciales fuera del código
> Una contraseña en `config.json` termina en el repositorio. Lo correcto es leerla de **variables de entorno** (con `dotenv` o `dotenvx` y un archivo `.env` que va en `.gitignore`), usando un `config.js` en vez de `config.json`.

## Limpiar al terminar

```bash
sudo -i -u postgres
dropdb demo_dev                   # eliminar la base
dropuser demo_user                # eliminar el usuario
exit
sudo service postgresql stop      # detener el servicio
```

Los conceptos de PostgreSQL, usuarios y permisos se ven en Bases de Datos: [[01 - SQL y PostgreSQL|SQL y PostgreSQL]].

## Preguntas de repaso

> [!question]- ¿Para qué sirve `.sequelizerc`?
> Para decirle a la CLI de Sequelize dónde están la configuración, los modelos, las migraciones y las seeds cuando no están en las carpetas por defecto, por ejemplo al moverlas dentro de `src/`.

> [!question]- ¿Por qué `psql` falla en un Mac recién instalado con Homebrew y cómo se resuelve?
> Porque intenta conectarse a una base con el nombre del usuario de macOS, que no existe. Se resuelve conectándose a la base por defecto con `psql postgres`.

> [!question]- ¿Por qué el usuario de la aplicación necesita `CREATEDB`?
> Porque comandos como `sequelize-cli db:create` crean la base con las credenciales de `config.json`. Sin ese permiso, el usuario solo puede trabajar sobre bases que ya existen.
