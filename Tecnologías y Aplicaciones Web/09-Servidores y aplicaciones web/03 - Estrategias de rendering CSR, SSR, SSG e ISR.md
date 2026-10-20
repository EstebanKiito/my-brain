---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Servidores y aplicaciones web"
tags:
  - web
  - rendering
  - react
  - origen/complemento
prerrequisitos:
  - "[[02 - Frontend, backend y frameworks web]]"
  - "[[05 - Un proyecto React con npm y Vite]]"
---

# Estrategias de rendering: CSR, SSR, SSG e ISR

Alguien tiene que convertir los datos en HTML. Puede hacerlo el navegador, el servidor en cada request o el servidor una sola vez antes de publicar. Cada opción cambia cuánto tarda en verse la página, cuánto trabaja el servidor y qué tan bien la indexan los buscadores. Estas son las cuatro estrategias más comunes.

## CSR: Client Side Rendering

Es lo que hace una aplicación React creada con Vite. El servidor entrega un `index.html` casi vacío más el JavaScript, y el **navegador** construye la página.

![Client side rendering del build al navegador](adjuntos/Client%20side%20rendering%20del%20build%20al%20navegador.png)

> [!example]- Transcripción de la imagen
> Tres columnas. **Build**: `index.html`, `scripts.js` (con los *components*) y `styles.css`. **Static Server**: los mismos tres archivos, tal cual. **Runtime (Web Browser)**: el navegador recibe el `index.html` y, dentro de él, monta los componentes del script y aplica los estilos.

- **Ventajas**: muy útil cuando hay mucha interacción y solo cambian los datos; después de la carga, navegar es rápido.
- **Desventajas**: la carga inicial puede ser lenta, porque se envía mucho JavaScript, y la página empieza **en blanco** hasta que el script corre.

## SSR: Server Side Rendering

El **servidor** genera el HTML completo **en cada request**, con los datos actuales, y el navegador lo muestra de inmediato. Después el JavaScript "hidrata" la página para hacerla interactiva.

- **Ventajas**: sirve para páginas cuyos datos cambian seguido y deben estar al día en cada request, como perfiles de usuario o dashboards en tiempo real.
- **Desventajas**: como el render ocurre en el servidor en cada request, el servidor carga con más trabajo.

## SSG: Static Site Generation

El HTML de cada página se genera **una sola vez, al construir** (*build*) el sitio, y se sirve como archivos estáticos.

- **Ventajas**: es la alternativa más rápida, porque el HTML ya está listo, y la mejor para el **SEO** (optimización para buscadores).
- **Ideal para**: sitios de contenido estático, como blogs, portafolios y documentación.
- **Desventaja**: cualquier cambio de contenido exige volver a construir el sitio.

## ISR: Incremental Static Regeneration

Una combinación de SSG con actualización: las páginas se generan estáticamente, pero se **regeneran por separado** cada cierto tiempo o cuando cambian sus datos, sin reconstruir todo el sitio. Así se mantiene la velocidad del contenido estático con datos razonablemente actualizados.

## Comparación

| | Dónde se genera el HTML | Cuándo | Primera carga | Carga del servidor | Datos al día |
|---|---|---|---|---|---|
| **CSR** | Navegador | Al ejecutar el JS | Lenta, en blanco | Baja | Sí (vía API) |
| **SSR** | Servidor | En cada request | Rápida | Alta | Sí |
| **SSG** | Servidor | Una vez, en el build | La más rápida | Mínima | Solo hasta el siguiente build |
| **ISR** | Servidor | En el build y luego por página | Muy rápida | Baja | Con cierto desfase |

## Next.js

React por sí solo hace CSR. Para las otras estrategias se usa un **framework** sobre React, como **Next.js**: incluye las herramientas y la configuración que React necesita, y agrega estructura, funcionalidades (SSR, SSG, ISR, rutas) y optimizaciones. Lo creó Vercel, una empresa de publicación de aplicaciones front-end, y es público en GitHub desde 2016.

> [!warning] Primero React, después Next.js
> Next.js agrega conceptos encima de React (qué corre en el servidor y qué en el cliente). Sin dominar React, es difícil entender por qué algo falla.

> [!tip] Elegir según el contenido
> Contenido que casi no cambia: SSG. Contenido público que cambia de vez en cuando: ISR. Datos personales o en tiempo real: SSR. Aplicaciones muy interactivas detrás de un login: CSR.

## Preguntas de repaso

> [!question]- ¿Por qué una aplicación con CSR muestra una página en blanco al inicio?
> Porque el HTML que entrega el servidor está casi vacío: el contenido lo dibuja el JavaScript, que primero tiene que descargarse y ejecutarse.

> [!question]- ¿Por qué SSG es la mejor opción para SEO?
> Porque el HTML ya está generado con todo su contenido, así que un buscador lo lee directamente, sin ejecutar JavaScript, y además se sirve muy rápido.

> [!question]- ¿Qué costo tiene SSR frente a CSR?
> Más carga en el servidor, que debe generar el HTML en cada request. A cambio, la página llega lista y con datos actualizados.
