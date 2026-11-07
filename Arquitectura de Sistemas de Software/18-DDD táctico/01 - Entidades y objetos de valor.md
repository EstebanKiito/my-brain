---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD táctico"
tags:
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[02 - El context map como mapa de decisiones de integración]]"
---

# Entidades y objetos de valor

DDD estratégico responde **qué contextos hay**. El bloque de integración responde **cómo se relacionan** y el de performance **cuánto cuesta cruzarlos**. El **DDD táctico** mira hacia **adentro de un bounded context**, y la pregunta cambia: ya no es "¿qué relación hay?", sino **"¿qué debe ser cierto al mismo tiempo?"**. Los bloques con que se responde son entidades, objetos de valor, agregados, repositorios, servicios y eventos. El ejemplo que se usa en todo el tema es el contexto **Checkout**, y el ejemplo en código es el proyecto abierto *domain-driven-hexagon* (Sairyss, licencia MIT).

## Entidad

> [!tip] Entidad
> Un objeto que **tiene identidad**: puede **cambiar sus atributos y seguir siendo el mismo**.

El pedido #101230 puede cambiar de estado, agregar líneas o cambiar de dirección de entrega, y sigue siendo el pedido #101230. Lo que lo define es su id, no sus datos. Un `UserEntity` sigue siendo el mismo usuario aunque cambie su correo.

## Objeto de valor (*value object*)

> [!tip] Objeto de valor
> Un objeto que **se define por sus atributos**, es **inmutable** y se compara **por valor**: dos objetos con los mismos datos son iguales.

Ejemplos típicos:
- **Valores fungibles**, como el **dinero**: un billete de \$1.000 es intercambiable por otro de \$1.000.
- **Identidades universales** como una **dirección**: "Av. Vicuña Mackenna 4860, Santiago" es esa dirección, venga de donde venga.

Como es inmutable, para "cambiar" un objeto de valor se crea uno nuevo. Además, **se valida al construirse**, así que nunca existe una dirección inválida en el sistema:

```typescript
export class Address extends ValueObject<AddressProps> {
  get country(): string { return this.props.country; }
  get street(): string { return this.props.street; }

  protected validate(props: AddressProps): void {
    if (!Guard.lengthIsBetween(props.country, 2, 50))
      throw new ArgumentOutOfRangeException('country is out of range');
    // ... también se valida street y postalCode
  }
}
```

> [!tip] Regla rápida
> **Si dos instancias con los mismos datos son intercambiables, es un objeto de valor.** Si importa *cuál* de las dos es, es una entidad.

## Objetos de valor frente a *primitive obsession*

**Primitive obsession** es modelar conceptos del dominio con tipos primitivos (`int`, `string`, `number`) y repartir la lógica asociada por todo el código. El ejemplo clásico es `amount: number`, que **no sabe de monedas**: nada impide sumar 100 dólares con 100 pesos.

```typescript
// Primitivo: el error compila
total = precioUSD + precioCLP;

// Objeto de valor: la regla vive en un solo lugar
class Dinero {
  constructor(readonly monto: number, readonly moneda: 'CLP' | 'USD') {}
  sumar(otro: Dinero): Dinero {
    if (otro.moneda !== this.moneda) throw new Error('Monedas distintas');
    return new Dinero(this.monto + otro.monto, this.moneda);
  }
}
```

El objeto de valor concentra la validación y las operaciones del concepto. En vez de validar un RUT o un correo en cada controlador, se valida una vez, al crear el objeto `Rut` o `Email`.

| | Entidad | Objeto de valor |
|---|---|---|
| Se identifica por | Su id | Sus atributos |
| Mutabilidad | Cambia a lo largo del tiempo | Inmutable (se reemplaza) |
| Igualdad | Mismo id | Mismos valores |
| Ejemplos en Checkout | Pedido, LíneaPedido, Cliente | Dinero, Dirección, Cantidad, Email |

> [!warning] El mismo concepto puede ser entidad en un contexto y valor en otro
> Una dirección es un objeto de valor en Checkout (solo importa a dónde enviar). En un contexto de Catastro, donde cada propiedad se sigue en el tiempo, puede ser una entidad. La clasificación depende del contexto, no del nombre.

## Preguntas de repaso

> [!question]- ¿Qué pregunta guía el DDD táctico y en qué se diferencia de la del DDD estratégico?
> El táctico pregunta qué debe ser cierto al mismo tiempo dentro de un bounded context: qué reglas e invariantes hay que proteger juntas. El estratégico pregunta qué contextos existen y cómo se relacionan entre ellos.

> [!question]- Clasifique como entidad u objeto de valor en un e-commerce: Pedido, Dinero, Cliente, Dirección de entrega, Cantidad.
> Entidades: Pedido y Cliente, porque tienen identidad y cambian en el tiempo. Objetos de valor: Dinero, Dirección de entrega y Cantidad, porque se definen por sus valores y son intercambiables si coinciden.

> [!question]- ¿Por qué un objeto de valor debe ser inmutable?
> Porque se comparte por valor. Si fuera mutable, cambiar la dirección de un pedido podría cambiar sin querer la de otro objeto que referencia la misma instancia. Al ser inmutable, cambiar significa crear uno nuevo y reemplazarlo, sin efectos colaterales.

> [!question]- ¿Qué es primitive obsession y qué problema concreto tiene `amount: number`?
> Es modelar conceptos del dominio con tipos primitivos. `amount: number` no sabe de monedas, así que permite sumar montos en monedas distintas, y la validación y las operaciones del dinero quedan repartidas por el código.

> [!question]- ¿Qué ventaja tiene validar en el constructor de un objeto de valor como `Address`?
> Que nunca existe una instancia inválida en el sistema. La validación ocurre en un solo lugar y el resto del código puede confiar en que cualquier `Address` cumple las reglas.

> [!question]- V o F: "Dos pedidos con exactamente los mismos productos y montos son el mismo pedido".
> Falso. El pedido es una entidad y se identifica por su id. Dos pedidos con los mismos datos siguen siendo dos compras distintas.

> [!question]- ¿Por qué una dirección puede ser objeto de valor en un contexto y entidad en otro?
> Porque la clasificación depende de qué le importa al contexto. A Checkout solo le importa el valor de la dirección para despachar. A un contexto que sigue la historia de cada inmueble le importa su identidad a lo largo del tiempo.
