---
ramo: Bases de Datos
tema: Normalización
tags: [bd/normalizacion, origen/apuntes]
prerrequisitos: ["[[04 - Segunda forma normal|Segunda forma normal]]"]
---
# Tercera forma normal

Una tabla está en **3NF** si está en 2NF y ningún atributo no clave depende de la llave **a través de otro atributo no clave** (no hay dependencias transitivas).

## Tercera forma normal (3NF)
Una relación está en 3NF si está en 2NF y ningún atributo no clave es transitivamente dependiente de la clave primaria.

Ejemplo de relación que **no** está en 3NF. Es la tabla de fabricantes que resultó de la [[04 - Segunda forma normal|2NF]], ahora con el continente; su llave es **Fabricante**:

| Fabricante | País Fabricante | Continente |
|---|---|---|
| Forte | Italia | Europa |
| Hoch | Alemania | Europa |

Dependencia transitiva: Fabricante → País Fabricante → Continente. El continente depende de la llave **a través** del país, que no es llave.

Descomposición para lograr 3NF:

Tabla 1:

| Fabricante | País Fabricante |
|---|---|
| Forte | Italia |
| Hoch | Alemania |

Tabla 2:

| País Fabricante | Continente |
|---|---|
| Italia | Europa |
| Alemania | Europa |

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

3. ¿Por qué en el ejemplo la llave es solo Fabricante y no (Fabricante, Modelo)?
> [!question]- Respuesta
> Porque con llave (Fabricante, Modelo), Fabricante → País sería una dependencia parcial y la tabla ni siquiera estaría en 2NF. Para mostrar una dependencia transitiva hace falta una tabla que ya esté en 2NF.

4. ¿Cómo se descompone una tabla para eliminar la dependencia País → Continente?
> [!question]- Respuesta
> Se saca (País, Continente) a una tabla aparte y se deja País en la tabla original como referencia.
