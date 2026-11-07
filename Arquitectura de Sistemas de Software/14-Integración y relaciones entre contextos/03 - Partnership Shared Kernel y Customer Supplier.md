---
ramo: "Arquitectura de Sistemas de Software"
tema: "Integración y relaciones entre contextos"
tags:
  - arquisis/integracion
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[02 - El context map como mapa de decisiones de integración]]"
---

# Partnership Shared Kernel y Customer Supplier

El context map tiene siete relaciones posibles. Esta nota cubre las tres **cooperativas**, donde ambos equipos se hablan y tienen algo de poder sobre el contrato: **Partnership**, **Shared Kernel** y **Customer/Supplier**. Las otras cuatro, que aplican cuando el poder es más desigual, están en [[04 - Conformist Anticorruption Layer Open Host Service y Separate Ways]].

## Partnership

**Descripción:** dos contextos que **solo tienen éxito juntos**, y por lo mismo también fallan juntos. Comparten la planificación y la cadencia de entregas, y el contrato lo diseñan entre los dos. Tiene un componente de negocio, porque ambos equipos pueden compartir objetivos y recursos.

Funciona como dos personas que se reparten un trabajo: "yo te envío estos datos con esta forma y tú los recibes así". Cada lado define su parte, pero el acuerdo es conjunto.

- **Pros:** coherencia. Ningún lado se entera tarde de un cambio.
- **Contras:** exige coordinación continua entre dos equipos y releases acoplados. **No escala a más de dos**: si crece la cantidad de personas involucradas, la coordinación se vuelve inmanejable. Además, **no se puede aplicar en contextos asimétricos**. Nadie puede pedirle al SII que planifique sus entregas junto con su startup.
- **Ejemplo:** Promociones y Checkout. Una promoción solo tiene sentido si Checkout la aplica bien, y Checkout depende de Promociones para calcular el total. Promociones es un contexto pequeño y ambos equipos pueden ponerse de acuerdo.

## Shared Kernel

**Descripción:** un **subconjunto del modelo compartido explícitamente**, acotado, que solo se cambia por acuerdo mutuo. Los contextos no se envían esos datos: ambos asumen la misma definición. El mecanismo es una librería o un esquema compartido. En el caso degenerado, una **base de datos compartida**.

**Ejemplo:** Checkout y Catálogo comparten el `product_id` y el `precio`, porque ambos deben significar exactamente lo mismo. El resto del modelo sigue separado: Catálogo guarda la imagen en 4K y Checkout la miniatura de 240p, y cada uno decide lo suyo.

- **Pros:** **cero traducción** en lo compartido.
- **Contras:** cada cambio del kernel exige acuerdo y **despliegues acoplados**: si uno modifica el kernel, el otro también tiene que actualizarse. El kernel **tiende a crecer** hasta convertirse en "el modelo", y en ese punto ya no hay dos contextos sino uno mal partido. Promueve un acoplamiento excesivo.

> [!warning] Shared Kernel no es "compartir todo"
> Lo que define al patrón es que el subconjunto es **pequeño, explícito y versionado por acuerdo**. Una base de datos completa compartida entre dos servicios es el caso degenerado y casi siempre un antipatrón: ningún equipo puede cambiar su esquema sin coordinarse con el otro. Un "modelo canónico" impuesto a toda la empresa es un Shared Kernel forzado a escala corporativa.

## Customer / Supplier

**Descripción:** hay un upstream (supplier, proveedor) y un downstream (customer, cliente), pero **D tiene voz**: sus necesidades entran en la planificación de U. El proveedor se modifica según lo que exigen sus clientes. El mecanismo típico es una **API con contrato versionado** y **tests de contrato dirigidos por el consumidor** (*consumer-driven contract tests*), donde D escribe las expectativas que U se compromete a no romper.

**Ejemplo:** Checkout consume la API de Catálogo y un día necesita que el precio venga con IVA. Como es su cliente, se lo pide, y Catálogo agenda el cambio y empieza a enviar el IVA.

