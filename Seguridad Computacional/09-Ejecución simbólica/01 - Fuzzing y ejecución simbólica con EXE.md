---
ramo: "Seguridad Computacional"
tema: "Ejecución simbólica"
tags:
  - seguridad/bugs
  - origen/complemento
prerrequisitos:
  - "[[01 - Buffer overflows y sus defensas]]"
---

# Fuzzing y ejecución simbólica con EXE

Los bugs son la fuente principal de exploits, así que automatizar su búsqueda automatiza la búsqueda de vulnerabilidades. Las pruebas escritas a mano cubren lo intencionado y lo ya conocido, pero no la funcionalidad no prevista ni los bugs desconocidos, y es difícil que ejecuten cada línea. Dos enfoques automáticos: *fuzzing* y ejecución simbólica (**EXE**).

## Ecosistema de bugs
Los investigadores buscan fallos y los divulgan al vendedor y, tras un plazo (por ejemplo 90 días), al público; los **CVE** los registran y hay programas de recompensas. Los bugs buscados incluyen división por cero, punteros nulos y accesos fuera de límites, y violaciones de *asserts* específicos (una transferencia que cambia la suma total de cuentas, una cookie que suplanta a otro usuario).

## Fuzzing
Se ejecuta el programa con muchas entradas aleatorias hasta que alguna cause un crash o dispare un `assert`.
- Hay que identificar las entradas (argumentos, solicitudes HTTP) y generar entradas **sintácticamente válidas** con contenido aleatorio donde hay libertad (`GET /transfer?from=xxx&to=yyy&amount=zzz`); si no, nunca se llega "profundo".
- **Ventajas:** funciona bien con buffer overflows, sirve en sistemas de caja negra por red y sin código fuente.
- **Desventajas:** consume CPU y se pierden bugs que exigen una entrada concreta (`if command == "credit"`) o muy estructurada (un compilador).

## Ejecución simbólica
Se ejecuta el programa con **valores simbólicos** (α, β) en vez de concretos y se explora cada camino:
1. Cada variable guarda una *expresión* en términos de las entradas.
2. En cada `if` el proceso se bifurca (`fork`): una rama agrega la condición a la **restricción de camino** (*path constraint*, pc) y la otra su negación.
3. Un **solver de restricciones** (STP) revisa si el pc es satisfacible; en una llamada a `error()` o un assert fallido, si lo es, entrega entradas concretas que lo disparan.

```
1. read x, y
2. if x > y:   x = y
4. if x < y:   x = x + 1
6. if x + y == 7:  error()
```
Camino con `α <= β` y `α < β`: `x = α + 1`, y `α + 1 + β == 7` tiene solución (`α=0, β=6`), así que EXE reporta el fallo con esas entradas. Un fuzzer aleatorio difícilmente lo encontraría.

![Componentes de EXE en tiempo de ejecución](adjuntos/Componentes%20de%20EXE%20en%20tiempo%20de%20ejecuci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Symbolic Execution Runtime Components": el *App Process* envía una *constraint* al *Solver* (STP), que responde "ok / no / don't know"; el *Scheduler* crea nuevos procesos (`createNewProc`) para el bucle de ejecución.

**EXE** traduce C a C (todo menos punto flotante): instrumenta asignaciones, expresiones y ramas (si todos los argumentos son concretos, ejecuta normal) y mantiene una tabla de rangos de memoria simbólicos. Un *servidor de búsqueda* elige qué proceso sigue: en profundidad se atasca en bucles con límites simbólicos, en amplitud no avanza; usa la heurística *best-first* (la línea menos ejecutada, con DFS un rato).

## Límites
- El solver es lo difícil: `x + y = 10` es fácil, `900 = x*x` requiere trucos y `10 = sha1(x)` agota el tiempo.
- No maneja punto flotante ni interacción con el SO (`open(nombre simbólico)`).
- Que no encuentre bugs no prueba que no haya: solo detecta crashes y asserts, el solver puede agotar el tiempo y puede haber demasiados caminos.
- Halló bugs críticos reales (filtros de paquetes BPF, `udhcpd`, `pcre`, sistemas de archivos del kernel), sobre todo buffer overflows.

## Ejecución concólica
Variante del laboratorio 3. Se ejecuta con entradas **concretas** y se va registrando la restricción simbólica del camino seguido (solo un lado de cada `if`); luego se niega una condición del pc, se resuelve para obtener nuevas entradas y se re-ejecuta, explorando otro camino. Es más fácil de agregar a un lenguaje como Python (tipos "proxy" que reemplazan `int` y `string`) y tolera funciones opacas (una consulta a BD), pero pierde algunas restricciones.

## Preguntas de repaso

> [!question]- ¿Por qué la ejecución simbólica encuentra bugs que un fuzzer aleatorio no?
> Porque mira la condición del programa (`x + y == 7`) y resuelve qué entradas la satisfacen, en vez de adivinar al azar.

> [!question]- ¿Por qué EXE consulta al solver en cada bifurcación?
> Para descartar caminos imposibles (restricciones contradictorias) y evitar explorar un número exponencial de ramas inalcanzables.

> [!question]- ¿Qué ventaja da la ejecución concólica cuando hay funciones que no se pueden analizar?
> Ejecuta esas funciones con valores concretos y solo registra restricciones donde puede, así no requiere una base de datos o librería simbólica completa.
