---
ramo: "Arquitectura de Sistemas de Software"
tema: "Cohesión acoplamiento y connascence"
tags:
  - arquisis/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[03 - Tradeoffs y conocimiento de dominio]]"
  - "[[02 - Acoplamiento]]"
  - "[[03 - Cohesión]]"
---

# Cohesión y acoplamiento entre módulos

Si diseñamos algo, ¿cómo sabemos si está bien? Necesitamos medidas que digan si un diseño aporta valor al cliente, al sistema y a cómo funciona. Las tres herramientas clásicas son la **cohesión**, el **acoplamiento** y la **connascence**. El objetivo de todo buen diseño se resume en una frase: **alta cohesión y bajo acoplamiento**.

## Cohesión

> [!tip] Cohesión
> Las partes que deben ir juntas **están juntas** en un mismo módulo, e interactúan idealmente mediante campos comunes o llamadas relacionadas.

Con alta cohesión, para realizar una acción solo hay que llamar a un lugar.
- **Buena cohesión: `numpy`.** Para un cálculo matemático, todo lo necesario está ahí: no hay que buscar en otro lado.
- **Poca cohesión: `string` o `io`.** Agrupan funcionalidades heterogéneas y hacen cosas extra (llamadas al sistema, por ejemplo), así que la cohesión se pierde.

En arquitectura, la cohesión se lleva al nivel de componentes: un componente debe agrupar una responsabilidad clara. Un servicio de "Pagos" que además envía newsletters tiene baja cohesión.

## Acoplamiento

> [!tip] Acoplamiento
> **Grado de interdependencia** entre dos o más componentes de software: qué tan juntos tienen que estar para funcionar.

Mal usado, el acoplamiento se vuelve rápidamente una propiedad indeseable. Con muchos puntos de conexión entre dos piezas, un cambio en una rompe la otra y aparece el **código spaghetti**. La idea es que dos piezas tengan **un solo punto de conexión**. Se reduce con **refactoring** y **patrones de diseño**.

### Tipos de acoplamiento entre módulos

Stevens, Myers y Constantine (1974, *Structured Design*) los ordenan de más fuerte a más débil:

| Tipo | Qué es | Ejemplo |
|---|---|---|
| **Contenido** (el más fuerte) | Un módulo depende de la implementación interna de otro | Leer directamente las variables privadas de otro módulo |
| **Común** | Usan propiedades o variables compartidas entre módulos | Variables globales que varios módulos modifican |
| **Control** | Un módulo controla el flujo del otro | Pasar un flag `modo="rapido"` que cambia lo que hace la función |
| **Stamp / estructura de datos** | Operan sobre estructuras de datos comunes | Dos servicios que leen y escriben las mismas tablas |
| **Datos** (el más débil) | Se pasan solo los datos específicos como parámetros | `calcular_iva(monto)` |

> [!example]- Ejemplo: de acoplamiento de contenido a acoplamiento de datos
> ```python
> # Contenido: Facturación lee el interior del carrito
> total = carrito._items_internos[0]._precio_bruto * 1.19
>
> # Datos: Facturación recibe solo lo que necesita
> total = calcular_total(precio_neto=carrito.subtotal(), tasa_iva=0.19)
> ```
> En el segundo caso, el carrito puede cambiar su estructura interna sin romper a Facturación.

## Por qué importa en arquitectura

Una aplicación evoluciona constantemente. Con alta cohesión, cada cambio queda dentro de un componente. Con bajo acoplamiento, ese cambio no se propaga a los demás. A nivel arquitectónico:
- **alta cohesión** permite asignar un componente a un equipo y desplegarlo por separado;
- **bajo acoplamiento** permite que un componente falle o cambie sin arrastrar al resto. Es la base de la **degradación elegante** (*graceful degradation*): el sistema pierde una función, pero no se cae entero.

> [!warning] Big ball of mud
> El antipatrón que resulta de no cuidar estas medidas: sin un plan de diseño, todo queda conectado con todo, con gran acoplamiento y poca cohesión, y el sistema se vuelve muy difícil de mantener. Puede ocurrir incluso con microservicios: si todos los servicios se llaman entre sí, ninguno es independiente. Es un *big ball of distributed mud*.

## Preguntas de repaso

> [!question]- ¿Por qué `numpy` se pone como ejemplo de alta cohesión y `io` de baja?
> `numpy` concentra todo lo necesario para el cálculo numérico en un módulo con un propósito claro. `io` agrupa operaciones variadas de entrada y salida y llamadas al sistema, así que sus partes no están tan relacionadas entre sí.

> [!question]- Ordene de más fuerte a más débil: acoplamiento de datos, de contenido, de control y común.
> Contenido > común > control > datos. El más deseable es el de datos: se pasan solo los parámetros necesarios.

> [!question]- Dos microservicios leen y escriben las mismas tablas. ¿Qué tipo de acoplamiento tienen y qué problema trae?
> Acoplamiento de stamp o estructura de datos: operan sobre una estructura común. Cualquier cambio de esquema que haga uno puede romper al otro, y no pueden evolucionar ni desplegarse de forma independiente.

> [!question]- ¿Qué relación tiene el bajo acoplamiento con la degradación elegante?
> Si los componentes dependen poco entre sí, la falla de uno no arrastra a los demás: el sistema pierde una funcionalidad pero sigue operando en lo demás.

> [!question]- ¿Qué es el big ball of mud y cómo se relaciona con un diagrama de microservicios todos conectados entre sí?
> Es el antipatrón de un sistema sin diseño claro, con alto acoplamiento y baja cohesión, muy difícil de mantener. Si todos los microservicios se llaman entre sí, ninguno es realmente independiente (no son quantas separadas), y se obtiene un big ball of distributed mud.

> [!question]- V o F: "Un sistema con alta cohesión necesariamente tiene bajo acoplamiento".
> Falso. Son medidas distintas: un componente puede estar muy bien agrupado internamente y aun así depender de muchos otros. Hay que cuidar ambas a la vez.

> [!question]- Mini caso: un servicio de pagos además genera reportes de marketing y envía newsletters. ¿Qué medida viola y qué propone?
> Viola la cohesión: mezcla responsabilidades no relacionadas. Se propone separar los reportes y el newsletter en otro componente (por ejemplo, Marketing) que consuma eventos de Pagos, con lo que Pagos queda cohesionado y el acoplamiento se reduce a un evento.
