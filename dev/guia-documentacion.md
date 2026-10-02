# Guía para escribir la documentación de opengeorock.org

Para quien escriba o traduzca páginas de `docs/` (personas o agentes). La
documentación es una **afirmación técnica**: alguien la usará para decidir
sobre un talud real. Precisión antes que extensión.

## 1. Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Índice de capítulos (números, títulos EN/ES, orden) | `tools/site.json` → `docs` |
| Página en inglés | `docs/<capítulo>/<slug>.html` |
| Su traducción | `es/docs/<capítulo>/<slug>.html` (mismo nombre, mismas `id`) |
| Estilos | `assets/css/docs.css` y, para los diagramas `.dg` y `.slope-svg`, `assets/css/site.css` (no añadir `<style>` en las páginas) |
| Plantilla | `dev/plantilla-doc.html` |
| Datos técnicos | el repositorio del programa (`OGR-Slip2D`), **nunca la memoria** |

Tras editar: `node tools/render_math.cjs` (ecuaciones) y
`python tools/sitio.py --check` (cabeceras, numeración, índice, enlaces).

## 2. Esqueleto de una página

Copia `dev/plantilla-doc.html`. No toques lo que hay entre
`<!-- @inc X -->` y `<!-- @end X -->`: lo escribe `tools/sitio.py`
(cabecera, índice lateral, título con su número, «en esta página»,
anterior/siguiente). Tú escribes solo dentro de
`<article class="doc prose">`, más `<title>` y `<meta name="description">`.

El título de la página (h1) y su número salen de `site.json`. Dentro del
artículo, el primer párrafo lleva `class="lede"` y resume la página en dos o
tres frases.

## 3. Componentes

| Necesito | Marcado |
|---|---|
| Sección numerada (3.2.1…) | `<h2 id="slug-en-ingles">Título</h2>` — el número lo pone `sitio.py`. **Siempre con `id` explícito en inglés** (la traducción conserva el mismo) |
| Subsección | `<h3 id="…">…</h3>` (sin número) |
| Ecuación destacada (numerada) | `<div class="eq" id="eq-bishop" data-tex="F = \dfrac{…}{…}"></div>` |
| Matemática en línea | `<span class="m" data-tex="\phi'"></span>` |
| «donde…» tras una ecuación | `<p class="where">where</p><dl class="symbols"><dt><span class="m" data-tex="c'"></span></dt><dd>effective cohesion (kPa)</dd>…</dl>` |
| Figura numerada | `<figure class="fig" id="fig-…"><div class="art"> SVG o &lt;img&gt; </div><figcaption>Texto del pie.</figcaption></figure>` |
| Captura del programa | `<figure class="fig shot-fig" id="fig-…"><div class="art"><img src="…webp" alt="…" width="…" height="…" loading="lazy"></div><figcaption>…</figcaption></figure>` |
| Tabla numerada | `<figure class="tbl" id="tbl-…"><figcaption>Título.</figcaption><div class="table-wrap"><table class="data">…</table></div></figure>` (números a la derecha: `class="n"` en `td`/`th`) |
| Referencia cruzada | `<a class="xref" href="#eq-bishop"></a>` → «Eq. (3.2.4)»; a otra página: `href="../theory/methods.html#eq-bishop"`; a una página entera: `href="../theory/methods.html"` → «Section 3.2». El texto lo pone `sitio.py` |
| Cita | `<a class="cite" href="../reference/bibliography.html#bishop1955">Bishop (1955)</a>` — clave de la §7 |
| Cómo lo hace el programa | `<div class="impl"><span class="label">In OGR Slip2D</span><p>…</p><span class="src">Source: <a href="https://github.com/samuelsl27/OGR-Slip2D/blob/main/ogr_slip2d/methods/bishop.py">ogr_slip2d/methods/bishop.py</a></span></div>` (ES: «En OGR Slip2D», «Código:») |
| Aviso | `<div class="note"><span class="label">Note</span><p>…</p></div>`; `note warn` para limitaciones; `note water` para agua |
| Menú o botón del programa | `<span class="ui">Analysis → Compute</span>`; teclas `<kbd>Ctrl</kbd>+<kbd>T</kbd>` |
| Bloque de código | `<div class="code"><pre><code>…</code></pre></div>` (escapa `<`, `>` y `&`) |
| Tarjetas de enlaces | `<div class="cards-doc"><a href="…"><b>Título</b><span>Una línea.</span></a>…</div>` |

