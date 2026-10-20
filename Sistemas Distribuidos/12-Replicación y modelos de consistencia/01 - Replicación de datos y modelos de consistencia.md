---
ramo: "Sistemas Distribuidos"
tema: "Replicación y modelos de consistencia"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Confiabilidad y sus propiedades]]"
---

# Replicación de datos y modelos de consistencia

Tener varias copias de los datos en distintos nodos es la forma más directa de tolerar fallas y atender a más usuarios. Pero cada vez que una copia se actualiza, deja de ser igual a las demás. La pregunta deja de ser "¿hay copias?" y pasa a ser "¿qué puede ver un cliente que lee una copia?". La respuesta la da el **modelo de consistencia** que el sistema promete.

## Por qué replicar

| Propiedad | Cómo ayuda la replicación |
|---|---|
| **Alta disponibilidad** | Si un nodo falla, otra copia sigue atendiendo; también aporta tolerancia a fallos |
| **Rendimiento y escalabilidad** | Copias cerca de los clientes reducen la **latencia** de las lecturas, y las solicitudes se **balancean** entre servidores, sin un cuello de botella único |
| **Operación desconectada** | Un cliente (por ejemplo, un celular) sigue trabajando con su copia local sin red y sincroniza al reconectarse |

Si hay $n$ réplicas y cada una falla con probabilidad $p$, la disponibilidad es $1 - \Pr(\text{todas fallan}) = 1 - p^n$. Con $p = 0{,}05$ y $n = 2$, es 99,75 %.

## El problema

Al actualizar una réplica, esta se diferencia de las otras. Sin un reloj global preciso, es difícil saber cuál fue la **última** escritura, y distintos clientes pueden leer valores distintos según la copia que consulten.

## Modelos de consistencia

> [!tip] Definición
> Un **modelo de consistencia** es un **contrato** entre los procesos (o nodos) y la base de datos: si los procesos aceptan obedecer ciertas reglas, la base de datos promete funcionar de forma consistente.

- Los modelos se expresan en términos de **escrituras** ($W$) y **lecturas** ($R$). En los diagramas, $W_A(x)=1$ es una escritura del nodo A que deja $x$ en 1, y $R_F(x)\rightarrow 0$ es una lectura de F que obtuvo 0.
- La replicación de un nodo A hacia un nodo B solo se **confirma** cuando B hace un read del dato y ve el valor.

Del más estricto al más relajado:

| Modelo | Qué garantiza |
|---|---|
| [[03 - Consistencia fuerte o linealizable\|Fuerte (linealizable)]] | Cada operación tiene efecto instantáneo en algún momento entre su inicio y su fin: respeta el tiempo real |
| [[02 - Consistencia secuencial\|Secuencial]] | Todos ven las operaciones en un mismo orden, que respeta el orden de cada proceso |
| [[04 - Consistencia causal\|Causal]] | Todos ven en el mismo orden solo las operaciones relacionadas causalmente |
| [[05 - Consistencia eventual\|Eventual]] | Si dejan de llegar escrituras, todas las réplicas terminan iguales |

> [!warning] Más consistencia, menos disponibilidad
> Cuanto más estricto el modelo, más coordinación exige entre réplicas, y más lento o menos disponible se vuelve el sistema. Esta tensión se formaliza con los teoremas CAP y PACELC.

## Preguntas de repaso

> [!question]- ¿Por qué la replicación crea un problema de consistencia que un solo servidor no tiene?
> Porque con varias copias, una escritura llega a cada réplica en momentos distintos. Mientras se propaga, distintas réplicas tienen valores distintos, y un cliente puede leer uno viejo.

> [!question]- ¿Qué gana un usuario de una app móvil con la operación desconectada?
> Puede seguir leyendo y modificando su copia local sin conexión; los cambios se sincronizan con el resto de las réplicas al reconectarse.

> [!question]- ¿Qué significa que un modelo de consistencia sea un "contrato"?
> Que la base de datos no promete consistencia absoluta, sino una garantía concreta a cambio de que los procesos sigan ciertas reglas. El programador debe saber qué contrato ofrece el sistema para razonar sobre lo que leerá.
