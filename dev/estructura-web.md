# Mapa del sitio

El sitio es **multipágina y bilingüe**: inglés en `/` y español en `/es/`, con las
mismas rutas. Este mapa evita tener que leerlo entero para tocar una línea: qué es
cada página, qué partes las escriben las herramientas, qué componentes aparecen
dónde, cuánto pesa cada recurso y qué datos envejecen. Los comentarios
`<!-- ====== NOMBRE ====== -->` de las páginas principales y los `id` de las secciones
son el índice de cada archivo: busca por ellos, no por número de línea.

**Los tamaños se midieron el 2026-10-02 sobre la versión 0.1.235 del programa y envejecen**
(KB = 1024 bytes); el comando para volver a medirlos está al final. Lo que este mapa
afirma de la estructura se puede comprobar con `python tools/sitio.py --check` y con
`tools/site.json`.

## 1. Cómo está montado

```
tools/site.json  ──┐   capítulos de la documentación, menú activo, versión, enlaces
tools/partials/  ──┼─► tools/sitio.py ─► regiones <!-- @inc … --> de cada página,
                   │                      numeración, referencias, buscador, sitemap
páginas EN (a mano)├─► tools/render_math.cjs ─► ecuaciones compuestas <!--k-->…<!--/k-->
                   └─► ../desarrollo/herramientas/traduccion.py ─► es/… (mismas rutas)

assets/css/site.css · assets/css/docs.css · assets/js/site.js   (los comparten todas)
```

1. **Las páginas** son HTML escrito a mano, en inglés. Cada una lleva `<title>`,
   `<meta name="description">`, su contenido y los marcadores de región.
2. **Las regiones** `<!-- @inc … -->` las rellena `tools/sitio.py` (sección 5). Ahí
   están la cabeza del documento, la cabecera, el pie y las piezas de la
   documentación. No se editan a mano.
3. **Lo compartido**: un CSS para todo el sitio, uno más para `docs/` y un JS.
   Ninguna página lleva `<style>` ni `<script>` propios.
4. **`es/`** es la salida de `traduccion.py montar`, que parte de
   `../desarrollo/traduccion/<clave>.es.html`.

## 2. Árbol de carpetas

```
WEB_OGR_v2/
├── index.html · 404.html · sitemap.xml · CNAME · .nojekyll
├── products/   index.html · slip2d.html
├── ai/ · examples/ · verification/ · download/ · about/      (un index.html cada una)
├── docs/       index.html y los cinco capítulos (la lista, en la sección 4)
│   └── getting-started/ · user-guide/ · theory/ · verification/ · reference/
├── es/         la misma estructura en español (y su 404.html)
├── assets/
│   ├── css/    site.css · docs.css
│   ├── js/     site.js · search-index.en.js · search-index.es.js (estos dos, generados)
│   ├── img/    shots/ · people/ · logos/ · iconos y og-image.png
│   ├── models/ los .ogr de los ejemplos
│   └── vendor/katex/   katex.min.css · LICENSE.txt · fonts/ (20 .woff2)
├── tools/      sitio.py · render_math.cjs · site.json · partials/ · vendor/ (katex.min.js)
├── dev/        estructura-web.md · guia-documentacion.md · plantilla-doc.html · changelog/
├── spec/       constitution/ · features/
├── .claude/    commands/ · skills/ · settings.json
└── AGENTS.md · CLAUDE.md · README.md · .mcp.json · .gitignore · .vscode/
```

