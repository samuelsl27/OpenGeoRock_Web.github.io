# opengeorock.org

Sitio público de la suite **OpenGeoRock**. Un sitio estático multipágina y
bilingüe (inglés en `/`, español en `/es/`), desplegado en GitHub Pages sobre
el dominio `opengeorock.org`.

Qué hay: la presentación del programa **OGR Slip2D** y de la suite, su servidor
MCP para agentes de IA con la guía de instalación, ejemplos con modelos `.ogr`
descargables, la página de verificación, la descarga desde el código fuente y la
documentación (primeros pasos, guía de usuario, manual de teoría con sus
ecuaciones y fuentes, verificación y referencia).

El programa vive en otro sitio: **[OGR-Slip2D](https://github.com/samuelsl27/OGR-Slip2D)**.
Este repositorio solo contiene la web.

## Verlo en local

No hay dependencias que instalar: basta Python 3 (y Node, solo para las ecuaciones).

```bash
python -m http.server 8000     # → http://localhost:8000  (inglés)  ·  /es/  (español)
```

Mejor con el servidor que abriendo los archivos con doble clic: `404.html` usa
rutas desde la raíz y solo se ve bien servida. Cuando falta una ruta, la 404 de la
web la sirve GitHub Pages, no este servidor: para verla, abre `/404.html`.

## Regenerarlo

Parte de cada página la escriben dos herramientas de `tools/`, y su salida se
versiona. Lo que hay en el repositorio es lo que sirve Pages: no hay build de
despliegue.

| Comando | Qué hace |
|---|---|
| `python tools/sitio.py` | Rellena cabecera, pie y cabeza de cada página desde `tools/partials/`; numera secciones, ecuaciones, figuras y tablas de la documentación; escribe la versión del programa (`tools/site.json`), el índice de búsqueda y `sitemap.xml` |
| `python tools/sitio.py --check` | Lo anterior y además comprueba enlaces, anclas, paridad EN/ES, imágenes de más de 300 KB y ecuaciones sin componer. Tiene que dar 0 errores para publicar |
| `python tools/sitio.py --only <página>…` | Solo esas páginas (para trabajar en paralelo sin pisar las de otros) |
| `node tools/render_math.cjs [<página>…]` | Compone las ecuaciones (`data-tex`) con KaTeX 0.19.0, incluido en `tools/vendor/` |

Las regiones `<!-- @inc … -->`, la numeración, el render de KaTeX, el índice de
búsqueda, `sitemap.xml` y todo `es/` son **salida generada**: no se editan a
mano. Las traducciones al español se preparan, comprueban y montan con
`../desarrollo/herramientas/traduccion.py` (fuera del repo; ver `AGENTS.md`).

## Publicar

```bash
git push origin main
```

GitHub Pages redespliega solo. **No hay entorno de pruebas**: lo que se sube a
`main` es producción. Antes: `/revisar` y `/publicar` (ver `.claude/commands/`).

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html`, `products/`, `ai/`, `examples/`, `verification/`, `download/`, `about/` | Las páginas principales |
| `docs/` | La documentación en cinco capítulos (estructura en `tools/site.json`) |
| `es/` | La copia en español, con las mismas rutas |
| `assets/` | CSS, JS, imágenes, modelos `.ogr` y KaTeX (CSS y fuentes) |
| `tools/` | `sitio.py`, `render_math.cjs`, `site.json`, parciales y KaTeX |
| `dev/` | Mapa del sitio, guía de la documentación y changelog |
| `spec/` | Constitución del proyecto y plantilla de features |
| `.claude/` | Comandos y skills del agente |
| `CNAME` | Dominio propio. No tocar |
| `AGENTS.md` | Contrato de trabajo para agentes de IA |

Notas, borradores, capturas en bruto y herramientas de producción viven fuera
del repo, en `web-OGR/desarrollo/`.

## Si desarrollas con IA

Lee **[`AGENTS.md`](AGENTS.md)** primero: stack, comandos, las ocho reglas, el
flujo de trabajo y lo que no se debe hacer. La más importante:

> **La estética no se cambia sin permiso explícito.** Texto, datos y
> enlaces, libremente. Colores, tipografías, espaciados y layout, solo con
> el OK del responsable.

La segunda, casi igual de importante: **ningún dato técnico se escribe de
memoria**. Versión, licencia, métodos y capacidades salen del repositorio del
programa y se cotejan con la versión que documenta la web (`tools/site.json`).
El comando `/sincronizar` hace justo eso.

Comandos disponibles: `/sincronizar`, `/revisar`, `/publicar`, `/seccion`. Para
escribir o traducir documentación: `dev/guia-documentacion.md`. Para saber dónde
está cada cosa: `dev/estructura-web.md`.

## Licencia

El contenido de la web (textos e imágenes) es © 2026 Samuel Sáez López.
El programa que documenta se publica bajo **AGPL-3.0-or-later**. KaTeX (MIT) va
incluido con su licencia en `tools/vendor/` y `assets/vendor/katex/`.
