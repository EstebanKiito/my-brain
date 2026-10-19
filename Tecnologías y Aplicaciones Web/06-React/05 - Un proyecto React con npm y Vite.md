---
ramo: "Tecnologías y Aplicaciones Web"
tema: "React"
tags:
  - web
  - react
  - vite
  - npm
  - origen/complemento
prerrequisitos:
  - "[[02 - Componentes, props y state]]"
  - "[[05 - Funciones, clases y módulos en JavaScript]]"
---

# Un proyecto React con npm y Vite

El navegador no entiende JSX ni sabe de dónde sacar el paquete `react`. Entre el código que se escribe y lo que corre en el navegador hacen falta dos herramientas: un **gestor de paquetes**, que descarga las librerías, y una **herramienta de build**, que traduce JSX, resuelve los `import` y sirve la aplicación durante el desarrollo.

## Gestores de paquetes

Así como Python tiene `pip` y Ruby tiene sus gemas, JavaScript tiene **npm** (y alternativas como **yarn**). Un proyecto declara sus dependencias en `package.json`:

```json
{
  "name": "todo-app",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "vite": "^6.0.0",
    "@vitejs/plugin-react": "^4.0.0"
  }
}
```

- `npm install` descarga todo lo declarado en la carpeta `node_modules/`, que **no se sube al repositorio**: se regenera desde `package.json`.
- `dependencies` son las librerías que la aplicación necesita para funcionar; `devDependencies` son las que solo se usan para desarrollar (la herramienta de build, el linter).
- `npm run dev` ejecuta el script `dev` definido arriba.

## Vite

**Vite** es una herramienta de front-end que facilita desarrollar y construir aplicaciones, y funciona con distintas librerías (Vue, React, Preact, Svelte o Lit). Ofrece:

- un servidor de desarrollo que se inicia con un comando (`vite`);
- **hot-reloading** (*HMR*, *hot module replacement*): al guardar un archivo, el navegador se actualiza sin perder el estado de la página;
- soporte para TypeScript, JSX y CSS, además de JavaScript;
- configuraciones por defecto razonables, para no tener que tomar decisiones de optimización a mano.

```bash
npm create vite@latest todo-app -- --template react
cd todo-app
npm install
npm run dev        # sirve la app en http://localhost:5173
```

## Qué trae un proyecto recién creado

| Archivo | Rol |
|---|---|
| `index.html` | La única página: tiene el `<div id="root">` y carga `src/main.jsx` como módulo |
| `src/main.jsx` | Punto de entrada: hace `createRoot(document.getElementById('root')).render(<App />)` |
| `src/App.jsx` | El componente raíz, desde donde se componen los demás |
| `package.json` | Dependencias y scripts |
| `vite.config.js` | Configuración de Vite (por ejemplo, el plugin de React) |

```mermaid
flowchart LR
    A[index.html] --> B[src/main.jsx]
    B --> C[App.jsx]
    C --> D[Componentes]
    E[npm run dev] -.compila JSX y sirve.-> A
```

> [!tip] Desarrollo frente a producción
> `npm run dev` sirve el código casi tal cual, para recargar rápido. `npm run build` genera en `dist/` archivos estáticos optimizados (minificados y agrupados), que son los que se publican.

> [!warning] Una aplicación React es una sola página
> El servidor entrega siempre el mismo `index.html` casi vacío, y es el JavaScript el que dibuja todo en el navegador. Este modelo se llama *client side rendering* y tiene consecuencias, por ejemplo para buscadores y para el tiempo de carga inicial.

## Preguntas de repaso

> [!question]- ¿Por qué `node_modules/` no se sube al repositorio?
> Porque es pesado y se puede regenerar exactamente con `npm install` a partir de `package.json` (y del archivo de bloqueo de versiones). Basta con versionar la lista de dependencias.

> [!question]- ¿Qué aporta Vite a un proyecto React?
> Traduce JSX a JavaScript, resuelve los `import` de paquetes, levanta un servidor de desarrollo con recarga en caliente y genera la versión optimizada para producción.

> [!question]- ¿Qué diferencia hay entre `dependencies` y `devDependencies`?
> Las primeras se necesitan para que la aplicación funcione (React, React DOM). Las segundas solo sirven para desarrollar o construir (Vite, linters, herramientas de testing), y no forman parte de lo que se ejecuta en producción.
