---
ramo: "Matemáticas Discretas"
tema: "Satisfacibilidad, consecuencia y resolución"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos:
  - "[[01 - Satisfacibilidad de fórmulas y tautologías proposicionales]]"
---

# Conjuntos de fórmulas y consecuencia lógica

Razonar es partir de ciertas premisas y concluir algo. Para formalizarlo hacen falta dos cosas: poder hablar de varias fórmulas a la vez (un conjunto $\Sigma$ de premisas) y precisar cuándo una conclusión "se deduce" de ellas.

## Satisfacer un conjunto

Una valuación $\sigma$ **satisface** un conjunto de fórmulas $\Sigma$, lo que se escribe $\sigma(\Sigma) = 1$, si $\sigma(\varphi) = 1$ para **toda** $\varphi \in \Sigma$. El conjunto es **satisfacible** si alguna valuación lo satisface; en caso contrario es **inconsistente**. Un conjunto equivale a la conjunción de sus fórmulas: $\Sigma \equiv \bigwedge_{\varphi \in \Sigma}\varphi$.

Por ejemplo, $\{p, p \to q\}$ es satisfacible (con $p = q = 1$) y $\{p, \neg p\}$ es inconsistente.

## Consecuencia lógica

> [!tip] Definición
> $\psi$ es **consecuencia lógica** de $\Sigma$, escrito $\Sigma \models \psi$, si toda valuación que satisface $\Sigma$ también satisface $\psi$.

La conclusión debe ser verdadera en **todos los mundos donde las premisas lo son**. Los mundos donde alguna premisa falla no se miran: ahí no hay obligación.

## Ejemplo: modus ponens

La regla $\{p, p \to q\} \models q$ se revisa con una tabla de verdad, buscando solo las filas donde $p$ y $p \to q$ valen $1$.

![Tabla de verdad de modus ponens](adjuntos/Tabla%20de%20verdad%20de%20modus%20ponens.png)

> [!example]- Transcripción de la imagen
> Tabla con columnas $p$, $q$, $p$, $p \to q$ y $q$ (las tres últimas separadas por líneas). Las filas son $00, 01, 10, 11$. La fila $p = 1, q = 1$ aparece resaltada: es la única donde $p$ vale $1$ y $p \to q$ vale $1$, y allí $q$ vale $1$.

Solo la última fila satisface las dos premisas, y en ella $q = 1$. Otras reglas se comprueban igual (se verificaron con todas las valuaciones):

- **Modus tollens:** $\{\neg q, p \to q\} \models \neg p$.
- **Demostración por partes:** $\{p \lor q \lor r,\; p \to s,\; q \to s,\; r \to s\} \models s$.

## Propiedades útiles

- **Premisas de más no estorban (monotonía):** si $\Sigma \models \psi$ y $\Sigma \subseteq \Sigma'$, entonces $\Sigma' \models \psi$, porque satisfacer $\Sigma'$ implica satisfacer $\Sigma$.
- **Conjunto vacío:** $\emptyset \models \psi$ equivale a que $\psi$ sea tautología.
- **Premisas inconsistentes:** si $\Sigma$ es inconsistente, $\Sigma \models \psi$ para toda $\psi$, ya que no existe ninguna valuación que verificar.
- **Relación con la implicación:** para $\Sigma$ finito, $\Sigma \models \psi$ si y solo si $\bigwedge\Sigma \to \psi$ es tautología.

> [!warning] $\models$ no es $\to$
> $\to$ es un conectivo que forma una fórmula y se evalúa en una valuación; $\models$ es una afirmación **sobre todas** las valuaciones. $p \to q$ puede ser falsa en algún mundo y aun así tener sentido; $p \models q$ es falsa apenas haya un mundo donde $p$ es verdadera y $q$ falsa.

## Preguntas de repaso

> [!question]- ¿Por qué una valuación que falsifica una premisa no puede refutar la consecuencia?
> La definición solo exige que $\psi$ valga $1$ cuando todas las premisas valen $1$. Si una premisa vale $0$ la condición es vacía y la valuación no cuenta.

> [!question]- ¿Es cierto que $\{p\} \models p \to q$?
> No: con $p = 1, q = 0$ la premisa es verdadera y $p \to q$ es falsa.

> [!question]- ¿Por qué de un conjunto inconsistente se deduce cualquier cosa?
> Porque no hay mundos que lo satisfagan; la condición "para todo mundo que satisface $\Sigma$" no tiene casos, así que se cumple siempre.

> [!question]- ¿Qué cambia en $\Sigma \models \psi$ si se agrega una premisa a $\Sigma$?
> Nada se pierde: toda consecuencia anterior se mantiene (monotonía), y pueden aparecer nuevas.
