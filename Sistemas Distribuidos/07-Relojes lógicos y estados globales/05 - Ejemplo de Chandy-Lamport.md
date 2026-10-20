---
ramo: "Sistemas Distribuidos"
tema: "Relojes lógicos y estados globales"
tags:
  - sd/estados-globales
  - origen/complemento
prerrequisitos:
  - "[[04 - Algoritmo de Chandy-Lamport]]"
---

# Ejemplo de Chandy-Lamport

El algoritmo de Chandy-Lamport se entiende de verdad al seguirlo paso a paso. Este ejemplo, con tres nodos (K, Y y S), muestra cuándo cada nodo guarda su estado, qué canales quedan vacíos y cómo se capturan los dos mensajes que estaban en tránsito. Notación: $C_{YK}$ es el canal **de Y hacia K**, grabado por K.

## Escenario

- **Nodo K:** eventos A, B, C, D y E. D es la recepción de un mensaje enviado desde H; E envía un mensaje que S recibe en K.
- **Nodo Y:** eventos F (recibe un mensaje de B), G (recibe un mensaje de I) y H (envía mensajes a K y a S).
- **Nodo S:** eventos I (envía a Y), J (recibe el mensaje de H) y K (recibe el mensaje de E).

## Paso a paso

**1. K inicia** después de B: guarda su estado (B), envía marcadores a Y y a S y empieza a grabar $C_{YK}$ y $C_{SK}$.

**2. S recibe el marcador de K** (es su primero), justo después de I: guarda su estado (I), $C_{KS} = [\,]$, envía marcadores a K y a Y y empieza a grabar $C_{YS}$.

![Chandy-Lamport tras el primer marcador](adjuntos/Chandy-Lamport%20tras%20el%20primer%20marcador.png)

> [!example]- Transcripción de la imagen
> K tiene A y B en verde (estado guardado) y S tiene I en verde. Marcadores rojos punteados salen de K hacia Y y S; marcadores azules salen de S hacia K y Y. Una línea verde marca el momento en que S recibe el marcador. Recuadros: $C_{YK}$ = …grabando…, $C_{SK}$ = …grabando…; $C_{KS} = [\,]$, $C_{YS}$ = …grabando…

**3. K recibe el marcador de S:** no llegó nada por ese canal mientras grababa, así que $C_{SK} = [\,]$ y deja de grabarlo.

**4. Y recibe el marcador de S** (su primero), después de H: guarda su estado (H), $C_{SY} = [\,]$, envía marcadores a K y a S y empieza a grabar $C_{KY}$. El marcador de K hacia Y sigue en camino.

![Chandy-Lamport con los tres estados guardados](adjuntos/Chandy-Lamport%20con%20los%20tres%20estados%20guardados.png)

> [!example]- Transcripción de la imagen
> Ahora Y tiene F, G y H en verde. Salen marcadores morados de Y hacia K y S. Recuadros: $C_{YK}$ = …grabando…, $C_{SK} = [\,]$; $C_{KY}$ = …grabando…, $C_{SY} = [\,]$; $C_{KS} = [\,]$, $C_{YS}$ = …grabando…

**5. K recibe el marcador de Y.** Antes, por ese canal, había llegado el mensaje de H (recibido en D), enviado **antes** de que Y guardara su estado y recibido **después** de que K guardara el suyo: es un mensaje en tránsito. $C_{YK} = [H \to D]$.

![Canal de Y a K con un mensaje grabado](adjuntos/Canal%20de%20Y%20a%20K%20con%20un%20mensaje%20grabado.png)

> [!example]- Transcripción de la imagen
> La línea verde está entre D y E en K, justo cuando llega el marcador morado de Y. Recuadro: $C_{YK} = [H \to D]$, $C_{SK} = [\,]$. Los demás canales siguen igual: $C_{KY}$ grabando, $C_{SY} = [\,]$, $C_{KS} = [\,]$, $C_{YS}$ grabando.

**6. Y recibe el marcador de K** (el rojo, que venía desde el paso 1). No llegó nada por ese canal mientras grababa: $C_{KY} = [\,]$.

![Canal de K a Y vacío](adjuntos/Canal%20de%20K%20a%20Y%20vac%C3%ADo.png)

> [!example]- Transcripción de la imagen
> El marcador rojo de K llega a Y. Recuadros: $C_{YK} = [H \to D]$, $C_{SK} = [\,]$; $C_{KY} = [\,]$ (destacado), $C_{SY} = [\,]$; $C_{KS} = [\,]$, $C_{YS}$ = …grabando…

**7. S recibe el marcador de Y.** Mientras grababa ese canal llegó el mensaje de H (recibido en J): $C_{YS} = [H \to J]$.

![Canal de Y a S con un mensaje grabado](adjuntos/Canal%20de%20Y%20a%20S%20con%20un%20mensaje%20grabado.png)

> [!example]- Transcripción de la imagen
> Recuadro final de S: $C_{KS} = [\,]$ y $C_{YS} = [H \to J]$ (destacado).

## Resultado

![Estado global final de Chandy-Lamport](adjuntos/Estado%20global%20final%20de%20Chandy-Lamport.png)

> [!example]- Transcripción de la imagen
> Una zona naranja ("Pasado") contiene A y B de K, F, G y H de Y, e I de S; el resto queda en el "Futuro". Recuadro: **Estado final:** Nodo K = Estado B, Nodo Y = Estado H, Nodo S = Estado I. **Mensajes pendientes:** mensaje desde el estado H al nodo K, y mensaje desde el estado H al nodo S.

| Componente | Valor guardado |
|---|---|
| Estado de K | B |
| Estado de Y | H |
| Estado de S | I |
| $C_{YK}$ | $[H \to D]$ |
| $C_{YS}$ | $[H \to J]$ |
| $C_{SK}$, $C_{KS}$, $C_{KY}$, $C_{SY}$ | $[\,]$ |

> [!tip] Cómo leer el resultado
> El corte es consistente: los mensajes recibidos en el pasado (B → F e I → G) tienen su envío también en el pasado. Los dos mensajes enviados en H y recibidos en el futuro (en D y en J) quedan guardados como **mensajes en tránsito**. Al restaurar esta foto, habría que volver a entregarlos.

> [!warning] Solo se graban los mensajes que llegan
> Un nodo graba los mensajes que **recibe** por un canal entre que guardó su estado y que llega el marcador de ese canal. Si en ese intervalo no llega nada, el canal queda vacío, aunque haya habido tráfico antes o después.

## Preguntas de repaso

> [!question]- ¿Por qué $C_{KS}$ queda vacío sin grabar nada?
> Porque es el canal por el que S recibió su **primer** marcador. Por FIFO, todo lo que K envió antes de su marcador ya había llegado a S.

> [!question]- ¿Por qué el mensaje H → D queda en $C_{YK}$ y no en el estado de K?
> Porque K lo recibió (en D) después de guardar su estado (B), pero Y lo envió antes de guardar el suyo (H). No pertenece a ningún estado local: estaba en el canal cuando se tomó la foto.

> [!question]- ¿Qué pasaría si Y hubiera recibido primero el marcador de K en vez del de S?
> Guardaría su estado en ese momento, el canal $C_{KY}$ quedaría vacío y empezaría a grabar $C_{SY}$. La foto sería otra, pero igualmente consistente: el algoritmo garantiza consistencia, no un instante específico.
