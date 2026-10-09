---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[02 - Arquitectura cliente-servidor|Arquitectura cliente-servidor]]"]
---
# Arquitectura en capas

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes", diagrama de herbertograca.com)
> **Qué es:** el sistema se organiza en **capas horizontales** con responsabilidades distintas. Cada capa usa solo a la de abajo. Es la arquitectura clásica de una aplicación monolítica.
>
> ![Slide - arquitectura en capas](adjuntos/Slide%20-%20arquitectura%20en%20capas.png)
>
> | Capa | Contiene | En Rails |
> |---|---|---|
> | User Interface (1.er nivel) | vistas en el navegador, CLI | HTML/ERB en el navegador |
> | Presentation | vistas, view models, controladores de entrada | controladores y vistas |
> | Application | controladores de aplicación, servicios, event listeners | *service objects* |
> | Domain Model | entidades, colecciones, value objects, servicios y eventos de dominio | modelos (lógica de negocio) |
> | Persistence | repositorios, query objects, **ORM** | Active Record |
> | Data (3.er nivel) | servidor de base de datos, búsqueda, APIs de terceros | PostgreSQL |
>
> Al costado está **Infrastructure** (framework, logging), que usan todas las capas.
>
> **Ventajas:**
> - separación de responsabilidades (cada capa es [[03 - Cohesión|cohesiva]]);
> - se puede cambiar una capa (por ejemplo, la base de datos) sin tocar las demás (bajo [[02 - Acoplamiento|acoplamiento]]).
>
> **¿Pero podemos escalar? (slides)** 100 usuarios… okay; 1.000 usuarios… okay; 1.000.000 de usuarios… "mmm, no lo creo". Un monolito en capas se despliega como **un solo bloque**. Ver [[04 - Escalamiento y teorema CAP|Escalamiento]].

## Preguntas de repaso

1. ¿Qué regla de dependencia siguen las capas?
> [!question]- Respuesta
> Cada capa usa (depende de) la capa inmediatamente inferior, no al revés.

2. ¿En qué capa está el ORM?
> [!question]- Respuesta
> En la capa de persistencia (Persistence), junto con los repositorios y los query objects.

3. ¿Qué limitación tiene una arquitectura en capas monolítica para millones de usuarios?
> [!question]- Respuesta
> Se despliega y escala como un solo bloque: para crecer hay que replicar toda la aplicación, aunque solo una parte esté sobrecargada.
