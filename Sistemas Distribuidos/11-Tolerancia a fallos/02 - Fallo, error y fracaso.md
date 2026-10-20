---
ramo: "Sistemas Distribuidos"
tema: "Tolerancia a fallos"
tags:
  - sd/tolerancia-a-fallos
  - origen/complemento
prerrequisitos:
  - "[[01 - Confiabilidad y sus propiedades]]"
---

# Fallo, error y fracaso

En el lenguaje cotidiano "falla", "error" y "fracaso" se usan como sinónimos, pero en tolerancia a fallos describen tres eslabones distintos de una misma cadena. Separarlos permite decidir **dónde** intervenir: el objetivo es atrapar los errores antes de que se conviertan en fracasos.

## La cadena de causalidad

$$\text{Fallo (fault)} \rightarrow \text{Error} \rightarrow \text{Fracaso (failure)}$$

- **Fallo:** la **causa** del error. Puede ser un defecto de hardware, de software o un error humano.
- **Error:** la **manifestación interna** del fallo en el sistema; es lo que no está ocurriendo como debería. Es el punto donde se ataca para evitar el fracaso.
- **Fracaso:** el **instante** en que el sistema no puede cumplir sus promesas; el servicio no se entrega como se esperaba.

Ejemplo: un programa espera un entero y recibe un string (**fallo**); no puede procesar el dato (**error**); la operación no se ejecuta y el usuario no obtiene el resultado (**fracaso**).

> [!tip] Un error no siempre termina en fracaso
> Si el sistema tiene mecanismos para tolerar la falla (servidores de respaldo, algoritmos que terminan aunque caiga un nodo), el error queda contenido y el usuario no nota nada. **Tolerancia a fallos** es exactamente eso: entregar el servicio aun con uno o más fallos, sin llegar nunca al fracaso.

## Tipos de fallos según su ocurrencia

| Tipo | Comportamiento | Ejemplos |
|---|---|---|
| **Transitorio** | Ocurre una vez y desaparece | El usuario ingresa mal un dato; se pierde un paquete en TCP |
| **Intermitente** | Aparece, desaparece solo y reaparece sin intervención | Un contacto eléctrico suelto |
| **Permanente** | Persiste hasta reemplazar el componente defectuoso | Un bug de software; un disco duro dañado |

Los transitorios se resuelven reintentando; los permanentes, no: reintentar solo repite el fracaso.

## Tipos de fracasos en un sistema distribuido

En un sistema distribuido los fracasos son **parciales**: algunos componentes fallan mientras otros siguen funcionando.

| Fracaso | Qué ocurre |
|---|---|
| **Caída** (*crash failure*) | El nodo funcionaba bien hasta que se apaga o se cuelga y deja de ejecutar su programa |
| **Omisión** (*omission failure*) | El nodo está activo, pero no responde. *Receive omission*: no recibe mensajes; *send omission*: no logra enviarlos |
| **De tiempo** (*timing failure*) | El nodo responde, pero fuera del intervalo de tiempo esperado |
| **Respuesta incorrecta** (*response failure*) | Responde mal. *Value failure*: el valor es incorrecto; *state-transition failure*: sigue un flujo de control incorrecto, fuera del orden esperado |
| **Bizantina** (*arbitrary failure*) | El nodo se comporta de forma impredecible (ver [[05 - Problema de los generales bizantinos\|generales bizantinos]]) |
| **Partición de red** | La red se divide en subgrupos incomunicados, aunque cada nodo siga funcionando |

> [!warning] Fracaso de tiempo no es "nunca responde"
> En una falla de tiempo el nodo **sí** responde, pero tarde (o demasiado pronto). Si no respondiera aunque se le diera todo el tiempo posible, sería una caída u omisión.

## Preguntas de repaso

> [!question]- ¿En qué eslabón de la cadena conviene intervenir y por qué?
> En el error: el fallo muchas veces no se puede evitar (hardware que se daña, datos mal ingresados), pero si el error se detecta y se contiene, no llega a convertirse en fracaso.

> [!question]- Un servidor a veces responde y a veces no, sin que nadie lo toque. ¿Qué tipo de fallo sugiere?
> Uno intermitente: aparece y desaparece por sí solo, como un contacto eléctrico suelto o un cable de red defectuoso.

> [!question]- ¿Qué distingue una partición de red de la caída de varios nodos?
> En la partición los nodos siguen funcionando y se comunican dentro de su subgrupo; lo que falla es la comunicación entre subgrupos. Desde cada lado, el otro parece caído, aunque no lo esté.
