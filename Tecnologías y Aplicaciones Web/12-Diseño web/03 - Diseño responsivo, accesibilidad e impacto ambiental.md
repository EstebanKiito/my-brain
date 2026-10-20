---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Diseño web"
tags:
  - web
  - diseno
  - accesibilidad
  - responsive
  - origen/complemento
prerrequisitos:
  - "[[02 - Jerarquía visual, patrones e identidad visual]]"
---

# Diseño responsivo, accesibilidad e impacto ambiental

Una misma aplicación web se usa desde un monitor de 27 pulgadas, un celular en el metro, un lector de pantalla o una conexión lenta. Diseñar bien implica considerar a todos esos usuarios. Además de la identidad visual, el diseño web enfrenta tres desafíos permanentes: el **diseño responsivo**, la **accesibilidad** y el **impacto ambiental**.

## Diseño responsivo

Un diseño **responsivo** se adapta al dispositivo en que se muestra. Hay dos dimensiones:

**Distintas resoluciones.** El layout se reorganiza según el ancho de la pantalla:

![Rangos de resolución en diseño responsivo](adjuntos/Rangos%20de%20resoluci%C3%B3n%20en%20dise%C3%B1o%20responsivo.png)

> [!example]- Transcripción de la imagen
> "Responsive Design": un monitor y un notebook bajo el rango **1024+ px**, con layout de varias columnas; una tablet horizontal y una vertical bajo **1023 - 768 px**; y dos celulares bajo **767 - 320 px**, con el contenido apilado en una sola columna.

**Distintas formas de interactuar.** No es lo mismo un mouse, preciso y con *hover*, que un dedo, impreciso y sin *hover*, o un teclado. En pantallas táctiles, los botones necesitan un tamaño mínimo y el contenido no puede depender del *hover* para mostrarse.

> [!tip] Mobile first
> Diseñar primero para la pantalla más pequeña obliga a decidir qué es esencial; después se agregan columnas y detalles para pantallas grandes. En CSS se implementa con *media queries* y layouts flexibles (Flexbox y Grid).

## Accesibilidad

Un sitio está bien diseñado e implementado **si incluso personas con algún tipo de discapacidad pueden usarlo**: visual, auditiva, motriz o cognitiva. En la práctica, la accesibilidad suele subestimarse, implementarse mal o directamente no considerarse.

Prácticas básicas:

- **Contraste suficiente** entre el texto y el fondo. Las pautas WCAG piden al menos **4.5:1** para texto normal.
- **Texto alternativo** (`alt`) en las imágenes, para los lectores de pantalla.
- **HTML semántico** (`nav`, `main`, `button`, `label`), que las tecnologías de asistencia entienden.
- **Navegación con teclado**: todo lo que se hace con el mouse debe poder hacerse con Tab y Enter.
- **No transmitir información solo con el color**; por ejemplo, un error marcado en rojo debe tener además un texto.

Herramientas para evaluarla:

- **WebAIM Contrast Checker**: calcula el contraste entre dos colores y si cumple las pautas.
- **WAVE**: evalúa la accesibilidad de una página completa y marca los problemas sobre ella.

> [!warning] La accesibilidad no es un extra
> Muchos usuarios la necesitan de forma permanente (ceguera, baja visión) y todos en algún momento (sol sobre la pantalla, un brazo enyesado). Agregarla al final es mucho más caro que considerarla desde el diseño.

## Impacto ambiental

Toda interacción en internet consume electricidad, en los centros de datos, en la red y en el dispositivo, y por lo tanto genera emisiones de carbono. El avance tecnológico tiene un efecto en el cambio climático que no se puede ignorar.

Hay prácticas que reducen la energía necesaria para servir una aplicación web, y muchas coinciden con hacer la navegación más simple y directa:

- imágenes comprimidas y en formatos modernos, cargadas solo cuando se ven;
- menos JavaScript y menos dependencias;
- uso de caché para no repetir descargas;
- flujos más cortos, para que el usuario llegue antes a lo que busca.

## Preguntas de repaso

> [!question]- ¿Por qué el diseño responsivo considera la forma de interactuar y no solo el tamaño de pantalla?
> Porque un dedo es menos preciso que un mouse y no tiene *hover*. Un diseño que depende de pasar el cursor por encima, o que usa botones diminutos, falla en pantallas táctiles aunque se vea bien.

> [!question]- Nombra tres prácticas de accesibilidad y a quién ayuda cada una.
> El texto alternativo en las imágenes ayuda a quienes usan lector de pantalla. El contraste suficiente ayuda a personas con baja visión (y a cualquiera bajo el sol). La navegación con teclado ayuda a quienes no pueden usar un mouse.

> [!question]- ¿Por qué mejorar el rendimiento de un sitio también reduce su impacto ambiental?
> Porque menos datos transferidos y menos procesamiento significan menos energía consumida en servidores, redes y dispositivos, y con ello menos emisiones.
