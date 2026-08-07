# Mapa de `index.html`

La página entera está en un archivo. Este mapa evita tener que leerlo
completo para tocar una línea. **Los números de línea son orientativos y
envejecen; los comentarios `<!-- ====== ====== -->` no.** Busca por el
comentario, no por el número.

Referencia tomada en v0.1.59 de la web (~1030 líneas).

## Bloques

| Líneas ≈ | Marca | Contenido |
|---|---|---|
| 1–11 | `<head>` | Meta, `canonical`, tipografías de Google |
| 12–482 | `<style>` | **Todo el CSS.** Ver más abajo |
| 486 | `<!-- TOP -->` | Barra superior fija, `nav.primary` |
| 504 | `<!-- HERO -->` | Titular, botones, tarjeta `.specimen`, tira `.stats` |
| 577 | `<!-- PROJECT -->` | `#project` — por qué existe, rejilla `.feat-grid` |
| 623 | `<!-- SOFTWARE -->` | `#software` — OGR Slip2D: `.sw-sub`, capturas `.screens`, ficha `.specs` |
| 753 | `<!-- SUITE ROADMAP -->` | `#suite` — las cinco filas `.suite-row` |
| 815 | `<!-- TEAM -->` | `#team` — personas, tarjeta `.attrib`, `.affils` |
| 938 | `<!-- CONTRIBUTE -->` | `#contribute` — tres `.channel` sobre fondo tinta |
| 983 | `<!-- FOOTER -->` | Columnas de enlaces y línea legal |

## Dentro del `<style>`

Ordenado por secciones comentadas, en este orden:

`:root` (tokens) → reset → typography → shell → top bar → hero →
stat strip → section base → project → software showcase → specs strip →
suite roadmap → team → affiliations → attribution → contribute →
footer → utility.

Los tokens y los componentes están documentados en la skill
[`diseno-web`](../.claude/skills/diseno-web/SKILL.md). **No edites este
bloque sin haberla leído y sin permiso explícito.**

## Dónde vive cada dato que envejece

Esto es lo que hay que revisar en cada sincronización con el programa:

| Dato | Aparece en |
|---|---|
| **Versión** (`v0.1.59`) | `.eyebrow` del hero · `.stats` («Source available») · `.sw-status` · línea legal del pie |
| **Licencia** (`AGPL-3.0-or-later`) | `.eyebrow` del hero · `.stats` · `#project .meta` · `.specs` · tarjeta `.attrib` · pie (enlaces y línea legal) · `<meta name="description">` |
| **Capacidades** | `.sw-sub` de `#software` · las 12 filas de `.specs` |
| **Estado de los 5 programas** | `.status-cell` de cada `.suite-row` |
| **Enlaces al repositorio** | botón del hero · canal 01 y 02 de `#contribute` · tarjeta de Samuel · columna *Resources* y *Connect* del pie |
| **Año del copyright** | línea legal del pie |

## Assets

| Ruta | Uso | Peso |
|---|---|---|
| `assets/screens/hero-analysis.png` | tarjeta `.specimen` del hero | 116 KB |
| `assets/screens/01-modeler.png` | fig 01 | 168 KB |
| `assets/screens/02-interpret.png` | fig 02 | 129 KB |
| `assets/screens/03-materials.png` | fig 03 | 26 KB |
| `assets/screens/04-surfaces.png` | fig 04 | 25 KB |
| `assets/people/samuel.jpg` | tarjeta del equipo | **4,3 MB ⚠️** |
| `assets/people/emilio.jpg` | avatar de 56 px | 9 KB |
| `assets/logos/upct.png` | `.affil` | 28 KB |
| `assets/logos/imga.png` | `.affil` | **1,0 MB ⚠️** |

Las dos marcadas superan con mucho el presupuesto de 300 KB por imagen y
son la mayor deuda de rendimiento de la página. `samuel.jpg` se muestra a
unos 500 px de ancho: pesa unas **40 veces** lo que necesita.

## Lo que la página deliberadamente NO tiene

Para que nadie lo "arregle" sin preguntar:

- **Sin JavaScript de aplicación.** Ni un `<script>` propio.
- **Sin menú hamburguesa.** Por debajo de 820 px el menú se oculta y solo
  queda el botón *Contribute*.
- **Sin modo oscuro.**
- **Sin analítica ni cookies.** La única petición externa son las
  tipografías de Google.
- **Sin favicon** (hoy). Es una carencia real, no una decisión.
- **Sin `og:image` ni tarjetas de Twitter.** Compartir el enlace no muestra
  previsualización.
