---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - definiciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Anatomía de una URL]]"
  - "[[04 - Mensajes HTTP y versiones del protocolo]]"
---

# Páginas, sitios y aplicaciones web

"Página", "sitio" y "aplicación" se usan como sinónimos en el lenguaje cotidiano, pero en el curso tienen significados precisos. La distinción importa porque el resto del ramo trata de pasar de páginas estáticas a **aplicaciones web** completas, con frontend, backend y base de datos.

## Cuatro definiciones

| Término | Definición | Ejemplo |
|---|---|---|
| **Página web** | Un documento que se puede visualizar en un navegador; tiene **una** URL | Un perfil específico de Facebook; la lista de códigos de estado de MDN |
| **Sitio web** | Una colección de páginas web relacionadas (enlazadas entre sí) bajo un mismo dominio | Todo lo que vive bajo `netflix.com`; Wikipedia |
| **Servidor web** | El computador que aloja un sitio web en Internet y responde las requests | La máquina que atiende `uc.cl` |
| **Aplicación web** | Un programa con el que se interactúa a través de un navegador | Un correo web, un sistema de inscripción de cursos |

> [!tip] La URL como criterio
> Una página es un solo documento y por eso tiene una única URL. Un sitio agrupa muchas URLs bajo el mismo dominio. Por eso "Facebook es una página web" está mal dicho: Facebook es un **sitio** (y una aplicación); un perfil concreto sí es una página.

## Dónde corre una aplicación web

La lógica principal de una aplicación web clásica corre en el **servidor**: el navegador le envía requests, el servidor procesa, consulta datos y responde, y el usuario ve el resultado. El navegador ejecuta solo lo necesario para la comunicación y el *rendering* de lo que recibe.

Esta frontera se va a mover durante el curso. Con JavaScript, y luego con React, una parte creciente de la lógica de interfaz se ejecuta en el navegador, mientras el servidor expone datos mediante una API. Aun así, la regla de fondo se mantiene: los datos y las decisiones que importan (permisos, validaciones definitivas) viven en el servidor.

```mermaid
flowchart LR
    U[Usuario] --> N[Navegador<br/>HTML, CSS, JS]
    N -- request HTTP --> S[Servidor web<br/>lógica de la aplicación]
    S --> D[(Base de datos)]
    S -- response HTTP --> N
```

## ¿Se puede montar un servidor en casa?

Sí. Cualquier computador conectado a Internet puede servir páginas; no hace falta un permiso especial. Lo que sí hay que resolver es que las conexiones de afuera lleguen a esa máquina: configurar el firewall y el router. El certificado solo hace falta para ofrecer HTTPS.

El router de una casa recibe las conexiones en su IP pública y no sabe a cuál de los dispositivos internos reenviarlas. El **port forwarding** resuelve eso: asocia un puerto público del router a la IP local de un dispositivo. Es lo que piden algunos juegos para que un jugador pueda "hostear" una partida y actuar como servidor.

> [!warning] Servidor web no es lo mismo que aplicación web
> El servidor web es la máquina (o el programa, como Apache o NGINX) que atiende requests. La aplicación web es el software que corre ahí y genera las respuestas. Un mismo servidor puede alojar varias aplicaciones.

## Preguntas de repaso

> [!question]- ¿Por qué Wikipedia es un sitio y no una página?
> Porque es una colección de muchísimos documentos, cada uno con su propia URL, enlazados entre sí bajo el mismo dominio. Cada artículo individual es una página.

> [!question]- ¿Qué diferencia a una aplicación web de un sitio web informativo?
> El usuario interactúa con la aplicación: envía datos, y el servidor los procesa y responde con contenido que depende de esa interacción (por ejemplo, su bandeja de correo). Un sitio informativo entrega principalmente los mismos documentos a todos.

> [!question]- ¿Para qué sirve el port forwarding?
> Para que un dispositivo de la red local sea accesible desde Internet: el router reenvía lo que llega a uno de sus puertos públicos hacia la IP y el puerto de ese dispositivo interno.
