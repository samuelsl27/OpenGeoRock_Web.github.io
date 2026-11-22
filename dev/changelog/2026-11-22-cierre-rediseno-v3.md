# 2026-11-22 — Cierre de la rama `rediseno-v3`

Solo documentación del repositorio y una rama local: ninguna página, ninguna herramienta.

## Qué cambió

- La rama local `rediseno-v3` se borró con `git branch -d`. Estaba entera en `main`
  (`git log main..rediseno-v3` vacío; apuntaba a `5e8c84b`) y no existía en GitHub
  (`git ls-remote --heads origin` solo da `main`).
- `AGENTS.md`, en «Flujo de trabajo»: la regla de las ramas ya no nombra `rediseno-v3` y queda
  como en los otros repositorios de la suite. Solo vive `main`. Un cambio grande va en una rama
  corta que se borra, en GitHub y en local, al fusionarla. Una rama sin fusionar no se borra sin
  OK, y si lleva algo que `main` no tiene, antes se archiva con una etiqueta `archivo/<nombre>`.
  Lo de no fusionar, commitear ni publicar sin OK no cambia.

## Qué se comprobó

- `python tools/sitio.py --check`: 94 páginas, 0 errores, 0 avisos.

## Sin tocar

- `.claude/commands/publicar.md` (paso 8) y `spec/constitution/roadmap.md` todavía nombran
  `rediseno-v3`.
