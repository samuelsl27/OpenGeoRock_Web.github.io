# 2026-11-21 — Una sección «Desarrollo» en el README

Solo cambia `README.md`: ninguna página, ninguna herramienta, nada de lo que sirve GitHub Pages
como parte del sitio.

## Qué se añadió

Una sección «Desarrollo», entre «Regenerarlo» y «Publicar», para quien clona solo este
repositorio: qué hace falta (Python 3 sin ningún paquete, Node solo para las ecuaciones, git),
las órdenes para comprobar y ver el sitio, qué **no** viene en el clon (`../desarrollo/`) y qué
piden dos de sus herramientas (Pillow y el programa OGR Slip2D instalado), y dónde está la guía
para montar la suite entera (`DESARROLLO.md`, en la raíz de la carpeta de trabajo `OGR_Suite`).

## Qué se comprobó

En un clon nuevo de GitHub (`1a35f6c`), en una carpeta temporal y sin `../desarrollo/`, con el
Python del sistema (3.14.7) y Node 24.18.1:

- `python tools/sitio.py --check`: 94 páginas, 0 errores, 0 avisos.
- `git status` después: limpio. La herramienta es idempotente sobre lo publicado.

## Qué se encontró

- `tools/site.json` documenta la versión 0.1.235 del programa, y el programa va por la 0.1.477.
  Ponerla al día es otro trabajo (`/sincronizar`), no de esta nota.
- La rama local `rediseno-v3`, que `AGENTS.md` nombra como el sitio del rediseño, está entera en
  `main` y solo existe en el PC de desarrollo.

## Sin comprobar

- `node tools/render_math.cjs` y las herramientas de `../desarrollo/`: no se han lanzado.
