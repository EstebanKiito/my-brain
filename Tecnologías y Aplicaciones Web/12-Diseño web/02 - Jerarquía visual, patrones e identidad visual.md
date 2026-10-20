---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Diseño web"
tags:
  - web
  - diseno
  - ui
  - origen/complemento
prerrequisitos:
  - "[[01 - Diseño web, UI y UX]]"
---

# Jerarquía visual, patrones e identidad visual

Un usuario no lee una página: la **escanea**. En segundos decide qué es lo importante y dónde hacer click. Tres herramientas hacen que ese escaneo funcione a favor del diseño: la **jerarquía visual**, que ordena qué se ve primero; los **patrones de diseño**, que reutilizan soluciones que el usuario ya conoce; y la **identidad visual**, que hace reconocible al producto.

## Jerarquía visual

La **jerarquía visual** es el principio de organizar los elementos según cómo las personas procesan la información en una página. Es un sistema para **priorizar** elementos de modo que se entiendan fácilmente. Algunas herramientas:

- **Tamaño**: lo más grande atrae la atención primero; se usa para aumentar o reducir la visibilidad de un elemento.
- **Color y contraste**: dirigen la mirada; un elemento de color fuerte sobre un fondo neutro destaca de inmediato.
- **Tipografía y estilos**: elegidos con cuidado, distinguen títulos, texto y acciones.
- **Espacio**: el espacio en blanco da balance, flujo y foco al layout; agrupa lo relacionado y separa lo distinto.
- **Composición**: le da una estructura al diseño, como una grilla o una diagonal que guía la lectura.

Un ejemplo es la portada del libro *Three Armies on the Somme*: una franja roja diagonal sobre un fondo gris resalta tres cascos, y el título y el autor siguen la misma diagonal, guiando la mirada de arriba hacia abajo.

> [!tip] La prueba del entrecerrar los ojos
> Al mirar una pantalla con los ojos entrecerrados, los detalles desaparecen y solo quedan las masas de tamaño y contraste. Si lo que se distingue primero no es lo más importante, la jerarquía está mal.

## Patrones de diseño

Los **patrones de diseño** de interfaces son **soluciones recurrentes a problemas de diseño comunes**. Funcionan como un **lenguaje común** entre diseñadores y, sobre todo, entre el diseño y los usuarios: si algo se resuelve siempre de la misma forma, el usuario no tiene que aprenderlo de nuevo.

- Para eliminar rápido un archivo del escritorio existen dos patrones de los años 70 que hoy todos reconocen: **arrastrar y soltar** (*drag and drop*) a la papelera, y los **atajos de teclado**.
- Para indicar qué tan segura es una contraseña mientras se escribe, el patrón es un **medidor de seguridad**:

![Patrón de medidor de seguridad de contraseñas](adjuntos/Patr%C3%B3n%20de%20medidor%20de%20seguridad%20de%20contrase%C3%B1as.png)

> [!example]- Transcripción de la imagen
> Cinco campos de contraseña, cada vez con más caracteres. Bajo cada uno, una barra de cuatro segmentos se llena y cambia de color: *Very weak* (vacía), *Weak* (un segmento rojo), *So-so* (dos naranjos), *Good* (tres verdes claros) y *Great!* (cuatro verdes).

> [!warning] No reinventar lo que el usuario ya sabe
> Un ícono de lupa que no busca, o un logo que no lleva al inicio, rompe expectativas aprendidas en miles de sitios. Innovar en un patrón conocido tiene un costo: el usuario tiene que aprender algo nuevo.

## Identidad visual

La **identidad visual** es la combinación de elementos gráficos que representan e identifican una marca. Le da reconocimiento y la diferencia de otras. Incluye la **paleta de colores**, la **tipografía**, los gráficos y los logos. Para que todos la apliquen igual, se suele documentar en un **manual de marca**, con las reglas de uso de cada elemento.

En la web, la identidad visual se traduce en decisiones concretas de CSS (variables de color, fuentes, espaciados), y en equipos grandes se formaliza en un **design system**.

## Preguntas de repaso

> [!question]- ¿Qué herramientas de jerarquía visual se pueden usar para destacar el botón principal de un formulario?
> Hacerlo más grande, darle un color de alto contraste distinto de los demás botones, rodearlo de espacio y ubicarlo donde termina la lectura del formulario.

> [!question]- ¿Por qué los patrones de diseño mejoran la usabilidad?
> Porque el usuario ya los conoce de otros sitios: reconoce la solución sin tener que aprenderla. Eso reduce el esfuerzo y los errores.

> [!question]- ¿Para qué sirve un manual de marca?
> Para que todos los que diseñan o programan apliquen la identidad igual (colores, tipografías, uso del logo), de modo que el producto se vea coherente y reconocible en todas sus pantallas.
