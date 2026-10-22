---
ramo: "Programación Avanzada"
tema: "PyQt avanzado"
tags:
  - programacion/gui
  - programacion/pyqt
  - programacion/multimedia
  - origen/complemento
prerrequisitos:
  - "[[05 - Eventos de mouse teclado y señales personalizadas]]"
  - "[[01 - Concurrencia en interfaces gráficas: QThread y señales seguras]]"
---

# Control avanzado de teclado con isAutoRepeat y reproducción de audio

Al desarrollar aplicaciones interactivas y videojuegos en PyQt surgen detalles de experiencia de usuario que van más allá del diseño visual básico: cómo evitar que mantener presionada una tecla detone acciones repetidas involuntarias, y cómo ambientar la interfaz con efectos de sonido rápidos y música de fondo sin saturar el sistema.

## El problema de la repetición automática de teclas (AutoRepeat)

A nivel de hardware y sistema operativo, cuando un usuario mantiene presionada una tecla (por ejemplo la barra espaciadora para saltar o disparar), el teclado no emite una sola señal sostenida; en su lugar, genera una **ráfaga continua de pulsaciones repetidas** (*auto-repeat*).

En una ventana de PyQt, esto se traduce en una sucesión veloz de eventos intercalados:

$$\text{keyPress} \longrightarrow \text{keyRelease} \longrightarrow \text{keyPress} \longrightarrow \text{keyRelease} \dots$$

Si tu aplicación incrementa un contador o mueve un personaje en cada `keyPressEvent`, una pulsación continua de medio segundo provocará decenas de saltos o disparos accidentales descontrolados.

### Filtrado con event.isAutoRepeat()

El objeto `QKeyEvent` provee el método **`isAutoRepeat()`**, que retorna `True` si la pulsación actual es un duplicado generado automáticamente por el sistema mientras la tecla sigue físicamente presionada:

```python
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

class VentanaJuego(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Presiona ESPACIO para saltar", self)
        self.saltos = 0

    def keyPressEvent(self, event):
        # Descartar pulsaciones automáticas repetidas por hardware
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_Space:
            self.saltos += 1
            self.label.setText(f"¡Salto genuino ejecutado! Total: {self.saltos}")

    def keyReleaseEvent(self, event):
        # Descartar liberaciones falsas generadas durante la repetición
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_Space:
            print("El jugador soltó físicamente la barra espaciadora.")
```

## Reproducción de audio en PyQt: QSoundEffect frente a QMediaPlayer

Para enriquecer la interfaz con sonido, el submódulo **`PyQt5.QtMultimedia`** ofrece dos herramientas con propósitos bien diferenciados:

```
+--------------------+---------------------------------+---------------------------------+
| Característica     | QSoundEffect                    | QMediaPlayer                    |
+--------------------+---------------------------------+---------------------------------+
| Propósito          | Efectos de sonido cortos        | Pistas largas y música de fondo |
| Formatos ideales   | Audio sin comprimir (.wav)      | Comprimidos (.mp3, .ogg, .wav)  |
| Latencia           | Mínima (precarga en memoria)    | Mayor (decodificación en flujo) |
| Casos de uso       | Clics, disparos, alertas, saltos| Música ambiental, podcasts      |
+--------------------+---------------------------------+---------------------------------+
```

### 1. Efectos de sonido rápidos con QSoundEffect
Carga el archivo de audio directamente en la memoria RAM para reproducirlo con latencia cero en cuanto el usuario presiona un botón:

```python
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSoundEffect

class ReproductorEfectos:
    def __init__(self, ruta_wav: str):
        self.efecto = QSoundEffect()
        # QSoundEffect exige rutas como objetos QUrl locales
        self.efecto.setSource(QUrl.fromLocalFile(ruta_wav))
        self.efecto.setVolume(0.8)  # Rango de 0.0 (mudo) a 1.0 (máximo)

    def sonar(self):
        self.efecto.play()
```

### 2. Música de fondo con QMediaPlayer
Gestiona pistas de audio extensas sin sobrecargar la memoria, permitiendo pausar, reanudar y controlar la posición de reproducción:

```python
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

reproductor_musica = QMediaPlayer()
contenido = QMediaContent(QUrl.fromLocalFile("assets/musica_fondo.mp3"))
reproductor_musica.setMedia(contenido)
reproductor_musica.setVolume(50)  # Rango de 0 a 100
reproductor_musica.play()
```

> [!tip] Sonido en bucle continuo
> En `QSoundEffect`, puedes configurar `efecto.setLoopCount(QSoundEffect.Infinite)` para que el efecto se repita sin cesar hasta que llames a `efecto.stop()` (ideal para sonidos de alarmas continuas o motores).

## Preguntas de repaso

> [!question]- ¿Qué problema causa el fenómeno de *auto-repeat* del teclado en un videojuego interactivo?
> Hace que mantener presionada una tecla dispare ráfagas repetitivas continuas de eventos `keyPressEvent`, provocando acciones descontroladas (múltiples saltos o disparos por segundo).

> [!question]- ¿Cómo se utiliza `event.isAutoRepeat()` para asegurar que una acción se ejecute exactamente una sola vez por pulsación física?
> Se verifica al inicio de `keyPressEvent`: si `event.isAutoRepeat()` retorna `True`, se hace un retorno temprano (`return`) para descartar el evento duplicado.

> [!question]- ¿Por qué se prefiere `QSoundEffect` por sobre `QMediaPlayer` para el sonido de un disparo o botón?
> Porque `QSoundEffect` precarga el audio completo sin comprimir en memoria, ofreciendo una latencia de respuesta inmediata (milisegundos) sin la sobrecarga de decodificación de `QMediaPlayer`.

> [!question]- ¿Cómo deben formatearse las rutas de archivos de audio al asignarlas a un `QSoundEffect`?
> No se pueden entregar como strings planos; deben envolverse en una URL de archivo local mediante `QUrl.fromLocalFile("ruta/al/archivo.wav")`.

