---
ramo: "Estructuras de Datos"
tema: "Estructuras lineales"
tags:
  - edd
  - listas-ligadas
  - c
  - implementacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Arreglos frente a listas ligadas]]"
  - "[[04 - Structs como objetos y tipos compuestos]]"
  - "[[02 - malloc, calloc y free]]"
---

# Implementación de una lista ligada en C

Una lista ligada en C combina tres herramientas del lenguaje: un [[03 - Structs anidados y structs recursivos|struct recursivo]] para el nodo, el [[02 - malloc, calloc y free|heap]] para que los nodos sobrevivan a las funciones y el [[04 - Structs como objetos y tipos compuestos|patrón init/destroy]] para encapsular la memoria. Esta implementación separa el **nodo** de la **lista**, que guarda la cabeza, la cola y el largo, para que agregar al final y consultar el largo sean $O(1)$.

## Los tipos

```c
typedef struct node
{
    int value;
    struct node* next;     // NULL en el último nodo
} Node;

typedef struct list
{
    Node* head;            // primer nodo
    Node* tail;            // último nodo: agregar al final en O(1)
    int count;             // largo, para no recorrer la lista al consultarlo
} List;
```

## Operaciones

```c
List* list_init(void)
{
    return calloc(1, sizeof(List));          // head = tail = NULL, count = 0
}

void list_append(List* list, int value)      // O(1) gracias a tail
{
    Node* node = malloc(sizeof(Node));
    *node = (Node){.value = value, .next = NULL};
    if (!list->head) list->head = node;      // lista vacía: el nodo es la cabeza
    else list->tail->next = node;            // si no, se cuelga del último
    list->tail = node;
    list->count += 1;
}

void list_insert_after(List* list, Node* prev, int value)   // O(1)
{
    Node* node = malloc(sizeof(Node));
    *node = (Node){.value = value, .next = prev->next};     // 1. el nuevo apunta al siguiente
    prev->next = node;                                      // 2. el anterior apunta al nuevo
    if (list->tail == prev) list->tail = node;
    list->count += 1;
}

Node* list_at_index(List* list, int index)   // O(n): hay que seguir los punteros
{
    Node* current = list->head;
    for (int i = 0; i < index && current; i++) current = current->next;
    return current;                          // NULL si el índice no existe
}

void list_destroy(List* list)
{
    Node* current = list->head;
    while (current)
    {
        Node* next = current->next;          // guardar el siguiente ANTES de liberar
        free(current);
        current = next;
    }
    free(list);
}
```

```c
int main(void)
{
    List* list = list_init();
    list_append(list, 1); list_append(list, 5); list_append(list, 3); list_append(list, 10);
    list_print(list);                                    // 1 -> 5 -> 3 -> 10 -> NULL
    list_insert_after(list, list_at_index(list, 1), 7);
    list_print(list);                                    // 1 -> 5 -> 7 -> 3 -> 10 -> NULL
    list_destroy(list);                                  // 0 leaks
    return 0;
}
```

`list_print` recorre con `for (Node* n = list->head; n; n = n->next)`, que es la forma idiomática de iterar una lista en C: el ciclo termina cuando `n` llega a `NULL`.

> [!warning] El orden de los punteros importa
> En `list_insert_after`, si primero se hace `prev->next = node`, se pierde la referencia al resto de la lista. Siempre se enlaza primero el nodo nuevo con el siguiente y después el anterior con el nuevo. En `list_destroy` pasa lo mismo: hay que guardar `current->next` **antes** del `free`, porque leerlo después es un *use after free*.

> [!tip] Casos borde
> Toda operación sobre una lista debe probarse con la lista **vacía** (`head == NULL`), con **un solo** nodo y sobre el **último** nodo, que obliga a actualizar `tail`. Ahí aparecen la mayoría de los *segmentation faults*.

## Preguntas de repaso

> [!question]- ¿Para qué sirve guardar `tail` y `count` además de `head`?
> `tail` permite agregar al final en $O(1)$ sin recorrer la lista. `count` permite saber el largo en $O(1)$. Sin ellos, ambas operaciones serían $O(n)$.

> [!question]- ¿Qué pasa si en `list_destroy` se hace `free(current); current = current->next;`?
> Se lee `next` de un nodo ya liberado (*use after free*). Puede funcionar por casualidad o caerse, y Valgrind lo reporta como lectura inválida.

> [!question]- ¿Por qué `list_append` necesita el caso especial `if (!list->head)`?
> Porque en una lista vacía no hay un último nodo al que colgar el nuevo (`tail` es `NULL`). El nodo nuevo pasa a ser a la vez la cabeza y la cola.

> [!question]- ¿Cuál es la complejidad de `list_at_index(list, i)` y por qué?
> $O(i)$, que es $O(n)$ en el peor caso, porque hay que avanzar nodo por nodo desde la cabeza: los nodos no están contiguos y no se puede calcular la dirección del $i$-ésimo.
