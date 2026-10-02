---
name: diseno-web
description: Sistema de diseño de opengeorock.org (dirección A «Cuaderno técnico») — tokens, tipografías, componentes, figuras SVG, animación, puntos de ruptura y qué está prohibido cambiar. Úsalo SIEMPRE antes de tocar assets/css/site.css, assets/css/docs.css o assets/js/site.js, o de añadir cualquier marcado visible.
---

# Sistema de diseño de opengeorock.org

**El diseño está cerrado.** Esta skill existe para que puedas trabajar dentro
de él, no para que lo mejores. Si crees que algo debería cambiar, **dilo y
espera el OK** — no lo apliques.

Los estilos viven en dos archivos compartidos: `assets/css/site.css` (todo el
sistema) y `assets/css/docs.css` (solo la documentación). El comportamiento, en
`assets/js/site.js`. Las páginas no llevan `<style>` ni `<script>` propios.

## La idea, en una frase

Papel cálido, tinta, un verde de marca y el bermellón reservado a la superficie
crítica de rotura; una lámina de dibujo técnico con su cajetín. Se parece a un
cuaderno de laboratorio o a un plano bien impreso, no a una landing de SaaS. Es
la propuesta **A** de las tres que se probaron (`desarrollo/propuestas/`), y
solo existe en modo claro.

---

## Tokens

Están en el `:root` de `site.css`. **Usa siempre la variable, nunca el valor
literal.**

```css
--paper:   #f4efe6   /* fondo base */
--paper-2: #ebe4d6   /* secciones alternas (.section.alt), cabeceras de tabla, hover */
--paper-3: #e1d8c6   /* sombra dura de las láminas, puntos de las barras de título */
--white:   #fbf9f4   /* superficies elevadas: tarjetas, láminas, tablas, buscador */
--ink:     #161512   /* texto principal; fondo de .section.ink, .foot y .btn.primary */
--ink-2:   #34302a   /* texto secundario */
--mute:    #6a645c   /* texto terciario y etiquetas */
--rule:    #16151221 /* filete estándar */
--rule-2:  #16151212 /* filete interno suave */

--green:      oklch(0.5 0.11 150)    /* marca: foco, pestaña activa, punto del eyebrow, tick */
--green-ink:  oklch(0.38 0.085 150)  /* el verde para texto: enlaces, cursivas, hover */
--green-soft: oklch(0.93 0.035 150)  /* fondos suaves: .tag.live, selección, resaltado */
--crit:       #c8431b                /* bermellón: superficie crítica, factor de seguridad, avisos */
--crit-soft:  #f5e1d7
--water:      #2f6fb3                /* agua: nivel freático, estanque, .note.water */
--water-soft: #dfe9f3
--sand #e8d9bd · --clay #d6bb98 · --gravel #c6c1ab · --rock #b4ad9f   /* estratos: solo rellenos de figuras */

--radius: 6px · --radius-lg: 10px
--sheet-shadow: 8px 8px 0 var(--paper-3)
--maxw: 1240px · --gutter: 32px (18px por debajo de 720 px) · --top-h: 64px
```

**Cada acento tiene un significado y no se reparte por gusto.** El verde es la
marca y la acción (enlaces, foco, estado «disponible»). El **bermellón** es la
superficie crítica y el factor de seguridad crítico, y por extensión lo que
advierte (`.note.warn`, `.tag.crit`). El **azul** es agua y nada más. Los cuatro
tintes de estrato son rellenos de figura. No añadas colores nuevos.

Sobre fondo oscuro (`.section.ink`, `.card.ink`, `.foot`) el texto se aclara con
`color-mix(in oklab, var(--paper) N%, transparent)`, no con grises nuevos.

Colores literales que ya existen y **no son un modelo a seguir**: la paleta del
bloque de código (`pre`), el naranja del logotipo (`.brand .la`), el trazo de
contacto y de capa débil de `.slope-svg`, el `#fff` de `.btn.green` y los
`.glyph` de la portada. Todo lo nuevo va con tokens.

## Tipografías

Tres familias con papeles fijos, cargadas desde Google Fonts (Inter 400/500/600;
JetBrains Mono 400/500; Newsreader 400/500 con cursivas). No uses otros pesos.

