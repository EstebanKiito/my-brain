---
ramo: Ingeniería de Software
tema: Principios de diseño
tags: [ingsoft/diseno, origen/apuntes]
prerrequisitos: ["[[11 - Polimorfismo y duck typing|Polimorfismo y duck typing]]"]
---
# Buen diseño de software

Un buen diseño orientado a objetos es el que hace que el código sea **fácil de entender, cambiar, probar y extender**. En el curso se evalúa con unas pocas heurísticas: sin código duplicado, bajo acoplamiento y alta cohesión.

## Diseño
- Un buen diseño es **fácil de entender, modificar, testear y extender**.
- Se puede **reutilizar**.
- **Fácil de implementar**.

## Heurística usada
- Evitar **código duplicado** (code clones) → [[05 - Código duplicado (code clones)|Código duplicado]]
- Minimizar las **dependencias entre clases** (acoplamiento) → [[02 - Acoplamiento|Acoplamiento]]
- **Principio de Simple Responsabilidad** (cohesión) → [[03 - Cohesión|Cohesión]]
- Facilitar el **mantenimiento y la extensibilidad**.
- Organizando el código **para el cambio**.
- **Aislando** para el cambio.

> [!tip] Complemento — Clean Code (slides "Diseño Orientado al Objeto")
> *"I like my code to be elegant and efficient. The logic should be straightforward to make it hard for bugs to hide, the dependencies minimal to ease maintenance, error handling complete according to an articulated strategy, and performance close to optimal so as not to tempt people to make the code messy with unprincipled optimizations. Clean code does one thing well."* (Bjarne Stroustrup, creador de C++)
>
> Las ideas clave de la cita son:
> - elegante y eficiente;
> - la lógica debe ser directa para que sea difícil que se escondan bugs;
> - dependencias mínimas para facilitar el mantenimiento;
> - manejo de errores completo según una estrategia;
> - rendimiento cercano al óptimo.

> [!tip] Complemento — ¿qué hace a un código extensible? (slides)
> - Piensa en un *add-on* de Chrome: no hay que recompilar Chrome, ni modificarlo, ni siquiera reiniciarlo para que funcione.
> - Un programa es **extensible** si se le pueden **agregar funcionalidades sin modificar el código actual** → [[06 - Principio abierto-cerrado|principio abierto/cerrado]].
> - En POO, los mecanismos que favorecen la extensión son la **herencia** y el **polimorfismo**.
>
> **Resumen de propiedades deseadas:** bajo acoplamiento, alta cohesión, sin código duplicado y favorecer el cambio y la extensibilidad. Para eso se usan los conceptos básicos de POO: [[04 - Encapsulamiento|encapsulamiento]], delegación, herencia y polimorfismo.
>
> Los tres ejemplos de la clase aplican estas ideas: [[07 - Ejemplo de diseño - Carrito de compras|carrito de compras]], [[08 - Ejemplo de diseño - Filtros de libros|filtros de libros]] y [[09 - Ejemplo de diseño - Bebidas con cafeína|bebidas con cafeína]].

## Preguntas de repaso

1. ¿Qué características tiene un buen diseño?
> [!question]- Respuesta
> Es fácil de entender, modificar, testear, extender, reutilizar e implementar.

2. ¿Qué heurísticas se usan en el curso para evaluar un diseño?
> [!question]- Respuesta
> Evitar código duplicado, minimizar las dependencias entre clases (bajo acoplamiento), aplicar responsabilidad única (alta cohesión), facilitar el mantenimiento y la extensibilidad, y organizar y aislar el código para el cambio.

3. ¿Qué significa que un programa sea extensible?
> [!question]- Respuesta
> Que se le pueden agregar funcionalidades nuevas sin modificar el código existente, como un add-on de Chrome.
