---
ramo: "Programación en C"
tema: "Structs"
tags:
  - c
  - structs
  - diseño
  - origen/complemento
prerrequisitos:
  - "[[03 - Structs anidados y structs recursivos]]"
---

# Structs como objetos y tipos compuestos

C no tiene clases, pero sí una convención muy usada para simularlas: un **struct con los datos** más un **conjunto de funciones** que lo reciben como primer argumento. Es la forma en que se programan las estructuras de datos del curso. Para datos pequeños que no necesitan identidad propia, en cambio, conviene lo contrario: tratarlos como **valores**, sin punteros.

## El patrón "objeto": init, métodos y destroy

```c
typedef struct dog
{
    char* name;
    struct dog* friend;
} Dog;

Dog* dog_init(char* name)              // "constructor": reserva en el heap e inicializa
{
    Dog* dog = malloc(sizeof(Dog));
    *dog = (Dog){.name = name, .friend = NULL};
    return dog;
}

void dog_bark(Dog* dog)               { printf("%s: guau!\n", dog->name); }   // "métodos"
void dog_meet(Dog* dog, Dog* friend)  { dog->friend = friend; friend->friend = dog; }
void dog_destroy(Dog* dog)            { free(dog); }                          // "destructor"

int main(void)
{
    Dog* bruno = dog_init("bruno");
    Dog* cata = dog_init("catalina");
    dog_meet(bruno, cata);
    dog_bark(bruno->friend);           // catalina: guau!
    dog_destroy(bruno);
    dog_destroy(cata);                 // un destroy por cada init: 0 leaks
    return 0;
}
```

- **`tipo_init`** concentra el `malloc` y deja el struct en un estado válido.
- Los **"métodos"** se llaman `tipo_accion` y reciben un puntero, para poder modificar el struct.
- **`tipo_destroy`** concentra el `free`. Si el struct es dueño de otros bloques (un arreglo, los nodos de una lista), los libera también, en el orden correcto.

Con esta convención, quien usa el struct no necesita saber cómo se maneja la memoria por dentro: basta con emparejar cada `init` con su `destroy`. Así se define, por ejemplo, la interfaz de una **lista ligada**:

```c
typedef struct list
{
    int value;
    struct list* next;
} List;

List* list_init(void);
List* list_append(List* list, int value);
List* list_at_index(List* list, int index);
void  list_destroy(List* list);
```

## Tipos compuestos: structs como valores

Un vector 3D, un punto o un color no necesitan vivir en el heap ni compartirse: son **contenedores** de unos pocos números. En ese caso se pasan y retornan **por valor**, directamente en el stack:

```c
typedef struct vector3d { double x, y, z; } Vec3D;

Vec3D vec3d_create(double x, double y, double z) { return (Vec3D){x, y, z}; }
double vec3d_dot(Vec3D a, Vec3D b) { return a.x * b.x + a.y * b.y + a.z * b.z; }
Vec3D vec3d_cross(Vec3D a, Vec3D b)
{
    return (Vec3D){a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x};
}
// vec3d_cross(i, j) con i = (1,0,0) y j = (0,1,0) da (0,0,1); vec3d_dot(i, j) = 0
```

> [!tip] ¿Puntero o valor?
> Si el dato es **grande**, debe **sobrevivir** a la función o **varias partes del programa lo comparten y modifican**, se usa el heap con punteros y el patrón init/destroy. Si es **pequeño e inmutable**, se usa por valor: no hay `malloc`, no hay que esperar al SO ni riesgo de leaks, y suele ser más rápido.

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene concentrar el `malloc` en `tipo_init` y el `free` en `tipo_destroy`?
> El manejo de memoria queda encapsulado en un solo lugar. Quien usa el struct solo tiene que llamar a un `destroy` por cada `init`, y es mucho más difícil dejar leaks o liberar en el orden incorrecto.

> [!question]- ¿Por qué `dog_meet` recibe punteros y no structs?
> Porque tiene que modificar los campos `friend` de los perros originales. Con copias, los cambios se perderían al retornar.

> [!question]- ¿Por qué `Vec3D` se pasa por valor sin problema?
> Porque es pequeño (24 bytes), no necesita sobrevivir a ninguna función y nadie lo comparte. Copiarlo es barato y evita el costo de pedir memoria al heap.

> [!question]- Si un struct de lista es dueño de sus nodos, ¿qué debe hacer `list_destroy`?
> Recorrer la lista y liberar cada nodo, guardando antes el puntero al siguiente para no perderlo, y terminar con todos los bloques liberados.
