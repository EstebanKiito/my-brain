---
ramo: "Sistemas Distribuidos"
tema: "Replicación y modelos de consistencia"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[04 - Consistencia causal]]"
---

# Consistencia eventual

En el extremo opuesto a la consistencia fuerte está la **consistencia eventual** (Vogels, 2009): no se promete casi nada sobre lo que se lee **ahora**, solo que, si dejan de llegar escrituras, todas las réplicas **terminarán iguales**. A cambio, el sistema es muy disponible y rápido. Es el modelo de muchas bases NoSQL y de las redes sociales.

## Definición

- **Prioriza** la alta disponibilidad y el rendimiento por sobre la consistencia.
- Si dos o más nodos no escriben exactamente al mismo tiempo (no hay **conflicto de escritura**), las réplicas **convergen** a copias idénticas.
- Se garantiza que las actualizaciones **se propagan eventualmente** a todas las réplicas.
- Mientras tanto, dos clientes pueden ver réplicas distintas, y un cliente puede ver **datos obsoletos**.
- Si hay un conflicto de escritura, se necesita una estrategia; por ejemplo, que una escritura sobrescriba a la otra.

Ver la versión desde las bases de datos en [[02 - Consistencia eventual y BASE|Consistencia eventual y BASE]].

## Causal no implica eventual

En la ejecución de [[04 - Consistencia causal|consistencia causal]] (H lee 2, 5, 9 y S lee 2, 9, 5), H terminó con $x=9$ y S con $x=5$: nunca convergen. Es causal, pero **no** eventual.

## Eventual pero no causal

![Ejecución eventual pero no causal](adjuntos/Ejecuci%C3%B3n%20eventual%20pero%20no%20causal.png)

> [!example]- Transcripción de la imagen
> A escribe $W_A(x)=2$, lee $R_A(x)\rightarrow 9$ y escribe $W_A(x)=5$. F lee 2, escribe 9 y lee 5. H lee 2, 9, 5. S lee 9, 2, 5. "Nodos H y S ven los write en distinto orden → no es consistente secuencial. Nodo S ve primero que x es 9 y luego que es 2 → no es consistente causal. Ojo que este caso sigue siendo factible: si la comunicación de A → S es más lenta, puede pasar que $W_A(x)=2$ llegue después de que F propagó su cambio. Todos llegan finalmente a ver x=5 → consistente eventual."

## Pregunta de aplicación

![Pregunta de modelos de consistencia](adjuntos/Pregunta%20de%20modelos%20de%20consistencia.png)

> [!example]- Transcripción de la imagen
> A escribe $W_A(x)=2$ y luego $W_A(x)=4$; F escribe $W_F(x)=7$. H lee 4 y luego 7. S lee 7, 2 y 4. Para cada modelo: fuerte ❌, secuencial ❌, causal ✅, eventual ❌.

- **No secuencial ni fuerte:** H ve 4 antes que 7 y S ve 7 antes que 4. El verificador de fuerza bruta no encontró ninguna secuencia válida.
- **Causal:** las únicas relaciones causales son $2 \rightarrow 4$ (mismo proceso), y ambos las respetan. El 7 es concurrente.
- **No eventual:** H termina con 7 y S con 4; no convergen.

| Modelo | Garantía | Costo |
|---|---|---|
| Fuerte | Siempre el último valor según el tiempo real | Muy alto |
| Secuencial | Un mismo orden para todos | Alto |
| Causal | Mismo orden de lo relacionado causalmente | Medio |
| Eventual | Convergencia sin nuevas escrituras | Bajo |

> [!warning] Los modelos no forman una escalera completa
> Fuerte implica secuencial, y secuencial implica causal. Pero la eventual mide otra cosa (la convergencia final): una ejecución puede ser causal y no eventual, o eventual y no causal.

## Preguntas de repaso

> [!question]- ¿Qué promete y qué no promete la consistencia eventual?
> Promete que, sin nuevas escrituras, todas las réplicas convergen al mismo valor. No promete que una lectura devuelva el último valor ni que todos vean las escrituras en el mismo orden.

> [!question]- ¿Por qué un sistema elegiría consistencia eventual?
> Porque cada réplica puede responder de inmediato con lo que tiene, sin coordinarse con las demás. Gana disponibilidad y rendimiento, a costa de mostrar datos obsoletos por un tiempo.

> [!question]- ¿Puede una ejecución ser causal y no eventual?
> Sí: si dos réplicas reciben dos escrituras concurrentes en órdenes distintos y se quedan con valores finales diferentes, se respetó la causalidad, pero no hay convergencia.
