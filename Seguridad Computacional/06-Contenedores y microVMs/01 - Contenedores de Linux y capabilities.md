---
ramo: "Seguridad Computacional"
tema: "Contenedores y microVMs"
tags:
  - seguridad/aislamiento
  - linux
  - origen/complemento
prerrequisitos:
  - "[[01 - Separación de privilegios y OKWS]]"
---

# Contenedores de Linux y capabilities

Aislar procesos solo con UIDs, permisos y `chroot` (como en OKWS) es difícil de manejar, porque Linux comparte mucho estado del kernel (PIDs, archivos, IPs, puertos). Los **contenedores** son "`chroot` en esteroides": un grupo de procesos con vistas privadas y recursos limitados, que corre en milisegundos y ocupa megabytes. Sirven para empaquetar software con sus dependencias, y para aislarlo en seguridad y rendimiento.

## Máquinas virtuales frente a contenedores
Una VM es *una CPU con muchos kernels*; un contenedor es *un kernel con muchos espacios de usuario*.

![Máquina virtual frente a contenedor LXC](adjuntos/M%C3%A1quina%20virtual%20frente%20a%20contenedor%20LXC.png)

> [!example]- Transcripción de la imagen
> Tabla VM / contenedor LXC. Sistema operativo: la VM ejecuta un SO invitado aislado; el contenedor usa el mismo SO del anfitrión (kernel compartido). Red: dispositivos de red virtuales / vista aislada de un adaptador virtual mediante namespaces. Aislamiento: completo respecto de otros invitados y del anfitrión / basado en namespaces y cgroups. Tamaño: del orden de gigabytes / de megabytes. Arranque: segundos a minutos / segundos.

## Los cuatro mecanismos

| Mecanismo | Qué hace |
|---|---|
| **Namespaces** | Un recurso solo ve a los del mismo namespace. Tipos: PID (procesos), UTS (hostname), IPC, User, Mount (puntos de montaje), Network y cgroup |
| **cgroups** | Limitan, contabilizan, priorizan y controlan los recursos de un grupo de procesos (CPU, memoria, disco, red, dispositivos). No son un límite de seguridad, pero frenan ataques de denegación de servicio |
| **Capabilities** | Dividen los poderes de root en permisos sueltos (`CAP_CHOWN`, `CAP_NET_ADMIN`, `CAP_NET_RAW`) para dar solo el necesario |
| **seccomp-bpf** | Filtro (un programa BPF) que decide qué *syscalls* puede hacer un proceso; los hijos lo heredan |

> [!tip] Resultado
> Un contenedor es un proceso Linux con privilegios limitados: namespaces aíslan elementos del kernel, capabilities reducen privilegios, cgroups limitan hardware y seccomp-bpf filtra las llamadas al kernel. Si un atacante toma el contenedor y es root dentro, aún no puede usar syscalls peligrosas.

### Ejemplo de capability: `ping`
`ping` necesita abrir sockets *raw*, antes reservado a root. Hoy `getcap /bin/ping` muestra que el binario lleva la capability `CAP_NET_RAW` (con las banderas `+ep`) y un usuario normal puede usarlo. Una copia sin la capability falla (`Operation not permitted`) hasta ejecutar `sudo setcap CAP_NET_RAW=ep ./ping`. Banderas: *effective* (activa), *inheritable* (heredada por los hijos) y *permitted* (permitida sin importar la del padre).

## Cuándo usarlos
Mejor segregación de privilegios en microservicios dentro de un solo host, contención del "radio de explosión" tras un compromiso y uso más eficiente de recursos que con virtualización. Su límite: comparten el kernel, así que un bug del kernel permite escapar.

## Preguntas de repaso

> [!question]- ¿Por qué un contenedor es menos aislado que una VM?
> Porque comparte el kernel con el anfitrión; un error del kernel (con 300+ syscalls expuestas) puede permitir escapar, mientras que una VM solo expone hardware virtual.

> [!question]- ¿Para qué sirven las capabilities en vez de simplemente ser root?
> Para dar a un proceso solo el poder concreto que necesita (por ejemplo, `CAP_NET_RAW` a `ping`), siguiendo el privilegio mínimo.

> [!question]- Si los cgroups no son un límite de seguridad, ¿por qué se usan?
> Evitan que un proceso monopolice CPU o memoria y afecte a los demás (denegación de servicio), lo que también es parte de la disponibilidad.
