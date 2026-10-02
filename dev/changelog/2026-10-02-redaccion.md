# 2026-10-02 — Revisión de la redacción: que se lea escrito por una persona

El autor leyó la web publicada y notó dos cosas en el texto: el español sonaba a
traducción (corregido en el commit `b862dc1`) y, en los dos idiomas, **la redacción
delataba que la había escrito una IA**. Esta revisión cambia la forma de las 47
páginas en inglés y en español, sin tocar el contenido técnico.

## Qué se quitó

- **Titulares de eslogan**, el rasgo más visible: «Ask for a slope. Get a factor of
  safety.», «Checked against references, not believed.», «Powerful by design.
  Local by default.», «Model. Compute. Interpret.». Ahora cada título describe su
  sección («Working with an AI agent», «How we verify the program», «Security and
  network access», «The three steps of an analysis»).
- **Contrastes «X, not Y»** retóricos, **frases lapidarias** de remate («a design is
  signed by an engineer, not by a program», «a control that does nothing is worse
  than none»), **tríadas** forzadas y **rayas** en casi todos los párrafos de la
  prosa inglesa (pasan a paréntesis, comas o dos puntos). Se mantienen los
  contrastes que dan información («nx and ny are intervals, not centres») y las
  rayas que son texto literal de la interfaz («Eurocode 7 — DA1 Combination 1»).
- **Entradillas con fórmula** («This chapter defines…, explains… and shows…»): cada
  página empieza ahora por su contenido.
- **Afirmaciones totales y adjetivos de folleto** que no eran literalmente ciertos.

En las páginas principales habla el equipo («we», «nosotros») con moderación; la
documentación sigue siendo impersonal. La regla quedó escrita en
`.claude/skills/contenido-tecnico/SKILL.md` (§ «Cómo se redacta»).

## Errores de contenido que salieron al reescribir

- `docs/user-guide/materials.html` decía que el grupo *Water Parameters* aparece
  siempre; el diálogo lo oculta con un método de agua subterránea por elementos
  finitos (`material_properties_dialog.py`, `grp_water.setVisible(not fea)`).
- `verification/index.html`: «either the number is exact, or the test fails»
  contradecía su propia tabla, que incluye una diferencia del 0.11 %.
- `products/index.html` daba en presente que todos los programas de la suite
  comparten el núcleo; solo existe OGR Slip2D, así que pasa a futuro.
- El menú de productos (`tools/partials/header.*.html`) cambia «Five programs, one
  open core.» por lo que dicen sus columnas: OGR Slip2D disponible, los otros
  cuatro previstos.

## Cómo se hizo y qué se comprobó

Las páginas inglesas se revisaron con el mismo flujo que las españolas: versión
ligera en `../desarrollo/traduccion/`, editada a la vez que la española, y
reconstruida con el nuevo `traduccion.py montar-en` (las españolas, con `montar`).

- `traduccion.py comprobar`: las 47 parejas EN/ES con los mismos `id`, `href`,
  `data-tex` y marcadores (salvo las dos diferencias intencionadas de siempre, en
  `404.html` y `docs/index.html`).
- `../desarrollo/herramientas/comparar_versiones.py`, nuevo: cada página frente a
  la publicada. No cambia ningún `id`, enlace, fórmula ni bloque de código, ni el
  número de párrafos, listas, tablas y figuras; las cifras solo cambian donde un
  titular nuevo nombra «OGR Slip2D» o repite un dato de la página. La lista de
  titulares cambiados está en `../desarrollo/notas/humanizar-titulares-2026-10-02.md`.
- `render_math.cjs`: 4146 ecuaciones, 0 errores (dos más que antes: una condición
  `F < 1` de la guía probabilística pasó de texto a fórmula, en los dos idiomas).
- `sitio.py --check`: 94 páginas, 0 errores, 0 avisos.
- Sin desbordamiento horizontal a 320 y 375 px en las páginas principales y en las
  de documentación más tocadas, en los dos idiomas; consola sin errores.
