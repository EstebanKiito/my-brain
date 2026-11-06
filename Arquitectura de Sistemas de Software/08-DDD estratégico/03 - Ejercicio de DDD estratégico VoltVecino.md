---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD estratégico"
tags:
  - arquisis/ddd
  - arquisis/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Bounded context lenguaje ubicuo y context map]]"
---

# Ejercicio de DDD estratégico VoltVecino

Las preguntas de DDD estratégico siguen siempre la misma secuencia: **dominio y subdominios** (con su clasificación y la justificación del core), **bounded contexts** (con términos que cambian de significado), **atributos priorizados** y **un estilo por contexto**. Este ejercicio resuelve un caso completo con esa secuencia.

## El caso

La cooperativa energética Villa Los Aromos agrupa unas **300 viviendas**, muchas con paneles solares que generan excedente. Hoy ese excedente se inyecta a la distribuidora ElecSantiago a un precio muy bajo. La cooperativa decide construir **VoltVecino** para que los vecinos se vendan los excedentes **directamente entre ellos**:
- Cada vivienda tiene un **nodo** (un medidor bidireccional con un mini PC), y todos ejecutan el mismo software.
- La energía se transa en **bloques de 15 minutos**: los nodos publican ofertas y demandas y negocian en una **subasta**, **sin servidor central**. Los acuerdos quedan en un **registro de transacciones replicado** en todos los nodos.
- Por regulación, se envía a ElecSantiago un **reporte diario**. Su API es antiquísima: identifica cada vivienda por un ID, trabaja en Wh, usa su propio formato de fechas y **no se modificará**.
- A fin de mes se **liquida**: se compensan compras y ventas, se aplica la comisión y se genera un cobro o abono a través de una **pasarela de pagos** externa.
- Un servicio de **pronóstico** consulta la API meteorológica para sugerir cuánto ofertar.
- Los vecinos usan una **app** (con un proveedor de identidad externo) y la directiva usa un **panel** para gestionar vecinos y **disputas**, que se resuelven revisando el registro.
- Se proyecta crecer de 300 a **5.000 viviendas** en tres años, con un **equipo de desarrollo pequeño**.

## 1. Dominio y subdominios

**Dominio:** comercialización comunitaria de energía (un mercado local).

| Subdominio | Tipo | Justificación |
|---|---|---|
| **Intercambio de energía** (ofertas, demandas, subasta, registro) | **Core** | Es la razón de existir del sistema: vender excedentes entre vecinos en vez de a la distribuidora |
| Liquidación mensual | Support | Necesario para el negocio, pero sigue al intercambio |
| Reportes regulatorios | Support | Obligación legal propia del contexto |
| Pronóstico de generación | Support | Mejora las ofertas del core |
| Gestión de vecinos | Support | Altas, bajas, viviendas y nodos |
| Gestión de disputas | Support | Reclamos resueltos con el registro |
| Pagos | Genérico | Pasarela externa |
| Identidad (auth) | Genérico | Proveedor de identidad externo |
| Datos meteorológicos | Genérico | API externa |

## 2. Bounded contexts y términos

| Bounded context | Cubre | Términos propios |
|---|---|---|
| **Mercado** | Intercambio de energía | Oferta, demanda, subasta, transacción |
| **Pronóstico** | Pronóstico de generación | Estimación, sugerencia de oferta |
| **Liquidación** | Liquidación mensual | Período, cargo, abono, comisión |
| **Vecinos** | Gestión de vecinos | Vecino, vivienda, preferencias |
| **Disputas** | Gestión de disputas | Reclamo, evidencia, resolución |
| **Reportes** | Reporte regulatorio | Reporte diario, suministro |

**Términos que cambian de significado:**
- **Energía:** en Mercado son **kWh por bloque de 15 minutos**; en Reportes, **Wh diarios por suministro**, en el formato de la distribuidora.
- **Vecino o participante:** en Mercado es **una vivienda o un nodo**; en Reportes, **el identificador de un suministro** de ElecSantiago.

La relación con ElecSantiago es un caso claro para una **capa anticorrupción** en el contexto Reportes: la distribuidora no cambiará su API, y sus Wh, IDs y fechas no deben contaminar el modelo del Mercado.

