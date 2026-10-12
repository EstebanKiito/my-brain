---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[03 - Primera forma normal|Primera forma normal]]"]
---
# Segunda forma normal

Una tabla está en **2NF** si está en 1NF y ningún atributo no clave depende de **solo una parte** de una llave compuesta (no hay dependencias parciales).

## Segunda forma normal (2NF) (mis apuntes)
Una relación está en 2NF si está en 1NF y todos los atributos no clave son completamente dependientes de la clave primaria, es decir, no hay dependencias parciales.

Ejemplo de relación NO en 2NF:

| Fabricante | Modelo | País Fabricante |
|---|---|---|
| Forte | X-Prime | Italia |
| Forte | Ultraclean | Italia |
| Hoch | Toothmaster | Alemania |

Dependencia funcional parcial: Fabricante → País Fabricante

Descomposición para lograr 2NF:

Tabla 1:

| Fabricante | Modelo |
|---|---|
| Forte | X-Prime |
| Forte | Ultraclean |
| Hoch | Toothmaster |

Tabla 2:

| Fabricante | País Fabricante |
|---|---|
| Forte | Italia |
| Hoch | Alemania |

> [!tip] Complemento
> - La llave de la tabla original es **(Fabricante, Modelo)**. País Fabricante depende solo de **Fabricante**, una parte de la llave: eso es una dependencia **parcial**.
> - La redundancia se ve en que "Forte → Italia" aparece dos veces. Si Forte se muda, hay que actualizar varias filas (anomalía de actualización).
> - **Solo puede haber dependencias parciales con llaves compuestas.** Una tabla en 1NF cuya llave es un solo atributo (por ejemplo, un `id`) está automáticamente en 2NF.
> - La descomposición es **sin pérdida**: `Tabla1 ⋈ Tabla2` (por Fabricante) reconstruye la tabla original.

## Preguntas de repaso

1. ¿Qué es una dependencia parcial?
> [!question]- Respuesta
> Un atributo no clave que depende de solo una parte de una llave compuesta, como Fabricante → País Fabricante cuando la llave es (Fabricante, Modelo).

2. ¿Por qué una tabla con llave de un solo atributo siempre está en 2NF (si está en 1NF)?
> [!question]- Respuesta
> Porque una llave de un atributo no tiene "partes" propias de las que otro atributo pueda depender parcialmente.

3. ¿Cómo se lleva el ejemplo a 2NF?
> [!question]- Respuesta
> Separando la dependencia parcial en su propia tabla: `(Fabricante, Modelo)` y `(Fabricante, País Fabricante)`.
