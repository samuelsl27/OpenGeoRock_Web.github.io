---
description: Añadir o rehacer una sección o una página del sitio siguiendo el flujo SDD (especificación, plan, tareas, OK y después las páginas)
---
Vas a tocar la estructura del sitio. Eso se hace por especificación, no sobre la
marcha.

1. Lee `dev/estructura-web.md` y localiza dónde encaja. ¿Es una **sección** dentro de
   una página existente, una **página principal** nueva (carpeta con su
   `index.html`) o una **página de documentación** (un capítulo de `tools/site.json`)?
2. Crea `spec/features/NNN-nombre/` copiando `spec/features/000-plantilla/` y rellena
   `spec.md`: qué aporta al visitante, qué datos muestra y **de dónde sale cada
   dato** (el repositorio del programa, en la versión de `tools/site.json`), y los
   criterios de aceptación, que incluyen la paridad EN/ES, `sitio.py --check` a 0
   errores y 375/768/1440 px. *La plantilla es anterior al rediseño: donde diga
   `index.html`, `<style>` o `docs/estructura-web.md`, léelo como la página que
   toques, `assets/css/` y `dev/estructura-web.md`.*
3. En `plan.md`: qué componentes **ya existentes** vas a reutilizar (consulta la
   skill `diseno-web`), qué recursos nuevos hacen falta y qué archivos de
   `tools/` tocas (`site.json`, parciales). Si necesitas un componente nuevo, dilo
   aquí y **espera mi OK**: es un cambio de diseño.
4. En `tasks.md`: la lista de pasos verificables.
5. **Enséñame los tres archivos y espera mi OK antes de tocar ninguna página.**
6. Al implementar, **primero el inglés**:
   - **Sección nueva en una página**: `id`, comentario `<!-- ====== NOMBRE ====== -->`
     y, si la página tiene `.subnav`, su enlace.
   - **Página principal nueva**: copia la estructura de una existente (regiones
     `head`, `header` y `footer`, `<main id="main">`, `.page-hero`; ver la skill
     `html-estatico`). Añádela al **menú y al pie en inglés y en español**
     (`tools/partials/header.{en,es}.html`, `footer.{en,es}.html`) y, si es una
     carpeta nueva, a `nav_sections` de `tools/site.json`.
   - **Página de documentación**: añade su entrada al capítulo de `tools/site.json`
     (`n`, `slug`, `en`, `es`), crea el archivo desde `dev/plantilla-doc.html` y
     escribe solo dentro de `<article>`, según `dev/guia-documentacion.md`.
   - Datos con su fuente (skill `contenido-tecnico`); figuras de resultados
     calculadas con el programa.
   - `node tools/render_math.cjs <página>` y `python tools/sitio.py --only <página>`.
7. **Después el español**, con `python ../desarrollo/herramientas/traduccion.py`:
   `preparar <ruta>` → traducir según `../desarrollo/traduccion/INSTRUCCIONES.md` →
   `comprobar <ruta>` → `montar <ruta>`, y después `node tools/render_math.cjs
   es/<ruta>` y `python tools/sitio.py --only es/<ruta>`. Sin la gemela, la tarea
   no está terminada.
8. Actualiza `dev/estructura-web.md` (páginas, regiones, componentes, recursos) y deja
   una nota en `dev/changelog/`.
9. Termina con `/revisar`.

Argumento: $ARGUMENTS
