---
ramo: "Testing"
tema: "Fundamentos del testing de software"
tags:
  - testing/fundamentos-del-testing-de-software
  - origen/complemento
prerrequisitos:
  - "[[Ingeniería de Software/06-Testing/02 - Error, defecto y falla|Error, defecto y falla]]"
---

# Qué es el testing, error, defecto, falla y el oráculo de prueba

## Por qué existe el testing: convertir confianza en evidencia

Imagina que son las 11 de la noche, acabas de subir un cambio a producción porque «era solo un refactor pequeño» y tu celular empieza a llenarse de mensajes: el sistema se cayó. Cuando programamos, solemos confiar en nuestra intuición de que el código funciona porque compila y pasa un par de casos básicos. El **testing de software** es la disciplina que reemplaza esa confianza subjetiva por **evidencia empírica**, ejercitando un programa con la intención explícita de encontrar fallas antes de que las sufra el usuario final.

De acuerdo con el estándar internacional ISO/IEC/IEEE, el testing evalúa si un sistema responde la pregunta fundamental: *¿hace lo que se supone que debe hacer —y únicamente eso?* La segunda mitad es crítica: un sistema puede funcionar perfecto en el «camino feliz», pero hacer algo peligroso ante una entrada inesperada. Tres desastres históricos muestran qué ocurre cuando la confianza reemplaza a la evidencia:

* **Therac-25 (1985–1987):** una máquina de radioterapia tenía una condición de carrera que solo se activaba cuando el operador tecleaba muy rápido cierta secuencia para corregir un comando. Al menos seis pacientes recibieron dosis $100$ veces superiores a la prescrita; varios murieron porque ninguna prueba cubrió esa secuencia de interacciones.
* **Mars Climate Orbiter (1999):** la NASA perdió una sonda de $327$ millones de dólares porque un módulo calculaba el impulso en unidades imperiales ($\text{lbf}\cdot\text{s}$) y el módulo receptor esperaba unidades métricas ($\text{N}\cdot\text{s}$), sin pruebas de integración entre ambos.
* **Knight Capital Group (2012):** un despliegue activó por accidente código obsoleto en la bolsa y ejecutó millones de órdenes erróneas en $45$ minutos, causando pérdidas por más de $460$ millones de dólares y la quiebra de la empresa.

---

## La cadena causal: error, defecto y falla

En el lenguaje coloquial se usan como sinónimos, pero el glosario **ISTQB** distingue tres eslabones causales estrictos (profundizando lo visto en [[Ingeniería de Software/06-Testing/02 - Error, defecto y falla|Error, defecto y falla]]):

![Cadena causal desde la persona que comete un error hasta la falla observable](adjuntos/Cadena%20error%20defecto%20y%20falla.png)

| Concepto | Definición operativa (ISTQB) | Ejemplo en `clasificar_fiebre` |
| :--- | :--- | :--- |
| **Error** (*mistake*) | Acción o equivocación humana (o de un modelo) de razonamiento al diseñar o programar. | Pensar que «mayor o igual a $38.0$» se escribe con el operador `>`. |
| **Defecto** (*defect* / *bug*) | La manifestación estática del error dentro del código fuente o documento. | La línea `elif temperatura_c > 38.0:` escrita en el archivo `.py`. |
| **Falla** (*failure*) | El comportamiento incorrecto observable externamente cuando el código se ejecuta. | Al llamar `clasificar_fiebre(38.0)`, el programa devuelve `"febrícula"` en vez de `"fiebre"`. |

> [!important] Defectos latentes y depuración
> Un **defecto** puede vivir oculto en el código durante años sin causar ninguna **falla** hasta que una entrada específica lo ejecuta y propaga su efecto a la salida. El **testing** detecta fallas al ejecutar el sistema; la **depuración** (*debugging*) es el proceso inverso de rastrear una falla hacia atrás para localizar y corregir el defecto en el código.

---

## Verificación frente a validación

* **Verificación (*¿estamos construyendo el sistema correctamente?*):** comprueba si el software se ajusta fielmente a su especificación técnica (por ejemplo, verificar que un campo `edad` acepte enteros entre $0$ y $120$ tal como pide el documento de diseño). El caso del *Mars Climate Orbiter* fue un fallo de verificación en la interfaz entre dos módulos.
* **Validación (*¿estamos construyendo el sistema correcto?*):** evalúa si el software resuelve la necesidad real del usuario en su contexto. Si ese formulario de edad pertenece a la contratación de un seguro de vida para adultos mayores, aceptar una edad de $5$ años cumple la especificación mal redactada (pasa la verificación), pero falla la validación del negocio.