## 3. Características arquitectónicas priorizadas

1. **Disponibilidad:** sin servidor central, el mercado no puede depender de un punto único de falla.
2. **Confiabilidad:** el registro replicado debe ser consistente entre los nodos, porque es la evidencia en las disputas.
3. **Escalabilidad:** de 300 a 5.000 viviendas en tres años.
4. **Seguridad:** pagos, identidad de los vecinos y un registro que sirve como evidencia.

También son defendibles la **integrabilidad** (ElecSantiago, pagos, meteorología, identidad) y la **mantenibilidad** (el equipo es pequeño).

## 4. Un estilo por contexto

| Contexto | Estilo | Por qué | Atributo |
|---|---|---|---|
| Mercado | **P2P** | Nodos idénticos que se comunican todos con todos, sin servidor central | Disponibilidad, tolerancia a caídas, escalabilidad |
| Liquidación | **Por lotes, secuencial** | Consolidación mensual de cobros y abonos | Confiabilidad |
| Reportes regulatorios | **Por lotes, secuencial** | Envío diario a ElecSantiago | Confiabilidad, integrabilidad |
| Vecinos, disputas, app y panel | **Cliente-servidor** | CRUD e interacción con usuarios | Usabilidad, mantenibilidad |
| Notificar transacciones entre nodos | **Pub/sub** | Avisar a los interesados sin acoplar a los nodos | Escalabilidad |

> [!tip] Checklist para el diagrama UML de la pregunta siguiente
> - El diagrama debe mostrar **todas** las funcionalidades del enunciado.
> - Los estilos deben ser **coherentes con los atributos priorizados**, y hay que explicar qué responsabilidad cubre cada uno.
> - Hay que **nombrar las interfaces** y **conectar todos los componentes**: un componente suelto sin justificación descuenta.

## Preguntas de repaso

> [!question]- ¿Por qué el intercambio de energía es el core y no la liquidación?
> Porque el valor de VoltVecino es que los vecinos vendan excedentes entre ellos a mejor precio, y eso ocurre en el intercambio (ofertas, subasta, registro). La liquidación es necesaria, pero es una consecuencia del intercambio y no lo que diferencia al sistema.

> [!question]- ¿Por qué pagos, identidad y datos meteorológicos son genéricos?
> Porque se resuelven con servicios externos ya existentes (una pasarela, un proveedor de identidad, una API meteorológica). Desarrollarlos no aporta diferenciación.

> [!question]- Explique cómo cambia el significado de "energía" entre Mercado y Reportes y qué patrón de integración sugiere.
> En Mercado son kWh por bloque de 15 minutos; en Reportes, Wh diarios por suministro, en el formato de ElecSantiago. Como la distribuidora no adaptará su API, conviene una capa anticorrupción en Reportes que traduzca el modelo propio al de ElecSantiago.

> [!question]- ¿Por qué P2P para el contexto Mercado?
> Porque todos los nodos ejecutan el mismo software, negocian entre sí y no hay servidor central por diseño. P2P da disponibilidad (no hay punto único de falla) y escalabilidad (cada vivienda nueva agrega un nodo), a cambio de complejidad en la consistencia del registro.

> [!question]- ¿Por qué Liquidación y Reportes usan un estilo por lotes secuencial?
> Porque son procesos periódicos (mensual y diario) que transforman todo el conjunto de transacciones en un resultado (cobros y abonos, o el reporte), paso a paso y sin necesidad de respuesta en tiempo real.

> [!question]- Nombre dos atributos que se podrían agregar a la lista priorizada y su justificación.
> Integrabilidad, porque hay que conectarse con ElecSantiago, la pasarela de pagos, la API meteorológica y el proveedor de identidad. Mantenibilidad, porque el equipo es pequeño y tiene que poder sostener el sistema.

> [!question]- En el caso del supermercado sin cajeros, ¿qué bounded contexts propone la ayudantía?
> Control de acceso (torniquete y app: reconocimiento facial, enrolamiento, usuario como perfil), seguimiento automatizado de compras (cámaras, RecognitionAI, carrito, producto visto físicamente) y pagos (cobro automatizado con PayPal). El core es el sistema automatizado de compras.
