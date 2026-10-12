---
ramo: Bases de Datos
tema: Privacidad de datos
tags: [bd/privacidad, origen/complemento]
prerrequisitos: ["[[03 - k-anonimato|k-anonimato]]"]
---
# ℓ-diversidad

La **ℓ-diversidad** refuerza el k-anonimato: además de grupos grandes, exige que en cada grupo el atributo sensible tenga **al menos ℓ valores distintos**. Así se evita el ataque de homogeneidad.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 15: Privacidad", [Machanavajjhala et al., 2006])
> **Definición:** además de lo que exige el k-anonimato, una tabla T es **ℓ-diversa** si para cada grupo de filas con los mismos CIds, y por cada atributo sensible S, existen **al menos ℓ valores distintos**.
>
> ```sql
> SELECT CIds, count(DISTINCT S) FROM T GROUP BY CIds;   -- todos deben ser ≥ ℓ
> ```
>
> - **Previene el ataque #1 (homogeneidad):** ya no hay un grupo donde todos tengan cáncer.
> - **Aumenta la resistencia al ataque #2 (datos auxiliares).**

> [!example] Ejemplo extra — el ataque que sigue funcionando (slides "Clase 15")
> El grupo 130\*\*/<30 ahora es diverso: {Heart, Diabetes, Cáncer, Flu}. Pero si el atacante sabe que Umeko **no** tiene cáncer, **no** tiene una enfermedad cardíaca y **no** tiene diabetes, descarta tres valores y aprende que **Umeko está resfriada**.
>
> La garantía solo resiste mientras el adversario conozca **menos de ℓ−2 datos negativos** sobre el grupo.

> [!tip] Complemento — balance de las técnicas de de-identificación (slides "Clase 15")
> - Son enfoques **formales y sistemáticos**, una mejora sustentable respecto de los enfoques ad-hoc.
> - **Aún así son susceptibles a ataques:** la protección depende de la información auxiliar del adversario.
> - **Automatizarlas tiene alto costo:** dada una tabla T, encontrar una T′ que satisfaga k-anonimato y maximice la utilidad es **NP-complejo** (Meyerson & Williams, 2004).
>
> Por eso aparece la [[05 - Privacidad diferencial|privacidad diferencial]], cuya garantía no depende de los datos auxiliares.

## Preguntas de repaso

1. Define ℓ-diversidad.
> [!question]- Respuesta
> Una tabla k-anónima es ℓ-diversa si en cada grupo con los mismos cuasi-identificadores el atributo sensible toma al menos ℓ valores distintos.

2. ¿Qué ataque previene la ℓ-diversidad y cuál no del todo?
> [!question]- Respuesta
> Previene el de homogeneidad. Solo resiste en parte el de datos auxiliares: si el atacante descarta suficientes valores, igual deduce el sensible.

3. ¿Cómo verificas con SQL que una tabla es ℓ-diversa?
> [!question]- Respuesta
> Con `SELECT CIds, count(DISTINCT S) FROM T GROUP BY CIds`: todos los conteos deben ser al menos ℓ.

4. ¿Por qué es difícil automatizar el k-anonimato óptimo?
> [!question]- Respuesta
> Porque encontrar la tabla k-anónima que maximiza la utilidad es un problema NP-complejo.
