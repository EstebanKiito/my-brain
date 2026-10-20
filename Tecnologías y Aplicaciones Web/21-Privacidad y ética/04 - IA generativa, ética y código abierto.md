---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Privacidad y ética"
tags:
  - web
  - etica
  - ia
  - open-source
  - origen/complemento
prerrequisitos:
  - "[[03 - Ética en computación y el código de la ACM]]"
  - "[[01 - IA, ML, DL y modelos de lenguaje]]"
---

# IA generativa, ética y código abierto

Hace pocos años, generar texto convincente era una capacidad que sus propios creadores consideraban peligrosa. Hoy cualquiera la tiene en el celular. Esta nota cierra la reflexión ética del ramo con los problemas que trae la IA generativa y con una forma concreta de usar el software para el bien: contribuir al código abierto.

## De peligrosa a accesible

En febrero de 2019, OpenAI anunció **GPT-2**, un sistema que genera texto de calidad similar al humano. Al principio no lo publicó completo, por temor a su mal uso: puede escribir artículos, noticias, historias, poemas e incluso código, y por lo tanto inventar noticias, falsificar textos y engañar. Pocos años después, herramientas mucho más capaces, como ChatGPT, están disponibles para cualquier persona.

## Problemas de la IA generativa

- **Propiedad intelectual**: los modelos se entrenan con millones de obras protegidas por derechos de autor, sin el consentimiento explícito de sus creadores. Las imágenes "al estilo Studio Ghibli" hicieron visible el problema.
- **Autoría**: ¿de quién es lo que genera el modelo? ¿De quien escribió el prompt, de la empresa del modelo o de los autores de los datos de entrenamiento?
- **Consumo de recursos**: entrenar y usar estos modelos consume mucha energía y agua. Según estimaciones citadas en la clase, una sola consulta a ChatGPT gasta el equivalente a una botella de agua de 500 ml, y que entrenar GPT-3 emitió tanto CO₂ como unos 125 vuelos de ida y vuelta entre Nueva York y Beijing.
- **Uso en contextos sensibles**: educación, salud, justicia o contratación, donde un error o un sesgo afecta a personas reales.

> [!warning] ¿Quién hizo este trabajo?
> En la clase, el profesor "confesó" que la había hecho completamente con IA, para luego decir que era mentira, ¿o no? Que ya no sea posible distinguir a simple vista plantea preguntas difíciles, por ejemplo qué deberían hacer las instituciones educativas al respecto.

## ¿Y ahora qué?

Puede parecer que el software es sobre todo peligroso, pero lo opuesto también es cierto: el mundo puede ser mejor y el software puede usarse para el bien. Lo importante es ser **consciente de que el propio código tiene un impacto**, y que decidir si ese impacto es positivo o negativo depende de quien lo escribe. Los casos de ética en computación de Santa Clara University y el curso *CS106S: Coding for Social Good* de Stanford son buenos puntos de partida.

## Código abierto

El **software de código abierto** (*open source software*, OSS) publica su código para que cualquiera lo use, lo estudie, lo modifique y lo comparta, según su licencia. Buena parte de lo usado en el ramo lo es: Node.js, React, Express, PostgreSQL, Chromium (la base de Google Chrome, aunque no Chrome mismo) y VS Code. GitHub es un buen lugar para encontrar proyectos donde contribuir.

> [!tip] Etiqueta para contribuir
> - **Ser respetuoso**: del otro lado hay personas.
> - **Recordar que los mantenedores suelen ser voluntarios**.
> - **Preguntar antes de hacer**: antes de trabajar en un PR, confirmar que esa contribución será bienvenida.
> - **Reportar bugs** de forma descriptiva, comprensiva y proactiva.
> - **Respetar la licencia**: es la base legal del código abierto.

## Preguntas de repaso

> [!question]- ¿Por qué OpenAI no publicó GPT-2 completo al principio?
> Por temor a su mal uso: generaba texto tan convincente que podía usarse para producir noticias falsas, falsificar textos y engañar a escala.

> [!question]- ¿Qué problemas de propiedad intelectual plantea la IA generativa?
> Que los modelos se entrenan con obras protegidas sin consentimiento de sus autores, y que no está claro quién es dueño de lo generado: el usuario, la empresa del modelo o los autores originales.

> [!question]- ¿Por qué conviene preguntar antes de abrir un PR en un proyecto de código abierto?
> Porque los mantenedores, muchas veces voluntarios, pueden no querer ese cambio o tener otro plan. Preguntar evita trabajo perdido y respeta el tiempo de quienes revisan.
