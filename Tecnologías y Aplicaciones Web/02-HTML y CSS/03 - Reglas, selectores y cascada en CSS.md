---
ramo: "Tecnologías y Aplicaciones Web"
tema: "HTML y CSS"
tags:
  - web
  - css
  - origen/complemento
prerrequisitos:
  - "[[01 - Anatomía de un documento HTML]]"
---

# Reglas, selectores y cascada en CSS

HTML dice qué es cada cosa; falta decir cómo se ve. **CSS** (*Cascading Style Sheets*) es un lenguaje especializado en diseño gráfico (tampoco es un lenguaje de programación) que define el **estilo** de cada elemento. Es el complemento de HTML para la presentación, la visualización y el diseño de las páginas, y funciona con **reglas** que el navegador aplica sobre los elementos seleccionados.

## Brevísima historia

| Año | Hito |
|---|---|
| 1996 | CSS1, primera especificación del W3C: fuentes, colores, atributos de texto, alineamiento y posicionamiento |
| 1998 | CSS2, superconjunto de CSS1: más tipos de posicionamiento, `z-index` y *media types* |
| 1999 en adelante | CSS3 se divide en **módulos** que extienden CSS2 y que siguen evolucionando |
| 2007 en adelante | "CSS4" no existe como versión única: cada módulo avanza con sus propios niveles |
| 2012 y 2016 | Flexbox y Grid quedan estables y soportados por los navegadores |

## Anatomía de una regla

```css
selector {
  propiedad: valor;
}
```

Una regla puede tener varias **declaraciones** y aplicarse a varios selectores a la vez:

```css
p {
  width: 500px;
  border: 1px solid black;
}

p, li, h1 {
  color: red;
}
```

## Selectores

| Selector | Selecciona | Ejemplo |
|---|---|---|
| `elemento` | Todos los elementos de ese tag | `h1 { color: red; }` |
| `#id` | El elemento con ese `id` (único) | `#identificador { background-color: red; }` |
| `.clase` | Los elementos con esa clase | `.planta { color: green; }` |
| `[atributo]` | Los elementos según un atributo | `li[class^="a"] { font-size: 200%; }` (clase que empieza con "a") |
| `:pseudoclase` | Un estado del elemento | `a:hover { color: red; }` (mouse encima) |

## Tres formas de insertar CSS

1. **Externo**: un archivo `.css` enlazado desde el `head` con `<link rel="stylesheet" href="mi-estilo.css"/>`. Es la forma habitual, porque varias páginas comparten un mismo archivo.
2. **Interno**: reglas dentro de un `<style>` en el `head`, que aplican a esa página. Se usa poco, por ejemplo cuando no se pueden modificar los archivos externos.
3. **Inline**: el atributo `style` de un elemento, como `<p style="color:red;">Texto rojo</p>`.

> [!warning] CSS inline es mala práctica
> Mezcla estructura (HTML) con presentación (CSS), obliga a repetir el mismo estilo en cada elemento y hace que cambiar el diseño signifique editar todo el HTML.

## La cascada

Varias reglas pueden apuntar al mismo elemento. El navegador las aplica en **cascada** (la C de CSS), con prioridades:

1. Las reglas **inline** son las más prioritarias.
2. Luego las de CSS **externo e interno** (todo lo que está en el `head`).
3. Por último, el **estilo por defecto** del navegador.

Una regla inline sobrescribe las externas e internas, y estas sobrescriben los valores por defecto del navegador. Dentro de un mismo nivel, gana el selector más **específico** (un `#id` pesa más que una `.clase`, y esta más que un tag); si empatan, gana la regla que aparece **después**.

> [!tip] Herencia frente a cascada
> La cascada resuelve qué regla gana sobre un mismo elemento. La **herencia** es otra cosa: algunas propiedades, como `color` o `font-size`, pasan de un elemento padre a sus hijos si nadie las redefine.

En Ingeniería de Software está la introducción a CSS usada con Rails: [[03 - CSS|CSS]].

## Preguntas de repaso

> [!question]- ¿Por qué se prefiere CSS externo sobre inline?
> Porque un solo archivo define el estilo de todas las páginas y separa la presentación de la estructura. Cambiar el diseño significa editar ese archivo, no cada elemento del HTML.

> [!question]- Un `p` tiene `color: blue` en el CSS externo y `style="color: red"`. ¿De qué color se ve y por qué?
> Rojo: las reglas inline tienen la prioridad más alta en la cascada y sobrescriben las del CSS externo e interno.

> [!question]- ¿Qué selecciona `li[class^="a"]`?
> Los `li` cuyo atributo `class` empieza con la letra "a". Es un selector de atributo con el operador `^=`, que significa "comienza con".
