# 2026-11-22 — Rutas relativas en lugar de las del PC anterior

Solo documentación del repositorio: ninguna página, ninguna herramienta, nada de lo que sirve
GitHub Pages como parte del sitio.

## Qué cambió

El 2026-11-22 la suite se mudó de `C:\Samuel\OGR_Suite` a `C:\Desarrollo\OGR_Suite`. Cuatro
archivos nombraban la ruta absoluta del PC anterior; ahora usan la ruta relativa a la raíz de
este repositorio, que no depende del PC:

- `AGENTS.md` y `dev/estructura-web.md`: la carpeta de trabajo es `../desarrollo/`.
- `.claude/commands/sincronizar.md` y `.claude/skills/contenido-tecnico/SKILL.md`: la copia
  local del programa es `../../Slip2D/OGR-Slip2D`.

`.claude/settings.local.json.example` conserva `C:/Samuel/OGR_Suite` a propósito: es una
plantilla cuyas rutas sustituye un script.

## Qué se comprobó

- `git grep` no encuentra la ruta antigua fuera de ese `.example`.
- `python tools/sitio.py --check`: 94 páginas, 0 errores, 0 avisos, sin tocar ninguna página.
