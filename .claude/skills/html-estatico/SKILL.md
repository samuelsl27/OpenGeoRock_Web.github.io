---
name: html-estatico
description: Reglas del HTML estático de este sitio — estructura de página, regiones generadas por sitio.py, rutas relativas según la profundidad, accesibilidad, rendimiento, imágenes, enlaces y despliegue en GitHub Pages. Úsalo al crear o editar páginas, imágenes o enlaces, y antes de publicar.
---

# HTML estático en GitHub Pages

Sitio multipágina, bilingüe, sin build de despliegue: lo que hay en el
repositorio es literalmente lo que se sirve. Parte del marcado lo escriben dos
herramientas de `tools/` (su salida se versiona); el resto lo escribes tú. Eso
simplifica mucho y castiga unas cuantas cosas.

## 1. GitHub Pages no ejecuta nada del servidor

- **No hay reescrituras ni redirecciones.** Un `href` a una ruta que no es un
  archivo del repositorio da 404. Por eso los enlaces internos apuntan a un
  archivo (`docs/index.html`, nunca `docs/`).
- **Nada de Cloudflare Email Protection.** Si copias marcado desde una página ya
  desplegada tras Cloudflare, traerás enlaces `/cdn-cgi/l/email-protection` y
  `<span class="__cf_email__">`. Aquí **no funcionan**: el script que los
  descifra no existe. Los correos van en `mailto:` planos. Ya pasó una vez.
- **`CNAME` no se toca.** Contiene `opengeorock.org`. Borrarlo o cambiarlo tira
  el dominio hasta que alguien lo restaure a mano. El `.nojekyll` de la raíz
  tampoco: sin él, Pages procesaría el sitio con Jekyll.
- **`404.html` es la única página de error que sirve Pages**, para cualquier ruta
  inexistente y a cualquier profundidad, así que sus enlaces y recursos son
  absolutos desde la raíz (`data-root="/"`). El servidor local no la sirve:
  ábrela en `http://localhost:8000/404.html`.

## 2. Estructura de una página

```html
<!doctype html>
<html class="no-js" lang="en" data-root="../">
<head>
<meta charset="utf-8">
<title>Verification — OGR Slip2D</title>
<meta name="description" content="Una o dos frases: sirven de resumen y de vista previa al compartir.">
<!-- @inc head -->
<!-- @end head -->
</head>
<body>
<!-- @inc header -->
<!-- @end header -->

<main id="main">
<section class="page-hero"> … </section>

<!-- ====== NOMBRE ====== -->
<section class="section" id="nombre"> … </section>
</main>

<!-- @inc footer -->
<!-- @end footer -->
</body>
</html>
```

- **Lo tuyo** en la cabeza es `<title>` y `<meta name="description">` (de ellos
  salen las etiquetas Open Graph y la entrada del buscador). Todo lo demás de
  `<head>` lo trae la región `head`: no pongas `<link>` ni `<script>` a mano.
- **`<html>`**: `sitio.py` reescribe la etiqueta entera (`class="no-js"`, `lang` y
  `data-root`); el `<script>` de la cabeza cambia `no-js` por `js`.
- **Un solo `<h1>`** por página. Las secciones usan `<h2>`; no saltes niveles por
  razones de tamaño: el tamaño lo pone el CSS.
- `<main id="main">` es obligatorio: es el destino del enlace «Skip to content».
- Los comentarios `<!-- ====== NOMBRE ====== -->` separan las secciones de las
  páginas principales y son su índice. Una sección a la que se enlaza lleva `id`.
- **Documentación**: `<body class="docs">` y el esqueleto de
  `dev/plantilla-doc.html` (`.doc-shell` con tres `aside`/`main`); escribes solo
  dentro de `<article class="doc prose">`. Guía: `dev/guia-documentacion.md`.

### Regiones generadas

`tools/sitio.py` sustituye lo que hay entre `<!-- @inc X -->` y `<!-- @end X -->`.
**No se editan a mano** (regla 5 de `AGENTS.md`); se cambia su fuente.

