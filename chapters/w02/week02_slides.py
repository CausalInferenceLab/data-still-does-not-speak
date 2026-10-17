import marimo

__generated_with = "0.25.1"
app = marimo.App(
    width="full",
    app_title="2주차 · 분석과 행동 데이터",
    layout_file="layouts/week02_slides.slides.json",
    css_file="theme/marimo-slides.css",
)

with app.setup(hide_code=True):
    import marimo as mo

    # 데이터
    import pandas as pd
    import numpy as np

    # 시각화
    import altair as alt

    # 통계·회귀
    import scipy.stats as stats
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    import marimo_slide_kit as kit
    from practice.data_io import read_csv
    kit.configure()
    _study_theme = alt.theme.register("study_slides", enable=True)(lambda: {"config": {
        "font": "Apple SD Gothic Neo, Malgun Gothic, sans-serif",
        "axis": {"labelFontSize": 18, "titleFontSize": 20, "labelOverlap": True, "tickCount": 7},
        "legend": {"labelFontSize": 18, "titleFontSize": 20, "orient": "top"},
        "view": {"stroke": None},
    }})


@app.cell(hide_code=True)
def title():
    kit.cover("Part 1. 행동의 이해", subtitle="2주차 · 분석과 행동 데이터", note="데이터는 여전히 말하지 않는다")
    return


