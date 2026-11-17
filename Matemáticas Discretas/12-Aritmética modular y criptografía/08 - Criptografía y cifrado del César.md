---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - discretas/criptografia
  - origen/complemento
prerrequisitos:
  - "[[02 - Congruencias módulo n y aritmética en Z_n]]"
---

# Criptografía y cifrado del César

La **criptografía** estudia cómo enviar y recibir mensajes en privado. Los cifrados clásicos usan aritmética modular de forma muy simple; sus límites explican por qué hicieron falta los sistemas de clave pública.

## El cifrado del César

Julio César protegía su correspondencia desplazando cada letra tres posiciones en el alfabeto, de modo que la A se escribe D, la B se escribe E y así sucesivamente, "dando la vuelta" al final.

![Cifrado del César: cada letra se reemplaza por la que está tres posiciones después](adjuntos/Cifrado%20del%20César%20desplazamiento%20de%20tres%20letras.png)

> [!example]- Transcripción de la imagen
> - Dos filas de letras. La fila superior muestra "... A B C D E F G H I ..." con la E resaltada; la inferior, "X Y Z A B C D E F ..." con la B resaltada.
> - Flechas curvas negras unen D, E y F de arriba con A, B y C de abajo: cada letra del texto se reemplaza por otra desplazada en el mismo número de lugares, y las letras X, Y, Z reaparecen al comienzo (vuelta del alfabeto).
> - El pie dice que Julio César usaba este método para su correspondencia privada.

Formalmente, con el alfabeto español de 27 letras numeradas $a = 0, b = 1, \dots, z = 26$ (la $ñ$ es la 14):

$$C = (M + 3) \bmod 27, \qquad M = (C - 3) \bmod 27.$$

**Ejemplo:** cifrar "holamundo". Los números son $h = 7$, $o = 15$, $l = 11$, $a = 0$, $m = 12$, $u = 21$, $n = 13$, $d = 3$, $o = 15$; sumando $3$ y reduciendo módulo $27$ se obtiene $10, 18, 14, 3, 15, 24, 16, 6, 18$, es decir **"krñdoxpgr"**.

## Versión general y vocabulario

Con un desplazamiento cualquiera $d$, $C = (M + d) \bmod 27$. Se usa el vocabulario de Alice y Bob: Alice quiere enviar a Bob el **texto plano** $M$; envía el **texto cifrado** $C$; ambos comparten la **llave** $d$.

Bob recupera el mensaje con $M = (C - d) \bmod 27$. Que esto funciona se ve reduciendo módulo $27$: $((M + d) \bmod 27 - d) \bmod 27 = (M + d - d) \bmod 27 = M \bmod 27 = M$, porque suma y resta respetan la congruencia.

## Por qué no basta

El cifrado del César tiene problemas serios:

- **Pocas llaves:** solo hay $27$ desplazamientos posibles; se prueban todos en un instante.
- **Llave compartida:** Bob necesita $d$, y enviársela a Bob por el mismo canal inseguro obligaría a protegerla con otra llave, una regresión sin fin.
- **Un solo secreto:** quien conozca la llave puede tanto cifrar como descifrar.

Los sistemas de **clave pública** resuelven el problema del intercambio de llaves usando dos funciones relacionadas pero distintas.

## Criptografía asimétrica: la idea

Se tienen dos funciones $E$ (encriptar) y $D$ (desencriptar) tales que:

- $D(E(M)) = M$ para todo mensaje $M$.
- $E$ por sí sola no sirve para desencriptar ($E(E(M)) \ne M$).
- Aunque $E$ y $D$ estén relacionadas, es **muy difícil** obtener $D$ a partir de $E$.

Entonces $E$ se publica (cualquiera puede escribir a Bob) y solo Bob guarda $D$. El sistema más usado es RSA, en [[09 - RSA: construcción, correctitud e implementación]].

## Preguntas de repaso

> [!question]- ¿Por qué el descifrado del César resta $d$ módulo $27$?
> Porque cifrar suma $d$ y restar $d$ deshace la suma; el módulo $27$ garantiza que el resultado vuelva a ser una letra.

> [!question]- Cifre "sol" con desplazamiento $3$ (alfabeto de 27 letras).
> $s = 19 \to 22 = v$, $o = 15 \to 18 = r$, $l = 11 \to 14 = ñ$: "vrñ".

> [!question]- ¿Por qué el César es inseguro aunque el atacante no conozca $d$?
> Porque hay solo $27$ llaves posibles y basta probarlas todas.

> [!question]- ¿Qué problema resuelve la criptografía de clave pública?
> El del intercambio de llaves: no hace falta compartir un secreto previo, pues $E$ es pública y solo $D$ se guarda en secreto.
