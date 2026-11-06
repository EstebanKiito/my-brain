---
ramo: "Arquitectura de Sistemas de Software"
tema: "Caché y protocolos web"
tags:
  - arquisis/performance
  - arquisis/cache
  - origen/complemento
prerrequisitos:
  - "[[03 - Tácticas de performance de Bass y Kazman]]"
---

# Caché conceptos desafíos y buenas prácticas

La caché es la táctica de performance más citada en las pautas, y también la más fácil de proponer mal. Es la táctica "múltiples copias de datos": guardar una respuesta cerca de quien la pide para no volver a calcularla ni a viajar por ella. Funciona muy bien cuando los datos se repiten y cambian poco, y es un error cuando cada petición necesita información fresca y distinta.

## Qué es

> [!tip] Caché
> **Replicación de datos en diversas instancias para elevar la performance.** Es un almacén de objetos o de pares llave-valor que guarda respuestas para servirlas sin repetir el trabajo.

Se decide cachear según tres requerimientos:
- **Proximidad:** acercar el dato al usuario (CDN, caché del navegador).
- **Latencia:** evitar una operación lenta (una consulta pesada, una API externa).
- **Tamaño:** cuánto cabe y cuánto conviene guardar. Muchas veces la caché vive en RAM, que es cara.

## La jerarquía de la CPU: el mismo principio

![Pirámide de la jerarquía de memoria con tamaños y latencias](adjuntos/Jerarquía%20de%20memoria%20y%20cachés%20de%20CPU.png)

> [!example]- Transcripción de la imagen
> | Nivel | Tamaño típico | Latencia |
> |---|---|---|
> | Registros | ~1 KB | 0,3 ns |
> | Caché L1 | 256 KB | 1,1 ns |
> | Caché L2 | 1 MB | 3,3 ns |
> | Caché L3 | 8 MB | 12,8 ns |
> | Caché L4 | 128 MB | 42,4 ns |
> | Memoria principal | 32 GB (US\$5-10/GB) | 62,9 ns |
> | SSD | 200 GB-1 TB (US\$0,67/GB) | ~0,1 ms |
> | Disco | 2-5 TB (US\$50/TB) | ~3 ms |
> Hacia arriba es más rápido; hacia abajo, más grande y más barato.

La CPU usa una arquitectura de capas de caché donde cada nivel es más lento y más grande que el anterior. Existen porque la RAM es mucho más lenta que el procesador. Las cachés de un sistema web siguen la misma lógica: una capa pequeña y rápida (Redis en RAM, la CDN) delante de una grande y lenta (la base de datos, el servidor de origen).

## Desafíos

| Desafío | Qué pasa | Cómo se maneja |
|---|---|---|
| **Sincronización y consistencia** | La caché puede servir datos viejos (*stale*) | Estrategias de **invalidación**: TTL, invalidar al escribir, versionar llaves |
| **Coherencia** | Varios nodos o servicios tienen copias distintas del mismo dato | Caché compartida (un Redis central), invalidación por eventos, aceptar consistencia eventual |
| **Warm-up** | Al partir, la caché está vacía y todo va al origen | **Prefetch**: precargar las llaves más usadas |
| **Tamaño** | La RAM es limitada | Políticas de **desalojo** (*eviction*) |
| **Complejidad** | Implementar caché no es gratis | Medir antes; cachear solo lo que lo justifica |

### Políticas de desalojo

- **LRU** (*Least Recently Used*): saca lo usado hace más tiempo. Es la más común.
- **LFU** (*Least Frequently Used*): saca lo usado menos veces. Es buena cuando hay datos populares estables.
- **FIFO**: saca lo más antiguo. Es simple, pero ignora el uso.

## Buenas prácticas generales

- **Entender qué datos necesitan caché**: archivos estáticos y consultas repetidas.
- Fijar **expiraciones** y **desalojo** con valores apropiados.
- Usar **caché jerárquico**: varias capas que aprovechan fortalezas distintas (navegador → CDN → caché de aplicación → base de datos).
- **Monitorear** la tasa de aciertos (*hit rate*), el tamaño y las expulsiones.
- **Escoger el stack correcto**, con ojo con el software propietario: Redis, Memcached, Varnish.
- **Prefetch** para mejorar el arranque y las respuestas predictivas.

