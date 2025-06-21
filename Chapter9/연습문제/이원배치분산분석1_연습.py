import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(123)

# 공장 및 작업자 숙련 수준
factory = ['A', 'B', 'C']
skill_level = ['Low', 'High']

# 품질 점수 생성
data = []
for f in factory:
    for s in skill_level:
        scores = np.random.normal(85 if s == 'High' else 80, 5, 30)  # 고급 작업자가 평균 점수 높음
        data.extend([(f, s, score) for score in scores])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['factory', 'skill_level', 'quality_score'])

# Two-Way ANOVA
model = ols('quality_score ~ C(factory) + C(skill_level) + C(factory):C(skill_level)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("ANOVA Table:\n", anova_table)

# 시각화 (상호작용 효과)
sns.pointplot(data=df, x='factory', y='quality_score', hue='skill_level', errorbar='sd', dodge=True)
plt.title('Interaction Effect of Factory and Skill Level on Quality Score')
plt.ylabel('Quality Score')
plt.xlabel('Factory')
plt.legend(title='Skill Level')
plt.show()

"""
========== 연습 문제 ==========

공장별 작업자 숙련도에 따른 품질 점수를 분석하는 이원배치분산분석 코드입니다.
3개 공장(A, B, C)과 2개 숙련도 수준(Low, High)을 요인으로 하는 2×3 요인설계를 분석합니다.

문제 1: 이원배치분산분석의 기본 개념을 설명하세요.
   - 이원배치분산분석(Two-Way ANOVA)과 일원배치분산분석의 차이점을 설명하세요.
   - 주효과(Main Effect)와 상호작용효과(Interaction Effect)의 개념을 설명하세요.
   - 이 예제에서 두 요인(공장, 숙련도)과 종속변수(품질점수)를 식별하세요.
   - 요인설계의 장점과 실험계획법에서의 중요성을 설명하세요.

문제 2: ANOVA 결과표를 해석하세요.
   - 각 요인의 F 통계량, 자유도, p-value의 의미를 설명하세요.
   - 공장 주효과의 통계적 유의성을 판단하세요.
   - 숙련도 주효과의 통계적 유의성을 판단하세요.
   - 공장×숙련도 상호작용효과의 통계적 유의성을 판단하세요.
   - 각 결과가 실제 품질관리에 시사하는 바를 설명하세요.

문제 3: 분산분석의 가정을 검증하세요.
   a) 정규성 가정(Normality)을 검정하세요:
      - Shapiro-Wilk 검정을 각 그룹별로 수행하세요.
      - Q-Q plot을 그려 정규성을 시각적으로 확인하세요.
   b) 등분산성 가정(Homoscedasticity)을 검정하세요:
      - Levene의 등분산 검정을 수행하세요.
      - Bartlett 검정을 수행하세요.
   c) 독립성 가정(Independence)에 대해 설명하세요.
   d) 가정 위배 시 대안적 방법들을 제시하세요.

문제 4: 상호작용 효과를 자세히 분석하세요.
   a) 상호작용 플롯을 해석하세요:
      - 평행선과 교차선의 의미를 설명하세요.
      - 현재 그래프에서 상호작용의 존재 여부를 판단하세요.
   b) 단순주효과(Simple Main Effects) 분석을 수행하세요:
      - 각 공장별로 숙련도의 효과를 분석하세요.
      - 각 숙련도별로 공장의 효과를 분석하세요.
      - 상호작용의 실제적 의미를 해석하세요.

문제 5: 사후검정(Post-hoc Tests)을 수행하세요.
   a) 공장 요인에 대한 다중비교를 수행하세요:
      - Tukey's HSD 검정
      - Bonferroni 보정
      - Scheffe 검정
   b) 각 사후검정 방법의 특징과 적용 상황을 설명하세요.
   c) 상호작용이 유의한 경우의 사후검정 전략을 설명하세요.
   d) 단순비교(Simple Comparisons)를 수행하세요.

문제 6: 효과크기를 계산하고 해석하세요.
   a) 부분 에타제곱(Partial η²)을 각 효과에 대해 계산하세요.
   b) Cohen's f를 계산하세요.
   c) 오메가제곱(ω²)을 계산하세요.
   d) 효과크기의 실제적 의미와 해석 기준을 제시하세요.
   e) 통계적 유의성 vs 실제적 유의성을 비교하세요.

문제 7: 시각화를 확장하고 개선하세요.
   a) 상자그림(Box Plot)으로 각 조건별 분포를 비교하세요.
   b) 바이올린 플롯(Violin Plot)으로 분포와 밀도를 표현하세요.
   c) 히트맵(Heatmap)으로 평균값을 시각화하세요.
   d) 오차막대가 있는 막대그래프를 그리세요.
   e) 개별 데이터 포인트를 포함한 스트립 플롯을 그리세요.
   f) 각 시각화 방법의 장단점과 적절한 사용 상황을 설명하세요.

문제 8: 기술통계와 탐색적 데이터 분석을 수행하세요.
   a) 각 조건별 평균, 표준편차, 중앙값, 사분위수를 계산하세요.
   b) 그룹별 표본 크기와 균형설계 여부를 확인하세요.
   c) 이상치(Outliers) 탐지를 수행하세요:
      - IQR 방법
      - Z-score 방법
      - Modified Z-score 방법
   d) 상관분석을 통해 요인들 간의 관계를 분석하세요.

문제 9: 대비분석(Contrast Analysis)을 수행하세요.
   a) 계획된 대비(Planned Contrasts)를 설정하세요:
      - 공장 A vs (공장 B + 공장 C)
      - 공장 B vs 공장 C
   b) 직교대비(Orthogonal Contrasts)의 개념을 설명하세요.
   c) 각 대비의 통계적 유의성을 검정하세요.
   d) 대비분석과 사후검정의 차이점을 설명하세요.

문제 10: 검정력 분석(Power Analysis)을 수행하세요.
   a) 현재 연구의 사후 검정력을 계산하세요.
   b) 원하는 검정력(0.8, 0.9)을 얻기 위한 표본 크기를 계산하세요.
   c) 효과크기별 필요 표본 크기를 비교하세요.
   d) 균형설계 vs 불균형설계의 검정력 차이를 분석하세요.
   e) 사전 검정력 분석의 중요성을 설명하세요.

문제 11: 불균형 설계(Unbalanced Design)를 분석하세요.
   a) 데이터에서 일부 관측치를 임의로 제거하여 불균형 설계를 만드세요.
   b) Type I, Type II, Type III 제곱합의 차이를 설명하세요.
   c) 불균형 설계에서 적절한 제곱합 선택 기준을 제시하세요.
   d) 균형설계 vs 불균형설계의 장단점을 비교하세요.

문제 12: 비모수적 방법으로 분석하세요.
   a) Kruskal-Wallis 검정을 수행하세요.
   b) Friedman 검정을 적용해보세요.
   c) 순위변환 ANOVA(Rank-transformed ANOVA)를 수행하세요.
   d) 모수적 방법과 비모수적 방법의 결과를 비교하세요.
   e) 각 방법의 적용 조건과 장단점을 설명하세요.

문제 13: 베이지안 분석을 적용하세요.
   a) 베이지안 ANOVA를 수행하세요.
   b) 베이즈 팩터(Bayes Factor)를 계산하세요.
   c) 사후분포(Posterior Distribution)를 시각화하세요.
   d) 빈도주의 vs 베이지안 접근법의 차이점을 설명하세요.
   e) 베이지안 방법의 장점과 해석상의 이점을 설명하세요.

문제 14: 반복이 있는 이원배치분산분석으로 확장하세요.
   a) 각 조건에서 여러 번의 반복 측정 데이터를 생성하세요.
   b) 중첩 설계(Nested Design)와 교차 설계(Crossed Design)를 구분하세요.
   c) 반복 요인을 추가한 삼원분산분석을 수행하세요.
   d) 반복의 효과와 상호작용을 분석하세요.

"""
