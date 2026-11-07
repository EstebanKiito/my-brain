---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - arquisis/docker
  - origen/complemento
prerrequisitos:
  - "[[01 - Cloud computing AWS y servidores Linux]]"
  - "[[03 - Máquinas virtuales y cliente-servidor]]"
  - "[[07 - Contenedores con Docker y Kubernetes]]"
---

# Docker contenedores e imágenes

"En mi computador funciona" es el problema que resuelven los contenedores. **Docker empaqueta el software para ejecutarlo en su propio entorno** aislado, con exactamente las dependencias que necesita. En el proyecto, todos los sistemas se levantan contenerizados y se coordinan con Docker Compose, que se ve en [[03 - Orquestación con Docker Compose]].

## Qué problemas resuelve

- **Portabilidad:** que el código funcione en todos los entornos.
- **Versionamiento** del entorno, no solo del código.
- **Aplicaciones con muchas dependencias** que chocan entre sí.

![Aplicaciones instaladas en el host frente a aplicaciones en contenedores](adjuntos/Aplicaciones%20en%20el%20host%20frente%20a%20contenedores.png)

> [!example]- Transcripción de la imagen
> - **The old way: applications on host.** Cuatro *App* comparten un mismo bloque de *Libraries* sobre el *Kernel*. Pie: pesado, no portable, depende del gestor de paquetes del sistema.
> - **The new way: deploy containers.** Cada *App* tiene sus propias *Libraries* y todas comparten el *Kernel*. Pie: pequeño, rápido, portable, usa virtualización a nivel del sistema operativo.

Antes, todas las aplicaciones y librerías se instalaban en el mismo sistema operativo y chocaban al compartir código. Con contenedores se logra:
- **consistencia** entre entornos;
- **portabilidad** entre nubes;
- **aislamiento** de recursos (asignación y seguridad);
- **CI/CD** más simple y **despliegues ágiles**;
- **observabilidad**: se mide la performance de cada contenedor.

## Cómo funciona por dentro

La contenedorización es **virtualización a nivel del sistema operativo**: los contenedores comparten el kernel del host, en vez de virtualizar hardware como una VM. Docker orquesta tecnologías nativas de Linux:
- **Namespaces:** aislamiento de procesos (PID), red (NET), archivos (MNT) y comunicación (IPC). Cada contenedor solo ve lo suyo.
- **Control groups (cgroups):** limitan cuánta CPU, memoria y disco usa cada contenedor.
- **Union file systems:** capas de solo lectura apiladas que se ven como un único sistema de archivos.

| | Máquina virtual | Contenedor |
|---|---|---|
| Arquitectura | Hipervisor; cada VM con su sistema operativo invitado | Motor sobre el host; comparten el kernel |
| Aislamiento | Fuerte (hardware) | Lógico (namespaces, cgroups) |
| Tamaño | Gigabytes | Megabytes |
| Arranque | Minutos | Milisegundos |

**Arquitectura de Docker** (es cliente-servidor): el **daemon** (`dockerd`) atiende la API y administra los objetos, el **cliente** (`docker`) le envía comandos, y los **registries** (Docker Hub, AWS ECR) almacenan y distribuyen imágenes.

## Dockerfile, imagen y contenedor

- **Dockerfile:** las instrucciones de instalación y configuración. Con él se crea la imagen.
- **Imagen:** el "instalador": un paquete **inmutable** con el código y sus dependencias.
- **Contenedor:** la **instancia en ejecución** de una imagen, con una capa temporal de escritura encima.
- **Volúmenes:** persisten datos fuera del ciclo de vida del contenedor.
- **Redes:** `bridge` (red interna, por defecto), `host` (usa la red de la máquina) y `overlay` (varias máquinas).

![Instrucciones principales de un Dockerfile](adjuntos/Instrucciones%20de%20un%20Dockerfile.png)

> [!example]- Transcripción de la imagen
> - `FROM <image>:<tag>`: la imagen base desde la cual se construye.
> - `RUN <command>`: ejecuta comandos en el contenedor durante la construcción.
> - `WORKDIR <path>`: se ubica en el directorio de trabajo dentro del contenedor.
> - `COPY <path_interno> <path_container>`: copia archivos o carpetas al contenedor.
> - `EXPOSE <port>`: expone un puerto de la red interna de Docker.
> - `CMD <command>`: el comando que se ejecuta al iniciar el contenedor.

