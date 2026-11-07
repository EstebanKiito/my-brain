---
ramo: "Arquitectura de Sistemas de Software"
tema: "Resolución de casos de diseño"
tags:
  - arquisis/casos
  - arquisis/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Cómo resolver una pregunta de diagrama de componentes]]"
  - "[[04 - Cómo elegir un estilo arquitectónico]]"
---

# Método para resolver un caso de prueba

La pregunta de caso vale cerca de **34 puntos** en cada interrogación: se elige uno de dos casos, se responden tres preguntas propias del caso (a, b, c) y luego cuatro comunes (d, e, f, g). Esta nota reúne cómo se corrigen, según las pautas de varios semestres, y los consejos que dio la ayudantía. Las notas siguientes resuelven casos reales con ese método.

## Estructura de la pregunta

| Ítem | Pide | Puntos |
|---|---|---|
| **a, b, c** | Medidas concretas para un problema del caso (base de datos, caché, escalabilidad, integración, seguridad) | 4 c/u |
| **d** | Al menos 3 **características arquitectónicas** en orden de prioridad, justificadas | 3 |
| **e** | Al menos 2 **estilos o patrones**, con la responsabilidad que ataca cada uno | 4 |
| **f** | **Diagrama de componentes UML** | 13 |
| **g** | **2 falencias o tradeoffs** de la solución, cómo se resuelven y qué implican | 2-4 |

## Preguntas a, b, c: la fórmula de 4 puntos

Las pautas reparten casi siempre así:
1. **Nombrar la medida** (1 punto): sharding, caché por zona, gRPC, OAuth2, MOM.
2. **Ubicarla en el sistema** (1 punto): "en la sección de lectores, entre los usuarios y el servidor".
3. **Justificarla** con el atributo y con el enunciado (2 puntos): "hay muchas escrituras y pocas lecturas, así que leader-follower no sirve".

A veces la pregunta es "¿es buena idea X?". **"No" puede ser la respuesta correcta**, pero hay que justificarlo y **proponer una alternativa** (2 + 2 puntos).

## Pregunta d: características

- Mínimo 3, **en orden**, cada una amarrada a una frase del enunciado.
- Las pautas traen listas de **válidas** y **no válidas**. Patrones que se repiten:

| Suele valer si… | Suele NO valer si… |
|---|---|
| **Escalabilidad**: "miles de usuarios", "se espera crecimiento", "100 GB por minuto" | **Integrabilidad**: no se habla de otros sistemas, o los sistemas son propios e idénticos |
| **Performance**: tiempos explícitos ("menos de 2 s", "rápidamente") | **Mantenibilidad / flexibilidad**: no se piden cambios ni funcionalidades futuras |
| **Seguridad**: datos sensibles, pagos, identidad, "no permitir accesos" | **Portabilidad**: solo "porque es app móvil" |
| **Disponibilidad / confiabilidad**: sistemas críticos, "no perder datos", banca | **Usabilidad / eficiencia**: casi nunca, salvo un público específico que lo justifique |
| **Elasticidad**: picos ("cuando ocurra un evento particular") | **Soporte**: salvo que haya un sistema de tickets |

## Pregunta e: estilos

- Mínimo 2, cada uno con **la responsabilidad concreta** que cubre ("pub/sub para la subida masiva de noticias").
- **Pub/sub aparece en casi todas las pruebas**, y EDA con workers es la herramienta típica para tareas pesadas.
- Nunca suman: **main y subrutinas** (bloqueante). Casi nunca: **pizarra**, **código móvil** y **máquina virtual**. **Cliente-servidor** solo con una responsabilidad específica.

## Pregunta f: diagrama

- Si no es un diagrama de componentes UML, **no se corrige**. No se deben copiar UMLs genéricos de internet.
- Descuentos típicos: **sin interfaces** (−6); **estilo declarado que no aparece** (−2 a −3 c/u); **falta un requisito funcional** (−1 a −2 c/u); **interfaz mal implementada o al revés** (−1 c/u, máximo −8); **componente desagregado** (−1 c/u); **interfaces importantes sin nombre** (−2).
- Debe mostrar **todas las funcionalidades** del enunciado y los estilos de la pregunta e.

## Pregunta g: falencias

- Se evalúa identificar un **tradeoff real** de la solución y una **solución aplicable**, con su implicancia.
- **No cuentan** las falencias de formato ("me faltó explotar un componente").
- **Plantilla:** "[Componente o decisión] causa [problema]; lo resolvería con [medida], lo que implica [costo]".

> [!tip] Consejos de la ayudantía para la prueba
> - **Ver las pautas**: muestran qué se descuenta y qué se espera.
> - **Estudiar los PPT**: los enunciados reutilizan sus conceptos y ejemplos.
> - Los atributos de calidad se eligen **pensando en los estilos**: hay estilos que priorizan seguridad y otros escalabilidad, y deben ser coherentes entre sí.
> - **Usabilidad y eficiencia casi no se evalúan.**

> [!warning] Errores que más descuentan
> - Atributos sin frase del enunciado que los respalde.
> - Estilos declarados que no aparecen en el diagrama.
> - Diagramas incompletos: una parte muy detallada y otra sin diagramar.
> - Medidas sin ubicación en el sistema o sin justificación.

## Preguntas de repaso

> [!question]- ¿Cómo se reparten típicamente los 4 puntos de una pregunta de medida (a, b, c)?
> 1 punto por nombrar una medida que resuelva el problema, 1 por indicar dónde va en el sistema y 2 por justificarla con el atributo y con el enunciado.

> [!question]- Si una pregunta propone usar caché y no es buena idea, ¿qué hay que responder para obtener el puntaje?
> Decir explícitamente que no es buena opción, justificarlo (por ejemplo, porque cada petición necesita información fresca y distinta) y proponer otra medida justificada (por ejemplo, un broker de mensajería).

> [!question]- ¿Por qué integrabilidad suele ser inválida en la pregunta d?
> Porque solo aplica si el enunciado habla de conectarse con otros sistemas externos o heterogéneos. Si los sistemas son propios e idénticos, o no se mencionan integraciones, no hay justificación.

> [!question]- Nombre tres estilos que casi nunca suman y por qué.
> Main y subrutinas, porque es bloqueante. Pizarra, porque exige un motor con muchas fuentes de conocimiento, algo que rara vez plantea el caso. Código móvil, porque exige traspaso de código entre ambientes, y no vale "porque es app móvil".

> [!question]- Escriba una falencia válida para un diagrama con un único broker central.
> El broker es un punto único de falla: si cae, ningún servicio recibe eventos. Lo resolvería con un cluster de brokers con quorum queues, lo que implica más costo de infraestructura y más complejidad operacional.

> [!question]- ¿Qué descuento tiene un diagrama sin interfaces y qué otro error relacionado se descuenta?
> −6 por no tener interfaces. Además, −1 por cada interfaz mal implementada (al revés o conectores sin interfaz) y −2 si las interfaces importantes no tienen nombre.

> [!question]- V o F: "En la pregunta e conviene listar todos los estilos posibles para asegurar puntaje".
> Falso. Se evalúa la responsabilidad justificada de cada estilo, y cada estilo declarado que no aparece en el diagrama descuenta en la pregunta f. Conviene elegir pocos y coherentes con los atributos.
