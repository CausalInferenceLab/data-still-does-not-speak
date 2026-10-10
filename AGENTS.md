# 현재 공개 방식 (2026-10-11)

사용자 결정으로 당분간 HTML만 공개합니다. PDF 생성 명령과 배포용 다운로드 링크를 제거했습니다. 아래 과거 인계 메모의 HTML/PDF 병행 결정은 현재 방식으로 대체됩니다. PDF 재개는 HTML과 스타일을 공유하고 페이지별 배치 비교를 통과한 뒤 검토합니다.

# 참여자 AI 튜터 모드

러너가 읽기·풀이·기록·GitHub 제출을 도와달라고 요청하면 먼저 [TUTOR.md](TUTOR.md)를 읽고 그 절차를 따릅니다. 러너의 생각과 확인한 근거를 함께 정리하고, 미확인 내용을 검증된 결과로 쓰지 않습니다.

- 러너 작업: [과제 안내](assignments/README.md), [러너 기록 템플릿](templates/runner-record.md), [제출 안내](CONTRIBUTING.md)를 사용합니다. 챕터를 읽고 지정된 연습문제 풀이 또는 사례 검토와 세 구간 기록을 함께 제출합니다. 문제 번호·사례가 미정이면 오너에게 확인합니다.
- 챕터 오너 작업: [챕터 안내](chapters/README.md)와 [챕터 노트 템플릿](templates/chapter-notes.md)으로 주차 준비 자료와 핵심 개념을 안내합니다. 슬라이드는 [SLIDES.md](SLIDES.md)를 따릅니다.
- 유지보수 작업: 아래 기존 인계 메모와 `DESIGN.md`를 참고해 저장소 구현을 다룹니다. 참여자 과제 제출 과정에서 설치·인증·테마·배포 설정을 바꾸는 작업으로 확대하지 않습니다.

과제 PR을 열면 제출 완료이며, 리뷰·병합·Pages 반영은 별도입니다. GitHub ID와 제출물은 공개됩니다. 개인정보·비밀 API 키·비공개 고객·회사 데이터를 포함하지 않으며, 허가 없이 교재 원문·스크린샷을 재배포하지 않습니다.

아래 인계 메모는 기존 기록을 보존한 것입니다. 경로·배포·검증·취약점 수치 등 과거 상태를 현재 상태로 간주하지 말고 필요한 경우 직접 확인합니다.

---

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
