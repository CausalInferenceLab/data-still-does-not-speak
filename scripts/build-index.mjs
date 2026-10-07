// dist/index.html — 모든 발표 자료 목록 (GitHub Pages 첫 화면)
import { readFileSync, writeFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { join } from "node:path";

const tokens = readFileSync("tokens/tokens.css", "utf8");
const decks = readdirSync("slides")
  .filter((d) => !d.startsWith("_") && statSync(join("slides", d)).isDirectory())
  .filter((d) => existsSync(join("slides", d, "index.md")))
  .sort()
  .map((d) => {
    const md = readFileSync(join("slides", d, "index.md"), "utf8");
    const fm = md.match(/^---\n([\s\S]*?)\n---/)?.[1] ?? "";
    const pick = (k) => fm.match(new RegExp(`^${k}:\\s*"?(.*?)"?\\s*$`, "m"))?.[1];
    return {
      dir: d,
      title: pick("title") ?? d,
      presenter: pick("presenter") ?? "",
      pdf: existsSync(join("dist", d, "index.pdf")),
    };
  });

const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const rows = decks
  .map(
    (d) => `<li><a href="./${d.dir}/">${esc(d.title)}</a>${d.presenter ? `<span>${esc(d.presenter)}</span>` : ""}${
      d.pdf ? ` <a class="pdf" href="./${d.dir}/index.pdf">PDF</a>` : ""
    }</li>`
  )
  .join("\n");

writeFileSync(
  "dist/index.html",
  `<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>발표 자료</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
${tokens}
body{margin:0;font-family:var(--font-family-body);color:var(--color-text-primary);background:var(--color-surface-page)}
.band{height:56px;background:var(--color-brand-peach)}
main{max-width:860px;margin:0 auto;padding:48px 24px 80px}
h1{font-size:32px;font-weight:800;margin:0 0 14px}
.rule{height:6px;width:100%;max-width:560px;background:linear-gradient(90deg,var(--color-brand-peach) 0 50%,var(--color-brand-blue) 50%);margin-bottom:36px}
ul{list-style:"▪   ";padding-left:22px;margin:0}
li{font-size:19px;margin:0 0 14px}
li a{color:var(--color-text-primary);font-weight:700;text-decoration:none}
li a:hover,li a:focus-visible{color:var(--color-brand-navy);text-decoration:underline}
li span{color:var(--color-text-muted);margin-left:12px;font-size:16px}
a.pdf{font-size:13px;font-weight:700;color:var(--color-brand-navy);border:1px solid var(--color-brand-blue);padding:1px 6px;margin-left:10px}
footer{position:fixed;bottom:0;left:0;right:0;height:36px;background:var(--color-brand-blue)}
</style></head><body>
<div class="band"></div>
<main><h1>발표 자료</h1><div class="rule"></div>
<ul>
${rows || "<li>아직 올라온 발표 자료가 없습니다. slides/ 폴더에 덱을 추가하세요.</li>"}
</ul></main><footer></footer></body></html>`
);
console.log(`index: ${decks.length} decks`);
