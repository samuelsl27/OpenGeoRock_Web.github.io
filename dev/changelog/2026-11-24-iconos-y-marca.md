# 2026-11-24 — Marca e iconos de los programas

La suite estrena identidad visual: un símbolo de piedra facetada como marca y un icono por programa,
diseñados en noviembre de 2026 (dirección «Capas», verde pátina como énfasis). Los másteres, los editables y el
generador viven fuera del repositorio, en `../desarrollo/iconos/` (README allí). El acento de la web no cambia:
sigue el sistema «Cuaderno técnico» con su verde de marca y el bermellón de rotura.

## Qué cambió

- **Marca** (`tools/partials/header.{en,es}.html` y `footer.{en,es}.html`): el talud con el arco naranja se
  sustituye por la piedra facetada, en línea y sin filtros, junto a «OpenGeoRock». En el pie, sobre tinta, la
  piedra va en tonos claros. Se quitan de `site.css` las reglas `.brand .lb/.ls/.la` del logotipo anterior.
- **Iconos de pestaña**: `assets/img/favicon.svg` (la piedra de 32 px ajustada a píxel), `favicon-32.png` y
  `apple-touch-icon.png` (180 px, la piedra sobre papel).
- **`assets/img/iconos/`** (nuevo): un SVG por programa (`ogr-slip2d`, `ogr-slip3d`, `ogr-fem2d`, `ogr-fem3d`,
  `ogr-data`) y el símbolo (`ogr-simbolo`).
- **Menú «Products»**: icono de 22 px en cada programa (30 px en el destacado), con `loading="lazy"`.
- **`products/index.html`**: icono de 64 px junto al nombre en las cinco tarjetas (`.prod-title`).
- **Fichas `products/slip2d.html`, `fem2d.html`, `data.html` y `download/index.html`**: icono de 84 px junto al
  `h1` (`.prod-head`; 56 px por debajo de 720 px).
- `site.css`: cuatro reglas nuevas (`.mega-ic`, `.prod-ic`, `.prod-title`, `.prod-head`) y su ajuste móvil.

### Segunda parte (mismo día)

- **Portada** (`index.html` y su español): los cinco glifos dibujados de `.suite` se sustituyen por los iconos
  (`img.glyph`, con `object-fit: contain` alineado a la izquierda). En la traducción guardada se cambiaron los
  marcadores `<!--SVG 1-->`–`<!--SVG 5-->` por las imágenes, se renumeraron los demás y se ajustó
  `index.svg.es.json`.
- **Pie**: los enlaces de las columnas heredaban de `li a` el verde subrayado, ilegible sobre tinta. `.foot li a`
  vuelve a heredar el color del pie, como el resto de su texto; el `:hover` sigue aclarándolos.
- **`og-image.png`**: el logotipo pequeño de la esquina pasa a ser la piedra; la cuadrícula del papel se reconstruyó
  debajo. El resto de la imagen no cambia (166 KB). Las redes sociales tardan en refrescar su copia.

## Qué no

- No cambia ningún token, color, tipografía ni el acento de la web.

## Qué se comprobó

- `python tools/sitio.py --check`: 98 páginas, 0 errores, 0 avisos.
- `traduccion.py comprobar` en las cinco páginas tocadas; el español se montó con `montar` (antes se verificó que
  montar desde la traducción guardada reproducía exactamente las páginas actuales).
- Capturas a 1440 px (productos, ficha de Slip2D, menú desplegado, pie), 768 px (FEM2D en español) y 375 px
  reales (productos, descargas, Slip2D y Data en español): sin desbordamiento horizontal.
- No se revisó la consola del navegador en un servidor local (solo capturas con Edge sin interfaz).
