---
description: Revisión de los cambios pendientes contra las seis reglas del proyecto
---
Eres un revisor senior de este sitio. Sobre los cambios pendientes
(`git diff` y `git status`):

1. Lista los archivos tocados.
2. Comprueba las **seis reglas de AGENTS.md**, una por una:
   - **Estética**: ¿hay algún cambio en el `<style>`, en tokens, tipografías,
     espaciado o layout que yo no haya aprobado explícitamente?
   - **Datos técnicos**: ¿cada cifra, versión, licencia y capacidad nueva
     tiene respaldo en el repositorio `OGR-Slip2D`?
   - **Enlaces**: ¿resuelve cada `href`? ¿queda algún `/cdn-cgi/`, algún
     `mailto:` ofuscado, o algún enlace vivo a algo aún no publicado?
   - **Navegación**: ¿toda sección nueva o renombrada está en `nav.primary`
     y en el pie?
   - **Responsive**: ¿el marcado nuevo aguanta a 375 px? ¿respeta el número
     de columnas de su rejilla (4 en `.stats` y `.specs`, 3 en `.channels`)?
   - **Imágenes**: ¿alguna supera 300 KB? ¿todas tienen `alt` útil y
     `loading` correcto?
3. Busca además: encabezados que salten de nivel, `<div>` clicables,
   enlaces externos sin `rel="noopener"`, SVG decorativos sin
   `aria-hidden`, y peticiones a dominios de terceros nuevos.

Devuelve markdown con severidad **alta / media / baja** y, en cada punto,
la línea concreta. Si una regla está limpia, **dilo explícitamente** en
lugar de omitirla.
