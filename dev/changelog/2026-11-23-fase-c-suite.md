# 2026-11-23 — OGR FEM2D, OGR Data y OGR-Core en la web (fase C)

Tercera fase del plan `../desarrollo/notas/plan-sincronizacion-v0.1.481.md`. Cotejado con lo publicado en GitHub:
OGR FEM2D `32a34b3` (v0.0.8), OGR-Core `v0.2.3` y OGR Data `c9d383b` (v0.1.0). Al aprobar el plan, FEM2D estaba en
v0.0.6; la propietaria eligió contar la v0.0.8, ya publicada.

## Qué cambió

- **`products/fem2d.html` (nueva, EN y ES)**, con los componentes de `slip2d.html`:
  - qué es: motor de elementos finitos 2D en Rust con referencia en Python, sin interfaz, línea de órdenes, archivo
    de proyecto ni instalador; se usa desde Python, desde el árbol de código; *pre-alpha*, AGPL-3.0-or-later;
  - lo que hace la v0.0.8: T3 y T6, deformación plana y axisimetría, elástico y Mohr–Coulomb con dilatancia (solo
    T6 en deformación plana), cargas, tensión inicial, fases con excavación, Newton–Raphson; una `note warn` dice
    que aún no hay mallador general;
  - validación: 4 casos con resultado (Kirsch 1898, Salençon 1969, Lamé 1852, Michell 1902) con las cifras de cada
    `caso.md`, y el caso 5 pendiente del mallador. Fuera el «0,6 % en σ1» del caso 004, que es de otro programa;
  - hoja de ruta en el orden de `plan_de_desarrollo.md`, sin fechas; ficha técnica; 293 tests.
- **Tarjetas y menú**: FEM2D pasa de *Planned* a *In development* y enlaza a su página; OGR Data pasa a *In early
  development* con una descripción que se ciñe a lo que tiene su v0.1.0 y dice que no tiene validación propia.
  Misma etiqueta gris discontinua (`.tag.soon`), solo cambia el texto. Pie del menú y textos de la portada y de
  `products/` al día.
- **OGR-Core**: la categoría 02 de `products/` dice que FEM2D también depende de él.

## Qué se comprobó

- `python tools/sitio.py --check`: 96 páginas, 0 errores, 0 avisos.
- `traduccion.py comprobar` en las tres páginas; el español se montó con `montar`.
- Portada, `products/` y `products/fem2d.html`, en EN y ES, a 375, 768 y 1440 px: sin desbordamiento de página ni
  imágenes rotas; consola sin errores.

## Qué no

- Las cuatro fuentes de la validación de FEM2D no entran en la bibliografía: la página de producto las nombra por
  autor y año, como la de Slip2D, y el repositorio las cita a través de manuales (Jaeger, Cook y Zimmerman 2007;
  Timoshenko y Goodier 1951) sin DOI.
- No se ha tocado «a shared Python core» de la portada, `products/` y `about/` (OGR Data no usa OGR-Core y el motor de
  FEM2D es Rust): pendiente de decisión.
- Iconos de FEM2D y Data: para después.

Anomalías encontradas: `../desarrollo/notas/anomalias-programa.md`, A6 (C1–C12).
