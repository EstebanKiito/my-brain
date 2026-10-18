---
ramo: Bases de Datos
tema: Gestión del curso
tags: [bd/curso, bd/proyecto, origen/apuntes]
prerrequisitos: ["[[01 - SQL desde Python con cursores|SQL desde Python con cursores]]"]
---
# Proyecto de Bases de Datos

Notas del proyecto semestral: una aplicación web en Flask conectada a PostgreSQL (grupo 73), con un esquema de restaurantes, platos y clientes.

## Comandos de terminal
```bash
python3.11 -m flask --app app run
```

En el servidor:

```bash
python3.11 -m flask --app app run --port=8073 --host=0.0.0.0
```

- `--port=8073`: cada grupo usa su puerto (8073 → grupo 73).
- `--host=0.0.0.0`: escucha en todas las IP disponibles, para que se pueda acceder desde fuera del servidor.

```bash
flask --app app run
```

La ruta `http://127.0.0.1:5000/select` ejecuta las consultas SELECT.

## Consideraciones informe entrega 2
1. Se cambió el largo del email en Subs, Clientes y Direcciones a `varchar(100)`.
2. Se cambió el largo de las direcciones a `varchar(100)`.
3. Se cambió el largo de los teléfonos.

> [!note] Omitido a propósito
> Dos recordatorios de esta lista tenían datos personales (un número de teléfono y nombres de compañeros) y no se migraron (ver `aceptados` en `_meta/Bases de Datos/mapeo.json`).

## Consultas

**1**

```sql
SELECT restaurantes.nombre 
FROM restaurantes JOIN platos 
ON platos.nombre_restaurante = restaurantes.nombre
WHERE platos.nombre = 'Pizza Margarita'
AND platos.disponibilidad = TRUE
AND restaurantes.vigente = TRUE;

-- Se muestran solo los restaurantes vigentes
```

**8**

```sql
SELECT platos.nombre, platos.nombre_restaurante
FROM platos;
```

## Preguntas de repaso

1. ¿Qué hace `--host=0.0.0.0` al levantar Flask en el servidor?
> [!question]- Respuesta
> Hace que la aplicación escuche en todas las interfaces de red (cualquier IP disponible), no solo en localhost, para que se pueda acceder desde fuera.

2. Explica la query 1 del proyecto.
> [!question]- Respuesta
> Une restaurantes con platos por el nombre del restaurante y devuelve los restaurantes vigentes que tienen disponible la "Pizza Margarita".

3. ¿Por qué el grupo 73 usaba el puerto 8073?
> [!question]- Respuesta
> Porque cada grupo tenía un puerto propio en el servidor compartido del curso, formado a partir de su número de grupo.
