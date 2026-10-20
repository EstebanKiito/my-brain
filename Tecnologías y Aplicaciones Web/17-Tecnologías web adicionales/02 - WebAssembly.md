---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Tecnologías web adicionales"
tags:
  - web
  - webassembly
  - rendimiento
  - origen/complemento
prerrequisitos:
  - "[[01 - Node.js como runtime de JavaScript]]"
---

# WebAssembly

JavaScript es rápido, pero no al nivel de C o C++. Para tareas intensivas, como editar video, correr un motor de juegos o hacer simulaciones, hacía falta otra cosa. **WebAssembly** (wasm) permite ejecutar en el navegador código escrito en C, C++ o Rust a una velocidad cercana a la nativa, y convive con JavaScript.

## Qué es

**WebAssembly** es un formato de **código binario** diseñado para ejecutarse en los navegadores modernos:

- **Es un nuevo lenguaje**: el "cuarto lenguaje de la web", junto con HTML, CSS y JavaScript.
- **Es binario**: no se escribe a mano, sino que es un **objetivo de compilación** (*compilation target*).
- **Es de bajo nivel**: sus instrucciones son cercanas al código de máquina.
- **Es para la web**: está diseñado para complementar las otras tecnologías web.

Lenguajes como C, Rust o Python se **compilan** a este formato y el navegador lo ejecuta de forma eficiente.

## Qué ofrece

- **Eficiencia**: es un formato para una máquina virtual basada en pila y un objetivo portable para compiladores de C, C++ y Rust.
- **Cliente y servidor**: corre en el navegador a velocidad casi nativa, y con **WASI** también fuera del navegador.
- **Seguridad**: se ejecuta en un *sandbox*, igual que JavaScript, y sus módulos se cargan desde JS.
- **Estándar**: lo desarrolla el W3C WebAssembly Working Group y lo soportan los navegadores modernos.

Por eso importa: paquetes más pequeños y ejecución más rápida, reutilización de código existente en C o C++, módulos de distintos lenguajes que interoperan, y la misma ejecución en cualquier sistema operativo o navegador.

## Cómo funciona

1. Se escribe el código en un lenguaje de alto nivel.
2. Se compila a **bytecode** de WebAssembly.
3. El navegador lo ejecuta, más rápido de cargar y de correr, y aislado como JavaScript.

![Compilación de C a WebAssembly con Emscripten](adjuntos/Compilaci%C3%B3n%20de%20C%20a%20WebAssembly%20con%20Emscripten.png)

> [!example]- Transcripción de la imagen
> *C/C++ source code* → **Emscripten** → *wasm module* + *HTML document* con *JS "glue" code*.

```c
#include <stdio.h>

int main() {
  printf("hello, world!\n");
  return 0;
}
```

Compilado con **Emscripten**, ese programa se convierte en un archivo `.wasm` binario (bytes como `0061 736d 0100…`, donde `0061 736d` es la firma `\0asm`). Ese binario tiene una representación textual legible, el **WAT** (*WebAssembly Text*), con instrucciones de pila como `local.get`, `i32.const` e `i32.sub`.

Además, el navegador hace **compilación en streaming**: empieza a compilar el módulo mientras todavía lo está descargando, sin esperar a tenerlo completo.

## Herramientas

| Herramienta | Uso |
|---|---|
| **Emscripten** | Compila C y C++ a wasm |
| **Rust** + `wasm-pack` | Compila Rust a wasm (`wasm-pack build --target web`) |
| **AssemblyScript** | Un lenguaje parecido a TypeScript que compila a wasm; se instala con npm |
| **wabt** | Herramientas de línea de comandos para convertir y examinar wasm y WAT |

Emscripten tiene tres modos, según lo que se quiere generar:

- `emcc archivo.c -o salida.html`: el módulo wasm, el JS de conexión y una página HTML de prueba. Sirve para prototipos.
- `emcc archivo.c -o salida.js`: el módulo y el JS de conexión, para integrarlo en un proyecto.
- `emcc archivo.c -o salida.wasm --no-entry`: solo el módulo, para escenarios avanzados.

> [!warning] El `.wasm` necesita un servidor
> El navegador debe recibir el archivo con el tipo `application/wasm`. Abrir el HTML directamente desde el disco no funciona; basta un servidor local como `python -m http.server`.

## No reemplaza a JavaScript

JavaScript es de alto nivel, flexible y tiene un ecosistema enorme. Ya es lo bastante rápido para la mayoría de los casos, y es el que interactúa con el DOM: de hecho, se usa para **cargar** los módulos wasm. WebAssembly se reserva para las partes que necesitan rendimiento cercano al nativo.

Casos de uso: aplicaciones de alto rendimiento (simulaciones, gráficos), multimedia, encriptación, intérpretes y máquinas virtuales, y portar código existente. Ejemplos conocidos son TensorFlow.js (hasta 10 veces más rápido que JS puro), los juegos de Unity exportados a la web, AutoCAD (más de 35 años de código en C/C++ llevados al navegador) y Google Earth. Aun así, su adopción no ha sido tan masiva como se esperaba.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que WebAssembly es un "compilation target"?
> Porque no está pensado para escribirse a mano: es el formato al que se compila código de otros lenguajes (C, C++, Rust), como el código de máquina lo es para un compilador tradicional.

> [!question]- Si WebAssembly es más rápido, ¿por qué no reemplaza a JavaScript?
> Porque JavaScript ya es suficientemente rápido para la mayoría de las tareas, es mucho más flexible y es el que maneja el DOM. Wasm complementa a JS en las partes que necesitan más rendimiento.

> [!question]- ¿Qué gana el navegador con la compilación en streaming?
> Empieza a compilar el módulo mientras se descarga, así que el código queda listo para ejecutarse antes que si esperara la descarga completa.
