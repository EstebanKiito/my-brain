---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, origen/apuntes]
prerrequisitos: ["[[01 - Proceso de desarrollo de software|Proceso de desarrollo de software]]", "[[03 - Procesos iterativos|Procesos iterativos]]"]
---
# Procesos incrementales

En un proceso incremental el sistema se construye **por piezas terminadas**: cada entrega agrega una parte nueva, pero el sistema no está completo hasta la última pieza.

## Características
- Con cada entrega tenemos acabada **una pieza más del sistema** (nuevas funcionalidades), pero **no está acabado hasta entregar la última pieza**.
- ¡**No feedback hasta terminar**!

> [!warning] Posible error / matiz
> Que no haya feedback es discutible. Cada pieza terminada *puede* mostrarse al usuario. Lo que realmente caracteriza al incremental "puro" es que **las piezas se planifican de antemano y no se vuelven a trabajar** con lo que se aprende: no hay iteración sobre lo ya construido. Registrado en `_meta/DUDAS.md`.

![Procesos incrementales - analogía de la Mona Lisa](adjuntos/Procesos%20incrementales%20-%20analogía%20de%20la%20Mona%20Lisa.png)

> [!note]- Qué muestra la imagen
> La persona ya tiene la imagen exacta del cuadro en la cabeza y lo pinta **por partes terminadas**: primero la cara completa (1), luego el cuerpo (2) y finalmente el cuadro entero (3). Cada parte queda lista y no se vuelve a tocar, pero el cuadro solo está completo al final.

> [!tip] Complemento — cuándo usarlo y comparación
> - **Supone requisitos claros desde el inicio:** como en la imagen, hay que saber exactamente qué cuadro se quiere pintar.
> - **Ventaja:** entrega partes funcionales antes que la [[02 - Modelo en cascada|cascada]] y reparte el trabajo en entregas manejables.
> - **Riesgo:** si el usuario cambia de opinión, las piezas ya hechas no estaban pensadas para cambiar.
> - La combinación con iteración da los [[08 - Procesos iterativos e incrementales|Procesos iterativos e incrementales]], la base de los procesos ágiles.
>
> | | [[03 - Procesos iterativos\|Iterativo]] | Incremental | Iterativo e incremental |
> |---|---|---|---|
> | Cada entrega | Mejora el todo | Agrega una pieza | Agrega piezas **y** mejora las existentes |
> | Usable antes del final | No necesariamente | Por partes | Sí, desde temprano |

## Preguntas de repaso

1. ¿Qué caracteriza a un proceso incremental?
> [!question]- Respuesta
> Cada entrega agrega una pieza nueva y terminada del sistema (nuevas funcionalidades), pero el sistema no está completo hasta entregar la última.

2. En la analogía de la Mona Lisa, ¿qué diferencia hay entre el enfoque incremental y el iterativo?
> [!question]- Respuesta
> En el incremental se pinta por partes terminadas (cara, cuerpo, resto) a partir de una idea ya exacta. En el iterativo se pinta el cuadro completo desde el inicio y se va refinando (boceto → color → detalle).

3. ¿Qué supuesto fuerte hace el enfoque incremental "puro"?
> [!question]- Respuesta
> Que los requisitos (la imagen final) se conocen desde el inicio, porque las piezas se planifican de antemano y no se rehacen.
