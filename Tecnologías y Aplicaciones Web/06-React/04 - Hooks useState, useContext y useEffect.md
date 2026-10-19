---
ramo: "Tecnologías y Aplicaciones Web"
tema: "React"
tags:
  - web
  - react
  - hooks
  - origen/complemento
prerrequisitos:
  - "[[03 - Eventos y ciclo de vida en React]]"
---

# Hooks useState, useContext y useEffect

Antes de los **hooks**, un componente que necesitaba estado o reaccionar a su ciclo de vida tenía que ser una clase. Los hooks son funciones que le dan esas capacidades a un **componente funcional**: permiten usar React sin clases, llevando la cuenta del estado y redibujando cuando corresponde.

Hay varias familias de hooks incorporados:

- **De estado**: `useState`, `useReducer`.
- **De contexto**: `useContext`.
- **De referencias**: `useRef`, `useImperativeHandle`.
- **De efectos**: `useEffect`.
- **De rendimiento**: `useMemo`, `useCallback`.

> [!warning] Las reglas de los hooks
> Los hooks se llaman solo en el nivel superior de un componente funcional (o de otro hook): nunca dentro de un `if`, un ciclo o una función anidada. React identifica cada hook por el **orden** en que se llama en cada render.

## `useState`: variables de estado

`useState(valorInicial)` retorna el valor actual y una función para actualizarlo. Un componente puede tener varios estados independientes:

![useState con dos variables de estado](adjuntos/useState%20con%20dos%20variables%20de%20estado.png)

> [!example]- Transcripción de la imagen
> "Este hook retorna un arreglo con dos valores: 1. El estado inicial del componente; 2. Una función para setear un nuevo estado". En `MyComponent`, `const [age, setAge] = useState(42);` y `const [name, setName] = useState('Taylor');`. Al lado, `handleClick()` llama a `setName('Robin')`.

El primer valor es el estado **actual**: solo coincide con el inicial en el primer render. Después de `setName('Robin')`, en el render siguiente `name` vale `'Robin'`.

## `useContext`: datos sin pasar props por cada nivel

Si muchos componentes de distintos niveles necesitan el mismo dato (el tema visual, el usuario conectado), pasarlo como prop por todos los intermedios es tedioso (*prop drilling*). Un **contexto** lo resuelve: un *provider* declara el valor y cualquier descendiente se **suscribe** con `useContext`, sin importar qué tan arriba esté el provider.

![Declaración y suscripción a un contexto](adjuntos/Declaraci%C3%B3n%20y%20suscripci%C3%B3n%20a%20un%20contexto.png)

> [!example]- Transcripción de la imagen
> - "Declaración de contexto": `MyPage` retorna `<ThemeContext.Provider value='dark'><Form /></ThemeContext.Provider>`.
> - "Suscripción a contexto": `Button()` hace `const theme = useContext(ThemeContext);`.
> - Texto: "El hook `useContext` permite suscribirse a un contexto, que puede estar mucho más arriba en el árbol, y acceder a su valor. Un contexto se declara a partir de un *context provider*, y su valor puede ser desde un simple *string* a un objeto con muchas *properties*".

El contexto mismo se crea una vez con `const ThemeContext = createContext('light')`, donde `'light'` es el valor por defecto si no hay provider.

## `useEffect`: sincronizar con el mundo externo

`useEffect` permite sincronizar un componente con un **sistema externo** y ejecutar efectos secundarios que no son de interfaz: pedir datos, abrir una conexión, crear un temporizador. Recibe una función y, opcionalmente, un arreglo de **dependencias** que decide cuándo se vuelve a ejecutar:

![Variantes de useEffect según dependencias](adjuntos/Variantes%20de%20useEffect%20seg%C3%BAn%20dependencias.png)

> [!example]- Transcripción de la imagen
> Texto: "Al usar `useEffect` podemos sincronizar un componente con un sistema externo, permitiéndonos ejecutar 'efectos secundarios' (no de UI) ante eventos en el ciclo de vida de un componente. Se gatilla en cada renderizado: cuidado con ciclos infinitos". Cinco variantes:
> - `useEffect(() => console.log('mount'), []);`
> - `useEffect(() => console.log('data1 update'), [data1]);`
> - `useEffect(() => console.log('any update'));`
> - `useEffect(() => () => console.log('data1 update or unmount'), [data1]);`
> - `useEffect(() => () => console.log('unmount'), []);`

| Dependencias | Cuándo corre el efecto |
|---|---|
| `[]` | Solo después del montaje |
| `[data1]` | Después del montaje y cada vez que cambia `data1` |
| (sin arreglo) | Después de **cada** render |

Si el efecto **retorna una función**, esa es la **limpieza** (*cleanup*): React la ejecuta antes de volver a correr el efecto y al desmontar el componente. Así se cierran las conexiones o los temporizadores que el efecto abrió:

![useEffect que conecta y desconecta un chat](adjuntos/useEffect%20que%20conecta%20y%20desconecta%20un%20chat.png)

> [!example]- Transcripción de la imagen
> `ChatRoom({ roomId })` guarda `serverUrl` con `useState('https://localhost:1234')`. Su efecto crea una conexión con `createConnection(serverUrl, roomId)`, llama a `connection.connect()` y retorna `() => { connection.disconnect(); }`. Las dependencias son `[serverUrl, roomId]`.

Si cambia `roomId`, React primero desconecta la sala anterior (limpieza) y luego conecta la nueva.

> [!warning] Ciclos infinitos
> Un efecto sin dependencias que actualiza el estado provoca un render, que vuelve a ejecutar el efecto, que vuelve a actualizar el estado… Hay que declarar las dependencias reales del efecto.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre `useEffect(f, [])` y `useEffect(f)`?
> Con `[]`, el efecto corre una sola vez, después de montar. Sin arreglo, corre después de cada render, lo que puede ser costoso o provocar ciclos si el efecto actualiza el estado.

> [!question]- ¿Para qué sirve la función que retorna un efecto?
> Es la limpieza: deshace lo que hizo el efecto (desconectar, cancelar un temporizador). React la ejecuta antes de repetir el efecto y al desmontar el componente, para no dejar recursos abiertos.

> [!question]- ¿Qué problema resuelve `useContext`?
> El de pasar un mismo dato como prop por muchos niveles intermedios que no lo usan. Cualquier componente bajo el provider puede leer el valor directamente.
