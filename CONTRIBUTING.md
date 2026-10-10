# 참여와 제출 안내

처음 GitHub을 사용한다면 [AI 튜터 안내](TUTOR.md)부터 시작하세요. 웹 화면만으로 제출할 수 있습니다.

## 역할별 작성 위치

아래 경로는 W03의 예시입니다. 실제 주차와 본인의 GitHub ID로 바꿉니다.

| 역할 · 자료 | 작성 위치 예시 | 시작점 |
| --- | --- | --- |
| 러너 · 연습문제 풀이 또는 사례 검토와 세 구간 기록 | `assignments/w03/<github-id>/README.md` | [과제 안내](assignments/README.md) · [러너 기록 템플릿](templates/runner-record.md) |
| 챕터 오너 · 핵심 개념과 주차 준비 자료 안내 | `chapters/w03/README.md` | [챕터 안내](chapters/README.md) · [챕터 노트 템플릿](templates/chapter-notes.md) |
| 발표자 · 선택 슬라이드 | `slides/w03-ch03/index.md` | [슬라이드 안내](SLIDES.md) · [덱 템플릿](templates/deck.md) |

러너는 챕터를 읽고 해당 주차에 지정된 연습문제 또는 사례를 다룬 뒤, 풀이·검토와 세 구간 기록을 함께 제출합니다. 구체적인 문제 번호나 사례가 아직 없으면 챕터 오너에게 확인하세요.

## GitHub 웹에서 제출하기

1. 원본 저장소의 **Fork**를 눌러 본인 계정에 사본을 만듭니다. 이미 포크가 있으면 그것을 사용합니다.
2. 본인 포크의 브랜치 메뉴에서 작업 브랜치를 만듭니다. 예: `w03-<github-id>`.
3. 역할에 맞는 템플릿 내용을 복사합니다. **Add file → Create new file**에서 위 표의 경로로 파일을 만들고 내용을 작성합니다. 이미 있는 파일은 그 파일을 편집합니다.
4. 저장하기 전에 아래 공개 확인 항목을 점검하고, 개인정보·비밀·비공개 데이터·허가 없는 교재 원문이 없으면 **Commit changes**로 현재 작업 브랜치에 저장합니다.
5. **Contribute → Open pull request** 또는 **Compare & pull request**를 엽니다. 대상(base)은 **원본 저장소의 `main`**, 출발(head)은 **본인 포크의 작업 브랜치**인지 확인합니다.
6. 비교 화면의 변경 파일 목록과 diff에서 본인 자료와 의도한 파일만 포함됐는지 확인하고 PR을 엽니다. 제목은 `[W03] GitHubID 러너 기록`처럼 적을 수 있습니다.

**과제 PR을 열면 제출 완료입니다.** 리뷰와 수정, main 병합, Pages 반영은 이후의 별도 단계입니다. PR을 연 것만으로 Pages에 게시되지는 않습니다.

수정 요청을 받으면 같은 포크의 같은 작업 브랜치에서 파일을 고치고 저장하세요. 기존 PR에 업데이트되므로 새 PR을 만들 필요가 없습니다. PR을 열 수 없으면 화면의 오류와 대상 저장소·브랜치를 확인하고, 권한이나 저장소 정책 문제는 담당자에게 문의하세요.

## 터미널을 이미 쓰는 사람을 위한 경로

Git과 인증이 이미 준비된 경우에만 사용하세요. `<github-id>`는 본인 ID로 바꿉니다. GitHub에서 먼저 본인 포크를 만들고, 그 포크를 clone합니다.

```sh
git clone https://github.com/<github-id>/data-still-does-not-speak.git
cd data-still-does-not-speak
git switch -c w03-<github-id>
```

아래 명령을 실행하기 전에 `<github-id>`를 모두 본인 ID로 바꿉니다. 편집기로 템플릿 내용을 본인의 `assignments/w03/<github-id>/README.md`에 복사해 작성한 뒤, 공개 확인 항목을 점검하고 작성한 파일만 지정합니다.

```sh
git add assignments/w03/<github-id>/README.md
git commit -m "W03 러너 기록"
git push origin w03-<github-id>
```

챕터 노트나 슬라이드를 작성했다면 `git add`에 그 파일의 정확한 경로를 지정합니다. `git add .`로 다른 변경을 함께 넣지 마세요. push 후 GitHub 웹에서 원본 `main`과 본인 포크의 작업 브랜치를 비교해 PR을 엽니다. 기존 PR을 수정할 때도 같은 브랜치에서 수정·커밋·push합니다.

## 공개 전에 확인하기

이 저장소와 PR은 공개됩니다. 폴더 이름으로 사용한 GitHub ID도 공개 계정 정보로 표시됩니다.

- 개인정보, 비밀 API 키, 비공개 고객·회사 데이터를 넣지 마세요.
- 허가 없이 교재 원문이나 스크린샷을 재배포하지 마세요. 문제 번호와 출처를 적고 자신의 풀이·요약을 작성합니다.
- AI를 활용했다면 실제 확인한 근거와 아직 확인하지 못한 내용을 구분하세요.
- 주차나 GitHub ID 자리표시자를 실제 값으로 바꾸고 변경 파일을 확인하세요.
