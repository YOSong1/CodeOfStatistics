import pandas as pd
import numpy as np
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(123)

# 참가자 및 시간대 정의
participants = list(range(1, 21))  # 20명의 참가자
months = ['Month1', 'Month2', 'Month3']

# 각 참가자의 체중 변화 데이터 생성
data = []
for participant in participants:
    initial_weight = np.random.normal(70, 5)  # 초기 체중 평균 70kg, 표준편차 5
    weights = [
        initial_weight,                        # Month1
        initial_weight - np.random.uniform(1, 3),  # Month2: 1~3kg 감소
        initial_weight - np.random.uniform(2, 5)   # Month3: 2~5kg 감소
    ]
    data.extend([(participant, months[i], weights[i]) for i in range(len(months))])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['participant', 'month', 'weight'])

# 반복 측정 ANOVA 수행
rm_anova = AnovaRM(data=df, depvar='weight', subject='participant', within=['month']).fit()
print(rm_anova)

# 시각화
sns.lineplot(data=df, x='month', y='weight', marker='o', errorbar=None)
plt.title('Weight Reduction Over Time')
plt.xlabel('Month')
plt.ylabel('Weight (kg)')
plt.show()

"""
========== 연습 문제 ==========

체중 감량 프로그램의 효과를 분석하는 반복측정분산분석 코드입니다.
동일한 참가자들이 3개월 동안 측정한 체중 변화를 분석합니다.

문제 1: 반복측정분산분석의 기본 개념을 설명하세요.
   - 반복측정분산분석(Repeated Measures ANOVA)과 일반 일원배치분산분석의 차이점을 설명하세요.
   - 반복측정설계(within-subject design)와 독립그룹설계(between-subject design)의 장단점을 비교하세요.
   - 이 예제에서 반복측정인자(within-subject factor)와 피험자(subject)를 식별하세요.
   - 반복측정분산분석을 사용하는 이유와 장점을 설명하세요.

문제 2: 결과 해석과 통계적 의미를 분석하세요.
   - F 통계량, 자유도, p-value의 의미를 설명하세요.
   - 시간에 따른 체중 변화가 통계적으로 유의한지 판단하세요.
   - 효과크기(effect size)의 개념과 중요성을 설명하세요.
   - 실제 체중 감량 프로그램의 효과를 어떻게 해석할 수 있는지 논의하세요.

문제 3: 구형성 가정(Sphericity Assumption)을 검증하세요.
   a) 구형성 가정의 개념과 중요성을 설명하세요.
   b) Mauchly의 구형성 검정을 수행하세요.
   c) 구형성 가정이 위배될 경우의 문제점을 설명하세요.
   d) Greenhouse-Geisser 보정과 Huynh-Feldt 보정을 적용하세요.
   e) 각 보정 방법의 차이점과 사용 기준을 설명하세요.

문제 4: 사후검정(Post-hoc Tests)을 수행하세요.
   a) 왜 사후검정이 필요한지 설명하세요.
   b) 대응표본 t-검정을 이용한 쌍별 비교를 수행하세요:
      - Month1 vs Month2
      - Month2 vs Month3  
      - Month1 vs Month3
   c) 본페로니 보정(Bonferroni correction)을 적용하세요.
   d) 터키의 HSD 검정(Tukey's HSD)을 적용하세요.
   e) 각 사후검정 방법의 장단점을 비교하세요.

문제 5: 효과크기를 계산하고 해석하세요.
   a) 부분 에타제곱(partial eta-squared)을 계산하세요.
   b) Cohen's d를 각 시점 간 비교에 대해 계산하세요.
   c) 효과크기의 크기별 해석 기준을 제시하세요.
   d) 통계적 유의성과 실질적 유의성의 차이를 설명하세요.

문제 6: 시각화를 확장하고 개선하세요.
   a) 개별 참가자의 변화 패턴을 보여주는 spaghetti plot을 그리세요.
   b) 상자 그림(box plot)을 이용해 각 시점별 분포를 비교하세요.
   c) 바이올린 플롯(violin plot)으로 분포와 밀도를 함께 표현하세요.
   d) 평균과 신뢰구간을 포함한 오차막대 그래프를 그리세요.
   e) 각 시각화 방법의 장점과 적절한 사용 상황을 설명하세요.

문제 7: 데이터의 기술통계와 분포를 분석하세요.
   a) 각 시점별 평균, 표준편차, 최솟값, 최댓값을 계산하세요.
   b) 정규성 검정(Shapiro-Wilk test)을 각 시점에 대해 수행하세요.
   c) 등분산성 검정(Levene's test)을 수행하세요.
   d) 이상치(outliers) 탐지와 처리 방안을 제시하세요.

문제 8: 누락 데이터 처리를 분석하세요.
   a) 데이터에 임의로 결측치를 생성하세요 (5-10%).
   b) 결측치가 반복측정분산분석에 미치는 영향을 분석하세요.
   c) 다양한 결측치 처리 방법을 적용하세요:
      - 완전 사례 분석(Complete Case Analysis)
      - 평균 대체(Mean Imputation)
      - 선형 보간(Linear Interpolation)
      - 다중 대체(Multiple Imputation)
   d) 각 방법의 결과를 비교하고 장단점을 논의하세요.

문제 9: 추세 분석(Trend Analysis)을 수행하세요.
   a) 선형 추세(linear trend) 검정을 수행하세요.
   b) 이차 추세(quadratic trend) 검정을 수행하세요.
   c) 다항식 대비(polynomial contrasts)를 적용하세요.
   d) 체중 감소 패턴이 선형적인지 비선형적인지 판단하세요.

문제 10: 혼합효과모델(Mixed Effects Model)과 비교하세요.
   a) 반복측정분산분석을 혼합효과모델로 재분석하세요.
   b) 고정효과(fixed effects)와 임의효과(random effects)를 설정하세요.
   c) 두 방법의 결과를 비교하고 차이점을 설명하세요.
   d) 혼합효과모델의 장점과 사용해야 하는 상황을 설명하세요.

문제 11: 검정력 분석(Power Analysis)을 수행하세요.
   a) 현재 연구의 검정력을 계산하세요.
   b) 원하는 검정력(0.8)을 얻기 위한 필요 표본 크기를 계산하세요.
   c) 효과크기별 필요 표본 크기를 비교하세요.
   d) 사전 검정력 분석의 중요성을 설명하세요.



"""


