# Causal-Lab 슬라이드 템플릿

마크다운으로 발표 자료를 쓰면 Causal-Lab 디자인이 적용된 HTML과 PDF가 만들어지는 템플릿입니다.
GitHub Actions가 빌드해서 GitHub Pages에 올립니다.

## 발표 자료 올리기

1. `templates/deck.md`를 `slides/<덱 폴더>/index.md`로 복사합니다.
2. front matter의 `title`, `presenter`, `footer`와 커버 슬라이드를 고칩니다.
3. 이미지는 같은 폴더의 `img/`에 넣고 `![](./img/파일.png)`로 씁니다.
4. Pull Request를 엽니다. CI가 빌드를 확인하고, main에 머지되면 Pages에 올라갑니다.

쓸 수 있는 레이아웃은 `slides/example/index.md`, 규칙은 [DESIGN.md](DESIGN.md)를 보세요.

## 미리보기

- **VS Code**: 추천 확장(Marp for VS Code)을 설치하면 이 테마로 바로 미리보기 됩니다.
- **로컬 서버**: `npm install` 후 `npm run dev`
- **전체 빌드**: `npm run build` → `dist/`에 덱별 `index.html`, `index.pdf`와 목록 페이지 (Chrome 필요)

## 처음 한 번 설정 (관리자)

저장소 Settings → Pages → Source를 **GitHub Actions**로 바꿉니다.

## 구조

```
DESIGN.md                 디자인 규칙
tokens/tokens.json        디자인 토큰 원본
tokens/tokens.css         CSS 변수 (자동 생성)
themes/causal-lab.css     Marp 테마
assets/                   로고 (테마에 자동 포함)
templates/deck.md         새 덱 템플릿
slides/example/           레이아웃 예시 덱
scripts/                  토큰 동기화, 빌드 보조
.github/workflows/        빌드 & 배포
```
