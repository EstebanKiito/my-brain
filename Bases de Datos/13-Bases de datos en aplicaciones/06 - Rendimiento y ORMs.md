---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, origen/complemento]
prerrequisitos: ["[[03 - ORMs|ORMs]]", "[[09 - Índices en bases de datos|Índices en bases de datos]]"]
---
# Rendimiento y ORMs

En una aplicación web lo más lento suele ser la base de datos, y muchas veces no por consultas pesadas sino por **muchas consultas chicas** que el ORM hace sin que se note (el problema N+1). Se arregla trayendo los datos relacionados en una sola consulta y midiendo antes de optimizar.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: Bases de Datos y desarrollo de software")
> - En una aplicación web, lo más lento generalmente es la base de datos (cuando no hay mucha lógica en el código).
> - Muchas veces la app no es lenta porque los datos estén mal modelados o la consulta sea muy pesada: **¡podríamos estar haciendo muchas consultas chicas!** (O podría faltar un índice.)
>
> **Ejemplo en Django:**
> ```python
> def my_view(request, article_id):
>     article = Article.objects.get(article_id)
>     return render(request, "my_view.html",
>                   {"article": article, "author": article.author})
> ```
> Hace **al menos dos consultas**: una para traer el artículo y otra para buscar el autor al pedir `article.author`. Juntas, con un join:
> ```python
> article = Article.objects.select_related("author").get(article_id)
> ```
> Para relaciones N-N o varias instancias relacionadas se usa `prefetch_related`. En Rails, el equivalente es `includes`/`preload`.
>
> **Medir antes de optimizar:** no se puede optimizar sin saber dónde está lo lento. En desarrollo se usan `django-debug-toolbar` o Rails Mini Profiler; en producción, herramientas de monitoreo (APM) como Scout o New Relic.
>
> **Idea clave:** para estimar el tiempo de una consulta contamos páginas leídas del disco ([[04 - Modelo de costos de IO|modelo de costos]]). Pero cuando la base está **al otro lado de una red**, la **cantidad de consultas** suele impactar más que su eficiencia. Eso no quita que haya que hacerlas bien.

> [!example] Ejemplo extra — el problema N+1
> ```python
> for article in Article.objects.all():   # 1 consulta
>     print(article.author.name)          # +1 consulta por cada artículo → N+1
> ```
> Con 100 artículos son 101 consultas. Con `Article.objects.select_related("author")` es **1** consulta con JOIN. Es el mismo argumento de la clase 4: optimizar el **número** de consultas más que cómo están escritas.

## Preguntas de repaso

1. ¿Qué es el problema N+1?
> [!question]- Respuesta
> Hacer una consulta para traer N objetos y luego una consulta extra por cada uno para traer un objeto relacionado: N+1 consultas en vez de 1 o 2.

2. ¿Cuántas consultas hace la vista de Django del ejemplo y cómo se reduce a una?
> [!question]- Respuesta
> Al menos dos (artículo y autor). Con `select_related("author")` se traen juntos con un join.

3. ¿Por qué el número de consultas puede importar más que su costo en I/O?
> [!question]- Respuesta
> Porque cada consulta a una base remota paga la latencia de la red y la conexión. Muchas consultas chicas pueden tardar más que una sola consulta más pesada.
