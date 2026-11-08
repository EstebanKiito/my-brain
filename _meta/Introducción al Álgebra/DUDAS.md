# Dudas y posibles errores en el material original — Introducción al Álgebra (MAT1207)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido, las discrepancias entre fuentes y las pautas que no calzan con el cálculo verificado.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

- ℹ️ **Notación de negación.** Las clases y apuntes usan la negación como una barra sobre la letra ($\bar p$). Al extraer el texto de los PDF, esa barra se pierde sistemáticamente, así que en las fuentes aparece "$p \vee p$" donde debe leerse "$p \vee \neg p$", etc. Todas las leyes, tautologías y ejercicios se reconstruyeron con la negación correcta (se verificó cada equivalencia con tabla de verdad).
- 🟡 **Guía 1b (negación de $M$).** La guía afirma que la negación de $M : (p \vee q) \Rightarrow (p \wedge r)$ equivale a $p \vee (q \wedge r)$. El cálculo con tablas de verdad da $\neg M \equiv (p \vee q) \wedge (\neg p \vee \neg r)$; la expresión $p \vee (q \wedge r)$ no es equivalente (falla, por ejemplo, con $p=F$, $q=V$, $r=F$). La nota de ejercicios usa la versión correcta.
- 🟡 **Guía 5a y Auxiliar P2.1 (conectivo "ni–ni").** Ambas fuentes escriben "$p \Leftrightarrow (p \downarrow q)$" y "$p \Leftrightarrow (p \downarrow p)$". Como $p \downarrow p \equiv \neg p$, lo correcto es "$\neg p \Leftrightarrow (p \downarrow p)$" (a la primera igualdad le falta la negación). La nota de ejercicios presenta las equivalencias correctas.