| Familia | Papel | Dónde |
|---|---|---|
| **Newsreader** (serif) | Titulares y cifras destacadas. Pesos 400/500, `letter-spacing` negativo. Las cursivas (`<em>`) van en `--green-ink`; `.crit` en bermellón | `h1`–`h3`, `.metric .v`, `.brand b`, `.mega-item.feature b`, `.doc-pager b`, `blockquote`, símbolos de `.dg` |
| **Inter** (sans) | Todo el texto corrido, los botones y `h4` | `body`, `p`, `.btn`, `.card p`, `h4` |
| **JetBrains Mono** | Etiquetas, metadatos, datos y código. Mayúsculas con `letter-spacing` ≈ 0.09 em y ~11 px (10,5 en tags y cabeceras de tabla) | `.label`, `.mono`, `.tag`, `.titleblock`, `table.data thead`, `.secnum`, `.fignum`, número de ecuación, `code`, `kbd`, `pre`, `.tool` |

La mono es el «instrumento de medida» de la web: si un texto es un dato, va en
mono; si es una idea, va en Inter; si es un titular, en Newsreader. Esa
correspondencia no se rompe. Un titular suele ser una frase corta cuya segunda
mitad va en `<em>`: *«Checked against references, <em>not believed.</em>»*.

## Motivos de plano

Lo que da a la web su aire de cuaderno técnico. Reutilízalos tal cual:

- **Rejilla de papel** de 32 px: `.hero::before` y `.page-hero::before` (se
  desvanece con una máscara) y la utilidad `.paper-grid`.
- **Lámina** `.sheet`: borde de tinta, sombra dura desplazada
  (`--sheet-shadow`, que comparten `.shot`, `.tabs`, `.chat`, `.mega` y el
  aviso de idioma), esquina `.corner` («Sheet 01») y **cajetín** `.titleblock`
  con pares clave/valor en mono; el factor de seguridad, en bermellón (`.v.fos`).
- **Numeración de sección** `§ 01 — …` en `.sec-num` y etiquetas `.label` en
  mayúsculas mono.
- **Barras de título de ventana** con tres puntos (`.shot .bar`, `.chat .bar`).
- **Convenciones de dibujo** en las figuras: nivel freático discontinuo azul con
  su triángulo y rayitas; estratos en arena, arcilla, grava y roca; superficies
  de búsqueda del bermellón (crítica) al verde (factor alto); la crítica gruesa
  con su centro y su radio.

---

## Componentes que ya existen

Antes de crear marcado nuevo, comprueba si alguno sirve. «Necesito… → uso…»:

| Necesito… | Uso | Notas |
|---|---|---|
| Cabecera de una página interior | `.page-hero` con `.crumbs`, `h1` y `.lede` (a veces en `.grid-2` con una `.note` al lado) | La portada usa `.hero` + `.hero-grid`; solo ella |
| Una sección con su título | `.section` (alterna con `.section.alt`) > `.wrap` > `.sec-head` (`.sec-num` + `h2` a la izquierda, párrafo a la derecha) | Cierra la página con `.section.ink` > `.wrap.cta-band` |
| Varias tarjetas | `.grid-3` / `.grid-4` > `.card`; `a.card` si enlaza; `.card.ink` destacada; `.card.planned` para lo que aún no existe | El estado, con `.tag.live` o `.tag.soon` |
| Las cinco piezas de la suite | `.suite` (1 tarjeta destacada + 4) | Solo la portada |
| Principios numerados con icono | `.feature-grid` > `.feature` (`.ic`, `h4`, `p`) | De 3 en 3 |
| Cifras destacadas | `.metrics` > `.metric` (`.v` serif, `.k` mono) | 6 en la fila |
| Ficha técnica clave/valor | `dl.spec-list` > `div` > `dt.label` + `dd`; `.one` para una columna | De dos en dos |
| Una figura calculada con su cajetín | `figure.sheet` > `.corner`, `.fig` (SVG) y `.titleblock` | Ver «Figuras» |
| Una captura del programa | `figure.shot` > `.bar` + `<img>` + `figcaption` | Capturas en inglés |
| Pasos de una instalación | `ol.steps` > `li` > `h4` + texto | Numera solo (01, 02…) |
| Variantes por sistema o cliente | `.tabs[data-group]` > `.tablist` + `.tabpanel` | Ver «Pestañas» |
| Un comando o código | `.code` > `pre` > `code` | El botón *Copy* lo añade el JS |
| Un aviso | `.note` (+ `.warn` para limitaciones, `.water` para agua) con `span.label` | Una limitación del programa es siempre `.warn` |
| Una tabla de datos | `.table-wrap` > `table.data`; `class="n"` en las celdas numéricas | Se desplaza sola en horizontal |
| Una sesión de agente | `.chat` > `.msg.user` / `.msg.agent` / `.tool` | Solo en `ai/` y la portada |
| Etiquetas y estado | `.tag` (`.live`, `.soon`, `.crit`, `.water`), `.chips`, `.eyebrow` con `.dot` | |
| Botones | `.btn` (`.primary`, `.green`, `.lg`, `.sm`), `.cta-row`; lo no disponible, `.btn.locked` o `aria-disabled="true"` | |
| Subnavegación de una ficha | `.subnav` (fija bajo la cabecera, con la sección activa) | Solo `products/slip2d.html` |
| Equipo y afiliaciones | `.people` > `.person`, `.avatar`, `.affil` | Solo `about/` |
| Lista con marcas | `ul.ticks` | |