| Región | Fuente | Contenido |
|---|---|---|
| `head` | `tools/partials/head.html` | viewport, `canonical`, `hreflang` EN/ES/x-default, Open Graph y Twitter, iconos, tipografías, `site.css`, `docs.css` (si la ruta empieza por `docs/`), `katex.min.css` (si la página tiene `data-tex`), `site.js` |
| `header` | `tools/partials/header.{en,es}.html` | enlace «Skip to content», barra con mega-menú, selector EN/ES, menú móvil; marca la entrada activa (`aria-current`) según `nav_sections` de `tools/site.json` |
| `footer` | `tools/partials/footer.{en,es}.html` | columnas de enlaces, línea legal con la versión y su fecha (`site.json`), selector de idioma; en EN, el aviso de idioma |
| `docnav` | `sitio.py` + `site.json` | buscador y árbol de capítulos |
| `dochead` | `sitio.py` + `site.json` | botón de contenido, migas, nº de capítulo, `h1`, «Describes OGR Slip2D <versión>» |
| `docfoot` | `sitio.py` | anterior/siguiente, «Edit this page», «Report a problem» |
| `pagetoc` | `sitio.py` | «En esta página» (h2/h3) y botón de imprimir |
| `docgroups` | `sitio.py` + `site.json` | las tarjetas de capítulos de `docs/index.html` |

Además `sitio.py` escribe `<span data-v>` (la versión de `site.json`), numera
secciones, ecuaciones, figuras y tablas, rellena las referencias `a.xref`, y
genera `assets/js/search-index.{en,es}.js` y `sitemap.xml`.

## 3. Rutas relativas según la profundidad

`data-root` (que escribe `sitio.py`) es el camino hasta la raíz. Los recursos
(`assets/…`) y los enlaces entre páginas se escriben **relativos a la propia
página**:

| Página | `data-root` | Hacia un recurso | Hacia otra página |
|---|---|---|---|
| `index.html` | *(vacío)* | `assets/img/…` | `docs/index.html` |
| `about/index.html`, `docs/index.html`… | `../` | `../assets/img/…` | `../ai/index.html` |
| `docs/theory/x.html`, `docs/user-guide/x.html`… | `../../` | `../../assets/img/…` | `../reference/bibliography.html#bishop1955` |
| `es/index.html` | `../` | `../assets/img/…` | `docs/index.html` (→ `es/docs/…`) |
| `es/docs/theory/x.html` | `../../../` | `../../../assets/img/…` | `../reference/bibliography.html#…` |
| `404.html`, `es/404.html` | `/` | `/assets/…` | `/index.html` |

Las páginas españolas viven en el mismo árbol bajo `es/`: **los enlaces entre
páginas se quedan igual que en el original** (siguen apuntando bien) y solo los
recursos de `assets/` necesitan un `../` más, que añade `traduccion.py montar`.
`es/**` no se escribe a mano.

## 4. Enlaces

- Todo enlace externo: `target="_blank" rel="noopener"`.
- Lo que aún no existe no lleva enlace vivo: `.btn.locked` o `aria-disabled="true"`
  con un `title` que diga cuándo llegará (regla 3).
- Las anclas (`#seccion`) tienen que existir: `sitio.py --check` lo comprueba.
- El selector EN/ES, `hreflang` y `canonical` los genera `sitio.py`.

## 5. Las imágenes son el coste real de una página

No hay optimización automática. El navegador descarga el archivo tal cual.

Antes de añadir una imagen:

1. Redimensiónala al tamaño en que se muestra (×2 como mucho, para pantallas de
   alta densidad). Herramienta: `desarrollo/herramientas/optimizar_imagenes.py
   ORIGEN DESTINO --w ANCHO` (calidad 80 por defecto; avisa si pasa de 300 KB).
2. **WebP**. PNG solo donde el formato lo exige: `og-image`, iconos y logotipos.
3. **Presupuesto: 300 KB.** `sitio.py --check` avisa de lo que pasa. Si te lo
   saltas, di por qué.
4. **`width` y `height` reales** del archivo, para que la página no salte al
   cargar (ojo: varias capturas de `docs/` aún no los llevan).
5. `loading="lazy"` salvo que esté sobre el pliegue, donde va `loading="eager"`.
6. `alt` que describa **lo que la imagen aporta**, no lo que es. Mal:
   `alt="captura"`. Bien: `alt="Grid search over a two-layer slope: the critical
   surface in red among candidate circles in green"`. En `/es/`, `alt` en español.
