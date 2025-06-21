import numpy as np
import pandas as pd
from scipy.stats import f_oneway
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

# 공장별 품질 점수 샘플 (품질 점수: 0~100 사이 값)
factory_a = np.random.normal(85, 5, 40)  # 공장 A: 평균 85, 표준편차 5
factory_b = np.random.normal(90, 7, 40)  # 공장 B: 평균 90, 표준편차 7
factory_c = np.random.normal(88, 6, 40)  # 공장 C: 평균 88, 표준편차 6

# 데이터프레임 생성
data = {
    'quality_score': np.concatenate([factory_a, factory_b, factory_c]),
    'factory': ['A'] * 40 + ['B'] * 40 + ['C'] * 40
}
df = pd.DataFrame(data)

# ANOVA 분석 (SciPy 사용)
f_stat, p_value = f_oneway(
    df[df['factory'] == 'A']['quality_score'],
    df[df['factory'] == 'B']['quality_score'],
    df[df['factory'] == 'C']['quality_score']
)
print(f"F-Statistic: {f_stat:.2f}, P-Value: {p_value:.4f}")

# ANOVA 분석 (Statsmodels 사용)
model = ols('quality_score ~ C(factory)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Table:\n", anova_table)

# 시각화
sns.boxplot(x='factory', y='quality_score', data=df)
plt.title('Quality Score Distribution by Factory')
plt.ylabel('Quality Score')
plt.xlabel('Factory')
plt.show()

"""
   연습 문제

문제: 제조업체 품질관리 분석

한 제조업체에서 세 개의 다른 공장(A, B, C)에서 생산되는 제품의 품질을 비교하고자 합니다.
품질 점수는 0~100점 사이의 값으로 측정되며, 각 공장에서 40개의 제품을 무작위로 선택하여 
품질 점수를 측정하였습니다.

데이터 정보:
- 공장 A: 40개 제품, 품질 점수 평균 85점, 표준편차 5점
- 공장 B: 40개 제품, 품질 점수 평균 90점, 표준편차 7점  
- 공장 C: 40개 제품, 품질 점수 평균 88점, 표준편차 6점

분석 목표:
세 공장 간의 품질 점수에 유의한 차이가 있는지 일원배치 분산분석(One-way ANOVA)을 
통해 검정하시오.

분석 요구사항:
1. 귀무가설(H0): 세 공장의 품질 점수 평균이 모두 같다 (μA = μB = μC)
2. 대립가설(H1): 적어도 한 공장의 품질 점수 평균이 다르다
3. 유의수준: α = 0.05

분석 결과 해석:
1. F-통계량과 p-값을 계산하시오
2. 유의수준 0.05에서 귀무가설을 기각할지 채택할지 결정하시오
3. 박스플롯을 통해 각 공장별 품질 점수 분포를 시각화하시오
4. 분석 결과를 바탕으로 경영진에게 제시할 결론을 작성하시오

예상 결과:
- F-통계량이 유의수준보다 크면 공장 간 품질 차이가 존재함을 의미
- 박스플롯을 통해 각 공장별 품질 점수의 중심경향과 분산을 비교
- 사후 검정(Post-hoc test)을 통해 어느 공장 간에 차이가 있는지 추가 분석 가능


============================================================================
"""
