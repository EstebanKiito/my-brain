---
ramo: "Programación en C"
tema: "Módulos, compilación y depuración"
tags:
  - c
  - make
  - makefile
  - compilacion
  - origen/complemento
prerrequisitos:
  - "[[02 - Compilación separada, enlazado y pragma once]]"
---

# Make y Makefile

**Make** automatiza la [[02 - Compilación separada, enlazado y pragma once|compilación separada]]: sabe qué archivo depende de cuál y, después de un cambio, **recompila solo lo necesario**. Las dependencias se escriben como **reglas** en un archivo llamado `Makefile`.

## Anatomía de una regla

```make
objetivo: dependencia_1 dependencia_2 ... dependencia_n
	comando                # la línea del comando empieza con TAB, no con espacios
```

Al invocar una regla, Make ejecuta su comando **solo si alguna dependencia "se cumple"**:

- Si la dependencia es **otra regla**, la invoca primero. Si esa regla ejecutó su comando, cuenta como cumplida.
- Si la dependencia es un **archivo**, se cumple cuando fue **modificado después** de la última vez que se generó el objetivo.

En otras palabras: un `.o` se recompila solo cuando cambió alguno de los archivos de los que depende.

## Las reglas del ejemplo de reptiles

El `.o` de un módulo depende de su `.c`, de su `.h` y de **todos los headers que incluye**:

![Regla de reptil.o](adjuntos/Make%20-%20regla%20de%20reptil.o.png)

> [!example]- Transcripción de la imagen
> "Compilación". En el diagrama de archivos, `reptil.h` y `reptil.c` están resaltados en rojo. Abajo, la regla `reptil.o: reptil.c reptil.h` con el comando `gcc reptil.c -c -o reptil.o`.

![Regla de frog.o](adjuntos/Make%20-%20regla%20de%20frog.o.png)

> [!example]- Transcripción de la imagen
> `reptil.h` y `reptil.c` ya tienen un check. Ahora están resaltados `frog.h`, `frog.c` y `reptil.h`, porque `frog.h` incluye `reptil.h`. Regla: `frog.o: frog.c frog.h reptil.h`, con el comando `gcc frog.c -c -o frog.o`.

![Regla de main.o](adjuntos/Make%20-%20regla%20de%20main.o.png)

> [!example]- Transcripción de la imagen
> Todos los headers de animales y `reptil.h` tienen check; `main.c` está resaltado con flechas rojas desde `frog.h`, `snake.h` y `turtle.h`. Regla: `main.o: main.c frog.h snake.h turtle.h reptil.h`, con el comando `gcc main.c -c -o main.o`.

![Makefile completo](adjuntos/Makefile%20completo%20del%20ejemplo%20de%20reptiles.png)

> [!example]- Transcripción de la imagen
> Archivo `Makefile`. `main: main.o reptil.o frog.o snake.o turtle.o` con `gcc main.o reptil.o frog.o snake.o turtle.o -o main`. `main.o: main.c frog.h snake.h turtle.h reptil.h` con `gcc main.c -c -o main.o`. `reptil.o: reptil.c reptil.h` con `gcc reptil.c -c -o reptil.o`. `frog.o: frog.c frog.h reptil.h`, `snake.o: snake.c snake.h reptil.h` y `turtle.o: turtle.c turtle.h reptil.h`, cada una con su `gcc … -c -o …`.

La **regla final** (`main`) depende de todos los `.o`: se ejecuta, es decir, se vuelve a enlazar, si hubo que recompilar cualquiera de ellos. Por ejemplo, si cambia `frog.c`, Make recompila solo `frog.o` y reenlaza `main`. Si cambia `reptil.h`, recompila los cinco `.o`, porque todos dependen de él.

## Un proyecto completo, verificado

```make
main: main.o contador.o reporte.o
	gcc main.o contador.o reporte.o -o main

main.o: main.c contador.h reporte.h
	gcc -Wall -Wextra -c main.c -o main.o

contador.o: contador.c contador.h
	gcc -Wall -Wextra -c contador.c -o contador.o

reporte.o: reporte.c reporte.h contador.h
	gcc -Wall -Wextra -c reporte.c -o reporte.o

clean:
	rm -f *.o main
```

```bash
make                # primera vez: compila los 3 .o y enlaza
touch reporte.c     # simula un cambio en reporte.c
make                # recompila SOLO reporte.o y reenlaza main
make                # sin cambios: "make: `main' is up to date."
make clean && make  # borra todo y recompila desde cero
```

> [!tip] Cómo se invoca
> `make` a secas ejecuta la **primera regla** del `Makefile`, por eso la regla del ejecutable final va primero. `make clean` ejecuta la regla `clean`, que no genera ningún archivo y sirve para borrar los compilados. Cuando el ejecutable queda "sucio" por compilaciones anteriores (por ejemplo, con el error *exec format error*), `make clean && make` lo resuelve.

En el curso, cada tarea trae un `Makefile` preparado: conviene leerlo para entender cómo compila el proyecto con un solo `make`. El curso tiene videos sobre el [proceso de compilación](https://www.loom.com/share/a07f3c11f0a942258d6a526dadd6cbaa) y sobre [Make](https://www.loom.com/share/ea4e8acb990942f49c4958426614cb91).

## Preguntas de repaso

> [!question]- ¿Cuándo ejecuta Make el comando de una regla cuyas dependencias son archivos?
> Cuando alguno de esos archivos se modificó después de la última vez que se generó el objetivo. Si nada cambió, la regla se salta.

> [!question]- ¿Por qué `frog.o` debe listar `reptil.h` como dependencia si `frog.c` no lo incluye directamente?
> Porque `frog.h` incluye `reptil.h`, así que su contenido termina dentro de `frog.c`. Si `reptil.h` cambia, `frog.o` queda desactualizado y hay que recompilarlo.

> [!question]- ¿Qué se recompila si se modifica `reptil.h` en el ejemplo?
> Los cinco `.o`, porque todos dependen de él directa o indirectamente, y después se reenlaza `main`.

> [!question]- ¿Por qué la regla del ejecutable va primero en el `Makefile`?
> Porque `make` sin argumentos ejecuta la primera regla, y lo que se quiere al escribir `make` es obtener el ejecutable completo.