@app.cell(hide_code=True)
def framework():
    mo.vstack([
        mo.vstack([mo.md("# 인과·행동·데이터"), mo.mermaid(
                                """
                                %%{init: {"themeVariables": {"fontSize": "26px", "fontFamily": "Apple SD Gothic Neo, sans-serif"}}}%%
                                block-beta
                                  columns 3

                                  space A["행동"] space
                                  space F[" "] space
                                  B["인과관계 다이어그램"] space C["데이터"]

                                  A --- B
                                  B --- C
                                  C --- A

                                  style A fill:#F4B183,stroke:#002060,color:#002060,stroke-width:2px
                                  style B fill:#8FAADC,stroke:#002060,color:#002060,stroke-width:2px
                                  style C fill:#002060,stroke:#002060,color:#FFFFFF,stroke-width:2px
                                  style F fill:transparent,stroke:transparent
                                """
                            )], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def chapter_questions():
    mo.vstack([mo.md('# Ch1–2에서 다루는 질문\n\n| Ch1 · 분석과 의사결정 | Ch2 · 행동과 데이터 |\n| --- | --- |\n| 예측과 추론은 어떻게 다른가? | 개인 특성·인지와 감정·의도·행동·기업 행동 |\n| 교란은 결과 해석을 어떻게 바꾸는가? | 기록의 범주, 행동 무결성, 시간과 맥락 |\n| C마트 매출과 선호도 분석 | AirCnC 변수 분류와 광고 성과 분석 |\n'), mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1–2</p>')], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md("""
            ## Ch1 · 분석과 의사결정
            ### 1. **우리는 데이터로 무엇을 알고 싶은가?**

            - **예측(Prediction):** 관찰한 정보로 아직 모르는 결과를 예측한다.
            - **추론(Inference):** 모집단의 특성이나 변수 간 관계를 추정하고, 그 불확실성을 판단한다.

            무엇을 알고 싶은지에 따라 모델을 평가하고 결과를 해석하는 기준이 달라진다.
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md("""
            ### 2. **의사결정은 질문을 바꾼다**

            구매 가능성 예측은 수요 예상이나 업무 우선순위에 활용할 수 있다. 쿠폰을 보낼 대상을 고를 때는 쿠폰으로 바뀔 행동을 묻는다.

            - **예측의 질문:** 누가 구매할 가능성이 높은가?
            - **개입의 질문:** 누구에게 쿠폰을 주면 구매가 늘어나는가?

            **구매 가능성이 높은 고객과, 쿠폰 때문에 구매를 늘릴 고객은 반드시 같지 않다.**

            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def causal_comparison():
    mo.vstack([mo.md('# 3. 관찰한 차이와 알고 싶은 효과\n\n| 관찰한 차이 | 알고 싶은 효과 |\n| --- | --- |\n| 쿠폰을 받은 고객과 받지 않은 고객의 구매량 차이 | 같은 고객에게 쿠폰을 줬을 때와 주지 않았을 때의 구매량 차이 |\n\n같은 고객의 같은 구매 기회에서 두 경우를 동시에 볼 수는 없다.\n\n다른 고객과 비교할 때는 **원래 고객이 달랐던 영향과 쿠폰의 효과를 구분**해야 한다.\n'), mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>')], gap=0.5)
    return


@app.cell(hide_code=True)
def behavior_people():
    mo.vstack([
        mo.md('# 4. 사람과 환경이 맞물려 행동이 나타난다\n\n**행동 = 사람 × 환경**\n\n1. **여러 요인이 함께 작용한다**  \n   아이 장난감을 부모가 구매한다면, 사용자의 필요와 구매자의 예산·판단이 함께 작용한다.\n2. **같은 사람도 상황에 따라 다르게 행동한다**  \n   블랙프라이데이에 앞으로 살 물량까지 미리 구매했다면? **비축 구매(stockpiling)** 는 구매 시점을 바꾼다.\n'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def behavior_experience():
    mo.vstack([
        mo.md("""# 4. 경험·목적·상대에 따라 달라지는 선택

    3. **경험과 시간에 따라 사람도 변한다**  
       브랜드를 보고 처음 샀어도, 사용 후에는 다른 기준으로 재구매할 수 있다.
    4. **같은 목적을 다른 방식으로 해결한다**  
       판매자가 정한 경쟁 제품 밖에서도 선택한다. 다른 분야의 제품·서비스로 같은 목적을 해결할 수 있다.
    5. **타인의 반응을 예상한다**  
       선물을 고를 때는 내 취향뿐 아니라 상대가 어떻게 받아들일지도 고려한다.
    """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def boycott_discussion():
    _view = mo.md("""
    ### 5. **기업 이슈 이후 매출이 감소했다**

    **가상 상황:** 한 기업의 사회적 이슈가 알려진 뒤 불매운동이 일어났다. 다음 달, 해당 기업의 매출이 감소했다.

    - **예측:** 다음 달 매출을 예상하려면 어떤 자료가 더 필요한가?
    - **효과:** 매출 감소를 불매운동의 효과로 판단하려면 무엇과 비교해야 하는가?
    - **행동:** 참여 의사가 실제 구매 중단으로 이어졌는가? 대체재와 시간에 따라 반응은 달라졌는가?

    불매운동의 강도와 매출에 모두 영향을 준 요인도 살핀다.
    """)
    mo.vstack([
        mo.Html('<div class="mt-legacy-long">' + mo.as_html(_view).text + '</div>'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def confounding():
    mo.vstack([mo.md('# 6. 교란\n\n기존 구매 성향이 높은 고객에게 쿠폰을 더 많이 제공했다면?\n\n- 기존 구매 성향 → 쿠폰을 받을 가능성\n- 기존 구매 성향 → 이후 구매 가능성\n\n**관심 원인과 결과 모두에 영향을 주는 공통 요인**이 교란변수다.\n\n쿠폰을 받은 고객의 구매량이 더 많아도, 그 차이를 전부 쿠폰의 효과로 읽을 수는 없다.\n'), mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>')], gap=0.5)
    return


@app.cell(hide_code=True)
def ice_data():
    ice_stand_df = read_csv(mo.notebook_location() / "practice" / "data" / "chap1-stand_data.csv")
    ice_survey_df = read_csv(mo.notebook_location() / "practice" / "data" / "chap1-survey_data.csv")
    mo.vstack([
        mo.md("""# 7. C마트의 매출 데이터

    | 변수 | 기록 |
    | --- | --- |
    | icecream_sales | 일일 아이스크림 매출 |
    | temps | 해당 날짜의 기온 |
    | summer_months | 여름철 여부 · 0/1 |
    | iced_coffee_sales | 일일 아이스커피 매출 |

    CSV에는 기온·매출 단위가 기재돼 있지 않다. 저자는 여름철 매출 차이를 여름방학과 연결해 설명한다.
    """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return ice_stand_df, ice_survey_df


@app.cell(hide_code=True)
def _():
    ice_temp = mo.ui.checkbox(value=True, label="기온 포함")
    ice_summer = mo.ui.checkbox(value=False, label="여름 여부 포함")
    ice_coffee = mo.ui.checkbox(value=False, label="아이스커피 매출 포함")
    ice_xaxis = mo.ui.dropdown(options=["temps", "iced_coffee_sales", "summer_months"], value="temps", label="산점도 X축")
    mo.vstack([
        mo.vstack([
                mo.md("""
            ### 8. **매출 데이터 · 변수를 선택하고 결과를 비교해보자**

            **아이스크림 매출을 무엇으로 설명하려는가?** 변수를 넣거나 빼기 전에, 선택 이유와 예상되는 결과를 생각해보자.
            """),
                mo.hstack([ice_temp, ice_summer, ice_coffee], justify="start", gap=2),
                ice_xaxis,
                mo.md("산점도는 선택한 X축과 매출의 **원자료 관계**이고, 계수표는 체크한 설명변수를 **함께 포함한 OLS 결과**다. 둘은 같은 해석이 아닐 수 있다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return ice_coffee, ice_summer, ice_temp, ice_xaxis


@app.cell(hide_code=True)
def _(ice_coffee, ice_stand_df, ice_summer, ice_temp, ice_xaxis):
    _cols = []
    if ice_temp.value:
        _cols.append("temps")
    if ice_summer.value:
        _cols.append("summer_months")
    if ice_coffee.value:
        _cols.append("iced_coffee_sales")
    _df = ice_stand_df[["icecream_sales"] + _cols].dropna()
    _X = pd.DataFrame({"const": np.ones(len(_df))}, index=_df.index)
    for _col in _cols:
        _X[_col] = _df[_col]
    _fit = sm.OLS(_df["icecream_sales"], _X).fit()
    _ci = _fit.conf_int()
    _coef = pd.DataFrame({
        "Parameter": _fit.params.index,
        "Estimate": _fit.params.values,
        "Std. Error": _fit.bse.values,
        "t": _fit.tvalues.values,
        "p-value": _fit.pvalues.values,
        "95% CI lower": _ci[0].values,
        "95% CI upper": _ci[1].values,
    })
    for _c in ["Estimate", "Std. Error", "t", "95% CI lower", "95% CI upper"]:
        _coef[_c] = _coef[_c].map(lambda _v: f"{_v:,.3f}")
    _coef["p-value"] = _coef["p-value"].map(lambda _v: "< 0.001" if _v < 0.001 else f"{_v:.3f}")
    _labels = {"temps": "Temperature", "iced_coffee_sales": "Iced coffee sales", "summer_months": "Summer (0/1)"}
    _points = alt.Chart(ice_stand_df).mark_circle(size=32, opacity=0.35, color="#8FAADC").encode(
        x=alt.X(ice_xaxis.value + ":Q", title=_labels[ice_xaxis.value], scale=alt.Scale(zero=False)),
        y=alt.Y("icecream_sales:Q", title="Ice cream sales", scale=alt.Scale(zero=False)),
        tooltip=["temps:Q", "icecream_sales:Q", "summer_months:N", "iced_coffee_sales:Q"],
    ).properties(height=260, width=900, autosize={"type": "fit", "contains": "padding"})
    if ice_summer.value:
        _points = _points.encode(color=alt.Color("summer_months:N", title="Summer", scale=alt.Scale(domain=[0,1], range=["#8FAADC", "#F4B183"])))
    _formula = "icecream_sales ~ " + (" + ".join(_cols) if _cols else "1 (intercept only)")
    _notes = []
    if ice_temp.value and ice_coffee.value:
        _r = ice_stand_df["temps"].corr(ice_stand_df["iced_coffee_sales"])
        _notes.append(f"기온–아이스커피 매출 상관계수: **{_r:.6f}**. 두 변수를 함께 넣기 전후, 개별 계수와 표준오차가 어떻게 달라지는가?")
    if ice_summer.value:
        _notes.append("여름 여부를 포함하거나 제외한 모형의 계수·표준오차·적합도를 비교해보자. 차이를 무엇으로 설명할 수 있는가?")
    ice_analysis = {"formula": _formula, "n": int(_fit.nobs), "r2": _fit.rsquared, "adjusted": _fit.rsquared_adj, "coef": _coef, "notes": _notes}
    mo.vstack([
        mo.vstack([
                mo.md("# 8. 매출 데이터 · 산점도"),
                mo.hstack([ice_temp, ice_summer, ice_coffee, ice_xaxis], justify="start", gap=1),
                mo.md(f"**현재 모형:** {_formula}  \n**n:** {int(_fit.nobs):,} · **R²:** {_fit.rsquared:.4f} · **조정 R²:** {_fit.rsquared_adj:.4f}"),
                mo.as_html(_points),
                kit.note("산점도는 원자료의 관계다. 통제변수를 함께 포함한 계수는 다음 페이지에서 비교한다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return (ice_analysis,)


@app.cell(hide_code=True)
def ice_coefficients(ice_analysis, ice_coffee, ice_summer, ice_temp):
    mo.vstack([
        mo.vstack([
                mo.md("# 8. 매출 데이터 · 회귀계수"),
                mo.hstack([ice_temp, ice_summer, ice_coffee], justify="start", gap=1),
                mo.md(f"**현재 모형:** {ice_analysis['formula']} · **n:** {ice_analysis['n']:,}"),
                mo.ui.table(ice_analysis["coef"], selection=None, show_data_types=False, page_size=5, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def ice_model_comparison(ice_analysis):
    mo.vstack([
        mo.md("# 8. 매출 데이터 · 모형 비교"),
        mo.md("  \n".join(ice_analysis["notes"])) if ice_analysis["notes"] else mo.md("변수를 하나씩 추가하며 기온 계수와 신뢰구간이 어떻게 달라지는지 비교한다."),
        mo.md("**현재 모형의 R²:** " + f"{ice_analysis['r2']:.4f} · **조정 R²:** {ice_analysis['adjusted']:.4f}"),
        mo.md("계수·검정은 OLS 가정에 따른 값이다. 인과효과에는 변수의 역할과 데이터 생성 과정, 예측력에는 새 데이터에서의 검증이 필요하다."),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    ice_group = mo.ui.radio(options=["전체 응답자", "구매 경험자", "구매 미경험자"], value="전체 응답자", inline=True, label="분석할 응답자")
    mo.vstack([
        mo.vstack([
                mo.md("""
            ### 9. **설문 데이터 · 누구를 분석하는가?**

            | 변수 | 의미 |
            | --- | --- |
            | vanilla | 바닐라 선호도 · 0~25 |
            | chocolate | 초콜릿 선호도 · 0~25 |
            | shopped | C마트에서 아이스크림을 구매한 경험 여부 · 0/1 |

            **처음 생각과 검토** · 바닐라를 좋아하는 사람은 초콜릿도 좋아할까? 구매 경험이 있는 사람만 분석한다면 결과가 같을까? 그 집단을 선택하는 이유는 무엇인가?
            """),
                ice_group,
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return (ice_group,)


@app.cell(hide_code=True)
def _(ice_group, ice_survey_df):
    if ice_group.value == "구매 경험자":
        _df = ice_survey_df.loc[ice_survey_df["shopped"] == 1].copy()
    elif ice_group.value == "구매 미경험자":
        _df = ice_survey_df.loc[ice_survey_df["shopped"] == 0].copy()
    else:
        _df = ice_survey_df.copy()
    _df = _df.dropna(subset=["vanilla", "chocolate"])
    _fit = sm.OLS(_df["chocolate"], sm.add_constant(_df[["vanilla"]])).fit()
    _ci = _fit.conf_int()
    _coef = pd.DataFrame({
        "Parameter": _fit.params.index,
        "Estimate": _fit.params.values,
        "Std. Error": _fit.bse.values,
        "t": _fit.tvalues.values,
        "p-value": _fit.pvalues.values,
        "95% CI lower": _ci[0].values,
        "95% CI upper": _ci[1].values,
    })
    for _c in ["Estimate", "Std. Error", "t", "95% CI lower", "95% CI upper"]:
        _coef[_c] = _coef[_c].map(lambda _v: f"{_v:,.4f}")
    _coef["p-value"] = _coef["p-value"].map(lambda _v: "< 0.001" if _v < 0.001 else f"{_v:.3f}")
    _r = _df["vanilla"].corr(_df["chocolate"])
    _plot_df = _df.sample(n=min(2000, len(_df)), random_state=42)
    _points = alt.Chart(_plot_df).mark_circle(size=26, opacity=0.28, color="#8FAADC").encode(
        x=alt.X("vanilla:Q", title="Vanilla preference (0–25)", scale=alt.Scale(domain=[0,25])),
        y=alt.Y("chocolate:Q", title="Chocolate preference", scale=alt.Scale(domain=[0,26])),
        tooltip=["vanilla:Q", "chocolate:Q", "shopped:N"],
    )
    _line_df = pd.DataFrame({"vanilla": [0.0, 25.0]})
    _line_df["chocolate"] = _fit.params["const"] + _fit.params["vanilla"] * _line_df["vanilla"]
    _line = alt.Chart(_line_df).mark_line(color="#002060", strokeWidth=2).encode(x="vanilla:Q", y="chocolate:Q")
    _chart = (_points + _line).properties(height=260, width=900, autosize={"type": "fit", "contains": "padding"})
    ice_survey_analysis = {"n": len(_df), "plot_n": len(_plot_df), "coef": _coef}
    mo.vstack([
        mo.vstack([
                mo.md("# 9. 설문 데이터 · 표본과 산점도"),
                ice_group,
                mo.md(f"**분석 대상:** {ice_group.value} · **n:** {len(_df):,} · **r:** {_r:.4f} · **R²:** {_fit.rsquared:.4f}"),
                mo.as_html(_chart),
                kit.note(f"산점도는 고정 난수로 뽑은 {len(_plot_df):,}명. 회귀선·상관·계수표는 선택 집단 전체 {len(_df):,}명으로 계산한다. 25 초과 원값을 보존해 Y축은 26까지 표시했다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return (ice_survey_analysis,)


@app.cell(hide_code=True)
def survey_coefficients(ice_group, ice_survey_analysis):
    mo.vstack([
        mo.vstack([
                mo.md("# 9. 설문 데이터 · 선택한 집단의 회귀계수"),
                ice_group,
                mo.md(f"**분석 대상:** {ice_group.value} · **n:** {ice_survey_analysis['n']:,} · chocolate ~ vanilla"),
                mo.ui.table(ice_survey_analysis["coef"], selection=None, show_data_types=False, page_size=5, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
                mo.md("구매 여부로 대상을 제한했을 때 관계가 어떻게 달라지는가? 선택 집단의 관계를 전체 응답자에게 그대로 적용할 수 있는가?"),
                mo.accordion({"해석의 범위": kit.note("계수는 선택 집단의 연관성이다. 검정·신뢰구간은 OLS 가정을 따른다.")}),
            ], gap=0.5),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def launch_discussion():
    mo.vstack([mo.md('# 10. 초코+바닐라 아이스크림을 출시한다면\n\n**혼합 제품을 출시하면 C마트 전체 아이스크림 매출이 늘어날까?**\n\n- 선호도 사이의 관계가 혼합 제품의 실제 구매로 이어질까?\n- 구매 경험자의 관계를 전체 고객에게 적용해도 될까?\n- 신제품 매출이 늘어도 기존 제품 구매가 옮겨온 것일 수 있지 않을까?\n\n현재 자료에는 혼합 제품의 출시 결과가 없다.\n'), mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1</p>')], gap=0.5)
    return


@app.cell(hide_code=True)
def chapter_two():
    mo.vstack([
        mo.md('# Ch2 · 행동과 데이터의 연결\n\n분석에 쓰는 기록은 사람의 행동을 어떻게 나타내는가?\n\n- **개념:** 개인 특성, 인지·감정, 의도, 행동, 비즈니스 행동\n- **측정:** 기록의 의미, 행동 단위, 관찰 가능성, 시간과 맥락\n- **실습:** AirCnC 변수 분류와 광고 성과 분석\n'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 1. 개인 특성\n\n- 분석 기간에 거의 변하지 않거나 서서히 변하는 개인 정보\n- 연령·교육 수준뿐 아니라 성향·생활습관도 포함한다.\n- 세분화·페르소나는 개인 특성을 활용하는 방법이다. 특성 자체의 정의와 구분한다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 2. 인지와 감정\n\n생각·감정·신념·만족감처럼 그때의 마음속 상태다.\n\n| 개인 특성 | 인지·감정 |\n| --- | --- |\n| 평소 꼼꼼한 성향 | 이번 구매에 대한 만족감 |'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 3. 의도\n\n“다음 여행에는 M&M 숙소를 예약하겠다.”\n\n앞으로 특정 행동을 하려는 계획이다. 실제 예약 여부는 별도 기록으로 확인해야 한다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 4. 행동\n\n- 실제로 일어난 활동\n- “후기를 읽겠다”는 계획과 실제로 읽은 기록은 다르다.\n- 의도가 항상 실행으로 이어지지는 않는다. **Intention–action gap**.\n- 분석 목적에 따라 후기 탐색과 구매를 구분한다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.vstack([
                mo.md("### 5. **의도와 실행 · 항상 이어지는 것은 아니다**"),
                mo.mermaid("%%{init: {\"theme\":\"base\",\"themeVariables\":{\"fontFamily\":\"Pretendard, Apple SD Gothic Neo, sans-serif\",\"fontSize\":\"18px\",\"lineColor\":\"#91A3B8\",\"edgeLabelBackground\":\"#FFFFFF\"},\"flowchart\":{\"curve\":\"basis\",\"nodeSpacing\":32,\"rankSpacing\":44}}}%%\nflowchart TB\n I(\"의도<br/>나는 X를 할 것이다\") -. 항상 실행되지는 않음 .-> A(\"행동<br/>실제로 X를 함\")\nclassDef peach fill:#FCEBDA,stroke:#D5A676,color:#5A3B22,stroke-width:1.2px,rx:12,ry:12;\nclassDef blue fill:#EAF0FA,stroke:#A6B9D6,color:#243A59,stroke-width:1.2px,rx:12,ry:12;\nclassDef navy fill:#183552,stroke:#183552,color:#FFFFFF,stroke-width:1.2px,rx:12,ry:12;\nclass I blue;\nclass A navy;"),
                mo.md('의도와 실행은 별도 기록으로 확인한다.')
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 6. 기업도 행동한다\n\n- 광고 제공, CRM 활동, CS 매뉴얼 변경\n- 고객이나 다른 직원에게 영향을 주려는 조직·직원의 활동도 행동이다.\n- 고객 기록을 읽을 때 기업이 무엇을 언제 바꿨는지도 확인한다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 7. 조회가 늘어난 이유\n\n**가상 예:** 후기 페이지를 자동으로 노출한 뒤 조회 기록이 늘었다.\n\n이 기록을 고객이 자발적으로 후기를 찾아 읽은 행동으로 볼 수 있을까?\n\n같은 지표라도 생성 방식과 접점이 바뀌면 의미가 달라진다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    aircnc_ch2_df = read_csv(mo.notebook_location() / "practice" / "data" / "AirCnC_MnM_exercises_data.csv")
    mo.vstack([
        mo.vstack([mo.md('# 8. AirCnC 광고의 목표\n\n다음 숙소 예약 때 **Mansions & Manors(M&M)도 고려하게 만드는 광고**다.\n\n**합성 학습자료다. 행 수를 고유 고객 수로 읽지 않는다.**'), mo.accordion({"데이터 미리보기 · 처음 5행": mo.ui.table(aircnc_ch2_df.head(5), selection=None, page_size=2, show_data_types=False, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}), "데이터 설명": mo.md("[저자 데이터 설명](https://raw.githubusercontent.com/BuissonFlorent/BehavioralDataAnalysis/master/Exercises%20and%20solutions/AirCnC_MnM_exercises_data_description.txt)  · 합성 학습 데이터다. 행 수를 고유 고객 수로 해석하지 않는다.")})], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_ch2_df,)


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.vstack([
                mo.md("### 9. **AirCnC · 광고와 목표 고객행동**"),
                mo.mermaid("%%{init: {\"theme\":\"base\",\"themeVariables\":{\"fontFamily\":\"Pretendard, Apple SD Gothic Neo, sans-serif\",\"fontSize\":\"18px\",\"lineColor\":\"#91A3B8\",\"edgeLabelBackground\":\"#FFFFFF\"},\"flowchart\":{\"curve\":\"basis\",\"nodeSpacing\":32,\"rankSpacing\":44}}}%%\nflowchart LR\n X(\"광고 제공<br/>ad\") -->|평가할 관계에 대한 질문| Y(\"목표 고객행동<br/>무엇을 결과로 볼까?\")\nclassDef peach fill:#FCEBDA,stroke:#D5A676,color:#5A3B22,stroke-width:1.2px,rx:12,ry:12;\nclassDef blue fill:#EAF0FA,stroke:#A6B9D6,color:#243A59,stroke-width:1.2px,rx:12,ry:12;\nclassDef navy fill:#183552,stroke:#183552,color:#FFFFFF,stroke-width:1.2px,rx:12,ry:12;\nclass X peach;\nclass Y navy;"),
                mo.md('광고 제공과 목표 고객행동의 관계를 살핀다. 이 화살표만으로 인과효과가 확인된 것은 아니다.')
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 10. AirCnC · 세 가지 기록\n\n| 변수 | 기록 |\n| --- | --- |\n| ad | 고객에게 광고가 제공됐는가? · 0/1 |\n| mm | M&M 숙소를 고려했는가? · 0/1 |\n| bkd | 고려하던 숙소를 예약했는가? · 0/1 |\n\n**bkd는 M&M 숙소 예약만을 뜻하지 않는다.**'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_context():
    mo.vstack([
        mo.md("""# 11. AirCnC · 소득·기간·지역

    | 변수 | 기록 |
    | --- | --- |
    | income | 고객 소득 · 통화·기간·개인/가구 구분 미명시 |
    | period | 0: 광고 전 / 1: 광고 집행 기간 |
    | zip | 지역 그룹의 가공 ID · 1~40 |

    """),
        mo.Html('<p class="mt-source">Buisson · Ch2, AirCnC 변수 설명</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_observed_context(aircnc_ch2_df):
    mo.vstack([
        mo.md(f"""# 11. AirCnC · 소득 결측과 광고 시점

    **소득 결측:** {aircnc_ch2_df['income'].isna().sum():,}행 ({aircnc_ch2_df['income'].isna().mean():.1%})  
    **관측 소득:** 중앙값 {aircnc_ch2_df['income'].median():,.1f} · 최댓값 {aircnc_ch2_df['income'].max():,.1f}

    | 기간 | 광고 제공 행 | 해당 기간 전체 행 |
    | --- | ---: | ---: |
    | 광고 전 · period=0 | {int(aircnc_ch2_df.loc[aircnc_ch2_df['period']==0,'ad'].sum()):,} | {int((aircnc_ch2_df['period']==0).sum()):,} |
    | 광고 집행 · period=1 | {int(aircnc_ch2_df.loc[aircnc_ch2_df['period']==1,'ad'].sum()):,} | {int((aircnc_ch2_df['period']==1).sum()):,} |

    소득은 관측된 값의 분포다. 광고는 period=1에만 제공됐다.
    """),
        mo.Html('<p class="mt-source">Buisson · Ch2, AirCnC 학습 데이터</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 12. 행동 무결성\n\n중요한 사업 질문과 핵심 변수부터 검증한다.\n\n- 정의: 어떤 행동을 담은 변수인가?\n- 기록: 실제로 어떻게 생성됐는가?\n- 시점: 언제 일어난 행동인가?'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 13. 내용 범주와 인과 역할\n\n| 구분 | 확인할 것 |\n| --- | --- |\n| 내용 범주 | 개인 특성 / 인지·감정 / 의도 / 행동 / 비즈니스 행동 |\n| 인과 역할 | 원인·결과, 매개·조절, 교란, 기타 공변량 |\n\n인지·의도가 항상 매개는 아니다. 개인 특성이 항상 조절도 아니다. **인과 역할은 분석 질문과 관계에 따라 검토한다.**'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 14. AirCnC · 변수 분류\n\nad · mm · bkd · income · period · zip\n\n- 기록의 의미를 근거로 다섯 범주와 맥락으로 나눈다.\n- 이 자료에서 측정하지 않은 개념도 찾는다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    aircnc_categories = mo.ui.dictionary({
        _name: mo.ui.dropdown(
            options=["개인 특성", "인지·감정", "의도", "행동", "비즈니스 행동", "맥락(시간·지역)"],
            allow_select_none=True, label=_name,
        ) for _name in ["ad", "mm", "bkd", "income", "period", "zip"]
    })
    mo.vstack([
        mo.vstack([
                mo.md("### 15. **AirCnC · 변수 범주 선택 실습**"),
                aircnc_categories.vstack(),
                mo.md('ad·mm·bkd·income·period·zip의 기록 의미를 보고 선택한다.'),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_categories,)


@app.cell(hide_code=True)
def _(aircnc_categories):
    _reference = {"ad": "비즈니스 행동", "mm": "행동", "bkd": "행동", "income": "개인 특성", "period": "맥락(시간·지역)", "zip": "맥락(시간·지역)"}
    mo.vstack([
        mo.md("# 15. AirCnC · 내 분류와 참고 분류"),
        mo.accordion({"참고 분류": mo.vstack([
                mo.ui.table(pd.DataFrame([
                    {"변수": _name, "내 분류": aircnc_categories.value[_name] or "미선택", "참고 분류": _kind}
                    for _name, _kind in _reference.items()
                ]), selection=None, show_data_types=False, page_size=6, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
                mo.md("mm·bkd는 고객의 행동이고 ad는 비즈니스 행동이다. 인지·감정과 의도는 이 데이터에서 측정되지 않았다. mm은 숙소 고려 행동의 기록이며, 미래 예약 의향 응답과 구분한다. 이 분류만으로 교란·매개 같은 인과 역할이 정해지지는 않는다."),
            ])}),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 16. Observable · Individual\n\n- **Observable:** 고객 곁에 있다면 확인할 수 있는 구체적인 행동인가?\n- **Individual:** 개인 수준의 행동이 분명한가? 통계적 독립성을 뜻하지 않는다.\n\n집계 탈퇴율은 고객 구성만 바뀌어도 달라질 수 있다. 개인의 탈퇴 가능성과 구분한다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 17. Atomic · 행동의 실행 경로\n\n주소 변경: **웹 / 예약 과정 / 콜센터**\n\n같은 지표에 서로 다른 행동 경로가 묶여 있는지 살핀다. 경로를 나누거나 합칠 기준은 분석 목적이다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 18. 횟수와 간격\n\n- **Frequency:** 단위 시간당 행동 횟수. 하루·주·월의 기준을 맞춘다.\n- **Duration:** 행동 사이 간격, 사건 이후 경과 시간, 시간에 따른 효과의 감쇠\n\n하루 동안 3회와 한 달 동안 3회는 같은 ‘3회’가 아니다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 19. 순서와 생활 시간표\n\n- **Contiguity:** 행동의 순서·근접성과 접점 연결. 온라인 시도 후 전화한 경우와 바로 전화한 경우를 구분한다.\n- **Social schedules:** 평일·주말, 출퇴근, 현지 시간 등 생활 시간표\n\n같은 시각의 기록도 생활 일정에 따라 맥락이 다르다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 20. 행동 당시의 정보\n\n- 고객이 정보를 얻은 시점과 회사가 이를 안 시점은 다를 수 있다.\n- 그 행동을 한 순간, 해당 주체가 알 수 있던 정보로 해석한다.\n- 나중에 알려진 사실을 과거 판단에 거꾸로 넣지 않는다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 21. 기록이 없는 것과 하지 않은 것\n\n1. 기록이 없다.\n2. 행동할 기회가 없었다.\n3. 기회가 있었지만 하지 않았다.\n\n관측되지 않았다는 이유만으로 셋을 같은 ‘0’으로 묶지 않는다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 22. 광고 성과의 기준\n\n**누구의 어떤 행동을 어느 기간에 볼 것인가?**\n\nAirCnC의 목표는 M&M 고려다. 전체 예약, M&M 고려, M&M 예약을 같은 결과로 취급하지 않는다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md('# 23. 지표와 비교\n\n- **분자·분모:** 선택한 결과가 일어난 행 / 분석 대상 행\n- **비교집단:** 광고 제공 / 미제공\n- **기간:** 전체 기간 / 광고 집행 기간\n\n관찰된 차이가 광고 때문인지 판단하려면 광고 배정 방식과 집단 구성에 대한 정보가 더 필요하다.'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    def aircnc_calculate(data, outcome, period_only=False, income=False, zip_effect=False, considerers=False):
        _df = data.assign(bkd_mm=data["bkd"] * data["mm"])
        if period_only:
            _df = _df.loc[_df["period"] == 1]
        if considerers:
            _df = _df.loc[_df["mm"] == 1]
        _before = len(_df)
        _needed = [outcome, "ad"] + (["income"] if income else []) + (["zip"] if zip_effect else [])
        # shortcut: 소득 결측은 원본처럼 제외한다. 결측 메커니즘을 분석할 때 대체 방법을 검토한다.
        _df = _df.dropna(subset=_needed).copy()
        _summary = _df.groupby("ad")[outcome].agg(n="size", mean="mean").reset_index()
        # 이항 비율의 Wilson 95% 구간: 상수 결과에서도 0폭 구간을 피한다.
        _z = stats.norm.ppf(0.975)
        _denom = 1 + _z**2 / _summary["n"]
        _center = (_summary["mean"] + _z**2 / (2 * _summary["n"])) / _denom
        _half = _z * np.sqrt(_summary["mean"] * (1 - _summary["mean"]) / _summary["n"] + _z**2 / (4 * _summary["n"]**2)) / _denom
        _summary["lower"] = _center - _half
        _summary["upper"] = _center + _half
        _mix = _df.groupby("ad").agg(n=("ad", "size"), 소득_관측수=("income", "count"), 소득_평균=("income", "mean")).reset_index()
        _X = pd.DataFrame({"const": 1.0, "ad": _df["ad"].astype(float)}, index=_df.index)
        if income:
            # 소득은 심하게 치우쳐 있어 로그로 넣는다. 최솟값이 0보다 크다.
            _X["log_income"] = np.log(_df["income"])
        _separated = 0
        if zip_effect:
            # 분석 표본에서 결과가 한 값뿐인 지역은 더미가 완전 분리를 일으켜 계수가 발산한다.
            # 그런 지역은 기준 지역에 합치고 개수를 표시한다.
            _ct = pd.crosstab(_df["zip"], _df[outcome])
            _bad = set(_ct.index[(_ct == 0).any(axis=1)]) if _ct.shape[1] > 1 else set(_ct.index)
            _separated = len(_bad)
            _dummies = pd.get_dummies(_df["zip"], prefix="zip", dtype=float)
            _dummies = _dummies.drop(columns=[f"zip_{_z}" for _z in _bad if f"zip_{_z}" in _dummies.columns])
            if not _dummies.empty:
                _dummies = _dummies.iloc[:, 1:]  # 남은 지역 중 첫 번째를 기준 지역으로 둔다
            _X = pd.concat([_X, _dummies], axis=1)
        _formula = "logit(" + outcome + ") ~ ad" + (" + log(income)" if income else "")
        if zip_effect:
            _formula += " + zip 더미(기준 지역 제외" + (f", 결과가 한 값뿐인 지역 {_separated}개는 기준에 합침" if _separated else "") + ")"
        _message = ""
        _coef = pd.DataFrame(columns=["Parameter", "AME (%p)", "SE (%p)", "95% CI lower (%p)", "95% CI upper (%p)", "p-value", "로그 오즈 계수"])
        if len(_df) < max(5, _X.shape[1] + 2) or len(_summary) < 2 or (_summary["n"] < 2).any():
            _message = "표본 또는 비교집단이 부족해 회귀를 표시하지 않는다. 기간·표본·통제 선택을 완화해 다시 비교한다."
        elif _df[outcome].nunique() < 2:
            _message = "결과변수가 상수여서 회귀를 표시하지 않는다. mm=1로 제한하고 mm을 결과로 고르면 모두 1이다. 다른 결과변수나 전체 고객을 선택한다."
        elif np.linalg.matrix_rank(_X.to_numpy(dtype=float)) < _X.shape[1]:
            _message = "설명변수가 선형 종속이어서 개별 계수를 식별할 수 없다. 통제 선택을 줄여 비교한다."
        else:
            import warnings
            _shown = ["ad"] + (["log_income"] if income else [])
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    _model = sm.Logit(_df[outcome].astype(float), _X.astype(float))
                    _fit, _ok = None, False
                    # Newton이 지역 더미·log(income) 조합에서 진동하면 L-BFGS로 다시 맞춘다.
                    for _method in ("newton", "lbfgs"):
                        try:
                            _fit = _model.fit(disp=0, maxiter=1000, method=_method)
                        except Exception:
                            continue  # 특이 행렬 등 수치 오류는 다음 방법으로 넘긴다
                        _ok = bool(_fit.mle_retvals.get("converged", False)) and bool(np.isfinite(_fit.bse.loc[_shown]).all())
                        if _ok:
                            break
                    # 평균 한계효과: 0/1 변수(ad)는 0→1 이산 변화, 연속 변수는 미분. 확률 단위라 %p로 읽는다.
                    _me = _fit.get_margeff(at="overall", method="dydx", dummy=True).summary_frame() if _ok else None
            except Exception:
                _fit, _ok, _me = None, False, None
            if not _ok or _me is None or not np.isfinite(_me.loc[_shown, "dy/dx"]).all():
                _message = "로지스틱 회귀가 수렴하지 않았다. 표본이 작거나 지역 더미에서 완전 분리가 생기면 추정이 불안정하다. 통제·표본 선택을 완화해 비교한다."
            else:
                _z = stats.norm.ppf(0.975)
                _ame = _me.loc[_shown, "dy/dx"].values * 100
                _se = _me.loc[_shown, "Std. Err."].values * 100
                _coef = pd.DataFrame({
                    "Parameter": ["ad", "log(income)"][: len(_shown)],
                    "AME (%p)": _ame,
                    "SE (%p)": _se,
                    "95% CI lower (%p)": _ame - _z * _se,
                    "95% CI upper (%p)": _ame + _z * _se,
                    "p-value": _me.loc[_shown, "Pr(>|z|)"].values,
                    "로그 오즈 계수": _fit.params.loc[_shown].values,
                })
        return {"n": len(_df), "before": _before, "formula": _formula, "summary": _summary, "mix": _mix, "coef": _coef, "message": _message}

    def aircnc_chart(summary, title):
        _base = alt.Chart(summary).encode(
            x=alt.X("ad:N", title="광고 제공 (0=미제공, 1=제공)"),
            tooltip=["ad:N", "n:Q", alt.Tooltip("mean:Q", format=".2%"), alt.Tooltip("lower:Q", format=".2%"), alt.Tooltip("upper:Q", format=".2%")],
        )
        _bars = _base.mark_bar(size=70).encode(
            y=alt.Y("mean:Q", title=title, axis=alt.Axis(format="%"), scale=alt.Scale(domain=[0, 1])),
            color=alt.Color("ad:N", scale=alt.Scale(domain=[0, 1], range=["#8FAADC", "#F4B183"]), legend=None),
        )
        _intervals = _base.mark_rule(color="#002060", strokeWidth=2).encode(y="lower:Q", y2="upper:Q")
        return (_bars + _intervals).properties(height=250, width=900, autosize={"type": "fit", "contains": "padding"})

    return aircnc_calculate, aircnc_chart


@app.cell(hide_code=True)
def aircnc_first_chart(aircnc_calculate, aircnc_ch2_df, aircnc_chart):
    aircnc_first = aircnc_calculate(aircnc_ch2_df, "bkd")
    mo.vstack([
        mo.vstack([
                mo.md("# 24. 전체 예약률과 광고의 목표"),
                mo.md("**예약률이 떨어졌는데 광고는 성공일까?** 전체 기간의 ad별 bkd 평균을 비교한다."),
                mo.as_html(aircnc_chart(aircnc_first["summary"], "전체 예약률")),
                kit.note("막대는 집단 평균, 선은 Wilson 95% 신뢰구간이다. bkd는 고려한 숙소의 예약이며 M&M만의 예약은 아니다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_first,)


@app.cell(hide_code=True)
def aircnc_first_table(aircnc_first):
    mo.vstack([
        mo.vstack([
                mo.md("# 24. 전체 예약률 · 비교집단과 불확실성"),
                mo.ui.table(aircnc_first["summary"].rename(columns={"mean": "예약률", "lower": "95% CI 하한", "upper": "95% CI 상한"}), selection=None, show_data_types=False, format_mapping={"예약률": "{:.4f}", "95% CI 하한": "{:.4f}", "95% CI 상한": "{:.4f}"}, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
                mo.md("예약률은 0~1 비율이다. 이 차이가 광고의 목표 행동을 측정하는지 확인한다. 두 집단의 신뢰구간이 겹치는지만으로 차이의 유의성을 판정하지 않는다. 관찰된 차이를 광고의 인과효과로 단정할 수도 없다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    aircnc_outcome = mo.ui.radio(options={
        "bkd · 고려한 숙소의 예약(전체 예약) — 플랫폼 전체 예약을 평가한다": "bkd",
        "mm · M&M 숙소 고려 — 광고의 고려 유도 목표를 평가한다": "mm",
        "bkd_mm · M&M 숙소 예약 — 목표 숙소 예약을 평가한다": "bkd_mm",
    }, value="bkd · 고려한 숙소의 예약(전체 예약) — 플랫폼 전체 예약을 평가한다", label="결과변수")
    mo.vstack([
        mo.vstack([
                mo.md("""
            ### 25. **2단계 · 분석 의도에 맞는 결과변수 고르기**

            **bkd_mm = bkd × mm**이다. 두 값이 모두 1인 행만 M&M 예약으로 센다.

            """),
                aircnc_outcome,
                mo.md("광고 목표에 맞는 결과변수는 무엇인가?"),
                mo.accordion({"결과를 해석할 때": mo.md("전체 예약, M&M 고려, M&M 예약은 서로 다른 질문에 답한다. bkd_mm의 분모는 선택한 표본 전체이며 M&M 고려자 수가 아니다. 어떤 지표에서 방향이 달라도 모순인지 판단하기 전에 목표와 분모를 확인한다.")}),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_outcome,)


@app.cell(hide_code=True)
def _():
    aircnc_period = mo.ui.radio(options=["전체 기간 · 원본 해설", "광고 기간만(period=1) · 추가 점검"], value="전체 기간 · 원본 해설", label="비교 기간")
    mo.vstack([
        mo.vstack([
                mo.md("### 26. **3단계 · 비교 기간 고르기**\n\n광고는 period=1에만 제공됐다. 전체 기간 비교에는 광고 전 기간도 섞인다."),
                aircnc_period,
                mo.md("기간을 맞추면 집단 차이가 어떻게 달라지는가?"),
                mo.accordion({"결과를 해석할 때": mo.md("기간을 맞춰도 광고 배정과 고객 구성의 차이까지 해결된 것은 아니다.")}),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_period,)


@app.cell(hide_code=True)
def _():
    aircnc_income = mo.ui.checkbox(value=False, label="소득(income) 포함")
    aircnc_zip = mo.ui.checkbox(value=False, label="지역(zip) 고정효과 포함")
    mo.vstack([
        mo.vstack([
                mo.md("### 27. **4단계 · 통제변수와 결측 확인하기**\n\n소득을 넣으면 결측 행을 제외한다. 통제변수와 함께 분석 표본도 달라진다."),
                mo.hstack([aircnc_income, aircnc_zip], justify="start"),
                mo.md("계수 변화가 소득 통제 때문인지 표본 변화 때문인지 구분할 수 있는가?"),
                mo.accordion({"결과를 해석할 때": mo.md("소득 통제 전후에는 분석 행 수도 달라진다. 소득 결측으로 제외된 고객의 특성이 다르면 결과의 적용 범위도 달라질 수 있다. 지역(zip)은 범주형으로 처리해 기준 지역을 뺀 더미를 넣는다.")}),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return aircnc_income, aircnc_zip


@app.cell(hide_code=True)
def _():
    aircnc_sample = mo.ui.radio(options=["전체 고객", "M&M을 고려한 고객만(mm=1)"], value="전체 고객", label="분석 표본")
    mo.vstack([
        mo.vstack([
                mo.md("### 28. **5단계 · 표본 제한의 함정**\n\nmm은 광고 이후의 행동이다. mm=1로 표본을 제한하면 비교 대상이 달라진다."),
                aircnc_sample,
                mo.md("mm=1인 표본에서 mm을 결과로 고르면 모든 값이 1이 된다."),
                mo.accordion({"결과를 해석할 때": mo.md("사후 처치 변수로 표본을 선택하면 집단 구성이 달라질 수 있어 전체 고객 비교나 광고 효과와 같게 읽을 수 없다. mm=1 표본의 bkd_mm은 bkd와 같고, mm은 항상 1이다. 소득 관측 수·평균은 구성 차이를 살피는 단서이며, 평균이 비슷해도 선택편향이 없다는 증거는 아니다.")}),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return (aircnc_sample,)


@app.cell(hide_code=True)
def _(
    aircnc_calculate,
    aircnc_ch2_df,
    aircnc_chart,
    aircnc_income,
    aircnc_outcome,
    aircnc_period,
    aircnc_sample,
    aircnc_zip,
):
    aircnc_result = aircnc_calculate(
        aircnc_ch2_df, aircnc_outcome.value,
        period_only=aircnc_period.value.startswith("광고"),
        income=aircnc_income.value, zip_effect=aircnc_zip.value,
        considerers=aircnc_sample.value.startswith("M&M"),
    )
    mo.vstack([
        mo.md("# 29. AirCnC · 결과변수와 집단 평균"),
        mo.md(f"**기간:** {aircnc_period.value} · **표본:** {aircnc_sample.value}  \n**분석 n:** {aircnc_result['n']:,} · **결측 제외:** {aircnc_result['before']-aircnc_result['n']:,}행"),
        mo.hstack([aircnc_outcome, mo.as_html(aircnc_chart(aircnc_result["summary"], aircnc_outcome.value).properties(width=560, height=280))], widths=[1,1.6], justify="start", gap=1),
        kit.note("집단 평균과 Wilson 95% 신뢰구간. 통제변수를 포함한 회귀 추정치는 다음 페이지에 표시한다."),
        mo.Html('<p class="mt-source">Buisson · Ch2, AirCnC 학습 데이터</p>'),
    ], gap=0.5)
    return (aircnc_result,)


@app.cell(hide_code=True)
def aircnc_model(
    aircnc_income,
    aircnc_period,
    aircnc_result,
    aircnc_sample,
    aircnc_zip,
):
    mo.vstack([
        mo.vstack([
                mo.md("# 29. AirCnC · 통제변수와 회귀 추정치"),
                mo.hstack([mo.vstack([aircnc_income, aircnc_zip]), aircnc_period, aircnc_sample], widths=[0.9, 1.2, 1.1], justify="start", gap=1),
                kit.note(f"현재 모형: {aircnc_result['formula']} (상수항 포함)"),
                mo.md(f"**결측 제외 전 n:** {aircnc_result['before']:,} → **분석 n:** {aircnc_result['n']:,}"),
                mo.md(aircnc_result["message"]) if aircnc_result["message"] else mo.ui.table(aircnc_result["coef"].rename(columns={"95% CI lower (%p)": "95% 하한 (%p)", "95% CI upper (%p)": "95% 상한 (%p)"}), selection=None, show_data_types=False, page_size=2,
                    format_mapping={"AME (%p)": "{:.3f}", "SE (%p)": "{:.3f}", "95% 하한 (%p)": "{:.3f}", "95% 상한 (%p)": "{:.3f}", "로그 오즈 계수": "{:.3f}", "p-value": lambda v: "<0.001" if v < .001 else f"{v:.3f}"},
                    column_widths={"Parameter": 130, "AME (%p)": 110, "SE (%p)": 110, "95% 하한 (%p)": 150, "95% 상한 (%p)": 150, "p-value": 100, "로그 오즈 계수": 150}, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
                kit.note("AME는 " +"광고 미제공→제공의 평균 확률 변화(%p)다. 계수표는 ad와 선택한 log(income)을 표시하며 상수항·지역 더미는 생략한다."),
            ], gap=1),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_composition(aircnc_result):
    mo.vstack([
        mo.md("# 29. AirCnC · 광고 제공 여부별 평균"),
        mo.ui.table(aircnc_result["summary"].rename(columns={"mean": "결과 평균", "lower": "95% CI 하한", "upper": "95% CI 상한"}), selection=None, show_data_types=False, format_mapping={"결과 평균": "{:.4f}", "95% CI 하한": "{:.4f}", "95% CI 상한": "{:.4f}"}, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
        mo.md("평균은 0~1 비율이다. 평균표·차트·회귀는 모두 같은 분석 표본을 쓴다."),
        mo.Html('<p class="mt-source">Buisson · Ch2, AirCnC 학습 데이터</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_income_composition(aircnc_result):
    mo.vstack([
        mo.md("# 29. AirCnC · 소득 관측과 표본 구성"),
        mo.ui.table(aircnc_result["mix"].round(2), selection=None, show_data_types=False, style_cell=lambda _row, _column, _value: {"fontSize": "18px"}),
        mo.md("소득 평균은 관측된 소득만으로 계산한다. 소득 통제를 켜면 분석 표본의 모든 행에 소득이 있다."),
        mo.Html('<p class="mt-source">Buisson · Ch2, AirCnC 학습 데이터</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_model_limits():
    mo.vstack([
        mo.md("""# 29. AirCnC · 추정치가 말하는 범위

        - 결과변수가 0/1이므로 **로지스틱 회귀**를 쓴다. 막대의 집단 평균과 통제변수를 포함한 회귀는 구분한다.
        - **AME(%p)** 는 다른 변수를 그대로 둔 채 광고 미제공→제공일 때 결과 확률의 평균 변화다. 통제변수가 없으면 집단 평균 차이와 같다.
        - 표준오차·p-value·신뢰구간은 최대우도 추정의 대표본 근사에 따른 값이다.
        - 같은 고객의 반복 관측인지 식별할 ID가 없어 **관측 독립성을 확인하지 못했다.**
        - 광고 배정 방식이 데이터에 없다. 작은 p-value나 통제변수 추가만으로 광고의 인과효과를 주장할 수 없다.
        """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def aircnc_comparison(aircnc_ch2_df):
    _data = aircnc_ch2_df.assign(bkd_mm=aircnc_ch2_df["bkd"] * aircnc_ch2_df["mm"])
    _means = _data.groupby("ad")[["bkd", "mm", "bkd_mm"]].mean()
    _consider = _data.loc[_data["mm"] == 1].groupby("ad")["bkd"].mean()
    mo.vstack([
        mo.md(f"""# 30. AirCnC · 목표 지표에 따라 달라지는 평가

        **전체 기간 · 소득 미통제 · 전체 표본**의 광고 미제공→제공 비교다.

        | 지표 | 미제공 | 제공 |
        | --- | ---: | ---: |
        | M&M 고려율 | {_means.loc[0,'mm']:.3%} | {_means.loc[1,'mm']:.3%} |
        | M&M 예약률 | {_means.loc[0,'bkd_mm']:.3%} | {_means.loc[1,'bkd_mm']:.3%} |
        | 전체 예약률 | {_means.loc[0,'bkd']:.3%} | {_means.loc[1,'bkd']:.3%} |
        | M&M 고려자만의 예약률 | {_consider.loc[0]:.3%} | {_consider.loc[1]:.3%} |

        M&M 고려·예약과 플랫폼 전체 예약은 서로 다른 성과 지표다. M&M 고려자만의 비교는 광고 이후 행동으로 표본을 선택했다는 점도 다르다.

        합성 학습용 관찰 기록이다. 작은 평균 차이만으로 광고의 성공이나 인과효과를 확정할 수 없다.
        """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def cmart_evidence():
    mo.vstack([
        mo.md('# 31. C마트 · 관찰한 것과 아직 모르는 것\n\n| 현재 자료 | 확인할 수 있는 관계 | 추가로 필요한 근거 |\n| --- | --- | --- |\n| 일별 매출·기온·여름 여부·아이스커피 매출 | 변수 선택에 따른 아이스크림 매출의 조건부 연관성 | 새 제품 출시가 총매출을 바꾸는 효과 |\n| 바닐라·초콜릿 선호도와 구매 경험 | 분석 집단에 따라 달라지는 선호도 사이의 관계 | 혼합 제품의 구매 의향과 실제 구매 |\n\n**선호도 사이의 관계가 신제품 출시 효과를 직접 측정한 것은 아니다.**\n'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1–2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def cmart_comparison():
    mo.vstack([
        mo.md('# 32. 신제품 출시 효과를 판단할 비교\n\n**초코+바닐라 아이스크림을 출시하면 C마트 전체 아이스크림 매출이 늘어나는가?**\n\n- 결과는 신제품 판매량만이 아니라 **전체 아이스크림 매출**로 정한다.\n- 신제품 매출과 기존 제품 매출이 각각 어떻게 달라지는지 구분한다.\n- 출시 전후 차이에는 계절·고객 구성 등 다른 변화가 섞일 수 있다.\n- 출시한 경우와 출시하지 않은 경우를 비교할 방법과 관찰기간을 정한다.\n\n이는 현재 자료의 분석 결과가 아니라, 출시 효과를 확인하기 위해 추가로 설계할 비교다.\n'),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch1–2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def regression_code():
    mo.vstack([
        mo.md(r"""# 직접 실행 · 회귀 코드

        [공유 저장소](https://github.com/CausalInferenceLab/data-still-does-not-speak)를 내려받은 뒤, 저장소 루트에서 실행한다.
        실행 준비는 `chapters/w02/README.md`에서 확인한다.

        ```bash
        bash scripts/week02.sh lab
        ```

        1. 매출: 기온 → 여름 여부 → 아이스커피 매출 순서로 회귀식에 추가한다.
        2. 예약: 같은 표본에서 소득 통제 전후 광고의 AME를 비교한다.
        3. 계수·신뢰구간·분석 행 수를 함께 확인한다.

        """),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### A1. **부록 A-1 · 개인 특성, 인지·감정, 의도**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | 개인 특성 | 분석 기간에 거의 변하지 않는 개인의 배경 정보 | 같은 사람의 연령대와 교육 수준을 함께 기록 |
            | 인지·감정 | 마음속 생각과 느낌으로, 의도와는 구분하는 개념 | 숙소 이용 경험을 얼마나 만족스럽게 느꼈는지 |
            | 의도 | 앞으로 특정 행동을 하려는 계획이나 마음의 결심 | 다음 여행에는 M&M 숙소를 예약하겠다는 계획 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### A2. **부록 A-2 · 행동과 비즈니스 행동**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | 행동·행동 경향 | 직접 관찰하는 행동과 반복 기록에서 드러나는 경향 | 예약 완료를 기록하고 반복 이용 여부도 살펴보기 |
            | 비즈니스 행동·프로세스 | 고객 등에 영향을 주는 조직·직원의 행동과 절차 | 특정 고객에게 광고를 제공하거나 상담 절차를 바꾸기 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### B1. **부록 B-1 · Observable, Individual, Atomic**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | Observable · 관찰 가능 | 고객 곁에 있다면 실제로 확인할 수 있는 행동인가 | 마음이 바뀜과 예약 화면을 닫은 행동을 구별하기 |
            | Individual · 개인 수준 | 집계 지표를 만들기 전 개인별 행동이 분명한가 | 전체 취소율의 변화가 고객 구성 때문인지 살펴보기 |
            | Atomic · 행동 단위 | 한 지표에 묶인 행동의 실행 경로를 알고 있는가 | 정보 변경을 앱·예약 과정·상담 경로로 확인하기 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### B2. **부록 B-2 · 시간의 네 측면**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | Frequency · 빈도 | 같은 시간 단위에서 행동이 몇 번 일어났는가 | 월별 횟수를 비교할 때 달의 길이 차이 확인하기 |
            | Duration · 지속·경과 시간 | 행동 사이 간격이나 사건 이후 경과 시간이 얼마인가 | 정보 변경 후 다음 예약까지 걸린 시간을 살펴보기 |
            | Contiguity · 연속·연결 | 행동 간 시간적 간격·선후와 접점 연결은 어떠한가 | 온라인 변경을 먼저 시도했는지 상담부터 했는지 보기 |
            | Social schedules · 생활 시간표 | 일·통근·주말 같은 생활 시간표가 행동에 미치는 맥락 | 평일 출근 시간과 주말의 이용 행동을 나누어 살펴보기 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### C1. **부록 C-1 · 고객 집단과 분석 단위**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | 세분화 | 비슷한 특성이나 행동을 기준으로 사람들을 묶는 일 | 이용 빈도와 방문 목적에 따라 고객 집단을 나누기 |
            | 페르소나 | 고객 집단을 이해하려고 만드는 근거 있는 가상 인물 | 주요 집단의 목적·상황을 묶어 가상 고객상 만들기 |
            | 가구 · household | 생활·소비를 함께하는 단위로, 개인과 구분하는 개념 | 가구 소득과 개인 소득이 같은 단위인지 먼저 확인 |
            | 대표성 | 표본의 구성과 결과가 목표 집단을 얼마나 반영하는가 | 응답자의 연령 구성이 목표 고객 집단과 비슷한지 확인 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


@app.cell(hide_code=True)
def _():
    mo.vstack([
        mo.md(r"""
            ### C2. **부록 C-2 · 인과 역할과 공변량**

            | 용어 | 쉬운 뜻 | 예시 |
            | --- | --- | --- |
            | 매개 | 원인이 결과에 영향을 미치는 과정의 중간 요인 | 알림이 기억을 돕고 기억이 참여를 높인다는 가설 |
            | 조절 | 조건에 따라 원인과 결과의 관계가 달라지는 요인 | 알림 효과가 신규·기존 사용자에게 다른지 검토하기 |
            | 교란 | 관심 원인과 결과 둘 모두에 영향을 주는 공통 요인 | 기존 구매 성향이 쿠폰 수령과 구매에 모두 영향을 준다는 가설 |
            | 공변량 | 분석에 함께 넣는 변수로, 인과적 역할은 따로 확인 | 연령을 분석에 넣어도 역할이 자동 결정되지는 않음 |
            """),
        mo.Html('<p class="mt-source">Buisson · Behavioral Data Analysis, Ch2</p>'),
    ], gap=0.5)
    return


if __name__ == "__main__":
    app.run()
