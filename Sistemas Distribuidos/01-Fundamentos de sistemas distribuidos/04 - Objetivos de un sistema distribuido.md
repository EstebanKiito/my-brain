---
ramo: "Sistemas Distribuidos"
tema: "Fundamentos de sistemas distribuidos"
tags:
  - sd/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[02 - Sistemas centralizados, descentralizados y distribuidos]]"
  - "[[03 - Desafíos de los sistemas distribuidos]]"
---

# Objetivos de un sistema distribuido

Repartir un sistema solo vale la pena si el resultado es mejor que un computador único. El libro guía resume qué significa "mejor" en seis objetivos; sirven como lista de chequeo para evaluar cualquier sistema distribuido.

| Objetivo | Qué busca | Ejemplos |
|---|---|---|
| **Compartir recursos** (*resource sharing*) | Acceder a recursos remotos sin preocuparse de su ubicación, sistema operativo o formato | Torrent, OneDrive |
| **Transparencia de distribución** (*distribution transparency*) | Ocultar que procesos y recursos están repartidos físicamente | La URL de un sitio, Google Drive |
| **Apertura** (*openness*) | Ofrecer componentes que se puedan usar o integrar fácilmente en otros sistemas | Protocolos de comunicación, aplicación web con microservicios |
| **Confiabilidad** (*dependability*) | Que las operaciones funcionen según lo esperado incluso ante fallos parciales | El buzón de tareas de Canvas, Google |
| **Seguridad** (*security*) | Que hardware, software y datos estén protegidos y no se alteren sin autorización | Permisos de edición en Google Drive, roles de estudiante y profesor en Canvas |
| **Escalabilidad** (*scalability*) | Seguir siendo efectivo (rendimiento, costo, facilidad de gestión) a medida que crece | Zoom (geográfica), retail en Cyber Day (tamaño) |

## Transparencia de distribución

La transparencia no es "honestidad": es **ocultar** que el sistema está distribuido, para que nadie detecte que hay $N$ nodos. Al entrar a Facebook el usuario no sabe a qué nodo se conectó. Hay varios tipos:

- **De acceso:** los recursos locales y remotos se acceden de la misma manera.
- **De ubicación:** se accede a un recurso sin conocer su ubicación física o en la red.
- **De migración:** se pueden mover recursos o clientes dentro del sistema sin interrumpir la operación.
- **De replicación:** se oculta que existen varias copias de un recurso (las copias protegen ante pérdidas).
- **De concurrencia:** varios nodos comparten un recurso al mismo tiempo sin conflictos.
- **De fallos:** las tareas se completan aunque fallen componentes, porque el sistema reconfigura o redirige las operaciones automáticamente.

> [!tip] Transparencia = ocultar
> Cada tipo de transparencia oculta una pregunta que el usuario no debería tener que hacerse: ¿es local?, ¿dónde está?, ¿se movió?, ¿cuántas copias hay?, ¿quién más lo usa?, ¿falló algo?

## Apertura

Un sistema abierto define **reglas generales** (interfaces y protocolos) que todos sus componentes cumplen. Así los componentes se pueden reemplazar o integrar con otros sistemas, y se evita el [acoplamiento](https://es.wikipedia.org/wiki/Acoplamiento_(inform%C3%A1tica)) excesivo entre ellos. Un protocolo como HTTP es el ejemplo típico: cualquier cliente que lo hable puede usar cualquier servidor.

## Confiabilidad y seguridad

**Confiabilidad** es poder confiar en que el sistema tendrá los archivos subidos y en que, si un nodo se cae, habrá otro al cual conectarse. **Seguridad** abarca autorizaciones, contraseñas y permisos que impiden que alguien altere los activos sin autorización. Ambas se profundizan en las unidades de tolerancia a fallos y de seguridad.

## Escalabilidad

Lo ideal es que agregar nodos mantenga o mejore el rendimiento. Se distinguen tres dimensiones:

- **De tamaño:** se agregan usuarios y recursos sin una baja perceptible del rendimiento.
- **Geográfica:** usuarios y recursos pueden estar muy separados sin que los retrasos de comunicación se noten demasiado.
- **Funcional:** se agregan funcionalidades sin romper lo existente ni perder rendimiento.

La relación entre escalar y mantener la consistencia de los datos se discute en [[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]].

> [!warning] Los objetivos chocan entre sí
> Más réplicas mejoran la confiabilidad y la escalabilidad, pero hacen más difícil la transparencia de concurrencia (todas las copias deben coincidir). Diseñar un sistema distribuido es elegir qué objetivo priorizar.

## Preguntas de repaso

> [!question]- ¿Qué tipo de transparencia se rompe si el usuario debe elegir manualmente "servidor Chile" o "servidor EE. UU."?
> La de ubicación: el usuario tiene que conocer dónde está el recurso para acceder a él. Un sistema transparente lo redirigiría al nodo adecuado sin preguntarle.

> [!question]- ¿Por qué la apertura reduce el acoplamiento?
> Porque los componentes dependen de reglas públicas (interfaces y protocolos) y no de los detalles internos de los demás. Mientras se respete la regla, un componente puede cambiarse por otro sin afectar al resto.

> [!question]- Un retail funciona bien todo el año pero colapsa en Cyber Day. ¿Qué dimensión de escalabilidad le falta?
> La de tamaño: no soporta el aumento de usuarios simultáneos sin una caída perceptible del rendimiento.
