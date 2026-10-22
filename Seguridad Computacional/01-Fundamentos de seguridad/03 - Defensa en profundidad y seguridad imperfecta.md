---
ramo: "Seguridad Computacional"
tema: "Fundamentos de seguridad"
tags:
  - seguridad/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[02 - Qué sale mal: política, modelo de amenaza y bugs]]"
---

# Defensa en profundidad y seguridad imperfecta

No existe la seguridad perfecta, y el defensor parte en desventaja: tiene recursos limitados, debe equilibrar seguridad y conveniencia, y si imagina 25 ataques, el atacante busca el 26. Esta nota resume cómo se juega igual con esas reglas.

## Defensa en profundidad
Se ponen defensas en cada capa y **nunca se asume que una funcionará**: firewall, y además contraseñas, y además un segundo factor. Si el atacante rompe un paso, aún le queda el siguiente; cada capa encarece el ataque. Sirve también para compensar un modelo de amenaza equivocado (por ejemplo, auditar todo por si las suposiciones fallan).

> [!tip] Regla
> Hacer que el costo del ataque supere el valor de lo protegido, o que el sistema sea menos atractivo que el de otros. Atacar a un país no es lo mismo que atacar a un negocio pequeño.

## Cómo mejorar un modelo de amenaza
- Hacerlo más explícito, para ver las debilidades.
- Hacerlo más simple y general: por ejemplo, no suponer que el diseño es secreto.
- Rediseñar para depender de menos suposiciones (autenticación resistente a phishing, no confiar en cientos de CAs).

## Un proceso iterativo
Diseñar, observar ataques y actualizar la comprensión de amenazas. Ayudan: usar componentes bien entendidos, los análisis *post mortem*, las bases públicas de vulnerabilidades (CVE), los programas de recompensas por reportes y un plan de recuperación (copias seguras). Los modelos de amenaza cambian con el tiempo (el phishing con IA es más fácil). Se buscan técnicas que cortan clases enteras de ataques, no solo parchar agujeros.

## Preguntas de repaso

> [!question]- ¿Por qué no basta con una defensa muy fuerte en una sola capa?
> Porque si esa capa falla, o su modelo de amenaza era erróneo, no queda nada. Varias capas con supuestos distintos hacen que un solo error no sea fatal.

> [!question]- Si la seguridad perfecta no existe, ¿qué se busca entonces?
> Que el ataque cueste más que lo que se gana con él, o que el sistema sea menos atractivo que otros, y limitar el daño con recuperación.

> [!question]- ¿Por qué es mala base de seguridad asumir que el diseño es secreto?
> Porque si se filtra (o alguien lo deduce), la seguridad cae por completo y es difícil de recuperar; es una suposición frágil.
