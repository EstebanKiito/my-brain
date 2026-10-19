---
ramo: "Tecnologías y Aplicaciones Web"
tema: "CSS moderno"
tags:
  - web
  - css
  - animaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Variables, anidamiento y selectores modernos]]"
  - "[[05 - DOM, CSSOM y critical rendering path]]"
---

# Animaciones en CSS

Un botón que cambia de color de golpe se siente brusco; uno que lo hace en 200 milisegundos se siente pulido. Las **animaciones en CSS** animan el paso de un estilo a otro, con control sobre la duración y sobre cómo cambia cada propiedad, sin escribir JavaScript. Hay tres herramientas: `transition`, `transform` y `animation` con `@keyframes`.

## `transition`: suavizar un cambio de estado

`transition` indica **cómo ocurre** el cambio entre dos estados de un elemento, por ejemplo entre su estado por defecto y `:hover`:

```css
.target {
  font-size: 2rem;
  background-color: palegoldenrod;
  transition: background-color 2s 500ms;   /* propiedad, duración, retraso */
}

.target:hover {
  background-color: darkorange;
}
```

En la forma abreviada, el primer tiempo es la **duración** (`transition-duration`) y el segundo, el **retraso** (`transition-delay`); ambos valen `0s` si se omiten. También se puede indicar la curva de aceleración, como `transition: margin-right 2s ease-in-out`, o animar todo con `transition: all 1s ease-out`.

## `transform`: mover, rotar y escalar

`transform` rota, escala, inclina o traslada un elemento, modificando su espacio de coordenadas:

```css
.a { transform: translate(120px, 50%); }     /* mover */
.b { transform: scale(2, 0.5); }             /* escalar en x e y */
.c { transform: rotate(0.5turn); }           /* rotar media vuelta */
.d { transform: skew(30deg, 20deg); }        /* inclinar */
.e { transform: scale(0.5) translate(-100%, -100%); }   /* combinar */
```

> [!tip] Animar `transform` y `opacity`
> `transform` y `opacity` no cambian el layout: el elemento sigue ocupando su lugar original, así que el navegador solo recompone la imagen y no recalcula las posiciones de toda la página. Por eso son las propiedades más baratas de animar; animar `width` o `margin` obliga a rehacer el layout en cada cuadro.

## `animation` y `@keyframes`

Para animaciones que no dependen de un cambio de estado (que se repiten o tienen varias etapas):

- **`@keyframes`** define qué estilos se aplican y **en qué momento** de la animación, con porcentajes.
- **`animation`** controla los tiempos (*timing*): duración, nombre, repeticiones y dirección.

```css
.element {
  animation: pulse 5s infinite;
}

@keyframes pulse {
  0% {
    background-color: #001F3F;
  }
  100% {
    background-color: #FF4136;
  }
}
```

La propiedad `animation` tiene una versión larga y una abreviada:

```css
/* Versión larga */
p {
  animation-duration: 3s;
  animation-name: slidein;
  animation-iteration-count: infinite;
  animation-direction: alternate;     /* ida y vuelta */
}

/* Abreviada */
p {
  animation: 3s infinite alternate slidein;
}
```

> [!warning] Respetar a quien prefiere menos movimiento
> Algunas personas sienten mareos con las animaciones. El sistema operativo permite pedir menos movimiento, y CSS lo detecta con `@media (prefers-reduced-motion: reduce)`, donde conviene desactivar o suavizar las animaciones.

## SVG animado

Los gráficos **SVG** viven dentro del DOM, así que sus elementos (`circle`, `path`) se pueden estilar y animar con las mismas herramientas de CSS. Es la base de muchas animaciones de íconos y logos.

## Preguntas de repaso

> [!question]- ¿Cuándo conviene `transition` y cuándo `@keyframes`?
> `transition` sirve para suavizar el paso entre dos estados que gatilla algo (un `:hover`, una clase agregada). `@keyframes` con `animation` sirve para animaciones autónomas, con varias etapas o que se repiten.

> [!question]- En `transition: background-color 2s 500ms`, ¿qué significa cada valor?
> Se anima la propiedad `background-color`, la transición dura 2 segundos y empieza después de un retraso de 500 milisegundos.

> [!question]- ¿Por qué animar `transform` es más eficiente que animar `margin-left`?
> Porque `transform` no afecta el layout: el navegador no recalcula las posiciones de los demás elementos, solo recompone la imagen. Cambiar `margin-left` obliga a recalcular el layout en cada cuadro de la animación.
