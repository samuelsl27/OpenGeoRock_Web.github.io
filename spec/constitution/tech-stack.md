# Stack y convenciones

## Tecnología

| Pieza | Decisión | Por qué |
|---|---|---|
| Formato | HTML5 estático **multipágina**: inglés en `/`, español en `/es/`, con las mismas rutas | Cada página se abre y se edita con un editor de texto; sin servidor y sin build de despliegue no hay build que se rompa |
| CSS | `assets/css/site.css` (el sistema de diseño «Cuaderno técnico») y `assets/css/docs.css` (solo `docs/`), compartidos | Un solo sitio donde cambiar el aspecto; se cachean entre páginas; ningún `<style>` por página |
| JavaScript | Vanilla, en `assets/js/site.js`: menú, pestañas, copiar código, buscador de la documentación, aviso de idioma, animación de figuras. **Sin frameworks ni build** | Mejora progresiva: sin JS la web se lee entera; nada que compilar ni que mantener contra una API que cambia |
| Matemáticas | KaTeX 0.19.0 (MIT) **pre-renderizado** con `tools/render_math.cjs`; al navegador solo llegan `assets/vendor/katex/katex.min.css` y sus fuentes | La ecuación llega ya compuesta: sin script de KaTeX, sin parpadeo, legible sin JS |
| Mantenimiento | `tools/sitio.py` (Python, biblioteca estándar) y `tools/render_math.cjs` (Node, sin `package.json`), con `tools/site.json` y `tools/partials/`. **Su salida se versiona** | Cabecera, pie, numeración, referencias cruzadas, índice de búsqueda y sitemap no se mantienen a mano en cada página |
| Tipografías | Inter · Newsreader · JetBrains Mono (Google Fonts) | Única dependencia externa, y es consciente |
| Alojamiento | GitHub Pages desde `main`; `.nojekyll` en la raíz | Gratis, versionado, sin servidor que administrar |
| Dominio | `opengeorock.org` vía `CNAME` | — |

**Sin gestor de paquetes, sin bundler, sin framework, sin preprocesador, sin
build de despliegue.** Lo que hay en el repositorio es lo que sirve Pages. Las
herramientas de `tools/` son una comodidad local, idempotente, cuya salida está
versionada: quien edite una coma no las necesita para que la web siga sirviendo.
No es una limitación temporal: es la decisión. Una web de proyecto que necesita
`npm install` para cambiar una coma se queda sin actualizar.

### Decisiones que fijan este stack (rediseño, 2026-10-01)

El registro completo, con su motivo, está en `../desarrollo/notas/decisiones.md`.

- Estética **A «Cuaderno técnico»**, elegida entre tres propuestas. Solo modo claro.
- **Bilingüe EN + ES**, con las mismas rutas. Sustituye a la decisión anterior de
  «sin multiidioma».
- **JavaScript permitido**, pero vanilla, sin frameworks ni build. Sustituye a «cero JS».
- **KaTeX pre-renderizado** (0.19.0, MIT): la web solo sirve CSS y fuentes.
- **Multipágina** con CSS y JS compartidos y `tools/sitio.py` para sincronizar
  cabecera, pie y menús. Sustituye a «un solo `index.html` con el CSS en línea».
- Las cifras técnicas salen del **código** de la versión documentada cuando el
  README del programa está desfasado.
- El mensaje del servidor MCP lleva fecha y «hasta donde sabemos»; nunca «el primero».
- Las capturas del programa, con la interfaz en inglés (arranca en inglés y la
  elección de idioma no se guarda).

## Idiomas

- **La web es bilingüe.** El inglés (británico) es la versión de referencia, en `/`;
  el castellano técnico de España, con tuteo, va en `/es/`, con las mismas rutas.
  El selector EN/ES está en la cabecera y el pie; `hreflang` y `sitemap.xml`
  declaran las alternativas. En las páginas inglesas, un aviso (una sola vez) ofrece
  el español a quien tiene el navegador en español. La versión española se **monta**
  desde `../desarrollo/traduccion/` con `traduccion.py`; no se escribe a mano.
- **El repositorio, en castellano**: `AGENTS.md`, `spec/`, `dev/`, comandos y
  skills. Quien mantiene esto piensa en castellano.

## Fuente de verdad

Los datos técnicos **no viven aquí**. Viven en
[`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D):

- `pyproject.toml` → versión y licencia
- el código → métodos, búsquedas, modelos de resistencia, menús y diálogos,
  herramientas MCP (gana al README y a los docstrings cuando discrepan)
- `docs/changelog/` → qué cambió y cuándo, y el recuento de tests
- `validacion/` → los casos de referencia, con su fuente
- `README.md` → la hoja de ruta de la suite

Esta web es una **vista** de ese repositorio **en una versión concreta**: la de
`tools/site.json` (hoy, la 0.1.235), que se cotejó con el commit publicado y no con
el árbol de trabajo. El comando `/sincronizar` existe para mantener la vista al día.

## Convenciones de código

- Indentación de 2 espacios. Atributos en minúscula, comillas dobles.
- Comentarios `<!-- ====== SECCIÓN ====== -->` como índice de las páginas principales.
- Las regiones `<!-- @inc X --> … <!-- @end X -->`, la numeración, el render de
  KaTeX, los índices de búsqueda, `sitemap.xml` y `es/**` son **salida generada**:
  se cambia la fuente y se relanza la herramienta.
- Sin `<style>` ni `<script>` propios en las páginas; variables CSS siempre por
  nombre (`var(--ink)`), nunca el literal.
- Iconos: SVG en línea, `viewBox="0 0 24 24"`, `stroke-width` 1.6–2. Figuras: SVG
  en línea con las clases `.slope-svg` o `.dg`, sin colores literales.
- Ecuaciones: TeX en `data-tex`; la numeración, las referencias cruzadas y las
  citas, según `dev/guia-documentacion.md`.
- Enlaces: los externos, `target="_blank" rel="noopener"`; los internos, a un
  archivo (`docs/index.html`) con ruta relativa a la profundidad de la página.
- Imágenes: WebP, `alt` descriptivo, `width` y `height`, `loading="lazy"` salvo
  sobre el pliegue, **máximo 300 KB**.

## Presupuestos

| Métrica | Objetivo |
|---|---|
| Peso de cualquier imagen | < 300 KB (`sitio.py --check` avisa). Hoy la mayor es `og-image.png`, con 161 KB |
| CSS y JS compartidos | sin presupuesto fijado; hoy, 64 KB sin comprimir (`site.css` 37 KB, `docs.css` 15 KB, `site.js` 13 KB) |
| HTML de una página | sin presupuesto fijado; las páginas de teoría llevan las ecuaciones ya compuestas y pesan de unos 85 KB a unos 570 KB (medido el 2026-10-02) |
| Peticiones a terceros | solo Google Fonts |
| Puntos de ruptura | los que ya existen: `site.css` 1100 · 960 · 720 px y `docs.css` 1280 · 1024 · 720 px; ninguno nuevo |
| Anchos de prueba | 375 · 768 · 1440 px |
