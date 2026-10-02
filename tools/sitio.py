#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sitio.py — mantenimiento de opengeorock.org, sin dependencias.

    python tools/sitio.py            sincroniza y regenera
    python tools/sitio.py --check    sincroniza y además comprueba

Qué hace (idempotente, se puede lanzar cuantas veces se quiera):

* Sustituye en cada página las regiones marcadas ``<!-- @inc X -->`` …
  ``<!-- @end X -->`` por los parciales de ``tools/partials/`` (cabecera, pie,
  cabeza del documento, índice lateral de la documentación…), con las rutas
  relativas correctas para la profundidad de la página y su idioma.
* Pone el idioma y la raíz relativa en ``<html>``, el selector EN/ES, los
  ``hreflang`` y la entrada activa del menú.
* En la documentación: numera secciones (h2), ecuaciones (``div.eq``),
  figuras (``figure.fig``) y tablas (``figure.tbl``) con el número del
  capítulo, rellena las referencias cruzadas ``a.xref``, genera «en esta
  página», anterior/siguiente y la portada de grupos.
* Rellena ``<span data-v></span>`` con la versión vigente del programa.
* Genera el índice de búsqueda (``assets/js/search-index.{en,es}.js``) y
  ``sitemap.xml``.

Con ``--check`` además: enlaces y anclas rotos, paridad EN/ES, imágenes de
más de 300 KB, ``<img>`` sin ``alt``, ecuaciones sin renderizar
(``node tools/render_math.cjs``) y marcadores ``{{…}}`` olvidados.

