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


# 샘플 데이터 생성
np.random.seed(42)
data = {
    'sales': np.concatenate([
        np.random.normal(100, 10, 30),  # A 유형
        np.random.normal(110, 15, 30),  # B 유형
        np.random.normal(105, 20, 30)   # C 유형
    ]),
    'type': ['A'] * 30 + ['B'] * 30 + ['C'] * 30
}

df = pd.DataFrame(data)

# SciPy로 ANOVA 수행
f_stat, p_value = f_oneway(
    df[df['type'] == 'A']['sales'],
    df[df['type'] == 'B']['sales'],
    df[df['type'] == 'C']['sales']
)
print(f"F-Statistic: {f_stat:.2f}, P-Value: {p_value:.4f}")

# Statsmodels로 ANOVA 수행
model = ols('sales ~ C(type)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# 시각화
sns.boxplot(x='type', y='sales', data=df)
plt.title('Sales Distribution by Advertisement Type')
plt.show()
