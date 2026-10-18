---
ramo: Ingeniería de Software
tema: Fundamentos web
tags: [ingsoft/web, ingsoft/html, origen/apuntes]
prerrequisitos: ["[[01 - Protocolo HTTP|Protocolo HTTP]]"]
---
# HTML

HTML (HyperText Markup Language) es el lenguaje de marcado utilizado para **estructurar y presentar contenido en la web**. Esta nota recorre sus elementos principales: estructura de la página, enlaces, imágenes, listas y atributos.

## Estructuras
HTML usa **etiquetas** para definir y organizar los elementos y las secciones de una página. Toda página tiene un `<head>` (metadatos, como el título de la pestaña) y un `<body>` (el contenido visible), que a su vez se divide en secciones como `<header>`, `<div>` y `<footer>`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página Web</title>
</head>
<body>
    <header>
        <h1>Bienvenidos a Mi Página Web</h1>
    </header>
    <div>
        <p>Este es el contenido principal de la página.</p>
    </div>
    <footer>
        <p>&copy; 2024 Mi Página Web</p>
    </footer>
</body>
</html>
```

## Enlaces
Los enlaces se crean con la etiqueta `<a>`, y el atributo `href` indica la URL de destino:
```html
<a href="https://www.example.com">Visita Example</a>
```

## Imágenes
Las imágenes se incorporan con la etiqueta `<img>`. El atributo `src` indica dónde está la imagen y `alt` es el texto alternativo que se muestra si no carga:
```html
<img src="imagen.jpg" alt="Descripción de la imagen">
```

## Listas
HTML tiene listas ordenadas (`<ol>`, numeradas) y no ordenadas (`<ul>`, con viñetas); cada elemento va en un `<li>`. Ejemplo de lista ordenada:
```html
<ol>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
</ol>
```

## Atributos de las etiquetas
Los atributos entregan información adicional sobre un elemento. Los más usados son `class` (agrupa elementos para darles estilo con CSS) e `id` (identifica un elemento único):
```html
<div class="contenedor">
    <p id="parrafoPrincipal">Este es un párrafo dentro de un contenedor.</p>
</div>
```

> [!tip] Complemento (slides "HTML + CSS")
> - **Estructura de una etiqueta:** `<p>` (etiqueta de apertura) + contenido + `</p>` (etiqueta de cierre) = **elemento** `p`.
> - **Listas sin numeración:** `<ul><li>Coffee</li><li>Tea</li><li>Milk</li></ul>`; **enumeradas:** `<ol>…</ol>`.
> - **Énfasis en textos:** `<i>` itálica, `<b>` negrita, `<em>` énfasis, `<strong>` importante, `<small>`, `<del>` tachado, `<ins>` insertado, `<sub>` subíndice, `<sup>` superíndice, `<mark>` resaltado.
> - **Atributos de `<img>`:** `src`, `alt`, `width`, `height`, `style`. Cada tag admite atributos distintos y uno solo pone los que necesita.
> - **Etiquetas semánticas:** `<header>` (cabecera de una página o sección) y `<footer>` (pie, por ejemplo con autor y contacto).
> - **Tablas:**
> ```html
> <table style="width:100%">
>   <tr><th>Company</th><th>Contact</th><th>Country</th></tr>
>   <tr><td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Germany</td></tr>
> </table>
> ```
> - **Detalles:** nunca dejes tags incompletos (cada tag que se abre debe cerrarse). Los tags HTML **no distinguen mayúsculas**: `<P>` es igual a `<p>`.
> - Documentación completa: https://www.w3schools.com/
> - Formularios: ver [[04 - Formularios HTML|Formularios HTML]]; estilos: ver [[03 - CSS|CSS]].

## Preguntas de repaso

1. ¿Qué atributo indica el destino de un enlace y cuál la ubicación de una imagen?
> [!question]- Respuesta
> `href` en `<a>` para el destino; `src` en `<img>` para la imagen (y `alt` para el texto alternativo).

2. ¿Qué diferencia hay entre `<ol>` y `<ul>`?
> [!question]- Respuesta
> `<ol>` es una lista ordenada (numerada); `<ul>` es una lista sin numeración (con viñetas). En ambas, los ítems van en `<li>`.

3. ¿Para qué sirven los atributos `class` e `id`?
> [!question]- Respuesta
> Identifican elementos: `class` agrupa varios elementos (para reutilizar estilos CSS) e `id` identifica un elemento único en la página.
