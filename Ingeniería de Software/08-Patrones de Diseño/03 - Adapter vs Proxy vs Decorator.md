---
ramo: Ingeniería de Software
tema: Patrones de Diseño
tags: [ingsoft/patrones, patron/estructural, origen/complemento]
prerrequisitos: ["[[03 - Patrón Adapter|Patrón Adapter]]", "[[05 - Patrón Proxy|Patrón Proxy]]", "[[01 - Patrón Decorator|Patrón Decorator]]"]
---
# Adapter vs Proxy vs Decorator

> [!tip] Complemento — nota nueva (comparación a partir de las notas de cada patrón)
> **Qué es:** los tres **envuelven** a otro objeto y le delegan las llamadas, así que el código se ve casi igual. La diferencia está en **la intención** y en **la interfaz**.
>
> | | [[03 - Patrón Adapter\|Adapter]] | [[05 - Patrón Proxy\|Proxy]] | [[01 - Patrón Decorator\|Decorator]] |
> |---|---|---|---|
> | Intención | **traducir** una interfaz incompatible | **controlar el acceso** al objeto real | **agregar** comportamiento |
> | Interfaz que expone | **distinta** a la del envuelto (la que espera el cliente) | **la misma** que el real | **la misma** que el decorado |
> | ¿Cambia el resultado? | traduce los datos o la llamada | normalmente no (filtra, cachea, registra) | sí, lo **extiende** (más costo, más texto) |
> | ¿Se apilan? | rara vez | rara vez | **sí**, varios decoradores uno sobre otro |
> | ¿Quién crea al envuelto? | se lo pasan | a menudo lo crea o controla el proxy (lazy loading) | se lo pasan |
> | Ejemplo del curso | RUT con puntos → `login_user` sin puntos | log de logins fallidos | pizza con toppings, abrigos |
>
> **Pregunta clave en la prueba:**
> - ¿El cliente y el servicio "hablan idiomas distintos"? → **Adapter**.
> - ¿Mismo idioma, pero quiero vigilar, filtrar o retrasar el acceso? → **Proxy**.
> - ¿Mismo idioma y quiero sumar funcionalidad combinable? → **Decorator**.
>
> El [[04 - Ejercicio - Proxy y Adapter en mensajería|ejercicio de WeChat]] pide implementar un Proxy y un Adapter sobre el mismo `Contact`. Fíjate que el adaptador ahí **mantiene** la interfaz (`receiveMessage`) pero **transforma los datos**: también se considera adaptación, porque traduce el contenido.

## Preguntas de repaso

1. ¿Cuál de los tres cambia la interfaz del objeto envuelto?
> [!question]- Respuesta
> El Adapter: expone la interfaz que espera el cliente, distinta de la del objeto adaptado. Proxy y Decorator mantienen la misma interfaz.

2. Quieres que un servicio de imágenes descargue la imagen solo la primera vez que se pide. ¿Qué patrón?
> [!question]- Respuesta
> Proxy (proxy virtual o de caché): misma interfaz, controla cuándo se crea o consulta el objeto real.

3. Quieres agregar compresión y luego encriptación a un stream, combinables en cualquier orden. ¿Qué patrón?
> [!question]- Respuesta
> Decorator: cada funcionalidad es un decorador con la misma interfaz y se pueden apilar.
