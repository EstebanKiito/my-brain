---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Escala e ingeniería inversa"
tags:
  - web
  - seguridad
  - ingenieria-inversa
  - origen/complemento
prerrequisitos:
  - "[[04 - Documentar y consumir APIs]]"
  - "[[03 - Abusos de las cookies]]"
---

# Ingeniería inversa y tipos de hackers

Las aplicaciones web exponen mucho más de lo que parece: todo el JavaScript del frontend llega al navegador, y cada request a la API se ve en DevTools. Estudiar un sistema desde afuera para entender cómo funciona es **ingeniería inversa**. Sirve para aprender, para integrarse con sistemas sin documentación y para encontrar vulnerabilidades, tanto para arreglarlas como para explotarlas.

## Qué es la ingeniería inversa

La **ingeniería inversa** es el proceso de obtener información o un diseño **a partir de un producto ya hecho**. Busca determinar sus componentes, cómo interactúan entre sí y cómo se fabricó. Se hace porque **no se tiene acceso** a las especificaciones ni a la documentación.

Más que copiar, es un método de resolución: estudiar el funcionamiento de algo hasta poder **entenderlo, modificarlo y mejorarlo**. Un caso conocido fuera del software es el de los juicios entre Apple y Samsung, donde se analizó en detalle el diseño de los teléfonos del otro.

## Nivel de extracción y completitud

| Concepto | Qué mide |
|---|---|
| **Nivel de extracción** | Qué tan sofisticado es el diseño que se logra extraer. De menor a mayor: la relación entre componentes, el modelo del sistema, el diseño estructural de los datos y el diseño de los procesos |
| **Completitud** | Cuánto detalle se obtiene en un nivel dado |

Ambas suelen ser **inversamente proporcionales**: a más bajo nivel de extracción, mayor completitud. Es fácil saber con detalle qué componentes hay y cómo se llaman; reconstruir el razonamiento completo de un proceso es mucho más difícil.

## En el mundo del software

Ventajas de la ingeniería inversa aplicada al software:

- **reducir la complejidad** de un sistema heredado, al entender qué hace realmente;
- **recuperar o actualizar información** perdida, como un diseño sin documentación;
- **identificar el alcance** de un producto;
- **facilitar la reutilización** de componentes;
- **analizar vulnerabilidades**.

En la web, la herramienta más directa es **DevTools**: la pestaña *Network* muestra los endpoints, métodos y formatos que usa el frontend, y permite usar APIs no documentadas. Dos casos reales muestran el alcance:

- Un desarrollador analizó el ejecutable de **GTA Online** y descubrió que la carga tardaba minutos por un parser de JSON ineficiente; su arreglo redujo el tiempo en un 70%.
- Un investigador usó ingeniería inversa para encontrar vulnerabilidades graves en el sistema de cuentas de **Electronic Arts**, que afectaban a cientos de millones de cuentas.

> [!warning] El frontend no guarda secretos
> Todo lo que se envía al navegador (código JS, claves de APIs, reglas de validación) puede leerse e imitarse. Las validaciones y permisos que importan tienen que verificarse en el servidor.

## Tipos de hackers

| Tipo | Quiénes son | Qué hacen |
|---|---|---|
| **Black hat** | Cibercriminales que acceden ilegalmente a sistemas con intenciones maliciosas | Al encontrar una vulnerabilidad, la explotan (por ejemplo, con un troyano). Ejemplo: ransomware |
| **White hat** | Hackers de seguridad **éticos** | Con **permiso** de las organizaciones, buscan debilidades en sus sistemas para corregirlas |
| **Gray hat** | Cruzan la línea entre el "bien" y el "mal" | Acceden **sin permiso** pero normalmente sin causar daño; pueden exigir un pago por revelar o solucionar lo que encontraron |

> [!tip] La diferencia es el permiso y la intención
> Las técnicas de un white hat y de un black hat pueden ser idénticas. Lo que cambia es si hay autorización del dueño del sistema y qué se hace con lo encontrado. Por eso existen los programas de *bug bounty*, que autorizan y pagan la búsqueda de vulnerabilidades.

## Preguntas de repaso

> [!question]- ¿Por qué la completitud suele disminuir al aumentar el nivel de extracción?
> Porque los niveles bajos (qué componentes hay y cómo se relacionan) se observan directamente, mientras que los altos (el diseño de los procesos y las decisiones detrás) hay que inferirlos, y esa inferencia deja huecos.

> [!question]- ¿Qué implica para la seguridad que el frontend se pueda inspeccionar?
> Que nada de lo que llega al navegador es secreto: cualquiera puede leer el código, ver las requests y enviar requests propias. El servidor debe validar todo y no confiar en el cliente.

> [!question]- ¿Qué distingue a un white hat de un gray hat?
> El permiso: el white hat trabaja con autorización de la organización para encontrar y corregir vulnerabilidades. El gray hat accede sin permiso, aunque normalmente sin causar daño.
