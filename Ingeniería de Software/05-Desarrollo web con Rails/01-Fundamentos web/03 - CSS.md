---
ramo: Ingeniería de Software
tema: Fundamentos web
tags: [ingsoft/web, ingsoft/css, origen/apuntes]
prerrequisitos: ["[[02 - HTML|HTML]]"]
---
# CSS

CSS (Cascading Style Sheets) es un lenguaje de hojas de estilo que se utiliza para describir la **apariencia y el formato** de un documento escrito en HTML.

A continuación, se destacan algunas características clave de CSS, junto con ejemplos de código:

## Estilos externos
Los estilos CSS pueden definirse en archivos separados con la extensión `.css` y enlazarse a los documentos HTML.

Ejemplo:
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="estilos.css">
    <title>Mi Página Estilizada</title>
</head>
<body>
    <h1>Hola Mundo</h1>
    <p>Este es un párrafo estilizado.</p>
</body>
</html>
```
```css
/* Archivo estilos.css */
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}
h1 {
    color: #333;
}
p {
    color: #666;
}
```

## Atributos
- Los atributos CSS definen cómo se deben mostrar los elementos HTML.
- Ejemplo:
```css
p {
    color: blue;
    font-size: 14px;
    background-color: yellow;
    margin: 10px;
    padding: 5px;
}
```

## Clases
- Las reglas de estilo CSS pueden **reutilizarse** asignando la misma clase a varios elementos HTML.
- Ejemplo:
```html
<div class="myClass">Este es un div con clase reutilizable.</div>
<p class="myClass">Este es un párrafo con la misma clase.</p>
```
```css
.myClass {
    color: red;
    font-weight: bold;
}
```

Estas características permiten a los desarrolladores crear y dar estilo a páginas web de manera eficiente y consistente.

> [!tip] Complemento — las tres formas de aplicar CSS (slides "HTML + CSS")
> | Forma | Cómo | Ejemplo |
> |---|---|---|
> | **Inline** | atributo `style` del elemento | `<h1 style="color:blue;">A Blue Heading</h1>` |
> | **Internal** | elemento `<style>` dentro de `<head>` | `<style> body {background-color: powderblue;} h1 {color: blue;} p {color: red;} </style>` |
> | **External** | elemento `<link>` a un archivo `.css` | `<link rel="stylesheet" href="styles.css">` |
>
> - **"Cascading"** significa que el estilo aplicado a un elemento padre **también se aplica a sus hijos** (herencia), y que cuando hay reglas en conflicto gana la más específica o la más cercana.
> - Con CSS se controlan el color, la fuente, el tamaño del texto, el espacio entre elementos y mucho más.
> - **Selectores básicos:** `p` (todos los `<p>`), `.clase` (atributo `class`), `#id` (atributo `id`).

> [!example] Ejemplo extra — márgenes y relleno
> `margin` es el espacio **fuera** del borde del elemento; `padding` es el espacio **dentro**, entre el borde y el contenido. En el ejemplo de los apuntes, `margin: 10px; padding: 5px;` separa el párrafo 10 px de sus vecinos y deja 5 px de fondo amarillo alrededor del texto.

## Preguntas de repaso

1. Nombra las tres formas de aplicar CSS a un HTML.
> [!question]- Respuesta
> Inline (atributo `style`), internal (etiqueta `<style>` en el `<head>`) y external (archivo `.css` enlazado con `<link>`).

2. ¿Cómo se aplica la misma regla a varios elementos distintos?
> [!question]- Respuesta
> Asignándoles la misma `class` y definiendo la regla con el selector `.nombreClase`.

3. ¿Qué significa "cascading" en CSS?
> [!question]- Respuesta
> Que los estilos se heredan de padres a hijos y que, cuando hay varias reglas para un mismo elemento, se resuelven por un orden de prioridad (especificidad y cercanía).
