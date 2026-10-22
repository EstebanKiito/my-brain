# PyQt avanzado — índice

Herramientas avanzadas para la construcción de interfaces gráficas interactivas, asíncronas y multimedia en Python utilizando PyQt: ejecución de tareas pesadas en segundo plano con `QThread` respetando la regla de hilo único para la GUI, comunicación segura mediante señales thread-safe, integración desacoplada entre sockets de red TCP y ventanas gráficas, temporizadores periódicos nativos con `QTimer` para animaciones y ejecuciones diferidas con `singleShot`, arquitectura de aplicaciones de escritorio completas con `QMainWindow` (menús, barras de herramientas, acciones `QAction`, barra de estado y widget central), control de pulsaciones de teclado descartando eventos automáticos con `event.isAutoRepeat()`, y reproducción multimedia de baja latencia con `QSoundEffect` y música de fondo con `QMediaPlayer`.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los tres notebooks principales y el notebook bonus de la decimocuarta semana del curso (QThreads, integración con networking, misceláneo y bonus de QTimer con QMainWindow), complementado con las diapositivas de clases.

## Orden de estudio
1. [[01 - Concurrencia en interfaces gráficas: QThread y señales seguras|Concurrencia en interfaces gráficas: QThread y señales seguras]]: prevención del congelamiento del GUI Thread, la regla de oro de Qt, delegación de cómputo a `QThread`, notificación thread-safe con `pyqtSignal` y exclusión mutua con `QMutex`.
2. [[02 - Integración de networking con PyQt: clientes y servidores asíncronos|Integración de networking con PyQt: clientes y servidores asíncronos]]: resolución del conflicto entre sockets bloqueantes y bucle de eventos, arquitectura Front/Back de red con hilos de escucha, y gestión de desconexiones en `closeEvent`.
3. [[03 - Temporizadores periódicos con QTimer y ejecución diferida|Temporizadores periódicos con QTimer y ejecución diferida]]: temporizadores dentro del bucle de eventos de la GUI, actualización periódica sin hilos secundarios (`timeout`), y ejecuciones diferidas de un solo disparo con `QTimer.singleShot()`.
4. [[04 - Estructura de ventanas completas con QMainWindow menús y barras|Estructura de ventanas completas con QMainWindow menús y barras]]: anatomía de aplicaciones de escritorio profesionales, asignación de `centralWidget`, comandos unificados con `QAction`, atajos de teclado y mensajes en la barra de estado.
5. [[05 - Control avanzado de teclado con isAutoRepeat y reproducción de audio|Control avanzado de teclado con isAutoRepeat y reproducción de audio]]: filtrado de ráfagas automáticas del teclado con `event.isAutoRepeat()`, efectos sonoros de latencia cero con `QSoundEffect` y pistas extensas con `QMediaPlayer`.

