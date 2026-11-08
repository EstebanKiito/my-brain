---
ramo: "Introducción al Álgebra"
tema: "Trigonometría: razones y resolución de triángulos"
tags:
  - intro-algebra/trigonometria
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Área de un triángulo]]"
  - "[[04 - Teorema del seno y del coseno]]"
---

# Ejercicios de prueba de resolución de triángulos

Preguntas de interrogaciones anteriores. Casi todas traen una figura con varios triángulos pegados; el trabajo está en elegir **en qué triángulo** usar cada teorema y en reconocer ángulos suplementarios (los que forman un ángulo extendido suman $180^\circ$). Las pautas puntúan por separado el teorema usado, el despeje y el valor final.

## Ejercicios

### 1. Área con un ángulo obtuso
Encuentre el área del triángulo $ABC$ con $AB = 2$, $AC = 3$ y $\angle BAC = 120^\circ$.

> [!example]- Solución
> Área $= \frac{1}{2} \cdot AB \cdot AC \cdot \sin(\angle BAC) = \frac{1}{2} \cdot 2 \cdot 3 \cdot \sin 120^\circ = 3 \sin 60^\circ = \frac{3\sqrt 3}{2}$. Se usa $\sin(180^\circ - \theta) = \sin\theta$.

### 2. Seno y coseno en triángulos pegados
En la figura, $BC = r$, $DB = s$, $AD = t$, $AB = x$, $\angle DCB = \alpha$ y $\angle BDC = \beta$. (a) Exprese $s$ en función de $r$, $\sin\alpha$ y $\sin\beta$. (b) Exprese $x$ en función de $s$, $t$ y $\cos\beta$. (c) Si $\beta = 2\alpha = \frac{\pi}{3}$ y $r = t = \sqrt 3$, calcule $x$.

![Triángulo ABC con el punto D sobre AC](adjuntos/Tri%C3%A1ngulo%20ABC%20con%20el%20punto%20D%20sobre%20AC.png)

> [!example]- Transcripción de la figura
> Triángulo $ABC$ alargado, con $C$ arriba, $B$ a la derecha y $A$ abajo a la izquierda. El punto $D$ está sobre el lado $AC$; el segmento $DB$ es horizontal y $BC$ vertical. Rótulos: $\alpha$ en el vértice $C$ (entre $CD$ y $CB$), $\beta$ en $D$ (entre $DC$ y $DB$), $r = BC$, $s = DB$, $t = AD$ y $x = AB$.

> [!example]- Solución
> (a) En el triángulo $DBC$, el lado $s = DB$ es opuesto a $\alpha$ y $r = BC$ es opuesto a $\beta$. Teorema del seno: $\frac{\sin\alpha}{s} = \frac{\sin\beta}{r}$, así que $s = \frac{r\sin\alpha}{\sin\beta}$.
> (b) En el triángulo $ADB$, el ángulo en $D$ es $\angle ADB = 180^\circ - \beta$ (suplementario de $\beta$). Teorema del coseno: $x^2 = s^2 + t^2 - 2st\cos(180^\circ - \beta) = s^2 + t^2 + 2st\cos\beta$, así que $x = \sqrt{s^2 + t^2 + 2st\cos\beta}$.
> (c) $s = \frac{\sqrt 3 \cdot \sin\frac{\pi}{6}}{\sin\frac{\pi}{3}} = \frac{\sqrt 3/2}{\sqrt 3/2} = 1$, y $x = \sqrt{1 + 3 + 2\sqrt 3 \cdot \frac{1}{2}} = \sqrt{4 + \sqrt 3}$.

### 3. La altura de un cerro
Un teleférico va desde $A$ hasta la cima $P$ de un cerro. $A$ está a $a$ metros del pie $B$ del cerro; el ángulo de elevación de $P$ visto desde $A$ es $\alpha$, y visto desde $B$ es $3\alpha$. Demuestre que la altura del cerro es $H = \dfrac{a\sin(3\alpha)}{2\cos\alpha}$.

![Teleférico desde A hasta la cima P](adjuntos/Telef%C3%A9rico%20desde%20A%20hasta%20la%20cima%20P.png)

> [!example]- Transcripción de la figura
> Dibujo de un cerro con la cima $P$ a la derecha. En el suelo, el punto $A$ a la izquierda y el pie $B$ del cerro, separados por la distancia $a$. Un cable rojo con una cabina va de $A$ a $P$ formando el ángulo $\alpha$ con el suelo; la ladera $BP$ forma el ángulo $3\alpha$. Una línea vertical discontinua desde $P$ marca la altura $H$.

