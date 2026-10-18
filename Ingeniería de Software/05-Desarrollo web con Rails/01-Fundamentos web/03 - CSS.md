---
ramo: Ingeniería de Software
tema: Fundamentos web
tags: [ingsoft/web, ingsoft/css, origen/apuntes]
prerrequisitos: ["[[02 - HTML|HTML]]"]
---
# CSS

CSS (*Cascading Style Sheets*) es el lenguaje de hojas de estilo que describe la **apariencia y el formato** de un documento HTML. HTML define la estructura; CSS, cómo se ve.

## Estilos externos
Los estilos se pueden definir en un archivo aparte, con extensión `.css`, y enlazarlo desde el `<head>` del HTML con `<link>`. Así un mismo archivo de estilos sirve para varias páginas:
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
Cada regla CSS tiene un **selector** (a qué elementos se aplica) y una lista de **propiedades** con sus valores, que definen cómo se muestran esos elementos:
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
Una regla se puede **reutilizar** asignando la misma clase a varios elementos HTML, aunque sean de distinto tipo. En CSS, la clase se selecciona con un punto (`.myClass`):
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
> `margin` es el espacio **fuera** del borde del elemento; `padding` es el espacio **dentro**, entre el borde y el contenido. En el ejemplo de la sección Atributos, `margin: 10px; padding: 5px;` separa el párrafo 10 px de sus vecinos y deja 5 px de fondo amarillo alrededor del texto.

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
