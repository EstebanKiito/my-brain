---
ramo: "Arquitectura de Sistemas de Software"
tema: "Flujo de datos e invocación implícita"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[02 - Main y subrutinas y arquitectura en capas]]"
---

# Flujo de datos por lotes y pipe and filter

En los estilos de **flujo de datos**, lo que importa es cómo se transforman los datos al pasar por los componentes: **datos de entrada → componente → datos de salida**. Hay dos variantes. **Por lotes secuencial** es simple y rígida. **Pipe and filter** es más poderosa y reorganizable. Ambas aparecen seguido en las pruebas, con una trampa sobre qué significa "filtrar".

![Un componente que recibe datos de entrada y entrega datos de salida](adjuntos/Componente%20de%20flujo%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - Croquis: **DATOS (IN)** entran a un componente rectangular y salen como **DATOS (OUT)**.
> - Bajo el componente hay una base de datos conectada por una interfaz.
> - Leyenda arriba: línea punteada = capas; línea continua = lotes.

## Por lotes, secuencial

**Programas separados que se ejecutan en orden.** Si todo el procesamiento de los datos se ordena paso a paso, se obtiene un flujo por lotes secuencial.
- **Aplicaciones por lotes:** sistemas de banca e inventario. Al final del día se toman las transacciones, se ordenan y se registran para tener información fidedigna.
- **Aplicaciones secuenciales:** control y robótica, compiladores.

**Características:**
- Es un **pipeline lineal y estricto**: un solo programa ejecutándose a la vez, sin información ni flujo en paralelo.
- Los datos van paso a paso, y cada programa **depende del anterior**.
- La salida de cada paso **debe tener el formato correcto** para la entrada del siguiente.
- Es **sencillo** y fácil de asociar con otros sistemas.

![Comparación entre capas y lotes](adjuntos/Lotes%20secuenciales%20frente%20a%20capas.png)

> [!example]- Transcripción de la imagen
> - Croquis con tres componentes en fila. Con línea punteada, las flechas que representan **capas** (ida y vuelta entre componentes). Con línea continua, las de **lotes** (solo hacia adelante).
> - El último componente tiene una X: si un paso falla, hay que volver a empezar.

**Diferencia con capas cerradas:** en capas, la petición pasa por todos los componentes y vuelve, y si falla una capa la petición falla completa. Por lotes es **exclusivamente para flujo de datos**: cada paso transforma y entrega al siguiente. **Lotes gana** cuando se procesa un volumen de datos. **Capas gana** cuando hay procesos distintos, peticiones y respuestas.

## Pipe and filter

Un estilo **sumamente poderoso**:
- Los **componentes (filtros)** tienen interfaces claras y cada uno cumple una **función encapsulada**.
- Los **pipes** (tuberías) suelen ser **unidireccionales y punto a punto**.
- Una transformación puede **empezar antes de que termine la anterior** (procesamiento de un flujo continuo), y los filtros pueden ser concurrentes.

```bash
cat Readme.md | grep "Error" | grep "shutdown"
```

Cada `|` es un pipe: la salida de `cat` entra a `grep`, cuya salida entra al siguiente `grep`.

**Ejemplos:** pipes de Linux, pipelines de procesamiento de imágenes (por ejemplo, en machine learning), procesamiento de audio y **ETLs**.

![Pipeline de JavaScript con struct, transform y load usando map y reduce](adjuntos/Pipeline%20map%20reduce%20como%20pipe%20and%20filter.png)

> [!example]- Transcripción de la imagen
> - Croquis con tres etapas anotadas arriba: **Struct**, **Transform**, **Load** (un ETL).
> - En JavaScript, un componente de entrada alimenta tres **MAP** en paralelo, que confluyen en un **reduce**.

![Pipe and filter encapsulado en un componente UML](adjuntos/Pipe%20and%20filter%20en%20UML.png)

> [!example]- Transcripción de la imagen
> - Croquis "En UML": un componente grande **Pipe & Filter** con una interfaz de entrada (con puerto) a la izquierda.
> - Dentro, **Filtro** → … → **Filtro** encadenados por interfaces, y una interfaz de salida a la derecha.

**Ventaja sobre lotes:** cada filtro se puede **reorganizar** según lo que se necesite, y se pueden insertar, quitar o reordenar filtros.

| Pros | Contras |
|---|---|
| **Modular**: fácil de modificar y mantener | Requiere un **proceso organizado**: **no soporta aplicaciones interactivas** |
| **Reusable**: los filtros sirven en otros pipelines | **Complejidad**: al extenderse, se acopla más |
| **Cada filtro puede escalar** por separado | **No toda la data es compatible** entre filtros |
| **Flexible y testeable** | Se acumula **overhead** y se transmite el **mínimo común denominador** de datos |

> [!warning] Pipe and filter filtra; no es "cualquier procesamiento"
> Las pautas aceptan pipe and filter para **filtrar** datos (descartar duplicados, validar formato, limpiar entradas) y lo rechazan cuando se usa para **procesamiento pesado**: "los filtros deben ser simples y, como dice el nombre, filtran los datos, no los procesan". Para procesar (analizar con IA, comprimir video) se usan workers, EDA o un estilo por lotes.

## Preguntas de repaso

> [!question]- ¿Qué caracteriza al estilo por lotes secuencial y dónde se usa?
> Programas que se ejecutan en orden, uno a la vez, donde cada uno depende del formato de salida del anterior. Se usa en procesos batch como el cierre diario de un banco o un inventario, y en procesos secuenciales como compiladores.

> [!question]- ¿Cuándo gana lotes y cuándo gana capas?
> Lotes gana cuando hay que procesar un volumen de datos con transformaciones sucesivas. Capas gana cuando hay procesos distintos con peticiones y respuestas, como una aplicación web que atiende usuarios.

> [!question]- ¿Qué ventaja tiene pipe and filter sobre lotes?
> Los filtros son independientes y reorganizables (se agregan, quitan o reordenan), cada uno puede escalar por separado y pueden trabajar sobre un flujo continuo de forma concurrente, sin esperar a que el paso anterior termine el lote completo.

> [!question]- ¿Por qué pipe and filter no sirve para aplicaciones interactivas?
> Porque es un flujo unidireccional de transformaciones: el dato entra, pasa por los filtros y sale. No contempla ida y vuelta con el usuario ni respuestas que cambien el flujo en medio.

> [!question]- Mini caso: noticias subidas en JSON deben revisarse para descartar duplicados y validar el formato antes de guardarse. ¿Aplica pipe and filter?
> Sí: es filtrado de datos. Un filtro descarta duplicados, otro valida el formato y otro normaliza campos, encadenados antes del almacenamiento. Encaja con lo que las pautas aceptan.

> [!question]- Mini caso: se propone pipe and filter para que una IA analice el audio de llamadas sospechosas. ¿Qué responde?
> Que no corresponde: analizar audio con IA es procesamiento pesado, no filtrado, y las pautas lo rechazan. Conviene encolar el trabajo para workers (EDA) o usar un flujo por lotes.

> [!question]- V o F: "En pipe and filter, los pipes son típicamente bidireccionales".
> Falso. Típicamente son unidireccionales y punto a punto: el dato fluye de un filtro al siguiente.
