---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de interfaces gráficas y ciclo de vida en PyQt]]"
  - "[[02 - Sistema de coordenadas y widgets básicos: etiquetas, entradas y botones]]"
---

# Eventos y señales: el mecanismo Signals and Slots

En las aplicaciones con interfaz gráfica, el orden en que se ejecutan las instrucciones no lo determina el programador en una secuencia fija, sino el usuario mediante sus acciones. Este modelo se denomina **programación dirigida por eventos** (*event-driven programming*), y en PyQt se implementa a través de la arquitectura de **señales y ranuras** (*signals and slots*).

## El bucle de eventos y la detección de acciones

Cuando se inicia `app.exec()`, PyQt entra en un bucle continuo de escucha. Cada vez que el usuario presiona una tecla, hace clic o redimensiona la ventana, el sistema operativo genera un evento y lo deposita en la cola de eventos de la aplicación:

![Flujo de interacción y bucle de eventos en PyQt](adjuntos/Flujo%20de%20interacci%C3%B3n%20y%20bucle%20de%20eventos%20en%20PyQt.png)

> [!example]- Transcripción de la imagen
> - Diagrama de flujo del bucle de eventos:
>   - El usuario realiza una acción visual (ej. clic en botón).
>   - La aplicación detecta el suceso en su cola de eventos.
>   - Se emite una señal que despacha la ejecución del manejador o ranura (*slot*) correspondiente.
>   - La interfaz se actualiza y el bucle vuelve a quedar a la espera de nuevas acciones.

## Arquitectura de Señales (Signals) y Ranuras (Slots)

Qt sustituye los callbacks tradicionales de bajo nivel por un mecanismo fuertemente tipado y desacoplado:

- **Señal (*Signal*):** es una notificación emitida por un objeto cuando cambia su estado o detecta una interacción (por ejemplo `boton.clicked`). El emisor no necesita saber quién responderá a la señal.
- **Ranura (*Slot*):** es cualquier método o función invocable (*callable*) de Python que se ejecuta en respuesta a una señal emitida.
- **Conexión (*connect*):** vincula una señal con un slot mediante la sintaxis:

$$\text{emisor}.\text{señal}.\text{connect}(\text{slot})$$

### Ejemplo de conexión y uso de sender()

```python
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

class VentanaContador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Votos")
        self.total = 0

        self.label = QLabel("Votos: 0")
        self.btn_sumar = QPushButton("Sumar voto")
        self.btn_restar = QPushButton("Restar voto")

        # Conectar señales clicked a sus respectivos slots
        self.btn_sumar.clicked.connect(self.actualizar_votos)
        self.btn_restar.clicked.connect(self.actualizar_votos)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_sumar)
        layout.addWidget(self.btn_restar)
        self.setLayout(layout)

    def actualizar_votos(self):
        # self.sender() identifica cuál de los dos botones detonó la señal
        origen = self.sender()
        if origen == self.btn_sumar:
            self.total += 1
        elif origen == self.btn_restar:
            self.total -= 1
        self.label.setText(f"Votos: {self.total}")
```

> [!warning] Cuidado con los paréntesis al conectar slots
> Al conectar una señal a una ranura debes pasar la **referencia a la función sin paréntesis**: `boton.clicked.connect(self.mi_metodo)`. Si escribes `connect(self.mi_metodo())` con paréntesis, ejecutarás el método inmediatamente durante la construcción de la ventana en lugar de esperar al clic.

> [!tip] Conexiones uno a muchos y muchos a uno
> Una misma señal puede conectarse a múltiples slots distintos que se ejecutarán en cadena, y un mismo slot puede recibir señales provenientes de diferentes emisores.

## Preguntas de repaso

> [!question]- ¿Qué significa que una interfaz gráfica opere bajo el paradigma de programación dirigida por eventos?
> Que el flujo de ejecución no sigue un orden secuencial predefinido en el código, sino que reacciona de forma asíncrona a los estímulos generados por el usuario o por el sistema operativo.

> [!question]- ¿Cuál es la diferencia fundamental entre una señal (*signal*) y un slot (*ranura*) en PyQt?
> La señal es el evento o mensaje emitido por un componente cuando ocurre un cambio, mientras que el slot es la función o método que recibe la notificación y ejecuta la lógica de respuesta.

> [!question]- ¿Qué ocurre si un programador escribe `boton.clicked.connect(self.saludar())` en lugar de `boton.clicked.connect(self.saludar)`?
> `self.saludar()` se ejecuta inmediatamente al inicializar la ventana y le entrega a `connect()` el valor de retorno (generalmente `None`), fallando o impidiendo que el clic posterior ejecute la función.

> [!question]- ¿Para qué sirve el método `self.sender()` dentro de un slot en PyQt?
> Retorna una referencia directa al widget u objeto específico que emitió la señal que acaba de detonar la ejecución del slot, permitiendo reutilizar el mismo método con múltiples emisores.

