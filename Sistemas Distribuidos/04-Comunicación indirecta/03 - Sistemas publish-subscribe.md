---
ramo: "Sistemas Distribuidos"
tema: "Comunicación indirecta"
tags:
  - sd/comunicacion-indirecta
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - Colas de mensajes]]"
---

# Sistemas publish-subscribe

En una cola, el productor deja un mensaje para que **un** consumidor lo procese. En un sistema **publish-subscribe**, el emisor publica **eventos** y el sistema los entrega a **todos** los interesados, según filtros que cada suscriptor declaró. Nadie conoce a nadie: publicadores y suscriptores solo conocen al sistema.

## Funcionamiento

![Sistema publish-subscribe con publicadores y suscriptores](adjuntos/Sistema%20publish-subscribe%20con%20publicadores%20y%20suscriptores.png)

> [!example]- Transcripción de la imagen
> Tres publicadores a la izquierda envían `publish(e1)`, `publish(e2)` y `advertise(t1)` al *Sistema Publish-subscribe*. A la derecha, dos suscriptores envían `subscribe(t1)` y `subscribe(t2)`, y el sistema entrega `notify(e1)` a un suscriptor.

- Los **publicadores** envían eventos (mensajes) a un servicio intermediario.
- Los **suscriptores** expresan interés en eventos mediante **filtros**.
- El sistema **compara** cada evento con los filtros y lo entrega a los suscriptores correspondientes.
- Puede garantizar **desacoplamiento temporal** si el sistema asegura la **persistencia** de los mensajes; eso depende de la implementación.

No hay que pensar en colas visibles (aunque por dentro pueda haber colas ocultas y filtros): el publicador manda y el suscriptor recibe.

## Operaciones básicas

| Operación | Quién la usa | Qué hace |
|---|---|---|
| `publish(e)` | Publicador | Envía el evento `e` |
| `subscribe(f)` | Suscriptor | Expresa interés en los eventos que cumplan el filtro `f` |
| `unsubscribe(f)` | Suscriptor | Revoca el interés en `f` |
| `notify(e)` | Sistema | Entrega el evento `e` a un suscriptor |
| `advertise(f)` *(opcional)* | Publicador | Declara el tipo de eventos (filtro `f`) que generará en el futuro |

## Modelos de suscripción

El filtro es la forma de expresar interés, y puede basarse en:

- **Channel-based:** los publicadores envían a **canales con nombre** y los suscriptores se suscriben a un canal completo. Es lo más parecido a una cola.
- **Topic-based:** cada evento trae un campo de **tema** (tópico), y la suscripción se basa en ese tema.
- **Content-based:** filtros más expresivos, que son **consultas sobre los valores de los atributos** del evento y permiten coincidencias más complejas.

Un filtro también puede mezclar los tres. Con las discusiones de GitHub del curso:

| Modelo | Suscripción |
|---|---|
| Channel-based | Todas las discusiones del curso |
| Topic-based | Solo las discusiones de la categoría "Tareas" |
| Content-based | Solo las discusiones que contengan "uwu" |

## Ejemplo en Python

Un broker mínimo en memoria, con los tres tipos de filtro como funciones:

```python
class Broker:
    def __init__(self):
        self.suscripciones = []                     # (filtro, callback)

    def subscribe(self, filtro, callback):
        self.suscripciones.append((filtro, callback))

    def publish(self, evento):
        for filtro, callback in self.suscripciones:
            if filtro(evento):                      # el broker compara evento y filtro
                callback(evento)                    # notify

broker = Broker()
canal = lambda e: e["canal"] == "discussions"
topico = lambda e: canal(e) and e["categoria"] == "Tareas"
contenido = lambda e: canal(e) and "uwu" in e["texto"]
```

Al publicar una discusión de "Tareas" la reciben los suscriptores del canal y del tópico. Al publicar "slides uwu" en otra categoría, la reciben los del canal y los del contenido.

## Heterogeneidad

Publish-subscribe busca la **heterogeneidad**: permite que interoperen componentes que **no fueron diseñados para trabajar juntos**, siempre que puedan publicar y suscribirse a eventos. El intermediario funciona como un traductor entre dos personas que no hablan el mismo idioma.

> [!warning] Cola frente a publish-subscribe
> En una cola, cada mensaje lo procesa **un** consumidor (se reparte el trabajo). En publish-subscribe, cada evento llega a **todos** los suscriptores cuyo filtro coincide (se difunde la información).

## Preguntas de repaso

> [!question]- ¿Para qué sirve `advertise` si es opcional?
> Permite que el sistema sepa de antemano qué tipos de eventos producirá un publicador, para preparar el enrutamiento o avisar a los suscriptores interesados. No es necesario para que funcione la entrega.

> [!question]- ¿Por qué el filtro content-based es el más expresivo y también el más costoso?
> Porque evalúa consultas sobre los valores de cada evento, en vez de comparar solo un nombre de canal o un tópico. Eso permite intereses muy específicos, pero obliga al sistema a examinar el contenido de cada evento contra cada filtro.

> [!question]- ¿Cómo ayuda publish-subscribe a integrar sistemas heterogéneos?
> Los componentes solo necesitan publicar y suscribirse a eventos con un formato acordado; no necesitan conocerse ni compartir interfaces. Así, sistemas hechos por separado pueden reaccionar a los mismos eventos.
