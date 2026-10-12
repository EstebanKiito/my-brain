---
ramo: Ingeniería de Software
tema: Fundamentos web
tags: [ingsoft/web, ingsoft/html, origen/apuntes]
prerrequisitos: ["[[02 - HTML|HTML]]", "[[01 - Protocolo HTTP|Protocolo HTTP]]"]
---
# Formularios HTML

Un formulario HTML permite a los usuarios **ingresar y enviar datos** al servidor (en un request HTTP, normalmente `POST`).

## Formulario
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="estilos.css">
    <title>Ejemplo de Formulario</title>
</head>
<body>
    <form action="/submit" method="post">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre"><br><br>
        <label for="email">Correo Electrónico:</label><br>
        <input type="email" id="email" name="email"><br><br>
        <label for="mensaje">Mensaje:</label><br>
        <textarea id="mensaje" name="mensaje"></textarea><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```

## Combo box (menú desplegable)
Un menú desplegable permite a los usuarios **seleccionar una opción de una lista**.
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="estilos.css">
    <title>Ejemplo de Combo Box</title>
</head>
<body>
    <form action="/submit" method="post">
        <label for="opciones">Selecciona una opción:</label><br>
        <select id="opciones" name="opciones">
            <option value="opcion1">Opción 1</option>
            <option value="opcion2">Opción 2</option>
            <option value="opcion3">Opción 3</option>
        </select><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```

> [!tip] Complemento — anatomía de un formulario (slides "HTML + CSS")
> - `action`: la **URL** a la que se envían los datos. `method`: el **método HTTP** (`get` o `post`).
> - `name`: la **clave** con que llega cada dato al servidor (`nombre=Ana&email=...`). Sin `name`, el dato no se envía.
> - `label for="x"` se asocia al input con `id="x"`: al hacer clic en el texto se enfoca el campo.
> - **Tipos de entrada:**
>   | Tipo | Descripción |
>   |---|---|
>   | `<input type="text">` | campo de texto de una línea |
>   | `<input type="radio">` | botón de radio (elegir **una** de varias opciones) |
>   | `<input type="checkbox">` | casilla (elegir **cero o más** opciones) |
>   | `<input type="submit">` | botón para enviar el formulario |
>   | `<input type="button">` | botón clickeable |
> - **Otros tipos:** button, checkbox, color, date, datetime-local, email, file, hidden, image, month, number, password, radio, range, reset, search, submit, tel, text (por defecto), time, url, week.
> - En Rails, los formularios se generan con *form helpers* (`form_with`), que producen este mismo HTML.

## Preguntas de repaso

1. ¿Qué indican los atributos `action` y `method` de un `<form>`?
> [!question]- Respuesta
> `action` es la URL a la que se envían los datos; `method` es el método HTTP que se usa (`get` o `post`).

2. ¿Qué diferencia hay entre `radio` y `checkbox`?
> [!question]- Respuesta
> Con radio se elige una sola opción de un grupo; con checkbox se pueden marcar cero o varias.

3. ¿Qué elemento HTML crea un combo box y cómo se define cada opción?
> [!question]- Respuesta
> `<select>`, con cada opción en `<option value="...">texto</option>`.

4. ¿Para qué sirve el atributo `name` de un input?
> [!question]- Respuesta
> Es la clave con que el dato llega al servidor. Sin `name`, el valor del campo no se envía.