> [!example]- Solución
> ![Triángulos auxiliares del teleférico](adjuntos/Tri%C3%A1ngulos%20auxiliares%20del%20telef%C3%A9rico.png)
>
> > [!example]- Transcripción de la figura
> > Figura 1: el triángulo $ABP$ con $\alpha$ en $A$, $\beta$ en $B$ (interior) junto a $3\alpha$ (exterior, sobre la prolongación discontinua del suelo) y $\gamma$ en $P$; la base $AB$ mide $a$. Figura 2: el triángulo rectángulo $BQP$, con hipotenusa $BP = \ell$, ángulo $3\alpha$ en $B$, cateto vertical $PQ = H$ y ángulo recto en $Q$.
>
> En $B$, el ángulo interior es $\beta = \pi - 3\alpha$ (suplementario de $3\alpha$). En el triángulo $ABP$: $\alpha + (\pi - 3\alpha) + \gamma = \pi$, así que $\gamma = 2\alpha$. Teorema del seno con $\ell = BP$ (opuesto a $\alpha$) y $a$ (opuesto a $\gamma$):
> $$\frac{\sin\alpha}{\ell} = \frac{\sin 2\alpha}{a} \implies \ell = \frac{a\sin\alpha}{\sin 2\alpha}.$$
> En el triángulo rectángulo $BQP$: $H = \ell\sin 3\alpha = \frac{a\sin\alpha\sin 3\alpha}{2\sin\alpha\cos\alpha} = \frac{a\sin 3\alpha}{2\cos\alpha}$, usando $\sin 2\alpha = 2\sin\alpha\cos\alpha$.

### 4. Dos observadores a lados opuestos
Desde $A$ se ve la punta de una torre con elevación de $45^\circ$; desde $B$, a $20$ m de $A$ y al otro lado de la torre, con elevación de $15^\circ$. Determine la altura de la torre.

> [!example]- Solución
> Sea $h$ la altura y $x$ la distancia de $A$ al pie. Entonces $\tan 45^\circ = \frac{h}{x}$ da $h = x$, y $\tan 15^\circ = \frac{h}{20 - h}$. Con $\tan 15^\circ = \tan(45^\circ - 30^\circ) = \frac{\sqrt 3 - 1}{\sqrt 3 + 1}$:
> $$(\sqrt 3 - 1)(20 - h) = (\sqrt 3 + 1)h \implies 20(\sqrt 3 - 1) = 2\sqrt 3\, h \implies h = \frac{10(\sqrt 3 - 1)}{\sqrt 3} = 10 - \frac{10\sqrt 3}{3} \approx 4{,}23 \text{ m}.$$

### 5. Un caso que parece ambiguo
En un triángulo $ABC$, $|AB| = 5\sqrt 2$, $|BC| = 5$ y $\angle BCA = 45^\circ$. Encuentre todos los valores posibles de $\angle CAB$ y de $|AC|$.

> [!example]- Solución
> Con la notación usual ($a = 5$ opuesto a $\alpha$, $c = 5\sqrt 2$ opuesto a $\gamma = 45^\circ$): $\sin\alpha = \frac{a\sin\gamma}{c} = \frac{1}{2}$, así que $\alpha = 30^\circ$ o $150^\circ$. La segunda es imposible porque $150^\circ + 45^\circ > 180^\circ$. Para $b = |AC|$, el teorema del coseno $c^2 = a^2 + b^2 - 2ab\cos\gamma$ da $b^2 - 5\sqrt 2\, b - 25 = 0$, cuya raíz positiva es $b = \frac{5\sqrt 2 + 5\sqrt 6}{2} = \frac{5\sqrt 2(1 + \sqrt 3)}{2}$.

### 6. Dos lados y el ángulo comprendido
En el triángulo $ABC$, $a = 2$, $b = 1$ y $\gamma = 60^\circ$. Determine $\beta$.

> [!example]- Solución
> Coseno: $c^2 = 4 + 1 - 2 \cdot 2 \cdot 1 \cdot \frac{1}{2} = 3$, así que $c = \sqrt 3$. Seno: $\sin\beta = \frac{b\sin\gamma}{c} = \frac{\sqrt 3/2}{\sqrt 3} = \frac{1}{2}$, y como $b$ es el lado menor, $\beta$ es agudo: $\beta = 30^\circ$ (el triángulo resulta rectángulo en $A$).

## Preguntas de repaso

> [!question]- En el ejercicio 2, ¿por qué aparece $+2st\cos\beta$ en vez de $-2st\cos\beta$?
> Porque el ángulo del triángulo $ADB$ en $D$ es $180^\circ - \beta$, y $\cos(180^\circ - \beta) = -\cos\beta$.

> [!question]- ¿Cómo se sabe en el ejercicio 6 que $\beta$ no es $150^\circ$?
> Al ángulo mayor se opone el lado mayor; $b = 1$ es el menor, así que $\beta$ es el menor de los tres ángulos y no puede ser obtuso.

> [!question]- ¿Qué relación hay entre un ángulo exterior de un triángulo y los interiores?
> El exterior es suplementario del interior adyacente, y por lo tanto igual a la suma de los otros dos interiores: en el teleférico, $3\alpha = \alpha + \gamma$, de donde $\gamma = 2\alpha$.
