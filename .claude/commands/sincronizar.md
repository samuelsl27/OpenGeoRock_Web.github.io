---
description: Sincroniza los datos técnicos de la web con la versión publicada del programa OGR-Slip2D
---
Comprueba si la web se ha desalineado del programa. **No cambies nada hasta el
paso 4.**

1. **Estado real del programa, en la versión que se va a documentar.** La web
   documenta una versión concreta (`tools/site.json`). Lee el **commit publicado**
   de esa versión, no el árbol de trabajo, que puede ir por delante (a 2026-10-02:
   web en la 0.1.235, árbol de trabajo en la 0.1.236). Con la copia local
   `C:\Samuel\OpenGeoRock_Slip2d\OGR-Slip2D`, `git show <commit>:ruta`; si no sabes
   qué commit es, pregúntamelo. Si no hay copia local, usa la API de GitHub o
   pídeme la ruta.
   - versión → `pyproject.toml`
   - licencia → `pyproject.toml` y `LICENSE`
   - métodos, búsquedas, modelos de resistencia y capacidades → el **código**
     (`ogr_slip2d/methods/`, `ogr_slip2d/search.py`,
     `ogr_core/materials/builtin_models.py`, `ogr_fem2d/solvers/seepage.py`) y el
     `README.md`; si discrepan, gana el código
   - herramientas MCP y cobertura → `ogr_api/inventory.py`, `ogr_mcp/`
   - número de tests → `docs/changelog/CHANGELOG_v<versión>.md`, línea «Suite
     entera» (el README puede ir por detrás)
   - casos de validación → `validacion/casos/`
   - estado de cada programa de la suite → tabla *Roadmap* del `README.md`
   - novedades desde la última sincronización → `docs/changelog/` **del programa**
     (no confundir con `dev/changelog/`, el de la web), desde la versión actual de
     `tools/site.json` hasta la nueva

2. **Qué afirma la web hoy** (el mapa está en `dev/estructura-web.md`, «Dónde vive
   cada dato que envejece»):
   - la versión: `tools/site.json`, los `<span data-v>` y, sobre todo, las notas que
     la llevan **escrita**: `grep -rn "0\.1\.235" --include=*.html .` (con la versión
     vigente de `site.json` en lugar de 0.1.235) y descartando los `data-v`. Cada
     una afirma algo de esa versión;
   - la licencia (portada, `products/`, `about/`, pie) y los números que se repiten:
     métodos, búsquedas, modelos de resistencia, herramientas MCP, tests y casos
     de validación (portada, `products/slip2d.html`, `ai/`, `verification/`,
     `docs/reference/mcp.html`…);
   - el estado «available» / «planned» de cada programa (`products/index.html`,
     portada, menú);
   - los ejemplos y las figuras calculadas: ¿cambia algún resultado con la versión
     nueva? (`examples/`, héroe, figuras de `docs/theory/`).

3. **Preséntame una tabla de diferencias**: dato · lo que dice la web · lo que dice
   el programa (con su fuente) · dónde está (ruta de la página, en inglés y en
   español). Marca cada diferencia como **crítica** (licencia, versión, estado del
   programa, afirmaciones de capacidad falsas, una limitación que ya no existe o
   una nueva que la web no cuenta) o **menor** (redacción, matiz). Para cada nota
   con la versión escrita, di si **sigue valiendo** en la versión nueva
   (verificado en el código).

4. **Espera mi OK.** Después aplica solo lo aprobado, sin tocar CSS, JS ni layout:
   - `tools/site.json` (`version` y `version_date`) y `python tools/sitio.py`
     completo: la versión se propaga sola a los `<span data-v>` y al pie;
   - los textos ingleses (skill `contenido-tecnico`) y las notas con versión;
   - lo que depende de un cálculo: recalcula la validación con
     `..\desarrollo\herramientas\recalcular_validacion.py` sobre una copia de ese
     commit (`git archive`), y rehaz los ejemplos y las figuras con la versión
     nueva (modelos en `..\desarrollo\modelos-ogr\`, `.ogr` publicados en
     `assets/models/`);
   - **el español**: los mismos cambios en `desarrollo/traduccion/<clave>.es.html` y
     `traduccion.py montar`;
   - `python tools/sitio.py --check` a 0 errores y una nota en `dev/changelog/`.

Si un dato no aparece en ninguna fuente del programa, **dilo** en lugar de
estimarlo: puede que sobre en la web. Y lo que no está publicado en el programa no
se documenta.
