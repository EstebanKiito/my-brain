---
ramo: "Seguridad Computacional"
tema: "Sandboxing de software"
tags:
  - seguridad/aislamiento
  - web
  - origen/complemento
prerrequisitos:
  - "[[01 - WebAssembly y aislamiento de fallas de software]]"
---

# Sandboxing de bibliotecas con RLBox

Las aplicaciones grandes (como Firefox) usan bibliotecas con errores: códecs de imagen y video, fuentes, descompresión. Aislarlas es posible (procesos, Wasm); lo difícil es la **interfaz** entre la aplicación y la biblioteca, que no se diseñó para ser no confiable. **RLBox** es un marco que ayuda a sandboxear bibliotecas de forma segura.

## Por qué sandboxear dentro del navegador
Cada pestaña ya tiene su proceso, y el aislamiento de sitio da un proceso por dominio. Pero una imagen maliciosa enviada a `google.com` (adjunto, Maps) se decodifica con una biblioteca vulnerable dentro de ese proceso y puede leer sus cookies. Un proceso único para todos los códecs tampoco basta: un códec comprometido podría usar la biblioteca gzip para producir JavaScript arbitrario en la página. Por eso se añade otro nivel de separación dentro del renderer, aprovechando que estas bibliotecas son casi funciones puras (datos entran, datos salen). Crear un sandbox cuesta 1-2 ms, así que se agrupan por `<renderer, biblioteca, origen, tipo de contenido>`.

## Errores típicos en la interfaz
- **Datos de la biblioteca sin validar:** pide saltar N bytes, y N fuera de rango provoca lecturas o escrituras fuera de límites en la app. También códigos de error inesperados.
- **Punteros:** las memorias de app y sandbox son distintas; hay que copiar, no pasar punteros. Pasar uno puede filtrar información de ASLR.
- **Doble lectura (*double-fetch*):** la app valida un campo compartido y lo vuelve a leer; la biblioteca lo cambió entre ambas (condición de carrera).
- **Callbacks:** la biblioteca podría llamar a cualquier función, con argumentos arbitrarios, en momentos o hilos inesperados.

## Mecanismos de RLBox
| Mecanismo | Qué hace |
|---|---|
| Valores **tainted** | Todo lo que sale del sandbox viene marcado como no confiable; no se usa como valor normal hasta validarlo. Los operadores mantienen la marca |
| **Validador** | `copy_and_verify` o `verify` comprueban el valor con una función específica de la aplicación (por ejemplo, ancho entre 1 y 9999) y recién entonces lo desenvuelven |
| Punteros tainted | Apuntan a memoria del sandbox; la memoria se copia explícitamente |
| **Congelamiento** | Una estructura se copia a una instantánea fuera del sandbox para evitar el doble-fetch |
| Callbacks | Se registran con `register_callback`, exigen argumentos tainted y se invocan a través de una función trampolín que comprueba que el destino es válido |

```cpp
tainted<int> t_width = sandbox_invoke(jpeg_sbx, get_width);
int safe_width = t_width.copy_and_verify([](int w) {
    return (w > 0 && w < 10000) ? w : 0;
});
```

## Resultados
Sandboxear una biblioteca toma de 1 a 3 días-persona y unos cientos de líneas; lo más difícil son los validadores, que exigen entender app y biblioteca. El overhead de CPU es modesto (3 % con SFI/NaCl, 13 % con procesos), aunque ciertas cargas sufren (27 % o 85 % de menos rendimiento en código intensivo o con muchos cruces de frontera). Se usa en producción en Firefox. Los mismos problemas aparecen en RPC entre servicios y con kernels no confiables.

## Preguntas de repaso

> [!question]- ¿Por qué no basta con un solo sandbox para todas las bibliotecas?
> Porque las bibliotecas comprometidas se pueden encadenar: una puede producir datos que otra, de mayor confianza (como el renderer), ejecuta; además un solo compromiso afectaría a todas.

> [!question]- ¿Qué problema resuelve el tipo `tainted`?
> Obliga, desde el compilador, a validar explícitamente cualquier dato que cruce desde el sandbox antes de usarlo, evitando olvidar comprobaciones.

> [!question]- ¿Qué es un error de doble-fetch y cómo se evita?
> Leer dos veces un dato compartido que la biblioteca puede modificar entre lecturas (comprobar y usar valores distintos); se evita copiando una instantánea (congelando) antes de validar.
