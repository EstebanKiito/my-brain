---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[04 - Eventos y señales: el mecanismo Signals and Slots]]"
---

# Eventos de mouse teclado y señales personalizadas

Más allá de los clics en botones nativos, las interfaces complejas requieren responder directamente a la posición del cursor, la pulsación de teclas del teclado y la transmisión de información propia del negocio entre distintos componentes de la aplicación. Para lograrlo, PyQt permite interceptar eventos del sistema y crear señales personalizadas.

## Manejadores de eventos de mouse y teclado

En PyQt, las interacciones físicas de hardware se gestionan sobrescribiendo métodos especiales de la clase base `QWidget`:

### 1. Eventos del ratón (mousePressEvent y mouseMoveEvent)
Cada vez que el usuario presiona un botón del ratón sobre la ventana, se ejecuta **`mousePressEvent(event)`**. El objeto `event` (instancia de `QMouseEvent`) provee información contextual detallada:

- `event.x()` y `event.y()`: coordenadas del cursor en píxeles relativas a la ventana.
- `event.button()`: indica cuál botón se presionó (`Qt.LeftButton`, `Qt.RightButton`).

> Por defecto, `mouseMoveEvent` solo se activa mientras se mantiene presionado un botón. Para recibir coordenadas continuas con solo mover el cursor, se debe activar `self.setMouseTracking(True)`.

### 2. Eventos del teclado (keyPressEvent)
Cuando la ventana tiene el foco y el usuario presiona una tecla, Qt invoca **`keyPressEvent(event)`**:

- `event.text()`: retorna el caracter alfanumérico escrito.
- `event.key()`: código numérico entero de la tecla, comparable con las constantes de `PyQt5.QtCore.Qt` (`Qt.Key_Escape`, `Qt.Key_Return`, `Qt.Key_W`, `Qt.Key_Space`).

```python
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

class VentanaControlTeclas(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Presiona una tecla...", self)
        self.label.setGeometry(20, 20, 260, 40)

    def keyPressEvent(self, event):
        tecla = event.key()
        if tecla == Qt.Key_Escape:
            self.close()  # Cierra la ventana al presionar Escape
        elif tecla == Qt.Key_Space:
            self.label.setText("¡Barra espaciadora presionada!")
        else:
            self.label.setText(f"Tecla: {event.text()} (Código: {tecla})")
```

## Señales personalizadas con pyqtSignal

Las señales predefinidas de Qt (como `clicked` o `textChanged`) solo informan eventos gráficos estándar. Para comunicar sucesos propios de nuestra aplicación (por ejemplo avisar que un juego terminó o que un usuario ingresó credenciales válidas), creamos **señales personalizadas** usando **`pyqtSignal`** de `PyQt5.QtCore`:

### Reglas para definir y emitir una señal personalizada
1. **Definición a nivel de clase:** la señal debe declararse obligatoriamente como un **atributo de clase** (fuera de `__init__`).
2. **Herencia de QObject:** la clase debe heredar de `QObject` o de cualquier widget de Qt (`QWidget`).
3. **Firma de tipos:** se indican los tipos de datos que la señal transportará (ej. `pyqtSignal(str, int)`).
4. **Emisión con .emit():** se invoca `self.mi_señal.emit(datos)` cuando ocurre el evento.

```python
from PyQt5.QtCore import QObject, pyqtSignal

class SensorTemperatura(QObject):
    # Declaración de la señal como atributo de clase indicando tipos
    alerta_temperatura = pyqtSignal(float, str)

    def __init__(self, limite: float):
        super().__init__()
        self.limite = limite

    def registrar_medicion(self, valor: float):
        if valor > self.limite:
            # Emisión de la señal con sus argumentos correspondientes
            self.alerta_temperatura.emit(valor, "PELIGRO: Sobrecalentamiento")
```

> [!warning] La señal DEBE ser atributo de clase
> Intentar definir `self.mi_senal = pyqtSignal()` dentro del constructor `__init__` genera un error en tiempo de ejecución. PyQt necesita registrar la estructura de señales durante la creación de la clase antes de instanciar cualquier objeto.

> [!tip] Emisión sin argumentos
> Si la señal solo sirve para notificar que un evento ocurrió sin necesidad de transportar datos adicionales, se define vacía: `senal_reinicio = pyqtSignal()`, y se emite simplemente con `self.senal_reinicio.emit()`.

## Preguntas de repaso

> [!question]- ¿Por qué es obligatorio definir las instancias de `pyqtSignal` como atributos de clase y no dentro de `__init__`?
> Porque Qt necesita registrar los metadatos de las señales en la tabla de despacho de la clase antes de que los objetos se instancien en memoria; definirlas dentro de `__init__` rompe el enlace interno de C++.

> [!question]- ¿Cómo se consultan las coordenadas del cursor dentro del método `mousePressEvent(event)`?
> Mediante los métodos `event.x()` y `event.y()` (o `event.pos()`), que retornan la posición en píxeles del puntero respecto a la esquina superior izquierda del widget.

> [!question]- ¿Qué método debe llamarse para que `mouseMoveEvent` capture el movimiento del cursor sin que el usuario mantenga presionado un botón?
> Se debe invocar `self.setMouseTracking(True)` sobre el widget o ventana correspondiente.

> [!question]- ¿Qué ocurre cuando una señal definida como `pyqtSignal(int)` invoca `.emit("Hola")`?
> Arroja un error de tipado (`TypeError`) porque el argumento entregado en `.emit()` no coincide con la firma de tipos declarada para la señal.

