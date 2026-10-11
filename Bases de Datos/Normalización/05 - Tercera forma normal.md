---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[04 - Segunda forma normal|Segunda forma normal]]"]
---
# Tercera forma normal

Una tabla está en **3NF** si está en 2NF y ningún atributo no clave depende de la llave **a través de otro atributo no clave** (no hay dependencias transitivas).

## Tercera forma normal (3NF) (mis apuntes)
Una relación está en 3NF si está en 2NF y ningún atributo no clave es transitivamente dependiente de la clave primaria.

Ejemplo de relación NO en 3NF:

| Fabricante | Modelo | País Fabricante | Continente |
|---|---|---|---|
| Forte | X-Prime | Italia | Europa |
| Hoch | Toothmaster | Alemania | Europa |

Dependencia transitiva: País Fabricante → Continente

Descomposición para lograr 3NF:

Tabla 1:

| Fabricante | Modelo | País Fabricante |
|---|---|---|
| Forte | X-Prime | Italia |
| Hoch | Toothmaster | Alemania |

Tabla 2:

| País Fabricante | Continente |
|---|---|
| Italia | Europa |
| Alemania | Europa |

> [!warning] Posible error (registrado en `_meta/Bases de Datos/DUDAS.md`)
> El ejemplo parte de la tabla de [[04 - Segunda forma normal|2NF]] con llave (Fabricante, Modelo), donde Fabricante → País Fabricante es **parcial**. Entonces la tabla original (y también la "Tabla 1" resultante) **no está ni siquiera en 2NF**, y la 3NF exige estar en 2NF.
>
> Para que el ejemplo sea solo de 3NF, la llave debería ser un solo atributo. Por ejemplo, `Modelo(modelo, fabricante, país, continente)` con llave `modelo` y la cadena modelo → fabricante → país → continente. La descomposición completa sería `(Fabricante, Modelo)`, `(Fabricante, País)` y `(País, Continente)`.

> [!tip] Complemento — definición de la clase (slides "Clase 7")
> Una relación R está en 3NF si para toda dependencia funcional **no trivial** X → Y:
> - **X es una superllave**, o
> - **Y es parte de una llave minimal** (atributo primo).
>
> Es equivalente a "sin dependencias parciales ni transitivas de atributos no clave". **3NF es menos restrictiva que BCNF**: permite un poco más de redundancia, pero garantiza que se pueda descomponer **sin perder dependencias**.
>
> **Transitividad:** si la llave K → País y País → Continente, Continente depende de K **a través** de País, que no es llave. Por eso "Italia → Europa" se repetiría en cada modelo italiano.

## Preguntas de repaso

1. ¿Qué es una dependencia transitiva?
> [!question]- Respuesta
> Cuando la llave determina un atributo no clave B, y B determina otro atributo no clave C. C depende de la llave "a través" de B.

2. Da la definición de 3NF de la clase.
> [!question]- Respuesta
> Para toda dependencia no trivial X → Y, X es superllave o Y es parte de alguna llave minimal.

3. ¿Por qué el ejemplo de mis apuntes no es un buen ejemplo de "2NF pero no 3NF"?
> [!question]- Respuesta
> Porque con llave (Fabricante, Modelo), Fabricante → País es una dependencia parcial: la tabla no está en 2NF.

4. ¿Cómo se descompone una tabla para eliminar la dependencia País → Continente?
> [!question]- Respuesta
> Se saca (País, Continente) a una tabla aparte y se deja País en la tabla original como referencia.
