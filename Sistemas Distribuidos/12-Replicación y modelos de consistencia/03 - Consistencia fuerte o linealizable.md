---
ramo: "Sistemas Distribuidos"
tema: "Replicación y modelos de consistencia"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[02 - Consistencia secuencial]]"
---

# Consistencia fuerte o linealizable

La consistencia secuencial admite cualquier orden que todos compartan, aunque contradiga el reloj. La **consistencia fuerte**, o **linealizabilidad** (Herlihy y Wing, 1986), agrega el **tiempo real**: el sistema debe comportarse como una única copia en la que cada operación ocurre en un instante preciso. Es lo que un usuario espera intuitivamente, y lo más caro de garantizar.

## Definición

> [!tip] Regla
> Cada operación debe parecer que tiene **efecto instantáneo** en algún momento entre su **inicio** y su **fin**. Al completarse un write, se propaga de inmediato a las demás réplicas: cualquier lectura posterior lo ve.

## Ejemplos

![Consistencia fuerte con una sola secuencia válida](adjuntos/Consistencia%20fuerte%20con%20una%20sola%20secuencia%20v%C3%A1lida.png)

> [!example]- Transcripción de la imagen
> A ejecuta $W_A(x)=1$, más tarde $W_A(y)=1$ y luego $R_A(x)$; F ejecuta $W_F(y)=2$ y $W_F(x)=2$ (entre las dos de A) y luego $R_F(y)$. Las operaciones no se superponen en el tiempo: "Solo 1 secuencia válida de writes".

Con las operaciones separadas en el tiempo, de las 6 secuencias que permitía la consistencia secuencial solo queda **una**: la del reloj.

![Consistencia fuerte con dos secuencias válidas](adjuntos/Consistencia%20fuerte%20con%20dos%20secuencias%20v%C3%A1lidas.png)

> [!example]- Transcripción de la imagen
> Ahora $W_A(x)=1$ y $W_F(y)=2$ se superponen en el tiempo (líneas punteadas). "Solo 2 secuencias válidas de writes: partir con $W_A(x)=1$ o partir con $W_F(y)=2$."

Cuando dos operaciones se **superponen**, cualquiera de las dos puede haber ocurrido primero, así que ambos órdenes son válidos.

## Secuencial pero no linealizable

![Secuencial pero no linealizable](adjuntos/Secuencial%20pero%20no%20linealizable.png)

> [!example]- Transcripción de la imagen
> A hace $W_A(x)=1$, que termina en $T_1$, y luego $R_A(x)\rightarrow 1$. F, en $T_2$ (con $T_1 < T_2$), lee $R_F(x)\rightarrow 0$ y después $R_F(x)\rightarrow 1$.

- **Es secuencialmente consistente:** existe la secuencia $R_F(x)\rightarrow 0,\ W_A(x)=1,\ R_F(x)\rightarrow 1,\ R_A(x)\rightarrow 1$ (encontrada también por el verificador de fuerza bruta).
- **No es linealizable:** el write terminó en $T_1$ y la lectura de F empezó después, en $T_2$, así que debió ver 1. Que vea 0 significa que la propagación de A aún no había llegado a F.

## Fuerte frente a secuencial

| | Secuencial | Fuerte (linealizable) |
|---|---|---|
| Orden que todos ven | Uno cualquiera, igual para todos | El del tiempo real |
| Respeta | El orden de cada proceso | El orden de cada proceso **y** el tiempo real |
| Relación | – | Toda ejecución linealizable es secuencial, no al revés |

> [!warning] El costo de la consistencia fuerte
> Para que una lectura siempre vea el último write, cada escritura debe llegar a todas las réplicas antes de terminar. Con la latencia de una red, garantizarlo es muy difícil y lento.

## Preguntas de repaso

> [!question]- ¿Por qué toda ejecución linealizable es secuencialmente consistente?
> Porque el orden del tiempo real es una secuencia válida que todos comparten y que respeta el orden de cada proceso, que es justo lo que pide la consistencia secuencial.

> [!question]- ¿Cuándo la consistencia fuerte admite más de un orden?
> Cuando dos operaciones se superponen en el tiempo: como cada una pudo tener efecto en cualquier instante de su intervalo, ambos órdenes son válidos.

> [!question]- En el ejemplo de $T_1 < T_2$, ¿qué tendría que haber leído F para que fuera linealizable?
> 1 en ambas lecturas, porque las dos empezaron después de que terminó el write de A.
