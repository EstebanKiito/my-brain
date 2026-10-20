---
ramo: "Sistemas Distribuidos"
tema: "Tolerancia a fallos"
tags:
  - sd/tolerancia-a-fallos
  - sd/invocacion-remota
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - RPC y stubs]]"
  - "[[02 - Fallo, error y fracaso]]"
---

# Semánticas de RPC ante fallos

Una llamada RPC parece local, pero cruza la red. Si el cliente no recibe respuesta, no sabe si la petición se perdió, si el servidor cayó antes de ejecutarla o si la ejecutó y lo que se perdió fue la respuesta. Reintentar puede ejecutar la operación dos veces; no reintentar puede no ejecutarla nunca. Las **semánticas de llamada** estandarizan qué promete un RPC frente a esas situaciones.

## Qué puede fallar

| Fallo | Consecuencia para el cliente |
|---|---|
| No se puede **localizar** el RPC (falla de la red o del propio RPC) | La llamada no se puede hacer |
| Se pierde el mensaje de **solicitud** | No hay respuesta; la operación no se ejecutó |
| El RPC **falla después de recibir** la solicitud | No hay respuesta, y no se sabe si la operación se ejecutó antes de la falla |
| Se pierde el mensaje de **respuesta** | Igual que el anterior: no se sabe si se ejecutó |
| El **cliente falla** después de enviar la solicitud | La operación queda como un **cálculo huérfano** (*orphan computation*) que consume recursos, y puede repetirse si el cliente reinicia y reintenta |

Los tres últimos son los difíciles: desde el cliente, "no se ejecutó" y "se ejecutó pero no supe" se ven igual.

## Las cuatro semánticas

![Semánticas de llamada RPC](adjuntos/Sem%C3%A1nticas%20de%20llamada%20RPC.png)

> [!example]- Transcripción de la imagen
> **Semántica de llamada (*delivery guarantees*):**
> - **Maybe:** el RPC puede ejecutarse una vez o no ejecutarse. Ocurre cuando no se aplican medidas de tolerancia a fallos; útil solo cuando los fallos ocasionales son aceptables.
> - **At-least-once:** el RPC se ejecuta al menos una vez, posiblemente más. El cliente retransmite la solicitud hasta recibir respuesta. Para evitar resultados incorrectos por duplicación, las operaciones deben ser idempotentes.
> - **At-most-once:** el RPC se ejecuta como máximo una vez, o ninguna. Implica filtrar duplicados en el RPC y retransmitir resultados almacenados.
> - **Exactly-once:** el RPC se ejecuta sí o sí una vez: una mezcla de retransmisiones del cliente y un RPC con semántica at-most-once.

| Semántica | ¿El cliente reintenta? | ¿El servidor filtra duplicados? | Ejecuciones |
|---|---|---|---|
| Maybe | No | No | 0 o 1 |
| At-least-once | Sí | No | 1 o más |
| At-most-once | Sí | Sí | 0 o 1 |
| Exactly-once | Sí, hasta tener respuesta | Sí | Exactamente 1 |

> [!tip] Idempotencia
> Una operación es **idempotente** si ejecutarla varias veces deja el mismo resultado que ejecutarla una vez: "fijar el saldo en 100" lo es, "sumar 100 al saldo" no. Con operaciones idempotentes, at-least-once es seguro y simple.

## Ejemplo en Python

Un depósito no idempotente: la primera llamada se ejecuta, pero su respuesta se pierde, y el cliente reintenta con el mismo identificador de solicitud.

```python
class Servidor:
    def __init__(self, filtrar):
        self.saldo, self.vistos, self.filtrar = 0, {}, filtrar

    def depositar(self, id_solicitud, monto):
        if self.filtrar and id_solicitud in self.vistos:
            return self.vistos[id_solicitud]   # devuelve el resultado guardado
        self.saldo += monto
        self.vistos[id_solicitud] = self.saldo
        return self.saldo
```

| Variante | Saldo final tras el reintento |
|---|---|
| Sin filtro (at-least-once) | 200: el depósito se aplicó dos veces |
| Con filtro de duplicados (at-most-once + reintentos = exactly-once) | 100: el reintento recibe el resultado guardado |

> [!warning] Exactly-once tiene un precio
> El servidor debe recordar qué solicitudes ya ejecutó y sus resultados, y esa memoria tiene que sobrevivir a sus propias caídas. Por eso muchos sistemas prefieren at-least-once con operaciones idempotentes.

## Preguntas de repaso

> [!question]- ¿Por qué at-least-once exige operaciones idempotentes?
> Porque el cliente reintenta hasta recibir respuesta y la operación puede ejecutarse varias veces. Si no es idempotente (como sumar a un saldo), cada repetición altera el resultado.

> [!question]- ¿Qué necesita el servidor para ofrecer at-most-once?
> Identificar cada solicitud (por ejemplo, con un id único), recordar las ya ejecutadas y, ante un duplicado, devolver el resultado almacenado sin volver a ejecutar.

> [!question]- ¿Qué es un cálculo huérfano y cuándo aparece?
> Es una operación que el servidor sigue ejecutando para un cliente que ya falló. Consume recursos y, si el cliente reinicia y reintenta, puede duplicar la operación.
