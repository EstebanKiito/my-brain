---
ramo: "Programación Avanzada"
tema: "PyQt avanzado"
tags:
  - programacion/gui
  - programacion/pyqt
  - origen/complemento
prerrequisitos:
  - "[[01 - Fundamentos de interfaces gráficas y ciclo de vida en PyQt]]"
  - "[[03 - Disposición de elementos: layouts y cuadrículas]]"
---

# Estructura de ventanas completas con QMainWindow menús y barras

Mientras que `QWidget` ofrece un lienzo en blanco básico sobre el cual montar componentes, las aplicaciones de escritorio tradicionales (editores de texto, navegadores, entornos de desarrollo) siguen un diseño ergonómico estandarizado con barras de menú superiores, barras de herramientas con accesos directos, un área de trabajo central y una barra de estado inferior. En PyQt, esta arquitectura la provee **`QMainWindow`**.

## Arquitectura visual de QMainWindow

`QMainWindow` hereda de `QWidget` pero añade una disposición espacial fija prediseñada:

![Estructura de componentes en QMainWindow](adjuntos/Estructura%20de%20componentes%20en%20QMainWindow.png)

> [!example]- Transcripción de la imagen
> - Esquema de áreas de `QMainWindow`:
>   - Arriba: Barra de Menú (*Menu Bar*) y Barras de Herramientas (*Toolbars*).
>   - Laterales: Paneles acoplables o flotantes (*Dock Widgets*).
>   - Centro: Widget Central único (*Central Widget*).
>   - Abajo: Barra de Estado (*Status Bar*).

![Aspecto de QMainWindow en macOS](adjuntos/Aspecto%20de%20QMainWindow%20con%20men%C3%BAs%20y%20barras%20en%20macOS.png)

> [!example]- Transcripción de la imagen
> - Renderizado nativo en macOS:
>   - La barra de menús se integra automáticamente en la barra superior del sistema operativo, mientras las barras de herramientas y el widget central permanecen dentro del marco de la ventana.

## Los cuatro componentes esenciales

### 1. El Widget Central (setCentralWidget)
En `QMainWindow` no se aplica un layout directamente sobre la ventana. En su lugar, se debe definir un **único widget central** mediante `self.setCentralWidget(widget)`. Si requieres varios controles, crea un contenedor `QWidget`, asígnale un layout y fíjalo como widget central.

### 2. Barra de Menú y Acciones (QAction)
Una acción (**`QAction`**) representa un comando unificado que puede detonarse desde el menú, una barra de herramientas o mediante un atajo de teclado:

```python
from PyQt5.QtWidgets import QAction

accion_guardar = QAction("&Guardar", self)
accion_guardar.setShortcut("Ctrl+S")
accion_guardar.setStatusTip("Guardar cambios en el archivo")
accion_guardar.triggered.connect(self.guardar_archivo)
```

La señal emitida al seleccionar una acción es **`triggered`**.

### 3. Barra de Herramientas (Tool Bar)
Se añade con `self.addToolBar("Nombre")` y permite anclar botones rápidos reutilizando las mismas instancias de `QAction`.

### 4. Barra de Estado (Status Bar)
Ubicada en el borde inferior de la ventana, despliega mensajes temporales al usuario:

```python
self.statusBar().showMessage("Archivo cargado exitosamente", 3000)  # Visible por 3 s
```

## Ejemplo integrado de ventana profesional

```python
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Editor de Texto")
        self.setGeometry(100, 100, 600, 400)

        # 1. Widget central: editor de texto enriquecido
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)

        # 2. Definir acción reutilizable con atajo
        accion_limpiar = QAction("&Limpiar", self)
        accion_limpiar.setShortcut("Ctrl+L")
        accion_limpiar.triggered.connect(self.editor.clear)

        # 3. Incorporar acción a la barra de menú
        menu_archivo = self.menuBar().addMenu("&Archivo")
        menu_archivo.addAction(accion_limpiar)

        # 4. Incorporar acción a la barra de herramientas
        barra_herramientas = self.addToolBar("Herramientas")
        barra_herramientas.addAction(accion_limpiar)

        # 5. Notificación inicial en la barra de estado
        self.statusBar().showMessage("Listo para escribir", 4000)
```

> [!warning] QMainWindow solo admite un widget central
> Intentar invocar `self.setLayout(vbox)` sobre una instancia de `QMainWindow` arrojará una advertencia o error en PyQt. Siempre asigna el layout a un `QWidget` intermedio y pásalo con `self.setCentralWidget()`.

> [!tip] Mnemónicos con el carácter &
> Escribir `&Archivo` en el nombre de un menú subraya automáticamente la primera letra (`A`) en sistemas Windows y Linux, permitiendo al usuario desplegar el menú presionando `Alt+A` desde el teclado.

## Preguntas de repaso

> [!question]- ¿Por qué no se debe llamar a `self.setLayout()` directamente sobre una instancia de `QMainWindow`?
> Porque `QMainWindow` ya posee su propio layout interno fijo reservado para gestionar barras de menú, barras de herramientas y barras de estado; los layouts de contenido deben aplicarse sobre el `centralWidget`.

> [!question]- ¿Cuál es la ventaja de utilizar objetos `QAction` en lugar de botones normales para los comandos de la aplicación?
> Permite reutilizar la misma acción lógica simultáneamente en la barra de menús, en las barras de herramientas y vinculada a un atajo de teclado (*shortcut*), compartiendo el mismo texto, icono y slot.

> [!question]- ¿Qué señal se emite cuando el usuario activa una opción de menú asociada a una `QAction`?
> La señal `triggered`, la cual se conecta a la función correspondiente con `accion.triggered.connect(slot)`.

> [!question]- ¿Cómo se muestra un mensaje informativo que desaparezca automáticamente tras 5 segundos en la barra inferior?
> Mediante la llamada `self.statusBar().showMessage("Texto informativo", 5000)`, indicando el tiempo de expiración en milisegundos como segundo parámetro.

