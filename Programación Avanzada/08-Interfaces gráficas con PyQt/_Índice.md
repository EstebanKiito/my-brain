# Interfaces gráficas con PyQt — índice

Conceptos y herramientas para el desarrollo de interfaces gráficas de usuario (GUI) en Python utilizando PyQt: ciclo de vida de la aplicación con `QApplication` y bucle de eventos, sistema bidimensional de coordenadas en pantalla, componentes visuales fundamentales (`QLabel`, `QLineEdit`, `QPushButton`, `QPixmap`), organización espacial adaptativa mediante layouts lineales (`QHBoxLayout`, `QVBoxLayout`) y en cuadrícula (`QGridLayout`), paradigma de programación dirigida por eventos con el mecanismo de señales y ranuras (*signals and slots*), captura de eventos de hardware de ratón y teclado, creación de señales personalizadas con `pyqtSignal`, patrones de arquitectura de software para desacoplamiento estricto entre Front-End y Back-End, y navegación fluida entre múltiples ventanas.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cinco notebooks de la novena semana del curso (interfaces gráficas, elementos gráficos básicos, eventos y señales, diseño front-back, y conexión entre ventanas), complementado con las diapositivas de clases.

## Orden de estudio
1. [[01 - Fundamentos de interfaces gráficas y ciclo de vida en PyQt|Fundamentos de interfaces gráficas y ciclo de vida en PyQt]]: el toolkit Qt y PyQt, rol de `QApplication`, ciclo del bucle de eventos con `app.exec()`, ventana base `QWidget` y depuración con `sys.excepthook`.
2. [[02 - Sistema de coordenadas y widgets básicos: etiquetas, entradas y botones|Sistema de coordenadas y widgets básicos]]: origen en la esquina superior izquierda, etiquetas de texto e imágenes con `QLabel` y `QPixmap`, entradas interactivas con `QLineEdit` y botones con `QPushButton`.
3. [[03 - Disposición de elementos: layouts y cuadrículas|Disposición de elementos: layouts y cuadrículas]]: gestión elástica del espacio con `QHBoxLayout` y `QVBoxLayout`, alineación bidimensional con `QGridLayout`, espaciadores `addStretch()` y modularización con POO.
4. [[04 - Eventos y señales: el mecanismo Signals and Slots|Eventos y señales: el mecanismo Signals and Slots]]: arquitectura dirigida por eventos, emisión y captura mediante señales y slots (`signal.connect`), paso de referencias y uso de `self.sender()`.
5. [[05 - Eventos de mouse teclado y señales personalizadas|Eventos de mouse, teclado y señales personalizadas]]: sobreescritura de `mousePressEvent` y `keyPressEvent`, definición de `pyqtSignal` como atributos de clase, tipado de señales y emisión con `.emit()`.
6. [[06 - Arquitectura de software: separación Front-End y Back-End|Arquitectura de software: separación Front-End y Back-End]]: principios de alta cohesión y bajo acoplamiento, responsabilidades de la vista frente a la lógica del modelo, y comunicación simétrica desacoplada mediante señales.
7. [[07 - Coordinación de múltiples ventanas mediante señales|Coordinación de múltiples ventanas mediante señales]]: navegación entre pantallas, transición de login a juego principal, métodos `show()` y `hide()`, y prevención de dependencias circulares.

