---
description: Comprobación previa al despliegue y publicación en GitHub Pages (revisar, resumen y OK explícito antes de commit y push)
---
`git push origin main` publica en **producción**. No hay entorno de pruebas ni
vuelta atrás salvo otro commit. Antes de llegar ahí:

1. **Ejecuta `/revisar`** y resuelve todo lo de severidad alta. Lo de media y baja
   me lo cuentas.
2. **Sincronización completa y comprobación.** Con nadie más editando páginas:
   `node tools/render_math.cjs` y `python tools/sitio.py --check` **sin `--only`**
   (solo así se regeneran `sitemap.xml` y los índices de búsqueda de los dos
   idiomas). Tiene que terminar con **0 errores**; los avisos de paridad (`falta la
   versión ES/EN`) y de páginas pendientes se resuelven o me los planteas.
3. **Datos.** La versión de `tools/site.json` es la que documentan las páginas y
   coincide con el commit publicado del programa (`/sincronizar` si no).
4. **Lo que solo se ve de punta a punta**, en local y en los dos idiomas: el menú y
   el selector EN/ES, el buscador de la documentación (`/`), una pestaña de `ai/`,
   el cajón del índice de `docs/` a 1024 px o menos y `http://localhost:8000/404.html`.
   Las capturas a 375/768/1440 px y la consola ya las cubre `/revisar`.
5. **Comprobaciones de despliegue**: `CNAME` contiene exactamente `opengeorock.org`;
   existe `.nojekyll`; ningún `PENDIENTE` en las páginas
   (`grep -rn PENDIENTE --include=*.html .`).
6. **Nota en `dev/changelog/`** con la fecha, qué cambió y **qué se comprobó** (y qué
   no).
7. **Enséñame**, en este orden:
   - el resumen de lo que cambia **para un visitante**;
   - `git status` y `git diff --stat`;
   - el `git diff` completo de lo escrito a mano (CSS, JS, `tools/`, markdown) y,
     de las páginas HTML, solo el texto cambiado: el render de KaTeX y las regiones
     generadas lo hacen ilegible (a petición, el diff íntegro);
   - el mensaje de commit propuesto.

   **Espera mi OK explícito antes de hacer commit y push.** Un OK a un resumen no
   vale para un cambio posterior.
8. Si estás en una rama que no es `main` (el rediseño vive en `rediseno-v3`),
   **pregunta cómo quiero llevarla a `main`** —fusión, o `git push origin
   <rama>:main`—. No lo decidas tú.
9. **Tras el push**: Pages redespliega solo. Comprueba en https://opengeorock.org
   la portada, `/es/`, una página de documentación con ecuaciones, `/sitemap.xml` y
   una ruta que no exista (tiene que salir la 404 de la web). Si algo falla, dímelo
   enseguida.

Mensaje de commit: una línea en imperativo describiendo el cambio visible para un
visitante, no el archivo tocado. *«Add the MCP installation guide for eight
clients»*, no *«edit ai/index.html»*.

Si algo de los pasos 1 a 5 falla, **para y dime qué falla**. No publiques a medias.
