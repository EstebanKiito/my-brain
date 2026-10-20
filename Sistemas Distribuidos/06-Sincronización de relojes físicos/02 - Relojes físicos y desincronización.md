---
ramo: "Sistemas Distribuidos"
tema: "Sincronización de relojes físicos"
tags:
  - sd/relojes
  - origen/complemento
prerrequisitos:
  - "[[01 - Coordinación en sistemas distribuidos]]"
---

# Relojes físicos y desincronización

Cada nodo de un sistema distribuido tiene su propio reloj, y ningún reloj de hardware es perfecto: con el tiempo, cada uno marca una hora distinta. Si los nodos usan esas horas locales para registrar eventos, el orden de los eventos queda mal. La **sincronización de relojes** busca reducir esas diferencias.

## El problema

Por su naturaleza, un sistema distribuido opera con **relojes físicos individuales** que divergen por variaciones del hardware y otros factores. Entonces un evento que ocurrió **después** de otro puede quedar registrado con una hora **anterior**:

- Si es un *like*, da igual.
- Si es una modificación a una base de datos, una transacción bancaria o un registro médico, el orden equivocado genera **inconsistencias** graves.
- Algunos servicios en línea incluso rechazan o bloquean a clientes cuyo reloj está muy desfasado, porque sus marcas de tiempo no calzan con las del servidor.

## Cómo funciona un reloj físico

Un **reloj físico** es un dispositivo electrónico que cuenta las **oscilaciones** de un cristal a una frecuencia definida y guarda el resultado en un contador.

- Los relojes de **cuarzo** tienen una **tasa de deriva** (*drift rate*) de aproximadamente $10^{-6}$ segundos por segundo, unos **31,5 segundos por año**. Sin conexión a una referencia externa, se desincronizan.
- Los relojes **atómicos**, basados en transiciones de átomos de cesio, son muchísimo más precisos.

$$10^{-6}\ \tfrac{\text{s}}{\text{s}} \times 31\,536\,000\ \tfrac{\text{s}}{\text{año}} \approx 31{,}5\ \tfrac{\text{s}}{\text{año}}$$

> [!tip] Regla
> Todo reloj físico que no sea atómico se va a desincronizar eventualmente. Por eso hay que **actualizar el contador cada cierto tiempo** consultando a una fuente mejor.

## Cómo se corrige un reloj

La sincronización busca un **orden temporal consistente** de los eventos:

- Si un nodo está **atrasado**, **adelanta** su reloj.
- Si un nodo está **adelantado**, normalmente **no retrocede**: hace que su reloj avance **más lento** hasta que los demás lo alcancen.

> [!warning] ¿Por qué no retroceder?
> Si el reloj vuelve atrás, un evento posterior puede quedar con una marca de tiempo **menor** que uno anterior del mismo nodo, o la misma hora puede repetirse. En un registro médico o en un log, eso rompe el orden de los eventos y genera inconsistencias. Ralentizar el reloj corrige el desfase sin que el tiempo "retroceda".

## Dos enfoques

| Enfoque | Qué sincroniza | Cuándo sirve |
|---|---|---|
| **Reloj físico** | La hora real (cercana a UTC) | Cuando importa la hora absoluta: registros, certificados, expiraciones |
| **Reloj lógico** | Solo el **orden** de los eventos | Cuando basta saber qué ocurrió antes de qué |

Para relojes físicos, el curso estudia tres algoritmos: [[03 - Método de Cristian|Cristian]], [[04 - Algoritmo de Berkeley|Berkeley]] y [[05 - Protocolo NTP|NTP]]. Los relojes lógicos (Lamport y vectoriales) se estudian en el tema siguiente.

## Preguntas de repaso

> [!question]- ¿Cuánto se desvía un reloj de cuarzo en un año y de dónde sale ese número?
> Unos 31,5 segundos: una deriva de $10^{-6}$ segundos por cada segundo, multiplicada por los aproximadamente 31,5 millones de segundos de un año.

> [!question]- Un nodo descubre que está 5 segundos adelantado. ¿Qué hace y por qué?
> En vez de retroceder 5 segundos, ralentiza su reloj hasta que los demás lo alcanzan. Así sus marcas de tiempo nunca disminuyen y no se rompe el orden de sus propios eventos.

> [!question]- ¿Cuándo basta un reloj lógico y cuándo hace falta un reloj físico sincronizado?
> Basta un reloj lógico cuando solo importa el orden relativo de los eventos. Hace falta un reloj físico cuando importa la hora real, por ejemplo para saber si un certificado expiró o para registrar la hora de un examen médico.
