---
ramo: "Arquitectura de Sistemas de Software"
tema: "Integración y relaciones entre contextos"
tags:
  - arquisis/integracion
  - origen/complemento
prerrequisitos:
  - "[[02 - Acoplamiento]]"
  - "[[04 - Encapsulamiento]]"
---

# Integrabilidad y el problema de la heterogeneidad

Ningún sistema real vive solo. Una tienda online conversa con un proveedor de pagos, un ERP heredado, un servicio de despachos y su propio catálogo. La **integrabilidad** mide cuánto cuesta hacer que esas piezas trabajen juntas. Es la característica que ordena todo el bloque de integración: context map, middleware, MOM, REST, gRPC y GraphQL son formas distintas de bajar ese costo.

## Por qué integrar: reuso y heterogeneidad

El **reuso de software** busca que una pieza sirva para más de un propósito, siempre con cuidado de no sacarla de su dominio. Krueger (1992) describe el proceso en cuatro pasos: **abstracción**, **selección**, **especialización** e **integración**. Además enumera las formas de reuso, desde lenguajes de alto nivel y copy-paste hasta componentes, esquemas, generadores de aplicaciones, transformaciones y la propia **arquitectura de software**. Integrar es el último paso: una pieza reusable no aporta nada mientras no se conecte con el resto.

La segunda razón es la **heterogeneidad**. Un sistema no puede ser un único bloque para siempre. Con los años aparecen datos en distintos formatos y con distinta semántica, distintos lenguajes y plataformas de hardware y software, y aplicaciones objetivo muy diferentes (ERP, SAP, PDM, SCM, B2B). La heterogeneidad no se elimina: se administra.

El costo es enorme. El mercado de aplicaciones de integración y middleware (AIM) pasó de unos US\$6.400 millones en 2005 a US\$11.000 millones en 2007 y cerca de US\$28.500 millones en 2017. Las pérdidas por mala integración en diseño asistido (CAD) se estimaron en US\$1.000 millones solo en 2002. Una empresa típica usa más de 22 aplicaciones, y las de más de 50.000 empleados pueden pasar de 788. Además, la integración no es solo con sistemas externos: los equipos internos de una misma empresa también tienen que integrarse.

## Definición

> [!tip] Integrabilidad (Bass y Kazman)
> Es el **esfuerzo requerido para integrar una aplicación en un contexto mayor**. No mide si dos sistemas *pueden* conectarse (casi siempre pueden), sino **cuánto cuesta** hacerlo y mantenerlo.

Por eso la integrabilidad es un **requisito estructural**: se decide en la forma interna del sistema (sus interfaces, sus dependencias, sus estándares), no en cómo se comporta en ejecución. Sus objetivos son:
- manejar bien el **acoplamiento** entre piezas;
- potenciar el uso y el reuso del software, con cuidado de no reusar fuera del dominio;
- dar **potencial evolutivo**, porque un sistema fácil de integrar es fácil de partir, reemplazar o extender;
- permitir **estilos más complejos** (servicios, eventos, microservicios), que solo son viables si integrar es barato.

Antes de integrar hay que pensar cómo se va a trabajar y qué hay que modificar para lograrlo, buscando el menor costo posible. Un monolito trabajado por un solo equipo casi no tiene problemas de integración. Cuando la organización se divide en equipos y áreas, cada frontera nueva es un punto de integración que hay que diseñar.

## Cómo se implementa la integrabilidad

El trabajo se ordena en dos verbos:

| Fase | Qué se mira o se hace |
|---|---|
| **Discernir** | **Distancia** entre los elementos que se integran (cuántos intermediarios y contextos hay entre ellos), su **connascence** (qué tienen que acordar para funcionar juntos) y la **capacidad de control** sobre el otro sistema (¿es nuestro? ¿lo podemos cambiar?) |
| **Actuar** | Definir cómo se añaden componentes nuevos, cómo se publican nuevas versiones sin romper a los consumidores y qué **estándares** se observan o adoptan |

En ambas fases se prefiere la alternativa que minimiza costos: líneas de código (LOC), tiempo, recursos y horas-hombre o equivalentes de jornada completa (HH/FTE).

## Niveles comunes de integración

![Dos sistemas en capas integrados a distintos niveles](adjuntos/Niveles%20comunes%20de%20integración.png)

> [!example]- Transcripción de la imagen
> - Dos sistemas, cada uno con las mismas capas apiladas: **Interfaces**, **Proceso**, **Aplicación**, **Datos** y **Red**.
> - Entre ambos, una flecha por nivel indica cómo se integran: integración **"manual"** (personas), **interfaz compartida**, **coordinación** de procesos, **interoperabilidad** de aplicaciones, **datos compartidos** y **conectividad** de red.