### Ecuaciones (KaTeX)

- TeX dentro del atributo: escapa `"` como `&quot;`, `<` como `&lt;`, `>` como
  `&gt;` y `&` como `&amp;` (en matrices: `&amp;`).
- Usa `\dfrac` en ecuaciones destacadas, `\tfrac` o `/` en línea.
- Notación común (§6): primas para efectivas (`c'`, `\phi'`, `\sigma'_n`),
  `F` para el factor de seguridad, `\alpha` inclinación de la base, `W` peso…
- Macros disponibles: `\cp` (c′), `\phip` (φ′), `\sigmap` (σ′), `\tanphi` (tan φ′), `\FS` (F) y `\dd` (d recta de las diferenciales).

### Figuras SVG en línea

Usa la clase `dg` y su vocabulario (definido en `site.css`, para que también lo usen las páginas que no son de documentación): `.ln` trazo
principal, `.thin`, `.dash`, `.crit` (superficie crítica, bermellón), `.grn`
(superficies de búsqueda), `.wat` (agua), `.frc` + `.arrowhead` (fuerzas),
rellenos `.s0`–`.s3` (arena, arcilla, grava, roca), `.hl` resaltado, `text`
(mono 13 px), `text.it` (símbolos en cursiva serif), `text.mute`.
**Nada de colores literales**. Cada SVG lleva `viewBox`, `role="img"` y un
`<title>`; si usa marcadores (`<marker>`), su `id` debe ser único en la
página (p. ej. `arrow-fbd`). Las figuras deben ser **verdaderas**: una dovela
dibujada con fuerzas que no actúan en ese método es un error.

## 4. Cómo se escribe

- **Inglés británico** en EN (*behaviour, optimisation, modelling, licence*),
  castellano técnico en ES. Términos geotécnicos correctos: *factor of safety*,
  *slip surface*, *pore pressure*, *limit equilibrium*, *seepage*; en ES
  *factor de seguridad*, *superficie de rotura*, *dovela*, *presión
  intersticial*, *nivel freático*, *grieta de tracción*, *peso específico*,
  *coeficiente parcial*, *desembalse rápido*. El glosario completo, alineado con la interfaz española del programa, está en `../desarrollo/traduccion/INSTRUCCIONES.md`.
- **Unidades SI** (m, kN, kPa, kN/m³, grados).
- **Cada fórmula con su fuente original** (autor y año), nunca el programa
  comercial que la implementa. **Ninguna marca de software de terceros.**
- **Lo que hace OGR Slip2D, exactamente**: ids, valores por defecto,
  límites y comprobaciones, sacados del código. Si el código declara una
  limitación o anomalía (p. ej. D171 en Hoek-Brown generalizado, D226 en el
  Eurocódigo 7), **la página la cuenta**, sin maquillarla.
- **Sin superlativos ni garantías.** Un proyecto lo firma una persona.
- Si no estás seguro al 80 %, **no lo escribas**: déjalo anotado en un
  comentario `<!-- PENDIENTE: … -->` y avisa.
- Los menús se nombran como aparecen en pantalla (en inglés; el programa
  arranca en inglés), también en las páginas en castellano.

## 5. Traducción al castellano

Misma estructura, mismas `id`, mismas figuras y ecuaciones (el `data-tex`
no se traduce, salvo palabras en `\text{}`), mismos enlaces con la ruta
`es/`. Se traducen el texto, los pies, los `alt`, los `title` de los SVG y
las etiquetas (`Note` → `Nota`, `In OGR Slip2D` → `En OGR Slip2D`,
`Source:` → `Código:`).

## 6. Notación común