- **Pros:** D influye, hay un contrato explícito y una "mesa" donde negociarlo.
- **Contras:** hay que negociar, y U termina agendando trabajo ajeno, porque cada cliente pide cosas a la medida. Si U tiene muchos D, **la mesa se llena** y el proveedor pasa más tiempo atendiendo pedidos que avanzando en lo suyo. La salida natural es el **Open Host Service**: publicar un protocolo pensado para todos en vez de negociar con cada uno.

## Comparación

| | Partnership | Shared Kernel | Customer/Supplier |
|---|---|---|---|
| ¿Quién decide el contrato? | Ambos, co-diseñado | Ambos, por acuerdo | U, pero con las necesidades de D en su plan |
| Mecanismo | Planificación y releases conjuntos | Librería o esquema compartido | API versionada y tests de contrato |
| Traducción | Mínima | Ninguna en lo compartido | La que U implemente para D |
| Escala a muchos equipos | No (máximo dos) | Mal (el kernel crece) | Hasta que la mesa se llena |
| Riesgo principal | Coordinación y releases acoplados | Despliegues acoplados y kernel que se come todo | U saturado de pedidos a medida |

> [!tip] Cómo distinguirlas en una pregunta
> - Si ambos lados **planifican juntos** y fallan juntos → Partnership.
> - Si ambos **usan el mismo código o esquema** para un subconjunto → Shared Kernel.
> - Si uno **pide** y el otro **implementa** para él → Customer/Supplier.

## Preguntas de repaso

> [!question]- ¿Por qué Partnership no sirve para integrarse con una entidad como el SII?
> Porque Partnership exige simetría: ambos equipos planifican y liberan juntos. El SII no coordina sus entregas con sus usuarios. Frente a un upstream tan poderoso, lo que corresponde es adaptarse (Conformist) o protegerse con una ACL.

> [!question]- ¿Qué significa que un Shared Kernel "tiende a crecer hasta ser el modelo"? ¿Qué consecuencia tiene?
> Como compartir evita traducir, los equipos tienden a meter cada vez más conceptos en el kernel. Cuando el kernel contiene casi todo el modelo, los dos contextos dejan de ser independientes: cada cambio requiere acuerdo y despliegue conjunto, así que en la práctica hay un solo contexto mal partido.

> [!question]- V o F: "Dos microservicios que leen y escriben las mismas tablas de una base de datos tienen una relación Shared Kernel bien implementada".
> Falso. Es el caso degenerado del Shared Kernel. El subconjunto compartido no es acotado ni explícito: es todo el esquema, así que cualquier cambio de tabla rompe al otro servicio.

> [!question]- Checkout necesita que Catálogo agregue el IVA a su respuesta y Catálogo lo implementa. ¿Qué relación es y qué mecanismo ayudaría a que no se rompa en el futuro?
> Customer/Supplier: el downstream (Checkout) influye en la planificación del upstream (Catálogo). Lo protegería un contrato versionado con tests dirigidos por el consumidor. Checkout escribe un test que exige el campo IVA, y Catálogo lo corre antes de cada release.

> [!question]- Un proveedor interno pasa de 2 a 15 equipos consumidores y cada uno le pide endpoints a medida. ¿Qué problema de Customer/Supplier aparece y hacia qué relación debería migrar?
> La mesa de negociación se llena: el proveedor agenda trabajo de 15 clientes y deja de avanzar en lo suyo. Debería migrar a Open Host Service con un Published Language, es decir, un protocolo único, documentado y pensado para todos los consumidores.

> [!question]- ¿Cuál es la ventaja principal y el costo principal de cada una de las tres relaciones cooperativas?
> Partnership: coherencia total, a cambio de coordinación continua y releases acoplados. Shared Kernel: cero traducción, a cambio de despliegues acoplados. Customer/Supplier: D tiene voz y hay contrato, a cambio de negociación y de que U agende trabajo ajeno.
