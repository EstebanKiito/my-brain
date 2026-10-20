---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Gestión del curso"
tags:
  - web
  - gestion-del-curso
  - proyecto
  - origen/complemento
prerrequisitos:
  - "[[01 - Evaluación y organización de IIC2513]]"
---

# Tareas y proyecto del curso

La parte práctica de IIC2513 consiste en construir una aplicación web completa, primero por piezas en las tareas individuales y después entera en el proyecto grupal. Esta nota resume qué pide cada evaluación práctica y dónde está en el vault lo necesario para resolverla. Las soluciones propias no se incluyen.

## El stack

| Capa | Tecnología | Notas del vault |
|---|---|---|
| **Frontend** | React | [[01 - React, JSX y Virtual DOM\|React, JSX y Virtual DOM]] y el resto del tema React |
| **Backend** | Node.js con Express | [[01 - Estructura de un proyecto Node con Express\|Estructura de un proyecto Node con Express]] |
| **Base de datos** | PostgreSQL, con Sequelize como ORM | [[03 - Configurar Sequelize y PostgreSQL\|Configurar Sequelize y PostgreSQL]] |

En términos de MVC, React es la vista, Express el controlador y Sequelize el modelo.

## Las tareas

Son dos, individuales, y funcionan como laboratorios para practicar cada lado de la aplicación por separado:

- **T1: frontend con React.** Se construye la interfaz de una aplicación: componentes, props, estado, eventos y consumo de datos.
- **T2: backend con Express.** Se entrega un frontend ya hecho y hay que construir la API que lo alimenta: rutas, modelos, migraciones, seeds y la conexión con PostgreSQL.

> [!tip] Lo que más se repite al hacer la T2
> - Levantar Postgres y crear el usuario y la base. En macOS con Homebrew, conectarse con `psql postgres`, porque el superusuario es el usuario del sistema.
> - Generar los modelos con `sequelize-cli model:generate` y **revisar** migraciones y modelos antes de migrar: tipos, `allowNull: false` y relaciones.
> - Generar y cargar seeds (`seed:generate`, `db:seed:all`).
> - Organizar las rutas con un router índice.
> - Responder `200` con `[]` cuando una lista está vacía, no `404`.
>
> Todo el detalle está en el tema [[01 - Estructura de un proyecto Node con Express|Construir una API con Express]].

## El proyecto

- Equipos de **3 personas**.
- **4 entregas**: una preliminar (E0) y tres de desarrollo (E1 a E3), con pesos crecientes: la E3 vale el 40% del proyecto.
- Busca acercarse al desarrollo de una aplicación web real: frontend, backend y base de datos integrados, trabajo con Git en equipo, calidad del código y despliegue.

Para trabajar en equipo sirven las prácticas de [[03 - Code review, GitHub flow y commits|Code review, GitHub flow y commits]] y [[04 - Integración y despliegue continuos|Integración y despliegue continuos]] (Render para el backend, Netlify o Vercel para el frontend).

> [!warning] Tareas y proyecto no comparten código
> Las tareas son individuales y el proyecto es grupal: compartir código de una tarea con el grupo, o entre grupos, se considera copia. Si se reutiliza código externo, hay que citar la fuente; si se usó una IA, hay que declararlo en el README.

## Preguntas de repaso

> [!question]- ¿Qué parte de la aplicación construye cada tarea?
> La T1 construye el frontend en React. La T2 construye el backend en Express, con Sequelize y PostgreSQL, a partir de un frontend entregado.

> [!question]- ¿Qué entrega del proyecto pesa más y por qué tiene sentido?
> La E3, con el 40%, porque es la aplicación final integrada. Las entregas anteriores construyen hacia ella y pesan menos.

> [!question]- Al generar modelos con sequelize-cli, ¿qué conviene revisar antes de `db:migrate`?
> Los tipos de cada columna, las restricciones como `allowNull: false` y las relaciones entre tablas (claves foráneas y asociaciones), tanto en la migración como en el modelo.
