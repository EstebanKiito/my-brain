---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/patrones-de-diseno
  - origen/complemento
prerrequisitos:
  - "[[05 - Eventos de mouse teclado y señales personalizadas]]"
  - "[[06 - Arquitectura de software: separación Front-End y Back-End]]"
---

# Coordinación de múltiples ventanas mediante señales

Casi cualquier aplicación real requiere más de una ventana: una pantalla inicial de inicio de sesión (*login*), un panel de configuración emergente, o la transición hacia la ventana principal del juego o panel administrativo. Gestionar la navegación entre pantallas sin acoplarlas entre sí es clave para evitar dependencias circulares.

## El problema del acoplamiento entre ventanas

Si la ventana de login crea directamente una instancia de la ventana del juego dentro de su código y la muestra con `self.ventana_juego.show()`, ambas quedan rígidamente vinculadas:

- La ventana de login ya no puede reutilizarse en otro contexto.
- Si la ventana de juego necesita avisar a la de login que el usuario cerró sesión, surge una **referencia circular** cruzada entre clases.
- Modificar el flujo de pantallas exige reescribir la lógica interna de todas las ventanas.

## Transición limpia desacoplada mediante señales

La solución idiomática consiste en aplicar el principio de bajo acoplamiento: **ninguna ventana conoce a las demás**. Cada ventana se limita a emitir una señal personalizada cuando termina su labor, y un controlador central o la lógica del Back-End coordina qué ventana se oculta y cuál se muestra:

```python
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout

# 1. Ventana de Inicio (Login)
class VentanaLogin(QWidget):
    # Señal emitida cuando el usuario presiona ingresar
    senal_autenticacion = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acceso")
        self.input_user = QLineEdit()
        self.btn_entrar = QPushButton("Iniciar Sesión")
        self.btn_entrar.clicked.connect(self.enviar_datos)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ingresa tu apodo:"))
        layout.addWidget(self.input_user)
        layout.addWidget(self.btn_entrar)
        self.setLayout(layout)

    def enviar_datos(self):
        usuario = self.input_user.text().strip()
        if usuario:
            self.senal_autenticacion.emit(usuario)

# 2. Ventana Principal de Juego
class VentanaJuego(QWidget):
    senal_volver_login = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Juego en Progreso")
        self.label_bienvenida = QLabel("Esperando jugador...")
        self.btn_salir = QPushButton("Cerrar Sesión")
        self.btn_salir.clicked.connect(self.volver)

        layout = QVBoxLayout()
        layout.addWidget(self.label_bienvenida)
        layout.addWidget(self.btn_salir)
        self.setLayout(layout)

    def iniciar_partida(self, nombre_jugador: str):
        self.label_bienvenida.setText(f"¡Bienvenido/a, {nombre_jugador}!")
        self.show()

    def volver(self):
        self.hide()
        self.senal_volver_login.emit()
```

## Coordinación en el punto de entrada

El controlador o archivo principal se encarga de cambiar la visibilidad de las ventanas usando los métodos nativos **`show()`** y **`hide()`**:

```python
def procesar_login_exitoso(usuario: str):
    ventana_login.hide()
    ventana_juego.iniciar_partida(usuario)

def procesar_cierre_sesion():
    ventana_login.show()

# Conexión de transiciones de pantalla
ventana_login.senal_autenticacion.connect(procesar_login_exitoso)
ventana_juego.senal_volver_login.connect(procesar_cierre_sesion)
```

> [!tip] Diferencia entre hide() y close()
> Invocar `self.hide()` oculta temporalmente la ventana de la vista del usuario manteniendo en memoria todo su estado y los textos ingresados. Invocar `self.close()` detona el evento de cierre (`closeEvent`) y puede destruir los recursos visuales del widget.

> [!warning] La trampa de cerrar la última ventana visible
> En PyQt, por defecto la aplicación finaliza si se cierra la última ventana abierta. Al alternar entre pantallas, asegúrate de invocar `nueva_ventana.show()` antes o inmediatamente después de ocultar la anterior, o configura `app.setQuitOnLastWindowClosed(False)` si necesitas períodos intermedios de transición.

## Preguntas de repaso

> [!question]- ¿Qué riesgo arquitectónico se presenta si la ventana de login contiene una referencia directa a la ventana del juego?
> Se genera un alto acoplamiento y potenciales referencias circulares que impiden reutilizar o testear la ventana de login de forma aislada.

> [!question]- ¿Cómo se comunican dos ventanas distintas en un programa con arquitectura desacoplada?
> La primera ventana emite una `pyqtSignal` al completar su acción, y un controlador exterior captura la señal, oculta la primera ventana y abre la segunda entregándole los datos.

> [!question]- ¿Cuál es la ventaja de utilizar `self.hide()` sobre `self.close()` al navegar entre ventanas?
> `hide()` solo vuelve invisible el widget manteniendo su estado interno intacto, permitiendo reabrir la ventana más tarde sin tener que volver a instanciar ni configurar sus componentes.

> [!question]- ¿Qué ocurre con la aplicación de PyQt si se llama a `self.close()` en la única ventana que estaba visible en pantalla?
> Si la propiedad `quitOnLastWindowClosed` está activa (comportamiento por defecto), PyQt interpreta que la interfaz terminó y finaliza automáticamente el proceso de la aplicación.
