---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[03 - Literales, cláusulas y formas normales DNF y CNF]]"
  - "[[05 - Consecuencia lógica e inconsistencia]]"
---

# Regla de resolución y factorización

Para decidir si $\Sigma \cup \{\neg\varphi\}$ es inconsistente las tablas de verdad son demasiado lentas. La **resolución** ofrece un método simbólico: trabajar con cláusulas y combinarlas con una única regla de inferencia hasta alcanzar la cláusula vacía.

## Primer ingrediente: trabajar con cláusulas

Un conjunto de fórmulas $\Sigma$ es equivalente a un conjunto de cláusulas: se lleva cada fórmula a CNF (ver [[03 - Literales, cláusulas y formas normales DNF y CNF]]) y se separa cada conjunción en sus cláusulas, ya que un conjunto equivale a la conjunción de sus elementos.

Ejemplo: para $\{p,\; q \to (p \to r),\; \neg(q \to r)\}$:

- $q \to (p \to r) \equiv \neg q \lor (\neg p \lor r) \equiv \neg q \lor \neg p \lor r$ (implicación material y asociatividad).
- $\neg(q \to r) \equiv \neg(\neg q \lor r) \equiv q \land \neg r$ (implicación y De Morgan), que aporta las cláusulas $q$ y $\neg r$.

Resultado: $\{p,\; \neg q \lor \neg p \lor r,\; q,\; \neg r\}$.

## Literales complementarios

Para un literal $\ell$, su **complemento** $\bar\ell$ es $\neg p$ si $\ell = p$ y es $p$ si $\ell = \neg p$. Dos literales $\ell$ y $\bar\ell$ se llaman **complementarios**.

## La regla de resolución

> [!tip] Resolución
> De dos cláusulas con literales complementarios se deduce la cláusula formada por todo lo demás:
> $$\frac{C_1 \lor \ell \lor C_2 \qquad C_3 \lor \bar\ell \lor C_4}{C_1 \lor C_2 \lor C_3 \lor C_4}$$

Es una regla **correcta**: $\{C_1 \lor \ell \lor C_2,\; C_3 \lor \bar\ell \lor C_4\} \models C_1 \lor C_2 \lor C_3 \lor C_4$. En un mundo donde ambas premisas son verdaderas, $\ell$ y $\bar\ell$ no pueden valer $1$ a la vez. Si $\ell = 0$, la primera premisa obliga a que $C_1$ o $C_2$ valga $1$; si $\ell = 1$, la segunda obliga a $C_3$ o $C_4$.

Casos particulares importantes:

- Con $p \lor q$ y $\neg p \lor r$ se obtiene $q \lor r$ ("se cancela $p$").
- Con $\ell$ y $\bar\ell$ (dos cláusulas de un solo literal) se obtiene $\square$: es la contradicción directa.
- Con $\ell$ y $\bar\ell \lor C$ se obtiene $C$ (equivale a modus ponens).

> [!warning] Se cancela un solo par de literales a la vez
> De $p \lor q$ y $\neg p \lor \neg q$ se obtiene $q \lor \neg q$ (resolviendo en $p$) o $p \lor \neg p$ (resolviendo en $q$), que son tautologías, **no** $\square$. Cancelar los dos pares al mismo tiempo sería incorrecto.

## La regla de factorización

Una cláusula puede traer el mismo literal repetido, y resolver puede producir esas repeticiones. La **factorización** elimina una copia:

$$\frac{C_1 \lor \ell \lor C_2 \lor \ell \lor C_3}{C_1 \lor \ell \lor C_2 \lor C_3}$$

También es correcta, porque $\ell \lor \ell \equiv \ell$. Sin ella, cláusulas como $s \lor s$ no se podrían reducir a $s$, y la demostración quedaría bloqueada.

## Preguntas de repaso

> [!question]- ¿Por qué la resolución es correcta aunque parezca que "desaparece" información?
> Porque la cláusula obtenida solo afirma lo que ya está garantizado: en cualquier mundo que cumpla las dos premisas, alguno de los literales restantes tiene que ser verdadero.

> [!question]- ¿Qué pasa si se resuelven dos cláusulas sin literales complementarios?
> La regla no se puede aplicar: sin un literal y su complemento no hay nada que cancelar.

> [!question]- ¿Por qué hace falta factorización además de resolución?
> Resolver puede dejar un literal duplicado ($s \lor s \lor r$), y para llegar a cláusulas más cortas (o a $\square$) hay que fusionar los duplicados.

> [!question]- ¿Qué cláusulas produce resolver $p$ con $\neg p \lor q \lor r$?
> $q \lor r$: se cancela $p$ y quedan los otros literales.
