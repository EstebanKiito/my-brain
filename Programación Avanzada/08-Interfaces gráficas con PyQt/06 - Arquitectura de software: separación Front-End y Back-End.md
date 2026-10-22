---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/patrones-de-diseno
  - origen/complemento
prerrequisitos:
  - "[[04 - Eventos y señales: el mecanismo Signals and Slots]]"
  - "[[05 - Eventos de mouse teclado y señales personalizadas]]"
---

# Arquitectura de software: separación Front-End y Back-End

En programas pequeños es tentador colocar la lógica del negocio, las reglas del juego y el cálculo de datos dentro de los mismos métodos de la ventana gráfica. Sin embargo, a medida que la aplicación crece, mezclar interfaz con lógica convierte el código en un monolito inmanejable, imposible de testear y frágil ante cualquier cambio.

## Cohesión y acoplamiento en interfaces gráficas

El buen diseño de software persigue dos metas arquitectónicas:

- **Alta cohesión (*High Cohesion*):** cada clase debe tener una responsabilidad única y claramente delimitada.
- **Bajo acoplamiento (*Low Coupling*):** los componentes deben depender lo mínimo posible unos de otros, de modo que modificar o reemplazar uno no rompa al resto.

Para lograrlo, dividimos el programa en dos capas conceptuales:

- **Front-End (Capa de Presentación):** gestiona widgets, botones, formularios, eventos de pantalla y despliegue visual. **No toma decisiones de negocio ni realiza cálculos pesados**.
- **Back-End (Capa de Lógica):** almacena el estado del modelo, valida reglas, procesa información y realiza cálculos. **No conoce widgets ni importa clases gráficas de PyQt**.

## Evolución del diseño: de monolito a señales

La interacción entre ambas capas suele evolucionar en tres etapas de diseño:

```
+-----------+-------------------------+-------------------------+----------------------------------+
| Versión   | Cohesión                | Acoplamiento            | Problema principal               |
+-----------+-------------------------+-------------------------+----------------------------------+
| V1: Monolito | Muy baja (hace todo) | N/A (una sola clase)    | Código espagueti e intraducible  |
| V2: Referencia | Media (separa clases) | Muy alto (se conocen)   | Back modifica widgets directo    |
| V3: Señales  | Alta (roles claros)   | Muy bajo (independientes)| Arquitectura modular y testeable|
+-----------+-------------------------+-------------------------+----------------------------------+
```

### La arquitectura desacoplada con pyqtSignal (V3)

En la solución profesional, **ni el Front conoce al Back, ni el Back conoce al Front**. Ambos se comunican exclusivamente a través de señales:

```python
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

# 1. BACK-END: Lógica pura, hereda de QObject para tener señales
class ProcesadorCalculo(QObject):
    senal_resultado = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.acumulado = 0

    def sumar_valor(self, cantidad: int):
        self.acumulado += cantidad
        # Emite el resultado sin saber quién o cómo se mostrará
        self.senal_resultado.emit(self.acumulado)

# 2. FRONT-END: Solo visualización y emisión de eventos de usuario
class VentanaVisual(QWidget):
    senal_solicitar_suma = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.label = QLabel("Total: 0")
        self.btn = QPushButton("Sumar 5")
        self.btn.clicked.connect(self.notificar_clic)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def notificar_clic(self):
        self.senal_solicitar_suma.emit(5)

    def mostrar_total(self, nuevo_total: int):
        self.label.setText(f"Total: {nuevo_total}")
```

### Coordinación en el punto de entrada (main.py)

El archivo principal orquesta la aplicación conectando las señales de ambas capas como un puente:

```python
# Conexión simétrica: Front -> Back y Back -> Front
front.senal_solicitar_suma.connect(back.sumar_valor)
back.senal_resultado.connect(front.mostrar_total)
```

> [!warning] El Back-End nunca debe importar QtWidgets
> Si tu archivo `backend.py` contiene `from PyQt5.QtWidgets import QLabel` o intenta llamar a `.setText()` sobre un widget, el acoplamiento es defectuoso. El Back-End solo debe conocer datos primitivos de Python y emitir señales.

> [!tip] Facilidad de prueba unitaria
> Una gran ventaja de esta separación es que puedes probar todo el Back-End con pruebas automáticas sin necesidad de abrir ventanas gráficas ni simular clics de ratón.

## Preguntas de repaso

> [!question]- ¿Por qué una arquitectura con alto acoplamiento entre Front y Back dificulta el mantenimiento?
> Porque cualquier cambio en la interfaz gráfica (como renombrar una etiqueta o cambiar un campo de texto) obligaría a modificar el código de la lógica del negocio en el Back-End.

> [!question]- ¿Cómo se logra que el Back-End notifique cambios al Front-End sin tener una referencia directa a la ventana?
> El Back-End emite una instancia de `pyqtSignal` con los datos calculados, y el programa principal conecta esa señal al método actualizador de la interfaz en el Front-End.

> [!question]- ¿Por qué el Back-End debe heredar de `QObject` en lugar de `QWidget`?
> Porque `QObject` es la clase mínima que provee el sistema de señales y slots de Qt sin cargar con toda la sobrecarga de ventanas, geometrías y renderizado gráfico que añade `QWidget`.

> [!question]- ¿Cuál es la única responsabilidad que debe tener el Front-End al recibir la interacción de un usuario?
> Capturar el evento visual (como el clic o texto ingresado) y emitir una señal personalizada con los parámetros necesarios hacia el Back-End.

