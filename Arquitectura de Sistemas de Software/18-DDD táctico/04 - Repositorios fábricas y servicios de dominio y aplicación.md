---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD táctico"
tags:
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[02 - Agregados y raíz del agregado]]"
---

# Repositorios fábricas y servicios de dominio y aplicación

Los agregados tienen que crearse, guardarse y usarse dentro de casos de uso. DDD táctico reparte esas responsabilidades entre cuatro piezas: **repositorios** (guardar y cargar), **fábricas** (crear válido), **servicios de dominio** (reglas que no son de una entidad) y **servicios de aplicación** (orquestar el caso de uso). Confundirlas es la forma más común de terminar con un modelo anémico.

## Repositorio

> [!tip] Repositorio
> Aparenta ser una **colección en memoria de un agregado**. Hay **uno por raíz** de agregado. **Carga y guarda la raíz completa**, y la persistencia (SQL, documentos, una API) es un detalle que el dominio no ve.

En la arquitectura hexagonal, el repositorio se define como un **puerto** (una interfaz en el lenguaje del dominio) y se implementa con un **adaptador**:

```typescript
export interface RepositoryPort<Entity> {
  insert(entity: Entity | Entity[]): Promise<void>;
  findOneById(id: string): Promise<Option<Entity>>;
  delete(entity: Entity): Promise<boolean>;
  transaction<T>(handler: () => Promise<T>): Promise<T>;
}

export interface UserRepositoryPort extends RepositoryPort<UserEntity> {
  findOneByEmail(email: string): Promise<UserEntity | null>;
}
```

Uno por raíz significa que existe `PedidoRepository`, pero no `LineaPedidoRepository`: las líneas se cargan y se guardan con su pedido. Un repositorio por tabla rompería la frontera del agregado.

## Fábrica

Una **fábrica construye agregados válidos desde el inicio**. Puede ser un método estático (`UserEntity.create(...)`) o una clase aparte cuando la construcción es compleja. Asigna el id, aplica los valores por defecto (rol `guest`), valida los invariantes y emite el evento de creación. Así nunca existe un agregado "a medio armar".

## Servicio de dominio

> [!tip] Servicio de dominio
> Una **regla de negocio que no pertenece naturalmente a una entidad**, por lo general porque involucra a varias. Ejemplo: `PoliticaDeDescuento`, que decide el descuento según el cliente, el carrito y las promociones vigentes.

Encapsula reglas, y a veces tiene restricciones fuertes: **no depende de librerías externas ni de infraestructura**, solo de código del dominio.

## Servicio de aplicación

> [!tip] Servicio de aplicación
> **Orquesta un caso de uso**: crear o cargar el agregado, invocar su comportamiento, guardarlo y publicar los eventos. **Aquí empieza y termina la transacción.**

```typescript
@CommandHandler(CreateUserCommand)
export class CreateUserService implements ICommandHandler {
  constructor(@Inject(USER_REPOSITORY) protected readonly userRepo: UserRepositoryPort) {}

  async execute(command: CreateUserCommand): Promise<Result<AggregateID, UserAlreadyExistsError>> {
    const user = UserEntity.create({                       // 1. crear con la fábrica
      email: command.email,
      address: new Address({ country: command.country, postalCode: command.postalCode, street: command.street }),
    });
    try {
      await this.userRepo.transaction(async () => this.userRepo.insert(user));  // 2. guardar en una transacción
      return Ok(user.id);
    } catch (error) {
      if (error instanceof ConflictException) return Err(new UserAlreadyExistsError(error));
      throw error;
    }
  }
}
```

El servicio de aplicación **no decide nada del negocio**: no calcula descuentos ni valida reglas, solo coordina.

## Dónde va cada cosa

| Pieza | Responsabilidad | No debe tener |
|---|---|---|
| Entidad / agregado | Invariantes y comportamiento propio | Infraestructura |
| Objeto de valor | Validación y operaciones del concepto | Identidad, mutabilidad |
| Fábrica | Construir agregados válidos | Persistencia |
| Repositorio (puerto) | Cargar y guardar raíces | Reglas de negocio |
| Servicio de dominio | Reglas entre varias entidades | Infraestructura, transacciones |
| Servicio de aplicación | Orquestar el caso de uso y la transacción | Lógica de negocio |

> [!warning] Sin lógica de negocio en el de aplicación; sin infraestructura en el de dominio
> Si el servicio de aplicación empieza a calcular el total o a decidir si un pedido se puede cancelar, se vuelve al modelo anémico. Si el servicio de dominio llama a la base de datos o a una API, se acopla a la infraestructura y deja de poder probarse de forma aislada.

## Preguntas de repaso

> [!question]- ¿Por qué hay un repositorio por raíz de agregado y no uno por tabla?
> Porque el agregado se carga y se guarda completo para proteger sus invariantes. Un repositorio de líneas de pedido permitiría modificarlas sin pasar por la raíz y rompería la frontera del agregado.

> [!question]- ¿Qué quiere decir que el repositorio "aparenta ser una colección en memoria"?
> Que el dominio lo usa como si fuera una lista de agregados (agregar, buscar por id, borrar) sin saber cómo se persisten. La base de datos, el ORM o el formato son detalles del adaptador que lo implementa.

> [!question]- Diferencie servicio de dominio y servicio de aplicación con un ejemplo de cada uno en Checkout.
> Servicio de dominio: `PoliticaDeDescuento`, que calcula el descuento a partir del cliente, el carrito y las promociones, es decir, una regla de negocio entre varias entidades. Servicio de aplicación: `ConfirmarPedidoService`, que carga el pedido, llama a `pedido.confirmar()`, lo guarda en una transacción y publica el evento.

> [!question]- ¿Dónde empieza y termina la transacción en DDD táctico y por qué ahí?
> En el servicio de aplicación, porque es quien conoce el caso de uso completo. Ahí se carga el agregado, se invoca su comportamiento y se guarda. Así la transacción abarca exactamente un agregado y un caso de uso.

> [!question]- ¿Qué aporta una fábrica frente a un constructor público con setters?
> Garantiza que el agregado nazca válido: asigna el id, aplica los valores por defecto, valida los invariantes y emite el evento de creación en un solo paso. Con setters, el objeto puede existir incompleto o inválido entre una llamada y otra.

> [!question]- V o F: "El servicio de aplicación debería validar que un pedido cancelado no pueda confirmarse".
> Falso. Esa es una regla del negocio y debe vivir en el agregado (`pedido.confirmar()` falla si está cancelado). El servicio de aplicación solo orquesta: carga, invoca, guarda y publica.
