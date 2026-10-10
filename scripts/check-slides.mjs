import { existsSync, readdirSync, statSync } from 'node:fs';
import { join, sep } from 'node:path';

const errors = [];
for (const entry of readdirSync('slides', { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const index = `slides/${entry.name}/index.md`;
  if (!existsSync(index) || !statSync(index).isFile()) {
    errors.push(`${index}: 발표 폴더에는 index.md가 필요합니다.`);
  }
}

function check(directory) {
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) check(path);
    else if (/\.(md|mdown|markdown|markdn)$/i.test(entry.name)) {
      const relative = path.split(sep).join('/');
      if (!/^slides\/[^/]+\/index\.md$/.test(relative)) {
        errors.push(`${relative}: 마크다운은 slides/<발표 폴더>/index.md만 허용합니다.`);
      }
    }
  }
}
check('slides');

if (errors.length) {
  console.error('슬라이드 파일 배치를 확인하세요:\n' + errors.map(error => `- ${error}`).join('\n'));
  console.error('발표 파일은 index.md로 저장하고, 일반 노트·과제는 chapters/ 또는 assignments/에 두세요.');
  process.exit(1);
}
console.log('슬라이드 파일 배치 검사 통과');
