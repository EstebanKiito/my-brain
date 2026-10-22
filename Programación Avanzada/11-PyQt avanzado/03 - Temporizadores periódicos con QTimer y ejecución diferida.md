---
ramo: "Programación Avanzada"
tema: "PyQt avanzado"
tags:
  - programacion/gui
  - programacion/pyqt
  - programacion/timers
  - origen/complemento
prerrequisitos:
  - "[[04 - Eventos y señales: el mecanismo Signals and Slots]]"
  - "[[01 - Concurrencia en interfaces gráficas: QThread y señales seguras]]"
---

# Temporizadores periódicos con QTimer y ejecución diferida

En videojuegos, animaciones y tableros interactivos es común requerir acciones repetitivas a intervalos regulares: mover un personaje en pantalla cada 30 milisegundos, actualizar un reloj cada segundo o refrescar datos meteorológicos periódicamente. Ejecutar un bucle con `time.sleep()` congelaría la interfaz, y usar hilos tradicionales exigiría coordinar señales complejas. Para este propósito, PyQt ofrece **`QTimer`**.

## La ventaja de QTimer frente a otros temporizadores

A diferencia de los hilos de `threading` o `QThread`, **`QTimer` opera directamente dentro del bucle de eventos del hilo principal**.

Esto significa que cada vez que el temporizador se activa, ejecuta el método conectado directamente en el contexto seguro de la interfaz gráfica, permitiendo **modificar widgets, actualizar posiciones y redibujar componentes de forma inmediata sin violar la seguridad de hilos**.

## Ciclo de vida y métodos de QTimer

La clase `QTimer` emite periódicamente la señal **`timeout`** tras transcurrir el intervalo fijado en milisegundos:

- **`setInterval(milisegundos)`:** establece la cadencia de repetición en milisegundos ($1000\text{ ms} = 1\text{ segundo}$).
- **`timeout.connect(slot)`:** vincula el evento periódico a la función o método que debe ejecutarse.
- **`start()`:** activa la cuenta regresiva periódica.
- **`stop()`:** suspende el temporizador.
- **`isActive()`:** retorna un booleano indicando si el temporizador está corriendo.

```python
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer

class CronometroSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cronómetro")
        self.segundos = 0

        self.label_tiempo = QLabel("Tiempo: 0 s")
        self.btn_iniciar = QPushButton("Iniciar / Pausar")
        self.btn_iniciar.clicked.connect(self.alternar_temporizador)

        # 1. Instanciar el temporizador de Qt
        self.timer = QTimer()
        self.timer.setInterval(1000)  # Cada 1000 ms = 1 segundo
        self.timer.timeout.connect(self.actualizar_segundo)

        layout = QVBoxLayout()
        layout.addWidget(self.label_tiempo)
        layout.addWidget(self.btn_iniciar)
        self.setLayout(layout)

    def alternar_temporizador(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start()

    def actualizar_segundo(self):
        # Modificación segura y directa de widgets en el hilo principal
        self.segundos += 1
        self.label_tiempo.setText(f"Tiempo: {self.segundos} s")
```

## Ejecución diferida de un solo disparo: singleShot

Cuando no se necesita un ciclo recurrente, sino únicamente **retrasar una acción futura** (por ejemplo ocultar un mensaje de confirmación después de 3 segundos o dar una pausa antes de iniciar una animación), se utiliza el método estático **`QTimer.singleShot()`**:

$$\text{QTimer.singleShot}(\text{milisegundos}, \text{funcion\_a\_ejecutar})$$

```python
def mostrar_notificacion_temporal(self):
    self.label_aviso.setText("¡Configuración guardada!")
    # Programa el borrado del aviso tras 3000 ms (3 segundos) sin bloquear la GUI
    QTimer.singleShot(3000, self.label_aviso.clear)
```

> [!warning] La unidad de tiempo es MILISEGUNDOS
> Un error clásico de principiante es invocar `timer.setInterval(5)` esperando 5 segundos de pausa. En Qt toda la medición de temporizadores se expresa en **milisegundos**; para 5 segundos debes especificar `5000`.

> [!tip] Animaciones fluidas a 60 FPS
> Para crear animaciones fluidas de juegos 2D en PyQt, configura un `QTimer` con un intervalo de aproximadamente $16\text{ ms}$ ($\frac{1000\text{ ms}}{60} \approx 16.6\text{ ms}$), correspondiente a una tasa de refresco estándar de 60 cuadros por segundo (*FPS*).

## Preguntas de repaso

> [!question]- ¿Por qué `QTimer` puede modificar etiquetas y botones directamente sin generar errores de concurrencia?
> Porque se ejecuta e integra de forma nativa dentro del bucle de eventos del hilo principal (`QApplication.exec()`), sin crear hilos secundarios que compitan por la memoria gráfica.

> [!question]- ¿Cuál es la señal emitida por un `QTimer` cada vez que transcurre el período configurado?
> La señal `timeout`, la cual se conecta a cualquier ranura o método mediante `timer.timeout.connect(metodo)`.

> [!question]- ¿Para qué se utiliza el método estático `QTimer.singleShot(ms, callback)`?
> Para ejecutar una función o método una única vez después de transcurrido un intervalo de tiempo especificado en milisegundos, sin necesidad de instanciar un temporizador permanente.

> [!question]- ¿Qué ocurre si se llama a `timer.setInterval(2)` en lugar de `timer.setInterval(2000)`?
> El temporizador se ejecutará a una velocidad vertiginosa cada 2 milisegundos (500 veces por segundo) en lugar de cada 2 segundos, saturando innecesariamente el procesador.
