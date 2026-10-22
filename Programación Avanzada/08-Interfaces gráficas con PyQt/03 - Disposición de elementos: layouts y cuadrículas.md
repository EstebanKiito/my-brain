---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[02 - Sistema de coordenadas y widgets básicos: etiquetas, entradas y botones]]"
---

# Disposición de elementos: layouts y cuadrículas

El posicionamiento absoluto mediante coordenadas fijas en píxeles no escala: al cambiar la resolución de la pantalla o estirar la ventana con el ratón, los controles quedan apiñados o se desbordan. Los **layouts** resuelven este problema calculando y redistribuyendo automáticamente el tamaño y la posición de los widgets de forma elástica y responsiva.

## Layouts lineales: QHBoxLayout y QVBoxLayout

PyQt provee dos clases principales para ordenar elementos en una sola dimensión:

- **`QHBoxLayout`:** dispone los widgets en una fila **horizontal** de izquierda a derecha.
- **`QVBoxLayout`:** dispone los widgets en una columna **vertical** de arriba hacia abajo.

![Estructura y alineación de layouts](adjuntos/Estructura%20y%20alineaci%C3%B3n%20de%20layouts%20verticales%20y%20horizontales.png)

> [!example]- Transcripción de la imagen
> - Esquema de cajas de layout:
>   - Arriba: disposición horizontal en `QHBoxLayout` alineando elementos en el eje X.
>   - Abajo: disposición vertical en `QVBoxLayout` apilando elementos en el eje Y.

Al combinar ambos layouts mediante anidación (`vbox.addLayout(hbox)`), logramos distribuciones visuales limpias:

| ![Ajuste horizontal](adjuntos/Distribuci%C3%B3n%20de%20widgets%20con%20ajuste%20horizontal%20QHBoxLayout.png) | ![Combinación anidada](adjuntos/Combinaci%C3%B3n%20anidada%20de%20layouts%20horizontal%20y%20vertical.png) |
|---|---|
| (a) Solo `QHBoxLayout` | (b) Anidando `QHBoxLayout` dentro de `QVBoxLayout` |

> [!example]- Transcripción de las imágenes
> - Ventanas con layouts lineales:
>   - (a) Tres etiquetas alineadas horizontalmente ocupando todo el ancho.
>   - (b) Etiquetas dispuestas en dos filas compactas empujadas hacia la parte superior.

## Distribución en cuadrícula: QGridLayout

Cuando necesitamos alinear elementos en filas y columnas regulares (como formularios o calculadoras), utilizamos **`QGridLayout`**:

- `grid.addWidget(widget, fila, columna)`: ubica el widget en la celda $(i, j)$ (índices base 0).
- `grid.addWidget(widget, fila, col, rowSpan, colSpan)`: permite que un widget se expanda ocupando múltiples filas o columnas adyacentes.

| ![Esquema de cuadrícula](adjuntos/Esquema%20de%20distribuci%C3%B3n%20espacial%20en%20QGridLayout.png) | ![Ventana con grid layout](adjuntos/Distribuci%C3%B3n%20de%20widgets%20en%20cuadr%C3%ADcula%20con%20QGridLayout.png) |
|---|---|
| Esquema conceptual (fila, col) | Resultado en ventana |

> [!example]- Transcripción de las imágenes
> - Esquema y resultado de `QGridLayout`:
>   - Izquierda: matriz de celdas indexadas por `(row, col)`.
>   - Derecha: ventana con cuatro botones distribuidos uniformemente en una cuadrícula $2 \times 2$.

## Creación de componentes modulares con POO

En lugar de definir toda la interfaz dentro de una sola clase gigante, la mejor práctica de ingeniería de software consiste en crear clases especializadas que hereden de `QWidget` para encapsular subcomponentes reutilizables:

| ![Botones independientes](adjuntos/Ventana%20con%20botones%20contadores%20independientes%20personalizados.png) | ![Formulario compuesto](adjuntos/Formulario%20compuesto%20modular%20con%20widgets%20y%20layouts.png) |
|---|---|
| Botones modulares con estado propio | Formulario ensamblado con layouts anidados |

> [!example]- Transcripción de las imágenes
> - Componentes modulares:
>   - Izquierda: dos botones personalizados que mantienen su propio conteo de clics independiente.
>   - Derecha: formulario completo con campos de texto, etiquetas y botones alineados elásticamente.

```python
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class FormularioLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acceso al Sistema")

        # 1. Crear widgets
        self.label_user = QLabel("Usuario:")
        self.input_user = QLineEdit()
        self.boton_login = QPushButton("Entrar")

        # 2. Layout horizontal para el campo de usuario
        layout_campo = QHBoxLayout()
        layout_campo.addWidget(self.label_user)
        layout_campo.addWidget(self.input_user)

        # 3. Layout vertical principal
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_campo)
        layout_principal.addStretch()  # Empuja el botón al fondo
        layout_principal.addWidget(self.boton_login)

        # 4. Asignar layout raíz a la ventana
        self.setLayout(layout_principal)
```

> [!tip] Espaciadores elásticos con addStretch()
> Invocar `layout.addStretch()` inserta un resorte invisible que absorbe todo el espacio libre sobrante, empujando a los widgets hacia los bordes de la ventana de forma profesional.

## Preguntas de repaso

> [!question]- ¿Por qué es preferible usar layouts en lugar de posicionar elementos con coordenadas manuales?
> Porque los layouts recalculan dinámicamente las dimensiones y posiciones relativas al redimensionar la ventana o cambiar de monitor, manteniendo una interfaz armónica y legible.

> [!question]- ¿Cuál es la diferencia de distribución entre `QHBoxLayout` y `QVBoxLayout`?
> `QHBoxLayout` ordena los widgets secuencialmente de forma horizontal en una fila (eje X), mientras que `QVBoxLayout` los apila de forma vertical en una columna (eje Y).

> [!question]- ¿Qué representan los parámetros `rowSpan` y `colSpan` en `QGridLayout.addWidget()`?
> Indican la cantidad de filas y columnas consecutivas que el widget abarcará a partir de su celda de origen, permitiendo elementos anchos o altos que cubran varias casillas.

> [!question]- ¿Cómo se inserta un layout secundario dentro de otro layout en PyQt?
> Se utiliza el método `addLayout(layout_hijo)` sobre el layout contenedor padre (por ejemplo `vbox.addLayout(hbox)`).

