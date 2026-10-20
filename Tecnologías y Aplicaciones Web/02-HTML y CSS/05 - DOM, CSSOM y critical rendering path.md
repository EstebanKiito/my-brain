---
ramo: "Tecnologías y Aplicaciones Web"
tema: "HTML y CSS"
tags:
  - web
  - dom
  - cssom
  - rendering
  - origen/complemento
prerrequisitos:
  - "[[02 - HTML5 y estructura semántica]]"
  - "[[04 - Modelo de caja]]"
---

# DOM, CSSOM y critical rendering path

El navegador recibe texto: bytes de HTML y de CSS. Para dibujar una página tiene que convertir ese texto en estructuras que pueda recorrer, combinarlas y calcular dónde va cada píxel. Ese proceso explica por qué JavaScript puede modificar una página ya cargada y por qué ciertos cambios de estilo son más caros que otros.

## DOM: el HTML como árbol

La representación interna de un documento HTML se llama **DOM** (*Document Object Model*). Es un modelo jerárquico en forma de **árbol**: cada tag y cada texto es un **nodo**, y el árbol se arma según el anidamiento de la página a partir del tag `html`. Lo estandariza el W3C.

![Construcción del DOM desde los bytes](adjuntos/Construcci%C3%B3n%20del%20DOM%20desde%20los%20bytes.png)

> [!example]- Transcripción de la imagen
> Cinco etapas de arriba hacia abajo:
> 1. **Bytes**: `3C 62 6F 64 79 3E 48 65 6C 6C 6F…` (hexadecimal).
> 2. **Characters**: `<html><head>…</head><body><p>Hello <span>web performance</span>…`.
> 3. **Tokens**: `StartTag: html`, `StartTag: head`, `EndTag: head`, `StartTag: body`, `StartTag: p`, `Hello`…
> 4. **Nodes**: html, head, meta, body, p, "Hello".
> 5. **DOM**: `html` con hijos `head` (con `meta` y `link`) y `body`. `body` tiene un `p` (con el texto "Hello,", un `span` con "web performance" y el texto "students") y un `div` con un `img`.

## CSSOM: el CSS como árbol

Así como existe el DOM para HTML, existe el **CSSOM** (*CSS Object Model*) para CSS. El navegador toma todo el CSS y arma otro árbol con los selectores definidos. Ese árbol es lo que hace funcionar la **cascada** (cada nodo hereda las propiedades de su padre y agrega o sobrescribe las suyas) y lo que permite leer y modificar estilos desde JavaScript. También lo estandariza el W3C.

![Árbol CSSOM con propiedades heredadas](adjuntos/%C3%81rbol%20CSSOM%20con%20propiedades%20heredadas.png)

> [!example]- Transcripción de la imagen
> - `body` tiene `font-size: 16px`.
> - Sus hijos `p`, `span` e `img` heredan `font-size: 16px` (en gris claro, porque viene del padre). Además, `p` agrega `font-weight: bold`, `span` agrega `color: red` e `img` agrega `float: right`.
> - El `span` dentro de `p` hereda `font-size: 16px` y `font-weight: bold`, y agrega `display: none`.
> - Nota al costado: la propiedad del *parent* aparece en gris claro.

## Critical rendering path

Una vez que llegan las requests y se construyen el DOM y el CSSOM, faltan tres pasos para ver la página:

![Critical rendering path](adjuntos/Critical%20rendering%20path.png)

> [!example]- Transcripción de la imagen
> Desde **Network** salen tres flechas: HTML → DOM, CSS → CSSOM y una directa a JavaScript. DOM, JavaScript y CSSOM confluyen en **Render Tree**, que sigue a **Layout** y luego a **Paint**. Todo el recorrido está rotulado como "Critical rendering path".

1. **Render tree**: combina DOM y CSSOM, e incluye **solo lo visible**. Un nodo con `display: none` (como el `span` del ejemplo) no entra.
2. **Layout**: calcula la posición y el tamaño exactos de cada elemento. Aquí actúa el [[04 - Modelo de caja|modelo de caja]].
3. **Paint**: dibuja los elementos píxel a píxel en la pantalla.

> [!tip] Por qué importa el orden
> Cambiar un color solo obliga a repintar (paint). Cambiar un tamaño o agregar un elemento obliga a recalcular el layout de todo lo que se ve afectado y luego repintar, lo que es más caro. Por eso las animaciones fluidas evitan modificar propiedades de layout.

> [!warning] `display: none` frente a `visibility: hidden`
> `display: none` saca el nodo del render tree: no ocupa espacio. `visibility: hidden` lo deja en el layout ocupando su lugar, pero no lo pinta.

El DOM se vuelve el protagonista cuando JavaScript lo modifica; eso se ve en el tema de DOM y eventos.

## Preguntas de repaso

> [!question]- ¿Por qué el navegador convierte el HTML en un árbol en vez de dibujarlo directo desde el texto?
> Porque el árbol refleja el anidamiento de los elementos, que determina la herencia de estilos y la posición en la página. Además es una estructura que JavaScript puede consultar y modificar, y que el navegador puede recorrer cada vez que algo cambia.

> [!question]- ¿Qué aporta el CSSOM al funcionamiento de la cascada?
> Al organizar el CSS como árbol, cada nodo puede heredar las propiedades de su padre y sobrescribir solo las que define. Así el estilo final de un elemento se obtiene recorriendo el árbol, en vez de reunir todas las reglas a mano.

> [!question]- ¿Qué etapa del critical rendering path se repite al cambiar `width` y cuál al cambiar `color`?
> Cambiar `width` obliga a repetir el layout (y después el paint), porque cambian tamaños y posiciones. Cambiar `color` solo requiere repintar.
