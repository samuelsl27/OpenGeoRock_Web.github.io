# Hoja de ruta de la web

Orden previsto. Cada punto se implementa por el flujo de
`spec/features/NNN-nombre/` y se aprueba antes de tocar las páginas.

## Hecho en el rediseño v3 (2026-10-01 y 02)

El rediseño vive en la rama `rediseno-v3` hasta que se publique. Cierra los puntos
que esta hoja de ruta tenía pendientes:

- **Imágenes optimizadas**: fotos y logotipos en `assets/img/`, en WebP o PNG,
  ninguno por encima de 300 KB.
- **Favicon, `og:image` y metadatos sociales**: en la cabeza de cada página
  (`tools/partials/head.html`) y en `assets/img/`.
- **Descargas**: `download/`, con la instalación desde el código fuente. Los
  instaladores firmados siguen pendientes y se marcan como *planned*.
- **Documentación**: `docs/`, en cinco capítulos (estructura en `tools/site.json`).
- **Sección de validación**: `verification/`.
- **Bilingüe**: inglés en `/` y español en `/es/`, con las mismas rutas.
- **Servidor MCP destacado** (`ai/`), **ejemplos con modelos `.ogr`** (`examples/`)
  y figuras calculadas con el propio programa.

## Pendiente (en este orden)

1. **Capítulo 4 de la documentación (verificación)**: `docs/verification/` —
   `methodology`, `slope-benchmarks` y `analytic-checks`—, ya declarado en
   `tools/site.json` y enlazado desde otras páginas, en inglés y en español.
2. **Paridad del español**: las páginas inglesas que aún faltan en `/es/` (las lista
   `python tools/sitio.py --check`).
3. **Instaladores firmados** y su página de descargas, cuando existan. Hoy el
   instalador está *planned* a propósito.
4. **Más ejemplos con modelo descargable**: soportes y análisis sísmico, según
   las notas de desarrollo.
5. **Publicaciones y citas**, según avance la tesis. `about/` ya explica cómo
   citar el programa.

## Mantenimiento continuo

- Ejecutar `/sincronizar` **en cada versión menor** del programa. La web llegó a
  estar 53 versiones y un cambio de licencia por detrás. Hoy documenta la versión
  de `tools/site.json`.
- Con cada versión nueva: **releer las notas de limitación** que llevan la versión
  escrita, y **rehacer los ejemplos y las figuras** si cambian los resultados.
- Revisar la hoja de ruta de la suite cuando cambie el estado de algún programa.

## Decidido que NO se hace

- Blog o sección de noticias. Nadie va a alimentarlo, y un blog muerto envejece
  peor que su ausencia.
- Formulario de contacto. El `mailto:` funciona y no necesita backend.
- Modo oscuro.
- Frameworks de JavaScript o de CSS, bundlers y `package.json`.
- Analítica y cookies.
