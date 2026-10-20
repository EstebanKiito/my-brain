---
ramo: "Sistemas Distribuidos"
tema: "Procesos e hilos en Python"
tags:
  - sd/procesos-e-hilos
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - Procesos y comunicación entre procesos]]"
---

# Procesos en Python con multiprocessing y subprocess

Un programa de Python es un proceso, pero puede crear otros. La biblioteca estándar ofrece dos caminos: `multiprocessing`, que lanza una función de Python en un proceso hijo, y `subprocess`, que ejecuta un programa externo como si se escribiera en la terminal. En los sistemas distribuidos del curso se usan para levantar varios nodos en una misma máquina.

## multiprocessing: una función en otro proceso

![Crear un proceso con multiprocessing](adjuntos/Crear%20un%20proceso%20con%20multiprocessing.png)

> [!example]- Transcripción de la imagen
> ```python
> from multiprocessing import Process
> import os
>
>
> def saludar():
>     print("Waku Waku")
>     print("PID del otro proceso:", os.getpid())
>
>
> if __name__ == "__main__":
>     print("PID del proceso actual:", os.getpid())
>     p = Process(target=saludar)
>     p.start()
> ```

Al ejecutarlo, los dos PID son distintos porque `saludar` corre en un proceso nuevo, con su propia memoria:

```text
PID del proceso actual: 67150
Waku Waku
PID del otro proceso: 67152
```

- `Process(target=...)` prepara el proceso hijo; `start()` lo lanza.
- El `if __name__ == "__main__"` es obligatorio: en macOS y Windows el hijo vuelve a importar el módulo, y sin esa guarda crearía procesos sin fin.
- No usa la terminal: Python crea el "mini proceso" por sí mismo.

## subprocess: ejecutar otro programa

`subprocess` lanza un comando externo, por ejemplo otro script. Hay dos formas según si el programa principal **espera** o no.

![Ejecutar un script con subprocess.run](adjuntos/Ejecutar%20un%20script%20con%20subprocess.run.png)

> [!example]- Transcripción de la imagen
> ```python
> import subprocess
>
> # Asumimos que otro_script.py existe en el mismo directorio
> # Run espera a que el script termine antes de continuar
> subprocess.run(["python3", "otro_script.py"])
>
> print("Script ejecutado correctamente.")
> ```

`run` **bloquea**: el `print` final aparece solo cuando `otro_script.py` terminó. Funciona como un *join* sobre el proceso hijo.

![Lanzar un script con subprocess.Popen](adjuntos/Lanzar%20un%20script%20con%20subprocess.Popen.png)

> [!example]- Transcripción de la imagen
> ```python
> import subprocess
>
> # Asumimos que otro_script.py existe en el mismo directorio
> # Popen no espera a que el script termine antes de continuar
> # stdout=subprocess.PIPE es para capturar los print del proceso
> # stderr=subprocess.PIPE es para capturar los errores del proceso
> process = subprocess.Popen(["python3", "otro_script.py", "4444", "localhost"],
>                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>
> print("Script ejecutandose correctamente.")
> ```

`Popen` **no espera**: el script hijo y el principal avanzan en paralelo. Los argumentos extra (`"4444"`, `"localhost"`) llegan al hijo en `sys.argv`, lo que sirve para levantar varios nodos con puertos distintos. Con `PIPE` la salida del hijo queda capturada en vez de imprimirse; se lee con `communicate()`, que además espera a que termine:

```python
salida, errores = process.communicate()
print(salida.decode().strip())   # otro_script recibió: ['4444', 'localhost']
```

| Herramienta | Qué ejecuta | ¿Espera al hijo? |
|---|---|---|
| `multiprocessing.Process` + `start()` | Una función de Python | No (se espera con `p.join()`) |
| `subprocess.run` | Un programa externo | Sí |
| `subprocess.Popen` | Un programa externo | No (se espera con `wait()` o `communicate()`) |

> [!warning] Capturar la salida sin leerla
> Si se usa `stdout=subprocess.PIPE` y nunca se lee, un hijo que imprime mucho puede llenar el buffer del pipe y quedarse bloqueado. Por eso se usa `communicate()` en vez de un `wait()` a secas.

La versión en C de estas ideas (`fork`, `exec`, `wait`) está en [[06 - Control de procesos con wait, exec y terminación|Control de procesos con wait, exec y terminación]].

## Preguntas de repaso

> [!question]- ¿Por qué los dos PID del ejemplo de `multiprocessing` son distintos?
> Porque `Process` crea un proceso nuevo, con su propio PID y su propia memoria. `saludar` no se ejecuta en el proceso original sino en el hijo.

> [!question]- Para levantar tres nodos que deben correr al mismo tiempo, ¿conviene `subprocess.run` o `Popen`?
> `Popen`, porque no espera a que el hijo termine. Con `run` el segundo nodo recién partiría cuando el primero muriera.

> [!question]- ¿Para qué sirve pasar `"4444"` y `"localhost"` como argumentos al script hijo?
> Para configurar cada proceso al lanzarlo, por ejemplo el puerto y el host donde escuchará. El hijo los lee desde `sys.argv`.