En la **documentación** (`docs.css`) además: `.doc-shell` (índice · texto · «en
esta página»), `.prose`, ecuaciones `.eq`, `dl.symbols` + `.where`, figuras
`figure.fig > .art`, tablas `figure.tbl`, `.impl` («En OGR Slip2D»), `.cards-doc`,
`a.cite` y `ol.refs`. Su marcado está en `dev/guia-documentacion.md`. Hay también
una galería de ejemplos (`.gallery` > `.example`) definida pero sin uso.

**Añadir una fila a una lista, una tarjeta a una rejilla existente o un ejemplo
nuevo es contenido, no diseño: hazlo sin preguntar.** Crear un componente nuevo
es diseño: pregunta.

### Rejillas: cuida el múltiplo

Un número de hijos que no encaje deja un hueco visible al final.

| Rejilla | Columnas (escritorio → ≤ 960 → ≤ 720) | Hijos |
|---|---|---|
| `.grid-3`, `.gallery`, `.feature-grid` | 3 → 2 → 1 | múltiplo de 3 (3 o 6) |
| `.grid-4` | 4 → 2 → 1 | 4 u 8 |
| `.metrics` | 6 → 3 (≤ 1100) → 2 | 6 |
| `.spec-list` | 2 → 1 | pares |
| `.suite` | 1,6fr + 4 → 2 con la destacada a todo el ancho (≤ 1100) → 1 | 5 |
| `.titleblock` | `--cols` (4 por defecto) → 2 (≤ 720) | los de `--cols` |

---

## Figuras

Hay dos vocabularios de SVG y **no llevan colores literales**: todo va por clases
y variables CSS.

**`.slope-svg`** (en `site.css`): el análisis calculado por el programa, generado
desde el JSON de resultados por `desarrollo/herramientas/generar_svg_talud.py` e
inyectado entre `<!-- svg:NOMBRE -->` y `<!-- /svg:NOMBRE -->`. Clases:
`.st-0`…`.st-3` (estratos), `.contact`, `.outline`, `.wt` (nivel freático) con
`.wt-mark` y `.wt-tick`, `.weak` (capa débil), `.pond`/`.pond-line` (agua
embalsada), `.drain`, `.sf` (superficies de búsqueda), `.centres circle`,
`.slices path`, `.critical` y `.crit-centre`. Cada superficie lleva en su `style`
`--f` (0 = la crítica, 1 = factor alto: da el color y la opacidad) y `--i` (orden
de aparición: da el retardo de la animación); cada centro, solo `--f`.

**`.dg`** (también en `site.css`, para que lo usen las páginas que no cargan
`docs.css`): los diagramas dibujados a mano de la documentación, de `examples/` y de
la 404, con `.ln`, `.thin`, `.dash`, `.crit`, `.grn`, `.wat`, `.frc` + `.arrowhead`,
rellenos `.s0`–`.s3`, `.hl`, y `text` en mono (`text.it` para símbolos en
cursiva serif). Cada SVG lleva `viewBox`, `role="img"` y un `<title>`. Los
marcadores (`<marker>`) llevan `id` único en la página. **Una figura tiene que ser
verdadera**: una dovela dibujada con fuerzas que no actúan en ese método es un
error.

