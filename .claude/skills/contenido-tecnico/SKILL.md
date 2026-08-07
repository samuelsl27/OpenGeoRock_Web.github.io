---
name: contenido-tecnico
description: Cómo verificar y escribir las afirmaciones técnicas de la web (versión, licencia, métodos, capacidades de OGR Slip2D). Úsalo antes de tocar cualquier cifra, nombre de método o descripción de lo que el programa sabe hacer.
---

# Contenido técnico: de dónde sale cada dato

La web afirma cosas sobre un programa de ingeniería. Quien las lea puede
decidir usarlo en un proyecto real. **Ningún dato se escribe de memoria.**

## La fuente de cada dato

Todo sale del repositorio [`OGR-Slip2D`](https://github.com/samuelsl27/OGR-Slip2D):

| Dato en la web | Fuente exacta |
|---|---|
| Número de versión | `pyproject.toml` → `[project] version` |
| Licencia | `pyproject.toml` → `license`, y `LICENSE` |
| Métodos de equilibrio límite | `ogr_slip2d/methods/` y la tabla de validación del `README.md` |
| Algoritmos de búsqueda | `ogr_slip2d/search.py` y `README.md` |
| Modelos de resistencia | `ogr_core/materials/builtin_models.py` |
| Capacidades de filtración | `ogr_fem2d/solvers/seepage.py` y `README.md` |
| Número de tests | `README.md`, sección *Tests* |
| Estado de cada programa de la suite | tabla *Roadmap* del `README.md` |

Si el dato no está en ninguno de esos sitios, **no va en la web**.

## Cómo verificar antes de escribir

```bash
# desde una copia del repositorio del programa
grep '^version' pyproject.toml
grep -i 'licence\|license' pyproject.toml
ls ogr_slip2d/methods/
```

Si no tienes el repositorio a mano, dilo y **deja el dato como está**. Un
número desactualizado es un problema; un número inventado es un fallo de
integridad.

## Cosas que se han desalineado antes

Estado real en el momento de escribir esto (v0.1.59), como recordatorio de
cuánto puede derivar la web si nadie la sincroniza:

- La web dijo **GPL-3.0** durante 17 versiones después de que el proyecto
  pasara a **AGPL-3.0-or-later** (el cambio fue en v0.1.43).
- La web anunciaba **4 métodos**; hay **7**.
- La web no mencionaba la **filtración por elementos finitos**, el
  **análisis probabilístico**, el **DXF**, los **coeficientes del
  Eurocódigo 7** ni la **interfaz de línea de comandos**, todos ya
  implementados.
- La web mostraba **v0.1.6** cuando el programa iba por **v0.1.59**.

La lección: la versión y la licencia se revisan **en cada cambio**, aunque
el encargo sea otro.

## Cómo se redacta

- **Estado honesto.** El programa está en desarrollo activo y es una
  versión de prueba. Se dice: *pre-release*, *in active development*. No se
  dice *stable*, *production-ready* ni *battle-tested*.
- **Código público ≠ versión publicada.** El código es legible y clonable;
  no hay instaladores firmados. Se distingue: *source available* frente a
  *downloads · soon*.
- **Fórmulas y métodos se citan por su fuente científica original** (Bishop
  1955, Spencer 1967, Morgenstern–Price 1965, Hoek et al. 2002), nunca por
  el programa comercial que los implementa. **La web no menciona marcas de
  software de terceros.**
- **Sin superlativos de marketing.** *The best*, *revolutionary*,
  *industry-leading* no aparecen. La página convence enseñando resultados
  verificables.
- **Sin garantías.** Nada en la web puede sugerir que los resultados no
  necesitan comprobación independiente. Un proyecto lo firma una persona,
  no un programa.

## Nomenclatura

| Correcto | Incorrecto |
|---|---|
| OpenGeoRock (la suite) | OpenGeoRock Slip2D |
| OGR Slip2D (el programa) | OGR-Slip2D, Slip2D a secas en un titular |
| `ogr-slip2d` (el paquete) | ogr_slip2d en texto corrido |
| factor of safety (FoS) | safety factor, security factor |
| slip surface | failure line, rupture line |
| pore pressure | water pressure |
| limit equilibrium | equilibrium limit |
| finite-element (adjetivo) | finite elements analysis |
