#!/usr/bin/env node
// SPDX-License-Identifier: MIT (KaTeX) — este script: © 2026 Samuel Sáez López
//
// render_math.cjs — pre-renderiza las ecuaciones de la web con KaTeX.
//
//   node tools/render_math.cjs            todas las páginas
//   node tools/render_math.cjs ruta.html  solo esas
//
// En el HTML se escribe solo la fuente TeX, en un atributo:
//   <span class="m" data-tex="\tan\phi'"></span>                 (en línea)
//   <div class="eq" id="eq-bishop" data-tex="F = \dots"></div>  (destacada)
// y este script mete dentro el resultado entre <!--k--> y <!--/k-->. Se puede
// relanzar siempre: sustituye el render anterior. No necesita npm install:
// usa el katex.min.js vendorizado en tools/vendor/ (KaTeX 0.19.0, MIT).
// En la web solo se sirven assets/vendor/katex/katex.min.css y sus fuentes.
"use strict";
const fs = require("fs");
const path = require("path");
const katex = require(path.join(__dirname, "vendor", "katex.min.js"));

const ROOT = path.resolve(__dirname, "..");
const SKIP = new Set([".git", ".claude", ".vscode", "tools", "spec", "dev", "node_modules", "assets"]);

// Macros compartidas por toda la documentación: una notación, un sitio.
const MACROS = {
  "\\FS": "F",
  "\\tanphi": "\\tan\\phi'",
  "\\cp": "c'",
  "\\phip": "\\phi'",
  "\\sigmap": "\\sigma'",
  "\\dd": "\\mathrm{d}",
};

function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (dir === ROOT && SKIP.has(e.name)) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith(".html")) out.push(p);
  }
  return out;
}

function decode(s) {
  return s
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&amp;/g, "&");
}

const RE = /(<(span|div)\b([^>]*?)\bdata-tex="([^"]*)"([^>]*)>)(?:<!--k-->[\s\S]*?<!--\/k-->)?(<\/\2>)/g;

let files = process.argv.slice(2).map((f) => path.resolve(f));
if (!files.length) files = walk(ROOT, []);
let total = 0, changed = 0, problems = 0;
for (const file of files) {
  const src = fs.readFileSync(file, "utf8");
  if (!src.includes("data-tex=")) continue;
  const out = src.replace(RE, (whole, open, tag, pre, tex, post, close) => {
    total++;
    const display = tag === "div" || /\bclass="[^"]*\beq\b/.test(open);
    const source = decode(tex);
    let rendered;
    try {
      rendered = katex.renderToString(source, {
        displayMode: display, output: "htmlAndMathml", throwOnError: true,
        strict: "ignore", macros: { ...MACROS }, trust: false,
      });
    } catch (err) {
      problems++;
      console.error(`ERROR ${path.relative(ROOT, file)}: ${err.message}\n      ${source}`);
      rendered = `<span class="katex-error" title="${err.message.replace(/"/g, "&quot;")}">${tex}</span>`;
    }
    return `${open}<!--k-->${rendered}<!--/k-->${close}`;
  });
  if (out !== src) { fs.writeFileSync(file, out, "utf8"); changed++; }
}
console.log(`${total} ecuaciones · ${changed} archivos actualizados · ${problems} errores`);
process.exit(problems ? 1 : 0);
