---
ramo: "Tecnologías y Aplicaciones Web"
tema: "CSS moderno"
tags:
  - web
  - css
  - frameworks
  - design-system
  - origen/complemento
prerrequisitos:
  - "[[02 - Variables, anidamiento y selectores modernos]]"
  - "[[02 - Jerarquía visual, patrones e identidad visual]]"
---

# Frameworks de CSS y design systems

Escribir todo el CSS desde cero en cada proyecto es lento y produce estilos inconsistentes. Hay tres familias de herramientas para evitarlo: **frameworks** con estilos listos (Bootstrap), **preprocesadores** que extienden el lenguaje (Sass, Less) y frameworks de **clases utilitarias** (Tailwind). A escala de una organización, todo eso se ordena en un **design system**.

## Bootstrap: componentes listos

**Bootstrap** es un framework de front-end con estilos y componentes ya hechos (botones, grillas, formularios, modales). Se incluye su CSS y su JS (por ejemplo, desde un CDN) y se usan sus **clases**:

```html
<div class="container mt-5">
  <h1 class="text-primary">Hello, Bootstrap!</h1>
  <button class="btn btn-success">Click Me</button>
</div>
```

Es rápido para prototipar, pero los sitios hechos con Bootstrap tienden a verse parecidos si no se personaliza.

## Preprocesadores: Sass y Less

**Sass** y **Less** extienden CSS con variables, anidamiento, funciones y mixins. Se escribe en su sintaxis (`.scss`, `.less`) y se **compila** a CSS normal, que es lo que se enlaza en el HTML.

```scss
// card.scss
@use 'sass:color';

$primary-color: #3498db;
$padding: 1rem;

.card {
  background: color.adjust($primary-color, $lightness: 20%);
  padding: $padding;

  .card-title {
    font-size: 1.5rem;
    color: $primary-color;
  }
}
```

```css
/* CSS generado */
.card {
  background: rgb(54.37%, 76.85%, 91.91%);   /* el azul, 20% más claro */
  padding: 1rem;
}
.card .card-title {
  font-size: 1.5rem;
  color: #3498db;
}
```

```less
// button.less
@primary-color: #e74c3c;
@padding: 8px;

.button {
  background-color: @primary-color;
  padding: @padding (2 * @padding);       // compila a: padding: 8px 16px;
  &:hover {
    background-color: lighten(@primary-color, 10%);   // compila a: #ed7669
  }
}
```

> [!tip] ¿Siguen siendo necesarios?
> Variables y anidamiento ya existen en CSS nativo. Los preprocesadores siguen aportando funciones de color, mixins, ciclos y la división en muchos archivos, pero agregan un paso de compilación.

## Tailwind: clases utilitarias

**Tailwind CSS** es un framework de **clases utilitarias** predefinidas: cada clase aplica una sola propiedad (`p-6` es un padding, `rounded-xl` un borde redondeado, `text-indigo-600` un color), y el diseño se arma combinándolas directamente en el HTML:

```html
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4">
  <h2 class="text-xl font-bold text-indigo-600">Hello, Tailwind!</h2>
  <p class="text-gray-500">Quick utility-first styling.</p>
</div>
```

> [!warning] Utilitarias no es lo mismo que inline
> Se parece a escribir estilos inline, pero las clases vienen de una escala fija de tamaños y colores, así que el diseño sigue siendo consistente. A cambio, el HTML se llena de clases.

Fuera de CSS, librerías como **Three.js** permiten gráficos 3D en el navegador con JavaScript (escenas, cámaras y mallas dibujadas con WebGL).

## Design systems

Un **design system** es un conjunto de estándares para diseñar y construir **a escala**, con un lenguaje común y consistencia visual en muchas páginas y canales. Reúne la identidad visual, los componentes reutilizables y las reglas de uso. Ejemplos:

- **Material Design** (Google): guías y componentes para diseñar interfaces.
- **El design system de Fintual**, desarrollado por Design Systems International, una consultora de diseño digital con presencia en Chile.
- **Guías de marca** como las de Redis.

**Storybook** es una herramienta para crear, documentar y probar cada componente de un design system por separado. Para practicar CSS de forma lúdica existe **CSSBattle**, donde se intenta replicar imágenes solo con CSS.

## Preguntas de repaso

> [!question]- ¿Qué tienen que hacer Sass y Less antes de que el navegador pueda usar sus estilos?
> Compilarse a CSS normal. El navegador no entiende la sintaxis de los preprocesadores; solo carga el `.css` generado.

> [!question]- ¿Qué diferencia hay entre el enfoque de Bootstrap y el de Tailwind?
> Bootstrap entrega componentes completos (`btn btn-success`) con un diseño ya decidido. Tailwind entrega clases de una sola propiedad para armar un diseño propio.

> [!question]- ¿Qué aporta un design system a una organización grande?
> Consistencia y velocidad: todos los equipos usan los mismos componentes, colores y reglas, así que los productos se ven coherentes y nadie rediseña desde cero un botón que ya existe.
