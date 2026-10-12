---
ramo: Bases de Datos
tema: Diseño entidad-relación
tags: [bd/diseño, bd/er, bd/ddl, origen/complemento]
prerrequisitos: ["[[04 - Jerarquías, entidades débiles y agregación|Jerarquías, entidades débiles y agregación]]", "[[03 - Llaves foráneas|Llaves foráneas]]"]
---
# Del modelo E/R al relacional

El diseño lógico traduce cada construcción del diagrama E/R a tablas: las entidades a tablas con su llave, y las relaciones a tablas con llaves foráneas o a una llave foránea dentro de una entidad, según su multiplicidad.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 6: Diseño de Bases de Datos II")
> | Construcción E/R | Tablas |
> |---|---|
> | **Entidad** | una tabla con sus atributos; la llave → `PRIMARY KEY` |
> | **Relación n a n** | tabla propia: llaves de las entidades (FK) + atributos de la relación; llave = unión de las llaves |
> | **Relación n a 1** (flecha) | basta una FK en la entidad del lado "n" (más los atributos de la relación); la tabla aparte sería redundante |
> | **Relación 1 a 1** | FK en cualquiera de las dos tablas + `UNIQUE` |
> | **Entidad débil** | su tabla incluye la llave del dueño; llave = (llave del dueño, llave parcial); FK con `ON DELETE CASCADE` |
> | **Relación múltiple** | tabla con las llaves de todas las entidades (con roles: `rut_cliente`, `rut_cajero`) |
> | **Agregación** | la relación agregada es una tabla; la relación externa referencia su llave |

**Relación n a n** — `Producto —fabrica(desde)— Compañía`:

```sql
CREATE TABLE producto(nombre varchar(30), precio int, categoria varchar(30), PRIMARY KEY (nombre));
CREATE TABLE compania(nombre varchar(30), valor_accion int, PRIMARY KEY (nombre));
CREATE TABLE fabrica(
  p_nombre varchar(30),
  c_nombre varchar(30),
  desde date,
  PRIMARY KEY (p_nombre, c_nombre),
  FOREIGN KEY(p_nombre) REFERENCES producto(nombre),
  FOREIGN KEY(c_nombre) REFERENCES compania(nombre)
);
```

**Relación n a 1** (cada producto tiene a lo más una compañía): `Producto(nombre, precio, categoría, Compañía.nombre, desde)`. Solo hace falta una FK en Producto.

**Entidad débil** — `Evaluación de Curso`:

```sql
CREATE TABLE evaluacion(
  nombre varchar(30) NOT NULL,
  codigo varchar(30) NOT NULL,
  fecha date DEFAULT NOW(),
  PRIMARY KEY (nombre, codigo),
  FOREIGN KEY(codigo) REFERENCES curso(codigo) ON DELETE CASCADE
);
```

Una tabla `De(E.nombre, C.código)` sería **redundante** (la relación es 1 a algo).

> [!tip] Complemento — jerarquías de clases: tres opciones (slides "Clase 6")
> | Opción | Tablas | Ventaja | Desventaja |
> |---|---|---|---|
> | **Solo subclases** (sin herencia) | `Vino(nombre, origen, año)`, `Cerveza(nombre, origen)` | sin joins | no hay bebidas genéricas ni solapadas; repite datos si hay solapamiento |
> | **Tabla para la superclase** (tablas múltiples) | `Bebida(nombre, origen)`, `Vino(nombre, año)`, `Cerveza(nombre)` | permite genéricas y solapadas | joins para ver todos los datos |
> | **Una sola tabla** (quitar la jerarquía) | `Bebida(nombre, origen, año, tipo)` | sin joins, más sencillo (y comprimible) | muchos nulos y repeticiones de la columna `tipo` |
>
> ¿Cuál es mejor? Con mucho solapamiento o muchas consultas por nombre, la opción 2. Con la opción 1 habría que consultar dos tablas.

> [!tip] Complemento — relación múltiple y agregación (slides "Clase 6")
> - `Alquila(Pl.titulo, Pl.año, Pr.rut-cl, Pr.rut-ca, L.id, fecha)`: Persona aparece dos veces, como cliente y como cajero.
> - Agregación: `Tiene(P.código, L.código, precio_por_noche)` y `Alquila(T.p_código, T.l_código, Pr.rut, hasta)`, donde `Alquila` referencia la llave de `Tiene`.

> [!example] Ejemplo extra — en Rails
> La opción "una sola tabla" es la **Single Table Inheritance** de [[04 - Modelos y Active Record|Active Record]] (columna `type`), y la relación n a n con tabla intermedia es `has_many :through` en las [[08 - Asociaciones en Active Record|asociaciones]].

## Preguntas de repaso

1. ¿Cómo se traduce una relación n a n con atributos?
> [!question]- Respuesta
> A una tabla propia con las llaves de ambas entidades como llaves foráneas, más los atributos de la relación. Su llave primaria es la combinación de esas llaves.

2. ¿Por qué una relación n a 1 no necesita tabla propia?
> [!question]- Respuesta
> Porque cada entidad del lado "n" se relaciona con a lo más una del otro lado. Basta guardar en ella una llave foránea (y los atributos de la relación).

3. ¿Cuál es la llave de la tabla de una entidad débil y qué cláusula lleva su FK?
> [!question]- Respuesta
> La llave del dueño más la llave parcial, por ejemplo (nombre, código). La FK lleva `ON DELETE CASCADE`, porque la entidad débil no existe sin su dueño.

4. Nombra las tres formas de traducir una jerarquía y una desventaja de cada una.
> [!question]- Respuesta
> Solo subclases: no permite entidades genéricas ni solapadas. Tabla por superclase y subclases: requiere joins. Una sola tabla: muchos nulos y repetición de la columna tipo.
