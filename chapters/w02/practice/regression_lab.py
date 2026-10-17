import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", app_title="2주차 · 회귀 직접 실행")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import statsmodels.formula.api as smf
    from data_io import read_csv

    return mo, pd, read_csv, smf


@app.cell
def _(mo):
    mo.md("""
    # 회귀 직접 실행

    회귀식을 수정하고 셀을 다시 실행한다. 계수와 신뢰구간, 분석에 쓴 행 수를 함께 본다.

    데이터: Buisson의 [BehavioralDataAnalysis](https://github.com/BuissonFlorent/BehavioralDataAnalysis/tree/1452368f9cc36e0a5292348598c49de11ef05672).
    저장소에 포함된 합성 학습 데이터를 사용한다. CSV에는 기온·매출 단위가 기재돼 있지 않다.
    """)
    return


@app.cell
def _(mo, read_csv):
    data_dir = mo.notebook_location() / "data"
    stand = read_csv(data_dir / "chap1-stand_data.csv")
    ads = read_csv(data_dir / "AirCnC_MnM_exercises_data.csv")
    return ads, stand


@app.cell
def _(mo):
    mo.md("""
    ## 1. 매출 · OLS

    `ols_formula`에 변수를 하나씩 추가한다.

    1. `icecream_sales ~ temps`
    2. `icecream_sales ~ temps + summer_months`
    3. `icecream_sales ~ temps + summer_months + iced_coffee_sales`

    기온 계수와 신뢰구간은 어떻게 달라지는가?
    """)
    return


@app.cell
def _():
    ols_formula = "icecream_sales ~ temps"
    return (ols_formula,)


@app.cell
def _(ols_formula, smf, stand):
    ols_fit = smf.ols(ols_formula, data=stand).fit()
    ols_coefficients = ols_fit.summary2().tables[1]
    return ols_coefficients, ols_fit


@app.cell
def _(mo, ols_coefficients, ols_fit):
    mo.vstack([
        mo.md(f"**분석 n:** {int(ols_fit.nobs):,} · **R²:** {ols_fit.rsquared:.4f}"),
        mo.ui.table(ols_coefficients.reset_index().round(3), selection=None),
        mo.md("계수는 선택한 변수들을 함께 넣었을 때의 연관성이다. 인과효과를 판단하려면 변수의 역할과 데이터 생성 과정을 검토해야 한다."),
    ])
    return


@app.cell
def _(mo):
    mo.md("""
    ## 2. 예약 여부 · 로지스틱 회귀

    광고 집행 기간(`period=1`)의 소득 관측 행으로 표본을 고정한다.
    `logit_formula`를 `bkd ~ ad`와 `bkd ~ ad + np.log(income)`으로 바꿔 비교한다.

    - `bkd`: 고려한 숙소의 예약 여부 · 0/1
    - `ad`: 광고 제공 여부 · 0/1
    - `income`: 소득. 분포가 치우쳐 있어 로그로 넣는다.

    소득 통제 전후 광고의 평균 한계효과(AME)는 어떻게 달라지는가?
    """)
    return


@app.cell
def _(ads):
    air_sample = ads.loc[ads["period"] == 1].dropna(subset=["bkd", "ad", "income"]).copy()
    return (air_sample,)


@app.cell
def _():
    logit_formula = "bkd ~ ad + np.log(income)"
    return (logit_formula,)


@app.cell
def _(air_sample, logit_formula, smf):
    # np는 회귀식 안의 np.log(income)을 평가할 때 사용한다.
    logit_fit = smf.logit(logit_formula, data=air_sample).fit(disp=False)
    assert logit_fit.mle_retvals["converged"], "회귀가 수렴했는지 확인한다."
    logit_ame = logit_fit.get_margeff(at="overall", dummy=True).summary_frame()
    return logit_ame, logit_fit


@app.cell
def _(logit_ame, logit_fit, mo):
    _display = logit_ame.rename(columns={
        "dy/dx": "AME (%p)", "Std. Err.": "SE (%p)",
        "Conf. Int. Low": "95% CI 하한 (%p)", "Cont. Int. Hi.": "95% CI 상한 (%p)",
    }).copy()
    _display[["AME (%p)", "SE (%p)", "95% CI 하한 (%p)", "95% CI 상한 (%p)"]] *= 100
    mo.vstack([
        mo.md(f"**분석 n:** {int(logit_fit.nobs):,} · 계수표의 `ad`는 광고 미제공→제공의 평균 확률 변화다."),
        mo.ui.table(_display.reset_index().round(3), selection=None),
        mo.md("소득 결측 행은 제외됐다. 광고 배정 방식과 고객의 반복 관측 여부는 확인할 수 없다. 이 표본의 조건부 연관성으로 읽는다."),
    ])
    return


if __name__ == "__main__":
    app.run()
