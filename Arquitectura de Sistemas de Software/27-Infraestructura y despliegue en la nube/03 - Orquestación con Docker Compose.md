---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - arquisis/docker
  - origen/complemento
prerrequisitos:
  - "[[02 - Docker contenedores e imágenes]]"
---

# Orquestación con Docker Compose

Una aplicación real tiene varios servicios: API, web, base de datos, workers. **Docker Compose** los define de forma declarativa en un archivo YAML y crea automáticamente la red, la resolución de nombres y el orden de arranque entre ellos.

## Por qué orquestar

Varios contenedores pequeños que trabajan juntos escalan mejor que uno gigante que lo hace todo y colapsa al crecer. En el curso se usa **Compose** para definir y levantar los servicios de forma declarativa.

```yaml
services:
  api:
    build: ./api              # carpeta con el Dockerfile de la API
    ports:
      - "5001:5000"           # puerto del PC : puerto del contenedor
  web:
    build: ./web
    ports:
      - "8080:8080"
    environment:
      - API_URL=http://api:5000   # se usa el nombre del servicio, no localhost
```

- **Mapeo de puertos `5001:5000`:** a la izquierda el puerto del computador y a la derecha el del contenedor.
- **Red interna:** Compose crea una red donde cada servicio se resuelve por su nombre (`http://api:5000`).
- Comandos: `docker compose up --build`, `docker compose ps` y `docker compose down` (detiene y borra contenedores y redes, pero no los volúmenes).

![Croquis de dos contenedores conectados por Docker Compose](adjuntos/Croquis%20de%20contenedores%20conectados%20con%20Docker%20Compose.png)

> [!example]- Transcripción de la imagen
> - Un recuadro **Docker** con un *container-node* (**API**, puerto 3000) conectado a una **DB**, y otro contenedor con un **listener** (puerto 3001).
> - A la izquierda, la conexión externa entra por el puerto `8000:3000` (*Expose*).
> - A la derecha, "Bridge: para conectar contenedores", y que `http://localhost:3000` se transforma en `http://api:3000` dentro de la red de Compose.
> - Abajo, "1 Dockerfile" por servicio.

![Comandos esenciales de Docker Compose](adjuntos/Comandos%20de%20Docker%20Compose.png)

> [!example]- Transcripción de la imagen
> - `docker compose down`: detiene y elimina contenedores, redes y recursos creados por Compose.
> - `docker compose build`: construye o recompila las imágenes de todos los servicios.
> - `docker compose up`: crea, conecta y levanta todos los servicios.
> - `docker compose ps`: estado de los contenedores del Compose.
> - `docker system prune`: limpia contenedores detenidos, redes e imágenes huérfanas.
> - `docker ps`: lista los contenedores activos.
> - `docker exec -it <ID> bash` (o `sh`): abre una terminal dentro del contenedor.

## Preguntas de repaso

> [!question]- En el compose, ¿por qué la web usa `http://api:5000` y no `http://localhost:5000`?
> Porque cada contenedor tiene su propia red: `localhost` sería el mismo contenedor web. Compose crea una red interna donde cada servicio se resuelve por su nombre, y la API escucha en el puerto 5000 dentro de su contenedor.

> [!question]- ¿Qué significa el mapeo `"5001:5000"`?
> Que el puerto 5001 del computador anfitrión redirige al puerto 5000 dentro del contenedor.

> [!question]- ¿Por qué varios contenedores pequeños orquestados escalan mejor que uno que lo hace todo?
> Porque cada servicio se puede escalar, reiniciar y actualizar por separado: si la API necesita más réplicas, no hay que replicar también la web. Un contenedor que lo hace todo crece hasta colapsar y es una sola unidad de falla.

> [!question]- ¿Qué borra `docker compose down` y qué conserva?
> Detiene y elimina los contenedores y las redes creadas por Compose, pero conserva los volúmenes declarados (por ejemplo, los datos de la base), salvo que se pida explícitamente borrarlos.

> [!question]- En un compose con `backend` y `postgres-db`, ¿para qué sirven `depends_on` y un volumen en la base?
> `depends_on` hace que Compose levante la base antes que el backend. El volumen guarda los datos de Postgres fuera del ciclo de vida del contenedor, así que no se pierden al recrearlo.
