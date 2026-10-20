---
ramo: "Sistemas Distribuidos"
tema: "Exclusión mutua distribuida"
tags:
  - sd/exclusion-mutua
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmo Token Ring]]"
  - "[[01 - Relojes lógicos de Lamport]]"
---

# Multicast de Ricart y Agrawala

Ni el servidor central ni el Token Ring respetan el orden en que se pidió el recurso. **Ricart y Agrawala** lo logran sin coordinador: quien quiere entrar le pregunta a **todos** los demás, y cada nodo decide a quién dejar pasar primero comparando **relojes lógicos**. El orden de acceso es el mismo orden total que definen los relojes.

## Algoritmo

1. Un nodo $N_i$ que quiere entrar a la sección crítica **incrementa su reloj lógico** y envía $\langle Reloj_i, N_i \rangle$ a los otros $N - 1$ nodos (*multicast*).
2. Cuando un nodo $N_x$ recibe la solicitud $\langle Reloj_i, N_i \rangle$:
   - a. si **no** está en la sección crítica y **no** quiere entrar, da permiso;
   - b. si **está** en la sección crítica, encola la solicitud;
   - c. si quiere entrar y su propia solicitud tiene un reloj **menor** (pidió antes), encola la solicitud;
   - d. si quiere entrar y su propia solicitud tiene un reloj **mayor** (pidió después), da permiso.
3. $N_i$ entra cuando recibió permiso de **todos** los $N - 1$ nodos.
4. Al salir, responde todas las solicitudes que tenía en cola.

Los empates de reloj se resuelven por el identificador del nodo, como en el par (contador, id) de [[06 - Algoritmo de la panadería y deadlock|la panadería]].

## Ejemplo

![Ricart y Agrawala en cuatro pasos](adjuntos/Ricart%20y%20Agrawala%20en%20cuatro%20pasos.png)

> [!example]- Transcripción de la imagen
> 1. S pide acceso al recurso crítico (RC) en tiempo 4 y T pide en tiempo 8; ambos envían su solicitud a los otros dos nodos.
> 2. K, que no quiere el recurso, responde "Ok" a S y a T. S piensa "Mi solicitud fue antes, dejar en cola la solicitud del nodo T"; T le responde "Ok" a S.
> 3. S tiene todos los permisos: "Accedo al R. Crítico".
> 4. S termina: "Listo, ahora respondo a T" y le envía "Ok". T accede al recurso crítico.

Una simulación en Python reprodujo el ejemplo: S entra primero, luego T, y se usaron 8 mensajes, $2(N-1) = 4$ por cada acceso.

## Características

- Quien necesita el recurso envía su solicitud por **multicast** y solo entra cuando **todos** respondieron.
- Usa **relojes lógicos** para establecer un **orden total** de las solicitudes.
- Si un nodo se cae, se deja de esperar su respuesta; cuando revive, primero debe **sincronizar su reloj lógico**.
- Garantiza **safety**, **liveness** y **ordering** según el reloj lógico. Si se usaran relojes físicos, tendrían que estar bien sincronizados para asegurar el orden.

## Desventajas

- **Muchos mensajes:** $2(N-1)$ por cada entrada ($N - 1$ solicitudes y $N - 1$ permisos), ineficiente en sistemas grandes o con uso frecuente.
- **Todos** los nodos participan en cada decisión de acceso: un nodo lento retrasa a todos.

## Comparación

| | Servidor central | Token Ring | Ricart y Agrawala |
|---|---|---|---|
| Safety | Sí | Sí | Sí |
| Liveness | Sí (si el servidor no cae) | Sí (si nadie cae) | Sí |
| Ordering | No | No | Sí, por reloj lógico |
| Mensajes por acceso | 3 | Hasta $N - 1$ de espera | $2(N-1)$ |
| Punto débil | El servidor | El token y el anillo | Todos los nodos participan |

> [!example] Pregunta de aplicación
> Una red de sensores de humo tiene mensajes que **siempre tardan lo mismo**, nodos de respaldo que hacen que la red **nunca vea una caída** y relojes de cuarzo que se sincronizan con NTP solo **cada dos años**. Se necesita safety, ordering y liveness para activar la alarma.
> - **Servidor central** sirve: sin fallas se cumplen safety y liveness, y como todos los mensajes tardan lo mismo, el orden de llegada coincide con el de envío, así que también hay ordering.
> - **Token Ring** no sirve, porque su orden es el del anillo.
> - **Ricart y Agrawala** no se puede asegurar, porque los sensores solo usan relojes físicos y están muy desincronizados.

## Preguntas de repaso

> [!question]- ¿Qué hace un nodo que también quiere entrar cuando recibe una solicitud con un reloj mayor que el suyo?
> La encola: su propia solicitud es anterior, así que debe entrar primero. Responderá a esa solicitud cuando salga de la sección crítica.

> [!question]- ¿Por qué Ricart y Agrawala sí garantiza ordering y el servidor central no?
> Porque ordena por el reloj lógico de la solicitud, que refleja el orden en que se pidió, y no por el orden en que llegaron los mensajes a un servidor.

> [!question]- ¿Cuántos mensajes requiere un acceso con 10 nodos?
> $2(10 - 1) = 18$: 9 solicitudes y 9 permisos.
