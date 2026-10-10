# OT 자료 보기·저장·수정 안내

## 자료 보기와 저장

- [Pages에서 OT 보기](https://causalinferencelab.github.io/data-still-does-not-speak/ot-live/): 하단 이전·다음 버튼 또는 방향키·Page Up/Down으로 이동합니다. Home은 첫 장, End는 마지막 장입니다.
- [PDF 저장](https://causalinferencelab.github.io/data-still-does-not-speak/ot-live/index.pdf): PDF 화면의 다운로드 버튼으로 저장할 수 있습니다.
- [GitHub에서 원본 내용 읽기](../slides/ot-live/index.md): 문서 형식이며, 발표 화면은 Pages에서 봅니다.
- HTML을 보관하려면 OT 화면에서 브라우저의 **페이지 다른 이름으로 저장 → 웹페이지, 전체**를 선택하고 HTML과 생성된 이미지 폴더를 함께 보관합니다.

공개 HTML은 읽기 전용입니다. 화면 텍스트 편집·행 추가·체크 변경 기능은 제공하지 않습니다.

## 수정 제안하기

1. 원본 저장소를 Fork하고, 본인 사본에서 작업 브랜치를 만듭니다. 기존 포크가 있으면 사용합니다.
2. `slides/ot-live/index.md`를 열고 연필 아이콘으로 내용을 수정합니다. 맨 위 설정과 슬라이드 구분선 `---`은 유지합니다.
3. **Commit changes**로 작업 브랜치에 저장하고 **Contribute → Open pull request**로 원본 `main`에 제안합니다.
4. 검토·병합 후 배포가 완료되면 Pages에 반영됩니다. PR을 여는 것만으로는 반영되지 않습니다.

자세한 화면별 절차는 [제출 안내](../CONTRIBUTING.md)를 참고하세요. 생성된 HTML·PDF는 직접 커밋하지 않습니다.

## 유지보수자 빌드

- 원본: `slides/ot-live/index.md`
- 전용 화면 스타일: `slides/ot-live/live.css`
- 생성 결과: `dist/ot-live/index.html`, `dist/ot-live/index.pdf`
- 전체 빌드: `npm run build`
- OT HTML만 다시 생성: `npm run build:ot-live` (기존 의존성이 설치된 환경)

화면 전용 CSS는 HTML 발표용입니다. PDF는 공통 Marp 테마로 생성하는 보조 출력입니다.

## 이름·LinkedIn·목표 한 줄

Google 폼으로 수집하고, 응답이 모이면 빌더가 한 번에 PR로 반영합니다. 폼 생성과 입력 링크 공유는 별도로 진행합니다. 자동 연동은 사용하지 않습니다.

- 이름과 목표 한 줄은 필수, LinkedIn은 선택 항목입니다.
- 폼에는 이름·목표와 선택한 LinkedIn 링크가 공개 GitHub·OT 자료에 반영됨을 안내합니다.
- 빌더는 이름을 가나다순으로 정렬하고, 인사 표와 목표 표를 함께 수정합니다.
- 폼 응답 시트 전체나 편집자용 링크는 공개 저장소에 올리지 않습니다.
- PR에는 의도한 변경만 포함합니다. 백업, `.DS_Store`, `dist/`, 이전 진행 메모는 커밋하지 않습니다.

## 현재 합의

자료 공유는 모임 2일 전 화요일 자정(24:00)까지, 기록 장소는 GitHub 레포지토리입니다. 카메라는 켜고 참여하며 챕터 오너 배정은 완료했습니다. 불참·지원과 연휴 주간 운영은 보류 상태로 추후 논의합니다.

## 기록 예시의 출처

10페이지 만족도 설문 기록은 프로젝트 LinkedIn 소개글의 사례를 설명용으로 재구성한 것입니다. 실제 분석 결과나 교재 연습문제의 정답이 아닙니다.
