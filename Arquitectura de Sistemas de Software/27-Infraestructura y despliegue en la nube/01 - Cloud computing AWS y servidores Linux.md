---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - origen/complemento
prerrequisitos:
  - "[[03 - Distribución serverless frontend y nube]]"
---

# Cloud computing AWS y servidores Linux

La mayoría de las veces el código corre localmente. Para el proyecto del curso, en cambio, todo se despliega en la nube. Esta nota reúne lo necesario para entender y defender ese despliegue: qué es el cloud computing, qué ofrece AWS (EC2, VPC, regiones) y cómo se trabaja en un servidor Linux por SSH.

## Cloud computing

Es **pagarle a una empresa para usar sus servidores**: RAM, disco y red. Al final, todo es arriendo de servidores.

**Ventajas:**
- servidores con mucha **disponibilidad** y más **seguridad**;
- **escalabilidad**: no se invierte en servidores sin saber si alcanzarán, y la capacidad se adapta a las necesidades;
- permite implementar la infraestructura que se quiera: almacenamiento, procesamiento de datos, virtualización.

| Modelo | Qué se arrienda | Ejemplos |
|---|---|---|
| **SaaS** (Software as a Service) | La aplicación completa | Zoom, Dropbox |
| **PaaS** (Platform as a Service) | Un entorno para hospedar la aplicación | Elastic Beanstalk, Heroku |
| **IaaS** (Infrastructure as a Service) | La infraestructura: máquinas, redes, bases de datos | EC2, RDS |

**Proveedores:** AWS, Google Cloud y Azure. Siempre hay que fijarse en la **flexibilidad**: diseñar pensando en la escalabilidad y analizar **cuándo conviene pasarse** a la nube.

## AWS

- Tiene una **capa gratuita** (créditos iniciales) y millones de servidores.
- Un **hipervisor** segmenta cada máquina física en **máquinas virtuales**, cada una con su CPU, RAM y sistema operativo, y se configura cuántos recursos usa cada una.
- **EC2** (*Elastic Compute Cloud*) son las máquinas virtuales. Se eligen por **tipo de instancia**, que difieren en precio por hora:
  - **t3** (`t3.nano`, `t3.micro`): de propósito general y baratas; son las del curso.
  - **c6i**: más CPU y RAM, y más caras.
- **VPC** (*Virtual Private Cloud*): la red propia dentro de AWS. Arrienda espacios de direcciones IP privadas para que nadie más acceda.
- **Regiones**: AWS funciona en todo el mundo, en regiones con varias zonas de disponibilidad.
- **Alerta de presupuesto** (*budget alert*): conviene configurarla al empezar, para que un error o un ataque no genere una factura inesperada.

**Otros paradigmas además de cliente-servidor:**
- **AWS Lambda** (serverless): se paga por ejecución y RAM.
- **Elastic Beanstalk** (PaaS): se sube la aplicación y AWS gestiona las instancias, el balanceo y el escalado.

## Linux en el servidor

En el mundo de los servidores domina **Linux**: es escalable, seguro, eficiente y está muy documentado. En el curso se usa **Ubuntu Server**.

**Arquitectura de Linux en 3 capas:** hardware → **kernel** (programas que abstraen el hardware) → **capa de usuario**.

**Herramientas:**
- **bash**: el shell de comandos (`cd`, `mkdir`, `sudo`, `sudo apt update`, `sudo apt install …`);
- **cron**: programar rutinas;
- **ssh**: conexión segura;
- **curl**: hacer peticiones HTTP;
- **sudo**: ejecutar con privilegios.

Para la navegación entre servicios se usan contenedores con **Docker**. A nivel empresarial, con muchos servidores, se usa **Kubernetes**.

### Conectarse a la instancia

La forma estándar es **SSH**. En Linux y macOS es nativo; en Windows se usa un cliente.

```bash
chmod 400 "ayudantia01-key.pem"     # la llave privada debe ser solo lectura para el dueño
ssh -i "ayudantia01-key.pem" ubuntu@ec2-18-222-221-224.us-east-2.compute.amazonaws.com
sudo apt update                       # actualizar el índice de paquetes
```

Hay que **guardar la llave** (`.pem`) para volver a acceder: si se pierde, no hay forma de conectarse a esa instancia.

> [!warning] No exponer la API directamente
> En el servidor, la API no se publica sola a internet. Delante va un **servidor web** (nginx) como reverse proxy, que controla el acceso, rutea el tráfico y puede distribuir carga. Ver [[04 - Redes DNS NGINX y despliegue básico]].

## Preguntas de repaso

> [!question]- Diferencie IaaS, PaaS y SaaS con un ejemplo de cada uno.
> IaaS arrienda infraestructura (máquinas, redes), como EC2. PaaS arrienda un entorno donde se despliega la aplicación sin gestionar servidores, como Elastic Beanstalk. SaaS entrega la aplicación lista para usar, como Zoom o Dropbox.

> [!question]- ¿Qué ventajas de cloud computing se relacionan con atributos de calidad?
> Disponibilidad (infraestructura redundante del proveedor), escalabilidad y elasticidad (crecer o decrecer según la necesidad sin invertir en hardware propio) y seguridad (controles del proveedor).

> [!question]- ¿Qué es una VPC y para qué sirve?
> Es una red privada virtual dentro de AWS: un espacio de direcciones IP propio donde viven las instancias, aislado de otros clientes. Permite controlar qué es público y qué es privado.

> [!question]- ¿Qué hace el hipervisor en un proveedor como AWS?
> Divide cada máquina física en varias máquinas virtuales, cada una con su CPU, RAM y sistema operativo asignados, para arrendarlas por separado.

> [!question]- ¿Por qué se ejecuta `chmod 400` sobre la llave antes de usar SSH?
> Porque SSH rechaza llaves privadas con permisos abiertos. `400` deja la llave como solo lectura para su dueño, y así nadie más en la máquina puede leerla.

> [!question]- ¿Cuándo convendría Lambda en vez de una EC2?
> Para cargas esporádicas o eventuales (un script puntual, una función que se ejecuta pocas veces), porque se paga solo por ejecución. Para un servicio con carga constante, o que necesita baja latencia desde la primera petición, suele convenir una EC2 o un contenedor.

> [!question]- V o F: "Cloud computing elimina la necesidad de diseñar pensando en la escalabilidad".
> Falso. La nube da recursos elásticos, pero la arquitectura debe aprovecharlos (servicios sin estado, balanceo, datos que escalen). Además, hay que evaluar el costo y el lock-in antes de migrar.
