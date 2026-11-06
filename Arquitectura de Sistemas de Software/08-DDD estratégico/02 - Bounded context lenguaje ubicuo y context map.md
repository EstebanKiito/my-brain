---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD estratégico"
tags:
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[01 - Dominio subdominios y diseño por dominio]]"
---

# Bounded context lenguaje ubicuo y context map

Los subdominios dividen el **problema**. Los **bounded contexts** dividen la **solución**: son las fronteras técnicas dentro de las cuales un modelo es consistente. El **context map** dibuja cómo se relacionan esas fronteras. Esta nota introduce los dos conceptos; las relaciones en detalle están en [[03 - Partnership Shared Kernel y Customer Supplier]] y en [[04 - Conformist Anticorruption Layer Open Host Service y Separate Ways]].

## Bounded context

> [!tip] Bounded context (contexto acotado)
> **Espacio donde los conceptos y las definiciones tienen consistencia, sin contradicciones.** Es un trozo del modelo de negocio internamente consistente, muy cohesionado. Un dominio puede tener **muchos** bounded contexts.

Cuando se habla de contexto acotado, se habla del **marco donde se encapsulan los subdominios**. Por eso pasa a ser un concepto **más técnico**: un bounded context puede cubrir uno o varios subdominios.

### Lenguaje ubicuo

Dentro de un bounded context se usa un **lenguaje ubicuo** (*ubiquitous language*): todos los involucrados (desarrolladores, expertos del negocio, el código) usan los mismos términos con el mismo significado. Entre contextos distintos, **la misma palabra puede significar cosas distintas**, y eso está bien.

**Ejemplo: "producto" en un e-commerce.**

| Contexto | Qué es un producto |
|---|---|
| Catálogo de ventas | Imagen, descripción y precio |
| Envíos | Tamaño y peso |
| Atención al cliente | Estado del producto y garantías |
| Facturación | Precio e IVA |

Otro ejemplo: un **stock** puede ser la cantidad disponible en un componente y otra cosa en otro. Forzar un único modelo de "producto" para todos haría que cada cambio pedido por un contexto afectara a los demás.

> [!warning] Bounded context ≠ quanta
> El bounded context es una frontera **de modelo** (dónde un vocabulario es consistente). La quanta es una frontera **de despliegue y de falla** (qué se despliega y se cae por separado). Lo ideal es que cada quantum corresponda a un bounded context, pero varios contextos pueden vivir en un solo quantum (un monolito modular), y un contexto puede desplegarse en varias quantas.

## Context map

> [!tip] Context map
> **Links de un subdominio a otro** (de un contexto a otro), que **mapean el conocimiento justo y necesario: el contrato**. Explicita las dependencias y los contratos de integración entre los contextos.

![Context map entre Catálogos, Facturación, Envíos y CS](adjuntos/Context%20map%20entre%20catálogo%20facturación%20envíos%20y%20atención%20al%20cliente.png)

> [!example]- Transcripción de la imagen
> - Croquis titulado "Context map" con cuatro contextos: **Catálogos**, **Facturación**, **Envíos** y **CS** (*customer service*, atención al cliente).
> - Catálogos → Facturación, con la etiqueta "compra". Facturación → Envíos, con la etiqueta "enviar". Envíos → CS, con la etiqueta "informar".

Cada flecha expresa qué información cruza de un contexto a otro y en qué dirección: una compra en Catálogos genera una factura, la factura dispara un envío y el envío informa a atención al cliente.

**Relaciones de context mapping** (se ven en detalle en integración): Conformist, Separate Ways, Anticorruption Layer (ACL), Open Host Service, Shared Kernel, además de Partnership y Customer/Supplier.

## Preguntas de repaso

> [!question]- Defina bounded context y explique por qué un dominio puede tener muchos.
> Es el espacio donde los conceptos y las definiciones son consistentes, sin contradicciones. Un dominio grande tiene áreas donde la misma palabra significa cosas distintas (producto, stock), así que se divide en varios contextos, cada uno con su propio modelo coherente.

> [!question]- ¿Qué es el lenguaje ubicuo y en qué alcance aplica?
> Es el vocabulario compartido por todos los involucrados (negocio, desarrolladores, código) dentro de un bounded context. Aplica solo dentro de ese contexto: en otro contexto, el mismo término puede significar otra cosa.

> [!question]- Dé dos términos que cambien de significado entre contextos en un e-commerce.
> "Producto": imagen y precio en Catálogo, tamaño y peso en Envíos. "Cliente": perfil y preferencias en Catálogo, dirección de entrega en Envíos y RUT y razón social en Facturación.

> [!question]- V o F: "Un bounded context es lo mismo que una quanta".
> Falso. El bounded context es una frontera de modelo y vocabulario. La quanta es una frontera de despliegue y de falla. Pueden coincidir, pero un monolito modular tiene varios contextos en una sola quanta.

> [!question]- ¿Qué mapea un context map y por qué se dice que mapea "el conocimiento justo y necesario"?
> Mapea las relaciones entre contextos: quién depende de quién y con qué contrato. Solo expone lo necesario para integrarse (el contrato), no el modelo interno de cada contexto, para no acoplarlos de más.

> [!question]- ¿Por qué el bounded context se considera más técnico que el subdominio?
> Porque el subdominio describe cómo se divide el negocio (el problema), mientras que el bounded context describe cómo se encapsula ese conocimiento en el software (la solución): qué modelo, qué fronteras de código y qué contratos.

> [!question]- ¿Qué problema aparece si se fuerza un único modelo de "producto" para todos los contextos?
> Cada contexto necesita atributos distintos. Un modelo único se vuelve enorme, y cada cambio pedido por un contexto (por ejemplo, Envíos agrega el volumen) obliga a coordinar con todos los demás. Se acoplan contextos que deberían evolucionar por separado.
