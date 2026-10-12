---
ramo: Bases de Datos
tema: Gestión del curso
tags: [bd/curso, bd/proyecto, origen/apuntes]
prerrequisitos: ["[[01 - SQL desde Python con cursores|SQL desde Python con cursores]]"]
---
# Proyecto de Bases de Datos

Notas del proyecto semestral: una aplicación web en Flask conectada a PostgreSQL (grupo 73), con un esquema de restaurantes, platos y clientes.

## Comandos de terminal (mis apuntes)
```bash
python3.11 -m flask --app app run
```

(en el server):

```bash
python3.11 -m flask --app app run --port=8073 --host=0.0.0.0
```

- puerto = 8073 → Grupo 73
- host = 0.0.0.0 → Cualquier ip que este disponible

```bash
flask --app app run
```

http://127.0.0.1:5000/select

Ruta para query select

> [!tip] Complemento
> - `--port=8073`: cada grupo tenía su puerto en el servidor del curso (grupo 73 → 8073). `--host=0.0.0.0` hace que Flask escuche en todas las interfaces de red, no solo en `localhost`, para poder abrirlo desde fuera del servidor.
> - En local Flask usa el puerto 5000 por defecto: http://127.0.0.1:5000/select es la ruta `/select` de la app, que ejecutaba las consultas.
> - La conexión a la base de datos desde Python se ve en [[01 - SQL desde Python con cursores|SQL desde Python con cursores]]; si la consulta lleva parámetros del usuario, hay que parametrizarla ([[02 - SQL injection y consultas parametrizadas|SQL injection]]).

## Consideraciones informe entrega 2
1. Cambiamos el largo de Email en Subs Clientes y Direcciones a 100 varchar
2. Cambiamos el largo de las direcciones a 100 varchar
3. Cambiemos el largo de telefonos.

Para acordarme después:
1. Al hacer cdeldes sobrescribir clientes

> [!note] Omitido a propósito
> Dos recordatorios de esta lista tenían datos personales (un número de teléfono y nombres de compañeros) y no se migraron (ver `aceptados` en `_meta/Bases de Datos/mapeo.json`).

## Querys

**1**

```sql
SELECT restaurantes.nombre 
FROM restaurantes JOIN platos 
ON platos.nombre_restaurante = restaurantes.nombre
WHERE platos.nombre = 'Pizza Margarita'
AND platos.disponibilidad = TRUE
AND restaurantes.vigente = TRUE;

-- Consideramos que se deben mostrar solo aquellos restuarantes que esten vigentes
```

**8**

```sql
SELECT platos.nombre, plato.nombre_restaurant
FROM platos
```

**2**

Input: email y gasto mensual

> [!warning] Posible error / inconcluso (registrado en `_meta/Bases de Datos/DUDAS.md`)
> - **Query 8:** usa `plato.` (sin s) y `nombre_restaurant`, pero la tabla es `platos` y en la query 1 la columna es `nombre_restaurante`. Además quedó sin `WHERE`. Versión consistente: `SELECT platos.nombre, platos.nombre_restaurante FROM platos;`
> - **Query 2:** solo está el enunciado ("Input: email y gasto mensual"); falta el SQL.
> - **"Al hacer cdeldes sobrescribir clientes":** no se entiende "cdeldes" (¿"deletes"?, ¿"CSV"?).

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
