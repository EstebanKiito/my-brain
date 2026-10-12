---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[06 - Microservicios|Microservicios]]"]
---
# Contenedores con Docker y Kubernetes

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes": "¿Cómo implementar una arquitectura con micro-servicios?")
> **Qué es:** los **contenedores** empaquetan una aplicación con sus dependencias para que corra igual en cualquier máquina. **Docker** los crea y ejecuta; **Kubernetes** los orquesta en un clúster.
>
> ## Máquinas virtuales vs. contenedores
> ![Slide - máquinas virtuales vs contenedores](adjuntos/Slide%20-%20máquinas%20virtuales%20vs%20contenedores.png)
>
> - **VM:** infraestructura → SO anfitrión → **hypervisor** → cada app con **su propio SO invitado** (pesado).
> - **Contenedores:** infraestructura → SO → **Docker Engine** → cada app con solo sus bins/libs. **Comparten el kernel**: son más livianos y arrancan más rápido.
>
> ## Docker
> ![Slide - Dockerfile, imagen y contenedor](adjuntos/Slide%20-%20Dockerfile,%20imagen%20y%20contenedor.png)
>
> **Dockerfile** → `build` → **imagen** → `run` → **contenedor**. Ejemplo de Dockerfile (slides):
> ```dockerfile
> # Especificamos la imagen de la que se heredará
> FROM python:3.6-alpine
> # Definimos algunas variables de ambiente
> ENV LIBRARY_PATH=/lib:/usr/lib
> ENV PYTHONUNBUFFERED 1
> # Ejecutamos algunos comandos para aprovisionar la imagen
> RUN mkdir /code
> WORKDIR /code
> ADD requirements.txt /code/
> RUN pip install -r requirements.txt
> # Copiamos el código
> ADD . /code/
> # Exponemos el puerto por donde se interactuará con la aplicación
> EXPOSE 8000
> # Definimos el comando de entrada a la aplicación
> CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
> ```
>
> ![Slide - comandos de Docker](adjuntos/Slide%20-%20comandos%20de%20Docker.png)
>
> **Ciclo de comandos:**
> - `build` (Dockerfile → imagen) y `tag` (nombrar la imagen);
> - `push`/`pull` (subir/bajar imágenes a un **Docker registry**);
> - `save`/`load` (respaldar en `backup.tar`);
> - `run` (imagen → contenedor) y `stop`/`start`/`restart`;
> - `commit` (contenedor → imagen).
>
> El cliente (`docker build`, `docker pull`, `docker run`) habla con el *Docker daemon* del host.
>
> ## Kubernetes
> ![Slide - arquitectura de Kubernetes](adjuntos/Slide%20-%20arquitectura%20de%20Kubernetes.png)
>
> *"Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications."*
>
> Kubernetes **agrupa, organiza, programa, vigila y lanza** los contenedores Docker en **nodos**, según lo que se necesite. Tiene un *control plane* (API server, scheduler, controller manager, etcd) y *worker nodes* con *pods* de contenedores.
>
> ## Evolución del despliegue
> ![Slide - evolución del despliegue](adjuntos/Slide%20-%20evolución%20del%20despliegue.png)
>
> **Tradicional** (apps directo sobre el SO) → **virtualizado** (VMs) → **contenedores** → **Kubernetes** (Kubernetes y Docker trabajan juntos para construir y correr aplicaciones en contenedores).

## Preguntas de repaso

1. ¿Por qué un contenedor es más liviano que una máquina virtual?
> [!question]- Respuesta
> Porque comparte el kernel del sistema operativo anfitrión y solo empaqueta la app y sus librerías. Cada VM, en cambio, incluye un sistema operativo invitado completo sobre un hypervisor.

2. ¿Qué relación hay entre Dockerfile, imagen y contenedor?
> [!question]- Respuesta
> El Dockerfile es la receta; con `docker build` se genera una imagen (plantilla inmutable), y con `docker run` se crea un contenedor (una instancia en ejecución de esa imagen).

3. ¿Qué hace Kubernetes que Docker solo no hace?
> [!question]- Respuesta
> Orquesta muchos contenedores en un clúster de nodos: decide dónde correrlos, los escala, los reinicia si fallan y gestiona sus despliegues.
