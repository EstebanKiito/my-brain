---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[06 - Clases, objetos y variables de clase]]"
  - "[[01 - Herencia y especialización de clases]]"
---

# Fundamentos de interfaces gráficas y ciclo de vida en PyQt

Hasta ahora los programas interactuaban mediante la terminal de comandos (CLI), donde el flujo de ejecución es lineal y síncrono. Las aplicaciones modernas requieren una **interfaz gráfica de usuario** (**GUI**, *Graphical User Interface*), donde el usuario interactúa visualmente mediante ventanas, botones y campos de texto en un flujo gobernado por eventos.

## La biblioteca PyQt y el bucle de eventos

**Qt** es una de las bibliotecas multiplataforma más robustas para desarrollo de interfaces gráficas en C++. **PyQt** es el enlace (*binding*) que permite utilizar todos los componentes de Qt desde Python.

Toda aplicación gráfica en PyQt depende de dos conceptos fundamentales:

1. **`QApplication`:** es el objeto central que administra los recursos globales, la configuración del sistema operativo y el ciclo de vida de la aplicación. Solo debe existir **una única instancia** de `QApplication` por programa.
2. **Bucle de eventos (*event loop*):** al invocar `app.exec()`, el programa entra en un ciclo infinito administrado por el sistema operativo que escucha activamente acciones del usuario (pulsaciones de teclas, clics de ratón, redibujado de ventanas) y despacha las respuestas adecuadas.

## Creación de una ventana básica

La clase base para cualquier elemento visual en PyQt es **`QWidget`**. Si un `QWidget` se crea sin un elemento contenedor padre, se comporta automáticamente como una **ventana independiente**:

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        # Configuración inicial de la ventana
        self.setWindowTitle("Mi Primera Ventana")
        # setGeometry(pos_x, pos_y, ancho, alto)
        self.setGeometry(200, 100, 300, 200)

if __name__ == "__main__":
    # 1. Instanciar la aplicación
    app = QApplication(sys.argv)
    # 2. Crear y mostrar la ventana
    ventana = MiVentana()
    ventana.show()
    # 3. Iniciar el bucle de eventos y retornar código de salida
    sys.exit(app.exec())
```

Al ejecutarse, PyQt delega el estilo del marco y los botones de minimizar, maximizar y cerrar al gestor de ventanas nativo del sistema operativo:

| ![Ventana genérica](adjuntos/Ventana%20vac%C3%ADa%20gen%C3%A9rica%20en%20PyQt.png) | ![Ventana macOS](adjuntos/Ventana%20vac%C3%ADa%20de%20PyQt%20en%20macOS.png) | ![Ventana Windows](adjuntos/Ventana%20vac%C3%ADa%20de%20PyQt%20en%20Windows.png) | ![Ventana Linux](adjuntos/Ventana%20vac%C3%ADa%20de%20PyQt%20en%20Linux.png) |
|---|---|---|---|
| Ventana genérica | macOS | Windows | Linux |

> [!example]- Transcripción de las imágenes
> - Muestra de una ventana vacía con fondo gris claro y barra de título en distintos sistemas:
>   - macOS: tres botones circulares (rojo, amarillo, verde) a la izquierda.
>   - Windows y Linux: botones clásicos de minimizar, maximizar y cerrar a la derecha.

> [!warning] Depuración de errores silenciosos en PyQt
> Por defecto, cuando ocurre una excepción en Python dentro de un método llamado por Qt, el bucle de eventos de C++ puede atraparla internamente y cerrar el programa de golpe sin imprimir el *traceback* en la terminal. Para forzar la visualización de los errores en consola, conviene redefinir el gestor de excepciones de Python al inicio del script:
> `sys.excepthook = lambda cls, exc, tb: sys.__excepthook__(cls, exc, tb)`

> [!tip] La regla de oro del bucle de eventos
> El método `app.exec()` es bloqueante: toma el control absoluto del hilo principal de ejecución. Ninguna línea de código ubicada después de `app.exec()` se ejecutará hasta que el usuario cierre todas las ventanas de la aplicación.

## Preguntas de repaso

> [!question]- ¿Por qué es obligatorio instanciar `QApplication` antes de crear cualquier `QWidget`?
> Porque `QApplication` inicializa el subsistema gráfico de Qt, los manejadores de fuentes y la conexión con el servidor gráfico del sistema operativo; sin ella, la creación de cualquier widget arroja error.

> [!question]- ¿Cuál es la función del método `app.exec()` en un programa con interfaz gráfica?
> Inicia el bucle de eventos (*event loop*), manteniendo el programa a la escucha permanente de acciones del usuario o del sistema operativo hasta que se solicite la salida.

> [!question]- ¿Qué representan los cuatro parámetros del método `setGeometry(x, y, w, h)`?
> `x` e `y` definen las coordenadas de la esquina superior izquierda de la ventana respecto a la pantalla del monitor; `w` define el ancho (*width*) y `h` el alto (*height*) en píxeles.

> [!question]- ¿Por qué un error de lógica dentro de un evento de PyQt a veces cierra la ventana sin mostrar nada en la consola?
> Porque la capa subyacente en C++ de Qt intercepta las excepciones no manejadas de Python y aborta el proceso; configurar `sys.excepthook` asegura que el stack trace completo se imprima siempre en la terminal.