| Símbolo | Significado | Unidad |
|---|---|---|
| F | factor de seguridad | — |
| c′, φ′ | cohesión y ángulo de rozamiento efectivos | kPa, ° |
| c_u (s_u) | resistencia al corte sin drenaje | kPa |
| W | peso de la dovela | kN/m |
| b, l | ancho de la dovela y longitud de su base (l = b sec α) | m |
| α | inclinación de la base de la dovela | ° |
| β | inclinación de la superficie del terreno sobre la dovela | ° |
| N, N′ | fuerza normal total y efectiva en la base | kN/m |
| S, S_m | resistencia disponible y movilizada en la base (S_m = S/F) | kN/m |
| u | presión intersticial en la base | kPa |
| E, X | fuerzas entre dovelas normal y tangencial | kN/m |
| λ, f(x) | factor de escala y función de fuerzas entre dovelas | — |
| θ | inclinación de la resultante entre dovelas | ° |
| k_h, k_v | coeficientes sísmicos horizontal y vertical | — |
| γ, γ_w | peso específico del suelo y del agua | kN/m³ |
| σ′_n, τ | tensión normal efectiva y tangencial en la base | kPa |

## 7bis. Trabajo en paralelo (varias personas o agentes a la vez)

- Cada cual edita **solo sus páginas**. No se tocan `assets/css`, `assets/js`,
  `tools/partials`, `tools/site.json` ni páginas ajenas: si hace falta un
  componente nuevo, se pide.
- Ecuaciones: `node tools/render_math.cjs docs/theory/mi-pagina.html` (solo
  tus archivos).
- Sincronizar: `python tools/sitio.py --only docs/theory/mi-pagina.html`
  (**nunca sin `--only`** mientras otros trabajan: reescribiría sus páginas).
- Comprobar: `python tools/sitio.py --only … --check` lista los problemas de
  todo el sitio; mira solo los tuyos.
- Curvas y valores de las figuras: calcúlalos importando el propio programa
  en un proceso aparte (`import ogr_core…`), de solo lectura, para que la
  figura dibuje lo que el programa calcula.

## 7. Claves de la bibliografía

`docs/reference/bibliography.html` define cada entrada con `id` = clave. Usa
solo estas (añadir una clave = añadirla a la bibliografía; la versión ES se
monta desde la EN). Lista generada de la bibliografía el 2026-10-02
(90 claves):

abramson2002 · aitken1926 · arai1985 · balmer1952 · barton1977 · barton1990 ·
bathe1979 · berg2009 · bishop1955 · bishop1960 · boutrup1980 · brooks1964 ·
cai2000 · carsel1988 · celia1990 · cheng2007 · chew1989 · ching1983 ·
cornell1969 · coulomb1776 · darcy1856 · dowell1971 · duchon1977 · duncan1990 ·
duncan2005 · duncan2014 · en1997 · en1998 · esterhuizen2001 · fellenius1927 ·
frank2004 · fredlund1977 · fredlund1978 · fredlund1994 · gardner1958 ·
giam1989 · greco1996 · harder1972 · hoek1980 · hoek2002 · iman1982 ·
ingber1989 · ito1975 · janbu1973 · jewell1996 · jibson1993 · kennedy1995 ·
kramer1996 · ladd1974 · li2004 · lowe1960 · mckay1979 · mercer2012 ·
metropolis1949 · mitsch1985 · mooney1985 · morgenstern1963 · morgenstern1965 ·
mualem1976 · neuman1973 · newmark1965 · patton1966 · perko2009 · prandtl1921 ·
qu2013 · reissner1924 · richards1931 · ruppert1995 · shepard1968 ·
siegel1981 · skempton1948 · skempton1954 · skempton1957 · skempton1957b ·
spencer1967 · steffensen1933 · su2009 · terzaghi1943 · terzaghi1950 ·
terzaghi1967 · turnbull1967 · ukritchon2017 · usace1970 · usace2003 ·
vangenuchten1980 · wegstein1958 · whitman1967 · wilson1983 · wright1987 ·
yamagami1988
