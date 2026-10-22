---
ramo: "Programación Avanzada"
tema: "Interfaces gráficas con PyQt"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de interfaces gráficas y ciclo de vida en PyQt]]"
---

# Sistema de coordenadas y widgets básicos: etiquetas, entradas y botones

Una interfaz gráfica está compuesta por múltiples elementos visuales interactivos denominados **widgets** (*window gadgets*). Para ubicar y configurar estos componentes dentro de una ventana, es necesario dominar el sistema de coordenadas de PyQt y sus clases fundamentales.

## Sistema de coordenadas en PyQt

A diferencia del plano cartesiano tradicional de las matemáticas, en los sistemas gráficos de ventanas:

- El punto de origen **$(0, 0)$** se ubica en la **esquina superior izquierda** de la ventana.
- Las coordenadas en el eje **$X$** crecen hacia la **derecha**.
- Las coordenadas en el eje **$Y$** crecen hacia **abajo**.

![Sistema de coordenadas bidimensional en PyQt](adjuntos/Sistema%20de%20coordenadas%20bidimensional%20en%20PyQt.png)

> [!example]- Transcripción de la imagen
> - Esquema de coordenadas en PyQt:
>   - Origen $(0,0)$ en el vértice superior izquierdo.
>   - Ancho (*width*) medido sobre el eje horizontal $X$.
>   - Alto (*height*) medido sobre el eje vertical $Y$ descendente.

## Widgets fundamentales

Todo widget secundario debe recibir como argumento a su widget contenedor padre (generalmente `self` dentro de la clase de la ventana).

### 1. Etiquetas de texto e imágenes (QLabel)
Muestra textos estáticos, indicaciones o imágenes que el usuario no puede editar directamente.

![Ventana con etiquetas de texto en PyQt](adjuntos/Ventana%20con%20etiquetas%20de%20texto%20en%20PyQt.png)

> [!example]- Transcripción de la imagen
> - Ventana con dos etiquetas de texto: una etiqueta superior que dice *"Ingresa tu nombre:"* y una inferior que muestra el estado actual.

Para desplegar una imagen en disco, se utiliza la clase **`QPixmap`** del módulo `PyQt5.QtGui`:

```python
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

etiqueta_foto = QLabel(self)
pixmap = QPixmap("assets/logo.png")
etiqueta_foto.setPixmap(pixmap)
```

![Visualización de imagen en QLabel con QPixmap](adjuntos/Visualizaci%C3%B3n%20de%20imagen%20en%20QLabel%20con%20QPixmap.png)

> [!example]- Transcripción de la imagen
> - Ventana gráfica que muestra el logotipo de Python centrado dentro de una etiqueta `QLabel`.

### 2. Cuadro de texto interactivo (QLineEdit)
Permite al usuario ingresar y editar una línea de texto plano:

- `self.input_nombre.text()`: obtiene el string actual escrito por el usuario.
- `self.input_nombre.setText("Nuevo texto")`: asigna contenido al campo.
- `self.input_nombre.setPlaceholderText("Escribe aquí...")`: define texto de ayuda temporal en gris.

### 3. Botones de comando (QPushButton)
Representa un botón clásico sobre el cual el usuario puede hacer clic para detonar una acción:

![Ventana básica con botón QPushButton](adjuntos/Ventana%20b%C3%A1sica%20con%20bot%C3%B3n%20QPushButton.png)

> [!example]- Transcripción de la imagen
> - Ventana con un botón gris centrado con el texto *"Mi Botón"*.

### Ensamblaje con posicionamiento absoluto

```python
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario de Registro")
        self.setGeometry(100, 100, 320, 180)

        # Posicionamiento absoluto manual: move(x, y)
        self.label_titulo = QLabel("Nombre de usuario:", self)
        self.label_titulo.move(20, 20)

        self.input_usuario = QLineEdit(self)
        self.input_usuario.setPlaceholderText("Ej: esteban123")
        self.input_usuario.setGeometry(20, 50, 280, 30)

        self.boton_enviar = QPushButton("Registrar", self)
        self.boton_enviar.setGeometry(20, 100, 120, 35)
```

> [!warning] La limitación del posicionamiento absoluto con move()
> Ubicar widgets fijando píxeles exactos (`move` o `setGeometry`) es frágil: si el usuario redimensiona la ventana, los elementos no se adaptan, se solapan o quedan ocultos fuera del marco visible. Para interfaces adaptables y responsivas se deben usar **Layouts**.

> [!tip] Ajustar tamaño de etiquetas automáticamente
> Después de cambiar el texto de un `QLabel` con `setText()`, llama a `etiqueta.adjustSize()` para que el recuadro del widget se expanda o contraiga al tamaño exacto del nuevo string sin cortar palabras.

## Preguntas de repaso

> [!question]- ¿Hacia qué dirección crecen las coordenadas del eje Y en PyQt y dónde se ubica el punto (0, 0)?
> El punto $(0, 0)$ está en la esquina superior izquierda de la ventana y el eje Y crece de forma positiva en dirección descendente hacia el borde inferior.

> [!question]- ¿Por qué se debe pasar `self` como segundo argumento al instanciar un widget (`QLabel("Texto", self)`)?
> Para establecer la relación de paternidad en Qt: el widget queda subordinado a esa ventana, se muestra dentro de ella y se destruye automáticamente cuando la ventana se cierra.

> [!question]- ¿Cómo se carga y visualiza una imagen en disco dentro de una interfaz de PyQt?
> Se crea un objeto `QPixmap` indicando la ruta del archivo de imagen y se asigna a un widget `QLabel` mediante su método `setPixmap(pixmap)`.

> [!question]- ¿Cuál es la principal desventaja de organizar una ventana usando únicamente `move(x, y)`?
> La interfaz no es responsiva: si la ventana cambia de tamaño o se ejecuta en una pantalla con distinta resolución o densidad de píxeles, los widgets quedan desalineados o cortados.
