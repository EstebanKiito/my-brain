---
ramo: "Arquitectura de Sistemas de Software"
tema: "Métodos de escalabilidad"
tags:
  - arquisis/escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Escalamiento vertical y horizontal]]"
---

# Modelación de sistemas para escalar

Agregar máquinas solo funciona si el sistema está **diseñado** para repartirse entre ellas. Los métodos de modelación de sistemas son recomendaciones y buenas prácticas sobre **componentes**, **conectores** y **configuraciones** que hacen que crecer sea barato. Son, en la práctica, la checklist para revisar un diagrama de componentes pensando en escalabilidad.

## Modelación de componentes

- **Dar a cada componente un propósito claro y bien definido.** Un componente que hace una sola cosa se escala de forma independiente.
- **Darle una interfaz simple y entendible.**
- **No recargar a los componentes con responsabilidades de interacción**: el ruteo y la coordinación van en los conectores.
- **Evitar la heterogeneidad innecesaria**: cada tecnología distinta agrega operación y traducciones.
- **Cuidar la sobrecarga de comunicación** y las **fuentes de datos distribuidas**.
- **Replicar datos cuando es necesario**, no por defecto.

## Modelación de conectores

- **Usar conectores explícitos**: que la comunicación se vea en el diseño (una cola, un balanceador, una API) y no esté escondida en el código.
- **Dar a cada conector una responsabilidad clara.**
- **Elegir el conector más simple** que resuelva la tarea.
- **Diferenciar dependencias directas de indirectas** (y asíncronas).
- **No poner funcionalidad de la aplicación en los conectores**: es el principio de *dumb pipes*.
- **Aprovechar los conectores explícitos para escalar los datos**: caché, *hoarding* (guardar datos localmente para trabajar desconectado), *prefetching* y *buffering*.

## Configuraciones

- **Evitar cuellos de botella** agregando componentes: **réplicas** y **balanceo de carga**.
- **Usar procesamiento paralelo**: si el problema es naturalmente paralelizable, escala con eficiencia.
- **Ubicar las fuentes de datos cerca de los consumidores**: caching, prefetching y réplicas, incluso a nivel físico (regiones).
- **Hacer transparente la distribución**: réplicas y despliegues fáciles, sin que el cliente sepa cuántas instancias hay.
- **Usar los estilos apropiadamente:**

| Escalan bien | Por qué |
|---|---|
| **Pub/sub y basados en eventos** | Emisores y receptores desacoplados; se agregan consumidores sin tocar al emisor |
| **Intérprete y pipe & filter** | Componentes independientes que se pueden replicar por separado |
| **Comunicación asíncrona** | El llamador no se bloquea; las colas absorben los picos |

## Caso: las reglas de Instagram

Instagram escaló de 0 a decenas de millones de usuarios con un equipo pequeño siguiendo estas prácticas:
1. **Pruebas unitarias y funcionales extensivas**, para poder cambiar rápido sin romper.
2. **Mantener el sistema DRY** (*Don't Repeat Yourself*).
3. **Acoplamiento débil** mediante notificaciones y señales.
4. **Casi todo el código en Python** (C solo si hace falta), lo que **promueve la especialización y la homogeneidad**.
5. **Revisiones de código frecuentes.**
6. **Mucho monitoreo**: munin, statsd, PagerDuty.
7. **¡No reinventar la rueda!**
8. **No sobreoptimizar ni adivinar dónde vendrá el problema de escalabilidad**: medir y atacar el cuello real.

> [!tip] La idea detrás de las reglas de Instagram
> Escalar no es solo infraestructura: es poder **cambiar el sistema rápido y con seguridad** mientras crece. Tests, código homogéneo, acoplamiento débil y monitoreo son lo que permite "cambiar las piezas del auto a 100 mph".

> [!warning] Poner lógica en los conectores
> Un balanceador o un broker que decide reglas de negocio se vuelve un componente que no se puede replicar ni cambiar libremente, y acopla a todos los que pasan por él. Los conectores transportan, enrutan y, a lo más, cachean.

## Preguntas de repaso

> [!question]- ¿Por qué conviene que cada componente tenga un propósito claro y bien definido para escalar?
> Porque se puede replicar y dimensionar según su propia carga. Un componente que mezcla responsabilidades obliga a escalar todo junto, aunque solo una de ellas esté saturada.

> [!question]- ¿Qué significa usar conectores explícitos y qué técnicas de datos habilitan?
> Que la comunicación entre componentes es un elemento visible del diseño (una cola, un balanceador, un proxy) y no una llamada escondida en el código. Al ser explícitos, se les puede agregar caché, prefetching, buffering o hoarding sin tocar los componentes.

> [!question]- Nombre tres configuraciones que mejoran la escalabilidad.
> Agregar réplicas con balanceo de carga, ubicar los datos cerca de los consumidores (caché, prefetching, réplicas regionales) y hacer la distribución transparente para el cliente. También usar procesamiento paralelo cuando el problema lo permite.

> [!question]- ¿Qué estilos menciona el curso como favorables para escalar y por qué?
> Pub/sub y basados en eventos, porque desacoplan emisores y receptores y permiten agregar consumidores sin tocar al emisor. Intérprete y pipe & filter, porque sus componentes independientes se replican por separado. Y en general la comunicación asíncrona, porque absorbe los picos en colas.

> [!question]- ¿Por qué Instagram escribió casi todo en Python y no en varios lenguajes "óptimos"?
> Para evitar la heterogeneidad innecesaria: un solo lenguaje permite que cualquiera del equipo entienda y cambie cualquier parte, reduce la operación y promueve la especialización. Solo se usaba C donde la performance realmente lo exigía.

> [!question]- V o F: "Conviene optimizar desde el inicio todas las partes que podrían ser cuello de botella en el futuro".
> Falso. La regla de Instagram es no sobreoptimizar ni adivinar: se mide, se identifica el cuello de botella real y se ataca ese. Optimizar por adelantado agrega complejidad donde quizás nunca haga falta.
