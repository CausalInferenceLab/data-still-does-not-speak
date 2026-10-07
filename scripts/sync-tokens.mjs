// tokens/tokens.json → tokens/tokens.css + themes/causal-lab.css(마커 사이 영역)
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const tokens = JSON.parse(readFileSync("tokens/tokens.json", "utf8"));
const lines = [];

const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
const fmt = (v) =>
  Array.isArray(v) ? v.map((f) => (/\s/.test(f) ? `"${f}"` : f)).join(", ") : String(v);

(function walk(node, path) {
  for (const [k, v] of Object.entries(node)) {
    if (k.startsWith("$")) continue;
    if (v && typeof v === "object" && "$value" in v) {
      lines.push(`  --${[...path, k].map(kebab).join("-")}: ${fmt(v.$value)};`);
    } else if (v && typeof v === "object") walk(v, [...path, k]);
  }
})(tokens, []);

const block = lines.join("\n");
writeFileSync(
  "tokens/tokens.css",
  `/* 자동 생성 파일 — tokens/tokens.json을 수정하고 \`npm run tokens\` 실행 */\n:root {\n${block}\n}\n`
);

const themePath = "themes/causal-lab.css";
const theme = readFileSync(themePath, "utf8");
const re = /(\/\* tokens:start \*\/)[\s\S]*?(\/\* tokens:end \*\/)/;
if (!re.test(theme)) throw new Error("tokens 마커를 테마에서 찾지 못했습니다");
let out = theme.replace(re, `$1\nsection {\n${block}\n}\n$2`);

// assets/의 로고를 data URI로 테마에 넣는다 → HTML 한 파일로 어디서든 열림
const logos = { "logo-causal-lab": "assets/logo-causal-lab.png", "logo-pseudolab": "assets/logo-pseudolab.png" };
const logoLines = Object.entries(logos)
  .filter(([, f]) => existsSync(f))
  .map(([k, f]) => `  --${k}: url("data:image/png;base64,${readFileSync(f).toString("base64")}");`);
const reLogo = /(\/\* logos:start \*\/)[\s\S]*?(\/\* logos:end \*\/)/;
out = out.replace(reLogo, logoLines.length ? `$1\nsection {\n${logoLines.join("\n")}\n}\n$2` : "$1\n$2");
writeFileSync(themePath, out);
console.log(`synced ${lines.length} tokens`);
