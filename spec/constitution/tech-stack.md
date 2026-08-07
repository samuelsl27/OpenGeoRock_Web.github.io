# Stack y convenciones

## Tecnología

| Pieza | Decisión | Por qué |
|---|---|---|
| Formato | HTML5 estático, un solo `index.html` | Se abre con doble clic. Sin build no hay build que se rompa |
| CSS | En línea, en un `<style>` del `<head>` | Una sola petición, cero FOUC, cero archivos que se desincronicen |
| JavaScript | **Ninguno** propio | Nada que mantener, nada que falle, nada que bloquear |
| Tipografías | Inter · Newsreader · JetBrains Mono (Google Fonts) | Única dependencia externa, y es consciente |
| Alojamiento | GitHub Pages desde `main` | Gratis, versionado, sin servidor que administrar |
| Dominio | `opengeorock.org` vía `CNAME` | — |

**Sin gestor de paquetes, sin bundler, sin framework, sin preprocesador.**
No es una limitación temporal: es la decisión. Una web de proyecto que
necesita `npm install` para cambiar una coma se queda sin actualizar.

## Idiomas

- **La web, en inglés.** Su público es internacional.
- **El repositorio, en castellano**: `AGENTS.md`, `spec/`, `docs/`,
  comandos y skills. Quien mantiene esto piensa en castellano.

## Fuente de verdad

Los datos técnicos **no viven aquí**. Viven en
[`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D):

- `pyproject.toml` → versión y licencia
- `README.md` → métodos, capacidades, número de tests, hoja de ruta
- `docs/changelog/` → qué cambió y cuándo

Esta web es una **vista** de ese repositorio. El comando `/sincronizar`
existe para mantener la vista al día.

## Convenciones de código

- Indentación de 2 espacios. Atributos en minúscula, comillas dobles.
- Comentarios `<!-- ====== SECCIÓN ====== -->` como índice del archivo.
- Variables CSS siempre por nombre (`var(--ink)`), nunca el literal.
- Iconos: SVG en línea, `viewBox="0 0 24 24"`, `stroke-width` 1.6–2.
- Enlaces externos: `target="_blank" rel="noopener"`.
- Imágenes: `alt` descriptivo, `loading="lazy"` salvo sobre el pliegue,
  **máximo 300 KB**.

## Presupuestos

| Métrica | Objetivo |
|---|---|
| Peso de la página (sin imágenes) | < 60 KB |
| Peso de cualquier imagen | < 300 KB |
| Peticiones a terceros | solo Google Fonts |
| Puntos de ruptura | los 7 que ya existen; ninguno nuevo |
