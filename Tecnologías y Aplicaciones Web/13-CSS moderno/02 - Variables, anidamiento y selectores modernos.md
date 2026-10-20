---
ramo: "Tecnologías y Aplicaciones Web"
tema: "CSS moderno"
tags:
  - web
  - css
  - origen/complemento
prerrequisitos:
  - "[[03 - Reglas, selectores y cascada en CSS]]"
  - "[[01 - Rendering entre navegadores y unidades CSS]]"
---

# Variables, anidamiento y selectores modernos

Durante años, CSS no tenía variables ni anidamiento: para eso existían preprocesadores como Sass. El CSS actual incorporó ambas cosas de forma nativa, además de muchos selectores nuevos. Así, cambiar el color principal de un sitio entero o escribir los estilos de un componente en un solo bloque ya no requiere herramientas extra.

## Variables (custom properties)

Las **variables CSS** (*custom properties*) definen valores que se reutilizan en el documento. Se declaran con dos guiones y se usan con `var()`:

```css
:root {
  --main-bg-color: brown;      /* :root es la pseudoclase global (el elemento html) */
  --espacio: 1rem;
}

details {
  background-color: var(--main-bg-color);
  padding: var(--espacio);
  color: var(--texto, black);  /* segundo argumento: valor por defecto */
}
```

El **selector donde se declara determina el scope**: una variable declarada en `:root` vale en todo el documento; una declarada en `section` solo vale dentro de las `section` y sus descendientes. Además, las variables participan de la cascada y se heredan.

> [!tip] Temas con variables
> Basta con redefinir las variables en un contexto para cambiar todo lo que las usa. Por ejemplo, `.oscuro { --main-bg-color: #111; }` cambia el fondo de todo lo que esté dentro de un elemento con clase `oscuro`, sin tocar ninguna otra regla.

## CSS anidado

El **anidamiento** (*nesting*) no agrega comportamiento nuevo, pero permite escribir los estilos de forma más legible, modular y mantenible, con menos selectores repetidos. La idea viene del preprocesador Sass:

```css
.card {
  padding: 1rem;

  & .titulo {          /* equivale a .card .titulo */
    font-size: 1.5rem;
  }

  &:hover {            /* equivale a .card:hover */
    box-shadow: 0 2px 8px gray;
  }
}
```

`&` representa al selector padre. Las dos formas, `parent { child {} }` y `parent { & child {} }`, el navegador las interpreta como `parent` y `parent child`.

## Selectores y combinadores modernos

| Selector | Selecciona |
|---|---|
| `A B` | Los `B` descendientes de `A` (a cualquier profundidad) |
| `A > B` | Los `B` hijos directos de `A` |
| `A + B` | El `B` inmediatamente después de `A` (hermano adyacente) |
| `A ~ B` | Todos los `B` hermanos que vienen después de `A` |
| `:nth-child(2n)` | Los hijos en posición par |
| `:not(.activo)` | Los elementos que no calzan con el selector |
| `:is(h1, h2, h3)` | Cualquiera de la lista (agrupa sin repetir) |
| `:has(img)` | Los elementos que **contienen** algo; es el primer selector de "padre" |

```css
/* Tarjetas que contienen una imagen: sin padding superior */
.card:has(img) { padding-top: 0; }
```

> [!warning] Lo nuevo puede no estar soportado
> Selectores como `:has()` o el anidamiento nativo son recientes. Antes de usarlos en producción hay que revisar en Can I Use si los navegadores del público objetivo los soportan.

## Preguntas de repaso

> [!question]- ¿Qué determina el scope de una variable CSS?
> El selector donde se declara: vale para ese elemento y sus descendientes. Declarada en `:root`, vale en todo el documento.

> [!question]- ¿A qué selector equivale `.menu { & > li {} }`?
> A `.menu > li`: los `li` que son hijos directos de un elemento con clase `menu`.

> [!question]- ¿Qué tiene de especial `:has()`?
> Permite seleccionar un elemento según lo que contiene, es decir, según sus descendientes. Hasta su llegada, CSS solo podía seleccionar "hacia abajo" o hacia los hermanos siguientes, nunca un padre según sus hijos.
