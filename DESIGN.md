# DESIGN.md — Causal-Lab 슬라이드 디자인 시스템

가짜연구소 인과추론팀(Causal-Lab) PPT 디자인을 마크다운 기반 템플릿으로 옮긴 문서입니다. 디자인만 담고 있으며 특정 발표 내용은 포함하지 않습니다.
발표자는 디자인을 신경 쓰지 않고 **내용만 `.md`로 쓰면** 같은 모양의 HTML(주) / PDF(부)가 만들어지는 것이 목표입니다.

- 디자인 토큰 원본: [`tokens/tokens.json`](tokens/tokens.json) (W3C Design Tokens 형식)
- CSS 변수: [`tokens/tokens.css`](tokens/tokens.css) — 자동 생성
- Marp 테마: [`themes/causal-lab.css`](themes/causal-lab.css)
- 새 덱 시작점: [`templates/deck.md`](templates/deck.md)
- 모든 레이아웃 예시: [`slides/example/index.md`](slides/example/index.md)

---

## 1. 디자인 원칙

원본 덱에서 읽어낸 규칙입니다. 새 레이아웃을 추가할 때도 이 네 가지를 지킵니다.

1. **두 가지 색이 반반.** 브랜드 장식은 항상 peach | blue 를 같은 비율로 나눠 씁니다. 제목 왼쪽 블록, 제목 밑 줄, 커버 위/아래 밴드 모두 같은 규칙입니다. 한 색만 쓰는 장식은 만들지 않습니다.
2. **장식은 제목에만.** 본문 영역은 흰 배경 + 검정 텍스트입니다. 카드, 그림자, 둥근 박스, 배경색 블록을 본문에 넣지 않습니다.
3. **강조는 navy + 밑줄 하나.** 섹션 헤딩만 navy(#002060)와 밑줄을 씁니다. 본문 중 강조가 필요하면 굵게, 대비가 필요하면 `muted`(회색)와 `navy`를 짝지어 씁니다 (예: "<span class="muted">A</span>를 넘어 <span class="navy">B</span>").
4. **흐리게 해서 위치를 알려준다.** 같은 목차 슬라이드를 반복할 때 지금 다루지 않는 항목은 `dim`으로 흐리게 처리합니다. 새 색을 추가하지 않고 위치를 보여주는 방법입니다.

---

## 2. 토큰

### 색

| 토큰 | 값 | 쓰임 |
|---|---|---|
| `color.brand.peach` | `#F4B183` | 커버 상단 밴드, 분할 장식의 왼쪽 |
| `color.brand.blue` | `#8FAADC` | 커버 하단 밴드, 분할 장식의 오른쪽 |
| `color.brand.navy` | `#002060` | 섹션 헤딩, 대비 강조 |
| `color.text.primary` | `#000000` | 제목, 본문 |
| `color.text.muted` | `#7F7F7F` | 주석, *(Optional)*, 페이지 번호 |
| `color.text.footer` | `#595959` | 하단 덱 이름 |
| `color.text.dim` | `#C9D4EA` | 포커스 슬라이드의 흐린 항목 |
| `color.text.link` | `#0563C1` | 링크 |
| `color.table.border` | `#4472C4` | 표 테두리 |

> 2026-10-08에 사용자가 지정한 `[Marketing_Science] Week01-OT.pdf`를 확인했습니다. PDF 벡터 색상에서 navy `#002060`을 확인했고, 커버와 본문의 peach | blue 장식 구성을 시각적으로 확인했습니다. peach와 blue는 여전히 추정값입니다. PDF 렌더링의 픽셀값은 색상 프로파일의 영향을 받으므로 PPT의 실제 색상값이나 밝기 변환으로 간주하지 않습니다.

### 글꼴

| 토큰 | 값 |
|---|---|
| `font.family.display`, `font.family.body` | Pretendard → Malgun Gothic → Apple SD Gothic Neo → Noto Sans CJK KR |
| `font.weight.medium` 500 | 본문 |
| `font.weight.heavy` 800 | 슬라이드 제목, 섹션 헤딩, 커버 |

OT PDF의 폰트 리소스에서 MalgunGothic / MalgunGothicBold와 NanumSquareR / B / EB를 확인했습니다. 현재 템플릿은 Pretendard를 웹용 대체 폰트로 유지합니다. 커버와 본문 시각 비교에서 기본 배치와 한글 표시는 확인했으며, 원본 글꼴의 정확한 재현을 뜻하지 않습니다. 실제 렌더링은 폰트 로딩 성공 여부와 설치된 대체 폰트에 영향을 받습니다.

### 글자 크기 (1280×720 기준)

| 토큰 | 값 | 요소 |
|---|---|---|
| `font.size.coverTitle` | 48px | 커버 『덱 이름』 |
| `font.size.coverSubtitle` | 28px | 회차 : 주제 |
| `font.size.presenter` | 26px | 발표자 \| 소속 |
| `font.size.title` | 38px | 슬라이드 제목 (h1) |
| `font.size.section` | 26px | 섹션 헤딩 (h2) |
| `font.size.body` | 23px | 본문, 목록 |
| `font.size.table` | 17px | 표 |
| `font.size.pageNumber` | 15px | 페이지 번호 |
| `font.size.footer` | 10px | 하단 덱 이름 |

### 크기

| 토큰 | 값 | 요소 |
|---|---|---|
| `size.slide` | 1280 × 720 | 16:9 |
| `size.padding` | x 52 / top 28 / bottom 56 | 본문 슬라이드 여백 |
| `size.accentBar` | 24 × 42 | 제목 왼쪽 2색 블록 |
| `size.splitRule.content*` | 752 × 6 | 제목 밑 2색 줄 (슬라이드 폭의 약 59%) |
| `size.splitRule.cover*` | 754 × 7 | 커버 제목 밑 2색 줄 (가운데 정렬) |
| `size.coverBand` | 위 18.5% / 아래 18.5% | 커버 밴드 높이 |
| `size.logo.content` | 64px | 본문 슬라이드 우상단 Causal-Lab 로고 |
| `size.list.indentSection` | 118px | 섹션 헤딩 아래 ▪ 목록 들여쓰기 |

---

## 3. 레이아웃

### 3-1. 커버 / 마무리 — `<!-- _class: cover -->`, `<!-- _class: closing -->`

```
┌──────────────────────────────────────────┐
│████████████ peach 밴드 18.5% ████████████│
│                         [가짜연구소][CL] │
│                『덱 이름』               │
│        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀        │  ← peach | blue 줄
│               회차 : 주제                │
│                                          │
│████████████ blue 밴드 18.5% █████████████│
│███████████████(footer)██ 발표자 | 소속 ██│
└──────────────────────────────────────────┘
```

| 마크다운 | 위치 |
|---|---|
| `# 『덱 이름』` | 가운데 제목 + 2색 줄 |
| `## 회차 : 주제` | 부제 (마무리 슬라이드에선 생략) |
| 일반 문단 `발표자 \| 소속` | 하단 밴드 오른쪽 |

페이지 번호는 `<!-- _paginate: skip -->`로 숨깁니다. 커버를 건너뛰고 다음 슬라이드가 1번이 됩니다.

### 3-2. 본문 슬라이드 (기본)

```
┌──────────────────────────────────────────┐
│ ▌▌ 슬라이드 제목                     [CL]│
│ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                  │
│                                          │
│ •  최상위 항목                           │
│      - 하위 항목                         │
│                                          │
│ •  최상위 항목                           │
│                                       12 │
│            (덱 이름 footer)              │
└──────────────────────────────────────────┘
```

목록 기호는 자동으로 정해집니다.

| 상황 | 기호 | 간격 |
|---|---|---|
| 섹션 헤딩 없는 목록 | `•` | 넓게 |
| `##` 섹션 헤딩 아래 목록 | `▪` + 들여쓰기 | 헤딩이 1개면 넓게, 2개 이상이면 붙여서 |
| 하위 항목 | `-` | 붙여서 |

자동 간격이 맞지 않으면 슬라이드에 `<!-- _class: compact -->` 또는 `<!-- _class: spacious -->`를 붙입니다.

### 3-3. 포커스 (목차 반복) — `<div class="dim">`

지금 다루지 않는 섹션을 `<div class="dim">` … `</div>`로 감쌉니다. 감싼 부분의 앞뒤에 빈 줄이 있어야 마크다운이 해석됩니다.

### 3-4. 프로필 — `<div class="profile">`

왼쪽 330px 사진(3:4로 잘림) + 오른쪽 목록. 사진 위 이름은 `<p class="name">이름 (English)</p>`.

### 3-5. 2단 — `<div class="cols">` / `<div class="cols-60-40">`

그래프 + 해석처럼 나란히 둘 때. 이미지는 최대 높이 480px로 자동 축소됩니다.

### 3-6. 표 + 하단 안내

표는 슬라이드 폭 84%, 가운데 정렬, 첫 열과 마지막 열은 가운데 맞춤입니다.
슬라이드 하단 중앙에 한 줄 안내를 둘 땐 `<p class="note">…</p>`.

---

## 4. 마크다운 → 디자인 대응표

| 마크다운 | 결과 |
|---|---|
| `# 제목` | 슬라이드 제목 (2색 블록 + 2색 줄) — 슬라이드당 1개 |
| `## 섹션` | navy 밑줄 섹션 헤딩 |
| `### 소제목` | 굵은 본문 크기 소제목 |
| `**굵게**` | 강조 |
| `*기울임*` | 회색 주석 — *(Optional)* 같은 부가 정보 |
| `<span class="navy">…</span>` / `<span class="muted">…</span>` | 대비 강조 |
| `> 인용` | 왼쪽 blue 선 인용 |
| `---` | 다음 슬라이드 |
| `![](./img/x.png)` | 이미지 — 덱 폴더의 `img/`에 둡니다 |
| `![bg right:40%](./img/x.png)` | Marp 기본 기능: 오른쪽 40%를 이미지로 채움 |

## 5. 하지 말 것

- 본문에 배경색 박스, 카드, 그림자, 둥근 모서리를 넣지 않습니다.
- peach 또는 blue를 글자색으로 쓰지 않습니다 (흰 배경에서 대비가 부족합니다).
- 슬라이드 하나에 `#` 제목을 두 개 쓰지 않습니다.
- 테마 CSS의 값을 직접 고치지 않습니다. `tokens/tokens.json`을 고치고 `npm run tokens`를 실행합니다.
- 로고 파일을 덱마다 넣지 않습니다. 로고는 테마에 들어 있습니다.

---

## 6. 토큰을 바꾸는 방법

1. `tokens/tokens.json`의 `$value`를 수정합니다.
2. `npm run tokens` → `tokens/tokens.css`와 `themes/causal-lab.css`의 `/* tokens:start */ … /* tokens:end */` 구간이 다시 생성됩니다. `assets/logo-*.png`도 이때 테마에 data URI로 들어갑니다.
3. 두 파일을 함께 커밋합니다. CI가 동기화 누락을 검사합니다.

## 7. 세로형 보고서

`reports/<주제>/index.html`은 슬라이드와 별도로 읽는 정적 보고서입니다. `reports/dataset-candidates/`가 첫 예시입니다.

- 색·서체는 공통 `tokens/tokens.css`를 참조합니다. 토큰과 Marp 테마를 변경하지 않습니다.
- 흰 본문, 검정 텍스트, navy 밑줄 섹션 제목, 제목 아래 peach | blue 반반 장식을 유지합니다.
- 표는 기존 blue 테두리와 굵은 열 제목을 사용합니다. 보고서에서는 전체 본문 폭을 쓰고 수치는 오른쪽 정렬합니다.
- 화면 본문은 17px, 표는 15px로 읽기 크기를 조정합니다. 모바일은 문서 폭을 유지하고 표 안에서 가로 스크롤합니다.
- A4 인쇄 CSS는 반복 표 헤더, 행 분할 방지, 데이터셋별 새 페이지를 지정합니다. 별도 PDF·Word 출력은 생성하지 않습니다.
- `scripts/build-index.mjs`가 보고서의 `index.html`·`report.css`와 공통 토큰만 `dist/`에 복사하고 자료 목록에 연결합니다.
