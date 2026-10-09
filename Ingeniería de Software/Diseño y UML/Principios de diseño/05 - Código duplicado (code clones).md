---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[01 - Buen diseño de software|Buen diseño de software]]"]
---
# Código duplicado (code clones)

Los *code clones* son **fragmentos de código repetidos** en varios lugares. Hacen el programa más difícil de mantener, porque cada cambio hay que repetirlo en todas las copias.

## Mis apuntes
- Heurística: **evitar código duplicado** (code clones).
- Ejemplo 2: `BookStore` repite código en los métodos `filterByTitle` y `filterByAuthor`; si se quiere añadir otro filtro, habría **más código duplicado** → ver [[08 - Ejemplo de diseño - Filtros de libros|Filtros de libros]].
- Ejemplo 3: **código duplicado entre clases** (`Tea` y `Coffee`); otra clase tendría mucho más código duplicado → ver [[09 - Ejemplo de diseño - Bebidas con cafeína|Bebidas con cafeína]].

> [!tip] Complemento (slides "Diseño Orientado al Objeto")
> - **Hipótesis:** un programa es más difícil de mantener si tiene varios clones.
> - **¿Por qué?** Si se necesita modificar un clon, hay que hacer la misma modificación en los demás.
> - Se encontraron muchos casos en que quien modificó un clon **no sabía que existían otros**, y eso causó bugs.
> - **Cómo eliminarlos:**
>   - **dentro de una clase:** extraer un método común parametrizado, o una estrategia (Strategy);
>   - **entre clases:** subir lo común a una superclase, una clase abstracta (Template Method) o un módulo.
> - Principio relacionado: **DRY** (*Don't Repeat Yourself*).

## Preguntas de repaso

1. ¿Por qué el código duplicado dificulta el mantenimiento?
> [!question]- Respuesta
> Porque cada cambio debe replicarse en todos los clones. Si se olvida alguno, aparecen bugs e inconsistencias.

2. ¿Cómo se elimina código duplicado entre dos clases parecidas?
> [!question]- Respuesta
> Subiendo lo común a una clase padre (posiblemente abstracta) y dejando en las hijas solo lo que varía (override), como en el ejemplo de las bebidas.

3. ¿Qué significa DRY?
> [!question]- Respuesta
> Don't Repeat Yourself: cada conocimiento o lógica debe tener una sola representación en el código.
