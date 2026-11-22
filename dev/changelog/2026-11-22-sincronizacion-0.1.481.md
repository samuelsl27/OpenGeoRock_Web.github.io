# 2026-11-22 — La web pasa a documentar OGR Slip2D 0.1.481 (fase A)

La web documentaba la 0.1.235 (2026-10-01). Ahora documenta la **0.1.481**, cotejada con el
commit publicado `99e40f9` de OGR-Slip2D y con OGR-Core `v0.2.2`, la etiqueta que fija su
`pyproject.toml`. Plan aprobado: `../desarrollo/notas/plan-sincronizacion-v0.1.481.md`, fase A.
Las fases B (contenido nuevo de Slip2D: Sarma, superficies no circulares del usuario, agua) y
C (FEM2D, OGR-Core y OGR Data) van aparte.

## Qué cambió

- `tools/site.json`: 0.1.481 · 2026-11-22 (fecha del commit de la versión, `79b001c`).
- **Cifras.** Métodos 9 → 10 (Sarma con dovelas no verticales, v0.1.464, sin caso de validación
  todavía, y así se dice). Modelos de resistencia 22 → 23 (`step_function`). Herramientas MCP
  74 → 75 (`user_surface_edit`); cobertura 121 de 145. Tests 5 265 → 7 551 casos (7 550 pasan,
  1 saltado; desde la v0.1.473 los del núcleo corren en OGR-Core). Búsquedas (7) y casos de
  validación (7) sin cambios.
- **Instalación y descarga.** Git pasa a ser imprescindible (pip trae `ogr-core` de GitHub); sale
  la vía del ZIP sin Git y `pyclipper`; entra `ogr-core`.
- **Código común en OGR-Core.** Las rutas «Source:» de `ogr_core/…` y del antiguo `ogr_fem2d`
  apuntan a `OGR-Core/blob/v0.2.2/…`; `ogr_fem2d` → `ogr_core.fem` en la API de Python;
  `products/`, categoría 02, dice que el núcleo de elementos finitos vive en OGR-Core.
- **Notas «0.1.235».** Revisadas una a una contra el código: las que siguen valiendo llevan
  «0.1.481»; las que ya no valen se quitan o se reescriben (Eurocódigo 7: γG, DA3, cargas por
  acción y sísmico; carga repartida hacia arriba; Hoek–Brown con envolvente de Mohr exacta;
  Compute Statistics desde el menú; Cancel; Restore Defaults; casillas de Preferences;
  deshacer; capas de agua, Measure y Dimension en Interpret; θs, θr y Ss; anotaciones y centro
  de superficie con clics; Convert Boundary; papeles DXF).
- **Recalculado con la 0.1.481** (resultados en `../desarrollo/modelos-ogr/*_v0.1.481.json` y
  `../desarrollo/notas/validacion-v0.1.481.json`):
  - cambian: Hoek–Brown (Fig. 3.5.1, columna HB de la Tabla 3.5.3; la antigua Fig. 3.5.2 se quita
    porque la curva evaluada y la envolvente de Mohr son ya la misma); Block Search (Figs. 3.4.3,
    3.4.4 y 3.4.5; ejemplos 2a, Spencer 0,988 → 0,991, y 2b, 1,180 → 1,184, con sus figuras);
    tablas de la norma 2.11.2, 3.12.1 y 3.12.2, y los ejemplos DA2/DA1-C1; Fig. 3.7.4 (segunda
    curva de retención, v0.1.278); §4.3.6 (2,8 → 3,5 × 10⁻⁷ m); el censo de rechazos del inicio
    rápido;
  - no cambian: los 7 casos de validación, el talud de ejemplo (1,0914331494631124, Bishop),
    los ejemplos 1, 2, 3, 4 y 5, y el resto de figuras de teoría y verificación.
- **Capturas** rehechas con la interfaz de la 0.1.481: `project-settings.webp`,
  `project-settings-design.webp` y `hydraulic-properties.webp`.
- Documentación interna: `.claude/skills/contenido-tecnico/SKILL.md`, `.claude/commands/
  sincronizar.md`, `dev/estructura-web.md` y `spec/constitution/tech-stack.md` (código común en
  OGR-Core; versión vigente).
- Fuera del repositorio: las herramientas de `../desarrollo/herramientas/` tenían la ruta del PC
  anterior escrita; ahora la sacan de su propia ubicación.

## Qué se comprobó

- `python tools/sitio.py --check`: 94 páginas, 0 errores, 0 avisos.
- `traduccion.py comprobar` en todas las páginas tocadas; el español se montó con `montar`.
- Ningún «0.1.235» queda en las páginas.
- Vista local a 375, 768 y 1440 px: ver el informe de la sesión.

Anomalías del programa encontradas: `../desarrollo/notas/anomalias-programa.md`, A6.
