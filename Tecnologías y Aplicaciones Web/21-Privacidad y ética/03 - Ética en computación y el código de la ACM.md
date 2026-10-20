---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Privacidad y ética"
tags:
  - web
  - etica
  - origen/complemento
prerrequisitos:
  - "[[01 - Calidad de software y QA]]"
  - "[[02 - GDPR, CCPA y la ley chilena de datos]]"
---

# Ética en computación y el código de la ACM

Quien desarrolla código debe ser consciente de que lo que construye tiene un impacto en otras personas y en el entorno. El software no existe en el vacío: influye en su contexto, y hay deberes legales, éticos y morales en juego. Esta nota presenta un estándar de referencia, el código de ética de la ACM, y casos reales que muestran por qué importa.

## El código de ética de la ACM

El ***ACM Code of Ethics and Professional Conduct*** fue adoptado por la ACM (*Association for Computing Machinery*) y por la IEEE Computer Society, y es un estándar para enseñar y practicar la ingeniería de software. Sus siete principios generales dicen que un profesional de la computación debería:

| Principio | En una frase |
|---|---|
| 1. Contribuir a la sociedad y al bienestar humano | Usar la tecnología para hacer del mundo un lugar mejor para todos |
| 2. Evitar el daño | Primero, no hacer daño; si ocurre, repararlo |
| 3. Ser honesto y confiable | Decir la verdad sobre lo que la tecnología puede y no puede hacer |
| 4. Ser justo y no discriminar | Construir tecnología que incluya a todos por igual |
| 5. Respetar el trabajo intelectual | Dar crédito donde corresponde y respetar el trabajo de otros |
| 6. Respetar la privacidad | Proteger los datos personales como si fueran propios |
| 7. Honrar la confidencialidad | Guardar los secretos confiados, salvo que la ley o la ética lo impidan |

## Bugs con consecuencias

| Caso | Qué pasó | Costo |
|---|---|---|
| **Ariane 5** (1996) | A los 37 segundos del primer lanzamiento, el cohete giró 90 grados y se autodestruyó. El sistema de referencia inercial convirtió un número de punto flotante de 64 bits a un entero de 16 bits, y el valor no cabía | Cerca de 370 millones de dólares |
| **CrowdStrike** (2024) | Una actualización del software de seguridad Falcon traía un archivo de configuración con datos malformados; el driver del kernel accedió a memoria inválida y millones de equipos Windows mostraron la pantalla azul | Más de 10 mil millones de dólares, con vuelos cancelados y bancos y hospitales interrumpidos |
| **AWS us-east-1** (octubre de 2025) | Una condición de carrera en la gestión del DNS de DynamoDB hizo que un registro antiguo sobrescribiera el activo y dejó el endpoint regional sin IPs; la falla se propagó en cascada a otros servicios | Muchísimos servicios de internet caídos |

Ninguno de estos casos fue malicioso. Fueron errores en sistemas de los que dependía mucha gente, y ahí está la responsabilidad: la calidad y las pruebas son también una cuestión ética.

## Tecnología que influye en las personas

- **Desinformación**: en la guerra entre Ucrania y Rusia circularon *deepfakes* (videos y audios generados artificialmente) que pasan por reales ante quien no sabe que no lo son.
- **Redes sociales**: los algoritmos de recomendación optimizan el tiempo en la plataforma, no el bienestar del usuario. Usan refuerzo intermitente (como las tragamonedas), crean *echo chambers* que polarizan y priorizan contenido que genera enojo o miedo porque produce más *engagement*.
  - El experimento emocional de Facebook (2014) manipuló el feed de casi 700 mil usuarios sin su consentimiento explícito.
  - Cambridge Analytica (2018) usó datos de 87 millones de usuarios de Facebook para influir en elecciones.
  - Estudios internos de Meta (2021) mostraron que Instagram empeora la imagen corporal de adolescentes.

> [!warning] Las métricas de negocio pueden ir contra los usuarios
> Optimizar tiempo en pantalla, clicks o compartidos puede entrar en conflicto directo con el bienestar de las personas, sobre todo de jóvenes y poblaciones vulnerables. Quien implementa esas métricas participa de esa decisión.

Preguntas abiertas que plantea el caso de las redes sociales: ¿deben las plataformas filtrar lo que se publica, y depende de si son un monopolio? ¿Quién es dueño de los datos de los usuarios? ¿Cuál es la responsabilidad de una empresa por cómo otros usan su producto? Para seguir pensando en esto están los documentales *The Great Hack*, *Coded Bias* y *The Social Dilemma*.

## Preguntas de repaso

> [!question]- ¿Qué principio del código de la ACM se pone en juego al exagerar lo que puede hacer un producto?
> Ser honesto y confiable: decir la verdad sobre lo que la tecnología puede y no puede hacer.

> [!question]- ¿Por qué un bug como el de CrowdStrike es también un problema ético y no solo técnico?
> Porque afectó a personas que dependían del sistema (vuelos, hospitales, bancos). Probar y desplegar con cuidado software del que depende mucha gente es parte de la responsabilidad de evitar el daño.

> [!question]- ¿Cómo puede un algoritmo de recomendación perjudicar a sus usuarios sin que nadie lo haya programado con esa intención?
> Al optimizar una métrica de negocio, como el tiempo en pantalla, aprende a priorizar contenido adictivo o que provoca emociones fuertes, aunque eso vaya contra el bienestar de quienes lo usan.
