---
ramo: Bases de Datos
tema: Lógica en la base de datos
tags: [bd/logica, bd/sql, origen/apuntes]
prerrequisitos: ["[[03 - Triggers|Triggers]]"]
---
# Trigger para descontar stock en PL/pgSQL

Ejemplo completo en PostgreSQL: una **función** en PL/pgSQL que descuenta el stock (y valida que no quede negativo) y un **trigger** que la llama después de cada venta.

## Ejemplo más completo (mis apuntes)
Supongamos que tenemos dos tablas: Productos y Ventas.
- **Productos:** Almacena información sobre los productos y su stock disponible.
- **Ventas:** Almacena información sobre las ventas realizadas.

### Estructura de las tablas
Tabla Productos

```sql
CREATE TABLE Productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);
```

Tabla Ventas

```sql
CREATE TABLE Ventas (
    id_venta SERIAL PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);
```

### Crear el trigger
Queremos que cada vez que se inserte una nueva venta en la tabla Ventas, se reduzca automáticamente el stock del producto correspondiente en la tabla Productos.

```sql
CREATE OR REPLACE FUNCTION reducir_stock() RETURNS TRIGGER AS $$
BEGIN
    UPDATE Productos
    SET stock = stock - NEW.cantidad
    WHERE id_producto = NEW.id_producto;
    
    -- Validacion de stock > 0:
    IF (SELECT stock FROM Productos WHERE id_producto=NEW.id_producto) < 0 THEN
        RAISE EXCEPTION 'Stock insuficiente %', NEW.id_producto;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Explicación de la función
- `UPDATE Productos SET stock = stock - NEW.cantidad`: Actualiza el stock del producto restando la cantidad vendida.
- `WHERE id_producto = NEW.id_producto`: Especifica el producto a actualizar, utilizando NEW.id_producto que es el valor del producto en la nueva fila de Ventas.
- `RETURN NEW`: Devuelve la nueva fila insertada en la tabla Ventas.

### Paso 2: Crear el trigger que llama a la función
Ahora creamos el trigger que se ejecutará después de cada inserción en la tabla Ventas.

```sql
CREATE TRIGGER reducir_stock_trigger
AFTER INSERT ON Ventas
FOR EACH ROW
EXECUTE FUNCTION reducir_stock();
```

### Ejemplo de uso
1. Insertar Productos

```sql
INSERT INTO Productos (nombre, precio, stock) VALUES ('Producto A', 100.00, 50);
INSERT INTO Productos (nombre, precio, stock) VALUES ('Producto B', 200.00, 30);
```

2. Insertar una Venta y Activar el Trigger

```sql
INSERT INTO Ventas (id_producto, cantidad, fecha) VALUES (1, 5, '2024-05-28');
```

Después de insertar esta venta, el stock del Producto A se reducirá automáticamente de 50 a 45.

> [!tip] Complemento — qué pasa si no alcanza el stock
> ```mermaid
> sequenceDiagram
>   participant App
>   participant Ventas
>   participant F as reducir_stock()
>   participant Productos
>   App->>Ventas: INSERT (1, 60, …)
>   Ventas->>F: AFTER INSERT, NEW = fila nueva
>   F->>Productos: stock = 45 - 60 = -15
>   F-->>App: RAISE EXCEPTION 'Stock insuficiente 1'
>   Note over App,Productos: toda la sentencia se deshace: ni la venta ni el UPDATE quedan
> ```
> - `RAISE EXCEPTION` aborta la sentencia completa. Como el `INSERT` y el `UPDATE` del trigger son parte de la misma transacción, se deshacen juntos (atomicidad, ver «Propiedades ACID»).
> - El `%` del mensaje se reemplaza por `NEW.id_producto`.
> - En un trigger `AFTER … FOR EACH ROW` el valor devuelto se ignora; `RETURN NEW` es una convención. En un trigger `BEFORE`, devolver `NEW` deja seguir la operación.
> - Alternativa sin trigger: `CHECK (stock >= 0)` en `Productos` haría fallar el `UPDATE` por sí solo.

## Preguntas de repaso

1. ¿Por qué en PostgreSQL hay que crear una función además del trigger?
> [!question]- Respuesta
> Porque en PostgreSQL el trigger no contiene el código: solo indica cuándo ejecutar una función que devuelve `TRIGGER` (`EXECUTE FUNCTION reducir_stock()`).

2. ¿Qué es `NEW` dentro de `reducir_stock()`?
> [!question]- Respuesta
> La fila recién insertada en Ventas. De ella se usan `NEW.cantidad` y `NEW.id_producto`.

3. Si el Producto A tiene stock 45 y se inserta una venta de 60 unidades, ¿qué pasa?
> [!question]- Respuesta
> El stock quedaría en -15, así que la función lanza `RAISE EXCEPTION 'Stock insuficiente 1'`. Se aborta la sentencia, y ni la venta ni el descuento quedan guardados.

4. ¿Cuál es el stock del Producto A después del `INSERT` de 5 unidades del ejemplo?
> [!question]- Respuesta
> 45 (50 − 5).
