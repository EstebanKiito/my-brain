---
ramo: "Tecnologías y Aplicaciones Web"
tema: "React"
tags:
  - web
  - react
  - componentes
  - origen/complemento
prerrequisitos:
  - "[[01 - React, JSX y Virtual DOM]]"
---

# Componentes, props y state

Un componente de React **recibe input y retorna lo que debe aparecer en pantalla**, compuesto de elementos React. Hay dos fuentes de input: las **props**, que le entrega su componente padre, y el **state**, que el propio componente recuerda entre interacciones. Cuando alguna de las dos cambia, React vuelve a dibujar el componente.

## Dos formas de escribir un componente

![Componente funcional frente a componente de clase](adjuntos/Componente%20funcional%20frente%20a%20componente%20de%20clase.png)

> [!example]- Transcripción de la imagen
> - Opción 1, componente funcional: `function MyComponent(props) { return <h1>Hello, {props.name}</h1>; }`.
> - Opción 2, componente de clase: `class Counter extends React.Component`, con un `constructor(props)` que llama a `super(props)` y un método `render()` que retorna `<h1>Hello, {this.props.name}</h1>`.
> - Recuadro "Pitfall" de la documentación de React: "We recommend defining components as functions instead of classes".

> [!tip] Usar funciones, no clases
> Los componentes funcionales son la forma recomendada. Con los hooks pueden tener estado y efectos, que antes exigían clases. Las clases quedan para entender código antiguo.

Los componentes se combinan como tags. El nombre debe empezar con **mayúscula**, para que JSX lo distinga de un tag HTML:

```jsx
function Example() {
  return (
    <PageLayout>
      <Header />
      <AuthorBio name="A" />
      <AuthorBio name="B" />
    </PageLayout>
  );
}
```

## Cómo empezar una interfaz

1. **Identificar y nombrar los componentes**: dividir la maqueta en cajas, como en la app de tareas (formulario, lista, tarea, botón).
2. **Construir una versión estática**: componentes que solo dibujan, sin interacción.
3. **Generar contenido dinámico con props**: pasar los datos de padres a hijos.
4. **Manejar el estado con `useState`**: agregar lo que cambia con la interacción.

## Props: los argumentos de un componente

Las **props** son la forma en que un componente le pasa información a sus descendientes. La sintaxis es como la de los atributos HTML, pero se puede pasar **cualquier valor**: números, objetos, arreglos o funciones. Para el hijo, las props son de **solo lectura**.

![Props de Avatar desde Profile](adjuntos/Props%20de%20Avatar%20desde%20Profile.png)

> [!example]- Transcripción de la imagen
> - `Avatar({ person, size })` retorna un `<img>` con `className='avatar'`, `src={getImageUrl(person)}`, `alt={person.name}`, `width={size}` y `height={size}` (los atributos están resaltados).
> - `Profile()` retorna un `<Card>` que contiene `<Avatar size={100} person={{ name: 'Katsuko Saruhashi', imageId: 'YfeOqp2' }} />`.

Las dobles llaves de `person={{ … }}` no son una sintaxis especial: las llaves externas indican "aquí va una expresión JavaScript" y las internas son el objeto literal.

## State: recordar valores al interactuar

El **state** es una propiedad **interna** de un componente que puede cambiar en el tiempo. En un componente funcional se crea con el hook `useState`, que recibe el valor inicial y retorna un arreglo con dos cosas:

1. el **valor actual** del estado (en el primer render, el valor inicial);
2. una **función para actualizarlo**.

```jsx
const [contador, setContador] = useState(0);
// ...
setContador(contador + 1);
```

![Contador con useState](adjuntos/Contador%20con%20useState.png)

> [!example]- Transcripción de la imagen
> El archivo `App.js` define `Counter`. Usa `const [count, setCount] = useState(0);` y una función `handleClick` que hace `setCount(count + 1)`. Retorna un `<button onClick={handleClick}>` con el texto "You pressed me {count} times". A la derecha, la vista previa muestra el botón "You pressed me 0 times".

> [!warning] No modificar el estado directamente
> `count = count + 1` no actualiza la pantalla: React no se entera del cambio. Solo la función setter (`setCount`) agenda un nuevo render con el valor actualizado.

> [!tip] Props y state gatillan el render
> Cualquier cambio en las props o en el state de un componente hace que se vuelva a renderizar. React calcula el nuevo Virtual DOM y aplica al DOM real solo las diferencias.

## Una aplicación mínima

```jsx
import ReactDOM from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<HelloMessage name="Antonio" />);
```

Son tres pasos: importar React DOM, definir los componentes y dibujarlos con `render` sobre el nodo raíz.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre props y state?
> Las props llegan desde el componente padre y el hijo no las modifica. El state es interno: lo crea y lo actualiza el propio componente con su función setter.

> [!question]- ¿Por qué `count = count + 1` no actualiza la interfaz?
> Porque React solo vuelve a renderizar cuando se llama a la función setter de `useState`. Una asignación directa cambia una variable local que se pierde en el siguiente render.

> [!question]- ¿Por qué los componentes se nombran con mayúscula?
> Porque JSX interpreta un tag en minúscula como un elemento HTML (`<div>`) y uno en mayúscula como un componente (`<Avatar>`).