Leída de abajo hacia arriba, la figura muestra integraciones cada vez más profundas:
- **Conectividad:** los sistemas solo se alcanzan por la red. Es requisito de todo lo demás.
- **Datos compartidos:** ambos leen y escriben la misma información, por ejemplo una base compartida. Es rápido de lograr, pero acopla mucho.
- **Interoperabilidad:** las aplicaciones se llaman entre sí por APIs o mensajes.
- **Coordinación:** los procesos de negocio de ambos se encadenan (un pedido dispara un despacho).
- **Interfaz compartida:** el usuario ve un solo sistema, aunque por debajo sean dos.
- **Manual:** una persona copia datos de una pantalla a otra. Es el nivel más caro, porque no escala y comete errores.

> [!warning] Modificable no implica integrable
> Las tácticas de integrabilidad se parecen a las de modificabilidad (encapsular, usar intermediarios), pero un sistema muy modificable **no es automáticamente fácil de integrar**. Puede estar muy bien modularizado por dentro y, aun así, no exponer interfaces claras hacia afuera, usar un protocolo propietario o no tener control de versiones. La integrabilidad hay que perseguirla explícitamente.

> [!warning] Más cómputo no es una táctica de integrabilidad
> Si el problema es conectar sistemas heterogéneos, agregar CPU o máquinas no ayuda. Eso es una táctica de performance. Las tácticas de integrabilidad actúan sobre las **dependencias**: encapsular, intermediar, adaptar, estandarizar y coordinar.

## Preguntas de repaso

> [!question]- ¿Por qué la integrabilidad se considera un requisito estructural y no operacional?
> Porque depende de la forma del sistema (interfaces, dependencias, estándares) y se paga en tiempo de desarrollo y mantención, no en tiempo de ejecución. Un sistema puede ser rapidísimo y aun así carísimo de conectar con otro.

> [!question]- La definición de integrabilidad habla de "esfuerzo". ¿Qué diferencia hay con decir "capacidad de integrarse"?
> Casi cualquier par de sistemas se puede integrar con suficiente trabajo, así que la capacidad no distingue nada. El esfuerzo (LOC, tiempo, recursos, HH) sí permite comparar diseños: un sistema integrable es el que se conecta barato y sigue siendo barato cuando el otro lado cambia.

> [!question]- V o F: "Si diseño un sistema altamente modificable, también será fácil de integrar en otro contexto".
> Falso. La modificabilidad mira hacia adentro y la integrabilidad hacia afuera. Un sistema bien modularizado puede no exponer interfaces claras, usar protocolos propietarios o no versionar sus contratos. Las tácticas se parecen, pero la integración hay que diseñarla explícitamente.

> [!question]- Ordene de menor a mayor acoplamiento: integración por datos compartidos, por conectividad y por interoperabilidad de aplicaciones. Justifique.
> Conectividad < interoperabilidad < datos compartidos. La conectividad solo exige alcanzarse por red. La interoperabilidad acopla a un contrato (API o mensaje), pero cada lado mantiene su modelo. Compartir datos acopla al esquema interno: cualquier cambio de tabla rompe al otro sistema.

> [!question]- Una empresa integra a su ERP con un proveedor copiando a mano un Excel diario. ¿En qué nivel de integración está y por qué es un problema?
> Es integración "manual". No escala con el volumen, introduce errores humanos y depende de la disponibilidad de una persona. Lo esperable es subir al menos a interoperabilidad (ingesta automática del archivo o una API).

> [!question]- ¿Qué tres cosas se miran en la fase de "discernir" y para qué sirve cada una?
> La distancia entre los elementos (más intermediarios significa más latencia y más puntos de falla), la connascence (qué deben acordar ambos lados, como nombres, formatos u orden) y la capacidad de control sobre el otro sistema (si se puede cambiar o hay que adaptarse). Con eso se decide si conviene negociar, adaptarse o traducir.

> [!question]- Alternativas: un equipo debe integrar 30 proveedores legados que envían catálogos en CSV, XLSX o JSON, tres veces al día. ¿Qué tácticas mejoran la integrabilidad? I. Exigir a todos un esquema universal. II. Un middleware adaptador por proveedor. III. Un orquestador del proceso de ingesta. IV. Más capacidad de cómputo. a) I y II · b) I, II y IV · c) II y III · d) Todas
> c) II y III. I falla porque no se puede imponer un esquema a proveedores poco sofisticados sobre los que no se tiene control: la adaptación la hace quien integra. II aísla la heterogeneidad de cada formato sin tocar el sistema original. III coordina los pasos (obtener, parsear, validar, transformar, cargar). IV es una táctica de performance, y además el volumen es bajo.
