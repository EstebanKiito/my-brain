---
ramo: "Tecnologías y Aplicaciones Web"
tema: "CSS moderno"
tags:
  - web
  - css
  - navegadores
  - origen/complemento
prerrequisitos:
  - "[[05 - DOM, CSSOM y critical rendering path]]"
  - "[[03 - Diseño responsivo, accesibilidad e impacto ambiental]]"
---

# Rendering entre navegadores y unidades CSS

Un mismo HTML con el mismo CSS no siempre se ve igual en todas partes: cada navegador dibuja con su propio motor, cada sistema operativo agrega sus detalles y cada pantalla tiene otro tamaño. Antes de pasar a las herramientas modernas de CSS conviene entender de dónde salen esas diferencias y elegir unidades de medida que se adapten.

## Motores de rendering

Así como cada navegador tiene un motor de JavaScript, tiene también un **motor de rendering** que convierte HTML y CSS en píxeles:

| Motor | Navegadores |
|---|---|
| **Blink** | Chrome, Edge, Opera, Brave |
| **Gecko** | Firefox |
| **WebKit** | Safari |

Aunque todos siguen los estándares del W3C, cada motor implementa y soporta las funcionalidades de forma levemente distinta: márgenes por defecto, tipografías, controles de formulario. También hay diferencias entre **sistemas operativos**; por ejemplo, las barras de desplazamiento ocupan espacio en Windows y se superponen al contenido en macOS.

## Normalizar el punto de partida

Cada navegador aplica una **hoja de estilos por defecto** (el último nivel de la cascada). Un **reset CSS** anula esos valores (márgenes, paddings, tamaños de títulos) para que todos los navegadores partan del mismo estado:

```css
*, *::before, *::after { box-sizing: border-box; }
body, h1, h2, p, ul { margin: 0; padding: 0; }
img { display: block; max-width: 100%; }
```

> [!tip] Revisar el soporte antes de usar
> **Can I Use** (caniuse.com) muestra qué versiones de cada navegador soportan una funcionalidad de CSS o de JavaScript. Es lo primero que se revisa antes de usar algo nuevo.

## Unidades de medida

| Tipo | Unidad | Relativa a |
|---|---|---|
| **Absoluta** | `px` | Un píxel de referencia; no cambia |
| **Relativa** | `em` | El tamaño de fuente del **elemento padre** |
| **Relativa** | `rem` | El tamaño de fuente de la **raíz** (`html`, normalmente 16px) |
| **Relativa** | `vw`, `vh` | El 1% del **ancho** o del **alto** de la ventana (*viewport*) |
| **Relativa** | `%` | El tamaño de la propiedad equivalente del padre |

![Escala tipográfica en rem y px](adjuntos/Escala%20tipogr%C3%A1fica%20en%20rem%20y%20px.png)

> [!example]- Transcripción de la imagen
> Una escala tipográfica con clases nombradas como aviones, de mayor a menor: `.text-747` = 2.5rem = 40px; `.text-777` = 2rem = 32px; `.text-787` = 1.5rem = 24px; `.text-767` = 1.25rem = 20px; `.text-757` = 1rem = 16px; `.text-crj200` = 1rem = 16px (en mayúsculas). Cada fila muestra un titular de ejemplo en ese tamaño.

La equivalencia de la figura supone una raíz de 16px: $1\,\text{rem} = 16\,\text{px}$, así que $2.5\,\text{rem} = 40\,\text{px}$.

> [!tip] Por qué preferir `rem` a `px` en el texto
> Si un usuario aumenta el tamaño de letra de su navegador (por ejemplo, por baja visión), todo lo definido en `rem` crece en proporción. Lo definido en `px` queda fijo e ignora su preferencia.

> [!warning] `em` se acumula
> Como `em` es relativo al padre, anidar elementos con `font-size: 1.2em` multiplica el tamaño en cada nivel: $1.2 \times 1.2 \times 1.2 \approx 1.73$ veces. `rem` evita ese efecto porque siempre se refiere a la raíz.

## Preguntas de repaso

> [!question]- ¿Por qué un mismo CSS puede verse distinto en Chrome y en Safari?
> Porque usan motores de rendering distintos (Blink y WebKit), con estilos por defecto y detalles de implementación diferentes, y porque el sistema operativo también influye (fuentes, barras de desplazamiento).

> [!question]- Con una raíz de 16px, ¿cuánto mide `1.5rem`? ¿Y `1.5em` dentro de un padre de 20px?
> `1.5rem` mide $1.5 \times 16 = 24$ px. `1.5em` mide $1.5 \times 20 = 30$ px, porque `em` se calcula sobre la fuente del padre.

> [!question]- ¿Para qué sirve un reset CSS?
> Para eliminar los estilos por defecto de cada navegador y partir del mismo estado en todos, de modo que las diferencias que queden sean solo las del CSS propio.
