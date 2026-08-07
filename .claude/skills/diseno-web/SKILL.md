---
name: diseno-web
description: Sistema de diseño de opengeorock.org — tokens, tipografía, componentes y qué está prohibido cambiar. Úsalo SIEMPRE antes de tocar el bloque <style> de index.html o de añadir cualquier marcado visible.
---

# Sistema de diseño de opengeorock.org

**El diseño está cerrado.** Esta skill existe para que puedas trabajar
dentro de él, no para que lo mejores. Si crees que algo debería cambiar,
**dilo y espera el OK** — no lo apliques.

## La idea, en una frase

Papel cálido, tinta negra, un solo acento verde, y tres tipografías con
papeles fijos. Se parece a un cuaderno de laboratorio bien impreso, no a
una landing de SaaS.

---

## Tokens

Están en `:root`, al principio del `<style>`. **Usa siempre la variable,
nunca el valor literal.**

```css
--paper:   #f5f1ea   /* fondo base */
--paper-2: #ede7dc   /* fondo de sección alterna (#software, #team) */
--paper-3: #e3dccd   /* fondos de chip y marcadores de posición */
--ink:     #141311   /* texto principal, y fondo de #contribute */
--ink-2:   #2a2824   /* texto secundario */
--mute:    #6b6660   /* texto terciario, etiquetas */
--rule:    #1413111f /* borde estándar */
--rule-2:  #14131114 /* borde punteado interno */

--accent:     oklch(0.52 0.11 148)  /* verde de superficie crítica */
--accent-ink: oklch(0.34 0.08 148)  /* el mismo, para texto e hover */
--terra: #c98a5f;  --ochre: #d4a36a  /* solo ecos de muestra de material */

--radius: 4px
--shadow: 0 1px 0 #14131108, 0 14px 40px -24px #14131140
```

**Un solo acento.** El verde marca la superficie crítica de rotura; es una
cita del programa, no decoración. No añadas colores. `--terra` y `--ochre`
existen para muestras de material y no se usan en ningún otro sitio.

Sobre fondo oscuro (`#contribute`, `.specs`) el texto se aclara con
`color-mix(in oklab, var(--paper) N%, transparent)`, no con grises nuevos.

## Tipografías

| Familia | Papel | Dónde |
|---|---|---|
| **Newsreader** (serif) | Titulares y cifras destacadas. Pesos 400/500, `letter-spacing` negativo. Las cursivas van en `--accent-ink` | `h1`, `h2`, `.sw-title`, `.stat .v`, `.suite-row .name` |
| **Inter** (sans) | Todo el texto corrido | `body`, `p`, `.descr`, `.bio` |
| **JetBrains Mono** | Etiquetas, metadatos, datos numéricos. Siempre en mayúsculas con `letter-spacing: 0.1em` y ~10.5 px | `.eyebrow`, `.stat .k`, `.specs .k`, `.mono` |

La mono es el "instrumento de medida" de la página: si un texto es un dato,
va en mono; si es una idea, va en Inter; si es un titular, en Newsreader.
Esa correspondencia no se rompe.

## Componentes que ya existen

Antes de crear marcado nuevo, comprueba si alguno sirve:

| Clase | Para qué |
|---|---|
| `.eyebrow` | Antetítulo de sección, con `<span class="dot">` |
| `.sec-head` | Cabecera de sección: título a la izquierda, `.meta` a la derecha |
| `.btn.primary` / `.btn.ghost` / `.btn.locked` | Botones. `.locked` para lo no disponible |
| `.tag` / `.tag.soon` | Chips pequeños |
| `.specimen` | Tarjeta de resultado del hero |
| `.stats` > `.stat` | Tira de cifras (rejilla de 4) |
| `.feat-grid` > `.feat` | Rejilla de principios numerados |
| `.screens` > `.screen` | Marco de captura con barra de título y pie |
| `.specs` > `.row` | Ficha técnica sobre fondo tinta (rejilla de 4) |
| `.suite-list` > `.suite-row` | Filas de la hoja de ruta, con `.status-cell` |
| `.person`, `.attrib`, `.affil` | Tarjetas del equipo |
| `.channels` > `.channel` | Tarjetas de contribución, con `.locked` |

**Añadir una fila a `.specs` o una tarjeta a un grid existente es
contenido, no diseño: hazlo sin preguntar.** Crear un componente nuevo es
diseño: pregunta.

### Rejillas: cuida el múltiplo

`.stats` y `.specs` son `repeat(4, 1fr)`; `.channels` es `repeat(3, 1fr)`.
Un número de hijos que no sea múltiplo deja un hueco visible al final.
Si añades filas a `.specs`, deja el total en 4, 8 o 12.

## Puntos de ruptura

`480 · 640 · 720 · 820 · 860 · 900 · 960` px. No inventes otros.

Dos comportamientos que sorprenden:

- Por debajo de **820 px** `nav.primary a:not(.cta)` se oculta: solo queda
  el botón *Contribute*. No hay menú hamburguesa, y es deliberado.
- Por debajo de **820 px** `.suite-row` pasa de 4 columnas a 2 y la
  descripción salta a `grid-column: 1/-1`.

Comprueba siempre a **375 px** y a **1440 px**. El `body` lleva
`overflow-x: hidden`, así que un desbordamiento no se ve pero rompe el
ancho: búscalo con las herramientas de desarrollo, no a ojo.

## Prohibido sin permiso explícito

- Cambiar cualquier token, tipografía, radio, sombra o espaciado.
- Modo oscuro. La página es clara a propósito.
- Animaciones nuevas. La única que hay es `@keyframes pulse` en
  `.sw-status`, y basta.
- Librerías de CSS o de iconos. Los iconos son SVG en línea, `stroke-width`
  1.6–2, `viewBox="0 0 24 24"`.
- Sacar el CSS a un archivo aparte, o partir `index.html`. Cambia el
  despliegue y hay que decidirlo, no deducirlo.
- Gradientes, glassmorphism, bordes de colores, sombras de color.
