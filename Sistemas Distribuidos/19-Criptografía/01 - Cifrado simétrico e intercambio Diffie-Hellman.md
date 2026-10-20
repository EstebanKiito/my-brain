---
ramo: "Sistemas Distribuidos"
tema: "Criptografía"
tags:
  - sd/seguridad
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - Métodos de ataque y medidas de seguridad]]"
---

# Cifrado simétrico e intercambio Diffie-Hellman

El cifrado oculta los mensajes para que un espía que los captura no pueda entenderlos, y es la base de la autenticación. Su forma más rápida usa una sola clave compartida, pero eso deja un problema: ¿cómo acuerdan dos nodos esa clave si el canal está vigilado? **Diffie-Hellman** responde esa pregunta.

## Conceptos básicos

| Término | Significado |
|---|---|
| **Texto plano** | El mensaje original, legible |
| **Texto cifrado** | El mensaje transformado, ilegible sin la clave correcta |
| **Llave** | Parámetro secreto que usa el algoritmo |
| **Encriptar** | Transformar texto plano en cifrado |
| **Desencriptar** | El proceso inverso |

## Cifrado simétrico

Usa **la misma clave secreta** para encriptar y desencriptar; también se llama **criptografía de clave secreta**. El nodo A y el nodo K acuerdan una clave $K_{ak}$; A envía `Encriptar(mensaje, K_ak)` y K aplica `Desencriptar(mensaje, K_ak)`.

| Algoritmo | Estado |
|---|---|
| **AES** | El estándar actual más adoptado; claves de 128, 192 o 256 bits |
| **DES** | Antiguo estándar de EE. UU.; inseguro por su clave de 56 bits, vulnerable a fuerza bruta. **3DES** (DES aplicado tres veces) también fue retirado |
| **IDEA** | Sucesor de DES, con clave de 128 bits |

> [!warning] El desafío principal
> Distribuir la clave secreta inicial de forma segura: si un tercero la intercepta cuando A y K la intercambian por primera vez, puede leer todo lo que viene después.

## Diffie-Hellman

Protocolo de **Whitfield Diffie y Martin Hellman** (1976): dos partes establecen una **clave secreta compartida** por un canal inseguro **sin transmitirla nunca**. Solo viajan datos públicos, construidos de modo que, combinados con un número secreto que cada parte conoce, ambas llegan al mismo valor. El espía ve los datos públicos, pero no puede derivar la clave sin uno de los secretos.

![Diffie-Hellman con colores](adjuntos/Diffie-Hellman%20con%20colores.png)

> [!example]- Transcripción de la imagen
> Con colores: A mezcla su secreto $K_a$ con el color público $P$ y obtiene $A$; K mezcla su secreto $K_k$ con $P$ y obtiene $K$. Se intercambian $A$ y $K$ por el canal. El espía (el nodo 🐸) ve $P$, $A$ y $K$. Luego cada uno mezcla su secreto con lo que recibió, $K_a + K$ y $K_k + A$, y ambos obtienen el mismo color $S$, que el espía no puede formar.

En números: con el módulo público $p = 23$ y la base $g = 5$, A elige $a = 6$ y publica $A = g^a \bmod p = 8$; K elige $k = 15$ y publica $K = g^k \bmod p = 19$. Luego A calcula $K^a \bmod p$ y K calcula $A^k \bmod p$: ambos obtienen **2** (verificado en Python). Para obtenerlo, el espía tendría que encontrar $a$ o $k$ a partir de $A$ o $K$ (el logaritmo discreto), lo que es inviable con números grandes.

```python
p, g = 23, 5
a, k = 6, 15                       # secretos
A, K = pow(g, a, p), pow(g, k, p)  # públicos: 8 y 19
pow(K, a, p) == pow(A, k, p) == 2  # True: la misma clave en ambos lados
```

### Su debilidad: man-in-the-middle

![Man-in-the-middle en Diffie-Hellman](adjuntos/Man-in-the-middle%20en%20Diffie-Hellman.png)

> [!example]- Transcripción de la imagen
> Diffie-Hellman no verifica la identidad de las partes: cualquiera puede interceptar y hacerse pasar por otro. A encripta con K creyendo hablar con el nodo K, pero el espía desencripta con K, modifica el mensaje, lo encripta con $K_2$ y lo envía al nodo K, que piensa "ohhh… mensaje del nodo A".

El espía hace un intercambio Diffie-Hellman con cada lado por separado y queda en medio, leyendo y alterando todo. Para evitarlo hay que **autenticar** a las partes, por ejemplo con firmas y certificados.

## Preguntas de repaso

> [!question]- ¿Por qué el cifrado simétrico necesita resolver aparte la distribución de claves?
> Porque ambos lados deben tener la misma clave secreta antes de comunicarse, y enviarla por la red la expondría a quien esté escuchando.

> [!question]- ¿Qué ve el espía en Diffie-Hellman y por qué no le basta?
> Ve los parámetros públicos y los valores $A$ y $K$. Para calcular la clave compartida necesitaría uno de los secretos $a$ o $k$, y obtenerlos a partir de lo público es computacionalmente inviable.

> [!question]- ¿Por qué Diffie-Hellman es vulnerable a un ataque de intermediario?
> Porque no verifica la identidad de quien responde: un atacante puede hacer un intercambio con cada parte por separado y ambas creerán estar hablando entre sí.
