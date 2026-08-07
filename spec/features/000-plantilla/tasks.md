# Tareas — [NNN] Nombre de la feature

Pasos pequeños y verificables. Uno a uno, sin adelantar.

## Preparación

- [ ] `spec.md` y `plan.md` aprobados
- [ ] Datos técnicos verificados contra `OGR-Slip2D` (skill `contenido-tecnico`)
- [ ] Si toca el `<style>`: **OK explícito recibido**

## Implementación

- [ ] Marcado en `index.html`, bajo su comentario de sección
- [ ] Enlaces con `target="_blank" rel="noopener"` donde corresponda
- [ ] Assets optimizados y colocados en `assets/`
- [ ] Si es sección nueva: `id` + `nav.primary` + pie

## Verificación

- [ ] `python -m http.server 8000` y revisión en el navegador
- [ ] Sin errores en la consola
- [ ] 375 px y 1440 px, sin scroll horizontal
- [ ] Todos los enlaces resuelven (incluidos anclas y `mailto:`)
- [ ] Cada criterio de aceptación de `spec.md`, marcado uno a uno

## Cierre

- [ ] `/revisar` sin hallazgos de severidad alta
- [ ] Nota en `docs/changelog/`
- [ ] `docs/estructura-web.md` actualizado si cambió la estructura
- [ ] `/publicar`
