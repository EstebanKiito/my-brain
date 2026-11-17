---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[04 - Conjuntos de fórmulas y consecuencia lógica]]"
---

# Consecuencia lógica e inconsistencia

Comprobar $\Sigma \models \psi$ por definición obliga a mirar todas las valuaciones. Hay un resultado que traduce la pregunta de consecuencia a una pregunta de satisfacibilidad, y esa traducción es la puerta de entrada al método de resolución.

## El teorema fundamental

> [!tip] Consecuencia como refutación
> $\Sigma \models \varphi$ si y solo si $\Sigma \cup \{\neg\varphi\}$ es inconsistente.

La idea: $\varphi$ se deduce de $\Sigma$ exactamente cuando es **imposible** tener las premisas verdaderas y la conclusión falsa a la vez.

**($\Rightarrow$)** Si $\Sigma \models \varphi$ y existiera $\sigma$ que satisface $\Sigma \cup \{\neg\varphi\}$, entonces $\sigma(\Sigma) = 1$ y $\sigma(\varphi) = 0$, lo que contradice la definición de consecuencia. Luego el conjunto es inconsistente.

**($\Leftarrow$)** Si $\Sigma \cup \{\neg\varphi\}$ es inconsistente, sea $\sigma$ con $\sigma(\Sigma) = 1$. Como ninguna valuación satisface el conjunto ampliado, necesariamente $\sigma(\neg\varphi) = 0$, es decir $\sigma(\varphi) = 1$. Entonces toda valuación que satisface $\Sigma$ satisface $\varphi$.

## Ejemplo

Para $\{p, p \to q\} \models q$ se agrega la negación de la conclusión y se busca una contradicción: el conjunto $\{p,\; p \to q,\; \neg q\}$ es inconsistente porque $p = 1$ obliga a $q = 1$ por la implicación, pero también $q = 0$. Esto es lo mismo que decir que no hay mundo donde las premisas valgan $1$ y la conclusión $0$.

Cuando la consecuencia **no** vale, el mismo método entrega el contraejemplo. Para $\{p \lor q\} \models p$ se estudia $\{p \lor q,\; \neg p\}$: es satisfacible con $p = 0, q = 1$, y esa valuación muestra que las premisas pueden ser verdaderas con la conclusión falsa. Por eso $p \lor q \not\models p$.

## La cláusula vacía

Se llama **cláusula vacía**, y se escribe $\square$, a una contradicción cualquiera: la disyunción de cero literales, que nunca es verdadera. Sirve como "meta" de las demostraciones por refutación.

> [!tip] Inconsistencia como consecuencia
> $\Sigma$ es inconsistente si y solo si $\Sigma \models \square$.

**($\Rightarrow$)** Si $\Sigma$ es inconsistente, toda valuación lo falsifica, así que la condición de $\Sigma \models \square$ se cumple sin casos que revisar. **($\Leftarrow$)** Si $\Sigma$ fuera satisfacible por $\sigma$, de $\Sigma \models \square$ saldría $\sigma(\square) = 1$, absurdo porque $\square$ es una contradicción.

Los dos resultados se encadenan: $\Sigma \models \varphi$ si y solo si $\Sigma \cup \{\neg\varphi\} \models \square$. Demostrar una consecuencia se vuelve **llegar a una contradicción**.

## Otras caracterizaciones de la consecuencia

Con estas mismas ideas se prueban, con distintos grados de trabajo, equivalencias frecuentes:

- Si $\Sigma \models \varphi \to \psi$, entonces $\Sigma \cup \{\varphi\} \models \psi$ (y también al revés).
- $\alpha \models \beta$ si y solo si $\alpha \equiv \alpha \land \beta$.
- Si $\varphi$ es tautología, $\Sigma \cup \{\varphi\} \models \psi$ implica $\Sigma \models \psi$: agregar una tautología no cambia los mundos que satisfacen el conjunto.

## Preguntas de repaso

> [!question]- ¿Por qué es útil pasar de "consecuencia" a "inconsistencia"?
> Porque la inconsistencia es una propiedad de un solo conjunto, que puede atacarse con un método mecánico (tablas o resolución). La consecuencia, en cambio, habla de todas las valuaciones de las premisas y de la conclusión a la vez.

> [!question]- Si $\Sigma \cup \{\neg\varphi\}$ fuera satisfacible, ¿qué prueba eso?
> Que $\Sigma \not\models \varphi$: la valuación que lo satisface es un contraejemplo, con premisas verdaderas y $\varphi$ falsa.

> [!question]- ¿Cómo se relacionan $\Sigma \models \square$ y $\Sigma \models \varphi \land \neg\varphi$?
> Son lo mismo: ambos dicen que $\Sigma$ no tiene valuaciones que lo satisfagan, porque la conclusión es una contradicción.
