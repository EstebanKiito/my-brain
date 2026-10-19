# Dudas y posibles errores en los apuntes originales — Tecnologías y Aplicaciones Web (IIC2513)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Fundamentos de la web
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Internet, routers e ISPs\|Internet, routers e ISPs]] | Slide de historia: "1993 Nacimiento de JavaScript (Brendan Eich)" | JavaScript se creó en 1995 en Netscape (la propia slide lo ubica junto a la primera guerra de navegadores, 1995-2001). La nota dice 1995. |
| ℹ️ | [[04 - Mensajes HTTP y versiones del protocolo\|Mensajes HTTP y versiones del protocolo]] | Captura de la slide de response: "Response status: Optional" y "Response body: Required" | Está invertido: la status line es obligatoria y el body es opcional (por ejemplo, `204 No Content`). La transcripción respeta la imagen y la nota lo aclara en un `[!warning]`. |

## JavaScript como lenguaje
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Tipos de datos en JavaScript\|Tipos de datos en JavaScript]] | Slide de números: `const octal = 0x237;` imprime `567` | `0x237` es hexadecimal (567 en decimal); el octal se escribe `0o237` (159), como dice el mismo texto de la slide. La nota usa `0o237` y la salida verificada con Node. |
| ℹ️ | [[04 - Operadores y control de flujo en JavaScript\|Operadores y control de flujo en JavaScript]] | Slide de control de flujo: `if !(variable > 5) { … }` | Es un error de sintaxis: la condición de un `if` siempre va entre paréntesis. La nota usa `if (!(variable > 5))`. |
| ℹ️ | [[01 - Origen de JavaScript, ECMAScript y TypeScript\|Origen de JavaScript, ECMAScript y TypeScript]] | Slide de versiones: "ECMAScript 2016: await y async (para ES2017)" y "ECMAScript 2017: generadores y promesas para programación asíncrona" | Las promesas y los generadores llegaron en ES2015; `async`/`await`, en ES2017. La nota usa esas fechas. |

## Asincronía en JavaScript
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Código asíncrono y callbacks\|Código asíncrono y callbacks]] | Apuntes: "Asíncrono: Ejecución paralela del código" | El código JavaScript corre en un solo hilo; lo que ocurre en paralelo es la espera (temporizador, red, disco). La nota define asíncrono como "no espera a las instrucciones diferidas", que es lo que dice la slide, y lo aclara en un `[!warning]`. |

## React
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Hooks useState, useContext y useEffect\|Hooks useState, useContext y useEffect]] | Slide y captura de `useState`: "retorna un arreglo con dos valores: 1. El estado inicial del componente" | Retorna el estado **actual**; coincide con el inicial solo en el primer render. La transcripción respeta la imagen y la nota lo aclara. |
| ℹ️ | [[01 - React, JSX y Virtual DOM\|React, JSX y Virtual DOM]] | Slide de rendering: `document.getElementById('#root')` | `getElementById` recibe el id sin `#` (el `#` es sintaxis de selector CSS); así devolvería `null`. La nota usa `getElementById('root')`, como la slide de la aplicación mínima. |
| ℹ️ | [[02 - Componentes, props y state\|Componentes, props y state]] | Slide de tipos de componentes: la sintaxis de clase es "útil cuando sí necesitamos pasar información de un componente a otro" | Con funciones también se pasa información (props) y, con hooks, se maneja estado. La documentación de React recomienda funciones, como dicen los apuntes ("No usar clases"). La nota sigue esa recomendación. |

## APIs web y REST
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Documentar y consumir APIs\|Documentar y consumir APIs]] | Slide "Ejemplo de POST request a API de GitHub" con Axios: usa `axios.get(query_url, data, …)` sobre `…/commits` | Crear una issue es `axios.post` sobre `…/issues` (además, `get` no recibe body). La nota usa `axios.post(url, data, config)`, verificado contra la API (sin token responde 401). |

## Calidad, CI y CD
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[04 - Integración y despliegue continuos\|Integración y despliegue continuos]] | Slides de hosting: Render y Netlify aparecen ambos como "recomendación para el backend de su proyecto" | Netlify está orientado sobre todo a frontends y sitios estáticos (los backends van como funciones serverless). Parece un texto duplicado de la slide de Render. La nota deja Render como la recomendación para el backend y Netlify para frontends. |
