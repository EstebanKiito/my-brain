---
ramo: Bases de Datos
tema: Privacidad de datos
tags: [bd/privacidad, origen/complemento]
prerrequisitos: ["[[02 - Anonimización y re-identificación|Anonimización y re-identificación]]", "[[03 - GROUP BY|GROUP BY]]"]
---
# k-anonimato

Una tabla es **k-anónima** si cada combinación de cuasi-identificadores aparece **al menos k veces**: cualquier persona se confunde con al menos k−1 otras. Se logra **generalizando** los valores (rangos, prefijos) y eliminando outliers.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 15: Privacidad", [Pierangela and Sweeney, 1998])
> **Definición:** sea $T(A_1, \dots, A_n)$ una tabla y $\mathcal{Q}$ sus CIds. T satisface **k-anonimato** si y solo si cada grupo de valores de CIds $Q_i \in \mathcal{Q}$ aparece **al menos k veces** en T. Así ningún individuo es identificable de forma única dentro de un grupo de tamaño k. Igual hay que **identificar** todos los cuasi-identificadores.
>
> **Se verifica con SQL:** todos los grupos deben cumplir `count(*) ≥ k`.
> ```sql
> SELECT CIds, count(*) FROM T GROUP BY CIds;   -- el mínimo de count(*) es el k
> ```

> [!example] Ejemplo extra — cómo se sube el k (slides "Clase 15", dataset de personas con age y education_num)
> 1. Agrupar por `age, education_num` exactos → hay grupos con 1 persona: **1-anónima**.
> 2. **Generalizar** por décadas: `(age/10)*10`, `(education_num/10)*10` → mejoró, pero **sigue siendo 1-anónima** (hay una sola persona de 90 años).
> 3. El problema son los **outliers**. Truncar las edades mayores que 60: `LEAST((age/10)*10, 60)` → **12-anónima**.
> 4. Con **más datos** (más filas) la misma consulta llega a **455-anonimato**.
> ```sql
> SELECT LEAST((age/10)*10, 60) AS a, (education_num/10)*10 AS e, count(*) AS c
> FROM person
> GROUP BY LEAST((age/10)*10, 60), (education_num/10)*10
> ORDER BY c ASC;      -- el primer c es el k
> ```
> (En la slide la columna aparece como `eduction_num`, una errata.)

> [!example] Ejemplo extra — otro ejemplo de la clase: de 1-anónima a 4-anónima
> Generalizando `zip` (13053 → 130\*\*), `age` (28 → <30) y suprimiendo `nationality` (\*):
> | zip | age | nationality | disease |
> |---|---|---|---|
> | 130\*\* | <30 | \* | Heart, Heart, Flu, Flu |
> | 1485\* | >40 | \* | Cáncer, Heart, Flu, Flu |
> | 130\*\* | 30-40 | \* | Cáncer, Cáncer, Cáncer, Cáncer |
>
> Cada grupo tiene 4 filas: **4-anónima**. ¿Hay algún problema? Sí:
> - **Ataque #1, homogeneidad:** Bob (13053, 35 años) cae en el grupo 130\*\*/30-40, donde **todos** tienen cáncer → aprendemos que Bob tiene cáncer.
> - **Ataque #2, datos auxiliares:** Umeko (13068, 24, japonesa) cae en 130\*\*/<30 (Heart o Flu). Si se sabe que los japoneses tienen muy baja incidencia de enfermedades cardíacas → Umeko tiene Flu.
>
> La solución al ataque #1 es la [[04 - ℓ-diversidad|ℓ-diversidad]].

## Preguntas de repaso

1. Define k-anonimato.
> [!question]- Respuesta
> Una tabla es k-anónima si cada combinación de valores de los cuasi-identificadores aparece al menos k veces, de modo que nadie es único dentro de un grupo de tamaño menor que k.

2. ¿Cómo verificas con SQL el k de una tabla?
> [!question]- Respuesta
> Con `SELECT CIds, count(*) FROM T GROUP BY CIds ORDER BY count(*)`: el menor conteo es el k.

3. ¿Qué técnicas suben el k?
> [!question]- Respuesta
> Generalizar valores (décadas, prefijos de zip), suprimir atributos, eliminar o truncar outliers y contar con más datos.

4. ¿Qué es el ataque de homogeneidad?
> [!question]- Respuesta
> Cuando todos los registros de un grupo k-anónimo tienen el mismo valor sensible: si sé que alguien está en ese grupo, conozco su valor sensible aunque no sepa cuál fila es.