## Cuándo sí y cuándo no

> [!example]- Caso: datos viejos por caché en servicios replicados
> **Problema:** cada réplica tiene su propia caché local. Un usuario actualiza su dirección en la réplica A, pero su siguiente petición cae en la réplica B, que le muestra la dirección antigua.
> **Solución:** reemplazar las cachés locales por una **caché compartida** (Redis) e **invalidar la llave al escribir** (*write-through* o borrar la llave). Si se mantienen cachés locales, invalidarlas con un evento `DireccionActualizada` publicado por pub/sub.
> **Comprobación:** el usuario actualiza en A, se invalida la llave en la caché compartida y B lee el dato nuevo, porque la caché ya no tiene la versión vieja.

> [!warning] Cuándo NO usar caché
> - **Cada petición necesita información fresca y distinta.** Por ejemplo, un servidor que pide a cada dispositivo datos para validar un intercambio: cachear haría que se validara con información vieja. Mejor otra medida, como un broker que reciba los mensajes.
> - **Datos que cambian constantemente:** la caché se invalida tanto que solo agrega trabajo y hace el sistema más lento.
> - **Encolar tareas para workers** es un trabajo para una cola, no para una caché.

## Preguntas de repaso

> [!question]- ¿Cuáles de estos son buenos usos de caché? I. Workers donde hay que encolar tareas · II. Una app que repite las mismas peticiones y recibe casi siempre lo mismo · III. Archivos estáticos lejanos que se quieren cerca de los clientes
> II y III. II es el caso clásico de consultas repetidas. III es una CDN. I es un caso para una cola de mensajes, no para una caché.

> [!question]- Alternativas sobre la caché: a) Almacena datos infinitos · b) Es un protocolo de los navegadores · c) Se puede implementar en el frontend, en un middleware o en el backend · d) Mejora la confiabilidad
> c). La caché existe en todas las capas: navegador, CDN, proxy y aplicación. a) es falsa porque el espacio es limitado (por eso existe el desalojo). b) es falsa porque no es solo del navegador. d) es falsa porque su objetivo es la performance y puede servir datos viejos.

> [!question]- V o F: "El caché solo sirve para mejorar la performance".
> Falso en sentido estricto. Su objetivo principal es la performance, pero al reducir la carga del origen también ayuda a la escalabilidad, y puede mejorar la disponibilidad sirviendo respuestas aunque el origen esté caído (por ejemplo, contenido stale en modo offline).

> [!question]- ¿Qué es el warm-up de una caché y cómo se mitiga?
> Es el período inicial en que la caché está vacía y todas las peticiones van al origen, que puede saturarse justo al arrancar o después de reiniciar. Se mitiga con prefetch: precargar las llaves más usadas antes de recibir tráfico.

> [!question]- Diferencie LRU y LFU y dé un caso donde LFU sea mejor.
> LRU expulsa lo usado hace más tiempo y LFU lo usado menos veces. LFU es mejor cuando hay un conjunto estable de datos muy populares (la portada de un diario) que no se quieren perder por un barrido puntual de datos poco usados que LRU dejaría entrar.

> [!question]- Mini caso: varias réplicas con caché local muestran datos viejos después de actualizar. Proponga una solución y explique por qué funciona.
> Usar una caché compartida e invalidar la llave en cada escritura, o publicar un evento de invalidación que todas las réplicas escuchan. Así ninguna réplica sirve una versión anterior a la última escritura, y la ventana de inconsistencia queda acotada.

> [!question]- ¿Por qué la jerarquía de cachés de la CPU es un buen modelo para pensar la caché web?
> Porque aplica el mismo principio: capas pequeñas y rápidas delante de capas grandes y lentas, con la expectativa de que la mayoría de los accesos se resuelvan arriba. En la web serían navegador, CDN, caché de aplicación y base de datos.
