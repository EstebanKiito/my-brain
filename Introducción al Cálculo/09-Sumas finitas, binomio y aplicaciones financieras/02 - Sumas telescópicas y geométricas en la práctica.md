---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - origen/complemento
prerrequisitos:
  - "[[01 - Notación sigma y sumas de potencias]]"
---

# Sumas telescópicas y geométricas en la práctica

Dos técnicas resuelven casi todas las sumas que no son de potencias: reconocer una **suma telescópica**, donde los términos se cancelan en cadena, y aplicar la fórmula de la **suma geométrica**. En cada ejercicio, el trabajo está en reescribir el término general para que aparezca la estructura. (La teoría de fondo, con otros ejemplos, está en [[02 - Sumas telescópicas|Introducción al Álgebra]].)

## La propiedad telescópica

> [!tip] Suma telescópica
> $\displaystyle \sum_{k=1}^{n}(a_k - a_{k-1}) = a_n - a_0$, y en general $\displaystyle \sum_{k=m}^{n}(a_k - a_{k+1}) = a_m - a_{n+1}$.

Al desarrollar, cada $a_k$ intermedio aparece una vez con $+$ y otra con $-$ y se anula; quedan solo los extremos. El procedimiento es: **escribir el término como $a_k - a_{k+1}$** (o $a_{k+1} - a_k$) con una sucesión $\{a_k\}$ adecuada.

**Fracciones parciales: $\sum \tfrac{1}{k(k + 1)}$ (clase 19).** Como $\tfrac{1}{k(k+1)} = \tfrac{1}{k} - \tfrac{1}{k+1}$, con $a_k = \tfrac{1}{k}$:
$$\sum_{k=1}^{n}\frac{1}{k(k + 1)} = a_1 - a_{n+1} = 1 - \frac{1}{n + 1} = \frac{n}{n + 1}.$$

**Factoriales: $\sum_{k=0}^{n} k\cdot k!$ (clase 19).** Se escribe $k\cdot k! = [(k + 1) - 1]\,k! = (k + 1)! - k!$, con $a_k = k!$:
$$\sum_{k=0}^{n} k\,k! = a_{n+1} - a_0 = (n + 1)! - 1.$$

**Con una pista (I7, 2023-1): $\sum_{k=1}^{n}(k^2 + 1)\,k!$.** Se verifica la sugerencia $(k^2 + 1)k! = k(k + 1)! - (k - 1)k!$, porque $k(k + 1)! = k(k + 1)k!$ y $k(k + 1) - (k - 1) = k^2 + 1$. Con $a_k = (k - 1)k!$ queda $a_{k+1} - a_k$ y
$$\sum_{k=1}^{n}(k^2 + 1)k! = a_{n+1} - a_1 = n(n + 1)! - 0 = n(n + 1)!.$$

**Con factoriales y cociente (Guía 9): $\sum \tfrac{k}{(k+1)!}$.** $\tfrac{k}{(k + 1)!} = \tfrac{(k + 1) - 1}{(k + 1)!} = \tfrac{1}{k!} - \tfrac{1}{(k + 1)!}$, y la suma vale $1 - \tfrac{1}{(n + 1)!}$.

**Con potencias de $2$ (Guía 9): $\sum \tfrac{k + 2}{k(k + 1)2^k}$.** Con $a_k = \tfrac{1}{k\,2^{k-1}}$ se tiene $a_k - a_{k+1} = \tfrac{2(k + 1) - k}{k(k + 1)2^k} = \tfrac{k + 2}{k(k + 1)2^k}$, luego la suma es $a_1 - a_{n+1} = 1 - \dfrac{1}{(n + 1)2^n}$.

**Con logaritmos (Examen, 2023-1): $\sum_{k=1}^{n}\ln\!\left(1 + \tfrac{1}{k}\right)$.** $\ln\tfrac{k + 1}{k} = \ln(k + 1) - \ln k$, con $c_k = \ln k$: la suma es $c_{n+1} - c_1 = \ln(n + 1)$.

## Suma geométrica

> [!tip] Suma geométrica
> Para $r \neq 1$: $\ 1 + r + r^2 + \dots + r^n = \dfrac{1 - r^{n+1}}{1 - r}$.

*Deducción.* Con $S = 1 + r + \dots + r^n$, se tiene $rS = r + r^2 + \dots + r^{n+1}$; restando, $S - rS = 1 - r^{n+1}$, es decir $S(1 - r) = 1 - r^{n+1}$. $\blacksquare$

**Ejemplo (clase 19): $\sum_{k=1}^{n}\tfrac{3^{k+1}}{4^k}$.** Se escribe $3\sum_{k=1}^{n}\left(\tfrac{3}{4}\right)^k = 3\left[\sum_{k=0}^{n}\left(\tfrac{3}{4}\right)^k - 1\right]$ y con $r = \tfrac{3}{4}$:
$$3\left[\frac{1 - (3/4)^{n+1}}{1/4} - 1\right] = 3\left[4 - 4\left(\tfrac{3}{4}\right)^{n+1} - 1\right] = 9 - 12\left(\tfrac{3}{4}\right)^{n+1}.$$

**Suma $1 - \tfrac{1}{2} + \tfrac{1}{4} - \dots - \tfrac{1}{512}$ (Guía 9).** Son los términos $\left(-\tfrac{1}{2}\right)^k$ con $k = 0, \ldots, 9$: $\dfrac{1 - (-1/2)^{10}}{1 + 1/2} = \dfrac{1023/1024}{3/2} = \dfrac{341}{512}$.

**Una suma con un factor $i$ (Guía 9): $\sum_{i=1}^{n} i\,r^i$.** Para $r \neq 1$ se obtiene $\dfrac{r\left(1 - (n + 1)r^n + n r^{n+1}\right)}{(1 - r)^2}$ (por ejemplo, restando $r\,T$ a $T = \sum i r^i$ queda una suma geométrica). Para $r = 1$ es $\tfrac{n(n + 1)}{2}$.

> [!warning] Cuidado con los índices
> La suma geométrica clásica empieza en $k = 0$. Si parte en $k = 1$ hay que restar el término $k = 0$ (que vale $1$), como en el ejemplo de $\tfrac{3^{k+1}}{4^k}$.

## Preguntas de repaso

> [!question]- ¿Qué se busca para ver que una suma es telescópica?
> Escribir el término general como $a_k - a_{k+1}$ (o $a_{k+1} - a_k$) con una sucesión $a_k$; entonces solo sobreviven los extremos.

> [!question]- Calcule $\sum_{k=1}^{n}\left(\sqrt{k + 1} - \sqrt{k}\right)$.
> Con $a_k = \sqrt{k}$ es telescópica: $\sqrt{n + 1} - 1$.

> [!question]- ¿Cuánto vale $\sum_{k=0}^{9} 2^k$?
> $\frac{1 - 2^{10}}{1 - 2} = 1023$.

> [!question]- ¿Por qué falla $\sum_{k=1}^{n} r^k = \frac{1 - r^{n+1}}{1 - r}$ si se usa tal cual?
> Esa fórmula incluye el término $k = 0$ (que vale $1$); la suma desde $k = 1$ es $\frac{1 - r^{n+1}}{1 - r} - 1 = \frac{r - r^{n+1}}{1 - r}$.
