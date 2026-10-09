---
ramo: Ingeniería de Software
tema: Rails
tags: [ingsoft/rails, origen/apuntes]
prerrequisitos: ["[[01 - Protocolo HTTP|Protocolo HTTP]]"]
---
# CRUD

CRUD son las **cuatro operaciones básicas sobre datos persistentes**. Casi toda aplicación web, y todo recurso en Rails, se organiza alrededor de ellas.

## Mis apuntes
- **CRUD** → **C**reate, **R**ead, **U**pdate, **D**elete

> [!tip] Complemento — CRUD en HTTP, SQL y Rails
> | Operación | HTTP | SQL | Acción del controlador Rails | Active Record |
> |---|---|---|---|---|
> | **Create** | `POST` | `INSERT` | `new` (formulario) + `create` | `Model.new(...).save` / `Model.create(...)` |
> | **Read** | `GET` | `SELECT` | `index` (todos) / `show` (uno) | `Model.all`, `Model.find(id)`, `Model.where(...)` |
> | **Update** | `PATCH` / `PUT` | `UPDATE` | `edit` (formulario) + `update` | `obj.update(...)` |
> | **Delete** | `DELETE` | `DELETE` | `destroy` | `obj.destroy` |
>
> Estas 7 acciones son las que genera `resources` en las rutas (ver [[10 - Rutas en Rails|Rutas en Rails]]) y las que implementa un controlador típico (ver [[09 - Controladores en Rails|Controladores en Rails]]).

## Preguntas de repaso

1. ¿Qué significa CRUD?
> [!question]- Respuesta
> Create, Read, Update, Delete: crear, leer, actualizar y borrar datos.

2. ¿Qué método HTTP y qué acción de Rails corresponden a "Update"?
> [!question]- Respuesta
> `PATCH` (o `PUT`) y la acción `update`; el formulario de edición lo muestra la acción `edit`.

3. ¿Por qué Create y Update tienen dos acciones cada una en Rails?
> [!question]- Respuesta
> Porque una muestra el formulario (`new` / `edit`, con GET) y la otra procesa los datos enviados (`create` con POST / `update` con PATCH).
