---
ramo: "Programación Avanzada"
tema: "PyQt avanzado"
tags:
  - programacion/gui
  - programacion/pyqt
  - programacion/concurrencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Hilos y procesos: el módulo threading]]"
  - "[[04 - Eventos y señales: el mecanismo Signals and Slots]]"
  - "[[05 - Eventos de mouse teclado y señales personalizadas]]"
---

# Concurrencia en interfaces gráficas: QThread y señales seguras

En una aplicación con interfaz gráfica, el hilo principal de ejecución (**GUI Thread**) está a cargo exclusivamente de ejecutar el bucle de eventos (`QApplication.exec()`), capturar clics y redibujar los componentes en pantalla. Si ejecutamos una tarea lenta en este hilo —como una descarga pesada o un cálculo matemático extenso—, la ventana se congelará de inmediato, mostrando el cursor de espera del sistema operativo.

## El problema del congelamiento de la GUI

Cuando un método de la ventana invoca una operación bloqueante (como `time.sleep()` o una petición de red), el bucle de eventos se detiene: los eventos de usuario se acumulan en la cola sin procesarse y el sistema operativo marca la aplicación como **"No responde"**.

Para mantener la interfaz fluida y responsiva mientras se procesan tareas largas, debemos ejecutar el trabajo pesado en segundo plano utilizando **`QThread`**.

![Animación de ejecución con QThread](adjuntos/Animaci%C3%B3n%20de%20ejecuci%C3%B3n%20concurrente%20con%20QThread%20en%20PyQt.gif)

> [!example]- Transcripción de la imagen
> - Animación de ventana gráfica:
>   - Dos procesos en paralelo: una barra de progreso que avanza gradualmente en segundo plano mientras los botones de la interfaz permanecen interactivos y receptivos al usuario.

## La regla de oro de PyQt: nunca alterar la GUI desde hilos secundarios

En Qt rige una ley arquitectónica estricta: **los widgets de la interfaz gráfica solo pueden ser manipulados por el hilo principal**.

Si un hilo secundario intenta modificar un widget directamente (por ejemplo ejecutando `self.etiqueta.setText("Listo")` desde su método `run()`), la aplicación sufrirá corrupción de memoria gráfica o finalizará abruptamente con un error de violación de segmento (*Segmentation Fault*).

### La solución: Comunicación segura con pyqtSignal

La forma correcta y segura de comunicar un hilo secundario con la interfaz consiste en emitir señales personalizadas. Qt intercepta automáticamente la señal y traslada la ejecución del slot receptor al **hilo principal de forma thread-safe**:

```python
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
import time

# 1. Hilo secundario para trabajo pesado
class TrabajadorPesado(QThread):
    # Señal personalizada que transporta el porcentaje de avance
    senal_progreso = pyqtSignal(int)
    senal_finalizado = pyqtSignal(str)

    def run(self):
        for i in range(1, 101, 25):
            time.sleep(0.04)  # Simula cálculo pesado
            self.senal_progreso.emit(i)
        self.senal_finalizado.emit("Proceso completado exitosamente")

# 2. Ventana en el hilo principal
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Presiona para iniciar")
        self.btn = QPushButton("Comenzar cálculo")
        self.btn.clicked.connect(self.iniciar_tarea)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def iniciar_tarea(self):
        self.btn.setEnabled(False)  # Desactivar botón durante la ejecución
        self.hilo = TrabajadorPesado()
        # Conectar señales del hilo a métodos del hilo principal
        self.hilo.senal_progreso.connect(self.actualizar_progreso)
        self.hilo.senal_finalizado.connect(self.tarea_terminada)
        self.hilo.start()

    def actualizar_progreso(self, porcentaje: int):
        self.label.setText(f"Procesando: {porcentaje}%")

    def tarea_terminada(self, mensaje: str):
        self.label.setText(mensaje)
        self.btn.setEnabled(True)
```

> [!warning] La referencia al hilo debe persistir en la instancia
> Al crear el hilo dentro de un método debes guardarlo como atributo (`self.hilo = TrabajadorPesado()`). Si usas una variable local (`hilo = TrabajadorPesado()`), el recolector de basura de Python destruirá el objeto al salir de la función antes de que el hilo termine, arrojando el error `QThread: Destroyed while thread is still running`.

> [!tip] Exclusión mutua con QMutex
> Si múltiples hilos `QThread` necesitan sincronizar el acceso a variables compartidas en memoria, puedes utilizar **`QMutex`** de `PyQt5.QtCore` (análogo a `threading.Lock`) mediante `mutex.lock()` y `mutex.unlock()`.

## Preguntas de repaso

> [!question]- ¿Por qué una llamada a `time.sleep(5)` dentro del método de un botón congela toda la ventana de PyQt?
> Porque bloquea el hilo principal donde corre el bucle de eventos (`app.exec()`), impidiendo que Qt procese eventos de redibujado de pantalla y clics del ratón.

> [!question]- ¿Qué consecuencia técnica ocurre si un `QThread` modifica directamente un widget (`label.setText()`) desde su método `run()`?
> Se viola el modelo de hilo único de Qt para componentes visuales, provocando condiciones de carrera en el servidor gráfico y caídas abruptas por *Segmentation Fault*.

> [!question]- ¿Cómo se asegura PyQt de que un slot se ejecute en el hilo correcto al recibir una señal de un `QThread`?
> Qt utiliza una conexión por cola (*queued connection*), depositando la señal en la cola de eventos del hilo principal para que este ejecute el slot en su propio contexto de forma segura.

> [!question]- ¿Qué causa el error `QThread: Destroyed while thread is still running`?
> Ocurre cuando la instancia del `QThread` se asigna a una variable local de un método; al terminar la función, Python elimina la referencia y recolecta el objeto mientras el hilo del sistema operativo sigue activo.