7. Las capturas del programa se hacen **con la interfaz en inglés** (arranca en
   inglés y la elección de idioma no se guarda) y se muestran con `figure.shot`
   (portada y fichas) o `figure.fig.shot-fig` (documentación).

Las figuras calculadas son **SVG en línea**, no imágenes: se inyectan entre
`<!-- svg:NOMBRE -->` y `<!-- /svg:NOMBRE -->` con
`desarrollo/herramientas/inyectar_svg.py`. Sin imágenes en base64 en las páginas.

## 6. Accesibilidad: lo mínimo que hay que respetar

- Todo elemento interactivo es `<a>` o `<button>`. Un `<div>` clicable no llega
  por teclado. Lo no disponible lleva `aria-disabled="true"` y un `title`.
- Los SVG decorativos llevan `aria-hidden="true"`; los informativos,
  `role="img"` y un `<title>` (con `aria-labelledby`).
- El foco visible (`:focus-visible`, contorno verde) no se quita nunca.
- Las navegaciones llevan `aria-label`, traducido en `/es/` (salvo `Breadcrumb` y
  `Pager` de las regiones `dochead` y `docfoot`, que `sitio.py` escribe siempre en
  inglés). Las pestañas siguen el patrón completo (ver `diseno-web`) y se manejan
  con las flechas.
- `<html lang>` correcto, y `lang` en el texto que cambie de idioma (el selector EN/ES
  ya lo lleva).
- **Contraste** (medido con los tokens): `--mute` sobre `--paper` 5,1:1 y sobre
  `--paper-2` 4,6:1 — vale; sobre `--paper-3` 4,1:1 — no, para texto que importe.
  El bermellón sobre `--paper` da 4,3:1 y sobre `--crit-soft` 3,9:1: no lo uses
  como único portador de información en texto pequeño (sobre `--white` sube a
  4,7:1). Las etiquetas mono de 10–11 px son metadatos repetidos en otro sitio:
  no metas ahí contenido único.
- `prefers-reduced-motion` anula la animación de las figuras: no la rodees.
- Sin JavaScript la web se lee entera (las pestañas muestran todos sus paneles).
  No hagas que un contenido dependa del JS.

## 7. Rendimiento

- CSS y JS compartidos y cacheables: `site.css` (más `docs.css` en `docs/`) y
  `site.js` con `defer`. El único script en la cabeza es el de una línea que
  cambia `no-js` por `js`.
- Las ecuaciones llegan ya compuestas (`render_math.cjs`): ni KaTeX ni su CSS
  cargan en páginas sin `data-tex`. Esa es la razón de que una página de teoría
  pese cientos de KB de HTML: no añadas peso sin motivo.
- La única petición a terceros son las tipografías de Google (`display=swap`,
  con `preconnect`). No añadas ninguna otra.
- El índice de búsqueda se descarga solo al enfocar el buscador.

## 8. Antes de publicar

```bash
python -m http.server 8000          # abre http://localhost:8000 y http://localhost:8000/es/
node tools/render_math.cjs          # si hay ecuaciones nuevas
python tools/sitio.py --check       # sincroniza y comprueba
git status && git diff --stat       # lee lo que vas a subir
```

Lista de comprobación:

- [ ] `sitio.py --check` termina con **0 errores**, y has leído los avisos
      (versión que falta en un idioma, páginas pendientes, imágenes de más de
      300 KB, ecuaciones sin componer).
- [ ] La página carga **sin errores ni avisos en la consola**.
- [ ] Se ve bien a **375, 768 y 1440 px**, sin scroll horizontal.
- [ ] Todo existe en inglés y en español, con la misma ruta.
- [ ] Versión y licencia coinciden con el repositorio del programa (skill
      `contenido-tecnico`) y con `tools/site.json`.
- [ ] Las imágenes nuevas pesan menos de 300 KB y tienen `alt`, `width` y `height`.
- [ ] Las páginas nuevas están en el menú y en el pie (EN y ES) y, si procede, en
      `nav_sections` o en los capítulos de `tools/site.json`.
- [ ] Ningún `PENDIENTE` en las páginas, y `CNAME` intacto.

`git push origin main` publica en producción. No hay vuelta atrás salvo otro
commit.
