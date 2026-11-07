---
ramo: "Arquitectura de Sistemas de Software"
tema: "Infraestructura y despliegue en la nube"
tags:
  - arquisis/infraestructura
  - origen/complemento
prerrequisitos:
  - "[[04 - Redes DNS NGINX y despliegue básico]]"
  - "[[02 - Caché web navegador proxy CDN y proxy inverso]]"
---

# Almacenamiento estático S3 CloudFront e infraestructura como código

El frontend del proyecto no corre en la EC2: se compila a archivos estáticos que se sirven desde **S3** a través de la CDN **CloudFront**. Y cuando hay que repetir toda la infraestructura (desarrollo, testing, producción), hacerlo a mano no escala: para eso está la **infraestructura como código**.

## Datos estáticos

Son datos que, una vez creados, **no cambian**: si cambian, se crea una versión nueva. Son **distribuibles** y se pueden expresar como **archivos** (HTML, JS, CSS, imágenes).

**¿Por qué no hospedarlos uno mismo?**
- **Escalabilidad:** hace falta mucha inversión para escalar.
- **Performance:** un servidor propio no tiene alcance mundial.
- **Confiabilidad:** es difícil asegurar que los datos no se pierdan.
- **Elasticidad:** cuesta responder a un peak de demanda.

| Modelo | Descripción |
|---|---|
| **On premises** | Servidor propio: alto riesgo |
| **Compartido, baja demanda** | Servicios como Drive u Outlook |
| **Compartido, alta demanda** | Aprovisionamiento con buena performance (S3) |

## Amazon S3

Servicio de **almacenamiento de objetos** escalable y seguro, con una **durabilidad altísima**: es muy improbable perder datos. Ofrece control de acceso, respaldos y optimización de costos.

![Flujo de almacenamiento en Amazon S3](adjuntos/Flujo%20de%20almacenamiento%20en%20Amazon%20S3.png)

> [!example]- Transcripción de la imagen
> - **Move data:** se mueven a S3 datos de distintas fuentes (analítica, logs, aplicaciones, video, respaldos).
> - **Amazon S3 / Store data:** se crean buckets y se suben objetos; S3 ofrece control de acceso, optimización de costo por clases de almacenamiento, replicación entre regiones, acceso desde on-premises o VPC, protección de datos y visibilidad del uso.
> - **Analyze data:** se usan servicios de AWS y de terceros (IA, analítica avanzada, machine learning) para obtener información.

**Subir el frontend:**
1. `npm run build` genera la carpeta compilada (`dist`).
2. Crear un **bucket** con nombre único y **desbloquear el acceso público** para que sea legible.
3. En *Properties*, habilitar **static website hosting** con `index.html` como documento índice y de error.
4. Agregar una **bucket policy** que permita `s3:GetObject` a todos sobre `BUCKET_ARN/*`.
5. Subir con la **AWS CLI**, usando las credenciales de **IAM** (*access key ID* y *secret access key*). **Solo se pueden ver una vez**: hay que guardarlas.

## CloudFront (CDN)

Una **CDN** entrega **baja latencia**, **protección** y **edge computing** (ejecutar pequeños códigos cerca de los usuarios). AWS ofrece **CloudFront**, con ubicaciones por todo el mundo, incluida una cerca de Chile.

**Flujo 1, caché válida:** el cliente consulta al DNS → el DNS lo dirige a CloudFront, **no a S3** → CloudFront tiene una copia no expirada y la entrega.

**Flujo 2, caché expirada:** igual, pero CloudFront ve que la copia expiró → pide la versión nueva a S3 → la guarda y la entrega.

**Flujo 3, actualizar el frontend:** subir los archivos nuevos a S3 → **invalidar la caché** de CloudFront → la próxima petición trae y guarda la versión nueva.

**HTTPS:** el certificado se instala en **CloudFront**, no en S3. Se gestiona con **ACM** (*AWS Certificate Manager*), y para usarlo con CloudFront **debe solicitarse en la región us-east-1**.

> [!warning] Subir a S3 no basta para ver los cambios
> Si no se invalida la caché de CloudFront, los usuarios siguen recibiendo la versión vieja hasta que expire. Es el desafío de consistencia de toda caché.

## Infraestructura como código (IaaC)

¿Qué pasa si se quiere replicar toda la infraestructura para tener instancias de **testing**, **desarrollo** y **producción**?

| Enfoque | Cómo | Problema |
|---|---|---|
| **Manual** | Repetir todos los pasos en la consola de AWS | Lento, propenso a errores, irrepetible |
| **Automatización imperativa** | Scripts con la CLI de AWS que dicen **paso a paso cómo** llegar | Hay que mantener la secuencia de pasos |
| **Automatización declarativa (IaaC)** | Se define el **estado final** y la herramienta resuelve el "cómo" | Curva de aprendizaje |

**¿Por qué usar IaaC?**
- **Consistencia y replicabilidad** de los entornos.
- Se **evita la configuración manual**.
- Permite **entornos de prueba** similares a producción y **altamente escalables**.
- Resuelve problemas de despliegue: **se edita la fuente, no el destino**.

Las herramientas se diferencian por **qué resuelven** (aprovisionamiento, configuración, despliegue), **qué etapa cubren** (setup inicial, mantenimiento) y **cómo funcionan** (imperativo o declarativo, infraestructura mutable o inmutable).

**Terraform** (declarativo): se describe la infraestructura en archivos y se opera con `init` (inicializa los proveedores), `validate` (revisa la sintaxis), `plan` (muestra qué cambiará), `apply` (lo aplica) y `destroy` (lo elimina).

```hcl
resource "aws_instance" "api" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t3.micro"
  tags = { Name = "api-produccion" }
}
```

## Preguntas de repaso

> [!question]- ¿Por qué conviene servir el frontend desde S3 + CloudFront y no desde la EC2?
> Porque son archivos estáticos: S3 los guarda con alta durabilidad y escala sin gestión, y CloudFront los acerca a los usuarios con caché, lo que baja la latencia y la carga de la EC2. La EC2 queda dedicada a la API.

> [!question]- Describa qué pasa cuando la copia en CloudFront expiró.
> El cliente llega a CloudFront por DNS. CloudFront detecta que su copia expiró, pide la versión nueva a S3, la guarda en caché y la entrega al cliente.

> [!question]- ¿Qué hay que hacer después de subir una versión nueva del frontend a S3?
> Invalidar la caché de CloudFront. Si no, los usuarios seguirán recibiendo la copia anterior hasta que expire.

> [!question]- ¿Dónde se instala el certificado HTTPS y en qué región se solicita?
> En CloudFront, no en S3. Se gestiona con ACM y debe pedirse en us-east-1 para poder asociarlo a CloudFront.

> [!question]- Diferencie la automatización imperativa de la declarativa.
> La imperativa define paso a paso cómo llegar al resultado (scripts con la CLI). La declarativa define el estado final deseado y la herramienta calcula los pasos (Terraform).

> [!question]- ¿Qué hace `terraform plan` y por qué es útil antes de `apply`?
> Muestra qué recursos se crearán, modificarán o eliminarán para llegar al estado declarado, sin aplicar nada. Permite revisar los cambios antes de afectar la infraestructura real.

> [!question]- V o F: "Con IaaC, si se quiere cambiar la infraestructura, se modifica directamente el servidor en la consola de AWS".
> Falso. Con IaaC se edita la fuente (el código de infraestructura) y se vuelve a aplicar. Modificar el destino a mano hace que el código y la realidad diverjan.
