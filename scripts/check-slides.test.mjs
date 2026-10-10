import assert from 'node:assert/strict';
import { cpSync, existsSync, mkdtempSync, mkdirSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import test from 'node:test';

const root = fileURLToPath(new URL('../', import.meta.url));
const deck = '---\nmarp: true\n---\n# Smoke test\n';

function build(files, command = 'build:html') {
  const cwd = mkdtempSync(join(tmpdir(), 'slide-layout-'));
  try {
    cpSync(join(root, 'package.json'), join(cwd, 'package.json'));
    cpSync(join(root, 'scripts'), join(cwd, 'scripts'), { recursive: true });
    writeFileSync(join(cwd, '.marprc.yml'), 'inputDir: ./slides\noutput: ./dist\n');
    for (const [name, content] of Object.entries(files)) {
      mkdirSync(dirname(join(cwd, name)), { recursive: true });
      writeFileSync(join(cwd, name), content);
    }
    const result = spawnSync('npm', ['run', command], { cwd, encoding: 'utf8', timeout: 20000 });
    const html = join(cwd, 'dist/demo/index.html');
    return { ...result, html: existsSync(html) ? readFileSync(html, 'utf8') : null };
  } finally {
    rmSync(cwd, { recursive: true, force: true });
  }
}

test('HTML build rejects an extra README before Marp can convert it', () => {
  const result = build({ 'slides/demo/index.md': deck, 'slides/demo/README.md': '# Notes\n' });
  assert.equal(result.status, 1, result.stdout + result.stderr);
  assert.match(result.stderr, /slides\/demo\/README\.md/);
  assert.equal(result.html, null);
});

test('valid deck, image assets, and notes outside slides still build', () => {
  const result = build({
    'slides/demo/index.md': deck,
    'slides/demo/img/chart.svg': '<svg xmlns="http://www.w3.org/2000/svg"/>',
    'chapters/w03/README.md': '# Chapter notes\n',
    'assignments/w03/learner/README.md': '# Learner record\n',
  });
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.match(result.html, /Smoke test/);
});

test('a deck folder with only assets reports its missing index.md', () => {
  const result = build({ 'slides/demo/img/chart.svg': '<svg/>' });
  assert.equal(result.status, 1, result.stdout + result.stderr);
  assert.match(result.stderr, /slides\/demo\/index\.md/);
});

for (const path of [
  'slides/notes.md',
  'slides/demo/img/notes.md',
  'slides/demo/INDEX.MD',
  'slides/demo/notes.markdown',
  'slides/demo/notes.mdown',
  'slides/demo/notes.markdn',
]) {
  test(`rejects Markdown outside the deck entry: ${path}`, () => {
    const files = { [path]: '# Notes\n' };
    // macOS can treat index.md and INDEX.MD as the same file.
    if (path !== 'slides/demo/INDEX.MD') files['slides/demo/index.md'] = deck;
    const result = build(files);
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.ok(result.stderr.includes(path), result.stderr);
    assert.equal(result.html, null);
  });
}

for (const command of ['build', 'dev', 'build:ot-live', 'build:reports']) {
  test(`${command} also blocks invalid Markdown before its build step`, () => {
    const result = build({ 'slides/demo/index.md': deck, 'slides/demo/README.md': '# Notes\n' }, command);
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stderr, /slides\/demo\/README\.md/);
    assert.equal(result.html, null);
  });
}

test('OT and listing publish HTML without PDF download links', () => {
  const cwd = mkdtempSync(join(tmpdir(), 'slides-html-only-'));
  try {
    for (const name of ['package.json', '.marprc.yml', 'scripts', 'tokens', 'themes', 'assets', 'slides']) {
      cpSync(join(root, name), join(cwd, name), { recursive: true });
    }
    symlinkSync(join(root, 'node_modules'), join(cwd, 'node_modules'), 'dir');
    mkdirSync(join(cwd, 'dist/ot-live'), { recursive: true });
    writeFileSync(join(cwd, 'dist/ot-live/index.pdf'), 'old local PDF');
    const result = spawnSync('npm', ['run', 'build'], { cwd, encoding: 'utf8', timeout: 30000 });
    assert.equal(result.status, 0, result.stdout + result.stderr);
    assert.equal(existsSync(join(cwd, 'dist/example/index.pdf')), false);
    assert.equal(readFileSync(join(cwd, 'dist/ot-live/index.pdf'), 'utf8'), 'old local PDF');
    for (const name of ['dist/index.html', 'dist/ot-live/index.html', 'dist/ot-live/guide.html']) {
      const html = readFileSync(join(cwd, name), 'utf8');
      assert.doesNotMatch(html, /href=["'][^"']*\.pdf/i);
    }
    const html = readFileSync(join(cwd, 'dist/ot-live/index.html'), 'utf8');
    assert.match(html, /<section\b/);
    assert.match(html, /href=".\/guide.html"/);
  } finally {
    rmSync(cwd, { recursive: true, force: true });
  }
});
