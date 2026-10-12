---
ramo: Bases de Datos
tema: Privacidad de datos
tags: [bd/privacidad, origen/complemento]
prerrequisitos: ["[[04 - ℓ-diversidad|ℓ-diversidad]]", "[[01 - Funciones de agregación|Funciones de agregación]]"]
---
# Privacidad diferencial

La **privacidad diferencial** es una propiedad de un **mecanismo** (no de los datos): las respuestas a consultas llevan **ruido aleatorio**, calibrado para que el resultado sea casi el mismo esté o no una persona en la base. Su garantía no depende de lo que sepa el atacante.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 15: Privacidad")
> **Definición:** sea $f$ un algoritmo aleatorio y $x, y$ dos bases de datos idénticas excepto por un individuo (a "distancia" ≤ 1). $f$ es **ϵ-diferencialmente privada** si para todo conjunto de resultados $S$:
> $$\Pr[f(x) \in S] \le e^{\epsilon} \cdot \Pr[f(y) \in S]$$
> Es decir, $f(x)$ y $f(y)$ son "casi lo mismo". Los mecanismos agregan **ruido aleatorio** a los resultados, y cuánto ruido depende de la **sensibilidad** de la consulta.
>
> **Ejemplo:** `SELECT count(*) FROM person WHERE age >= 40` → 14237. ¿Cuál es la **sensibilidad**? ¿Cuánto puede variar como máximo el resultado si se agrega o se saca un individuo? **En 1.**
>
> **Mecanismo de Laplace:** $F(x) = f(x) + Lap(s/\epsilon)$, con $s$ la sensibilidad y $\epsilon$ el **presupuesto de privacidad**. Con $\epsilon = 0{,}1$, cada ejecución da algo como 14211,23 · 14265,77 · 14265,92 · 14209,09: útil, porque el error es pequeño frente a 14237.
>
> **Consulta maliciosa:** `… WHERE name = 'Alan Brito' AND target = '<=50k'` (respuesta real: 1) devuelve 18,47 · 15,16 · −0,69 · −2,12… ¿Es útil? No, pero no importa: la consulta era maliciosa (demasiado selectiva).

> [!tip] Complemento — el presupuesto ϵ (slides "Clase 15")
> - **Si se repite la consulta muchas veces**, el promedio de las respuestas revela que el valor es 1: las consultas **no son independientes**. Por eso ϵ es un **presupuesto**: se reparte entre todas las consultas. Si se hacen 4, cada una usa ϵ/4, y por eso **cada respuesta trae más ruido**.
> - **Composición secuencial:** si $F_1$ es $\epsilon_1$-DP y $F_2$ es $\epsilon_2$-DP, liberar ambos resultados es $(\epsilon_1 + \epsilon_2)$-DP.
> - **Composición paralela:** si se divide el dataset en k pedazos **disjuntos** ($x_1 \cup \dots \cup x_k = X$) y se aplica $F$ ($\epsilon$-DP) a cada uno, el total sigue siendo **ϵ-DP**, mucho mejor que $k\epsilon$. Ejemplo de la clase: una tabla de conteos por educación y sexo con ruido en cada celda (Bachelors/Female: 1619 → 1618,32).

> [!tip] Complemento — garantías y limitaciones (slides "Clase 15")
> | Lo bueno | Lo malo |
> |---|---|
> | el adversario no puede distinguir entre las dos bases: el resultado es el mismo participe yo o no | **no funciona para datos sintéticos**, solo para respuestas de consultas (es propiedad del mecanismo, no de los datos) |
> | "nada malo me pasa como resultado de mi participación": si pasa, habría pasado igual sin mí | **garantía difícil de interpretar**: ¿qué ϵ basta? |
> | se demuestra formalmente | ϵ muy chico ⇒ poca utilidad; ϵ muy grande ⇒ se vuelve posible re-identificar |
> | **independiente de los datos auxiliares** del adversario, incluso si conoce toda la base menos la fila objetivo | aún no se sabe qué ϵ es "suficiente" |
> | previene los ataques de asociación contra k-anonimato y ℓ-diversidad; es lo más cercano a una "anonimización verdadera" | |

> [!tip] Complemento — resumen del tema (slides "Clase 15")
> | Técnica | Idea | Debilidad |
> |---|---|---|
> | De-identificación | eliminar identificadores; la más usada | enfoques ad-hoc, alto riesgo de errores |
> | k-anonimato | grupos de tamaño ≥ k | homogeneidad y datos auxiliares |
> | ℓ-diversidad | grupos diversos | datos auxiliares (≥ ℓ−2 datos negativos) |
> | Privacidad diferencial | indistinguibilidad del mecanismo | elegir ϵ; solo respuestas a consultas |

## Preguntas de repaso

1. ¿Qué garantiza que un mecanismo sea ϵ-diferencialmente privado?
> [!question]- Respuesta
> Que para dos bases que difieren en un solo individuo, la probabilidad de cualquier resultado cambia a lo más en un factor $e^\epsilon$. El resultado casi no depende de si esa persona participa.

2. ¿Qué es la sensibilidad de una consulta y cuánto vale para un `count(*)`?
> [!question]- Respuesta
> Cuánto puede cambiar como máximo el resultado al agregar o quitar un individuo. Para un conteo vale 1.

3. ¿Por qué ϵ se llama presupuesto?
> [!question]- Respuesta
> Porque cada consulta gasta parte de él. Repetir consultas permite promediar el ruido, así que ϵ se reparte entre todas (composición secuencial) y cada respuesta lleva más ruido.

4. ¿Qué ventaja tiene la privacidad diferencial sobre k-anonimato y ℓ-diversidad?
> [!question]- Respuesta
> Su garantía no depende de los datos auxiliares del adversario, así que resiste los ataques de asociación.
