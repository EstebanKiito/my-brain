---
ramo: "Tecnologías y Aplicaciones Web"
tema: "React"
tags:
  - web
  - react
  - eventos
  - origen/complemento
prerrequisitos:
  - "[[02 - Componentes, props y state]]"
---

# Eventos y ciclo de vida en React

Un componente no solo dibuja: responde al usuario y pasa por etapas, como aparecer en pantalla, actualizarse y desaparecer. React maneja los eventos con una sintaxis parecida a la de los eventos *inline* de HTML, pero con funciones de verdad, y define un **ciclo de vida** que explica cuándo conviene ejecutar cada tipo de código.

## Eventos: de HTML a React

En HTML con JavaScript, un evento inline se escribe como un string con código:

![Evento inline en el DOM](adjuntos/Evento%20inline%20en%20el%20DOM.png)

> [!example]- Transcripción de la imagen
> "Eventos en React se manejan de manera similar a eventos en el DOM (en particular, de manera similar a la definición de eventos *inline*). En el DOM (con HTML y JS)": `<button onclick="handleClick()">Click Me</button>` junto a `function handleClick() { alert('Button clicked!'); }`. Están resaltados `onclick="handleClick()"` y el nombre de la función.

En React el atributo va en *camelCase* (`onClick`) y recibe **la función misma**, no un string con su llamada. Como las funciones son objetos, el handler se pasa como cualquier otra prop:

```jsx
function ButtonExample() {
  const handleClick = () => {
    alert('Button clicked!');
  };
  return <button onClick={handleClick}>Click Me</button>;
}
export default ButtonExample;
```

> [!warning] Pasar la función, no llamarla
> `onClick={handleClick}` entrega la función para que React la llame en el click. `onClick={handleClick()}` la ejecuta **durante el render** y entrega su resultado; si además actualiza el estado, provoca un ciclo infinito de renders. Para pasar argumentos se usa una flecha: `onClick={() => borrar(id)}`.

## Handlers como props

Como un handler es solo una función, un componente padre puede pasárselo a un hijo. Así el hijo avisa que "algo pasó" y el padre decide qué hacer con su propio estado:

```jsx
function Tarea({ texto, onBorrar }) {
  return <li>{texto} <button onClick={onBorrar}>x</button></li>;
}

function Lista() {
  const [tareas, setTareas] = useState(['Preparar', 'Subir']);
  return (
    <ul>
      {tareas.map((t) => (
        <Tarea key={t} texto={t} onBorrar={() => setTareas(tareas.filter((x) => x !== t))} />
      ))}
    </ul>
  );
}
```

> [!tip] Los datos bajan, los eventos suben
> El estado vive en el componente más alto que lo necesita y baja como props. Los hijos lo modifican llamando a funciones que también recibieron como props.

## Ciclo de vida de un componente

![Ciclo de vida de un componente de clase](adjuntos/Ciclo%20de%20vida%20de%20un%20componente%20de%20clase.png)

> [!example]- Transcripción de la imagen
> Diagrama de React 16.4 con tres columnas: **Mounting**, **Updating** y **Unmounting**.
> - **Render phase** ("pura, sin efectos secundarios; React puede pausarla, abortarla o reiniciarla"): `constructor` (solo al montar), `getDerivedStateFromProps`, `shouldComponentUpdate` (solo al actualizar; si retorna falso, corta) y `render`. Una actualización se gatilla por *New props*, `setState()` o `forceUpdate()`.
> - **Pre-commit phase** ("puede leer el DOM"): `getSnapshotBeforeUpdate`.
> - **Commit phase** ("puede trabajar con el DOM, ejecutar efectos y agendar actualizaciones"): "React updates DOM and refs", y luego `componentDidMount`, `componentDidUpdate` o `componentWillUnmount`.

| Fase | Qué ocurre |
|---|---|
| **Inicialización** | El componente empieza su trabajo: se configuran el estado y las props (en las clases, en el `constructor`) |
| **Montaje** (*mounting*) | El componente se crea y se inserta en el DOM como nodo |
| **Actualización** (*updating*) | El estado o las props cambian en respuesta a eventos del usuario y el componente se vuelve a renderizar |
| **Desmontaje** (*unmounting*) | La última fase: el componente se quita del DOM |

El diagrama corresponde a los componentes de clase, con un método por cada momento. En los componentes funcionales las mismas fases se manejan con un solo hook, `useEffect`, que se ejecuta después del montaje y de las actualizaciones, y cuya función de limpieza corre antes de desmontar. Se ve en [[04 - Hooks useState, useContext y useEffect|Hooks useState, useContext y useEffect]].

> [!warning] El render debe ser puro
> Durante la fase de render no se deben hacer efectos secundarios (pedir datos, modificar el DOM, crear temporizadores), porque React puede ejecutarla varias veces o descartarla. Esos efectos van en la fase de commit: `componentDidMount` en clases, `useEffect` en funciones.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `onclick="handleClick()"` en HTML y `onClick={handleClick}` en React?
> En HTML el atributo es un string de código que el navegador evalúa al hacer click. En React es una prop que recibe directamente la función (en camelCase), y React la invoca cuando ocurre el evento.

> [!question]- ¿Cómo puede un componente hijo modificar el estado de su padre?
> El padre le pasa como prop una función que actualiza su estado. El hijo la llama ante un evento, y el padre se vuelve a renderizar con el nuevo valor.

> [!question]- ¿En qué fase del ciclo de vida conviene pedir datos a un servidor y por qué?
> Después del montaje (`componentDidMount` o `useEffect`), en la fase de commit. El render debe ser puro, porque React puede repetirlo o descartarlo, mientras que el commit ocurre una sola vez por actualización.
