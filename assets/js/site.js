/* opengeorock.org — comportamiento de la web (vanilla, sin dependencias).
   Todo es mejora progresiva: sin JS la web se lee entera.
   Índice: menú móvil · mega-menú · pestañas · copiar código · índice lateral
   de docs · «en esta página» · buscador · aviso de idioma · animaciones. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  doc.classList.add("js");
  var LANG = doc.lang && doc.lang.slice(0, 2) === "es" ? "es" : "en";
  var ROOT = doc.getAttribute("data-root") || "";
  var T = {
    en: { copy: "Copy", copied: "Copied", noResults: "No results for", searching: "Loading index…", menu: "Menu", close: "Close" },
    es: { copy: "Copiar", copied: "Copiado", noResults: "Sin resultados para", searching: "Cargando índice…", menu: "Menú", close: "Cerrar" }
  }[LANG];

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function store(key, val) {
    try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) { return null; }
  }

  /* ---------- menú móvil ---------- */
  var menuBtn = $(".menu-btn"), mobileNav = $(".mobile-nav");
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener("click", function () {
      var open = mobileNav.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    mobileNav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { mobileNav.classList.remove("open"); menuBtn.setAttribute("aria-expanded", "false"); document.body.style.overflow = ""; }
    });
  }

  /* ---------- mega-menú ---------- */
  $$(".has-menu").forEach(function (item) {
    var btn = $("button", item), timer;
    function set(open) { item.classList.toggle("open", open); btn.setAttribute("aria-expanded", open ? "true" : "false"); }
    btn.addEventListener("click", function (e) { e.stopPropagation(); set(!item.classList.contains("open")); });
    if (window.matchMedia("(hover: hover)").matches) {
      item.addEventListener("mouseenter", function () { clearTimeout(timer); set(true); });
      item.addEventListener("mouseleave", function () { timer = setTimeout(function () { set(false); }, 180); });
    }
    document.addEventListener("click", function (e) { if (!item.contains(e.target)) set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") set(false); });
  });

  /* ---------- pestañas (con grupos sincronizados y memoria) ---------- */
  function selectTab(tabs, tab, focus) {
    var list = $(".tablist", tabs);
    $$('[role="tab"]', list).forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
      var panel = document.getElementById(t.getAttribute("aria-controls"));
      if (panel) panel.hidden = !on;
    });
    if (focus) tab.focus();
  }
  $$(".tabs").forEach(function (tabs) {
    var list = $(".tablist", tabs);
    var tabsBtns = $$('[role="tab"]', list);
    var group = tabs.getAttribute("data-group");
    tabsBtns.forEach(function (t, i) {
      t.addEventListener("click", function () {
        selectTab(tabs, t);
        if (group) {
          var key = t.getAttribute("data-key");
          store("ogr-tab-" + group, key);
          $$('.tabs[data-group="' + group + '"]').forEach(function (other) {
            if (other === tabs) return;
            var match = $('[role="tab"][data-key="' + key + '"]', other);
            if (match) selectTab(other, match);
          });
        }
      });
      t.addEventListener("keydown", function (e) {
        var j = null;
        if (e.key === "ArrowRight") j = (i + 1) % tabsBtns.length;
        if (e.key === "ArrowLeft") j = (i - 1 + tabsBtns.length) % tabsBtns.length;
        if (e.key === "Home") j = 0;
        if (e.key === "End") j = tabsBtns.length - 1;
        if (j !== null) { e.preventDefault(); tabsBtns[j].click(); tabsBtns[j].focus(); }
      });
    });
    var initial = null;
    if (location.hash) {
      var target = document.getElementById(location.hash.slice(1));
      if (target && tabs.contains(target)) {
        var panel = target.closest('[role="tabpanel"]');
        if (panel) initial = $('[aria-controls="' + panel.id + '"]', list);
      }
    }
    if (!initial && group) {
      var saved = store("ogr-tab-" + group);
      if (saved) initial = $('[role="tab"][data-key="' + saved + '"]', list);
    }
    selectTab(tabs, initial || tabsBtns[0]);
  });

  /* ---------- copiar código ---------- */
  $$(".code").forEach(function (box) {
    var pre = $("pre", box);
    if (!pre || $(".copy", box)) return;
    var b = document.createElement("button");
    b.type = "button"; b.className = "copy"; b.textContent = T.copy;
    b.addEventListener("click", function () {
      var text = pre.innerText.replace(/\n$/, "");
      var done = function () { b.textContent = T.copied; b.classList.add("done"); setTimeout(function () { b.textContent = T.copy; b.classList.remove("done"); }, 1600); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done);
      else { var ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta); ta.select(); try { document.execCommand("copy"); done(); } catch (e) {} ta.remove(); }
    });
    box.appendChild(b);
  });

  /* ---------- índice lateral de la doc (móvil) ---------- */
  var side = $(".doc-side"), sideBtn = $(".doc-side-toggle");
  if (side && sideBtn) {
    sideBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = side.classList.toggle("open");
      sideBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (side.classList.contains("open") && !side.contains(e.target)) { side.classList.remove("open"); sideBtn.setAttribute("aria-expanded", "false"); }
    });
    var cur = $('.doc-nav a[aria-current="page"]', side);
    if (cur && cur.scrollIntoView) { var r = cur.getBoundingClientRect(); if (r.top > window.innerHeight - 80) side.scrollTop = cur.offsetTop - 120; }
  }

  /* ---------- «en esta página» y subnavegación: sección activa ---------- */
  function spy(links) {
    if (!links.length || !("IntersectionObserver" in window)) return;
    var map = {};
    links.forEach(function (a) { var id = decodeURIComponent(a.getAttribute("href").slice(1)); var el = document.getElementById(id); if (el) map[id] = a; });
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var ids = Object.keys(map);
      var active = null;
      for (var i = 0; i < ids.length; i++) { if (visible[ids[i]]) { active = ids[i]; break; } }
      if (active) links.forEach(function (a) { a.classList.toggle("active", a === map[active]); });
    }, { rootMargin: "-80px 0px -60% 0px" });
    Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
  }
  spy($$('.doc-toc a[href^="#"]'));
  spy($$('.subnav a[href^="#"]'));
  var printBtn = $(".doc-toc .print");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });

  /* ---------- buscador de la documentación ---------- */
  var indexState = 0, indexQueue = [];
  function loadIndex(cb) {
    if (window.OGR_SEARCH) return cb(window.OGR_SEARCH);
    indexQueue.push(cb);
    if (indexState) return;
    indexState = 1;
    var s = document.createElement("script");
    s.src = ROOT + "assets/js/search-index." + LANG + ".js";
    s.onload = function () { var q = indexQueue; indexQueue = []; q.forEach(function (f) { f(window.OGR_SEARCH || []); }); };
    document.head.appendChild(s);
  }
  function norm(s) { return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function highlight(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return out;
  }
  function snippet(text, terms) {
    var n = norm(text), pos = -1;
    for (var i = 0; i < terms.length; i++) { pos = n.indexOf(terms[i]); if (pos >= 0) break; }
    if (pos < 0) return text.slice(0, 150) + (text.length > 150 ? "…" : "");
    var start = Math.max(0, pos - 60);
    return (start > 0 ? "…" : "") + text.slice(start, start + 170) + (start + 170 < text.length ? "…" : "");
  }
  function search(index, query) {
    var terms = norm(query).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    var res = [];
    index.forEach(function (e) {
      var t = norm(e.t), h = norm(e.h || ""), x = norm(e.x || ""), score = 0, all = true;
      terms.forEach(function (term) {
        var s = 0;
        if (t.indexOf(term) >= 0) s += 10;
        if (h.indexOf(term) >= 0) s += 6;
        if (x.indexOf(term) >= 0) s += 2;
        if (!s) all = false;
        score += s;
      });
      if (all && score) res.push({ e: e, s: score + (e.h ? 0 : 1) });
    });
    res.sort(function (a, b) { return b.s - a.s; });
    return res.slice(0, 14).map(function (r) { return r.e; });
  }
  $$(".doc-search").forEach(function (box) {
    var input = $("input", box), panel = $(".results", box), sel = -1;
    if (!input || !panel) return;
    function render(q) {
      loadIndex(function (index) {
        var items = search(index, q);
        var terms = norm(q).split(/\s+/).filter(Boolean);
        sel = -1;
        if (!q.trim()) { panel.classList.remove("show"); panel.innerHTML = ""; return; }
        if (!items.length) { panel.innerHTML = '<div class="empty">' + T.noResults + " «" + esc(q) + "»</div>"; panel.classList.add("show"); return; }
        panel.innerHTML = items.map(function (e) {
          var title = e.h ? e.t + " › " + e.h : e.t;
          return '<a href="' + ROOT + e.u + '"><b>' + highlight(title, terms) + "</b><span>" + highlight(snippet(e.x || "", terms), terms) + "</span></a>";
        }).join("");
        panel.classList.add("show");
      });
    }
    var deb;
    input.addEventListener("input", function () { clearTimeout(deb); deb = setTimeout(function () { render(input.value); }, 90); });
    input.addEventListener("focus", function () { loadIndex(function () {}); if (input.value) render(input.value); });
    input.addEventListener("keydown", function (e) {
      var links = $$("a", panel);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!links.length) return;
        sel = e.key === "ArrowDown" ? Math.min(sel + 1, links.length - 1) : Math.max(sel - 1, 0);
        links.forEach(function (a, i) { a.classList.toggle("sel", i === sel); });
        links[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        if (links.length) { e.preventDefault(); (links[sel >= 0 ? sel : 0]).click(); }
      } else if (e.key === "Escape") { panel.classList.remove("show"); input.blur(); }
    });
    document.addEventListener("click", function (e) { if (!box.contains(e.target)) panel.classList.remove("show"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && !/input|textarea/i.test((document.activeElement || {}).tagName || "")) {
      var input = $(".doc-search input");
      if (input) { e.preventDefault(); input.focus(); }
    }
  });

  /* ---------- aviso de idioma (solo una vez) ---------- */
  var hint = $(".lang-hint");
  if (hint && LANG === "en" && !store("ogr-lang-hint")) {
    var langs = (navigator.languages || [navigator.language || ""]).join(",").toLowerCase();
    var alt = $('link[rel="alternate"][hreflang="es"]');
    if (/(^|,)es/.test(langs) && alt) {
      var go = $("a.go", hint);
      if (go) go.href = alt.getAttribute("href");
      hint.classList.add("show");
      $$("[data-dismiss]", hint).forEach(function (b) { b.addEventListener("click", function () { hint.classList.remove("show"); store("ogr-lang-hint", "1"); }); });
      if (go) go.addEventListener("click", function () { store("ogr-lang-hint", "1"); });
    }
  }

  /* ---------- animaciones al entrar en pantalla ---------- */
  var anim = $$("[data-animate]");
  if (anim.length) {
    if ("IntersectionObserver" in window) {
      var io2 = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("animate"); io2.unobserve(en.target); } });
      }, { threshold: 0.25 });
      anim.forEach(function (el) { io2.observe(el); });
    } else anim.forEach(function (el) { el.classList.add("animate"); });
  }
})();
