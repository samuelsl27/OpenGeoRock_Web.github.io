---
name: contenido-tecnico
description: Cómo verificar y escribir las afirmaciones técnicas de la web (versión, licencia, métodos, capacidades de OGR Slip2D), cómo se citan las fuentes, cómo se documenta una limitación del programa, qué terminología usar (EN y glosario ES) y cómo se hacen las figuras con datos reales. Úsalo antes de tocar cualquier cifra, nombre de método, cita o descripción de lo que el programa sabe hacer.
---

# Contenido técnico: de dónde sale cada dato

La web afirma cosas sobre un programa de ingeniería, y su documentación se usará
para decidir sobre un talud real. Quien la lea puede basar un proyecto en ella.
**Ningún dato se escribe de memoria.**

## La fuente de cada dato

Todo sale del repositorio [`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D)
(copia local del autor: `C:\Samuel\OpenGeoRock_Slip2d\OGR-Slip2D`):

| Dato en la web | Fuente exacta |
|---|---|
| Versión que documenta la web | `tools/site.json` (`version`, `version_date`); debe coincidir con `pyproject.toml` → `[project] version` **del commit publicado** |
| Licencia | `pyproject.toml` → `license`, y `LICENSE` |
| Métodos de equilibrio límite (ids, valores por defecto) | `ogr_slip2d/methods/`, `ogr_slip2d/interslice.py`, `ogr_core/project/settings.py` |
| Algoritmos de búsqueda | `ogr_slip2d/search.py` |
| Modelos de resistencia | `ogr_core/materials/builtin_models.py` |
| Filtración y agua subterránea | `ogr_fem2d/solvers/seepage.py`, `ogr_core/hydraulic/` |
| Menús, diálogos y comportamiento de la interfaz | `ogr_gui/main_window.py` y los diálogos de `ogr_gui/dialogs/` |
| Servidor MCP: herramientas, perfiles, cobertura | `ogr_api/inventory.py`, `ogr_mcp/`, `docs/mcp/*.md` (el código manda sobre la prosa) |
| Número de tests | `docs/changelog/CHANGELOG_v<versión>.md`, línea «Suite entera». **No** el README del programa, que puede ir por detrás (hoy dice 4836; el changelog de la 0.1.235 dice 5265) |
| Casos de validación | `validacion/casos/*/esperado.json` (valores y fuente) y `validacion/README.md` |
| Estado de cada programa de la suite | tabla *Roadmap* del `README.md` |
| Novedades entre versiones | `docs/changelog/` |

Ya hay fichas extraídas del código de la 0.1.235 en
`../desarrollo/notas/ficha-tecnica-motor-v0.1.235.md` y
`../desarrollo/notas/ficha-producto-interfaz-v0.1.235.md`: sirven para localizar
rápido, no sustituyen al código. Si el dato no está en ninguno de estos sitios,
**no va en la web**.

**El código manda.** Cuando el README o un docstring discrepan del código, gana el
código (decisión del 2026-10-01), y la web cuenta lo que el código hace.

## Qué versión se documenta

La web documenta **una versión concreta**, la de `tools/site.json`. `sitio.py` la
escribe en todos los `<span data-v>` y en el pie. Se coteja con el **commit
publicado** de esa versión, no con el árbol de trabajo del autor, que puede ir
por delante (a 2026-10-02: la web documenta la 0.1.235 y el árbol de trabajo ya es
la 0.1.236, sin publicar). Un dato tomado del árbol de trabajo sería falso.

```bash
# desde una copia del repositorio del programa, solo lectura
git show <commit>:pyproject.toml | grep -i '^version\|license'
git show <commit>:docs/changelog/CHANGELOG_v0.1.235.md | grep -n 'Suite entera'
ls ogr_slip2d/methods/
```

Para ejecutar el programa en una versión publicada (recalcular una cifra), usa una
copia de ese commit aparte (`git archive`) delante en `PYTHONPATH`, nunca el árbol
de trabajo. Si no tienes el repositorio a mano, dilo y **deja el dato como está**.
Un número desactualizado es un problema; un número inventado es un fallo de
integridad.

Algunas notas de las páginas dependen de la versión y llevan **escrita** («Version
0.1.235», «en la versión 0.1.235») en lugar de `<span data-v>`, porque afirman algo de
esa versión concreta. Al cambiar de versión hay que revisarlas una a una
(`/sincronizar`): puede que la limitación ya no exista.

## Cómo se documenta una limitación del programa

El programa tiene defectos declarados y anomalías sin declarar. La web **los
cuenta, sin maquillarlos ni corregirlos**:

1. **Verifica en el código** (o ejecutándolo, en un proceso aparte y de solo
   lectura) antes de afirmar que el programa no hace algo. Un menú que existe pero
   no hace nada, un valor que no se aplica, una casilla sin conectar: se
   comprueba, no se supone.
2. **Se escribe en una caja de aviso** `note warn`, con una etiqueta que dice qué es
   (*Known limitation*, *Known defect*, *Version 0.1.235*, *Not applied in this
   version (D226)*; en ES, *Limitación conocida*, *Defecto conocido*, *Versión
   0.1.235*…):

   ```html
   <div class="note warn"><span class="label">Known limitation</span><p>…</p></div>
   ```
3. **Con su identificador** cuando el propio código lo declara (D171 en Hoek–Brown
   generalizado, D226 en el Eurocódigo 7), y con la **versión** escrita.
4. **Con lo que hace el usuario en su lugar**, si hay una salida (por ejemplo,
   comprobar la superficie crítica con otra búsqueda).
5. **Sin culpar ni suavizar**: «The program's own source records (defect D171)
   that…», «reported, not corrected».
6. **Lo que no puedes verificar no se publica como hecho.** Si hace falta que el
   autor confirme una lectura del código, déjalo en
   `../desarrollo/notas/pendientes-docs.md` y no en la página.
7. **Las anomalías nuevas se informan con evidencia al autor, no se corrigen.** El
   repositorio del programa queda fuera del alcance del trabajo en la web. Se anotan en
   `../desarrollo/notas/anomalias-programa.md` con qué pasa, un control, por qué
   importa y cómo reproducirlo.

Los consejos de ingeniería (no son limitaciones del programa) van en
`note warn` con la etiqueta *Engineering judgement* (ES: *Criterio de
ingeniería*): un resultado se contrasta con cálculos independientes y un proyecto
lo firma una persona, no un programa.

## Cómo se cita

- **Fórmulas y métodos se citan por su fuente científica original** (autor y año:
  Bishop 1955, Spencer 1967, Morgenstern–Price 1965, Hoek et al. 2002), nunca por
  el programa comercial que los implementa. **La web no menciona marcas de
  software de terceros.** Si el código solo atribuye un modelo a un programa
  comercial y no a su fuente, la referencia original se busca y se verifica; no se
  inventa una atribución.
- **En el texto**: `<a class="cite" href="../reference/bibliography.html#bishop1955">Bishop
  (1955)</a>`. Al final de cada página de teoría, `<h2 id="references">` y una lista
  `ul.refs`.
- **La clave es el `id`** de la entrada en `docs/reference/bibliography.html`: esa
  página es la fuente de verdad (la lista de claves de `dev/guia-documentacion.md`
  puede ir por detrás). Una clave nueva se añade a la bibliografía **en inglés y en
  español**; `sitio.py --check` marca como error una cita cuya ancla no existe.
- **Los datos bibliográficos no se escriben de memoria.** Se cotejan con el
  registro del editor o con Crossref (autores, título, revista, volumen, páginas,
  año). Lo que no se pueda cotejar no se añade; se anota la duda en
  `../desarrollo/notas/` (hay una verificación de toda la bibliografía en
  `verificacion-bibliografia.md`). Si el año del código y el de la publicación
  difieren, vale el de la publicación verificada.
- Referencias cruzadas dentro de la documentación: `<a class="xref" href="#eq-bishop"></a>`,
  sin escribir el número a mano.

## Cómo se redacta

- **Estado honesto.** El programa está en desarrollo activo y es una versión
  preliminar. Se dice: *pre-release*, *in active development*. No se dice
  *stable*, *production-ready* ni *battle-tested*.
- **Código público ≠ versión publicada.** El código es legible y clonable; no hay
  instaladores firmados. Se distingue: *source available* frente a *installers ·
  planned*.
- **Sin superlativos de marketing.** *The best*, *revolutionary*, *industry-leading*
  no aparecen. La web convence enseñando resultados verificables.
- **Sin garantías.** Nada puede sugerir que los resultados no necesitan
  comprobación independiente.
- **Que se lea escrito por una persona.** El autor revisó la web en octubre de
  2026 porque la redacción delataba a una IA. Un título describe su sección
  (*How we verify the program*, no *Checked against references, not believed.*);
  nada de eslóganes en dos tiempos, contrastes «X, not Y» en cada párrafo, frases
  lapidarias de remate, tríadas forzadas ni una raya por frase (en castellano,
  ninguna en la prosa). Mejor un dato que un adjetivo; frases de longitud
  variada; en las páginas del proyecto habla el equipo (*we*, «nosotros») con
  moderación, y la documentación es impersonal. Ejemplos reales, antes y
  después, en `../desarrollo/traduccion/ESTILO-HUMANO.md`.
- **El mensaje del MCP lleva fecha y «hasta donde sabemos», nunca «el primero» a
  secas** (no es defendible). Redacción adoptada: *One of the first geotechnical
  programs with an official MCP server — and, to our knowledge (October 2026), the
  first open-source slope-stability program to ship one.* / *Uno de los primeros
  programas geotécnicos con servidor MCP oficial y, hasta donde sabemos (octubre de
  2026), el primer programa de estabilidad de taludes de código abierto que lo
  incluye.*
- **Unidades SI** (m, kN, kPa, kN/m³, grados). En `/es/`, los números del programa
  conservan el punto decimal (1.290) y el espacio fino para los miles (1 859): son
  datos que coinciden con lo que muestra la pantalla.
- **Los menús y botones del programa se nombran como aparecen en pantalla**, en
  inglés, también en castellano: `<span class="ui">Analysis → Compute</span>`;
  teclas, `<kbd>Ctrl</kbd>+<kbd>T</kbd>`. Las capturas, con la interfaz en inglés.
- **Inglés británico** en EN (*behaviour*, *optimisation*, *licence*); **castellano
  técnico de España, con tuteo**, en ES (nunca «usted»).
- **Lo que hace OGR Slip2D, exactamente**: ids, valores por defecto, límites y
  comprobaciones salen del código, no de lo que parece razonable.

## Figuras con datos reales

Una figura que muestra **resultados** (factores de seguridad, presiones, curvas,
convergencia) sale de un **cálculo real del programa**, no de valores escritos a
mano ni de otro programa:

1. Se construye el modelo (en la ventana, o por MCP con `model_define`), se calcula
   con la versión documentada y se guarda el `.ogr` en `../desarrollo/modelos-ogr/`.
2. Se exportan los resultados a JSON (con `python_exec`) y de ahí un script de
   `../desarrollo/herramientas/` genera el SVG (`generar_svg_talud.py`,
   `generar_svg_presiones.py`, `generar_svg_ff_fm.py`, `generar_svg_desembalse.py`).
   `inyectar_svg.py` lo mete entre `<!-- svg:NOMBRE -->` y `<!-- /svg:NOMBRE -->`.
3. Si la página ofrece el modelo, se publica el `.ogr` mínimo en `assets/models/`.
4. El pie de figura dice qué se dibuja y los números del texto **coinciden con la
   figura y con la tabla**. Si el motor cambia en una versión nueva, las figuras y
   los ejemplos se **recalculan**.
5. Los esquemas dibujados a mano (`.dg`) han de ser **verdaderos**: no se dibujan
   fuerzas que ese método no tiene.
6. Las capturas de ventanas se hacen con `QWidget.grab()` desde `python_exec` y se
   optimizan a WebP (≤ 300 KB).

Los números de validación (casos publicados, comprobaciones, tests) se recalculan
con `../desarrollo/herramientas/recalcular_validacion.py` sobre la versión
publicada, nunca de memoria ni de un recuento antiguo.

## Cosas que se han desalineado antes

Como recordatorio de cuánto puede derivar la web si nadie la sincroniza:

- La web dijo **GPL-3.0** durante 17 versiones después de que el proyecto pasara a
  **AGPL-3.0-or-later** (en la v0.1.43), y llegó a estar **53 versiones** por detrás.
- Mostraba 4 métodos cuando había 7, y no mencionaba la filtración por elementos
  finitos, el análisis probabilístico, el DXF, el Eurocódigo 7 ni la línea de
  comandos, todos ya implementados.
- El README del programa dice 4836 tests; la suite de la 0.1.235 cerró con 5265.
- Hay docstrings que no dicen lo que hace el código (por ejemplo, un docstring
  habla de «una única iteración de punto fijo» y el código busca un cambio de signo
  y refina; otro llama GPL-3.0 a la licencia del proyecto, que es AGPL). Por eso se
  lee el código.
- `docs/mcp/README.md` del programa habla de 113 acciones cubiertas de 136; el
  inventario de `ogr_api/inventory.py`, de otras cifras (la web usa las del código).

La lección: la versión y la licencia se revisan **en cada cambio**, aunque el
encargo sea otro.

## Nomenclatura

| Correcto | Incorrecto |
|---|---|
| OpenGeoRock (la suite) | OpenGeoRock Slip2D |
| OGR Slip2D (el programa) | OGR-Slip2D, Slip2D a secas en un titular |
| `ogr-slip2d` (el paquete) | ogr_slip2d en texto corrido |
| factor of safety (FoS) | safety factor, security factor |
| slip surface | failure line, rupture line |
| pore pressure | water pressure |
| limit equilibrium | equilibrium limit |
| finite-element (adjetivo) | finite elements analysis |

### Glosario inglés–español

El de la propia interfaz española del programa cuando existe (`ogr_gui/i18n/`). El
glosario completo está en `../desarrollo/traduccion/INSTRUCCIONES.md`; estos son
los términos que más se repiten.

| Inglés | Español |
|---|---|
| factor of safety (FoS, F) | factor de seguridad (FS, F) |
| slip surface / critical surface | superficie de rotura / superficie crítica |
| slice, method of slices | dovela, método de dovelas |
| interslice force | fuerza entre dovelas |
| limit equilibrium | equilibrio límite |
| pore pressure | presión intersticial |
| water table, piezometric line | nivel freático, línea piezométrica |
| seepage, seepage face | filtración, superficie de rezume |
| groundwater | agua subterránea |
| finite element(s), mesh | elementos finitos, malla |
| boundary condition | condición de contorno |
| hydraulic conductivity | conductividad hidráulica |
| unsaturated, suction | no saturado, succión |
| rapid drawdown | desembalse rápido |
| unit weight | peso específico |
| cohesion, friction angle | cohesión, ángulo de rozamiento |
| effective stress | tensión efectiva |
| undrained shear strength | resistencia al corte sin drenaje |
| weak layer, tension crack | capa débil, grieta de tracción |
| bench, berm, crest, toe | banco, berma, coronación, pie |
| embankment, slope | terraplén, talud |
| search (Grid Search, Block Search…) | búsqueda; los nombres propios se dejan en inglés |
| support, anchor, soil nail | soporte, anclaje, bulón |
| pseudo-static seismic, yield acceleration | sísmico pseudoestático, aceleración de fluencia |
| probability of failure, reliability index | probabilidad de rotura, índice de fiabilidad |
| random variable, probabilistic | variable aleatoria, probabilístico (nunca «probabilista») |
| partial factor, design approach | coeficiente parcial, enfoque de proyecto |
| back analysis | retroanálisis |
| benchmark, validation case | caso de referencia, caso de validación |
| test suite, pre-release | batería de tests, versión preliminar |
| source code, open source | código fuente, código abierto |
| AI agent | agente de IA |