Fuera del repositorio, en `C:\Samuel\OpenGeoRock_Slip2d\web-OGR\desarrollo\` (desde la
raíz de este repo, `../desarrollo/`): notas, modelos `.ogr` de los que salen las
figuras, capturas en bruto, herramientas de producción y el trabajo de traducción.
Ver `AGENTS.md`.

## 3. Páginas principales

| Ruta | Contenido | `data-nav` | EN | ES |
|---|---|---|---|---|
| `index.html` | Portada: héroe con el SVG de un análisis real, la suite, OGR Slip2D, IA y MCP, verificación, licencia | — | 46 KB | 48 KB |
| `products/index.html` | La suite: los cinco programas por categoría y las cuatro formas de usarlos | `products` | 17 KB | 18 KB |
| `products/slip2d.html` | Ficha de OGR Slip2D con subnavegación fija: métodos, agua, probabilístico, diseño, flujo, ficha técnica | `products` | 70 KB | 72 KB |
| `ai/index.html` | Servidor MCP: qué es, una sesión real, instalación por cliente (pestañas), ventana compartida, herramientas, seguridad, preguntas | `ai` | 36 KB | 38 KB |
| `examples/index.html` | Cinco ejemplos resueltos, cada uno con su figura calculada, sus datos y su modelo `.ogr` | `examples` | 126 KB | 128 KB |
| `verification/index.html` | Verificación: la regla, los casos publicados, las soluciones cerradas y la batería de tests | `verification` | 22 KB | 23 KB |
| `download/index.html` | Instalación desde el código fuente en Windows, macOS y Linux; estado de los instaladores | `download` | 17 KB | 18 KB |
| `about/index.html` | Principios, equipo y afiliaciones, licencia en la práctica, cómo contribuir y cómo citar | `about` | 22 KB | 23 KB |
| `docs/index.html` | Portada de la documentación: buscador y los cinco capítulos | `docs` | 19 KB | 19 KB |
| `404.html` | Página de error de GitHub Pages; rutas absolutas desde la raíz | — | 12 KB | 12 KB |

`data-nav` es la clave de `nav_sections` en `tools/site.json`: la entrada del menú
que `sitio.py` marca con `aria-current="page"` según la carpeta de la página. La
portada y la 404 no marcan ninguna.

Secciones de cada página (los comentarios `<!-- ====== … ====== -->`):

- `index.html`: HERO · SUITE · SLIP2D · AI / MCP · VERIFICATION · OPEN · CTA
- `products/index.html`: SLOPE STABILITY · FINITE ELEMENTS · DATA · INTERFACES
- `products/slip2d.html`: HERO · OVERVIEW · LEM · GROUNDWATER · PROBABILISTIC · DESIGN · WORKFLOW · SPECS · VERIFICATION
- `ai/index.html`: HERO · WHAT · DEMO · INSTALL · WINDOW · TOOLS · SECURITY · PROMPTS · FAQ
- `examples/index.html`: HERO · EJEMPLO 1 · EJEMPLO 2 · EJEMPLO 3 · EJEMPLO 4 · EJEMPLO 5
- `verification/index.html`: PRINCIPLE · BENCHMARKS · ANALYTIC · SUITE
- `about/index.html`: PRINCIPLES · TEAM · LICENCE · CONTRIBUTE · CITE

`docs/index.html` y `404.html` no llevan esos comentarios.

**La 404.** GitHub Pages sirve `404.html`, y solo la de la raíz, para cualquier ruta
inexistente y a cualquier profundidad; por eso usa rutas absolutas desde la raíz
(`data-root="/"`). `es/404.html` solo se alcanza desde el selector de idioma de la
propia 404. En total: 44 páginas en inglés (5,2 MB) y 44 en
español (5,3 MB).

## 4. Documentación

Cinco capítulos, con su estructura (números, `slug`, títulos EN/ES y orden) en
`tools/site.json` → `docs`. Añadir una página es añadirla ahí y crear el archivo
desde `dev/plantilla-doc.html`. Cómo se escribe: `dev/guia-documentacion.md`.

**1 · Getting started** (`docs/getting-started/`) — Install OGR Slip2D, build and analyse your first slope, and find your way around the program.

| Nº | Archivo | Título | EN | ES |
|---|---|---|---|---|
| 1.1 | `installation.html` | Installation | 26 KB | 27 KB |
| 1.2 | `quick-start.html` | Quick start: your first model | 53 KB | 54 KB |
| 1.3 | `interface.html` | The interface | 63 KB | 67 KB |

**2 · User guide** (`docs/user-guide/`) — Every step of a model in the order you build it: geometry, materials, water, loads, supports, search and results.

| Nº | Archivo | Título | EN | ES |
|---|---|---|---|---|
| 2.1 | `project-settings.html` | Project settings | 78 KB | 81 KB |
| 2.2 | `geometry.html` | Geometry and boundaries | 53 KB | 56 KB |
| 2.3 | `materials.html` | Materials | 73 KB | 75 KB |
| 2.4 | `water.html` | Water and pore pressure | 74 KB | 77 KB |
| 2.5 | `loads.html` | Loads and seismic loading | 49 KB | 51 KB |
| 2.6 | `supports.html` | Supports | 45 KB | 48 KB |
| 2.7 | `surfaces.html` | Slip surfaces and search | 78 KB | 82 KB |
| 2.8 | `results.html` | Computing and interpreting results | 41 KB | 44 KB |
| 2.9 | `groundwater.html` | Finite-element groundwater | 42 KB | 45 KB |
| 2.10 | `probabilistic.html` | Probabilistic and sensitivity analysis | 53 KB | 55 KB |
| 2.11 | `design-standards.html` | Design standards | 33 KB | 35 KB |
| 2.12 | `automation.html` | Reports, scripting and the command line | 32 KB | 34 KB |

**3 · Theory manual** (`docs/theory/`) — The equations OGR Slip2D solves, with their assumptions, their original sources and how they are implemented.

| Nº | Archivo | Título | EN | ES |
|---|---|---|---|---|
| 3.1 | `limit-equilibrium.html` | Limit equilibrium and the factor of safety | 85 KB | 87 KB |
| 3.2 | `methods.html` | Methods of slices | 452 KB | 456 KB |
| 3.3 | `interslice.html` | Interslice forces, convergence and admissibility | 247 KB | 251 KB |
| 3.4 | `search.html` | Slip-surface search | 387 KB | 394 KB |
| 3.5 | `strength.html` | Shear strength models | 570 KB | 574 KB |
| 3.6 | `pore-pressure.html` | Pore pressure and unsaturated strength | 322 KB | 328 KB |
| 3.7 | `seepage.html` | Finite-element seepage | 352 KB | 356 KB |
| 3.8 | `rapid-drawdown.html` | Rapid drawdown | 258 KB | 260 KB |
| 3.9 | `seismic.html` | Seismic analysis | 248 KB | 251 KB |
| 3.10 | `supports.html` | Support forces | 347 KB | 351 KB |
| 3.11 | `probabilistic.html` | Probabilistic analysis | 223 KB | 225 KB |
| 3.12 | `partial-factors.html` | Partial factors (Eurocode 7) | 149 KB | 151 KB |

**4 · Verification** (`docs/verification/`) — How results are checked against published cases and closed-form solutions, case by case.

| Nº | Archivo | Título | EN | ES |
|---|---|---|---|---|
| 4.1 | `methodology.html` | Verification methodology | pendiente | pendiente |
| 4.2 | `slope-benchmarks.html` | Limit-equilibrium benchmarks | pendiente | pendiente |
| 4.3 | `analytic-checks.html` | Groundwater and analytic checks | pendiente | pendiente |

**5 · Reference** (`docs/reference/`) — The MCP server, the command line, the Python API, the file format, error codes, notation and bibliography.

| Nº | Archivo | Título | EN | ES |
|---|---|---|---|---|
| 5.1 | `mcp.html` | MCP server | 87 KB | 93 KB |
| 5.2 | `cli.html` | Command-line interface | 45 KB | 48 KB |
| 5.3 | `python-api.html` | Python API | 41 KB | 43 KB |
| 5.4 | `file-format.html` | The .ogr file format | 40 KB | 42 KB |
| 5.5 | `error-codes.html` | Error codes | 48 KB | 51 KB |
| 5.6 | `notation.html` | Notation and glossary | 181 KB | 183 KB |
| 5.7 | `bibliography.html` | Bibliography | 41 KB | 42 KB |

Páginas declaradas en `site.json`: 37. Escritas en inglés: 34 (4,8 MB); en
español: 34 (4,9 MB). Pendientes en inglés: `docs/verification/methodology.html`, `docs/verification/slope-benchmarks.html`, `docs/verification/analytic-checks.html`. Las páginas de
teoría pesan de 85 KB a 570 KB porque llevan las ecuaciones ya compuestas
(KaTeX con salida HTML y MathML) y figuras SVG en línea.

## 5. Regiones `<!-- @inc … -->`

`tools/sitio.py` sustituye lo que hay entre `<!-- @inc X -->` y `<!-- @end X -->`.
Es idempotente: se puede lanzar cuantas veces se quiera.

| Región | La rellena | Dónde está | Contenido |
|---|---|---|---|
| `head` | `tools/partials/head.html` (+ `site.json`) | todas, dentro de `<head>` | viewport, `canonical`, `hreflang` EN/ES/x-default, Open Graph y Twitter (de `<title>` y `description`), iconos, tipografías, `site.css`, `docs.css` (rutas `docs/…`), `katex.min.css` (páginas con `data-tex`), `site.js` (1,4 KB) |
| `header` | `tools/partials/header.en.html` · `header.es.html` | todas, tras `<body>` | enlace «Skip to content», barra con mega-menú, selector EN/ES, menú móvil; marca la entrada activa (5,1 KB · 5,3 KB) |
| `footer` | `tools/partials/footer.en.html` · `footer.es.html` | todas, antes de `</body>` | columnas de enlaces, línea legal con la versión y su fecha, selector de idioma; en EN, el aviso «¿Prefieres leer esta web en español?» (3,1 KB · 2,9 KB) |
| `docnav` | `sitio.py` | páginas de `docs/` (no `docs/index.html`), en `aside.doc-side` | buscador y árbol de capítulos con la página actual |
| `dochead` | `sitio.py` | páginas de `docs/`, en `header.doc-head` | botón «Contents», migas, nº de capítulo, `h1` y «Describes OGR Slip2D 0.1.235» |
| `docfoot` | `sitio.py` | páginas de `docs/`, tras `</article>` | anterior/siguiente, «Edit this page», «Report a problem» |
| `pagetoc` | `sitio.py` | páginas de `docs/`, en `aside.doc-toc` | «En esta página» (h2 y h3) y botón de imprimir |
| `docgroups` | `sitio.py` | `docs/index.html` | las tarjetas de los cinco capítulos |

Además, en cada página `sitio.py`:

- reescribe `<html class="no-js" lang data-root>` (`data-root` es el camino hasta la
  raíz: vacío, `../`, `../../`…; `/` en la 404);
- escribe `<span data-v>` con la versión de `site.json`;
- **en la documentación**, numera con el número de la página (3.2, 5.7…): los `h2` como
  3.2.1, 3.2.2…, las ecuaciones `div.eq` (`data-n`), las figuras `figure.fig` y las
  tablas `figure.tbl`, con «Figure»/«Figura» y «Table»/«Tabla» en el pie; y rellena
  el texto de las referencias cruzadas `a.xref`;
- genera `assets/js/search-index.en.js` y `search-index.es.js` (una entrada por
  página y por `h2`) y `sitemap.xml` con sus alternativas `hreflang` — **solo con una
  ejecución completa**, no con `--only`;
- con `--check`: enlaces y anclas rotos, paridad EN/ES, imágenes de más de 300 KB,
  `<img>` sin `alt`, marcadores `{{…}}` olvidados y ecuaciones sin componer.

## 6. CSS y JavaScript

| Archivo | Peso | Contenido, por bloques comentados |
|---|---|---|
| `assets/css/site.css` | 38 KB | tokens · base · tipografía · maqueta · cabecera · botones · etiquetas · cabeceras de sección · héroe · lámina · figura del talud y diagramas `.dg` · cifras · tarjetas · pestañas · código · avisos · tablas · pasos · chat · listas · galería de ejemplos · personas · subnavegación fija · llamada final · aviso de idioma · pie · utilidades · responsive (1100 · 960 · 720 px) · impresión |
| `assets/css/docs.css` | 14 KB | índice lateral · columna central · ecuaciones · figuras y tablas numeradas · cajas propias de la doc · anterior/siguiente · «en esta página» · portada de la documentación · responsive (1280 · 1024 · 720 px) · impresión |
| `assets/js/site.js` | 13 KB | menú móvil · mega-menú · pestañas (grupos sincronizados y memoria) · copiar código · índice lateral de la doc (móvil) · «en esta página» y subnavegación: sección activa · buscador de la documentación · aviso de idioma · animaciones al entrar en pantalla |

Los tokens, las tipografías, los componentes y los puntos de ruptura están
documentados en la skill [`diseno-web`](../.claude/skills/diseno-web/SKILL.md).
**No edites estos archivos sin haberla leído y sin permiso explícito.** `site.js`
es mejora progresiva (sin él, la web se lee entera) y su único almacenamiento es
`localStorage`: `ogr-tab-<grupo>` (la pestaña elegida) y `ogr-lang-hint` (el aviso
de idioma descartado).

### Componentes: dónde se usan

Solo las páginas principales; en `docs/`, ver la guía de la documentación.

| Componente | Clases | Páginas |
|---|---|---|
| Héroe de la portada | `.hero`, `.hero-grid`, `.hero-note` | `index.html` |
| Cabecera de página interior | `.page-hero`, `.crumbs` | todas las principales |
| Subnavegación fija | `.subnav` | `products/slip2d.html` |
| Cifras destacadas | `.metrics` > `.metric` | `index.html`, `products/slip2d.html`, `verification/` |
| Lámina con cajetín | `.sheet`, `.corner`, `.titleblock` | `index.html`, `products/slip2d.html`, `examples/` |
| Captura del programa | `.shot` | `ai/`, `examples/`, `products/slip2d.html` |
| Figura calculada del talud | `.slope-svg` | `index.html`, `products/slip2d.html`, `examples/` y varias de `docs/` |
| Tarjetas | `.card`, `.card.ink`, `.card.planned` | `index.html`, `products/`, `about/`, `verification/`, `download/` |
| Suite de cinco programas | `.suite` | `index.html` |
| Principios con icono | `.feature-grid` | `index.html`, `products/slip2d.html`, `about/` |
| Pestañas | `.tabs` | `ai/` (clientes MCP), `download/` (sistemas), `products/slip2d.html` |
| Pasos numerados | `.steps` | `ai/` |
| Sesión de agente | `.chat` | `ai/`, `index.html` |
| Ficha clave/valor | `.spec-list` | `products/slip2d.html`, `examples/` |
| Tabla de datos | `.table-wrap` > `table.data` | casi todas |
| Aviso | `.note`, `.note.warn` | `ai/`, `about/`, `verification/`, `index.html` y casi toda la documentación |
| Código con botón de copiar | `.code` | `ai/`, `download/`, `about/` y la documentación de referencia |
| Llamada final | `.cta-band` en `.section.ink` | `index.html`, `products/`, `ai/`, `examples/`, `verification/` |
| Equipo y afiliaciones | `.people`, `.person`, `.affil` | `about/` |
| Etiquetas y estado | `.tag.live`, `.tag.soon`, `.chips` | `index.html`, `products/`, `download/`, `examples/` |

Hay clases definidas y sin uso hoy: la galería de ejemplos (`.gallery`, `.example`).

## 7. Recursos (`assets/`)

Total del repositorio sin `.git`: 12,8 MB; `assets/` pesa 1,8 MB.

### Imágenes

| Archivo | Uso | Peso |
|---|---|---|
| `assets/img/og-image.png` | vista previa al compartir (Open Graph, 1200×630); la pone la región `head` | 161 KB |
| `assets/img/apple-touch-icon.png` | icono de pantalla de inicio (180×180); región `head` | 7,0 KB |
| `assets/img/favicon-32.png` | favicon de respaldo (32×32); región `head` | 1,1 KB |
| `assets/img/favicon.svg` | favicon; región `head` | 338 B |
| `assets/img/people/samuel.webp` | tarjeta del equipo en `about/` (1200×900) | 132 KB |
| `assets/img/people/emilio.webp` | avatar en `about/` (158×158) | 3,3 KB |
| `assets/img/logos/upct.png` | afiliación en `about/` | 27 KB |
| `assets/img/logos/imga.png` | afiliación en `about/` | 40 KB |
| `assets/img/shots/boundary-conditions.webp` | `docs/user-guide/groundwater` | 20 KB |
| `assets/img/shots/define-materials.webp` | `docs/getting-started/quick-start`, `docs/user-guide/materials` | 24 KB |
| `assets/img/shots/groundwater-interpret.webp` | `docs/getting-started/interface`, `docs/theory/seepage`, `docs/user-guide/groundwater` | 40 KB |
| `assets/img/shots/histogram.webp` | `products/slip2d.html`, `examples/` | 24 KB |
| `assets/img/shots/hydraulic-properties.webp` | `docs/user-guide/groundwater` | 19 KB |
| `assets/img/shots/interpret.webp` | `products/slip2d.html`, `docs/getting-started/interface`, `quick-start` y `docs/user-guide/results` | 60 KB |
| `assets/img/shots/main-window.webp` | `products/slip2d.html` (héroe, `eager`), `ai/`, `docs/getting-started/interface` y `quick-start` | 106 KB |
| `assets/img/shots/project-settings-design.webp` | `docs/user-guide/design-standards` | 36 KB |
| `assets/img/shots/project-settings.webp` | `docs/getting-started/quick-start`, `docs/user-guide/project-settings` | 33 KB |
| `assets/img/shots/qs-geometry.webp` | `docs/getting-started/quick-start` | 32 KB |
| `assets/img/shots/random-variables.webp` | `docs/user-guide/probabilistic` | 38 KB |
| `assets/img/shots/seepage.webp` | `products/slip2d.html` | 37 KB |
| `assets/img/shots/statistics-convergence.webp` | `docs/theory/probabilistic` | 34 KB |
| `assets/img/shots/statistics-window.webp` | `docs/getting-started/interface`, `docs/theory/probabilistic`, `docs/user-guide/probabilistic` | 27 KB |
| `assets/img/shots/surface-options.webp` | `docs/user-guide/surfaces` | 40 KB |

Las capturas del programa son de la interfaz en inglés. Ninguna imagen supera los
300 KB.

### Modelos `.ogr`

| Archivo | Ejemplo | Peso |
|---|---|---|
| `assets/models/ej01-two-layer-slope.ogr` | 1 · talud de dos capas con nivel freático (también en `docs/getting-started/quick-start`) | 8,3 KB |
| `assets/models/ej02a-embankment-no-berm.ogr` | 2 · terraplén con capa débil, sin berma | 8,9 KB |
| `assets/models/ej02b-embankment-berm.ogr` | 2 · el mismo terraplén con berma | 8,9 KB |
| `assets/models/ej03-earth-dam-toe-drain.ogr` | 3 · presa de tierras con dren de pie: filtración estacionaria y estabilidad | 157 KB |
| `assets/models/ej04-two-layer-slope-probabilistic.ogr` | 4 · el talud de dos capas con resistencias inciertas | 9,1 KB |
| `assets/models/ej05-earth-dam-drawdown.ogr` | 5 · desembalse rápido como problema de filtración transitoria | 392 KB |

Son texto (JSON) y los descargan los ejemplos de `examples/`. Los modelos de partida,
con sus resultados, viven en `../desarrollo/modelos-ogr/`.

### KaTeX

`assets/vendor/katex/`: `katex.min.css` (24 KB), `LICENSE.txt`
y `fonts/` (20 archivos `.woff2`, 254 KB). KaTeX 0.19.0 (MIT). El motor
que compone las ecuaciones, `katex.min.js` (266 KB), vive en
`tools/vendor/` y **no se sirve**.

### Generados

`assets/js/search-index.en.js`, `assets/js/search-index.es.js` y `sitemap.xml`: los
escribe `tools/sitio.py` **solo en una ejecución completa** (no con `--only`), y
crecen con cada página nueva. No se editan a mano.

## 8. Dónde vive cada dato que envejece

Esto es lo que hay que revisar en cada sincronización con el programa
(`/sincronizar`):

| Dato | Fuente en la web | Aparece en |
|---|---|---|
| **Versión** del programa (`0.1.235`) | `tools/site.json` (`version`, `version_date`) | Escrita sola, con `<span data-v>`: portada, `products/`, `download/`, `examples/`, `verification/`, `docs/` («Describes OGR Slip2D…») y el pie, con su fecha. **Escrita a mano** en las notas ligadas a una versión (`grep -rn "0.1.235"` descartando `data-v`): sobre todo `docs/getting-started/interface.html` y `docs/user-guide/` |
| Versiones históricas («desde v0.1.xxx») | — | `about/` (cambio de licencia), `ai/` (servidor y puente de ventana), `docs/reference/`: son hechos pasados |
| **Licencia** (`AGPL-3.0-or-later`) | — | portada, `products/slip2d.html`, `products/` y `about/` (en palabras), `ai/`, `docs/user-guide/automation.html`, pie |
| Métodos, búsquedas, modelos de resistencia, tipos de soporte, distribuciones | — | portada, `products/`, `products/slip2d.html` (cifras, pestañas y ficha técnica), `ai/`, `docs/theory/`, `docs/user-guide/`, `docs/reference/cli.html` y `python-api.html` |
| Herramientas MCP, acciones de menú y perfil compacto | — | `ai/index.html`, `docs/reference/mcp.html`, portada, `products/`, `products/slip2d.html` |
| Número de tests | — | portada, `products/slip2d.html`, `verification/`, `examples/`, `docs/getting-started/installation.html`, `docs/theory/search.html` |
| Casos de validación y comprobaciones | `../desarrollo/notas/validacion-v0.1.235.json` | `verification/`, portada, `products/slip2d.html`, `examples/`, `docs/theory/probabilistic.html`; el capítulo 4 de la documentación los repetirá |
| Estado de los cinco programas | — | `products/index.html`, portada (suite), menú (`tools/partials/header.*`), `download/` (instaladores *planned*) |
| Resultados de los ejemplos (p. ej. el factor de seguridad del ejemplo 1) | `../desarrollo/modelos-ogr/` | `examples/`, héroe de la portada, `products/slip2d.html`, `ai/`, `docs/getting-started/quick-start.html` y páginas de teoría |
| Requisito de Python | — | `download/`, `ai/`, portada, `products/slip2d.html`, `verification/`, `docs/getting-started/installation.html`, `docs/reference/mcp.html` |
| Enlaces al repositorio, a `issues`, al changelog y a `LICENSE` | `tools/site.json` (`repo_program`, `repo_web`) | `tools/partials/header.*` y `footer.*`, `about/`, `download/`, `ai/`, `verification/` y el pie de cada página de `docs/` |
| Año del copyright y correo de contacto | — | pie (`tools/partials/footer.*`), `about/` |

## 9. Lo que el sitio deliberadamente NO tiene

Para que nadie lo «arregle» sin preguntar:

- **Sin build de despliegue, sin `package.json`, sin frameworks.** Lo versionado es lo
  servido; las herramientas de `tools/` son locales y su salida se versiona.
- **Sin analítica ni cookies.** La única petición externa son las tipografías de
  Google. El único almacenamiento es `localStorage`, para dos preferencias de
  interfaz.
- **Sin modo oscuro.**
- **Sin formularios ni backend.** El contacto es un `mailto:`.
- **Sin blog ni sección de noticias.**
- **Sin `robots.txt`, sin integración continua ni tests automáticos.** La comprobación
  es `sitio.py --check` más la revisión manual de `/revisar`.
- **Sin `.github/`**: Pages publica la rama `main` tal cual.

## 10. Cómo volver a medir

```bash
# pesos de páginas y recursos
find . -name '*.html' -not -path './tools/*' -not -path './dev/*' -printf '%s %p\n' | sort -n | tail
du -sb assets assets/img assets/models assets/vendor

# lo que falta en un idioma, páginas pendientes, imágenes de más de 300 KB
python tools/sitio.py --check
```
