---
ramo: "Programación en C"
tema: "Structs"
tags:
  - c
  - structs
  - punteros
  - heap
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición e inicialización de structs]]"
  - "[[02 - Paso por valor y punteros como referencia]]"
---

# Punteros a structs y operador flecha

En la práctica, los structs se manejan casi siempre **a través de punteros**. Hay dos razones. Pasar un struct por valor copia todos sus campos y la función trabaja sobre la copia. Y los structs que deben sobrevivir a la función que los crea, como los nodos de una lista, tienen que vivir en el [[01 - Stack frente a heap|heap]], que solo se alcanza con punteros.

## Por valor frente a por puntero

```c
typedef struct account
{
    int balance;
} Account;

void add_copia(Account account, int amount)   { account.balance += amount; }
void add_balance(Account* account, int amount) { account->balance += amount; }

int main(void)
{
    Account acc = {.balance = 0};
    add_copia(acc, 100);
    printf("%d\n", acc.balance);    // 0: se modificó una copia que murió con la función
    add_balance(&acc, 100);
    printf("%d\n", acc.balance);    // 100
    return 0;
}
```

Es la misma regla del [[02 - Paso por valor y punteros como referencia|paso por valor]]: para que una función modifique un struct, tiene que recibir su dirección. Además, una copia de un struct grande en cada llamada gasta stack y tiempo.

## El operador flecha `->`

Con un puntero `p` a un struct, el campo `x` se alcanza con `(*p).x`: primero se desreferencia y después se accede al campo. Los paréntesis son obligatorios, porque `.` tiene más precedencia que `*`. Como esto se escribe todo el tiempo, C tiene un atajo:

> [!tip] Regla
> `p->x` es exactamente `(*p).x`. Se usa **punto** con un struct y **flecha** con un **puntero** a struct.

```c
Account* h = malloc(sizeof(Account));   // struct en el heap: en el stack queda solo h
*h = (Account){.balance = 5};           // inicializar la memoria apuntada
h->balance += 1;                        // acceder y modificar con flecha
printf("%d %d\n", h->balance, (*h).balance);   // 6 6
free(h);
```

| Se tiene | Para leer el campo | Ejemplo |
|---|---|---|
| Un struct `s` | `s.campo` | `acc.balance` |
| Un puntero `p` a struct | `p->campo` | `h->balance` |
| Un arreglo de structs `A` | `A[i].campo` | `diego.dogs[0].name` |
| Un puntero a puntero `pp` | `(*pp)->campo` | poco habitual |

> [!warning] `p->campo` con `p` sin inicializar
> `Account* h; h->balance = 0;` compila, pero escribe en una dirección basura. Antes de usar la flecha, el puntero tiene que apuntar a algo válido: un `malloc`/`calloc` o la dirección de un struct existente.

## Preguntas de repaso

> [!question]- ¿Por qué `add_copia(acc, 100)` deja `acc.balance` en 0?
> Porque C pasa una copia del struct completo. La función modifica la copia, que vive en su propio marco del stack y se descarta al retornar.

> [!question]- ¿Qué significa `p->x` en términos de `*` y `.`?
> `(*p).x`: desreferenciar el puntero para obtener el struct y después tomar su campo `x`.

> [!question]- ¿Por qué `*p.x` no es lo mismo que `(*p).x`?
> Porque el operador `.` tiene más precedencia que `*`. `*p.x` se interpreta como `*(p.x)`: busca un campo `x` en el puntero (que no tiene campos) y lo desreferencia. Por eso existe la flecha.

> [!question]- ¿Dónde vive un struct creado con `malloc(sizeof(Account))` y qué queda en el stack?
> El struct vive en el heap. En el stack queda solo la variable puntero, con su dirección.
