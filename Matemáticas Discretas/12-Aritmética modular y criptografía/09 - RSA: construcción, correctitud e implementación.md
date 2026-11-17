---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/criptografia
  - origen/complemento
prerrequisitos:
  - "[[05 - Inversos modulares y congruencias lineales]]"
  - "[[07 - Pequeño teorema de Fermat]]"
  - "[[08 - Criptografía y cifrado del César]]"
---

# RSA: construcción, correctitud e implementación

RSA (Rivest, Shamir, Adleman) es el sistema de clave pública más usado. Se apoya en una asimetría: multiplicar dos primos es fácil, pero factorizar el producto es muy difícil, y el pequeño teorema de Fermat garantiza que el descifrado deshace al cifrado.

## El algoritmo

1. Elegir dos primos distintos $P$ y $Q$.
2. Calcular $N = PQ$ y $\varphi(N) = (P-1)(Q-1)$.
3. Elegir $e$ y $d$ con $ed \equiv 1 \pmod{\varphi(N)}$ (inversos módulo $\varphi(N)$).
4. Definir $E(M) = M^e \bmod N$ y $D(M) = M^d \bmod N$.

La **clave pública** es $(e, N)$ y se publica; la **clave privada** es $(d, N)$. Los mensajes son números $M \in \{0, \dots, N-1\}$.

**Ejemplo:** $P = 7$, $Q = 11$, $e = 13$, $d = 37$. Entonces $N = 77$, $\varphi(N) = 6 \cdot 10 = 60$ y $13 \cdot 37 = 481 = 8 \cdot 60 + 1$. Con $M = 5$: $E(5) = 5^{13} \bmod 77 = 26$ y $D(26) = 26^{37} \bmod 77 = 5$.

## Exponenciación modular sin calculadora

$5^{13}$ es demasiado grande para calcularlo entero, pero se puede reducir módulo $77$ tras cada multiplicación. Con **cuadrados sucesivos**: $5^2 = 25$, $5^4 = 625 \equiv 9$, $5^8 \equiv 81 \equiv 4$. Como $13 = 8 + 4 + 1$,

$$5^{13} \equiv 5^8 \cdot 5^4 \cdot 5 \equiv 4 \cdot 9 \cdot 5 = 180 \equiv 26 \pmod{77}.$$

Del mismo modo $37 = 32 + 4 + 1$ y $26^2 \equiv 60$, $26^4 \equiv 58$, $26^8 \equiv 53$, $26^{16} \equiv 37$, $26^{32} \equiv 60$; entonces $26^{37} \equiv 60 \cdot 58 \cdot 26 \equiv 15 \cdot 26 = 390 \equiv 5$. Con exponente de $k$ bits bastan unas $2k$ multiplicaciones, no $2^k$.

```python
def potencia_mod(m, e, n):
    r = 1
    m %= n
    while e:
        if e & 1: r = r * m % n
        m = m * m % n
        e >>= 1
    return r
```

## Correctitud: $D(E(M)) = M$

> [!tip] Teorema (RSA)
> Para todo $M \in \{0, \dots, N-1\}$, $D(E(M)) = M$.

Se tiene $D(E(M)) = (M^e \bmod N)^d \bmod N = M^{ed} \bmod N$, y hay que probar $M^{ed} \equiv M \pmod{PQ}$. Como $P$ y $Q$ son coprimos, por el lema del [[06 - Teorema chino del resto]] basta probarlo módulo $P$ y módulo $Q$. Módulo $P$ hay dos casos:

- **$P \mid M$:** ambos lados valen $0$ módulo $P$.
- **$P \nmid M$:** $ed = k(P-1)(Q-1) + 1$ y, por Fermat, $M^{P-1} \equiv 1 \pmod P$. Entonces
$$M^{ed} = \left(M^{P-1}\right)^{k(Q-1)} \cdot M \equiv 1 \cdot M = M \pmod P.$$

El argumento para $Q$ es idéntico. Por ello $E$ y $D$ son inversas.

## Implementación

Hay tres problemas que resolver eficientemente:

1. **Generar primos $P$ y $Q$:** requiere tests de primalidad, fuera del alcance de este curso.
2. **Generar $e$ y $d$:** se elige $e$ al azar hasta que $\operatorname{MCD}(e, \varphi(N)) = 1$ y se calcula $d = s \bmod \varphi(N)$, donde $(s, t)$ es la salida de Euclides extendido para $(e, \varphi(N))$.
3. **Calcular $E$ y $D$:** exponenciación modular por cuadrados sucesivos.

```text
GenED(P, Q):
    N <- P * Q
    e <- entero aleatorio
    mientras MCD(e, phi(N)) > 1: e <- entero aleatorio
    (s, t) <- EuclidesExtendido(e, phi(N))
    d <- s mod phi(N)
    retornar (e, d)
```

Con $P = 7$, $Q = 11$ y $e = 7$ resulta $d = 43$: $7 \cdot 43 = 301 = 5 \cdot 60 + 1$. Cifrar $M = 5$ da $5^7 \bmod 77 = 47$ y descifrar $47^{43} \bmod 77$ devuelve $5$.

## RSA en la práctica

La seguridad depende de que factorizar $N = PQ$ no se sabe hacer en tiempo polinomial. Las claves reales usan $N$ de 2048 bits (unos 600 dígitos) y se suele fijar $e = 65537 = 2^{16} + 1$, que hace barato el cifrado. Las llaves públicas se autentican con certificados.

> [!warning] Entregar el $\varphi(N)$ rompe el sistema
> Quien conoce $\varphi(N)$ calcula $d$ con Euclides extendido. Por eso $P$ y $Q$ (de los que se deduce $\varphi(N)$) deben mantenerse secretos.

## Preguntas de repaso

> [!question]- ¿Por qué $e$ debe ser coprimo con $\varphi(N)$?
> Porque $d$ es el inverso de $e$ módulo $\varphi(N)$, y solo existe si $\operatorname{MCD}(e, \varphi(N)) = 1$.

> [!question]- ¿Dónde se usa el teorema de Fermat en la prueba de correctitud?
> Para reducir $M^{k(P-1)(Q-1)}$ a $1$ módulo $P$ (y análogamente módulo $Q$) cuando $P \nmid M$.

> [!question]- ¿Por qué se reduce módulo $N$ tras cada multiplicación al calcular $M^e$?
> Para que los números no crezcan; la congruencia respeta el producto, así que el resultado final no cambia.

> [!question]- Con $P = 5$, $Q = 11$ y $e = 3$, ¿cuánto vale $d$?
> $\varphi(N) = 40$ y $3 \cdot 27 = 81 = 2 \cdot 40 + 1$, luego $d = 27$.
