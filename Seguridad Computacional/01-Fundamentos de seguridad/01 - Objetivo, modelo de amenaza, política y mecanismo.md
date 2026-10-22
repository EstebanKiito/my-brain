---
ramo: "Seguridad Computacional"
tema: "Fundamentos de seguridad"
tags:
  - seguridad/fundamentos
  - origen/complemento
prerrequisitos: []
---

# Objetivo, modelo de amenaza, política y mecanismo

Construir un sistema seguro es difícil porque la seguridad es un objetivo **negativo**: implementar que el ayudante pueda leer el archivo de notas es fácil, pero garantizar que *nadie más* pueda, por ningún camino, exige pensar en todos los ataques posibles (un error en el servidor, una contraseña adivinada, un laptop robado, tráfico interceptado, un insider). Por eso el ramo pide **pensamiento sistémico**: los detalles importan. Para ordenar ese pensamiento se usan cuatro piezas.

## Las cuatro piezas

| Pieza | Qué es | Ejemplo |
|---|---|---|
| **Objetivo** | La propiedad de seguridad que se quiere lograr | "Solo Alice puede leer el archivo F" |
| **Modelo de amenaza** | Suposiciones sobre lo que el atacante puede y no puede hacer | "Puede adivinar contraseñas, pero no robar el servidor" |
| **Política** | Reglas que, dentro del modelo, cumplen el objetivo | Permisos sobre F; contraseña más 2FA |
| **Mecanismo** | Software o hardware que hace cumplir la política | Cuentas, permisos de archivo, cifrado |

> [!tip] Idea clave
> Seguridad = objetivo + modelo de amenaza + política + mecanismo. El objetivo dice *qué* se protege, el modelo dice *de quién y hasta dónde*, y política y mecanismo son el *cómo*. Si el modelo de amenaza es incorrecto, la seguridad se rompe aunque el resto esté bien hecho.

## Tríada CIA

Los objetivos se agrupan en tres categorías:
- **Confidencialidad:** el adversario no puede aprender información secreta.
- **Integridad:** el adversario no puede corromper el estado del sistema.
- **Disponibilidad:** el sistema sigue funcionando pese al adversario (por ejemplo, ante un DDoS).

## Capas

La política puede incluir componentes humanos (no compartir contraseñas) que los mecanismos no pueden forzar. Además, las piezas se apilan: el mecanismo de una capa suele ser la política de la capa inferior (los permisos de archivo del sistema operativo se apoyan a su vez en el aislamiento del kernel).

## Preguntas de repaso

> [!question]- ¿Por qué se dice que la seguridad es un "objetivo negativo"?
> Porque no basta con que lo permitido funcione: hay que asegurar que *ninguna* ruta, incluso una no prevista, permita lo prohibido. Un solo hueco entre muchos posibles basta para romperla.

> [!question]- ¿Qué diferencia hay entre política y mecanismo?
> La política son las reglas (quién puede qué); el mecanismo es la implementación concreta que las hace cumplir (permisos, cifrado, contraseñas).

> [!question]- ¿Qué pasa si el modelo de amenaza es incorrecto?
> Política y mecanismo pueden estar perfectos y aun así fallar, porque defienden contra un atacante que no es el real (por ejemplo, asumir que ningún usuario cae en phishing).
