---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[04 - Equivalencias y negación con cuantificadores]]"
---

# Consecuencia lógica en predicados y reglas de inferencia

«Todas las personas son mortales; Sócrates es persona; luego Sócrates es mortal.» La lógica proposicional no puede explicar por qué este argumento es válido, porque necesita «todas» y objetos concretos. La lógica de predicados sí, y la noción de consecuencia se extiende de manera natural.

## Definición de consecuencia

Una interpretación $I$ **satisface un conjunto** $\Sigma$ de fórmulas sobre $\bar a$ si satisface cada una de ellas.

> [!tip] Consecuencia lógica
> $\varphi$ es **consecuencia lógica** de $\Sigma$, $\Sigma \models \varphi$, si para toda interpretación $I$ y valores $\bar a$ del dominio: si $I \models \Sigma(\bar a)$ entonces $I \models \varphi(\bar a)$.

Se cumple que $\Sigma \models \varphi$ si y sólo si $\Sigma \cup \{\neg\varphi\}$ no es satisfacible (es inconsistente). Esto permite probar consecuencias por refutación y es la base del sistema deductivo.

## Ejemplos de consecuencias (válidas e inválidas)

| Candidato | ¿Válido? | Razón |
|---|---|---|
| $\{\forall x\,\varphi \wedge \forall x\,\psi\} \models \forall x\,(\varphi \wedge \psi)$ | sí | si todos cumplen $\varphi$ y todos cumplen $\psi$, todos cumplen ambas |
| $\{\exists x\,\varphi \wedge \exists x\,\psi\} \models \exists x\,(\varphi \wedge \psi)$ | **no** | dominio $\{0, 1\}$, $\varphi$ sólo en $0$ y $\psi$ sólo en $1$ |
| $\{\forall x\,\varphi\} \models \exists x\,\varphi$ | sí | el dominio es no vacío, el elemento que existe cumple $\varphi$ |
| $\{\forall x\,\exists y\,\varphi(x, y)\} \models \exists x\,\forall y\,\varphi(x, y)$ | **no** | $R = \{(0, 1), (1, 1)\}$ sobre $\{0, 1\}$: todo elemento apunta a $1$, pero ninguno apunta a $0$ |

## Cuatro reglas de inferencia para cuantificadores

Además de resolución y factorización de la lógica proposicional, se usan:

| Regla | Premisa | Conclusión | Cuidado |
|---|---|---|---|
| **Especificación universal** | $\forall x\,\varphi(x)$ | $\varphi(a)$ para **cualquier** $a$ | $a$ puede ser cualquier objeto |
| **Generalización universal** | $\varphi(a)$ con $a$ **arbitrario** | $\forall x\,\varphi(x)$ | $a$ no puede ser un objeto particular con supuestos |
| **Especificación existencial** | $\exists x\,\varphi(x)$ | $\varphi(a)$ para **algún** $a$ nuevo | $a$ es un nombre nuevo, no usado antes |
| **Generalización existencial** | $\varphi(a)$ para algún $a$ | $\exists x\,\varphi(x)$ | basta un testigo |

> [!warning] Nombre nuevo en la especificación existencial
> Si ya se sabe $\exists x\,P(x)$ y $\exists x\,Q(x)$, no se puede usar el **mismo** $a$ para ambos: serían testigos distintos. Cada especificación existencial introduce una constante fresca.

## Ejemplo: Sócrates por resolución

Con $P(x)$: «$x$ es persona», $M(x)$: «$x$ es mortal» y la constante $s$ (Sócrates), el argumento es $\{\forall x\,(P(x) \to M(x)),\ P(s)\} \models M(s)$. Se reemplaza la implicación y se agrega la negación de la conclusión; se busca la cláusula vacía:

1. $\forall x\,(\neg P(x) \vee M(x))$ (premisa)
2. $\neg P(s) \vee M(s)$ (especificación universal de 1)
3. $P(s)$ (premisa)
4. $M(s)$ (resolución de 2 y 3)
5. $\neg M(s)$ (negación de la conclusión)
6. $\square$ (resolución de 4 y 5)

Como el conjunto con la negación de la conclusión es inconsistente, la conclusión es consecuencia lógica.

## Refutar un argumento

Un argumento **no** es válido si existe una interpretación que satisface todas las premisas y falla la conclusión. Ejemplo: «Todos los albos son borrachos. Algunos cruzados no son borrachos. No hay hinchas cruzados y albos a la vez. Luego ningún cruzado es borracho.» Con dominio $\{1, 2, 3, 4\}$, $A = \{1\}$, $B = \{1, 2, 3\}$, $C = \{3, 4\}$ las premisas se cumplen (el $4$ es cruzado y no borracho; nadie es albo y cruzado), pero el $3$ es cruzado y borracho: la conclusión falla.

## Preguntas de repaso

> [!question]- ¿Por qué la especificación existencial exige un nombre nuevo?
> Porque $\exists x\,\varphi(x)$ sólo asegura que hay **algún** objeto con la propiedad, no cuál. Si se reutilizara un nombre ya conocido se supondría, sin justificación, que ese objeto específico cumple $\varphi$.

> [!question]- ¿Por qué $\forall x\,\varphi \models \exists x\,\varphi$ pero $\exists x\,\varphi \not\models \forall x\,\varphi$?
> Con dominio no vacío, si todos cumplen $\varphi$ al menos uno lo hace. Lo contrario falla si un objeto cumple $\varphi$ y otro no.

> [!question]- ¿Cómo se prueba que un argumento en predicados es inválido?
> Con un contramodelo: una interpretación (de preferencia con un dominio de pocos elementos) donde todas las premisas sean verdaderas y la conclusión falsa.
