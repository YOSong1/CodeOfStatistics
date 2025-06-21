import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 1. 데이터 생성
np.random.seed(42)

levels = ['A', 'B', 'C']
n_rep = 5  # 각 수준당 반복 횟수

true_means = {'A': 50, 'B': 55, 'C': 60}  # 각 수준별 실제 평균 가정
std_dev = 3  # 측정값의 분산(표준편차)

data = []
for level in levels:
    for _ in range(n_rep):
        value = np.random.normal(loc=true_means[level], scale=std_dev)
        data.append([level, value])

df = pd.DataFrame(data, columns=['ProcessTimeLevel', 'Measurement'])

# 2. 기술 통계 확인
desc_stats = df.groupby('ProcessTimeLevel')['Measurement'].describe()
print("===== 기술 통계 =====")
print(desc_stats, "\n")

# 3. 박스플롯 시각화
fig, ax = plt.subplots(figsize=(8, 6))
df.boxplot(by='ProcessTimeLevel', column='Measurement', grid=False, ax=ax)
plt.title('Boxplot of Measurements by ProcessTimeLevel')
plt.suptitle('')  # 자동으로 생성되는 상위 제목 제거
plt.xlabel('Process Time Level')
plt.ylabel('Measurement')
plt.show()

# 4. ANOVA 분석
model = ols('Measurement ~ C(ProcessTimeLevel)', data=df).fit()
anova_result = sm.stats.anova_lm(model, typ=2)

print("===== ANOVA 결과 =====")
print(anova_result)
