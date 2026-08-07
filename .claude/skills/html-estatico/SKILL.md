---
name: html-estatico
description: Reglas del HTML estático de este sitio — accesibilidad, rendimiento, imágenes, enlaces y despliegue en GitHub Pages. Úsalo al añadir marcado, imágenes o enlaces, y antes de publicar.
---

# HTML estático en GitHub Pages

Sin build, sin JavaScript de aplicación. Lo que hay en el repositorio es
literalmente lo que se sirve. Eso simplifica mucho y castiga tres cosas.

## 1. GitHub Pages no ejecuta nada del servidor

- **No hay reescrituras ni redirecciones.** Un `href` a una ruta que no es
  un archivo del repositorio da 404.
- **Nada de Cloudflare Email Protection.** Si copias marcado desde una
  página ya desplegada tras Cloudflare, traerás enlaces
  `/cdn-cgi/l/email-protection` y `<span class="__cf_email__">`. Aquí **no
  funcionan**: el script que los descifra no existe. Los correos van en
  `mailto:` planos. Ya pasó una vez.
- **`CNAME` no se toca.** Contiene `opengeorock.org`. Borrarlo o cambiarlo
  tira el dominio hasta que alguien lo restaure a mano.

## 2. Las imágenes son el único coste real de la página

No hay optimización automática. El navegador descarga el archivo tal cual.

Antes de añadir una imagen:

1. Redimensiónala al tamaño en que se muestra (×2 como mucho, para pantallas
   de alta densidad).
2. WebP, o JPEG de calidad 80.
3. **Presupuesto: 300 KB.** Si te lo saltas, di por qué.
4. `loading="lazy"` salvo que esté sobre el pliegue, donde va
   `loading="eager"`.
5. `alt` que describa **lo que la imagen aporta**, no lo que es. Mal:
   `alt="captura"`. Bien: `alt="Grid search over a two-layer slope: the
   critical surface in red among candidates in green"`.

Las capturas del programa llevan `object-fit: contain` sobre fondo blanco y
un `aspect-ratio` que coincide con el de la imagen original, para que no se
recorten ni se deformen.

## 3. Accesibilidad: lo mínimo que hay que respetar

- Un solo `<h1>` (el del hero). Las secciones usan `<h2>`. No saltes niveles
  por razones de tamaño: el tamaño lo pone el CSS.
- Todo elemento interactivo es `<a>` o `<button>`. Un `<div>` clicable no
  llega por teclado. Lo no disponible se marca con `aria-disabled="true"` y
  un `title` que explique cuándo llegará.
- Los SVG decorativos llevan `aria-hidden="true"`; los informativos, un
  `<title>` dentro.
- Contraste: `--mute` (#6b6660) sobre `--paper` (#f5f1ea) ronda 4.6:1 —
  vale para texto normal, **no** para texto por debajo de 12 px que además
  sea información esencial. Las etiquetas mono de 10.5 px son metadatos
  repetidos en otro sitio; no metas ahí contenido único.
- Todo enlace externo: `target="_blank" rel="noopener"`.

## 4. Antes de publicar

```bash
python -m http.server 8000     # abre http://localhost:8000
git diff                        # lee lo que vas a subir
```

Lista de comprobación:

- [ ] La página carga sin errores en la consola.
- [ ] Ningún enlace da 404 (incluidos los `mailto:` y los anclas `#seccion`).
- [ ] Se ve bien a **375 px** y a **1440 px**, sin scroll horizontal.
- [ ] Versión y licencia coinciden con el repositorio del programa
      (ver la skill `contenido-tecnico`).
- [ ] Las imágenes nuevas pesan menos de 300 KB y tienen `alt`.
- [ ] Los anclas nuevos están en `nav.primary` y en el pie.

`git push origin main` publica en producción. No hay vuelta atrás salvo
otro commit.
