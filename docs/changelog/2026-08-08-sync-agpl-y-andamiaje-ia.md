# 2026-08-08 — Sincronización con OGR-Slip2D v0.1.59 y andamiaje para IA

Primera sincronización de la web con el repositorio del programa desde que
este se hizo público. La web iba **53 versiones y un cambio de licencia**
por detrás.

## Lo que se encontró

El desfase era mayor de lo esperado, y en la dirección peligrosa: la web
prometía menos y afirmaba mal.

| Dato | Decía | Es |
|---|---|---|
| Licencia | GPL-3.0 | **AGPL-3.0-or-later** (cambió en v0.1.43) |
| Versión | v0.1.6 | **v0.1.59** |
| Código | «downloads soon», sin enlace al repositorio | **público en GitHub** |
| Métodos LEM | 4 | **7** |
| Filtración FE, probabilístico, DXF, Eurocódigo 7, CLI, ES/EN | no se mencionaban | implementados |

**Un fallo funcional aparte**: los tres enlaces de correo eran
`/cdn-cgi/l/email-protection` con el correo ofuscado por Cloudflare,
heredados de guardar una página ya desplegada. En GitHub Pages **daban
404**: el script que los descifra no existe ahí. Llevaban rotos desde el
despliegue. Sustituidos por `mailto:` planos y eliminado el `<script>` de
Cloudflare, que también daba 404.

## Lo que se cambió

**Datos** — licencia, versión y estado en los seis sitios donde aparecen
(hero, `.stats`, `#project`, `.specs`, tarjeta de autoría, pie), más el
`<meta name="description">` y un `<link rel="canonical">`.

**Capacidades** — `.sw-sub` reescrito y la ficha `.specs` ampliada de 7 a
12 filas: métodos, superficies, modelos de resistencia, filtración,
cargas, probabilístico, Eurocódigo 7, interoperabilidad y suite de tests.
Doce mantiene la rejilla de 4 columnas en 3 filas exactas.

**Código público** — botón *Source on GitHub* en el hero, canal 01
(*Read the code*) y canal 02 (*Issues & validation cases*, que sustituye al
foro bloqueado) en `#contribute`, enlace en la tarjeta de Samuel, y columna
*Resources* del pie con README, changelog, CONTRIBUTING y LICENSE.

**Nota de licencia** — la tarjeta de autoría explica ahora el paso de GPL a
AGPL y por qué, en lugar de solo nombrar la licencia vigente.

**Sin cambios en el `<style>`.** Ni un token, ni una tipografía, ni un
espaciado. Todo el trabajo es contenido dentro de componentes existentes.

## Andamiaje para desarrollo con IA

Nuevo: `AGENTS.md` (seis reglas, la primera es que la estética no se toca
sin permiso), `CLAUDE.md`, `.claude/` con cuatro comandos
(`/sincronizar`, `/revisar`, `/publicar`, `/seccion`) y tres skills
(`diseno-web`, `contenido-tecnico`, `html-estatico`), `.mcp.json` con
Context7, `spec/` con la constitución y la plantilla de feature, y
`docs/estructura-web.md` como mapa del archivo único.

La skill `diseno-web` congela los tokens y el catálogo de componentes: es
lo que impide que un agente "mejore" la paleta por su cuenta.

## Qué se comprobó

- Búsqueda de `GPL-3.0`, `v0.1.6`, `cdn-cgi` y `__cf_email__`: solo queda
  la mención histórica intencionada a GPL en la tarjeta de autoría.
- Página servida en local, revisada a 375 px y 1440 px, sin errores en
  consola y sin scroll horizontal.
- Los cinco anclas del menú resuelven.

## Qué queda por hacer

- `assets/people/samuel.jpg` pesa **4,3 MB** y se muestra a ~500 px;
  `assets/logos/imga.png` pesa **1,0 MB**. Es la deuda más cara de la
  página y el primer punto de `spec/constitution/roadmap.md`.
- No hay favicon ni `og:image`.
- El canal de contacto directo por correo salió de `#contribute` al entrar
  el de código; sigue en la tarjeta del equipo y en el pie. Decidir si se
  quiere recuperar.