La estructura de la documentación (capítulos, títulos EN/ES y orden) vive en
``tools/site.json``: añadir una página es añadirla allí y crear el archivo.
"""
from __future__ import annotations

import argparse
import html as htmlmod
import json
import posixpath
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
PARTIALS = TOOLS / "partials"
CFG = json.loads((TOOLS / "site.json").read_text(encoding="utf-8"))
BASE = CFG["base_url"]
VERSION = CFG["version"]

EXCLUDE_TOP = {".git", ".claude", ".vscode", "tools", "spec", "dev", "node_modules", "assets"}
IMG_BUDGET = 300 * 1024

L = {
    "en": {
        "docs": "Documentation", "fig": "Figure", "tbl": "Table", "eq": "Eq.", "sec": "Section",
        "prev": "Previous", "next": "Next", "on_page": "On this page", "print": "Print this page",
        "edit": "Edit this page", "issue": "Report a problem", "describes": "Describes OGR Slip2D",
        "docs_home": "Documentation home", "contents": "Contents", "search": "Search the documentation",
        "anchor": "Link to this section", "lang": "Language", "chapter": "Chapter",
        "crumbs": "Breadcrumb", "pager": "Pages",
    },
    "es": {
        "docs": "Documentación", "fig": "Figura", "tbl": "Tabla", "eq": "Ec.", "sec": "Sección",
        "prev": "Anterior", "next": "Siguiente", "on_page": "En esta página", "print": "Imprimir esta página",
        "edit": "Editar esta página", "issue": "Informar de un problema", "describes": "Válido para OGR Slip2D",
        "docs_home": "Portada de la documentación", "contents": "Contenido", "search": "Buscar en la documentación",
        "anchor": "Enlace a esta sección", "lang": "Idioma", "chapter": "Capítulo",
        "crumbs": "Ruta de navegación", "pager": "Páginas",
    },
}

ICON = {
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 016.5 3H20v15H6.5A2.5 2.5 0 004 20.5z"/><path d="M4 20.5A2.5 2.5 0 016.5 18H20v3H6.5A2.5 2.5 0 014 20.5z"/></svg>',
    "list": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>',
    "print": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="1.5"/><path d="M6 14h12v7H6z"/></svg>',
}

# ---------------------------------------------------------------------------
# rutas


def all_pages() -> list[str]:
    out = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT).as_posix()
        parts = rel.split("/")
        if parts[0] in EXCLUDE_TOP or any(x.startswith("_") for x in parts):
            continue
        out.append(rel)
    return sorted(out)


def lang_of(rel: str) -> str:
    return "es" if rel.startswith("es/") else "en"


def base_rel(rel: str) -> str:
    return rel[3:] if rel.startswith("es/") else rel


def root_of(rel: str) -> str:
    # GitHub Pages sirve 404.html en cualquier ruta inexistente, a cualquier
    # profundidad: sus enlaces tienen que ser absolutos desde la raíz.
    if base_rel(rel) == "404.html":
        return "/"
    return "../" * rel.count("/")


def localized(base: str, lang: str) -> str:
    return ("es/" + base) if lang == "es" else base


def pretty(rel: str) -> str:
    return rel[: -len("index.html")] if rel.endswith("index.html") else rel


def nav_key(rel: str) -> str | None:
    b = base_rel(rel)
    for prefix, key in CFG["nav_sections"].items():
        if b.startswith(prefix):
            return key
    return None


# ---------------------------------------------------------------------------
# documentación: índice plano

DOC_PAGES: list[dict] = []
for _g in CFG["docs"]:
    for _p in _g["pages"]:
        DOC_PAGES.append({**_p, "group": _g, "rel": f"docs/{_g['dir']}/{_p['slug']}.html"})
DOC_BY_REL = {d["rel"]: d for d in DOC_PAGES}


# ---------------------------------------------------------------------------
# utilidades HTML


def region(text: str, name: str, content: str) -> str:
    pat = re.compile(r"(<!-- @inc %s -->)(.*?)(<!-- @end %s -->)" % (re.escape(name), re.escape(name)), re.S)
    return pat.sub(lambda m: m.group(1) + "\n" + content.strip("\n") + "\n" + m.group(3), text)


def has_region(text: str, name: str) -> bool:
    return f"<!-- @inc {name} -->" in text


def strip_tags(s: str) -> str:
    s = re.sub(r"<!--k-->.*?<!--/k-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", strip_tags(s)).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "section"


def attr(tag: str, name: str) -> str | None:
    m = re.search(r'\s%s="([^"]*)"' % re.escape(name), tag)
    return m.group(1) if m else None


def set_attr(tag: str, name: str, value: str) -> str:
    if attr(tag, name) is not None:
        return re.sub(r'(\s%s=")[^"]*(")' % re.escape(name), lambda m: m.group(1) + value + m.group(2), tag, count=1)
    return tag[:-1] + f' {name}="{value}">' if tag.endswith(">") else tag


def partial(name: str, lang: str) -> str:
    for cand in (PARTIALS / f"{name}.{lang}.html", PARTIALS / f"{name}.html"):
        if cand.exists():
            return cand.read_text(encoding="utf-8")
    raise FileNotFoundError(f"falta el parcial {name} ({lang})")


def fill(tpl: str, ctx: dict) -> str:
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(ctx.get(m.group(1), m.group(0))), tpl)


def title_of(text: str) -> str:
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    return htmlmod.unescape(m.group(1).strip()) if m else ""


def desc_of(text: str) -> str:
    m = re.search(r'<meta name="description" content="([^"]*)"', text)
    return htmlmod.unescape(m.group(1)) if m else ""


# ---------------------------------------------------------------------------
# parciales comunes


def lang_switch(rel: str) -> str:
    lang, root, b = lang_of(rel), root_of(rel), base_rel(rel)
    cur = ' aria-current="true"'
    return (
        f'<span class="lang" role="group" aria-label="{L[lang]["lang"]}">'
        f'<a href="{root}{b}" hreflang="en" lang="en"{cur if lang == "en" else ""}>EN</a>'
        f'<a href="{root}es/{b}" hreflang="es" lang="es"{cur if lang == "es" else ""}>ES</a></span>'
    )


def head_html(rel: str, text: str) -> str:
    lang, root, b = lang_of(rel), root_of(rel), base_rel(rel)
    alts = (
        f'<link rel="alternate" hreflang="en" href="{BASE}{pretty(b)}">\n'
        f'<link rel="alternate" hreflang="es" href="{BASE}{pretty("es/" + b)}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{BASE}{pretty(b)}">'
    )
    extra = []
    if b.startswith("docs/"):
        extra.append(f'<link rel="stylesheet" href="{root}assets/css/docs.css">')
    if "data-tex=" in text:
        extra.append(f'<link rel="stylesheet" href="{root}assets/vendor/katex/katex.min.css">')
    ctx = {
        "root": root, "base": BASE, "canonical": BASE + pretty(rel), "alternates": alts,
        "og_title": htmlmod.escape(title_of(text), quote=True), "og_desc": htmlmod.escape(desc_of(text), quote=True),
        "og_locale": "es_ES" if lang == "es" else "en_GB", "extra_css": "\n".join(extra), "version": VERSION,
    }
    return fill(partial("head", lang), ctx)


def header_html(rel: str) -> str:
    lang, root = lang_of(rel), root_of(rel)
    h = fill(partial("header", lang), {"root": root, "lroot": root + ("es/" if lang == "es" else ""),
                                       "lang_switch": lang_switch(rel), "version": VERSION})
    key = nav_key(rel)
    if key:
        h = re.sub(r'(<a [^>]*data-nav="%s")' % key, r'\1 aria-current="page"', h)
        h = h.replace(f'<div class="has-menu" data-nav="{key}"', f'<div class="has-menu current" data-nav="{key}"')
    return h


def footer_html(rel: str) -> str:
    lang, root = lang_of(rel), root_of(rel)
    return fill(partial("footer", lang), {"root": root, "lroot": root + ("es/" if lang == "es" else ""),
                                          "lang_switch": lang_switch(rel), "version": VERSION,
                                          "version_date": CFG["version_date"]})


# ---------------------------------------------------------------------------
# documentación


def doc_link(root: str, lang: str, d: dict) -> str:
    return root + localized(d["rel"], lang)


def docnav_html(rel: str) -> str:
    lang, root, b = lang_of(rel), root_of(rel), base_rel(rel)
    t = L[lang]
    out = [
        '<div class="doc-search">' + ICON["search"]
        + f'<input type="search" placeholder="{t["search"]}  /" aria-label="{t["search"]}" autocomplete="off">'
        + '<div class="results" role="listbox"></div></div>',
        f'<nav class="doc-nav" aria-label="{t["docs"]}">',
        f'<a class="home" href="{root}{localized("docs/index.html", lang)}">{ICON["book"]} {t["docs_home"]}</a>',
    ]
    for g in CFG["docs"]:
        out.append(f'<details open><summary>{g["n"]} · {g[lang]}</summary><ul>')
        for p in g["pages"]:
            d = DOC_BY_REL[f"docs/{g['dir']}/{p['slug']}.html"]
            cur = ' aria-current="page"' if d["rel"] == b else ""
            out.append(f'<li><a href="{doc_link(root, lang, d)}"{cur}><span class="n">{p["n"]}</span><span>{p[lang]}</span></a></li>')
        out.append("</ul></details>")
    out.append("</nav>")
    return "\n".join(out)


def dochead_html(rel: str) -> str:
    lang, root, b = lang_of(rel), root_of(rel), base_rel(rel)
    d, t = DOC_BY_REL[b], L[lang]
    g = d["group"]
    return (
        f'<button class="doc-side-toggle" type="button" aria-controls="doc-side" aria-expanded="false">{ICON["list"]} {t["contents"]}</button>\n'
        f'<nav class="crumbs label" aria-label="{t["crumbs"]}"><a href="{root}{localized("docs/index.html", lang)}">{t["docs"]}</a>'
        f'<span aria-hidden="true">/</span><span>{g["n"]} · {g[lang]}</span></nav>\n'
        f'<div class="chapter label">{d["n"]}</div>\n'
        f'<h1>{d[lang]}</h1>\n'
        f'<div class="meta label"><span>{t["describes"]} <span data-v>{VERSION}</span></span></div>'
    )


def docfoot_html(rel: str) -> str:
    lang, root, b = lang_of(rel), root_of(rel), base_rel(rel)
    t = L[lang]
    i = next(k for k, d in enumerate(DOC_PAGES) if d["rel"] == b)
    parts = [f'<nav class="doc-pager" aria-label="{t["pager"]}">']
    if i > 0:
        p = DOC_PAGES[i - 1]
        parts.append(f'<a class="prev" href="{doc_link(root, lang, p)}"><span class="label">← {t["prev"]} · {p["n"]}</span><b>{p[lang]}</b></a>')
    if i < len(DOC_PAGES) - 1:
        n = DOC_PAGES[i + 1]
        parts.append(f'<a class="next" href="{doc_link(root, lang, n)}"><span class="label">{n["n"]} · {t["next"]} →</span><b>{n[lang]}</b></a>')
    parts.append("</nav>")
    parts.append(
        f'<div class="doc-edit label"><a href="{CFG["repo_web"]}/blob/main/{rel}" target="_blank" rel="noopener">{t["edit"]} ↗</a>'
        f'<a href="{CFG["repo_program"]}/issues" target="_blank" rel="noopener">{t["issue"]} ↗</a></div>'
    )
    return "\n".join(parts)


def docgroups_html(rel: str) -> str:
    lang, root = lang_of(rel), root_of(rel)
    out = ['<div class="groups">']
    for g in CFG["docs"]:
        out.append(f'<section class="group" id="g-{g["dir"]}"><h3><span class="n">{g["n"]}</span>{g[lang]}</h3>')
        out.append(f'<p>{g.get("d_" + lang, "")}</p><ul>')
        for p in g["pages"]:
            d = DOC_BY_REL[f"docs/{g['dir']}/{p['slug']}.html"]
            out.append(f'<li><a href="{doc_link(root, lang, d)}"><span class="n">{p["n"]}</span><span>{p[lang]}</span></a></li>')
        out.append("</ul></section>")
    out.append("</div>")
    return "\n".join(out)


ARTICLE_RE = re.compile(r'(<article class="doc[^"]*"[^>]*>)(.*?)(</article>)', re.S)


def number_article(body: str, num: str, lang: str):
    """Numera h2, ecuaciones, figuras y tablas. Devuelve (html, etiquetas, índice)."""
    labels: dict[str, tuple[str, str]] = {}
    toc: list[tuple[str, str, str]] = []
    t = L[lang]
    counters = {"sec": 0, "eq": 0, "fig": 0, "tbl": 0}

    def heading(m):
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        inner = re.sub(r'<span class="secnum">.*?</span>\s*', "", inner, flags=re.S)
        inner = re.sub(r'\s*<a class="anchor"[^>]*>.*?</a>', "", inner, flags=re.S).strip()
        wrapped = re.fullmatch(r'<span class="ht">(.*)</span>', inner, flags=re.S)
        if wrapped:
            inner = wrapped.group(1).strip()
        hid = attr("<x" + attrs + ">", "id")
        if not hid:
            hid = slugify(inner)
            attrs += f' id="{hid}"'
        text = strip_tags(inner)
        num_html = ""
        if level == "2":
            counters["sec"] += 1
            sn = f"{num}.{counters['sec']}"
            labels[hid] = ("sec", sn)
            toc.append(("h2", hid, f"{sn} {text}"))
            num_html = f'<span class="secnum">{sn}</span>'
        else:
            toc.append(("h3", hid, text))
        anchor = f'<a class="anchor" href="#{hid}" aria-label="{t["anchor"]}">#</a>'
        return f'<h{level}{attrs}>{num_html}<span class="ht">{inner}</span>{anchor}</h{level}>'

    body = re.sub(r"<h([23])((?:\s[^>]*)?)>(.*?)</h\1>", heading, body, flags=re.S)

    def classes(tag: str) -> set[str]:
        return set((attr(tag, "class") or "").split())

    def eq(m):
        tag = m.group(0)
        if "eq" not in classes(tag):
            return tag
        counters["eq"] += 1
        n = f"{num}.{counters['eq']}"
        eid = attr(tag, "id")
        if eid:
            labels[eid] = ("eq", n)
        return set_attr(tag, "data-n", n)

    body = re.sub(r"<div\b[^>]*>", eq, body)

    def fig(m):
        whole = m.group(0)
        open_tag = whole.split(">", 1)[0] + ">"
        cls = classes(open_tag)
        if not cls & {"fig", "tbl"}:
            return whole
        kind = "tbl" if "tbl" in cls else "fig"
        counters[kind] += 1
        n = f"{num}.{counters[kind]}"
        fid = attr(open_tag, "id")
        if fid:
            labels[fid] = (kind, n)
        word = t[kind]

        def cap(cm):
            inner = re.sub(r'<span class="fignum">.*?</span>\s*', "", cm.group(2), flags=re.S)
            return f'{cm.group(1)}<span class="fignum">{word} {n}</span> {inner.strip()}</figcaption>'

        return re.sub(r"(<figcaption[^>]*>)(.*?)</figcaption>", cap, whole, count=1, flags=re.S)

    body = re.sub(r"<figure\b[^>]*>.*?</figure>", fig, body, flags=re.S)
    return body, labels, toc


def pagetoc_html(rel: str, toc) -> str:
    t = L[lang_of(rel)]
    items = "".join(f'<li class="{lv}"><a href="#{i}">{htmlmod.escape(x)}</a></li>' for lv, i, x in toc)
    return (f'<span class="label">{t["on_page"]}</span><ul>{items}</ul>'
            f'<button class="print" type="button">{ICON["print"]} {t["print"]}</button>')


def fill_xrefs(rel: str, text: str, all_labels: dict) -> tuple[str, list[str]]:
    lang = lang_of(rel)
    t = L[lang]
    problems = []

    def rep(m):
        tag, inner = m.group(1), m.group(2)
        if attr(tag, "data-keep") is not None:
            return m.group(0)
        href = attr(tag, "href") or ""
        path, _, frag = href.partition("#")
        target = rel if not path else posixpath.normpath(posixpath.join(posixpath.dirname(rel), path))
        lab = None
        if frag:
            lab = all_labels.get(target, {}).get(frag)
        elif base_rel(target) in DOC_BY_REL:
            lab = ("page", DOC_BY_REL[base_rel(target)]["n"])
        if not lab:
            problems.append(f"{rel}: referencia cruzada sin destino numerado: {href}")
            return m.group(0)
        kind, n = lab
        label = {"eq": f"{t['eq']} ({n})", "fig": f"{t['fig']} {n}", "tbl": f"{t['tbl']} {n}",
                 "sec": f"{t['sec']} {n}", "page": f"{t['sec']} {n}"}[kind]
        return f"{tag}{label}</a>"

    text = re.sub(r'(<a class="xref"[^>]*>)(.*?)</a>', rep, text, flags=re.S)
    return text, problems


# ---------------------------------------------------------------------------
# índice de búsqueda y sitemap


def search_entries(rel: str, text: str) -> list[dict]:
    b = base_rel(rel)
    lang = lang_of(rel)
    if b in DOC_BY_REL:
        page_title = f'{DOC_BY_REL[b]["n"]} {DOC_BY_REL[b][lang]}'
    else:
        page_title = re.sub(r"\s*[—|-]\s*OpenGeoRock.*$", "", title_of(text)).strip() or title_of(text)
    m = ARTICLE_RE.search(text) or re.search(r"(<main[^>]*>)(.*?)(</main>)", text, re.S)
    body = m.group(2) if m else ""
    out = []
    chunks = re.split(r"(?=<h2[\s>])", body)
    intro = strip_tags(chunks[0])[:420] if chunks else ""
    out.append({"t": page_title, "u": rel, "x": intro or desc_of(text)})
    for ch in chunks[1:]:
        hm = re.match(r"<h2([^>]*)>(.*?)</h2>", ch, re.S)
        if not hm:
            continue
        hid = attr("<x" + hm.group(1) + ">", "id")
        htext = strip_tags(re.sub(r'<span class="secnum">.*?</span>|<a class="anchor".*?</a>', "", hm.group(2), flags=re.S))
        out.append({"t": page_title, "h": htext, "u": rel + (f"#{hid}" if hid else ""), "x": strip_tags(ch[hm.end():])[:360]})
    return out


def write_sitemap(pages: list[str]):
    rows = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for rel in pages:
        if base_rel(rel) == "404.html":
            continue
        b = base_rel(rel)
        rows.append(f"  <url><loc>{BASE}{pretty(rel)}</loc>"
                    f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}{pretty(b)}"/>'
                    f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}{pretty("es/" + b)}"/></url>')
    rows.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(rows) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# comprobaciones


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.imgs_no_alt: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a and a["id"]:
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if key in a and a[key] is not None and tag in ("a", "link", "script", "img", "source", "iframe"):
                self.links.append((tag, a[key]))
        if tag == "img" and "alt" not in a:
            self.imgs_no_alt.append(a.get("src", "?"))


def check(pages: list[str]) -> int:
    errors, warns = [], []
    parsed = {}
    for rel in pages:
        c = Collector()
        txt = (ROOT / rel).read_text(encoding="utf-8")
        c.feed(txt)
        parsed[rel] = (c, txt)
    for rel, (c, txt) in parsed.items():
        for src in c.imgs_no_alt:
            errors.append(f"{rel}: <img> sin alt ({src})")
        if re.search(r"\{\{\w+\}\}", txt):
            errors.append(f"{rel}: marcador {{...}} sin rellenar")
        if re.search(r'data-tex="[^"]*"[^>]*>(?!<!--k-->)', txt):
            warns.append(f"{rel}: hay ecuaciones sin renderizar (node tools/render_math.cjs)")
        for tag, link in c.links:
            if re.match(r"^(https?:|mailto:|tel:|javascript:|data:)", link) or link == "":
                continue
            path, _, frag = link.partition("#")
            if not path:
                target = rel
            elif path.startswith("/"):
                target = posixpath.normpath(path.lstrip("/")) if path.strip("/") else "index.html"
                if path.endswith("/") and path.strip("/"):
                    target = posixpath.join(target, "index.html")
                if not (ROOT / target).exists():
                    errors.append(f"{rel}: enlace roto: {link}")
                    continue
            else:
                target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), path))
                if path.endswith("/"):
                    target = posixpath.join(target, "index.html")
                if target.startswith(".."):
                    errors.append(f"{rel}: enlace fuera del sitio: {link}")
                    continue
                if not (ROOT / target).exists():
                    errors.append(f"{rel}: enlace roto: {link}")
                    continue
            if frag and target.endswith(".html"):
                if target in parsed and frag not in parsed[target][0].ids:
                    errors.append(f"{rel}: ancla inexistente: {link}")
    en = {p for p in pages if lang_of(p) == "en" and p != "404.html"}
    es = {base_rel(p) for p in pages if lang_of(p) == "es" and base_rel(p) != "404.html"}
    for p in sorted(en - es):
        warns.append(f"falta la versión ES de {p}")
    for p in sorted(es - en):
        warns.append(f"falta la versión EN de es/{p}")
    for d in DOC_PAGES:
        for lang in ("en", "es"):
            r = localized(d["rel"], lang)
            if r not in parsed:
                warns.append(f"página de la documentación pendiente: {r}")
    for img in (ROOT / "assets").rglob("*"):
        if img.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif") and img.stat().st_size > IMG_BUDGET:
            warns.append(f"imagen de más de 300 KB: {img.relative_to(ROOT).as_posix()} ({img.stat().st_size // 1024} KB)")
    for w in warns:
        print("AVISO ", w)
    for e in errors:
        print("ERROR ", e)
    print(f"\n{len(pages)} páginas · {len(errors)} errores · {len(warns)} avisos")
    return 1 if errors else 0


# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="comprobar enlaces, paridad e imágenes")
    ap.add_argument("--only", nargs="+", metavar="PÁGINA",
                    help="escribir solo estas páginas (rutas relativas al repo); no regenera índice ni sitemap. "
                         "Para trabajar en paralelo sin pisar páginas ajenas")
    a = ap.parse_args()
    only = {Path(p).resolve().relative_to(ROOT).as_posix() if Path(p).is_absolute() else Path(p).as_posix()
            for p in (a.only or [])}

    pages = all_pages()
    texts: dict[str, str] = {}
    all_labels: dict[str, dict] = {}
    tocs: dict[str, list] = {}
    for rel in pages:
        text = (ROOT / rel).read_text(encoding="utf-8")
        lang, root = lang_of(rel), root_of(rel)
        text = re.sub(r"<html[^>]*>", f'<html class="no-js" lang="{lang}" data-root="{root}">', text, count=1)
        text = region(text, "head", head_html(rel, text))
        text = region(text, "header", header_html(rel))
        text = region(text, "footer", footer_html(rel))
        text = re.sub(r"<span data-v>[^<]*</span>", f"<span data-v>{VERSION}</span>", text)
        b = base_rel(rel)
        if b in DOC_BY_REL:
            text = region(text, "docnav", docnav_html(rel))
            text = region(text, "dochead", dochead_html(rel))
            text = region(text, "docfoot", docfoot_html(rel))
            m = ARTICLE_RE.search(text)
            if m:
                body, labels, toc = number_article(m.group(2), DOC_BY_REL[b]["n"], lang)
                text = text[: m.start(2)] + body + text[m.end(2):]
                all_labels[rel] = labels
                tocs[rel] = toc
        elif has_region(text, "docnav"):
            text = region(text, "docnav", docnav_html(rel))
        if has_region(text, "docgroups"):
            text = region(text, "docgroups", docgroups_html(rel))
        texts[rel] = text

    problems = []
    index = {"en": [], "es": []}
    for rel, text in texts.items():
        text, probs = fill_xrefs(rel, text, all_labels)
        problems += probs
        if rel in tocs:
            text = region(text, "pagetoc", pagetoc_html(rel, tocs[rel]))
        texts[rel] = text
        if base_rel(rel) != "404.html":
            index[lang_of(rel)] += search_entries(rel, text)
        if only and rel not in only:
            continue
        old = (ROOT / rel).read_text(encoding="utf-8")
        if old != text:
            (ROOT / rel).write_text(text, encoding="utf-8")

    if only:
        missing = only - set(texts)
        for m in sorted(missing):
            print("AVISO  --only: no es una página del sitio:", m)
        print(f"escritas solo {len(only - missing)} páginas (sin índice ni sitemap)")
        return check(all_pages()) if a.check else 0
    for lang, entries in index.items():
        js = "window.OGR_SEARCH=" + json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + ";\n"
        (ROOT / "assets" / "js" / f"search-index.{lang}.js").write_text(js, encoding="utf-8")
    write_sitemap(pages)
    for p in problems:
        print("AVISO ", p)
    print(f"sincronizadas {len(pages)} páginas · versión {VERSION}")
    if a.check:
        return check(all_pages())
    return 0


if __name__ == "__main__":
    sys.exit(main())
