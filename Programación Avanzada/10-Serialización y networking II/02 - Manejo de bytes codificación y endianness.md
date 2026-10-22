---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/networking
  - programacion/bytes
  - origen/complemento
prerrequisitos:
  - "[[08 - Archivos, encoding y bytes]]"
---

# Manejo de bytes codificación y endianness

Los cables de red y los adaptadores inalámbricos no comprenden cadenas de texto, listas ni diccionarios de Python: únicamente transmiten pulsos binarios estructurados en **octetos o bytes** (bloques de 8 bits con valores de 0 a 255). Para programar comunicaciones de bajo nivel mediante sockets, es indispensable manipular flujos de bytes y comprender su ordenamiento en memoria.

## Los tipos bytes y bytearray en Python

En Python disponemos de dos estructuras fundamentales para representar secuencias binarias:

- **`bytes`:** secuencia **inmutable** de enteros en el rango $[0, 255]$. Se definen con el prefijo `b` (por ejemplo `datos = b"Hola"`, equivalente a `[72, 111, 108, 97]`).
- **`bytearray`:** versión **mutable** de `bytes`. Permite alterar valores individuales por índice (`ba[0] = 65`) sin tener que crear un nuevo objeto en memoria.

![Tabla de caracteres ASCII](adjuntos/Tabla%20de%20caracteres%20ASCII%20y%20representaci%C3%B3n%20en%20bytes.jpg)

> [!example]- Transcripción de la imagen
> - Tabla histórica de codificación ASCII:
>   - Mapea valores decimales y hexadecimales del 0 al 127 a caracteres de control, dígitos y letras del alfabeto latino.

Para transformar strings a bytes y viceversa usamos **`encode()`** y **`decode()`** indicando la codificación universal **UTF-8**:

$$\text{str} \xrightarrow{\text{.encode('utf-8')}} \text{bytes} \xrightarrow{\text{.decode('utf-8')}} \text{str}$$

## Conversión numérica y el concepto de Endianness

Cuando necesitamos enviar números enteros a través de la red (por ejemplo para indicar el tamaño de un archivo que transferiremos), debemos convertirlos a bytes explícitamente usando **`to_bytes()`** y **`int.from_bytes()`**.

El **Endianness** define el orden en que los bytes de un número multibyte se distribuyen en las direcciones de memoria:

- **Big-endian (orden de red o *network byte order*):** el byte más significativo se almacena al principio (a la izquierda). Es el estándar obligatorio de los protocolos de internet.
- **Little-endian:** el byte menos significativo se almacena al principio. Es el orden natural de los procesadores modernos de arquitectura x86 y ARM.

```python
# El número 1000 en hexadecimal es 0x03E8 (requiere 2 bytes: 03 y E8)
numero = 1000

# Big-endian: primero el más significativo (03) luego el menor (E8)
bytes_red = numero.to_bytes(2, byteorder="big")
print(f"Big-endian (red): {bytes_red}")

# Little-endian: orden invertido (E8 primero)
bytes_local = numero.to_bytes(2, byteorder="little")
print(f"Little-endian:     {bytes_local}")

# Reconstrucción del entero desde bytes
recuperado = int.from_bytes(bytes_red, byteorder="big")
print(f"Entero recuperado: {recuperado}")
```

```
Big-endian (red): b'\x03\xe8'
Little-endian:     b'\xe8\x03'
Entero recuperado: 1000
```

## Procesamiento en trozos (Chunks)

Al transmitir o leer datos de gran tamaño (como un archivo de video de 500 MB), intentar cargarlo completo en una sola variable satura la memoria RAM. La técnica estándar consiste en procesar la información en **trozos o bloques de tamaño fijo** (*chunks*), típicamente de 4096 bytes ($4\text{ KB}$):

```python
CHUNK_SIZE = 4096

def leer_por_bloques(ruta_archivo: str):
    with open(ruta_archivo, "rb") as f:
        while True:
            bloque = f.read(CHUNK_SIZE)
            if not bloque:
                break  # Fin del archivo alcanzado (EOF)
            yield bloque
```

> [!warning] La trampa de mezclar endianness entre emisor y receptor
> Si un cliente envía el tamaño de un mensaje codificado en *big-endian* y el servidor lo decodifica usando *little-endian*, el número interpretado será completamente erróneo (por ejemplo $1000$ (`0x03E8`) se interpretará como $59395$ (`0xE803`)), provocando lecturas desfasadas o caídas del programa.

> [!tip] Estándar de red
> En todas las transmisiones de red a través de sockets, utiliza siempre `byteorder="big"` para cualquier conversión numérica entera.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia de mutabilidad entre el tipo `bytes` y el tipo `bytearray`?
> `bytes` es una secuencia inmutable (sus elementos no pueden modificarse tras su creación), mientras que `bytearray` es mutable y permite alterar bytes directamente por su índice.

> [!question]- ¿Qué significa que un sistema sea *Big-endian* y por qué se le conoce como el orden de red?
> Significa que los bytes de mayor peso o significancia se ubican en las direcciones de memoria más bajas; se le llama orden de red porque los estándares de internet (IETF) fijaron este orden para el envío de paquetes.

> [!question]- ¿Por qué no se debe leer un archivo grande completo con `f.read()` antes de transmitirlo por la red?
> Porque carga todos los megabytes o gigabytes del archivo simultáneamente en la memoria RAM del proceso; procesarlo por *chunks* (bloques de 4096 bytes) mantiene el consumo de memoria constante y bajo.

> [!question]- ¿Qué ocurre si un entero de valor 300 se intenta convertir a bytes mediante `(300).to_bytes(1, byteorder='big')`?
> Python arroja una excepción `OverflowError`, porque un solo byte solo puede almacenar valores entre 0 y 255.
