---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[03 - Superllaves, claves candidatas y clave primaria|Superllaves, claves candidatas y clave primaria]]", "[[06 - Principios de diseño de bases de datos|Principios de diseño de bases de datos]]"]
---
# Dependencias funcionales

Una dependencia funcional X → Y dice que los valores de X **determinan** los de Y. Es la herramienta para detectar redundancia y anomalías, y la base de las formas normales.

## Dependencias funcionales
Una dependencia funcional en una relación R es una restricción entre dos conjuntos de atributos. Si X e Y son conjuntos de atributos de R, **X determina Y** (se escribe X → Y) si para todo par de tuplas $t_1$ y $t_2$ de R se cumple: si $t_1[X] = t_2[X]$, entonces $t_1[Y] = t_2[Y]$.

### Ejemplo
Se considera la tabla `Guías`:

| gid | nombre | score | horas | valorHora |
|---|---|---|---|---|
| 1 | Juan | 8 | 40 | 18000 |
| 2 | Johanna | 8 | 30 | 18000 |
| 3 | Cristian | 5 | 30 | 15000 |
| 4 | Pedro | 8 | 32 | 18000 |

Dependencia funcional: **score → valorHora**. El valor de `valorHora` está determinado por `score`: todas las filas con score 8 tienen valorHora 18000.

> [!tip] Complemento — por qué importan: redundancia y anomalías (slides "Clase 7: Dependencias y Formas Normales")
> En `Guías(gid, nombre, score, horas, valorHora)` el pago por hora depende del score, y eso causa:
> | Problema | En Guías |
> |---|---|
> | **Gasto de espacio** | guardamos 18000 muchas veces |
> | **Anomalía de inserción** | si llega Pablo con score 9 y no sabemos el valorHora del 9, no podemos insertarlo |
> | **Anomalía de actualización** | si cambia el valor del score 8, hay que cambiarlo en **todas** las tuplas; si se olvida una, los datos quedan inconsistentes |
> | **Anomalía de eliminación** | si elimino a Cristian, pierdo que el score 5 paga 15000 |
>
> **Solución:** descomponer en `Guías(gid, nombre, score, horas)` y `Valor(score, valorHora)`. Lo que pasó es que **score determina valorHora**: eso es una dependencia funcional.

> [!tip] Complemento — más ejemplos (slides "Clase 7")
> - `Personas(rut, nombre)`: rut → nombre.
> - `Películas(pid, título, año, director)`: título, año → director.
> - `Programación(cine, película, director, dirección, teléfono, horario, precio)`: cine → teléfono, dirección; película → director; cine, película, horario → precio.
> - **El lado izquierdo no es necesariamente una llave** (score no lo es en Guías).
> - **Dependencia buena vs mala:** en `ES(Empleado, Salario)`, Empleado → Salario es buena porque Empleado es llave. En `DJE(Depto, Jefe, Empleado)`, Depto → Jefe es mala: Depto no es llave, así que el hecho "Pérez es jefe de D1" se repite. Si Vargas renuncia y se borra su fila, se pierde que Correa es jefe de D2.
>
> **Objetivo de la normalización:** eliminar anomalías minimizando la redundancia. Para eso hay que (1) averiguar las dependencias que aplican y (2) descomponer las tablas en tablas más pequeñas.

## Preguntas de repaso

1. Define formalmente X → Y.
> [!question]- Respuesta
> Para todo par de tuplas t1, t2 de R: si t1[X] = t2[X], entonces t1[Y] = t2[Y].

2. ¿Qué anomalías causa score → valorHora en la tabla Guías?
> [!question]- Respuesta
> De inserción (no se puede agregar un guía si no se conoce el valor de su score), de actualización (cambiar el valor del score 8 obliga a cambiar varias tuplas) y de eliminación (borrar el único guía con score 5 pierde su valor hora).

3. ¿El lado izquierdo de una dependencia tiene que ser una llave?
> [!question]- Respuesta
> No. score → valorHora es válida aunque score no sea llave, y justamente ese tipo de dependencia causa redundancia.

4. ¿Cómo se elimina la redundancia de Guías?
> [!question]- Respuesta
> Descomponiendo en `Guías(gid, nombre, score, horas)` y `Valor(score, valorHora)`.
