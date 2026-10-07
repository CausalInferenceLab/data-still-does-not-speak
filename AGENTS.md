# AGENTS.md — 작업 인계 메모

이 저장소에서 작업을 이어받는 코딩 에이전트를 위한 문서입니다. 작업 전에 이 파일과 `DESIGN.md`를 읽으세요.

## 목표

가짜연구소 인과추론팀(Causal-Lab) PPT 슬라이드 **디자인만** 추출해서, 팀원들이 GitHub에 `.md`로 자료를 쓰면
그 디자인이 적용된 HTML(주) / PDF(부)가 자동으로 만들어지는 템플릿 저장소.

## 결정된 사항

- **디자인만 가져온다.** 원본 덱(2025년 Marketing Science OT)의 발표 내용, 이름, 일정은 옛 자료이므로 저장소에 넣지 않는다.
  예시 덱(`slides/example/`)과 템플릿(`templates/deck.md`)은 자리표시자 텍스트만 쓴다.
- **원본은 md 하나, 출력은 HTML + PDF 둘 다.** HTML로만 통일하면 GitHub 저장소 화면에서 렌더링이 안 되고(Pages 필요),
  PDF로 공유·보관하던 기존 운영 방식과 충돌하기 때문.
- **도구는 Marp** (`@marp-team/marp-cli`). 테마는 `themes/causal-lab.css`.
- **디자인 토큰 원본은 `tokens/tokens.json`** (W3C Design Tokens 형식). `npm run tokens`가
  `tokens/tokens.css`와 테마의 `/* tokens:start */…/* tokens:end */` 구간을 다시 생성하고,
  `assets/logo-*.png`를 data URI로 테마의 `/* logos:start */…/* logos:end */` 구간에 넣는다.
  테마의 두 마커 구간은 손으로 고치지 않는다.
- 폰트는 Pretendard 우선 (원본은 맑은 고딕 계열).
- 색은 Office 테마 표준색으로 추정한 값: peach `#F4B183`, blue `#8FAADC`, navy `#002060`.

## 현재 상태

- 테마, 토큰, 동기화 스크립트, 예시 덱, 템플릿, GitHub Actions(PR 빌드 검사 + main 머지 시 Pages 배포) 완료.
- 로컬에서 `npm run build`로 HTML/PDF 생성과 Playwright 스크린샷 비교로 원본과 크기·간격을 맞춤.

## 남은 일 / 확인 필요

- [ ] 원본 PPT 파일에서 실제 색상값 확인 후 `tokens.json` 보정 (현재 값은 추정치)
- [ ] Pretendard가 원본 느낌과 맞는지 확인. 아니면 `font.family.*` 순서 조정
- [x] 기존 GitHub 저장소에 통합, Pages Source를 GitHub Actions로 설정, 첫 배포 확인
- [ ] 필요하면 레이아웃 추가 (예: 그래프+해석 강조형, 코드 슬라이드)

## 2026-10-08 이어받기 결과

- 사용자 지정 비교 원본: `/Users/jhyuck/Downloads/[Marketing_Science] Week01-OT.pdf` (18쪽). 원본 내용은 저장소에 복사하지 않았다.
- PDF에서 navy `#002060`, 맑은 고딕과 나눔스퀘어 폰트 리소스 확인. peach/blue의 PPT 실제 값 확인은 여전히 남아 있다.
- Pretendard는 웹용 대체로 유지. 1280×720 예시 커버/본문 캡처에서 로딩과 배치를 확인했다.
- 승인받은 `npm ci --ignore-scripts` 후 `npm run build` 성공: 9슬라이드 HTML/PDF와 덱 목록 생성. PDF용 Chrome은 제한된 환경 밖에서 실행해야 했다.
- 설치 시 npm이 취약점 12건(낮음 2, 보통 1, 높음 9)을 보고했다. 의존성 버전은 변경하지 않았다.
- 배포 대상: `https://github.com/CausalInferenceLab/data-still-does-not-speak.git`. 기존 README와 소개 이미지를 보존해야 한다.
- 사용자 재인증 후 PR #1을 main에 반영했다. GitHub Actions 빌드/배포 성공(run `37690702740`), 공개 목록/9슬라이드 HTML/PDF 접속 검증 완료.
- 배포 주소: `https://causalinferencelab.github.io/data-still-does-not-speak/`. 원본 폴더의 `origin`도 대상 저장소로 연결했다.

## 작업 규칙

- 레이아웃이나 토큰을 바꾸면 `DESIGN.md`도 같이 고친다.
- 디자인 확인은 `npm run build` 후 `dist/example/index.html`을 1280×720으로 스크린샷해서 본다.
- marp-cli를 직접 실행할 땐 `--no-stdin`을 붙인다 (없으면 stdin을 기다리며 멈춤).
