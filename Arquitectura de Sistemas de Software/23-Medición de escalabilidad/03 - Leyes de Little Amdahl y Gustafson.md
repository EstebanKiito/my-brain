---
ramo: "Arquitectura de Sistemas de Software"
tema: "Medición de escalabilidad"
tags:
  - arquisis/escalabilidad
  - arquisis/calculos
  - origen/complemento
prerrequisitos:
  - "[[01 - Escalabilidad escenarios y cuellos de botella]]"
---

# Leyes de Little Amdahl y Gustafson

Tres leyes permiten razonar con números sobre la escalabilidad antes de comprar servidores. **Little** dimensiona cuánta concurrencia hay que atender. **Amdahl** dice cuánto se puede acelerar un problema fijo agregando procesadores. **Gustafson** dice cuánto más trabajo se puede procesar en el mismo tiempo.

## Ley de Little

$$L = \lambda \cdot W$$

- $L$: número promedio de peticiones **dentro del sistema**.
- $\lambda$: tasa promedio de **llegada** (y de salida, en régimen estable).
- $W$: **tiempo promedio** que pasa cada petición en el sistema.

Es muy buena para **dimensionar sistemas**: ¿a cuántos clientes simultáneos tengo que atender si mi sistema crece?

**Ejemplo:** llegan **200 req/s** y cada una tarda **0,3 s**. Entonces $L = 200 \cdot 0{,}3 = 60$ peticiones en curso en promedio. Si cada instancia maneja bien 20 peticiones concurrentes, hacen falta $60 / 20 = 3$ instancias, más un margen. Si la latencia sube a 0,6 s por un problema en la base de datos, $L$ sube a 120 y hacen falta 6 instancias: **la latencia y la capacidad están ligadas**.

## Ley de Amdahl

$$S(N) = \frac{1}{(1-p) + \frac{p}{N}}$$

- $p$: fracción **paralelizable** del trabajo.
- $N$: número de procesadores.
- La parte secuencial $(1-p)$ no se acelera nunca.

**Límite:** con infinitos procesadores, $S_{max} = \frac{1}{1-p}$. Esta ley pone un **límite a cuánto podemos optimizar** un trozo de código y **apunta a dónde conviene optimizar**: a la parte secuencial. Su limitación es que supone un **problema de tamaño fijo**.

| $p$ | $N = 4$ | $N = 10$ | $N = 100$ | $N \to \infty$ |
|---|---|---|---|---|
| 50% | 1,6 | 1,82 | 1,98 | **2** |
| 75% | 2,29 | 3,08 | 3,88 | **4** |
| 90% | 3,08 | 5,26 | 9,17 | **10** |
| 95% | 3,48 | 6,9 | 16,8 | **20** |

![Curvas de speedup de la ley de Amdahl para distintas porciones paralelas](adjuntos/Curva%20de%20la%20ley%20de%20Amdahl%20según%20la%20porción%20paralela.png)

> [!example]- Transcripción de la imagen
> - Gráfico *Amdahl's Law*: speedup (0 a 20) frente al número de procesadores (1 a 65.536, en escala logarítmica).
> - Cuatro curvas según la porción paralela: 50% se aplana en 2, 75% en 4, 90% en 10 y 95% en 20.
> - Todas suben rápido al principio y luego se vuelven horizontales: agregar procesadores deja de servir.

**Ejemplo:** un proceso de 100 s tiene un 10% secuencial (leer la configuración y escribir el resultado) y un 90% paralelizable. Con 10 workers: $S = 1/(0{,}1 + 0{,}09) \approx 5{,}26$, es decir, unos 19 s. Con 100 workers, $S \approx 9{,}17$ (unos 10,9 s). Pasar de 10 a 100 workers multiplica el costo por 10 y solo baja de 19 s a 10,9 s: es la **ley de retornos decrecientes** del escalamiento horizontal.

## Ley de Gustafson

Si **congelamos el tiempo**, ¿cuánto **más** podemos procesar con más procesadores?

$$S(N) = N - (N-1)\cdot s$$

donde $s$ es la fracción secuencial. Es equivalente a $S = s + p \cdot N$ con $p = 1 - s$.

![Rectas de speedup de la ley de Gustafson](adjuntos/Curvas%20de%20la%20ley%20de%20Gustafson.png)

> [!example]- Transcripción de la imagen
> - Gráfico *Gustafson's Law*: speedup frente al número de procesadores (0 a 100). Son rectas que crecen sin aplanarse, con menor pendiente cuanto mayor es la fracción secuencial (las curvas van de 0,1 a 0,9).
> - Debajo, la derivación: $S = s + p \times N = s + (1-s) \times N = N + (1-N) \times s = N - (N-1) \times s$.

**Ejemplo:** con $s = 0{,}1$ y $N = 10$, $S = 10 - 9 \cdot 0{,}1 = 9{,}1$. Con $N = 100$, $S = 90{,}1$. En el mismo tiempo se procesa unas 90 veces más trabajo.

> [!tip] Amdahl frente a Gustafson
> - **Amdahl:** el problema es **fijo** y la pregunta es cuánto más **rápido** lo resuelvo. Es pesimista: hay un techo.
> - **Gustafson:** el tiempo es **fijo** y la pregunta es cuánto **más grande** puede ser el problema. Es optimista: crece casi linealmente.
> Las dos son ciertas. Lo que cambia es la pregunta.

## Preguntas de repaso

> [!question]- Un servicio recibe 500 req/s con latencia promedio de 0,2 s. ¿Cuántas peticiones hay en el sistema en promedio y cuántas instancias se necesitan si cada una maneja 25 concurrentes?
> $L = 500 \cdot 0{,}2 = 100$ peticiones en el sistema. Se necesitan $100 / 25 = 4$ instancias, más un margen para los picos.

> [!question]- Según Little, ¿qué pasa con la capacidad necesaria si la latencia se duplica con la misma tasa de llegada?
> $L = \lambda W$ también se duplica, así que hay el doble de peticiones simultáneas y se necesita el doble de capacidad concurrente. Bajar la latencia es una forma de escalar.

> [!question]- Un programa es 80% paralelizable. ¿Cuál es el speedup máximo posible según Amdahl y cuánto se obtiene con 4 procesadores?
> Máximo: $1/(1-0{,}8) = 5$. Con 4 procesadores: $1/(0{,}2 + 0{,}8/4) = 1/0{,}4 = 2{,}5$.

> [!question]- ¿Qué recomienda Amdahl sobre dónde optimizar?
> Atacar la parte secuencial: es la que fija el techo $1/(1-p)$. Agregar procesadores a la parte paralela tiene rendimientos decrecientes, y reducir la secuencial sube el techo.

> [!question]- Con $s = 0{,}2$ y 50 procesadores, calcule el speedup según Gustafson e interprételo.
> $S = 50 - 49 \cdot 0{,}2 = 40{,}2$. En el mismo tiempo se puede procesar unas 40 veces más trabajo que con un procesador.

> [!question]- ¿Por qué Amdahl y Gustafson parecen contradecirse y por qué no lo hacen?
> Amdahl fija el tamaño del problema y mide la reducción del tiempo, así que choca con la parte secuencial. Gustafson fija el tiempo y deja crecer el problema, y como la parte paralela crece con N, el speedup también crece. Responden preguntas distintas.

> [!question]- V o F: "Si duplico los servidores, el tiempo de procesamiento se reduce a la mitad".
> Falso en general. Por Amdahl, solo la parte paralelizable se acelera, y además la coordinación entre servidores agrega overhead. La reducción es menor que la mitad y decrece al agregar más servidores.
