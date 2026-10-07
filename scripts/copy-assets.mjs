// slides/ 안의 이미지 등 md가 아닌 파일을 dist/로 같은 구조로 복사
import { cpSync, existsSync } from "node:fs";
if (existsSync("slides")) {
  cpSync("slides", "dist", {
    recursive: true,
    filter: (src) => !src.endsWith(".md"),
  });
}
console.log("copied slide assets → dist/");
