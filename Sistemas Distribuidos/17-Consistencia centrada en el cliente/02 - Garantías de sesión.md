---
ramo: "Sistemas Distribuidos"
tema: "Consistencia centrada en el cliente"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Consistencia centrada en el cliente]]"
---

# Garantías de sesión

Cada una de las cuatro garantías de sesión se define con una frase precisa, se reconoce en un diagrama de dos réplicas y se implementa con alguna variante de **tokens de sesión** o **vectores de versión**. En los diagramas, el cliente A puede leer o escribir en cualquiera de las dos réplicas.

## Monotonic reads

> [!tip] Definición
> Si un cliente lee $X_z$, cualquier lectura posterior del mismo cliente devuelve $X_z$ o una versión $X_d$ tal que $W(X_z \rightarrow X_d)$.

![Monotonic reads con dos réplicas](adjuntos/Monotonic%20reads%20con%20dos%20r%C3%A9plicas.png)

> [!example]- Transcripción de la imagen
> (a) ✅: A escribe y lee $X_1$ en la réplica 1; en la réplica 2, B escribe $W_B(X_1 \rightarrow X_2)$ y A lee $X_2$. (b) ❌: B escribe $W_B(X_1 \mid X_2)$, sin conocer $X_1$, y A lee $X_2$ en la réplica 2: una versión que no deriva de lo que ya había visto.

![Monotonic reads cumplido y violado](adjuntos/Monotonic%20reads%20cumplido%20y%20violado.png)

> [!example]- Transcripción de la imagen
> El mismo ejemplo, junto con la definición de las garantías y la intuición "una vez que has visto algo, no esperarías ver una versión anterior o inconsistente a lo que viste recién".

**Implementación:** un balanceador de carga usa un token de sesión (por ejemplo, un session ID) para dirigir las lecturas del cliente a la misma réplica, o a una con una versión igual o más reciente.

## Monotonic writes

> [!tip] Definición
> Si un cliente escribe $X_z$, cualquier escritura posterior del mismo cliente debe ser una versión $X_d$ tal que $W(X_z \rightarrow X_d)$.

![Monotonic writes en cuatro casos](adjuntos/Monotonic%20writes%20en%20cuatro%20casos.png)

> [!example]- Transcripción de la imagen
> A escribe $X_1$ en la réplica 1. (a) ✅: en la réplica 2, $W_B(X_1 \rightarrow X_2)$ y luego $W_A(X_2 \rightarrow X_3)$. (b) ❌: $W_B(X_1 \mid X_2)$ y $W_A(X_1 \mid X_3)$: la segunda escritura de A no conoce la primera. (c) ❌: $W_B(X_1 \mid X_2)$ y $W_A(X_2 \rightarrow X_3)$: A escribe sobre una versión que no deriva de su $X_1$. (d) ✅: $W_B(X_1 \mid X_2)$ y $W_A(X_1 \rightarrow X_3)$: A sí construye sobre su propia escritura.

**Implementación:** el cliente no envía la siguiente escritura hasta recibir confirmación de la anterior (lo que puede implicar esperar que se propague), o usa tokens con vectores de versión para que el servidor solo aplique la escritura si ya tiene las anteriores.

## Read your writes

> [!tip] Definición
> Si un cliente escribe $X_z$, cualquier lectura posterior del mismo cliente devuelve $X_z$ o una versión $X_d$ tal que $W(X_z \rightarrow X_d)$.

![Read your writes cumplido y violado](adjuntos/Read%20your%20writes%20cumplido%20y%20violado.png)

> [!example]- Transcripción de la imagen
> A escribe $X_1$ en la réplica 1. (a) ✅: en la réplica 2, $W_B(X_1 \rightarrow X_2)$ y A lee $X_2$, que incluye su cambio. (b) ❌: $W_B(X_1 \mid X_2)$ y A lee $X_2$, una versión que ignora su propia escritura.

**Implementación:** un token de sesión redirige las lecturas solo a servidores que ya tienen la escritura propagada, o se espera la confirmación de la escritura.

## Writes follow reads

> [!tip] Definición
> Si un cliente lee $X_z$, cualquier escritura posterior del mismo cliente debe ser una versión $X_d$ tal que $W(X_z \rightarrow X_d)$.

![Writes follow reads cumplido y violado](adjuntos/Writes%20follow%20reads%20cumplido%20y%20violado.png)

> [!example]- Transcripción de la imagen
> A escribe $X_1$ y B lee $X_1$ en la réplica 1. (a) ✅: en la réplica 2, $W_C(X_1 \rightarrow X_2)$ y luego $W_B(X_2 \rightarrow X_3)$. (b) ❌: $W_C(X_1 \mid X_2)$ y $W_B(X_2 \rightarrow X_3)$: la escritura de B se aplica sobre una versión que no deriva de lo que leyó.

**Implementación:** cada lectura devuelve un identificador de causalidad (por ejemplo, un vector de versión), y la escritura siguiente lo incluye para que solo se aplique en nodos que ya tienen esa versión o una posterior.

## Pregunta de aplicación

![Pregunta de garantías de sesión del cliente A](adjuntos/Pregunta%20de%20garant%C3%ADas%20de%20sesi%C3%B3n%20del%20cliente%20A.png)

> [!example]- Transcripción de la imagen
> Réplica 1: $W_A(X_1)$, $R_A(X_1)$, $R_B(X_1)$, y más tarde $R_A(X_1)$, $R_A(X_4)$, $R_B(X_4)$. Réplica 2: $W_B(X_1 \mid X_2)$, $R_B(X_1)$, $W_B(X_1 \rightarrow X_3)$, $R_A(X_3)$, $W_A(X_3 \rightarrow X_4)$, $R_A(X_4)$. Para el cliente A: monotonic reads ❌ (lee $X_3$ en una réplica y luego vuelve a leer una versión pasada); read your writes ❌ (escribe $X_4$ pero después no lee esa versión); monotonic writes ✅ (sus escrituras muestran una progresión); writes follow reads ✅ (escribe siempre en base a lo que vio).

> [!warning] Leer con el tiempo, no con la réplica
> Las garantías se evalúan sobre la secuencia de operaciones **del cliente** en el tiempo, aunque cada una ocurra en una réplica distinta.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre monotonic writes y writes follow reads?
> Monotonic writes relaciona las escrituras del cliente entre sí (cada una se basa en la anterior). Writes follow reads relaciona una escritura con lo que el cliente **leyó** antes.

> [!question]- ¿Cómo implementa un balanceador monotonic reads?
> Con un token de sesión que dirige las lecturas del cliente siempre a la misma réplica, o a una que tenga una versión igual o más nueva que la última que vio.

> [!question]- Publicas un comentario, recargas y no aparece. ¿Qué garantía falló y cómo se evitaría?
> Read your writes. Se evita dirigiendo tus lecturas a una réplica que ya tenga tu escritura, o esperando su confirmación antes de mostrar la página.
