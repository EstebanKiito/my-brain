---
ramo: Ingeniería de Software
tema: Historias de usuario
tags: [ingsoft/requisitos, origen/complemento]
prerrequisitos: ["[[06 - Épicas, temas e historias|Épicas, temas e historias]]", "[[04 - Criterio INVEST|Criterio INVEST]]"]
---
# Cómo dividir historias de usuario

> [!tip] Complemento — nota nueva (fuente: slides "Historias de Usuario")
> **Qué es:** cuando una historia es demasiado grande (una épica, o que no cumple la S de INVEST), se divide en historias más pequeñas. **Regla clave:** al dividir, deben seguir siendo **historias de usuario** (con valor para alguien) y **no tareas**.
>
> | Estrategia | Historia grande | Se divide en… |
> |---|---|---|
> | **Por operación (CRUD)** | As an online seller I can manage my product online so I can keep my product up to date for customers | …**add** new products so that customers have purchase options · …**update** existing products so I can adjust for changes in pricing · …**delete** products so I can remove products that I don't sell anymore |
> | **Por pasos del flujo (workflow)** | As a customer I can pay for the goods in my shopping cart so I can get the product delivered at home | …**log into my account** so I don't have to enter my shipping information every time · …**confirm my order** so I can correct mistakes before I make the payment |
> | **Por criterio de aceptación** | As an online buyer I can use my reward points so I can redeem those points while shopping | …**see my reward points** in my account so I know whether I have points that I can redeem · …**select the number of points** to use so I can redeem only the points I need |
> | **Por happy / unhappy path** | As an online buyer I can log into my account so I can access secured billing information | **(happy)** …log into my account so I can access my secured billing information · **(unhappy)** …reset my password when my login fails so I can log back in again · **(unhappy)** as an online seller I can block users after 3 failed attempts so I can protect the site against hackers |
> | **Por roles** | As a restaurant owner I can make reservations so I can provide timely service to the customer | …make reservations **for members**… · …make reservations **for guests** so I can provide timely service |

> [!example] Ejemplo extra — dividir mal vs. bien
> Historia: *"Como alumno necesito inscribir mis cursos para armar mi semestre"*.
> - ❌ **Tareas, no historias:** "crear tabla de cursos", "hacer endpoint de inscripción", "diseñar la vista".
> - ✅ **Historias:** por flujo, "buscar un curso por sigla", "inscribir una sección" y "ver mi horario resultante"; por unhappy path, "ser avisado si hay tope de horario".

## Preguntas de repaso

1. Nombra las 5 estrategias de división de las slides.
> [!question]- Respuesta
> Por operación (agregar, actualizar, eliminar), por pasos del flujo (workflow), por criterio de aceptación, por happy / unhappy path y por roles.

2. ¿Qué regla hay que respetar al dividir una historia?
> [!question]- Respuesta
> Cada parte debe seguir siendo una historia de usuario que aporta valor a alguien, no una tarea técnica.

3. Divide por happy / unhappy path la historia "Como comprador puedo pagar con tarjeta para completar mi compra".
> [!question]- Respuesta
> **Happy:** como comprador puedo pagar con una tarjeta válida para completar mi compra. **Unhappy:** como comprador puedo reintentar el pago cuando mi tarjeta es rechazada para no perder mi carrito; como comprador soy avisado si mi tarjeta está vencida para usar otro medio de pago.
