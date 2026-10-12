---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, origen/complemento]
prerrequisitos: ["[[07 - Estimación de software|Estimación de software]]"]
---
# Puntos de función y líneas de código (medir el tamaño)

> [!tip] Complemento — nota nueva (fuente: slides "Estimaciones" y libro del curso, cap. 7.9)
> **Qué es:** las métricas para estimar el **tamaño** del software, que es la base para estimar esfuerzo y tiempo.
>
> ## Líneas de código (LOC)
> - Es la forma **más sencilla** de medir el tamaño, pero no necesariamente la mejor.
> - **Ventaja:** al terminar el proyecto se conoce exactamente: basta contar las líneas.
> - **Desventajas:**
>   - es muy difícil estimarla **al inicio**;
>   - depende del **lenguaje** (unos son más verbosos), del **estilo** (indentación, llaves, saltos de línea), de la **calidad del código** (`i++` vs `i = i + 1`) y de los **comentarios** y líneas en blanco.
> - Se necesitan métricas que **no dependan del lenguaje** y que **faciliten la estimación temprana**.
>
> **Deseconomía de escala:** a mayor tamaño, **menor productividad**. Un producto de 100.000 LOC requiere probablemente **más de 10 veces** el tiempo de uno de 10.000 LOC, porque más personas significan más canales de comunicación: con N personas hay **N(N−1)/2** canales (2 → 1, 3 → 3, 5 → 10).
>
> ## Puntos de función (PF)
> Fue muy popular en los 80 y 90. Cumple los dos requisitos: es temprana e independiente del lenguaje.
>
> **1) Contar 5 elementos y clasificar cada uno por complejidad:**
> | Tipo | Baja | Mediana | Alta |
> |---|---|---|---|
> | Entradas | ×3 | ×4 | ×6 |
> | Salidas | ×4 | ×5 | ×7 |
> | Consultas | ×3 | ×4 | ×6 |
> | Archivos internos (tablas) | ×7 | ×10 | ×15 |
> | Archivos externos (tablas) | ×5 | ×7 | ×10 |
>
> Por ejemplo, 2 entradas de baja complejidad dan 2 × 3 = 6 puntos y 3 consultas de alta complejidad dan 3 × 6 = 18 puntos. La suma son los **Puntos de Función No Ajustados (PFNA)**.
>
> **2) Factor de complejidad (FC):** se asigna un valor de **0 a 5** a cada uno de **14 factores** y se suman (N entre 0 y 70):
> comunicaciones · funciones distribuidas · objetivos de desempeño · configuración sobrecargada · tasa de transacciones · entrada de datos online · eficiencia para el usuario · actualización en línea · proceso complejo · reuso · facilidad de instalación · facilidad de operación · varios sitios · facilidad de mantención.
>
> **3) Fórmulas:**
> - **FC = 0,65 + N/100**, con 0,65 ≤ FC ≤ 1,35 (ajusta el tamaño hasta ±35%).
> - **PF = PFNA × FC**
>
> ## Story points
> También independientes del lenguaje y tempranos; ponderan cada historia por su complejidad. Ver [[01 - Story points|Story points]].

> [!example] Ejemplo extra — cálculo completo de puntos de función
> - 4 entradas bajas (4 × 3 = 12)
> - 2 salidas medianas (2 × 5 = 10)
> - 3 consultas bajas (3 × 3 = 9)
> - 2 archivos internos medianos (2 × 10 = 20)
> - 1 archivo externo bajo (1 × 5 = 5)
>
> PFNA = 12 + 10 + 9 + 20 + 5 = **56**. Si los 14 factores suman N = 35, entonces FC = 0,65 + 0,35 = **1,00** y PF = 56 × 1,00 = **56**.

## Preguntas de repaso

1. ¿Qué desventajas tienen las líneas de código como métrica de tamaño?
> [!question]- Respuesta
> Son difíciles de estimar al inicio y dependen del lenguaje, del estilo de escritura, de la calidad del código y de los comentarios o líneas en blanco.

2. ¿Qué cinco elementos cuentan los puntos de función?
> [!question]- Respuesta
> Entradas, salidas, consultas, archivos (tablas) internos y archivos (tablas) externos, cada uno clasificado en complejidad baja, mediana o alta.

3. Si N = 70, ¿cuánto vale el factor de complejidad? ¿Y si N = 0?
> [!question]- Respuesta
> Con N = 70, FC = 0,65 + 0,70 = 1,35. Con N = 0, FC = 0,65. El tamaño se ajusta entre −35% y +35%.

4. ¿Qué es la deseconomía de escala en software?
> [!question]- Respuesta
> Que la productividad baja a medida que el proyecto crece, porque se necesitan más personas y los canales de comunicación crecen como N(N−1)/2.
