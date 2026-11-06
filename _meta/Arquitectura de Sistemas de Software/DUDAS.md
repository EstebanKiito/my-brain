# Dudas y correcciones de contenido — Arquitectura de Sistemas de Software (IIC2173)

Estados: 🟡 abierta · ✅ resuelta · ℹ️ informativa.

## Integración y relaciones entre contextos

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ informativa | `05 - Ejercicio del context map de un e-commerce.md` | `Clases I2 …html`: *"Checkout → Envío … quizás es más Conformista → Me modifico en base a lo que el sistema de envíos necesita"* (lo mismo para Notificaciones) | Si Checkout es U y se modifica según lo que necesita Envío (D), la relación es **Customer/Supplier**: en Conformist es D quien adopta el modelo de U sin negociar. La slide no da la respuesta ("justifiquen con la pregunta del poder"), así que la nota presenta Customer/Supplier y Conformist como válidas, cada una con su condición. |
| ℹ️ informativa | `05 - Ejercicio del context map de un e-commerce.md` | Slide "El mapa del e-commerce" | La slide solo plantea las siete flechas como ejercicio, sin solución. Las respuestas de Checkout → Inventario, Pagos → Checkout y ERP → Inventario se deducen de la regla del poder y de la pizarra (ACL junto al medio de pago). |

## gRPC GraphQL y MCP

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ resuelta | `01 - gRPC y protobuf para comunicación entre módulos.md` | `Clases I2 …html`: *"No uso protocolos HTTP necesariamente, pueden ser otros protocolos entre computadores"* | La slide de gRPC dice "Sobre HTTP/2; en el navegador vía gRPC-Web o Connect". gRPC usa HTTP/2 como transporte; lo que no hace es usar la semántica REST (recursos y verbos) ni ser web-nativo. La nota sigue a la slide. |

## Asincronía y control de demanda

| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ✅ resuelta | `02 - Asincronía y el modelo de NodeJS.md` | Slide "NodeJS: Arquitectura" (Performance, p. 72): "Pool de threads (libelo)" y "Loop de eventos (libdev)" | Son erratas de **libeio** y **libev**, las librerías originales de Node para el pool de hilos y el loop de eventos, hoy reemplazadas por **libuv**. La transcripción de la imagen no repite los nombres y la nota menciona libuv. |
