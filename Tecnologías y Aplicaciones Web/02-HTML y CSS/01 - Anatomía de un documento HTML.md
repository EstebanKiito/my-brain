---
ramo: "Tecnologías y Aplicaciones Web"
tema: "HTML y CSS"
tags:
  - web
  - html
  - origen/complemento
prerrequisitos:
  - "[[04 - Mensajes HTTP y versiones del protocolo]]"
---

# Anatomía de un documento HTML

Lo que el servidor entrega en el body de una response HTTP, la mayoría de las veces, es un documento HTML. **HTML** (*HyperText Markup Language*) es un **lenguaje de marcado**, no de programación: no tiene variables ni ciclos. Su trabajo es definir el **significado y la estructura** del contenido web, marcando con **etiquetas** (*tags*) de qué se trata cada texto y qué información adicional tiene cada elemento.

```html
<p class="mi-planta">Mi planta es muy verde y tiene 5 años</p>
<img src="./planta.jpeg" alt="Foto de mi planta" width="200px"/>
```

## Brevísima historia

| Año | Versión o hito |
|---|---|
| 1991 | HTML "1": Tim Berners-Lee publica una lista de 18 tags |
| 1994 | Se crea el W3C (*World Wide Web Consortium*) |
| 1995-1997 | HTML 2: estandariza lo que ya existía para "equilibrar el terreno" entre navegadores |
| 1997 | HTML 3.2: la primera versión desarrollada y estandarizada por el W3C |
| 1997-2014 | HTML 4.0: soporte para CSS y JavaScript |
| 2014 en adelante | HTML5: más accesible y semántico; es el que se usa hoy |

## Anatomía de un elemento

Un **elemento** se forma con un tag de apertura, el contenido y un tag de cierre. Los **atributos** van en el tag de apertura y le dan propiedades con un valor:

```html
<etiqueta atributo="valor">Contenido</etiqueta>
```

Los elementos se pueden **anidar**, lo que da una sintaxis clara y fácil de *parsear*:

```html
<p>Mi planta es <strong>muy</strong> verde</p>
```

También existen **elementos vacíos**, sin contenido ni tag de cierre, como `<img src="./planta.jpeg" alt="Foto de mi planta"/>` o `<br>`.

## El esqueleto de un documento

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Título de la pestaña</title>
  </head>
  <body>
    <p>Contenido</p>
  </body>
</html>
```

- `<!DOCTYPE html>` le indica al navegador cómo parsear el documento (como HTML moderno, según el W3C).
- `html` es el **nodo raíz**.
- `head` contiene lo que no se ve: título, metadatos y links a documentos auxiliares (hojas de estilo, scripts).
- `<meta charset="utf-8">` declara la codificación del documento; sin ella, las tildes y la ñ pueden verse mal.
- `title` es el título de la página que aparece en la pestaña.
- `body` contiene todo lo que se quiere mostrar.

## Tags más usados

| Tag | Uso |
|---|---|
| `h1` … `h6` | Encabezados o títulos de sección, de mayor a menor nivel |
| `p` | Párrafo de texto |
| `div` | Contenedor genérico (se usa mucho para aplicar CSS) |
| `em`, `b`, `i` | Énfasis, negrita e itálica |
| `ul`, `ol`, `li` | Lista no ordenada, lista ordenada (numerada) y cada ítem |
| `a` | *Anchor*: enlace a otra página (`href`), incluso `mailto:` |
| `img` | Imagen incrustada (`src`, `alt`) |
| `br` | Salto de línea |
| `select`, `option` | Menú desplegable y sus opciones |
| `form`, `input` | Formulario e inputs de tipo `text`, `password`, `checkbox`, `radio`, `submit`… |
| `<!-- … -->` | Comentario |

La referencia completa está en la documentación de elementos HTML de MDN. El navegador permite ver el HTML de cualquier página: el código fuente con Ctrl+U, o la request que lo trajo en la pestaña *Network* de DevTools.

> [!tip] Marcar según el significado
> Para escribir HTML se parte del contenido y se pregunta qué **es** cada parte: un título de sección es un `h2`, una introducción es un `p` y una enumeración es un `ul` con sus `li`. El aspecto visual se decide después, con CSS.

> [!warning] HTML no es un lenguaje de programación
> HTML describe estructura; no decide nada ni repite nada. La lógica la aporta JavaScript y la presentación la aporta CSS.

En Ingeniería de Software está la versión de este tema usada con Rails: [[02 - HTML|HTML]] y [[04 - Formularios HTML|Formularios HTML]].

## Preguntas de repaso

> [!question]- ¿Qué va en `head` y qué va en `body`, y por qué se separan?
> En `head` van los metadatos que el navegador necesita para procesar la página (codificación, título, hojas de estilo); en `body`, el contenido visible. Separarlos permite que el navegador configure el documento antes de mostrar nada.

> [!question]- ¿Por qué un `<img>` no tiene tag de cierre?
> Porque es un elemento vacío: no envuelve contenido. Toda su información (la ruta, el texto alternativo) va en los atributos.

> [!question]- ¿Para qué sirve `<!DOCTYPE html>`?
> Le indica al navegador que el documento es HTML moderno y que debe parsearlo según el estándar actual, en vez de usar modos de compatibilidad antiguos.
