---
description: Revisión de los cambios pendientes contra las ocho reglas del proyecto, con comprobación automática, capturas a 375/768/1440 px y consola
---
Eres un revisor senior de este sitio. Sobre los cambios pendientes:

1. **Qué cambió.** `git status` y `git diff --stat`. Separa lo **escrito a mano**
   (CSS, JS, `tools/`, markdown, el texto de las páginas) de lo **generado**
   (regiones `<!-- @inc … -->`, render de KaTeX, numeración, `search-index`,
   `sitemap.xml`, `es/**`). Lista los archivos tocados.

2. **Comprobación automática.**
   - Si hay ecuaciones nuevas: `node tools/render_math.cjs <páginas>`; tiene que
     decir `0 errores`.
   - `python tools/sitio.py --check`. Primero sincroniza (escribe lo generado) y
     después comprueba; es idempotente. **0 errores** es el listón. Los avisos
     (`falta la versión ES/EN`, `página de la documentación pendiente`, `imagen de
     más de 300 KB`, `ecuaciones sin renderizar`, `referencia cruzada sin destino
     numerado`) se listan uno a uno.
   - Con trabajo ajeno en curso, `--only <tus páginas> --check` (la comprobación
     cubre igualmente todo el sitio; mira solo lo tuyo).

3. **Las ocho reglas de `AGENTS.md`**, una por una:
   - **Estética**: ¿hay algún cambio en `assets/css/`, `assets/js/` o
     `tools/partials/` que afecte al aspecto o al comportamiento y que yo no haya
     aprobado explícitamente? ¿Un `<style>` o `style=""` nuevo, un color literal,
     un componente inventado?
   - **Datos técnicos**: ¿cada cifra, versión, licencia, método y capacidad nuevos
     tiene respaldo en `OGR-Slip2D` **en la versión de `tools/site.json`**? ¿La
     versión va en `<span data-v>` y no tecleada (salvo las notas ligadas a una
     versión)?
   - **Enlaces**: ¿0 errores de `--check`? ¿Queda algún `/cdn-cgi/`, algún
     `mailto:` ofuscado, algún enlace vivo a algo aún no publicado, algo marcado
     «disponible» que sea *planned*?
   - **Paridad EN/ES**: cada página inglesa tocada tiene su gemela en `es/`
     actualizada: `python ../desarrollo/herramientas/traduccion.py comprobar
     <ruta>` (id, `href`, `data-tex` y marcadores idénticos). ¿Se editó `es/**` a
     mano en vez de su fuente en `desarrollo/traduccion/`?
   - **Generado**: tras relanzar `render_math` y `sitio.py`, `git diff` no debe
     cambiar: si cambia, alguien editó a mano una región, la numeración o un render.
   - **Documentación**: `h2` con `id` en inglés, `data-tex` en vez de TeX suelto,
     `a.xref` y `a.cite` con claves que existen, limitaciones en `note warn`,
     figuras de resultados calculadas con el programa, ningún `PENDIENTE`
     (`grep -rn PENDIENTE --include=*.html .`).
   - **Responsive**: ver el punto 4.
   - **Imágenes**: ¿alguna supera 300 KB? ¿WebP? ¿todas con `alt` útil, `width`,
     `height` y `loading` correcto? ¿Las capturas, en inglés?

4. **En el navegador.** Sirve el sitio (`python -m http.server 8000`) y abre, en
   **inglés y en español**, cada página tocada y, si has tocado CSS, JS o
   parciales, **una de cada tipo** (portada, `products/slip2d.html`, `ai/`,
   `examples/`, `verification/`, `download/`, `about/`, `docs/index.html`, una
   página de teoría con ecuaciones, una de guía de usuario, `docs/reference/mcp.html`
   y `/404.html`). En cada una:
   - **Capturas a 375, 768 y 1440 px** (la vista previa del navegador con
     `resize_window`, o Chrome headless con
     `..\desarrollo\herramientas\capturar.ps1 -Url … -Out … -W 375`). Se guardan
     en `../desarrollo/capturas-web/`, no en el repo.
   - **Sin scroll horizontal.** `body` lleva `overflow-x: hidden`: un desbordamiento
     no se ve. En la consola, esto lista lo que se sale del ancho (no cuentan los
     contenedores que se desplazan solos, el MathML oculto de KaTeX ni el interior
     de los SVG, que se recorta):
     ```js
     [...document.querySelectorAll("body *")].filter(e =>
       e.getBoundingClientRect().right > innerWidth + 1 &&
       !e.closest(".table-wrap, .eq, pre, .tablist, .subnav, .katex-mathml") &&
       !(e.closest("svg") && e.tagName.toLowerCase() !== "svg"))
     ```
   - **Consola sin errores ni avisos**, y en red ningún 404 (fuentes de KaTeX,
     imágenes, `search-index`).
   - Si tocaste el JS: menú móvil y mega-menú (clic, `Esc`), pestañas (flechas),
     botón *Copy*, el buscador de la documentación (`/`) y el índice lateral de
     `docs/` a 1024 px o menos.

5. **Además**: encabezados que salten de nivel, más de un `<h1>`, `<div>` clicables,
   enlaces externos sin `rel="noopener"`, SVG decorativos sin `aria-hidden`,
   `<img>` sin `alt`, y peticiones a dominios de terceros nuevos (hoy solo Google
   Fonts).

Devuelve markdown con severidad **alta / media / baja** y, en cada punto, la ruta
y la línea concreta:

- **alta** bloquea la publicación: error de `--check`, dato técnico sin respaldo,
  cambio estético sin OK, enlace vivo a lo no publicado, scroll horizontal o error
  de consola, página sin su gemela, lo generado editado a mano, notas internas en
  una página.
- **media**: se arregla antes de publicar si es sencillo (avisos de `--check`,
  imagen pesada, `alt` pobre, `width`/`height` que faltan).
- **baja**: deuda que se anota (cosméticos, matices de redacción).

Si una regla está limpia, **dilo explícitamente** en lugar de omitirla. Termina con
una línea: «listo para `/publicar`» o qué falta.
