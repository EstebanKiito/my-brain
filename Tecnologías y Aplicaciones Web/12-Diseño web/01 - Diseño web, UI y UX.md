---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Diseño web"
tags:
  - web
  - diseno
  - ui
  - ux
  - origen/complemento
prerrequisitos:
  - "[[02 - HTML5 y estructura semántica]]"
  - "[[01 - React, JSX y Virtual DOM]]"
---

# Diseño web, UI y UX

Que una aplicación funcione no basta: si el usuario no entiende dónde hacer click, no encuentra lo que busca o se cansa leyendo, la aplicación fracasa igual. El **diseño web** se ocupa de esa parte, y conviene distinguir sus dos caras, la interfaz (UI) y la experiencia (UX), antes de pasar al código.

## Interfaces

Una **interfaz** es el punto de contacto entre las máquinas y los usuarios. Hoy la gran mayoría son **interfaces gráficas**: se interactúa con elementos visuales en pantalla, como botones, selectores, menús y campos de texto.

## Qué es el diseño web

El **diseño web** es el diseño de la experiencia y de la interfaz de un sitio durante su desarrollo, más que su implementación en código. Sus temas principales son:

- la **identidad visual**: el color, la tipografía y las imágenes;
- el **layout**: cómo se estructura y categoriza la información;
- la **comunicación clara del contenido**: no confundir al usuario y guiar su experiencia.

## UI frente a UX

- **UI** (*User Interface*): la interactividad y el aspecto (*look*) de un producto, una aplicación o una página.
- **UX** (*User Experience*): la experiencia completa del usuario al usar e interactuar con el producto.

![Tareas de UX designers y UI designers](adjuntos/Tareas%20de%20UX%20designers%20y%20UI%20designers.png)

> [!example]- Transcripción de la imagen
> Tabla "UX vs. UI designers":
> - **UX designer**: diseña la interacción, traza el recorrido del usuario (*user pathway*), planifica la arquitectura de información y es experto en *wireframes*, prototipos e investigación.
> - **UI designer**: diseña lo visual, elige color y tipografía, planifica la estética y es experto en *mockups*, gráficos y layouts.

> [!tip] Una forma de recordarlo
> La UX decide **qué pasos** sigue el usuario y en qué orden. La UI decide **cómo se ve** cada uno de esos pasos. Una interfaz preciosa con un flujo confuso es buena UI y mala UX.

## Prototipado

Antes de programar, conviene **prototipar**: dibujar la interfaz para discutirla y corregirla cuando cambiarla todavía es barato.

- **Wireframe**: esquema de baja fidelidad, solo cajas y textos, para definir la estructura.
- **Mockup**: diseño visual de alta fidelidad, con colores, tipografía e imágenes.
- **Prototipo**: un mockup navegable, que simula la interacción.

Herramientas recomendadas:

- **Figma**: herramienta gráfica colaborativa, la recomendada para diseñar y esquematizar interfaces.
- **Canva**: plataforma de diseño gráfico con herramientas para múltiples tipos de diseño.

## Fuentes de inspiración

| Sitio | Para qué |
|---|---|
| **Web Design Museum** | Ver versiones antiguas de sitios y aplicaciones |
| **Interaction Museum** | Técnicas de interacción basadas en investigación de HCI (interacción humano-computador) |
| **Dribbble** | Compartir trabajos de diseño y ver los de otros |
| **Awwwards** | Un sitio destacado cada día por su diseño |

> [!warning] Diseñar después de programar sale caro
> Cambiar un rectángulo en Figma toma segundos. Cambiar un flujo ya implementado en React y Express obliga a rehacer componentes, rutas y a veces el modelo de datos. Por eso el diseño va antes del código.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre UI y UX?
> La UI es el aspecto y la interactividad de cada pantalla (colores, tipografía, botones). La UX es la experiencia completa: si el usuario logra su objetivo, en cuántos pasos y con cuánta fricción.

> [!question]- ¿Para qué sirve un wireframe si después se hará un diseño completo?
> Para acordar la estructura y el flujo sin distraerse con colores ni detalles visuales. Es rápido de hacer y de cambiar, y evita pulir visualmente una pantalla que quizá ni siquiera hace falta.

> [!question]- ¿Cuáles son los tres temas centrales del diseño web?
> La identidad visual (color, tipografía, imágenes), el layout (cómo se organiza la información) y la comunicación clara del contenido (guiar al usuario sin confundirlo).
