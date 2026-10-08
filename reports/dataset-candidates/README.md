# 데이터셋 후보 소개

『데이터는 여전히 말하지 않는다』 러너를 위한 세 후보 소개입니다.

- 로컬: [index.html](index.html)을 브라우저에서 열기
- 공개: [GitHub Pages 보고서](https://causalinferencelab.github.io/data-still-does-not-speak/reports/dataset-candidates/)
- 구성: 배경 → 개괄적인 질문 → 전체 변수표 → 수치 분포 → 해석의 한계 → 출처·이용 조건

2026년 10월 8일 원본 전체에서 집계하고 독립 검증한 수치를 사용합니다. 결측·취소·반복 행을 유지했고 표준편차는 표본 표준편차입니다. 상세 분석 정의와 방법은 러너들이 결정합니다.

`index.html`은 정적 보고서, `report.css`는 화면·인쇄 스타일입니다. 색·글꼴은 공통 `tokens/tokens.css`를 참조합니다. HTML 본문을 직접 수정할 수 있습니다. PDF·Word 파일은 생성하지 않습니다.

`npm run build:reports`는 보고서 HTML·CSS와 공통 토큰만 `dist/`에 복사하고 목록을 갱신합니다. `npm run build`에도 같은 단계가 포함됩니다. 보고서 폴더의 원본 데이터나 기타 파일을 자동 복사하지 않습니다.
