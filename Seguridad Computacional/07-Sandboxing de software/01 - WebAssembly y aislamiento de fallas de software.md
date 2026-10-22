---
ramo: "Seguridad Computacional"
tema: "Sandboxing de software"
tags:
  - seguridad/aislamiento
  - web
  - origen/complemento
prerrequisitos:
  - "[[02 - Firecracker y aislamiento con microVMs]]"
---

# WebAssembly y aislamiento de fallas de software

Los navegadores necesitan ejecutar código rápido y no confiable (de otros lenguajes, de alto rendimiento) sin que toque datos de otros sitios ni del usuario. Los mecanismos anteriores no sirven: `chroot` y contenedores exigen root o configuración previa, y Firecracker solo corre en Linux. El **aislamiento de fallas de software** (*Software Fault Isolation*, SFI) no depende del hardware ni del SO ni de privilegios, pero exige cooperación: no se puede aislar un binario cualquiera, sino código compilado para ello.

## La idea de SFI y su versión moderna
SFI inserta comprobaciones en cada acceso a memoria, restringe las llamadas al sistema, impone un flujo de control seguro y encierra módulos no confiables. **WebAssembly** (Wasm) es un SFI moderno, que corre en el navegador o por línea de comandos (`wasmtime`).

![SFI y su aplicación en WebAssembly](adjuntos/SFI%20y%20su%20aplicaci%C3%B3n%20en%20WebAssembly.png)

> [!example]- Transcripción de la imagen
> Dos columnas con flechas: SFI → Wasm. "Insertar comprobaciones de acceso a memoria" → "comprueba los límites de cada carga y almacenamiento"; "restringir syscalls inseguras" → "sin syscalls, solo importaciones que da el anfitrión"; "imponer flujo de control seguro" → "flujo de control estructurado y llamadas indirectas validadas"; "encerrar módulos no confiables" → "módulos aislados en el navegador o runtime".

Un módulo define funciones, globales, tablas (destinos de punteros a función), una memoria contigua de 0 a `sz` y sus importaciones y exportaciones. Flujo: código C → compilador a Wasm → **validador** (verifica tipos) → intérprete o compilador a código nativo.

## Por qué Wasm sí y x86 no
Aislar x86 nativo es difícil: no se sabe qué direcciones se accederán ni a dónde saltará el código, y con instrucciones de longitud variable ni siquiera se detectan los `syscall`. El diseño de Wasm permite traducir casi uno a uno a código nativo y comprobar:
- **Estado:** globales y locales se verifican en compilación (su cantidad es constante); en el stack se conoce la profundidad en cada instrucción gracias al flujo de control estructurado. Para la memoria, cada `store` se comprueba (`if a+8 >= memsz { panic }`) y se aprovecha la memoria virtual: se reservan 8 GB (dirección de 32 bits más offset de 32 bits) y un acceso fuera de rango causa un fallo de página.
- **Flujo de control (CFI):** los saltos directos van solo a código traducido; los tipos de función garantizan que se pasen los argumentos correctos (si no, la función leería otras posiciones del stack, quizá una dirección de retorno); `call_indirect` solo salta a funciones válidas de la tabla.

> [!warning] Aislamiento no es seguridad de memoria
> Un programa C compilado a Wasm puede tener un buffer overflow dentro de su memoria; Wasm solo garantiza que no afectará al resto del sistema.

## Uso y riesgos
Lo usan todos los navegadores (Photoshop en la web) y servidores de borde (Fastly, Cloudflare), con arranque de bajo overhead; WASI define la interfaz con el sistema. El compilador es parte de la TCB: un error en un compilador (un valor de 32 bits restaurado con extensión de signo, que hacía restar de la base de memoria) rompió el sandbox. Se reduce la TCB con un **verificador** pequeño del binario (VeriWasm).

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene SFI frente a contenedores y VM?
> No necesita privilegios, ni soporte de hardware o del SO, ni configuración del administrador, y los cambios de contexto son más baratos; la desventaja es que exige compilar el código para el sandbox.

> [!question]- ¿Para qué sirve el flujo de control estructurado de Wasm?
> Permite conocer en compilación la profundidad del stack y las posiciones de locales, de modo que los accesos se verifican sin comprobaciones dinámicas y los saltos solo van a destinos válidos.

> [!question]- Si Wasm aísla el módulo, ¿por qué un overflow dentro de él es un problema?
> Porque no protege al propio programa: puede comportarse mal o ser manipulado dentro de su sandbox, aunque no pueda salir de él.
