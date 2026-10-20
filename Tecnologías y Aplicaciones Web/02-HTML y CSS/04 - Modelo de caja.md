---
ramo: "Tecnologías y Aplicaciones Web"
tema: "HTML y CSS"
tags:
  - web
  - css
  - box-model
  - origen/complemento
prerrequisitos:
  - "[[03 - Reglas, selectores y cascada en CSS]]"
---

# Modelo de caja

Para el navegador, cada elemento HTML es un rectángulo. Saber cómo se calcula ese rectángulo explica la mayoría de las sorpresas de CSS: por qué un elemento de `200px` termina ocupando `260px`, o por qué dos elementos quedan más separados de lo esperado. El **modelo de caja** (*box model*) es esa caja que envuelve a todo elemento.

## Las cuatro capas

Desde afuera hacia adentro:

- **margin** (margen): distancia entre el exterior y el borde del elemento; es espacio transparente que lo separa de sus vecinos.
- **border** (borde): la frontera visible del elemento.
- **padding** (relleno): distancia entre el contenido y el borde; toma el color de fondo del elemento.
- **content** (contenido): el texto o la imagen, con su `width` y `height`.

![Modelo de caja en DevTools](adjuntos/Modelo%20de%20caja%20en%20DevTools.png)

> [!example]- Transcripción de la imagen
> - Panel de DevTools con cajas anidadas. **margin** vale 0 en los cuatro lados; **border** vale 20 en los cuatro lados; **padding** vale 10 en los cuatro lados; el contenido mide **200×50**.
> - Debajo: el tamaño total **260×110**, posición `static`.
> - "Box Model Properties": `box-sizing: content-box`, `display: block`, `float: none`, `line-height: normal`, `position: static` y `z-index: auto`.

## Cómo se calcula el tamaño

Con el valor por defecto `box-sizing: content-box`, `width` y `height` miden **solo el contenido**. El padding y el borde se suman por fuera:

$$\text{ancho total} = \text{width} + 2 \cdot \text{padding} + 2 \cdot \text{border}$$

En el ejemplo de la imagen: $200 + 2\cdot 10 + 2\cdot 20 = 260$ de ancho y $50 + 2\cdot 10 + 2\cdot 20 = 110$ de alto. El margen no cuenta en el tamaño del elemento, pero sí en el espacio que ocupa en la página.

```css
.caja {
  width: 200px;
  height: 50px;
  padding: 10px;
  border: 20px solid gray;
  margin: 0;
}
```

> [!tip] `box-sizing: border-box`
> Con `border-box`, `width` incluye el padding y el borde, y el contenido se achica para caber. Muchos proyectos lo aplican a todos los elementos porque hace que el tamaño declarado sea el tamaño real.

> [!warning] Padding o margin
> El padding agranda el área del elemento (con su fondo y su zona clickeable). El margin solo lo separa de los demás. Para "dar aire" dentro de un botón se usa padding; para separar dos botones, margin.

## Probar HTML y CSS

El panel de estilos de DevTools permite apagar, prender y editar propiedades en vivo y ver el modelo de caja de cualquier elemento. Para probar código propio hay tres opciones:

- Abrir un archivo `.html` local directamente en el navegador.
- Levantar un servidor local; Python trae uno por defecto: `python -m http.server`.
- Usar un editor en línea como Codepen.

Los navegadores siguen los mismos estándares, pero implementan algunas funcionalidades de forma levemente distinta. Conviene elegir uno con el que se tenga comodidad (atajos, DevTools, extensiones) y probar en los demás.

## Preguntas de repaso

> [!question]- Un elemento tiene `width: 300px`, `padding: 15px` y `border: 5px`. ¿Cuánto mide de ancho con `content-box` y con `border-box`?
> Con `content-box` mide $300 + 2\cdot15 + 2\cdot5 = 340$ px. Con `border-box` mide 300 px, y el contenido se reduce a $300 - 30 - 10 = 260$ px.

> [!question]- ¿Por qué el margen no tiene color de fondo y el padding sí?
> Porque el padding es parte del elemento (está dentro de su borde) y lo pinta su `background`. El margen está fuera del borde: es espacio que separa al elemento de sus vecinos.

> [!question]- ¿Para qué sirve levantar `python -m http.server` en vez de abrir el archivo directo?
> Para que el navegador cargue la página por HTTP, como en un sitio real. Algunas funcionalidades (cargar módulos de JavaScript, hacer `fetch` a archivos locales) no funcionan con el esquema `file:`.
