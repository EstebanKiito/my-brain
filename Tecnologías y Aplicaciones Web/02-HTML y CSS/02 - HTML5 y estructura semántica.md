---
ramo: "Tecnologías y Aplicaciones Web"
tema: "HTML y CSS"
tags:
  - web
  - html
  - html5
  - origen/complemento
prerrequisitos:
  - "[[01 - Anatomía de un documento HTML]]"
---

# HTML5 y estructura semántica

Antes de HTML5, casi toda página se armaba con `div`: un `div id="header"`, un `div id="menu"`, varios `div class="post"`. Funcionaba, pero el documento no decía qué era cada parte; solo lo sugerían los nombres que eligiera cada desarrollador. HTML5 agrega tags con **significado propio**, de modo que la estructura queda descrita en el mismo HTML.

## Tags semánticos

![Estructura HTML4 frente a HTML5 semántico](adjuntos/Estructura%20HTML4%20frente%20a%20HTML5%20sem%C3%A1ntico.png)

> [!example]- Transcripción de la imagen
> - **HTML4 Structure**: `div id="header"` arriba; a la izquierda `div id="menu"`; a la derecha dos `div class="post"`; abajo `div id="footer"`.
> - **HTML5 Structure**, la misma página con tags semánticos: `header`, `nav`, dos `article` y `footer`.

| Tag | Qué representa |
|---|---|
| `header` | Encabezado de la página o de una sección |
| `nav` | Bloque de navegación (menús, links principales) |
| `article` | Contenido independiente y reutilizable, como un post o una noticia |
| `aside` | Contenido lateral relacionado, como una barra lateral |
| `footer` | Pie de página o de sección |
| `figure` | Una figura (imagen, diagrama) con su descripción |
| `details` | Contenido que el usuario puede expandir |
| `progress` | Barra de progreso |

```html
<article>
  <header>
    <h1>Título del artículo</h1>
    <h4>Un subtítulo</h4>
    <p>Descripción o resumen.</p>
  </header>
</article>
```

> [!tip] Por qué importa la semántica
> Un lector de pantalla puede saltar directo al `nav` o al `article` principal, y un buscador entiende qué parte de la página es el contenido. Con `div` genéricos ambos tienen que adivinar. Además, el código es más fácil de leer.

## Otras novedades de HTML5

- **Audio y video nativos** con `<audio>` y `<video>`, sin plugins. Se ofrecen varias fuentes y el navegador usa la primera que soporte:

```html
<video controls autoplay>
  <source src="x.ogg" type="video/ogg" />
  <source src="x.mp4" type="video/mp4" />
  Navegador no soporta elemento video.
</video>
```

- **SVG nativo**: gráficos vectoriales escritos directamente en el HTML.

```html
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
</svg>
```

- **Almacenamiento en el cliente** con `localStorage` y `sessionStorage` (se detalla en el tema de almacenamiento en el cliente).
- La **API de WebSockets**, para comunicación bidireccional con el servidor.

Estas capacidades nativas son parte de por qué desaparecieron los plugins como Flash: casi todo lo que ofrecían ahora lo hace HTML5 de forma estándar, con un modelo de seguridad que controlan los propios navegadores.

> [!warning] El texto de respaldo no es decoración
> El texto dentro de `<video>` o `<audio>` solo aparece si el navegador no soporta el elemento. Es la forma de degradar con elegancia en lugar de mostrar un hueco vacío.

## Preguntas de repaso

> [!question]- ¿Qué gana una página al cambiar `div id="menu"` por `nav`?
> Que el significado queda en el propio tag: los lectores de pantalla, los buscadores y otros desarrolladores saben que es la navegación sin depender de un nombre de id elegido a mano.

> [!question]- ¿Por qué `<video>` admite varios `<source>`?
> Porque no todos los navegadores soportan los mismos formatos. El navegador recorre las fuentes en orden y reproduce la primera que puede decodificar.

> [!question]- ¿Cuándo corresponde usar `article` y cuándo `div`?
> `article` corresponde a contenido con sentido propio, que podría publicarse por separado (un post, una noticia). `div` es un contenedor sin significado, útil solo para agrupar elementos y aplicarles estilo.
