---
ramo: Ingeniería de Software
tema: Procesos de desarrollo
tags: [ingsoft/procesos, ingsoft/agil, origen/apuntes]
prerrequisitos: ["[[Procesos iterativos e incrementales]]"]
---
# Metodologías ágiles y manifiesto ágil

Las metodologías ágiles son procesos **iterativos e incrementales** que priorizan a las personas, el software funcionando, la colaboración con el cliente y la flexibilidad ante el cambio. Sus valores y principios están en el **Manifiesto Ágil**.

## Modelo ágil (agile)
- Se valora más a **individuos e interacciones** que procesos y herramientas.
- **+ Software funcional − Documentación exhaustiva**
- **Colaboración con clientes**
- **Flexibilidad**

![Metodología ágil - ciclo](adjuntos/Metodología%20ágil%20-%20ciclo.png)

> [!note]- Transcripción de la imagen
> Ciclo "Metodología AGILE": 1. Evaluación de procesos y estructura actual de la empresa → 2. Sugerencias de mejora y optimización de procesos → 3. Diseño de la aplicación en conjunto con el cliente → 4. Construcción e implementación de la aplicación → 5. Evaluación y monitoreo → (vuelve a 1).

## Manifiesto Ágil
- *"Nuestra mayor prioridad es satisfacer al cliente a través de una entrega temprana y continua de software valioso para él"*.
- *"Abrazamos los cambios en los requerimientos, incluso si llegan tarde en el proceso"*.

> [!tip] Complemento — los 4 valores completos (slides "Procesos de Desarrollo de Software")
> Dar más valor a…
> | Más valor a… | …que a |
> |---|---|
> | Individuos e interacciones | procesos y herramientas |
> | Software funcional | documentación exhaustiva |
> | Colaboración con el cliente | negociación de un contrato |
> | Respuesta al cambio | seguir un plan |
>
> El manifiesto aclara que los elementos de la derecha **también tienen valor**, pero se valoran más los de la izquierda. Fuente: https://agilemanifesto.org/principles.html

> [!tip] Complemento — los 12 principios (libro del curso, cap. 2.4)
> Los dos que anotaste son los primeros. El libro los resume así:
> 1. **Satisfacción del cliente** con entregas tempranas y continuas de software valioso.
> 2. **Cambios en los requisitos** bienvenidos, incluso tarde, para dar ventaja competitiva.
> 3. **Entrega frecuente** de software funcionando, prefiriendo intervalos cortos.
> 4. **Colaboración** diaria entre clientes/usuarios y desarrolladores.
> 5. **Individuos motivados**: darles el entorno y la confianza que necesitan.
> 6. **Comunicación cara a cara** como la forma más efectiva.
> 7. **Software funcionando** como medida principal de progreso.
> 8. **Desarrollo sostenible**: un ritmo constante que se pueda mantener.
> 9. **Excelencia técnica** y buen diseño, que mejoran la agilidad.
> 10. **Simplicidad**: maximizar el trabajo *no* realizado.
> 11. **Equipos autoorganizados**.
> 12. **Reflexión y ajuste** a intervalos regulares.
>
> El manifiesto lo escribió un grupo de **17 desarrolladores** (2001) como reacción a los problemas de los procesos tradicionales como la [[Modelo en cascada|cascada]].

> [!tip] Complemento — modelos ágiles conocidos (libro)
> - **Scrum:** iteraciones de duración fija (*sprints*, generalmente de 2 a 3 semanas). El *product owner* prioriza y, al final de cada sprint, hay **review** del producto y **retrospectiva** del proceso. Es tan popular que muchas veces se usa como sinónimo de "ágil".
> - **Kanban:** **sin** iteraciones de largo fijo. Optimiza el flujo de tareas de "por hacer" a "hecho" visualizando el progreso y **limitando el trabajo en curso**.
> - **[[Programación extrema (XP)]]:** un conjunto de buenas prácticas técnicas, como pruebas primero y programación en pares.
> - Alistair Cockburn (coautor del manifiesto) resume la agilidad en **colaborar, entregar, reflexionar, mejorar** (*Heart of Agile*).

> [!warning] Error común
> "Ágil" **no** significa "sin documentación" ni "sin planificación". Significa que, cuando hay que elegir, se privilegia el software funcionando y la respuesta al cambio. Se sigue documentando y planificando, pero lo justo y en ciclos cortos.

## Preguntas de repaso

1. Enuncia los 4 valores del Manifiesto Ágil.
> [!question]- Respuesta
> Individuos e interacciones sobre procesos y herramientas; software funcionando sobre documentación exhaustiva; colaboración con el cliente sobre negociación de contratos; respuesta al cambio sobre seguir un plan.

2. ¿Qué dice el primer principio del manifiesto?
> [!question]- Respuesta
> "Nuestra mayor prioridad es satisfacer al cliente a través de una entrega temprana y continua de software valioso para él".

3. ¿Por qué los procesos ágiles son iterativos e incrementales?
> [!question]- Respuesta
> Porque entregan software funcionando en ciclos cortos: cada ciclo agrega funcionalidad (incremental) y la ajusta según el feedback (iterativo). Así se acepta el cambio incluso tarde.

4. ¿Cuál es la diferencia principal entre Scrum y Kanban?
> [!question]- Respuesta
> Scrum trabaja en iteraciones de duración fija (sprints) con reuniones de review y retrospectiva. Kanban no usa iteraciones fijas: optimiza un flujo continuo de tareas limitando el trabajo en curso.

5. Verdadero o falso: el Manifiesto Ágil promueve la documentación exhaustiva como prioridad.
> [!question]- Respuesta
> Falso. Valora más el software funcionando que la documentación exhaustiva, aunque reconoce que la documentación también tiene valor.
