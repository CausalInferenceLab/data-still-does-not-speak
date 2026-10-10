// dist/index.html — 모든 발표 자료 목록 (GitHub Pages 첫 화면)
import { readFileSync, writeFileSync, readdirSync, existsSync, statSync, mkdirSync, copyFileSync } from "node:fs";
import { join } from "node:path";

const tokens = readFileSync("tokens/tokens.css", "utf8");
// 보고서는 HTML/CSS만 공개한다. 원본 데이터와 README 등은 복사하지 않는다.
const reports = existsSync("reports") ? readdirSync("reports")
  .filter((d) => !d.startsWith("_") && statSync(join("reports", d)).isDirectory())
  .filter((d) => existsSync(join("reports", d, "index.html")))
  .sort()
  .map((d) => {
    const source = join("reports", d);
    const output = join("dist", "reports", d);
    mkdirSync(output, { recursive: true });
    for (const name of ["index.html", "report.css"]) {
      if (existsSync(join(source, name))) copyFileSync(join(source, name), join(output, name));
    }
    const html = readFileSync(join(source, "index.html"), "utf8");
    return { dir: d, title: html.match(/<h1>(.*?)<\/h1>/)?.[1] ?? d };
  }) : [];
mkdirSync("dist/tokens", { recursive: true });
copyFileSync("tokens/tokens.css", "dist/tokens/tokens.css");
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
    };
  });

const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const rows = decks
  .map(
    (d) => `<li><a href="./${d.dir}/">${esc(d.title)}</a>${d.presenter ? `<span>${esc(d.presenter)}</span>` : ""}</li>`
  )
  .join("\n");
const reportRows = reports.map((r) => `<li><a href="./reports/${r.dir}/">${esc(r.title)}</a></li>`).join("\n");

writeFileSync(
  "dist/index.html",
  `<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>스터디 자료</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>
${tokens}
body{margin:0;font-family:var(--font-family-body);color:var(--color-text-primary);background:var(--color-surface-page)}
.band{height:56px;background:var(--color-brand-peach)}
main{max-width:860px;margin:0 auto;padding:48px 24px 80px}
h1{font-size:32px;font-weight:800;margin:0 0 14px}
h2{font-size:23px;color:var(--color-brand-navy);margin:32px 0 18px}
.rule{height:6px;width:100%;max-width:560px;background:linear-gradient(90deg,var(--color-brand-peach) 0 50%,var(--color-brand-blue) 50%);margin-bottom:36px}
ul{list-style:"▪   ";padding-left:22px;margin:0}
li{font-size:19px;margin:0 0 14px}
li a{color:var(--color-text-primary);font-weight:700;text-decoration:none}
li a:hover,li a:focus-visible{color:var(--color-brand-navy);text-decoration:underline}
li span{color:var(--color-text-muted);margin-left:12px;font-size:16px}
footer{position:fixed;bottom:0;left:0;right:0;height:36px;background:var(--color-brand-blue)}
</style></head><body>
<div class="band"></div>
<main><h1>스터디 자료</h1><div class="rule"></div>
${reportRows ? `<h2>보고서</h2><ul>${reportRows}</ul>` : ""}
<h2>발표 자료</h2>
<ul>
${rows || "<li>아직 올라온 발표 자료가 없습니다. slides/ 폴더에 덱을 추가하세요.</li>"}
</ul></main><footer></footer></body></html>`
);
console.log(`index: ${decks.length} decks`);
console.log(`reports: ${reports.length} static reports`);
