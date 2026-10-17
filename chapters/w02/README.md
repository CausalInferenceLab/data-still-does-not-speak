# W02 · 분석과 행동 데이터

Ch1–2의 개념을 C마트 매출·선호도와 AirCnC 광고 데이터로 살펴본다.

## 설치 없이 사용

[발표 보기](https://causalinferencelab.github.io/data-still-does-not-speak/w02/slides/) · [회귀 코드 실습](https://causalinferencelab.github.io/data-still-does-not-speak/w02/lab/)

이 변경이 main에 반영되고 GitHub Actions 배포가 끝나면 위 주소에서 사용할 수 있다. Python은 각자의 브라우저 안에서 실행된다. 체크박스를 바꿔 재계산하거나 실습 코드를 수정할 수 있다. 처음 열 때 Python과 패키지를 받으므로 인터넷 연결이 필요하다.

## 로컬 설치와 실행

macOS·Linux에서는 Git으로 내려받은 뒤 아래 스크립트를 실행한다.

```bash
git clone https://github.com/CausalInferenceLab/data-still-does-not-speak.git
cd data-still-does-not-speak
bash scripts/week02.sh slides
```

스크립트가 uv를 확인하고, 없으면 프로젝트의 `.tools/uv/`에 설치한다. Python·marimo·분석 패키지는 고정된 `uv.lock`으로 준비한다. 셸 프로필과 시스템 Python은 바꾸지 않는다.

회귀 코드를 수정하려면:

```bash
bash scripts/week02.sh lab
```

터미널에 표시된 URL을 연다. 발표 화면은 방향키로 이동하며 체크박스·표본 선택·변수 분류·표 검색을 사용할 수 있다. 실습 화면에서는 코드 셀을 고친 뒤 다시 실행한다.

Windows 또는 uv를 직접 사용할 경우, [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) 후 프로젝트 폴더에서:

```bash
cd chapters/w02
uv sync --frozen --python 3.11
uv run --frozen marimo run week02_slides.py
# 코드 실습은 별도 터미널에서
uv run --frozen marimo edit practice/regression_lab.py
```

## 직접 바꿔 볼 것

- **매출 OLS:** 기온 → 여름 여부 → 아이스커피 매출 순서로 회귀식에 추가한다. 기온 계수와 신뢰구간을 비교한다.
- **예약 여부 로지스틱 회귀:** `bkd ~ ad`와 `bkd ~ ad + np.log(income)`을 비교한다. 광고 집행 기간의 소득 관측 행 4,259개로 표본을 고정했다.
- 회귀식을 수정하고 해당 셀을 다시 실행한다. 계수·신뢰구간·분석 행 수를 함께 확인한다.

발표 자료에서는 소득 통제를 켜면 결측 행을 제외하므로 표본 수도 달라진다. 코드 실습에서는 같은 표본에서 회귀식만 바꾸어 비교한다.

## 데이터와 해석 범위

저자 제공 합성 학습 데이터다. `ad`는 광고 제공, `mm`은 M&M 숙소 고려, `bkd`는 고려하던 숙소의 예약 기록이다. `bkd * mm`을 M&M 예약 지표로 사용한다. 지역은 범주형으로 처리한다.

고객 ID와 광고 배정 방식은 제공되지 않는다. 행 수를 고유 고객 수로 읽거나, 관찰된 연관성을 광고의 인과효과로 확정할 수 없다. 소득 결측 행을 제외한 결과의 적용 범위도 살핀다.

출처: Florent Buisson, 『Behavioral Data Analysis』 Ch1–2 및 [저자 코드](https://github.com/BuissonFlorent/BehavioralDataAnalysis/tree/1452368f9cc36e0a5292348598c49de11ef05672).
데이터 파일과 해시는 [source-manifest.json](practice/source-manifest.json), 이용 조건은 [UPSTREAM-LICENSE](practice/UPSTREAM-LICENSE)에 있다.

## 확인

```bash
uv run --project chapters/w02 python chapters/w02/check_regression.py
```

이 명령은 회귀식 변경, 같은 표본의 비교, 수렴과 AME를 검사한다. 발표용 CSS는 `theme/marimo-slides.css`, 페이지 배치는 `layouts/week02_slides.slides.json`에서 관리한다.

## 웹 배포

GitHub Actions가 기존 Marp 자료를 만든 뒤 같은 Python 노트북을 WebAssembly HTML로 내보낸다. 발표는 `dist/w02/slides/`, 편집 가능한 코드 실습은 `dist/w02/lab/`에 생성된다. 기존 자료 목록에 두 링크가 추가된다.

로컬 빌드:

```bash
uv run --frozen --project chapters/w02 python scripts/build-week02.py
node scripts/build-index.mjs
```

`.marimo.toml`은 이 자료의 실행 설정이다. `.venv`, `.cache`, `.tools`와 개인 설정은 배포하지 않는다.
