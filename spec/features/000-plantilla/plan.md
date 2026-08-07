# Plan — [NNN] Nombre de la feature

**Cómo** se construye lo que describe `spec.md`.

## Dónde va

- Sección: [`#software`, nueva sección entre X e Y, ...]
- Marca de referencia en `index.html`: `<!-- ====== ... ====== -->`
- Ver `docs/estructura-web.md` antes de decidir.

## Componentes que se reutilizan

| Componente | Para qué | ¿Sirve tal cual? |
|---|---|---|
| [`.specs > .row`] | [...] | [sí / no, y por qué] |

Consulta `.claude/skills/diseno-web/SKILL.md`. Reutilizar es la vía por
defecto; crear es la excepción que hay que justificar.

## Componentes nuevos

[Ninguno, idealmente. Si hay alguno: descríbelo, di por qué ninguno de los
existentes sirve, y **espera el OK antes de implementarlo**.]

## Rejillas afectadas

[`.stats` y `.specs` son de 4 columnas; `.channels`, de 3. Si añades
elementos, di cuántos quedan en total y si el número sigue siendo múltiplo.]

## Assets nuevos

| Archivo | Origen | Tamaño servido | Peso tras optimizar |
|---|---|---|---|
| [...] | [...] | [p. ej. 620 px de ancho] | [< 300 KB] |

## Riesgos

- [Qué puede romper. Puntos de ruptura, longitud del texto en móvil,
  contraste sobre fondo tinta...]
