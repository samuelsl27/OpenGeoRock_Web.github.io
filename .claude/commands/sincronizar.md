---
description: Sincroniza los datos técnicos de la web con el repositorio OGR-Slip2D
---
Comprueba si la web se ha desalineado del programa. **No cambies nada hasta
el paso 4.**

1. Consigue el estado real del programa. Si hay una copia local de
   `OGR-Slip2D`, léela; si no, usa la API de GitHub o pídeme la ruta:
   - versión → `pyproject.toml`
   - licencia → `pyproject.toml` y `LICENSE`
   - métodos, búsquedas, capacidades y número de tests → `README.md`
   - estado de cada programa de la suite → tabla *Roadmap* del `README.md`
   - novedades desde la última sincronización → `docs/changelog/`

2. Extrae de `index.html` lo que la web afirma hoy: versión (aparece en el
   `.eyebrow` del hero, en `.stats`, en `.sw-status` y en el pie), licencia
   (hero, `.stats`, `#project .meta`, `.specs`, tarjeta `.attrib`, pie),
   métodos y capacidades (`.sw-sub` y `.specs`), y el estado de las filas
   de `.suite-list`.

3. **Preséntame una tabla de diferencias**: dato · lo que dice la web · lo
   que dice el repositorio · dónde está en `index.html`. Marca cada
   diferencia como **crítica** (licencia, versión, estado del programa,
   afirmaciones de capacidad falsas) o **menor** (redacción, matiz).

4. Espera mi OK. Después aplica solo lo aprobado, sin tocar el `<style>`
   ni el layout, y añade una nota en `docs/changelog/`.

Si un dato no aparece en ninguna fuente del programa, **dilo** en lugar de
estimarlo: puede que sobre en la web.
