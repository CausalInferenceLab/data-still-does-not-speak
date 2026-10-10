# Causal-Lab 슬라이드 템플릿

마크다운으로 발표 자료를 쓰면 Causal-Lab 디자인이 적용된 HTML과 PDF가 만들어지는 템플릿입니다.
GitHub Actions가 빌드해서 GitHub Pages에 올립니다.

## 챕터 오너의 내용과 선택 슬라이드

챕터 오너가 꼭 해야 하는 일은 **내용 정리**이고, 슬라이드는 **선택**입니다.

| 구분 | 위치 | 필수 여부 | 결과를 보는 곳 |
| --- | --- | --- | --- |
| 챕터 내용 | `chapters/<주차>/README.md` ([템플릿](templates/chapter-notes.md)) | 챕터 오너가 작성 | GitHub 화면에서 문서로 읽기 |
| 발표 슬라이드 | `slides/<덱 폴더>/index.md` ([템플릿](templates/deck.md)) | 선택 | PR이 main에 머지된 뒤 Pages |

처음 GitHub 제출을 연습하는 분은 [TUTOR.md](TUTOR.md)로 시작하세요.

## 변환 범위: 참여자 규약과 실제 빌드 범위

실제 빌드 설정(`.marprc.yml`의 `inputDir: ./slides`)은 `slides/` 폴더 안의 Markdown을 대상으로 합니다. 즉 `slides/` 안에 `index.md`가 아닌 다른 `.md`를 두면 Marp가 그것도 변환하려 할 수 있습니다.

그래서 참여자는 다음 규약을 지킵니다.

- `slides/<덱 폴더>/`에는 **`index.md`만** 둡니다. 이미지는 `img/`에 둡니다.
- 챕터 노트와 과제 같은 일반 `.md`는 `chapters/`와 `assignments/`에 둡니다. 이 폴더들은 빌드 입력이 아니며 HTML로 자동 변환되지 않습니다. GitHub 문서 화면에서 읽습니다.
- Pages의 덱 목록 페이지는 `slides/<덱 폴더>/index.md`가 있는 폴더를 찾아 만듭니다. 이 파일 이름이 다르면 목록에 나타나지 않습니다.
- Pages에는 PR이 main에 머지된 뒤에 올라갑니다. PR을 열었다고 Pages에 바로 보이지 않습니다.

## 발표 자료 올리기

1. `templates/deck.md`를 `slides/<덱 폴더>/index.md`로 복사합니다. 덱 폴더 이름은 `w03-ch03`처럼 주차와 챕터를 씁니다.
2. 템플릿 맨 위 front matter(`marp: true`, `theme: causal-lab` 등)는 지우지 말고 유지합니다. `title`, `presenter`, `footer`와 커버 슬라이드만 고칩니다.
3. 슬라이드는 한 줄짜리 `---`로 구분합니다.
4. 이미지는 같은 폴더의 `img/`에 넣고 정확한 상대경로로 씁니다. 예: `![](./img/파일.png)`. 경로나 파일 이름의 대소문자가 다르면 이미지가 보이지 않습니다.
5. Pull Request를 엽니다. CI가 빌드를 확인하고, main에 머지되면 Pages에 올라갑니다.

GitHub 웹에서 제출하는 순서(Fork, branch, 파일 올리기, PR)는 [TUTOR.md](TUTOR.md)와 [CONTRIBUTING.md](CONTRIBUTING.md)를 보세요. 공개 저장소이므로 개인정보, 비밀, 비공개 데이터, 교재 문제 원문이나 스크린샷은 슬라이드에 넣지 않습니다.

쓸 수 있는 레이아웃은 `slides/example/index.md`, 규칙은 [DESIGN.md](DESIGN.md)를 보세요.

## 미리보기

- **VS Code**: 추천 확장(Marp for VS Code)을 설치하면 이 테마로 바로 미리보기 됩니다.
- **로컬 서버**: `npm ci` 후 `npm run dev`
- **전체 빌드**: `npm run build` → `dist/`에 덱별 `index.html`, `index.pdf`와 목록 페이지 (Chrome 필요)

러너와 챕터 오너는 설치 없이 GitHub 웹만으로 제출할 수 있습니다. 로컬 미리보기는 선택입니다.

## 유지보수자: 로컬 환경

CI는 `npm ci`로 `package-lock.json`에 고정된 버전을 설치합니다. 로컬에서도 같은 환경을 만들려면 `npm ci`를 씁니다. 설치는 각자의 환경에서 직접 판단해 실행하세요.

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
