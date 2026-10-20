---
ramo: "Tecnologías y Aplicaciones Web"
tema: "CSS moderno"
tags:
  - web
  - css
  - layout
  - flexbox
  - grid
  - origen/complemento
prerrequisitos:
  - "[[04 - Modelo de caja]]"
  - "[[02 - Variables, anidamiento y selectores modernos]]"
---

# Flexbox y Grid

Durante mucho tiempo, centrar un elemento o armar columnas en CSS requería trucos con `float` y márgenes. **Flexbox** (2012) y **Grid** (2016) resolvieron el layout de verdad. Cada uno se diseñó con una fortaleza distinta, y elegir entre ellos depende sobre todo de cuántas dimensiones tiene lo que se quiere ordenar.

![Flexbox en una dimensión y Grid en dos](adjuntos/Flexbox%20en%20una%20dimensi%C3%B3n%20y%20Grid%20en%20dos.png)

> [!example]- Transcripción de la imagen
> **Flexbox**, *one-dimensional layout*: tres cajas (roja, verde, amarilla) alineadas en una fila. **Grid**, *multi-dimensional layout*: una caja amarilla y una verde apiladas a la izquierda, y una caja roja alta a la derecha que ocupa dos filas.

## Flexbox

El módulo **Flexbox Layout** distribuye y alinea elementos dentro de un contenedor de forma eficiente, incluso cuando su tamaño es desconocido o dinámico. Trabaja en **una dimensión**: una fila o una columna.

![Contenedor e items en Flexbox](adjuntos/Contenedor%20e%20items%20en%20Flexbox.png)

> [!example]- Transcripción de la imagen
> Izquierda: un rectángulo morado rotulado **container** que contiene tres cajas naranjas. Derecha: la misma figura con las tres cajas señaladas como **items**.

Las propiedades se reparten entre el **contenedor** y los **items**:

```css
.barra {
  display: flex;                    /* el contenedor se vuelve flex */
  flex-direction: row;              /* eje principal: row o column */
  justify-content: space-between;   /* alineación en el eje principal */
  align-items: center;              /* alineación en el eje cruzado */
  gap: 1rem;                        /* espacio entre items */
  flex-wrap: wrap;                  /* bajar de línea si no caben */
}

.barra .buscador {
  flex: 1;                          /* este item crece y toma el espacio sobrante */
}
```

> [!tip] Centrar en dos líneas
> `display: flex; justify-content: center; align-items: center;` centra el contenido horizontal y verticalmente, el problema clásico que antes requería trucos.

## Grid

El módulo **Grid Layout** es un layout **bidimensional**: controla filas y columnas a la vez. Un elemento puede ocupar desde una celda hasta un **área** (el espacio entre cuatro líneas de la grilla).

```css
.pagina {
  display: grid;
  grid-template-columns: 200px 1fr;          /* barra lateral fija + contenido flexible */
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "nav    main"
    "footer footer";
  gap: 1rem;
}
header { grid-area: header; }
nav    { grid-area: nav; }
main   { grid-area: main; }
footer { grid-area: footer; }

.galeria {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));  /* columnas que se adaptan al ancho */
}
```

La unidad `fr` representa una **fracción del espacio disponible**: `1fr 2fr` reparte el espacio en tercios.

## Cuál usar

| Si los elementos… | Usar |
|---|---|
| van **en línea**, en una sola dimensión (una barra de navegación, los botones de una tarjeta) | **Flexbox** |
| forman **filas y columnas** (el layout de la página, una galería) | **Grid** |

No hay una regla única: es criterio de quien programa. Una guía útil es **Grid para el layout de la página y Flexbox para los componentes**, y considerar también la responsividad: cómo se reordenan los elementos en distintos tamaños de pantalla. Para practicar están las guías de CSS-Tricks y las interactivas de Josh W. Comeau.

> [!warning] Las propiedades van en el contenedor
> `justify-content`, `align-items` y `grid-template-columns` se escriben en el **padre** que tiene `display: flex` o `display: grid`, no en los hijos. Ponerlas en el hijo es un error muy común.

## Preguntas de repaso

> [!question]- ¿Qué diferencia fundamental hay entre Flexbox y Grid?
> Flexbox ordena en una dimensión (una fila o una columna) y deja que el contenido defina los tamaños. Grid define filas y columnas a la vez y ubica los elementos en esa grilla.

> [!question]- ¿Qué hace `flex: 1` en un item?
> Le permite crecer para ocupar el espacio sobrante del contenedor. Si varios items tienen `flex: 1`, se reparten ese espacio en partes iguales.

> [!question]- ¿Qué logra `repeat(auto-fill, minmax(150px, 1fr))`?
> Crea tantas columnas de al menos 150px como quepan en el ancho disponible, y reparte el resto del espacio entre ellas. La galería se vuelve responsiva sin media queries.
