# OpenGeoRock — sitio web

Sitio público de la suite **OpenGeoRock** en [opengeorock.org](https://opengeorock.org).
Una sola página estática que presenta el proyecto, el programa **OGR Slip2D**,
la hoja de ruta de la suite y el equipo.

**Dos repositorios, y conviene no confundirlos:**

| Repositorio | Qué es |
|---|---|
| `OpenGeoRock_Web.github.io` | **este**: la web. HTML estático, sin build |
| [`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D) | el programa. Python, es la **fuente de verdad** de todo dato técnico |

Autor y titular del copyright: Samuel Sáez López (UPCT).
El programa es AGPL-3.0-or-later; esta web documenta ese hecho, no lo decide.

> Este archivo es el **contrato de trabajo** con cualquier agente de IA.
> Se consulta antes de cada acción. Si algo aquí contradice lo que parece
> razonable, gana este archivo — y si de verdad está mal, dilo antes de
> saltártelo.

---

## Stack

- **HTML5 estático**. Un único `index.html` con el CSS **en línea** en un
  `<style>` del `<head>`. No hay JavaScript de aplicación.
- **Sin build, sin dependencias, sin gestor de paquetes.** Lo que hay en el
  repositorio es exactamente lo que sirve GitHub Pages.
- **Tipografías**: Inter, Newsreader y JetBrains Mono desde Google Fonts.
- **Despliegue**: GitHub Pages desde `main`, dominio propio vía `CNAME`
  (`opengeorock.org`).

## Comandos

No hay build. Para trabajar:

```bash
python -m http.server 8000     # servidor local → http://localhost:8000
git status && git diff          # ver qué cambió antes de publicar
git push origin main            # publica: Pages redespliega solo
```

**`git push` sobre `main` publica en producción.** No hay entorno de
pruebas intermedio. Revisa en local antes.

## Estructura del proyecto

| Ruta | Contenido |
|---|---|
| `index.html` | La página entera: `<style>` + secciones. Ver `docs/estructura-web.md` |
| `assets/screens/` | Capturas de la aplicación |
| `assets/people/` | Fotos del equipo |
| `assets/logos/` | Logotipos de instituciones colaboradoras |
| `CNAME` | Dominio propio. **No tocar** |
| `spec/` | Especificaciones SDD: constitución y features |
| `docs/` | Mapa de la página, changelog y notas de sesión |
| `.claude/` | Comandos y skills del agente |

---

## Las seis reglas

### 1. La estética no se cambia sin permiso explícito

El diseño está terminado y es deliberado: paleta de papel cálido, un único
acento verde, tres tipografías con papeles fijos. **No propongas ni apliques
rediseños, animaciones, modo oscuro, librerías de UI ni cambios de paleta
por iniciativa propia.**

Puedes cambiar **texto, datos y enlaces** libremente. Para cualquier cosa
que altere cómo se *ve* la página —color, tipografía, espaciado, tamaño,
sombra, radio, layout— **pregunta primero y espera el OK**.

Añadir contenido dentro de un componente que ya existe (una fila más en
`.specs`, un enlace más en el pie) **no** es un cambio estético. Inventar
un componente nuevo, sí.

Los tokens y los patrones están en `.claude/skills/diseno-web/SKILL.md`.
Léelo antes de tocar el `<style>`.

### 2. Todo dato técnico se copia de OGR-Slip2D, no se recuerda

Versión, licencia, número de tests, métodos implementados, capacidades:
la fuente es el repositorio del programa —`pyproject.toml`, `README.md`,
`docs/changelog/`— **no** tu memoria ni lo que ya pone la web.

Un número inventado en un sitio de software de ingeniería es peor que un
número ausente: alguien lo citará.

Si no puedes consultar el repositorio en ese momento, **dilo y deja el dato
como está**. No lo estimes.

### 3. Ningún enlace roto, y ninguna promesa sin fecha

Antes de publicar, cada `href` tiene que resolver. Ojo con dos trampas ya
sufridas:

- La página tuvo enlaces `/cdn-cgi/l/email-protection` con los correos
  ofuscados por Cloudflare. En GitHub Pages **dan 404**: el script que los
  descifra no existe ahí. Los correos van en `mailto:` planos.
- Lo que aún no existe se marca con la clase `.locked` o `.muted` y un
  `title` que explique cuándo llega. **Nunca** un enlace vivo a algo que no
  está publicado.

### 4. La página es una sola: los anclas y el menú van juntos

Cada sección tiene su `id` y su entrada en `nav.primary` y en el pie. Si
añades o renombras una sección, actualiza **los tres sitios**. Una sección
sin entrada en el menú es una sección que nadie encuentra.

### 5. Todo lo visible se prueba en móvil

El CSS tiene puntos de ruptura en 480, 640, 720, 820, 860, 900 y 960 px, y
`nav.primary a:not(.cta)` **desaparece por debajo de 820 px**. Un texto que
cabe en escritorio puede romper la rejilla en móvil.

Prueba a 375 px y a 1440 px como mínimo. El `body` nunca debe hacer scroll
horizontal.

### 6. Las imágenes pesan, y aquí se nota

`assets/` se sirve tal cual, sin optimización. Una foto de 4 MB en el hero
son cuatro segundos de espera en 4G.

Antes de añadir una imagen: redimensiónala al tamaño en que se muestra,
guárdala como WebP o JPEG de calidad 80, y ponle `loading="lazy"` salvo que
esté sobre el pliegue. Presupuesto: **300 KB por imagen**, y si te lo
saltas, di por qué.

---

## Flujo de trabajo

- **Antes de una tarea no trivial, propón un plan y espera mi OK.** Usa
  plan mode.
- **Una tarea a la vez.** Al terminar, dime qué cambiaste y qué comprobaste.
- **Si no estás seguro al 80 %, pregunta. No inventes** — sobre todo en
  cifras técnicas y en afirmaciones sobre lo que el programa sabe hacer.
- **Sé escéptico con lo que te pido.** Si algo huele mal, dilo.
- **Al terminar, lista qué probaste y qué falta por probar.**
- Los cambios con contenido nuevo dejan una nota en `docs/changelog/`.

---

## No hagas

- **No cambies la estética sin preguntar.** Regla 1. Es la más importante.
- **No toques `CNAME`.** Un cambio ahí tira el dominio.
- **No añadas frameworks, bundlers ni `package.json`.** El valor de este
  sitio es que no tiene cadena de construcción: se abre el HTML y ya.
- **No añadas analítica, cookies, píxeles de seguimiento ni fuentes de
  terceros nuevas** sin pedírmelo. Hoy la única petición externa son las
  tipografías de Google.
- **No metas correos ofuscados por Cloudflare.** Ver regla 3.
- **No inventes capacidades del programa.** Si `README.md` de OGR-Slip2D no
  lo dice, la web no lo dice.
- **No conviertas «planeado» en «disponible».** El estado de cada programa
  de la suite se toma de la hoja de ruta del repositorio.
- **No subas binarios grandes** (instaladores, vídeos, PDF pesados). Van en
  las *releases* de GitHub, no aquí.

---

## Convenciones

- **Idioma de la web: inglés.** El repositorio se documenta en castellano
  (este archivo, `spec/`, `docs/`), pero todo texto que ve el visitante va
  en inglés.
- **Terminología geotécnica correcta**: *factor of safety*, *slip surface*,
  *pore pressure*, *limit equilibrium*, *seepage*. Ni traducciones libres ni
  sinónimos de marketing.
- **Nombres**: *OpenGeoRock* es la suite; *OGR Slip2D* es el programa;
  `ogr-slip2d` es el paquete instalable. No se mezclan.
- HTML indentado a 2 espacios, atributos en minúscula, comillas dobles.
- Los comentarios `<!-- ====== SECCIÓN ====== -->` separan secciones. Son
  el índice de navegación del archivo: mantenlos.
- Enlaces externos siempre con `target="_blank" rel="noopener"`.

---

© 2026 Samuel Sáez López — UPCT
