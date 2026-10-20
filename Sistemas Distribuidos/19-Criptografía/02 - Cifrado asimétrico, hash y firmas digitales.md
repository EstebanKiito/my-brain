---
ramo: "Sistemas Distribuidos"
tema: "Criptografía"
tags:
  - sd/seguridad
  - python
  - origen/complemento
prerrequisitos:
  - "[[01 - Cifrado simétrico e intercambio Diffie-Hellman]]"
---

# Cifrado asimétrico, hash y firmas digitales

El cifrado asimétrico rompe el problema de compartir un secreto: cada participante tiene **dos** llaves, una pública que puede repartir y una privada que nunca sale de sus manos. Con ese par se puede cifrar para alguien sin acordar nada antes y, al revés, **firmar** para demostrar quién envió un mensaje.

## Cifrado asimétrico

- Usa un par de claves relacionadas matemáticamente: una **llave pública** ($PK$) y una **llave privada** ($SK$).
- La pública se comparte libremente; la privada solo la conoce su creador.
- También se llama **criptografía de clave pública**.

**Para confidencialidad:** A cifra con la llave **pública de S**, `Encriptar(mensaje, PK_S)`, y solo S puede descifrar con su llave **privada**, `Desencriptar(mensaje, SK_S)`.

**Para firmar:** A cifra con **su llave privada**, `Encriptar(mensaje, SK_A)`, y cualquiera lo descifra con la **pública de A**. Si funciona, el mensaje solo pudo venir de A.

| Algoritmo | Idea |
|---|---|
| **RSA** (Rivest, Shamir y Adleman) | El más conocido; su seguridad se basa en lo difícil que es factorizar el producto de dos primos muy grandes |
| **ECC** (curvas elípticas) | Seguridad comparable a RSA con claves más cortas y menos cómputo; ideal para móviles. Bitcoin y Ethereum firman transacciones con ECDSA |

> [!warning] Su desafío
> Es entre **100 y 1000 veces** más lento que el cifrado simétrico, y firmar un documento grande completo es lento y costoso.

## Funciones hash

Una **función hash** toma un mensaje de cualquier largo y produce una cadena de bits de **largo fijo**. Cualquier cambio en el mensaje produce un hash distinto: en SHA-256, "hola" y "Hola" dan hashes completamente diferentes (`b221d9db…` y `e633f4fc…`).

| Propiedad | Significado |
|---|---|
| **Unidireccional** | Es inviable recuperar el mensaje a partir del hash |
| **Resistencia débil a colisiones** | Dado un mensaje $m$ y su hash $h$, es inviable encontrar otro $m'$ con el mismo hash |
| **Resistencia fuerte a colisiones** | Es inviable encontrar **cualquier** par $m \neq m'$ con el mismo hash |

## Firmas digitales

![Firma digital con hash](adjuntos/Firma%20digital%20con%20hash.png)

> [!example]- Transcripción de la imagen
> Ambas partes conocen la llave pública. El nodo A envía al nodo Y el documento original junto con el hash firmado con $SK_a$. Y aplica el hash al documento, descifra la firma con la llave pública de A y compara ambos hashes.

Como firmar el documento entero es lento, se firma solo su **hash**, que es corto:

1. A calcula el hash del documento y lo cifra con su llave privada: esa es la **firma**.
2. A envía el documento y la firma.
3. El receptor calcula el hash del documento, descifra la firma con la llave pública de A y compara.

```python
P, Q = 61, 53; n = P * Q; phi = (P - 1) * (Q - 1)
e = 17; d = pow(e, -1, phi)                        # llave pública (e, n), privada d
h = int.from_bytes(hashlib.sha256(doc).digest(), "big") % n
firma = pow(h, d, n)                               # firmar con la privada
pow(firma, e, n) == h                              # verificar con la pública: True
```

Con este RSA de juguete, la firma verifica con el documento original y falla con uno alterado (probado en Python).

> [!tip] Lo que garantiza una firma
> - **Integridad:** si el mensaje cambió en el camino, el hash calculado no coincide con el de la firma.
> - **No repudio:** el **emisor** no puede negar haber firmado, porque solo él tiene la llave privada. (No garantiza que el receptor no niegue haberlo recibido.)

## Preguntas de repaso

> [!question]- Para enviar un mensaje que solo S pueda leer, ¿con qué llave se cifra?
> Con la llave pública de S: solo su llave privada puede descifrarlo.

> [!question]- ¿Por qué se firma el hash y no el documento completo?
> Porque el cifrado asimétrico es lento, y el hash es corto y de largo fijo. Firmarlo es mucho más barato y, por la resistencia a colisiones, sigue identificando al documento.

> [!question]- ¿Qué significa el no repudio y quién no puede negar qué?
> Que el emisor no puede negar haber firmado el mensaje, porque solo él tiene la llave privada que produjo la firma.
