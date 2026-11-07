---
ramo: "Arquitectura de Sistemas de Software"
tema: "Integración y relaciones entre contextos"
tags:
  - arquisis/integracion
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[03 - Partnership Shared Kernel y Customer Supplier]]"
  - "[[03 - Patrón Adapter]]"
---

# Conformist Anticorruption Layer Open Host Service y Separate Ways

Cuando el poder sobre el contrato es desigual, o cuando no conviene integrarse, quedan cuatro relaciones: D se adapta (**Conformist**), D se protege (**Anticorruption Layer**), U se publica para todos (**Open Host Service + Published Language**) o nadie se integra (**Separate Ways**).

## Conformist

**Descripción:** D **adopta el modelo de U tal cual**, porque U no tiene motivo para acomodarse a él. Aquí el importante es el proveedor, y el consumidor es el que se modifica. El mecanismo es simplemente ser cliente del API ajeno, con el vocabulario de U metido en el código propio.

- **Pros:** cero negociación y cero traducción, así que se integra rápido.
- **Contras:** los cambios ajenos entran a tu modelo. Si U cambia, D cambia también. **El costo no se paga hoy: se paga el día que U cambia.**
- **Ejemplo:** usar los objetos de la API de un proveedor de envíos (`Shipment`, `Parcel`, sus estados) directamente en las clases del dominio propio.

## Anticorruption Layer (ACL)

**Descripción:** D construye una **capa que traduce el modelo ajeno al propio**, y nada del vocabulario de U cruza esa capa. No es un sistema aparte: es una capa **dentro de la frontera de D**, antes de consumir, que adapta y filtra lo que llega para quedarse solo con lo que el dominio necesita. El mecanismo es un adaptador, una fachada o un traductor. Es la táctica de **encapsular** (Bass y Kazman) aplicada a un modelo completo.

![Dos equipos conectados U-D con una ACL del lado de D](adjuntos/Relación%20con%20capa%20anticorrupción%20entre%20dos%20equipos.png)

> [!example]- Transcripción de la imagen
> - Dos óvalos, "Team 1" y "Team 2", cada uno con varios módulos internos conectados entre sí.
> - Una línea los une. El extremo de Team 1 está marcado **U** y el de Team 2 **D**.
> - En el borde de Team 2, justo donde llega la línea, hay un rectángulo **ACL**: la traducción ocurre en la frontera del downstream.

- **Pros:** protege tu modelo. **Cambiar de proveedor es cambiar la capa, no migrar datos.**
- **Contras:** un segundo modelo que mantener, es decir, más código. Es **barata de escribir pero cara de diseñar**, porque exige entender bien los dos modelos.
- **Ejemplo:** Checkout recibe del proveedor de pagos estados como `AUTHORIZED_PENDING_CAPTURE`. Su ACL los traduce a los estados propios (`Pagado`, `Rechazado`). Si mañana se cambia de proveedor, solo se reescribe la ACL.

## Open Host Service + Published Language

**Descripción:** U publica un **protocolo de acceso pensado para todos sus consumidores** (OHS) y un **lenguaje documentado** para la traducción (PL). Es lo contrario a construir una API "para conectarme con alguien": se construye para que **cualquiera pueda acoplarse**. Ejemplos de PL: la especificación OpenAPI de una API o el esquema de los eventos (AsyncAPI, *schema registry*).

- **Pros:** **escala a N consumidores**, y nadie necesita conocer el modelo interno de U.
- **Contras:** U paga la estabilidad y el versionado. El lenguaje publicado es un **compromiso público**, así que será muy difícil cambiarlo.
- **Ejemplo:** Catálogo expone una API documentada de productos que usan Checkout, Búsqueda, Recomendaciones y la app móvil.

## Separate Ways

**Descripción:** **no integrar** y duplicar lo poco que se necesita. Nadie habla con nadie: cada sistema guarda lo que le hace falta y es independiente.

![Dos equipos con la conexión cortada](adjuntos/Separate%20Ways%20sin%20integración%20entre%20dos%20equipos.png)

> [!example]- Transcripción de la imagen
> - Los mismos óvalos "Team 1" y "Team 2" con sus módulos internos.
> - La línea que los unía está cruzada por una **X roja**: no existe integración entre ellos.

