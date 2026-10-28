---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Sistemas operativos"
tags:
  - algoritmos/sistemas-operativos
  - algoritmos/arquitectura
  - origen/complemento
prerrequisitos:
  - "[[05 - El computador básico y su set de instrucciones|El computador básico y su set de instrucciones]]"
---

# El sistema operativo como intermediario

Ya tenemos el hardware y un set de instrucciones. Para ejecutar un programa hay que usar la CPU, la memoria y los dispositivos de entrada/salida, pero escribir esas operaciones en cada programa sería inviable. El **sistema operativo** (SO) es el programa que se encarga de esos servicios comunes y permite que las aplicaciones se ejecuten.

## El problema

Sin sistema operativo, cada programa tendría que saber cómo leer el teclado, mover el mouse, dibujar en pantalla, decidir en qué posición de memoria escribir y leer archivos del disco. Muchos programas necesitan exactamente los mismos servicios, así que repetir esa lógica en cada uno sería un desperdicio y una fuente de errores.

La solución es un programa "maestro" que se ejecuta permanentemente y ofrece esos servicios a los demás.

> [!tip] Definición
> Un **sistema operativo** es el programa que permite ejecutar programas (**procesos**) sobre la CPU, administrar la memoria entre ellos y gestionar los dispositivos de entrada/salida.

## Qué administra

| Recurso | Qué hace el SO |
|---|---|
| **CPU** | Decide qué proceso se ejecuta en cada momento |
| **Memoria** | Reparte la memoria disponible entre los procesos |
| **Entrada/salida** | Coordina el uso de teclado, pantalla, disco y otros dispositivos |

También ofrece una **interfaz de usuario** (*shell*): la capa que permite dar órdenes al computador, ya sea con comandos o con una interfaz gráfica como GNOME o Xfce.

## Modo usuario y modo kernel

El procesador distingue dos niveles de privilegio:

- **Modo usuario:** donde corren las aplicaciones. No pueden acceder directamente al hardware ni a ciertas instrucciones.
- **Modo kernel:** donde corre el núcleo del sistema operativo. Tiene acceso total al hardware.

Para pedir un servicio, una aplicación hace una **llamada al sistema** (*system call*). La llamada cruza la frontera entre ambos modos, el kernel ejecuta la operación y devuelve el resultado.

![Llamada al sistema: la aplicación pide open() y el kernel ejecuta la implementación](adjuntos/Llamada%20al%20sistema.png)

> [!example]- Transcripción de la imagen
> - Arriba, la `user application` en modo usuario.
> - La aplicación llama a `open()`, que pasa por la `system call interface`.
> - La interfaz cruza al modo kernel y ejecuta la implementación de `open()`.
> - Al terminar, el resultado vuelve a la aplicación con `return`.

> [!warning] El SO no es la interfaz gráfica
> GNOME, Xfce o la terminal son programas que se comunican con el SO, pero no son el SO. El núcleo es la parte que administra los recursos; la interfaz es la cara visible.

## Preguntas de repaso

> [!question]- ¿Por qué no basta con el hardware y el set de instrucciones para ejecutar programas?
> Porque los programas necesitan servicios comunes (teclado, pantalla, memoria, disco) que alguien debe administrar. Sin SO, cada programa tendría que implementarlos.

> [!question]- ¿Qué tres recursos administra principalmente un sistema operativo?
> La CPU, la memoria y los dispositivos de entrada/salida.

> [!question]- ¿Qué es una llamada al sistema?
> El mecanismo por el cual una aplicación en modo usuario pide un servicio al kernel, como abrir un archivo o escribir en pantalla.

> [!question]- ¿Cuál es la diferencia entre modo usuario y modo kernel?
> En modo usuario las aplicaciones tienen acceso restringido al hardware; en modo kernel el sistema operativo tiene acceso total para administrar los recursos.
