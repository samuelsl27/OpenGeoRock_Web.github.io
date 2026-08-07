# opengeorock.org

Sitio público de la suite **OpenGeoRock**. Una sola página estática,
desplegada en GitHub Pages sobre el dominio `opengeorock.org`.

El programa vive en otro sitio: **[OGR-Slip2D](https://github.com/samuelsl27/OGR-Slip2D)**.
Este repositorio solo contiene la web.

## Trabajar en local

No hay build ni dependencias.

```bash
python -m http.server 8000     # → http://localhost:8000
```

También sirve abrir `index.html` con doble clic, aunque las rutas relativas
se comportan mejor con el servidor.

## Publicar

```bash
git push origin main
```

GitHub Pages redespliega solo. **No hay entorno de pruebas**: lo que se
sube a `main` es producción.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html` | La página entera: CSS en línea + secciones |
| `assets/` | Capturas, fotos y logotipos |
| `CNAME` | Dominio propio. No tocar |
| `AGENTS.md` | Contrato de trabajo para agentes de IA |
| `.claude/` | Comandos y skills del agente |
| `spec/` | Constitución del proyecto y plantilla de features |
| `docs/` | Mapa de `index.html` y changelog |

## Si desarrollas con IA

Lee **[`AGENTS.md`](AGENTS.md)** primero. Resume las seis reglas, el flujo
y lo que no se debe hacer. La más importante:

> **La estética no se cambia sin permiso explícito.** Texto, datos y
> enlaces, libremente. Colores, tipografías, espaciados y layout, solo con
> el OK del responsable.

La segunda, casi igual de importante: **ningún dato técnico se escribe de
memoria**. Versión, licencia, métodos y capacidades salen del repositorio
del programa. El comando `/sincronizar` hace justo eso.

Comandos disponibles: `/sincronizar`, `/revisar`, `/publicar`, `/seccion`.

## Licencia

El contenido de la web (textos e imágenes) es © 2026 Samuel Sáez López.
El programa que documenta se publica bajo **AGPL-3.0-or-later**.
