---
ramo: "Programación Avanzada"
tema: "PyQt avanzado"
tags:
  - programacion/gui
  - programacion/pyqt
  - programacion/networking
  - origen/complemento
prerrequisitos:
  - "[[01 - Concurrencia en interfaces gráficas: QThread y señales seguras]]"
  - "[[03 - Sockets TCP en Python: arquitectura y ciclo de vida]]"
  - "[[06 - Arquitectura de software: separación Front-End y Back-End]]"
---

# Integración de networking con PyQt: clientes y servidores asíncronos

Construir aplicaciones en red interactivas —como salas de chat, pizarras colaborativas o videojuegos multijugador— combina dos mundos con requerimientos opuestos: interfaces gráficas gobernadas por eventos visuales rápidos y sockets de red cuyas llamadas (`recv()`, `accept()`) son intrínsecamente bloqueantes. Para unirlos sin congelar la pantalla, aplicamos una arquitectura desacoplada basada en hilos y señales.

## El conflicto fundamental entre Sockets y la GUI

Un socket TCP en modo bloqueante detiene la ejecución del hilo actual hasta que lleguen paquetes de red. Si ejecutamos `sock.recv()` dentro del hilo de la ventana, la interfaz gráfica dejará de responder de inmediato.

Por otra parte, la lógica de red no debe conocer ni manipular directamente botones ni etiquetas de PyQt para no violar el principio de responsabilidad única ni provocar condiciones de carrera en el servidor gráfico.

## Arquitectura de integración Front-End y Back-End de red

Para resolver este desafío desacoplamos la aplicación en dos componentes independientes que se comunican exclusivamente mediante señales de Qt:

![Arquitectura de integración networking y PyQt](adjuntos/Arquitectura%20de%20integraci%C3%B3n%20entre%20networking%20y%20PyQt.png)

> [!example]- Transcripción de la imagen
> - Diagrama de arquitectura de comunicación:
>   - El usuario interactúa con la ventana en el hilo principal (`Front-End`), que emite señales hacia el `Back-End`.
>   - El `Back-End` ejecuta el socket de red en un `QThread` dedicado en segundo plano.
>   - Al recibir datos por la red, el `QThread` emite señales hacia el `Front-End` para actualizar la vista de forma segura.

### Implementación del cliente de red en un QThread

El cliente de red hereda de `QThread`. Su método `run()` establece el socket y permanece en un bucle continuo a la escucha de mensajes:

```python
import socket
from PyQt5.QtCore import QThread, pyqtSignal

class ClienteRed(QThread):
    # Señal emitida hacia la GUI cuando llega un mensaje desde el servidor
    senal_mensaje_recibido = pyqtSignal(str)

    def __init__(self, host: str, puerto: int):
        super().__init__()
        self.host = host
        self.puerto = puerto
        self.activo = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.sock.connect((self.host, self.puerto))
            while self.activo:
                # recv() bloquea únicamente dentro de este hilo secundario
                datos = self.sock.recv(1024)
                if not datos:
                    break
                # Emitir señal thread-safe hacia el hilo principal de la GUI
                self.senal_mensaje_recibido.emit(datos.decode("utf-8"))
        except ConnectionError:
            self.senal_mensaje_recibido.emit("[Error de conexión con el servidor]")
        finally:
            self.sock.close()

    def enviar_mensaje(self, texto: str):
        # Método invocado desde el Front-End para despachar datos a la red
        if self.activo:
            self.sock.sendall(texto.encode("utf-8"))
```

### Integración en la Ventana Gráfica

La ventana se limita a conectar sus eventos visuales con los métodos del cliente y recibir las señales entrantes:

```python
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QPushButton, QVBoxLayout

class VentanaChat(QWidget):
    def __init__(self, cliente_red: ClienteRed):
        super().__init__()
        self.cliente = cliente_red

        # Componentes visuales
        self.historial = QTextEdit()
        self.historial.setReadOnly(True)
        self.input_msg = QLineEdit()
        self.btn_enviar = QPushButton("Enviar")

        # Conectar eventos visuales
        self.btn_enviar.clicked.connect(self.despachar_texto)
        # Conectar señal del socket hacia la actualización de pantalla
        self.cliente.senal_mensaje_recibido.connect(self.mostrar_nuevo_mensaje)

        layout = QVBoxLayout()
        layout.addWidget(self.historial)
        layout.addWidget(self.input_msg)
        layout.addWidget(self.btn_enviar)
        self.setLayout(layout)

    def despachar_texto(self):
        mensaje = self.input_msg.text().strip()
        if mensaje:
            self.cliente.enviar_mensaje(mensaje)
            self.input_msg.clear()

    def mostrar_nuevo_mensaje(self, texto: str):
        self.historial.append(texto)
```

> [!warning] Cierre seguro de conexiones con closeEvent
> Al cerrar la ventana, el bucle `while self.activo:` en el hilo de red seguirá corriendo a menos que lo desactives. Sobrescribe el método `closeEvent(self, event)` en tu ventana para apagar la bandera (`self.cliente.activo = False`), cerrar el socket y llamar a `self.cliente.quit()`.

> [!tip] Ventaja del desacoplamiento
> Esta arquitectura te permite reemplazar el socket TCP por un cliente de WebSockets o una conexión UDP sin tener que tocar ni una sola línea del código visual de la ventana.

## Preguntas de repaso

> [!question]- ¿Por qué no se debe invocar `sock.recv()` directamente dentro del método de un botón de la interfaz?
> Porque `recv()` es una llamada bloqueante que espera paquetes de red; ejecutarla en el hilo de la ventana congela por completo la interfaz gráfica y detiene el redibujado de componentes.

> [!question]- ¿Cómo se asegura que un mensaje recibido por el socket de red actualice un `QTextEdit` sin violar la seguridad de hilos?
> El hilo de red emite una `pyqtSignal` con el texto recibido; Qt transfiere la ejecución al hilo principal de la GUI, que ejecuta el slot para modificar el widget de forma segura.

> [!question]- ¿Cuál es la función del método `enviar_mensaje()` en la clase `ClienteRed`?
> Permite que la interfaz gráfica entregue un texto al objeto de red para que este lo codifique a bytes y lo transmita por el socket hacia el servidor.

> [!question]- ¿Qué ocurre si el usuario cierra la ventana gráfica pero no se detiene el hilo del socket de red?
> El hilo secundario permanecerá activo en segundo plano en el sistema operativo, impidiendo que el proceso de Python termine por completo al salir.