- **Pros:** cero acoplamiento. Es **la relación más barata que existe**.
- **Contras:** duplicación y posibles **inconsistencias**. Si Checkout guarda su propia copia de los precios, una oferta nueva de Catálogo no le llega y cobra el precio antiguo. Deja de ser barata cuando lo duplicado crece o cambia seguido, porque mantener bases de datos separadas en sincronía es muy complicado.

## Las siete relaciones en una tabla

| Relación | Quién se adapta | Traducción | Úsala cuando |
|---|---|---|---|
| Partnership | Ambos, juntos | Mínima | Dos equipos que solo tienen éxito juntos |
| Shared Kernel | Ambos, por acuerdo | Ninguna en lo compartido | Un subconjunto pequeño debe significar lo mismo |
| Customer/Supplier | U, para D | La que U implemente | D es interno y tiene voz |
| Conformist | D, sin negociar | Ninguna | U no te escucha y su modelo es aceptable |
| ACL | D, con una capa | Total, del lado de D | U no te escucha y su modelo te contaminaría |
| OHS + PL | U, una vez para todos | U publica el lenguaje | U tiene muchos consumidores |
| Separate Ways | Nadie | No hay integración | Lo compartido es poco y cambia poco |

> [!warning] Conformist vs ACL: la misma situación, dos respuestas
> Ambas aparecen cuando **D no tiene poder sobre U**. La diferencia es qué se hace con el modelo ajeno. Conformist lo acepta tal cual: es barato hoy y caro cuando U cambia. ACL lo traduce: es caro hoy y barato cuando U cambia o cuando hay que reemplazarlo. Para un proveedor externo crítico (pagos, legados), la pauta espera ACL.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que en Conformist "el costo se paga el día que U cambia"?
> Porque D usa el modelo de U sin traducirlo, y hoy no gasta nada en negociar ni traducir. Pero ese modelo ajeno está repartido por todo su código, así que cuando U cambia un campo o un estado, el cambio se propaga por todo D.

> [!question]- ¿Dónde vive una ACL: en el upstream, en el downstream o en un sistema aparte? ¿Por qué?
> En el downstream, dentro de su frontera, justo antes de consumir. Su objetivo es proteger el modelo de D, así que la mantiene quien se beneficia de ella. No hace falta un sistema aparte (aunque un middleware puede cumplir ese rol).

> [!question]- V o F: "Una ACL es barata de diseñar porque solo copia campos de un objeto a otro".
> Falso. Es barata de escribir pero cara de diseñar: para traducir bien hay que entender a fondo ambos modelos (qué significa cada estado del proveedor y a qué concepto propio corresponde). Una mala traducción filtra el modelo ajeno igual que no tener capa.

> [!question]- ¿Qué gana y qué pierde un upstream al pasar de Customer/Supplier a Open Host Service?
> Gana escala: atiende a N consumidores con un solo protocolo y deja de negociar con cada uno. Pierde flexibilidad: el lenguaje publicado se vuelve un compromiso público que debe mantener estable y versionado, y cambiarlo es muy difícil.

> [!question]- Checkout decide guardar su propia tabla de precios y no consultar a Catálogo (Separate Ways). Dé un escenario donde esto falla.
> Catálogo publica una oferta del 30% y Checkout sigue cobrando el precio antiguo porque su copia no se actualizó. La relación es barata mientras lo duplicado sea poco y estable, pero el precio cambia seguido, así que la inconsistencia aparece rápido.

> [!question]- Mini caso: una startup integra su sistema con el registro civil, que expone una API XML con un protocolo muy específico que solo dos desarrolladores entienden. ¿Qué relación y qué táctica propone?
> El registro civil no se va a adaptar, así que D no tiene poder. Conviene una ACL implementada como middleware que encapsule el protocolo y el XML y exponga una interfaz simple y compatible con el resto del sistema. Las tácticas a nombrar son encapsulamiento de la complejidad, abstracción de servicios comunes y uso de un intermediario. El costo es un componente más que mantener.

> [!question]- Alternativas: ¿cuál relación escala mejor cuando un contexto tiene muchos consumidores? a) Partnership · b) Shared Kernel · c) Customer/Supplier · d) Open Host Service
> d). Partnership no pasa de dos equipos, Shared Kernel acopla los despliegues de todos y Customer/Supplier satura la mesa de negociación. OHS publica un protocolo único que cualquiera puede consumir sin conocer el modelo interno.
