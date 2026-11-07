---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - indice
---

# Índice — Infraestructura y despliegue en la nube

La infraestructura del proyecto: **cloud computing** y AWS (EC2, VPC, regiones), servidores Linux por SSH, **Docker y Docker Compose**, redes TCP/IP, **DNS**, **nginx** como reverse proxy, el despliegue básico en una EC2, el frontend en **S3 + CloudFront** y la **infraestructura como código** con Terraform.

## Contenido

1. [[01 - Cloud computing AWS y servidores Linux]] — IaaS, PaaS y SaaS, EC2 y tipos de instancia, VPC, regiones, Lambda y Beanstalk, capas de Linux y conexión por SSH.
2. [[02 - Docker contenedores e imágenes]] — Qué resuelve Docker, namespaces y cgroups, VM frente a contenedor, Dockerfile, capas, buenas prácticas, pros y contras.
3. [[03 - Orquestación con Docker Compose]] — Por qué orquestar, docker-compose.yml con mapeo de puertos y red interna por nombre de servicio, y comandos esenciales.
4. [[04 - Redes DNS NGINX y despliegue básico]] — TCP/IP y enrutamiento, resolución DNS y registros, IP elástica, nginx, forward frente a reverse proxy y el despliegue en una EC2.
5. [[05 - Almacenamiento estático S3 CloudFront e infraestructura como código]] — Datos estáticos, S3 y bucket policy, flujos de CloudFront con caché e invalidación, HTTPS con ACM, y IaaC imperativo frente a declarativo con Terraform.