---

## El oráculo de prueba y el ejemplo de `clasificar_fiebre`

Ejecutar una función y ver qué imprime **no es hacer testing**. Para probar necesitamos una fuente de verdad externa —independiente del propio código— que determine cuál es el resultado esperado para compararlo con el resultado real: eso es un **oráculo de prueba** (*test oracle*). Si modelamos un programa como $P : D \to R$, un caso de prueba es un par $(d, \text{esperado}(d))$ con $d \in D$, y el oráculo emite un veredicto:

$$\text{veredicto}(d) = \bigl[ P(d) = \text{esperado}(d) \bigr] \in \{\text{pasa}, \text{falla}\}$$

En muchos sistemas reales (simulaciones físicas, compiladores o agentes de IA) no existe una tabla simple con la respuesta exacta de antemano; a esta dificultad fundamental se la conoce como el **problema del oráculo**, y motiva técnicas como el *property-based testing* o el *metamorphic testing*. Veamos cómo actúa la especificación clínica como oráculo sobre `clasificar_fiebre`:

```python
def clasificar_fiebre(temperatura_c):
    if temperatura_c < 35.0:
        return "hipotermia"
    elif temperatura_c < 37.5:
        return "normal"
    elif temperatura_c > 38.0:   # Defecto: la tabla exige >= 38.0
        return "fiebre"
    else:
        return "febrícula"
```

Si la especificación clínica (nuestro oráculo) exige `"fiebre"` para temperaturas **iguales o mayores que $38.0\text{ }^\circ\text{C}$**, probar con $36.6$ ejecuta la función pero no activa el defecto. Solo al probar el borde exacto $d = 38.0$ con `self.assertEqual(clasificar_fiebre(38.0), "fiebre")` el oráculo compara `"febrícula" == "fiebre"` y denuncia la falla.

---

## Preguntas de repaso

> [!question]- Un equipo investiga un incidente en producción y anota: (1) el programador olvidó que el descuento solo aplica a compras sobre $\$10\,000$, (2) falta la condición `and monto > 10000` en el `if`, y (3) a un cliente con una compra de $\$5\,000$ se le cobró con descuento. Clasifica cada evento según ISTQB.
> 1. **Error (*mistake*):** la confusión mental u olvido del programador respecto a la regla de negocio.
> 2. **Defecto (*defect* / *bug*):** la condición incompleta que quedó escrita estáticamente dentro del código fuente.
> 3. **Falla (*failure*):** el cobro incorrecto observable durante la ejecución en producción cuando un cliente compró por $\$5\,000$.

> [!question]- ¿Por qué el propio código bajo prueba jamás puede usarse como su propio oráculo de prueba?
> Porque el propósito del oráculo es contrastar el comportamiento implementado $P(d)$ contra una fuente de verdad independiente $\text{esperado}(d)$. Si calculáramos el valor esperado usando la misma lógica del programa bajo prueba, cualquier defecto en el código se repetiría en el oráculo y la prueba siempre daría «pasa» incluso estando rota.

> [!question]- En `clasificar_fiebre`, ¿por qué ejecutar la prueba `assert clasificar_fiebre(36.6) == "normal"` no revela ninguna falla a pesar de que el código contiene un defecto en la línea `elif temperatura_c > 38.0:`?
> Porque un defecto solo produce una falla cuando la entrada alcanza la línea defectuosa, altera el estado o flujo respecto de lo esperado y propaga esa diferencia hasta la salida. Con $36.6$, el flujo entra en la segunda rama (`temperatura_c < 37.5`) y retorna `"normal"` sin llegar a evaluar jamás la condición defectuosa `> 38.0`.

> [!question]- Explica con un ejemplo la diferencia entre un fallo de verificación y un fallo de validación.
> Si la especificación pide ordenar una lista de menor a mayor y el algoritmo devuelve los elementos desordenados, hay un **fallo de verificación** (no construimos el sistema según su especificación). Si en cambio el algoritmo ordena perfectamente de menor a mayor sin ningún bug, pero el usuario final necesitaba ver primero las transacciones más recientes (orden descendente), hay un **fallo de validación** (construimos el sistema equivocado para la necesidad real).
