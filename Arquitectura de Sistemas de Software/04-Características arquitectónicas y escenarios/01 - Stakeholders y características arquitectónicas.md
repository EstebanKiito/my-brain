---
ramo: "Arquitectura de Sistemas de Software"
tema: "Características arquitectónicas y escenarios"
tags:
  - arquisis/atributos
  - origen/complemento
prerrequisitos:
  - "[[03 - Tradeoffs y conocimiento de dominio]]"
---

# Stakeholders y características arquitectónicas

Los requerimientos llegan desde muchas personas a la vez, y cada una pide algo distinto: el analista quiere que todo salga rápido, quien despliega quiere estabilidad, marketing quiere funcionalidades. ¿Qué se atiende primero? Responder esa pregunta es el corazón del trabajo arquitectónico, y en la prueba se traduce en la pregunta más repetida del curso: **"indique las características arquitectónicas fundamentales, en orden de prioridad, y justifique"**.

## Identificar componentes

Antes de priorizar hay que saber de qué está hecho el sistema. Métodos para identificar componentes:
- **Partición por dominio frente a partición técnica.** Por ejemplo, decidir entre capas (técnica) y servicios por área de negocio (dominio). Normalmente solo conocemos la técnica.
- **Modelo actor/acción** (desde RUP): "el usuario hace X sobre Y con el rol Z". Ayuda a capturar requisitos y es muy cercano a las historias de usuario.
- **Event storming**: ¿qué eventos gobiernan la aplicación? Logra un buen alcance de la complejidad.
- **Domain-Driven Design**, que se ve más adelante en el curso.

## Stakeholders

> [!tip] Stakeholders
> Las **partes involucradas** del proyecto que pueden verse afectadas por su resultado: usuarios, clientes, desarrolladores, operaciones, negocio, e incluso terceros afectados u otras organizaciones.

Características típicas:
- hacen **peticiones ilimitadas**;
- tienen **poca o nula consideración por otras áreas**;
- tienen **vistas parciales** del negocio.

Dicen **cómo quieren que funcione** algo, no necesariamente qué implementar. Los requisitos nuevos siempre vienen de ellos, y el arquitecto recibe esos requisitos y decide qué tradeoffs aceptar.

## Características arquitectónicas

> [!tip] Características arquitectónicas
> También llamadas **NFR** (*non-functional requirements*, requisitos no funcionales) o **atributos de calidad**. Las propiedades no funcionales son el **resultado de las decisiones de arquitectura**; los requisitos no funcionales son los **"valores" que se esperan** de esas propiedades: que sea más rápida, escalable, segura, confiable…

- Influyen en cómo se entiende y se trata la parte técnica.
- Son **críticas para la operación** y para su éxito.
- Su definición proviene de las **metas de negocio** y de la experiencia del equipo.

**Un sándwich no puede tener todos los ingredientes:** hay que elegir qué deseos cumplirá el sistema, y en eso se diferencia la aplicación.

![Tabla de tipos de requisitos no funcionales](adjuntos/Tipos%20de%20requisitos%20no%20funcionales.png)

> [!example]- Transcripción de la imagen
> | Tipo | Ejemplos de NFR |
> |---|---|
> | Estructural | Mantenibilidad, Flexibilidad/Extensibilidad, Interoperabilidad |
> | Operacional | Performance, Escalabilidad, Confiabilidad, Disponibilidad |
> | Transversal | Seguridad, Auth/auth, Usabilidad, Reusabilidad, Soporte, Time to market |

- **Estructurales:** se ven en el **código**.
- **Operacionales:** se ven en la **operación** (runtime).
- **Transversales:** afectan tanto al código como a la operación.

## Cómo decide el arquitecto cuáles son clave

| Factor | Ejemplo |
|---|---|
| **Tiempo** | "Somos una startup: en 6 meses nos compran". Importa más tener la app funcionando y soportando carga que un código pulcro |
| **Dinero** | "Solo tenemos 5 devs". Los sueldos limitan lo que se puede construir y operar |
| **Mercado** | "Mañana sale el producto de la competencia". El diferenciador manda |
| **Estándares** | "El equipo solo maneja C y Assembler". Conviene que el código sea lo más mantenible posible |
| **Pasado / presente / futuro** | Decidir con base en lo que ocurrió, lo que ocurre y lo que se espera |

En el curso se piden **al menos 3** atributos, aunque un sistema real puede tener más. Cada atributo es **una promesa que debe cumplirse**. **Un atributo sin métrica pierde sustentabilidad.** Demasiados atributos limitan la capacidad de acción, y muy pocos limitan la utilidad.

> [!warning] Cómo se corrige la pregunta de atributos
> Las pautas traen listas de atributos **válidos** y **no válidos** para cada caso. Un atributo solo suma si está **ligado al enunciado**.
> - "Se esperan 10.000 usuarios" justifica **escalabilidad**.
> - "No se habla de conectar con otros sistemas" hace que **integrabilidad** no aplique.
> - **Portabilidad** solo vale si hay distintos ambientes reales (sistemas operativos o plataformas), no "porque es una app de celular".
> - **Mantenibilidad** o **reusabilidad** suelen ser inválidas si el enunciado no habla de cambios frecuentes.
> Hay que ordenarlos por prioridad y justificar cada uno con una frase del caso.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre una propiedad no funcional y un requisito no funcional?
> La propiedad no funcional (el atributo de calidad que el sistema exhibe) es el resultado de las decisiones de arquitectura. El requisito no funcional es el valor que se espera de esa propiedad, como "p95 < 500 ms".

> [!question]- Clasifique como estructural, operacional o transversal: mantenibilidad, disponibilidad, seguridad, performance, interoperabilidad.
> Estructurales: mantenibilidad e interoperabilidad. Operacionales: disponibilidad y performance. Transversal: seguridad.

> [!question]- ¿Por qué los stakeholders no pueden definir solos la arquitectura?
> Porque hacen peticiones ilimitadas, consideran poco a las otras áreas y tienen vistas parciales del negocio. El arquitecto integra sus pedidos, los prioriza y decide los tradeoffs.

> [!question]- Mini caso: Comisaría Virtual emite permisos críticos y denuncias con identidad del usuario, con alta demanda en pandemia. Indique tres atributos en orden de prioridad.
> 1) Seguridad: maneja identidad y trámites sensibles. 2) Disponibilidad: los permisos son críticos y el servicio debe estar arriba. 3) Escalabilidad: picos masivos de demanda. Mantenibilidad sería la menos importante, porque no había muchos cambios.

> [!question]- ¿Qué factores usa el arquitecto para decidir qué atributos priorizar?
> El tiempo disponible, el dinero y el tamaño del equipo, el mercado y la competencia, los estándares y las capacidades del equipo, y el análisis del pasado, el presente y el futuro del negocio.

> [!question]- V o F: "En una app para celular siempre corresponde priorizar portabilidad".
> Falso. Solo corresponde si el caso exige correr en ambientes distintos (varios sistemas operativos o plataformas) y se justifica. Que sea una app móvil no basta por sí solo.

> [!question]- ¿Qué es el modelo actor/acción y para qué sirve?
> Es una forma de capturar requisitos del tipo "el usuario hace X sobre Y con el rol Z", cercana a las historias de usuario. Sirve para identificar componentes y las responsabilidades del sistema.
