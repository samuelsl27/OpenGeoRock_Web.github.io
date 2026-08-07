---
description: Comprobación previa al despliegue y publicación en GitHub Pages
---
`git push origin main` publica en **producción**. Antes de llegar ahí:

1. Ejecuta `/revisar` y resuelve todo lo de severidad alta.
2. Levanta `python -m http.server 8000` y comprueba en el navegador:
   - la página carga sin errores en consola;
   - los cinco anclas del menú (`#project`, `#software`, `#suite`, `#team`,
     `#contribute`) llevan a su sección;
   - se ve correctamente a **375 px** y a **1440 px**, sin scroll
     horizontal;
   - las imágenes cargan y ninguna aparece recortada o deformada.
3. Verifica que `CNAME` sigue conteniendo exactamente `opengeorock.org`.
4. Añade una nota en `docs/changelog/` con la fecha, qué cambió y **qué se
   comprobó**.
5. Enséñame el `git diff` completo y el mensaje de commit propuesto.
   **Espera mi OK antes de hacer commit y push.**

Mensaje de commit: una línea en imperativo describiendo el cambio visible
para un visitante, no el archivo tocado. *«Update licence to AGPL-3.0 and
sync Slip2D capabilities»*, no *«edit index.html»*.

Si algo del paso 2 falla, **para y dime qué falla**. No publiques a medias.
