---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - origen/complemento
prerrequisitos:
  - "[[02 - Sumas telescópicas y geométricas en la práctica]]"
  - "[[04 - Exponencial y logaritmo en otras bases]]"
---

# Ahorro y préstamos

Un crédito hipotecario es una **recurrencia**: cada mes la deuda crece por el interés y baja por la cuota que se paga. Con la suma geométrica se obtiene una fórmula cerrada que relaciona el monto prestado, la cuota, el interés y el plazo. Los problemas de ahorro y préstamo están entre las aplicaciones más antiguas de las matemáticas: ya hay tablillas babilónicas, de la época de Hammurabi, con cálculo de interés compuesto.

## Las variables

> [!tip] Variables del préstamo
> - $p_i$: **monto insoluto**, la parte del crédito aún pendiente de pago después de pagar las primeras $i$ cuotas ($p_0$ es el monto prestado).
> - $r_m$: tipo de interés **mensual**.
> - $\Delta$: monto de la **cuota** mensual.
> - $N$: **plazo** de amortización en años (hay $12N$ cuotas).

## La tasa mensual

Un banco declara una tasa anual $r_a$ (por ejemplo $3{,}17\,\%$), pero cobra interés mensual. En Chile (Banco Estado), la tasa mensual se define para que doce meses de interés compuesto den la tasa anual:
$$(1 + r_m)^{12} = 1 + r_a \iff r_m = (1 + r_a)^{1/12} - 1.$$
Con $r_a = 3{,}17\,\%$ queda $r_m = (1{,}0317)^{1/12} - 1 \approx 0{,}2604\,\%$. El significado de "tasa anual" varía de un país a otro.

## La recurrencia

Al final de cada mes se agrega el interés del mes, $r_m\,p_i$, y se descuenta la cuota:
$$p_{i+1} = p_i + r_m\,p_i - \Delta = p_i(1 + r_m) - \Delta.$$
Iterando: $p_1 = p_0(1 + r_m) - \Delta$, $p_2 = p_0(1 + r_m)^2 - \Delta\big(1 + (1 + r_m)\big)$, $p_3 = p_0(1 + r_m)^3 - \Delta\big(1 + (1 + r_m) + (1 + r_m)^2\big)$, y en general (se prueba por inducción)
$$p_i = p_0(1 + r_m)^i - \Delta\sum_{j=0}^{i-1}(1 + r_m)^j.$$

## La fórmula cerrada

Con la suma geométrica $\sum_{j=0}^{i-1}x^j = \dfrac{1 - x^i}{1 - x}$ y $x = 1 + r_m$:
$$p_i = p_0(1 + r_m)^i - \Delta\,\frac{(1 + r_m)^i - 1}{r_m}.$$
Pagar el crédito en $N$ años significa $p_{12N} = 0$, y de ahí:

> [!tip] Monto prestado en función de la cuota
> $$p_0 = \frac{\Delta}{r_m}\cdot\frac{(1 + r_m)^{12N} - 1}{(1 + r_m)^{12N}} = \frac{\Delta}{r_m}\left(1 - (1 + r_a)^{-N}\right),$$
> porque $(1 + r_m)^{12N} = (1 + r_a)^N$. Despejando la cuota: $\ \Delta = \dfrac{p_0\,r_m}{1 - (1 + r_a)^{-N}}$.

La fórmula tiene sentido aunque $N$ sea una variable continua, y se puede graficar $p_0$ como función de $N$: **crece con el plazo pero nunca supera $\tfrac{\Delta}{r_m}$**, porque $(1 + r_a)^{-N} \to 0$. Aunque se viviera para siempre, no se puede pedir prestado más allá de ese monto. Con $\Delta = 9$ UF, el máximo es $\tfrac{9}{(1{,}0317)^{1/12} - 1} \approx 3460$ UF.

## Ejemplos

**Cuánto se puede pedir (clase 23).** Con $\Delta = 9$ UF y $r_a = 3{,}17\,\%$:

| $N$ (años) | $p_0$ (UF, según la clase) | $p_0$ con $r_m$ sin redondear |
|---|---|---|
| $8$ | $764$ | $764$ |
| $15$ | $1293$ | $1292$ |
| $20$ | $1606$ | $1605$ |
| $25$ | $1874$ | $1872$ |
| $30$ | $2103$ | $2101$ |

En un crédito a $25$ años se pueden pedir unas $1874$ UF (alrededor de $61{,}4$ millones de pesos al valor de la UF del 06/06/2022: $9$ UF son $294\,908$ pesos). La tabla de la clase usa $r_m$ redondeado a $0{,}26\,\%$; con la tasa exacta las cifras bajan en unas pocas UF.

**La cuota y el costo total (clase 23).** Un préstamo de $1000$ UF a $20$ años con interés mensual de $\tfrac{2}{3}\,\%$. Entonces $r_a = \left(1 + \tfrac{2/3}{100}\right)^{12} - 1 \approx 0{,}083$ y
$$\Delta = \frac{p_0\,r_m}{1 - (1 + r_a)^{-N}} = \frac{1000 \cdot \tfrac{2/3}{100}}{1 - (1{,}083)^{-20}} \approx 8{,}36\ \text{UF}.$$
El monto total pagado es $M = \Delta \cdot 12N = 8{,}36 \cdot 240 \approx 2006{,}4$ UF: **más del doble** del préstamo, por los intereses.

> [!warning] Cuidar la tasa
> $r_a$ y $r_m$ no son proporcionales: $r_m \neq \tfrac{r_a}{12}$, porque el interés compuesto crece. Y en las fórmulas con $(1 + r_a)^{-N}$ el plazo $N$ va en **años**, mientras que con $r_m$ el exponente es el número de meses $12N$.

## Preguntas de repaso

> [!question]- ¿Qué significa que $p_{12N} = 0$?
> Que después de las $12N$ cuotas mensuales el monto insoluto es cero: el crédito quedó totalmente pagado.

> [!question]- ¿Por qué el monto máximo prestable no crece sin límite al aumentar $N$?
> Porque $p_0 = \frac{\Delta}{r_m}\big(1 - (1 + r_a)^{-N}\big)$ y el paréntesis se acerca a $1$: queda acotado por $\frac{\Delta}{r_m}$.

> [!question]- ¿Qué sucede con el costo total del crédito al alargar el plazo?
> Con la misma cuota se puede pedir más, pero se paga durante más meses y el total pagado $12N\Delta$ crece; los intereses pesan cada vez más sobre el capital.

> [!question]- ¿De dónde sale la suma $\sum_{j=0}^{i-1}(1 + r_m)^j$ en $p_i$?
> De iterar $p_{i+1} = p_i(1 + r_m) - \Delta$: cada cuota pagada en el mes $j$ se "capitaliza" por los meses restantes, y la suma de esas potencias es geométrica.
