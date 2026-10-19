---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Construir una API con Express"
tags:
  - web
  - sequelize
  - orm
  - migraciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Rutas y routers en Express]]"
  - "[[03 - Configurar Sequelize y PostgreSQL]]"
---

# Modelos, migraciones y seeds con Sequelize

Con Sequelize conectado, falta crear el primer **recurso**: la tabla, el modelo para usarla desde JavaScript, unos datos iniciales y las rutas que los exponen. La CLI de Sequelize automatiza casi todo con tres piezas: **modelos**, **migraciones** y **seeds**.

## El flujo completo

```bash
# 1. Modelo y migración
yarn sequelize-cli model:generate --name Movie \
  --attributes title:string,genre:string,description:string,rating:float
# 2. Crear la tabla
yarn sequelize-cli db:migrate
# 3. Archivo de seed
yarn sequelize-cli seed:generate --name first-movies
# 4. Escribir las seeds en src/seeders/… y cargarlas
yarn sequelize-cli db:seed:all
```

| Pieza | Qué es | Dónde queda |
|---|---|---|
| **Modelo** | Clase de JavaScript que representa la tabla (`Movie.findAll()`) | `src/models/movie.js` |
| **Migración** | Cambio versionado al esquema de la base (crear la tabla `Movies`) | `src/migrations/<fecha>-create-movie.js` |
| **Seed** | Datos iniciales para poblar las tablas | `src/seeders/<fecha>-first-movies.js` |

`model:generate` crea el modelo **y** su migración, y agrega solo las columnas `id`, `createdAt` y `updatedAt`. Las migraciones se aplican en orden y `db:migrate:status` muestra cuáles están aplicadas.

## Ajustar antes de migrar

Lo que genera la CLI es un punto de partida. Antes de `db:migrate` conviene revisar **la migración y el modelo**:

- los **tipos** (un texto largo es `TEXT`, no `STRING`);
- las restricciones, como `allowNull: false` en los campos obligatorios;
- las **relaciones** entre tablas: claves foráneas con `references` en la migración, y `belongsTo`/`hasMany` en el método `associate` del modelo.

> [!warning] Los arreglos no se generan bien
> La CLI no interpreta bien atributos de tipo arreglo en `--attributes`. Esos campos se agregan después, a mano, en la migración y en el modelo.

## Una seed

```javascript
'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Movies', [
      {
        title: 'Arrival',
        genre: 'Sci-fi/Thriller',
        description: 'A linguist must interpret the language of aliens who have come to Earth.',
        rating: 7.9,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    ], {});
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Movies', null, {});
  },
};
```

`up` aplica la seed y `down` la deshace. En las seeds hay que llenar `createdAt` y `updatedAt` a mano, porque `bulkInsert` no pasa por el modelo.

> [!warning] Las seeds no se registran
> A diferencia de las migraciones, Sequelize no guarda qué seeds ya corrieron: ejecutar `db:seed:all` dos veces inserta los datos dos veces. Para empezar de cero se usa `db:seed:undo:all`.

## Exponer el recurso

El router usa el modelo, que se importa desde `src/models` (su `index.js` carga todos los modelos):

```javascript
// src/routes/movies.js
const express = require('express');
const { Movie } = require('../models');

const router = express.Router();

router.get('/', async (req, res) => {
  try {
    const movies = await Movie.findAll();
    res.json(movies);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error al cargar las películas' });
  }
});

router.get('/:id', async (req, res) => {
  const movie = await Movie.findByPk(req.params.id);
  if (!movie) return res.status(404).json({ error: 'Película no encontrada' });
  res.json(movie);
});

router.post('/', async (req, res) => {
  try {
    res.status(201).json(await Movie.create(req.body));
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

module.exports = router;
```

Con esto quedan los pasos naturales para completar la API: el CRUD completo (`PUT`, `DELETE`), las credenciales en variables de entorno, un segundo recurso como `Users`, una tabla que relacione ambos (por ejemplo `Likes`) y el consumo desde un frontend en React.

Las migraciones y los ORMs en general están en [[04 - Migraciones de bases de datos|Migraciones de bases de datos]] y [[03 - ORMs|ORMs]].

## Preguntas de repaso

> [!question]- ¿Por qué el esquema se cambia con migraciones y no editando la tabla a mano?
> Porque una migración es un cambio versionado y reproducible: queda en el repositorio, se aplica en orden en cualquier máquina (otros desarrolladores, producción) y se puede revertir.

> [!question]- ¿Qué diferencia hay entre una migración y una seed?
> La migración cambia la **estructura** (crear tablas, columnas, relaciones). La seed inserta **datos** iniciales en esa estructura.

> [!question]- ¿Por qué el `GET /movies` captura errores y responde 500 en vez de 404?
> Porque si falla la consulta (la base caída, un error de SQL), el problema es del servidor y no de lo que pidió el cliente. El 404 se reserva para un recurso que no existe, como `GET /movies/99`.
