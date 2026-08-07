---
description: Añadir o rehacer una sección de la página siguiendo el flujo SDD
---
Vas a tocar la estructura de la página. Eso se hace por especificación, no
sobre la marcha.

1. Lee `docs/estructura-web.md` y localiza dónde encaja la sección.
2. Crea `spec/features/NNN-nombre/` copiando `spec/features/000-plantilla/`
   y rellena `spec.md`: qué aporta al visitante, qué datos muestra y **de
   dónde sale cada dato**, y los criterios de aceptación.
3. En `plan.md`: qué componentes **ya existentes** vas a reutilizar
   (consulta la skill `diseno-web`). Si necesitas uno nuevo, dilo aquí y
   **espera mi OK** — es un cambio de diseño.
4. En `tasks.md`: la lista de pasos verificables.
5. **Enséñame los tres archivos y espera mi OK antes de tocar
   `index.html`.**
6. Al implementar: añade el `id`, la entrada en `nav.primary`, la entrada
   en el pie y el comentario `<!-- ====== NOMBRE ====== -->`. Actualiza
   `docs/estructura-web.md`.
7. Termina con `/revisar`.

Argumento: $ARGUMENTS