```dockerfile
FROM python:3.12-slim                                  # imagen base oficial (Docker Hub)
WORKDIR /app                                           # carpeta de trabajo
COPY requirements.txt .                                # primero las dependencias…
RUN pip install --no-cache-dir -r requirements.txt     # …para aprovechar la caché de capas
COPY app.py .                                          # el código, que cambia seguido, al final
EXPOSE 5000                                            # puerto donde escucha la app
CMD ["python", "app.py"]                               # comando al encender el contenedor
```

**Capas:** cada instrucción es una capa apilada sobre la anterior. Si solo cambia el código, Docker reconstruye desde esa capa y reutiliza las anteriores, así que **el orden importa**: lo estable arriba y lo que cambia abajo.

**Buenas prácticas:**
- **Multi-stage builds:** compilar en una imagen pesada y copiar solo el binario a una imagen liviana.
- Agrupar comandos con `&&` y limpiar la caché del gestor de paquetes en la misma capa.
- Usar `.dockerignore` (excluir `.git`, `.env`, `node_modules`).
- Preferir `COPY` a `ADD`.
- Terminar con un **usuario no-root** (mínimo privilegio).

**Comandos útiles:** `build`, `run`, `ps`, `stop` (detención controlada), `kill` (inmediata), `rm`, `prune`, `exec -it … sh` (abrir una terminal dentro), `cp`, `logs`, `stats` (consumo de CPU, RAM y red).

![Croquis del flujo Dockerfile, imagen y contenedor](adjuntos/Croquis%20de%20Dockerfile%20imagen%20y%20contenedor.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, un recuadro **Docker** con un *contenedor* que tiene un *listener* y otro *contenedor* con la *API* conectada a una base de datos.
> - Al centro, el flujo **Dockerfile → Imagen → Container**, con la nota "1 Dockerfile, 1 imagen por contenedor".
> - A la derecha, las instrucciones `CMD [node, api.js]`, `CMD [node, listener.js]`, `FROM node`, `COPY`, `RUN npm install`, y la nota "capas: OS + node".

| Pros | Contras |
|---|---|
| Paridad estricta de entornos | **Superficie de seguridad**: un exploit del kernel compartido puede comprometer el host |
| **Inmutabilidad**: no se parchea, se reemplaza la imagen | **Estado**: los contenedores son efímeros, y las bases de datos requieren volúmenes bien diseñados |
| Integración natural con CI/CD | **Clústeres**: Docker gestiona un nodo; a gran escala hace falta un orquestador (Kubernetes) |

## Preguntas de repaso

> [!question]- Diferencie Dockerfile, imagen y contenedor.
> El Dockerfile son las instrucciones para construir. La imagen es el paquete inmutable resultante, con el código y sus dependencias. El contenedor es una instancia en ejecución de esa imagen.

> [!question]- ¿Por qué en un Dockerfile se copian las dependencias antes que el código?
> Porque cada instrucción es una capa cacheada. Si el código cambia pero las dependencias no, Docker reutiliza la capa de `pip install` y solo reconstruye desde `COPY app.py`, lo que acelera el build.

> [!question]- ¿Qué tecnologías de Linux usa Docker para aislar contenedores?
> Namespaces (aislamiento de procesos, red y archivos), cgroups (límites de CPU, memoria y disco) y union file systems (capas apiladas de solo lectura).

> [!question]- Nombre dos riesgos de usar contenedores.
> La seguridad, porque comparten el kernel y un exploit puede escapar al host, y el manejo del estado, porque los contenedores son efímeros y las bases de datos requieren volúmenes y diseño cuidadoso. A gran escala, además, hace falta un orquestador.

> [!question]- V o F: "Un contenedor incluye su propio sistema operativo completo, igual que una máquina virtual".
> Falso. El contenedor comparte el kernel del host y solo empaqueta la aplicación con sus librerías. Por eso pesa megabytes y arranca en milisegundos.
