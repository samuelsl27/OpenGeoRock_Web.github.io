# OpenGeoRock — sitio web

Sitio público de la suite **OpenGeoRock** en [opengeorock.org](https://opengeorock.org).
Sitio estático **multipágina y bilingüe** (inglés en `/`, español en `/es/`):
presenta el proyecto y el programa **OGR Slip2D**, su servidor MCP para agentes
de IA, ejemplos con modelos descargables, la verificación del programa y una
documentación científica en cinco capítulos (primeros pasos, guía de usuario,
manual de teoría, verificación y referencia).

**Dos repositorios, y conviene no confundirlos:**

| Repositorio | Qué es |
|---|---|
| `OpenGeoRock_Web.github.io` | **este**: la web. HTML estático, sin build de despliegue |
| [`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D) | el programa. Python, es la **fuente de verdad** de todo dato técnico |

Autor y titular del copyright: Samuel Sáez López (UPCT).
El programa es AGPL-3.0-or-later; esta web documenta ese hecho, no lo decide.

> Este archivo es el **contrato de trabajo** con cualquier agente de IA.
> Se consulta antes de cada acción. Si algo aquí contradice lo que parece
> razonable, gana este archivo — y si de verdad está mal, dilo antes de
> saltártelo.

**Qué leer antes de tocar cada cosa:**

| Vas a… | Lee antes |
|---|---|
| localizar una página, una región o un recurso | `dev/estructura-web.md` (el mapa) |
| cambiar algo que se ve: CSS, marcado nuevo, una figura | `.claude/skills/diseno-web/SKILL.md` |
| crear o editar una página, una imagen o un enlace; publicar | `.claude/skills/html-estatico/SKILL.md` |
| escribir una cifra, una limitación, una cita, una traducción | `.claude/skills/contenido-tecnico/SKILL.md` |
| escribir o traducir una página de `docs/` | `dev/guia-documentacion.md` y `dev/plantilla-doc.html` |

---

## Stack

- **HTML5 estático multipágina.** Cada página es un `.html` completo. La cabeza
  del documento, la cabecera, el pie y las piezas repetidas de la documentación
  son regiones `<!-- @inc … -->` que rellena `tools/sitio.py` desde
  `tools/partials/` y `tools/site.json`.
- **CSS y JavaScript compartidos**: `assets/css/site.css` (el sistema de diseño),
  `assets/css/docs.css` (solo `docs/`) y `assets/js/site.js`. JavaScript
  **vanilla, sin frameworks**; mejora progresiva: sin JS la web se lee entera.
  Ni `<style>` ni `<script>` propios dentro de las páginas.
- **Ecuaciones: KaTeX pre-renderizado.** Se escriben como `data-tex` y
  `tools/render_math.cjs` inserta el HTML ya compuesto. Al navegador solo llegan
  el CSS y las fuentes de `assets/vendor/katex/`; no se carga ningún script de
  KaTeX.
- **Tipografías**: Inter, Newsreader y JetBrains Mono desde Google Fonts.
- **Sin build de despliegue, sin gestor de paquetes.** Lo que hay en el
  repositorio es exactamente lo que sirve GitHub Pages. Las herramientas de
  `tools/` (Python con su biblioteca estándar y Node **sin `package.json`**) se
  ejecutan en local y **su salida se versiona**.
- **Despliegue**: GitHub Pages desde `main`, dominio propio vía `CNAME`
  (`opengeorock.org`). El `.nojekyll` de la raíz (vacío) evita que Pages procese
  el sitio con Jekyll.

## Comandos

```bash
python -m http.server 8000                       # servidor local → http://localhost:8000 (y /es/)
node tools/render_math.cjs docs/theory/x.html    # compone las ecuaciones de esas páginas (sin argumentos: todas)
python tools/sitio.py                            # sincroniza regiones, numeración, índice de búsqueda y sitemap
python tools/sitio.py --only docs/theory/x.html  # solo esas páginas (no toca índice ni sitemap)
python tools/sitio.py --check                    # lo anterior + enlaces, anclas, paridad EN/ES, imágenes
git status && git diff --stat                    # ver qué cambió antes de publicar
git push origin main                             # publica: Pages redespliega solo
```

Traducción al español (la herramienta vive fuera del repo; ver «Fuera del repositorio»):

```bash
python ../desarrollo/herramientas/traduccion.py preparar  docs/theory/x.html   # deja la página «ligera» para traducir
python ../desarrollo/herramientas/traduccion.py comprobar docs/theory/x.html   # compara la traducción con el original
python ../desarrollo/herramientas/traduccion.py montar    docs/theory/x.html   # escribe es/docs/theory/x.html
node tools/render_math.cjs es/docs/theory/x.html && python tools/sitio.py --only es/docs/theory/x.html
```

Las dos herramientas de `tools/` son **idempotentes**: relanzarlas con todo
sincronizado no cambia nada. `sitio.py --check` siempre sincroniza primero y
comprueba después; no existe una comprobación de solo lectura.

**`git push` sobre `main` publica en producción.** No hay entorno de pruebas
intermedio. Revisa en local antes (`/revisar`, `/publicar`).

## Estructura del proyecto

| Ruta | Contenido |
|---|---|
| `index.html` | Portada |
| `products/`, `ai/`, `examples/`, `verification/`, `download/`, `about/` | Páginas principales (`products/slip2d.html` es la ficha del programa) |
| `docs/` | Documentación en cinco capítulos: `getting-started/`, `user-guide/`, `theory/`, `verification/`, `reference/`. Capítulos, títulos EN/ES y orden: `tools/site.json` |
| `es/` | La copia en español, con **las mismas rutas**. Es la salida de `traduccion.py montar` |
| `404.html` | Página de error de GitHub Pages (rutas desde la raíz) |
| `assets/css/`, `assets/js/` | `site.css`, `docs.css`, `site.js` y los índices de búsqueda `search-index.{en,es}.js` (generados) |
| `assets/img/` | `shots/` (capturas del programa), `people/`, `logos/`, iconos y `og-image.png` |
| `assets/models/` | Los `.ogr` que descargan los ejemplos |
| `assets/vendor/katex/` | CSS, fuentes y licencia de KaTeX 0.19.0 |
| `tools/` | `sitio.py`, `render_math.cjs`, `site.json`, `partials/` y `vendor/` (el `katex.min.js` que usa `render_math.cjs`) |
| `dev/` | Mapa del sitio, guía y plantilla de la documentación, `changelog/` |
| `spec/` | Especificaciones SDD: constitución y features |
| `.claude/` | Comandos y skills del agente |
| `.mcp.json` | Servidor MCP del proyecto (Context7); su clave va en `CONTEXT7_API_KEY`, nunca en el archivo |
| `sitemap.xml` | Generado por `sitio.py` |
| `CNAME` | Dominio propio. **No tocar** |

### Fuera del repositorio

Notas, borradores, capturas en bruto y herramientas de producción **no viven
aquí** sino en `C:\Samuel\OpenGeoRock_Slip2d\web-OGR\desarrollo\` (desde la raíz
de este repo, `../desarrollo/`). No se versiona: en un clon nuevo no existe, y
los flujos de traducción y de figuras dependen de ella. Sus carpetas:

- `notas/`: decisiones del rediseño, fichas del programa, anomalías encontradas,
  pendientes de la documentación, verificación de la bibliografía.
- `modelos-ogr/`: los `.ogr` y los resultados JSON de los que salen las figuras y
  los ejemplos.
- `herramientas/`: `traduccion.py`, los `generar_svg_*.py`, `inyectar_svg.py`,
  `optimizar_imagenes.py`, `capturar.ps1`, `recalcular_validacion.py`.
- `traduccion/`: el trabajo de traducción por página y `INSTRUCCIONES.md`, con el
  glosario.
- `capturas-raw/`, `capturas-web/`, `propuestas/`: capturas del programa sin
  optimizar, capturas de la web para revisarla y las propuestas visuales A/B/C
  (se eligió la A).

---

## Las ocho reglas

### 1. La estética no se cambia sin permiso explícito

El diseño es la dirección **A «Cuaderno técnico»** y está cerrado: papel cálido,
tinta, un verde de marca, el bermellón reservado a la superficie crítica de
rotura, tres tipografías con papeles fijos y solo modo claro. Sus tokens están
en el `:root` de `assets/css/site.css`. **No propongas ni apliques rediseños,
modo oscuro, librerías de UI, animaciones nuevas ni cambios de paleta,
tipografía, espaciado o layout por iniciativa propia.**

Puedes cambiar **texto, datos y enlaces** libremente. Para cualquier cosa que
altere cómo se *ve* la web —o cómo se comporta— pregunta primero y espera el
OK: tocar `site.css`, `docs.css` o `site.js`, o inventar un componente. Los
parciales de `tools/partials/` se editan para menús y enlaces (siempre EN y ES
a la vez), no para cambiar su aspecto.

Añadir contenido dentro de un componente que ya existe (una fila más en una
`.spec-list`, un ejemplo más, una página de documentación hecha con la
plantilla) **no** es un cambio estético. Inventar un componente, sí.

Tokens, tipografías, componentes y puntos de ruptura:
`.claude/skills/diseno-web/SKILL.md`. Léelo antes de tocar nada visible.

### 2. Todo dato técnico sale del repositorio de OGR-Slip2D y se coteja con su versión

Versión, licencia, número de métodos, búsquedas, modelos de resistencia y
herramientas MCP, valores por defecto, menús, diálogos, tests: la fuente es el
repositorio del programa —`pyproject.toml`, su código, `docs/changelog/`,
`validacion/`— **no** tu memoria ni lo que ya pone la web. Si el README del
programa y el código discrepan, gana el código.

La web documenta **una versión concreta**: la de `tools/site.json`
(`version`), que `sitio.py` escribe en cada `<span data-v>` y en el pie. Se
coteja con el commit publicado de esa versión, no con el árbol de trabajo del
autor, que puede ir por delante.

Un número inventado en un sitio de software de ingeniería es peor que un
número ausente: alguien lo citará. Si no puedes consultar el repositorio en ese
momento, **dilo y deja el dato como está**. No lo estimes.
Detalle en `.claude/skills/contenido-tecnico/SKILL.md`.

### 3. Ningún enlace roto, y nada «disponible» que no lo esté

`python tools/sitio.py --check` tiene que terminar con **0 errores** antes de
publicar. Ojo con dos trampas ya sufridas:

- La web tuvo enlaces `/cdn-cgi/l/email-protection` con los correos ofuscados
  por Cloudflare. En GitHub Pages **dan 404**: el script que los descifra no
  existe ahí. Los correos van en `mailto:` planos.
- Lo que aún no existe se marca como tal —`.tag.soon`, `.card.planned`,
  `.btn.locked` o `aria-disabled="true"`, con un texto que diga cuándo llega— y
  **nunca** lleva un enlace vivo. Hoy OGR Slip2D es *source available ·
  pre-release*; los instaladores y los otros cuatro programas de la suite son
  *planned*.

### 4. Cada página existe en inglés y en español

Toda página existe en `/` y en `/es/` **con la misma ruta**, las mismas `id`,
las mismas ecuaciones y las mismas figuras. La versión **inglesa es la de
referencia**: se escribe y se corrige allí. La española **se monta**, no se
escribe a mano en el repo: parte de `../desarrollo/traduccion/<clave>.es.html` y
`traduccion.py montar` produce `es/…`. Un arreglo hecho solo en `es/…` se pierde
en el siguiente `montar`. `sitio.py --check` avisa de las páginas que faltan en
un idioma; no debe faltar ninguna al publicar.

### 5. Lo generado no se edita a mano

`sitio.py` y `render_math.cjs` escriben parte de cada página. **No edites a mano**:

- las regiones `<!-- @inc … -->` … `<!-- @end … -->` (cabeza, cabecera, pie,
  índice lateral, título y pie de la documentación, «en esta página»);
- la numeración de secciones, ecuaciones, figuras y tablas, y el texto de las
  referencias cruzadas `a.xref`;
- `<span data-v>` y los atributos de `<html>` (`lang`, `data-root`);
- el render de KaTeX entre `<!--k-->` y `<!--/k-->`;
- `assets/js/search-index.*.js` y `sitemap.xml`;
- `es/**` (salida de `montar`).

Cambia la fuente —`tools/partials/`, `tools/site.json`, el `data-tex`, la
página inglesa— y relanza la herramienta.

### 6. La documentación se escribe según la guía

Toda página de `docs/` sigue `dev/guia-documentacion.md`: capítulos y orden en
`tools/site.json`; `h2` con `id` explícito en inglés; ecuaciones en `data-tex`;
figuras y tablas numeradas; referencias cruzadas `a.xref`; citas `a.cite` con
las claves de la bibliografía; lo que hace el programa, en una caja `.impl`, y
sus limitaciones, en una `note warn`. Cada fórmula con su fuente científica
original.

Las figuras que muestran **resultados** salen de **cálculos reales del
programa** —modelos en `../desarrollo/modelos-ogr/`, `.ogr` publicados en
`assets/models/`—, nunca de valores escritos a mano. Y ningún `<!-- PENDIENTE -->`
queda en lo que se publica: va a `../desarrollo/notas/pendientes-docs.md`.

### 7. Todo lo visible se prueba a 375, 768 y 1440 px

Los puntos de ruptura reales son 720, 960, 1024, 1100 y 1280 px. A 375 px es el
móvil; a 768 px el menú ya está colapsado y las rejillas pasan a una o dos
columnas; a 1440 px la documentación muestra sus tres columnas. Revisa los tres
anchos, en ambos idiomas, **sin errores en la consola y sin scroll horizontal**.
El `body` lleva `overflow-x: hidden`, así que un desbordamiento no se ve pero
rompe el ancho: búscalo con las herramientas de desarrollo, no a ojo.

### 8. Las imágenes pesan, y aquí se nota

`assets/` se sirve tal cual, sin optimización. Antes de añadir una imagen:
redimensiónala al tamaño en que se muestra (×2 como mucho), guárdala como
**WebP** de calidad ~80 (PNG solo para `og-image`, iconos y logotipos), con `alt`
útil, `width` y `height` reales y `loading="lazy"` salvo sobre el pliegue.
Presupuesto: **300 KB por imagen** (`sitio.py --check` avisa); si te lo saltas, di
por qué. Los originales sin optimizar no entran al repo.

---

## Flujo de trabajo

- **Antes de una tarea no trivial, propón un plan y espera mi OK.** Usa plan mode.
- **Una tarea a la vez.** Al terminar, dime qué cambiaste y qué comprobaste.
- **Si no estás seguro al 80 %, pregunta. No inventes** — sobre todo en cifras
  técnicas y en afirmaciones sobre lo que el programa sabe hacer.
- **Sé escéptico con lo que te pido.** Si algo huele mal, dilo.
- **Al terminar, lista qué probaste y qué falta por probar.**
- **Orden de trabajo en una página:** primero el inglés; luego `render_math` y
  `sitio.py`; después el español (`traduccion.py`); al final `sitio.py --check`.
- **Trabajo en paralelo:** cada cual edita solo sus páginas y sincroniza con
  `--only`. Detalle en `dev/guia-documentacion.md` (§ «Trabajo en paralelo»).
- Los cambios con contenido nuevo dejan una nota en `dev/changelog/`.
- Los cambios grandes se hacen en una rama distinta de `main` (el rediseño vive
  en `rediseno-v3`). **Nada se fusiona en `main`, se commitea ni se publica sin
  mi OK explícito**; el procedimiento está en `/publicar`.
- Comandos del proyecto: `/sincronizar` (datos al día con el programa),
  `/revisar` (revisión de los cambios), `/publicar` (revisar + resumen + OK +
  publicar), `/seccion` (añadir o rehacer una sección o página).

---

## No hagas

- **No cambies la estética sin preguntar.** Regla 1. Es la más importante.
- **No toques `CNAME`.** Un cambio ahí tira el dominio.
- **No añadas frameworks, bundlers ni `package.json`**, ni dependencias nuevas en
  `tools/`. El valor de este sitio es que lo versionado es lo servido y que se
  puede abrir y editar sin cadena de construcción.
- **No añadas analítica, cookies, píxeles de seguimiento ni fuentes de terceros
  nuevas** sin pedírmelo. Hoy la única petición externa son las tipografías de
  Google, y el único almacenamiento es `localStorage` para dos preferencias de
  interfaz (la pestaña elegida y el aviso de idioma descartado).
- **No metas correos ofuscados por Cloudflare.** Regla 3.
- **No inventes capacidades del programa.** Si el repositorio de OGR-Slip2D no lo
  dice, la web no lo dice.
- **No conviertas «planeado» en «disponible».** El estado de cada programa de la
  suite se toma de la hoja de ruta del repositorio del programa.
- **No nombres programas comerciales de terceros.** Las fórmulas se citan por su
  fuente científica (Bishop 1955, Spencer 1967, Morgenstern–Price 1965…).
- **No edites lo generado** (regla 5), ni `es/**` a mano.
- **No ejecutes `python tools/sitio.py` sin `--only`** mientras otras personas o
  agentes editan páginas: reescribiría las suyas.
- **No dejes notas internas en lo que se publica** (`PENDIENTE`, borradores): van
  a `../desarrollo/notas/`.
- **No subas binarios grandes** (instaladores, vídeos, PDF pesados). Van en las
  *releases* de GitHub, no aquí. Los `.ogr` de `assets/models/` son texto y solo
  los de los ejemplos.
- **No publiques sin OK.** `git push origin main` es producción.

---

## Convenciones

- **Idioma.** El repositorio se documenta en castellano (este archivo, `spec/`,
  `dev/`, comandos y skills). La web es bilingüe: inglés británico en `/`
  (*behaviour*, *licence*, *modelling*) y castellano técnico de España, con
  tuteo, en `/es/`. Los menús y botones del programa se nombran como aparecen en
  pantalla (en inglés) también en las páginas en castellano.
- **Terminología geotécnica correcta**: *factor of safety*, *slip surface*,
  *pore pressure*, *limit equilibrium*, *seepage* —en castellano, *factor de
  seguridad*, *superficie de rotura*, *presión intersticial*, *equilibrio
  límite*, *filtración*—. Ni traducciones libres ni sinónimos de marketing.
  Unidades SI. Glosario completo en la skill `contenido-tecnico`.
- **Nombres**: *OpenGeoRock* es la suite; *OGR Slip2D* es el programa;
  `ogr-slip2d` es el paquete instalable, con los comandos `ogr-slip2d`,
  `ogr-slip2d-cli` y `ogr-slip2d-mcp`. No se mezclan.
- HTML indentado a 2 espacios, atributos en minúscula, comillas dobles.
- Los comentarios `<!-- ====== SECCIÓN ====== -->` separan las secciones de las
  páginas principales. Son el índice de navegación del archivo: mantenlos.
- **CSS**: variables por nombre (`var(--ink)`), nunca el literal. Nada de
  `<style>` en las páginas; evita el `style=""` (solo las propiedades
  personalizadas `--f`, `--i` y `--cols`, y ajustes puntuales que ya existen).
- **Enlaces**: los externos, siempre con `target="_blank" rel="noopener"`; los
  internos apuntan a un archivo (`docs/index.html`, nunca `docs/`) con la ruta
  relativa que corresponde a la profundidad de la página (skill
  `html-estatico`). Solo `404.html` usa rutas desde la raíz.

---

© 2026 Samuel Sáez López — UPCT