Los iconos son SVG en línea con `viewBox="0 0 24 24"` y `stroke-width` entre 1,6
y 2.

### Animación

La única animación es la de la figura del talud: aparecen los centros y las
superficies, se dibuja la crítica y entran las dovelas y su centro. Se activa con
la clase `.animate`: fija en la portada, y en `examples/` con `data-animate`, que
el JS convierte en `.animate` cuando la figura entra en pantalla (25 % visible).
Sin JS no se oculta nada: las reglas que ocultan los elementos solo valen bajo
`.js [data-animate]:not(.animate)`. `prefers-reduced-motion` la anula. Una figura
nueva con animación debe llevar `--f` y `--i`.

### Pestañas

`.tabs` necesita el marcado completo: `.tablist[role=tablist]` con
`button[role=tab][id][aria-controls][data-key]` y un
`.tabpanel[role=tabpanel][id][aria-labelledby]` por pestaña, con `hidden` en todos
menos el primero. `data-group` en `.tabs` sincroniza las pestañas del mismo grupo
entre bloques y recuerda la elección (`localStorage`, clave `ogr-tab-<grupo>`).
Sin JS se ven todos los paneles.

---

## Puntos de ruptura

Los reales, por archivo: `site.css` **1100 · 960 · 720** px; `docs.css` **1280 ·
1024 · 720** px. No inventes otros.

| Ancho | Qué cambia |
|---|---|
| ≤ 1280 | Desaparece «En esta página» (`.doc-toc`): la documentación pasa a dos columnas |
| ≤ 1100 | Menú compacto, el botón de GitHub pierde su texto, `.suite` a 2 columnas, `.metrics` 6 → 3, pie 5 → 3 columnas |
| ≤ 1024 | El índice lateral de la documentación pasa a cajón (botón *Contents*), una columna |
| ≤ 960 | Se ocultan el menú de escritorio, el selector EN/ES y el botón de GitHub: aparecen el botón de menú y `.mobile-nav`. Hero, `.grid-2`, `.sec-head`, `.cta-band` y `.people` a una columna; `.grid-3`, `.grid-4`, `.gallery` y `.feature-grid` a dos; `.spec-list` a una |
| ≤ 720 | `--gutter` 18 px, secciones de 64 px, `.metrics` a 2, todas las rejillas a 1, `.titleblock` a 2, pie a 2; se oculta el botón «Get OGR Slip2D» de la barra; en docs el número de ecuación pasa bajo la fórmula |

Comprueba siempre a **375 px**, **768 px** y **1440 px**: caen en tres regímenes
distintos (móvil, de una columna; tableta, con el menú colapsado y el índice de la
documentación en cajón; escritorio, con la documentación a tres columnas). Si
tocas la maqueta de la documentación, mira también entre 1024 y 1280 px (índice
fijo, sin «en esta página»).

El `body` lleva `overflow-x: hidden`, así que un desbordamiento no se ve pero rompe
el ancho: búscalo con las herramientas de desarrollo, no a ojo (las tablas, las
ecuaciones destacadas y el código se desplazan solos; lo demás no debe salirse).
`/revisar` trae el fragmento de consola que lo lista.

## Prohibido sin permiso explícito

- Cambiar cualquier token, tipografía, radio, sombra o espaciado.
- Modo oscuro. La web es clara a propósito.
- Animaciones nuevas. Aparte de la figura del talud solo hay transiciones de
  interfaz (hover, menú, cajón lateral).
- Librerías de CSS o de iconos.
- Un `<style>` en las páginas, o CSS nuevo fuera de `site.css` y `docs.css`.
- Colores literales en CSS o en SVG nuevos.
- Decoración nueva: gradientes de relleno, sombras difusas o de color, esquinas
  más redondeadas. El único «cristal» es el desenfoque de la barra superior y de
  la subnavegación fijas.
- Crear un componente nuevo sin preguntar.
