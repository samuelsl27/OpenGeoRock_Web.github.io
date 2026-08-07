# Hoja de ruta de la web

Orden previsto. Cada punto se implementa por el flujo de
`spec/features/NNN-nombre/` y se aprueba antes de tocar `index.html`.

## Deuda pendiente (lo primero)

1. **Optimizar `assets/people/samuel.jpg` (4,3 MB) y
   `assets/logos/imga.png` (1,0 MB).** Es el mayor problema medible de la
   página. Sin cambio visual: mismo encuadre, mismo recorte.
2. **Favicon.** Hoy no hay ninguno: la pestaña sale con el icono genérico.
3. **`og:image` y metadatos sociales.** Compartir el enlace en LinkedIn o
   Slack no muestra previsualización, y este proyecto se difunde justo por
   ahí.

## Contenido

4. **Página o sección de descargas**, cuando existan instaladores firmados.
   Hoy el botón está en `.locked` a propósito.
5. **Enlace a la documentación**, cuando haya algo más que el `README`.
6. **Sección de validación**: la tabla de casos de referencia del programa
   es el argumento más fuerte que tiene el proyecto y no aparece en la web.
7. **Publicaciones y citas**, según avance la tesis.

## Mantenimiento continuo

- Ejecutar `/sincronizar` **en cada versión menor** del programa. La web
  llegó a estar 53 versiones y un cambio de licencia por detrás.
- Revisar la hoja de ruta de la suite cuando cambie el estado de algún
  programa.

## Decidido que NO se hace

- Blog o sección de noticias. Nadie va a alimentarlo, y un blog muerto
  envejece peor que su ausencia.
- Multiidioma en la web. El público es internacional; el inglés basta.
- Formulario de contacto. El `mailto:` funciona y no necesita backend.
- Modo oscuro.
