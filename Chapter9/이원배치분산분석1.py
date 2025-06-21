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
np.random.seed(42)

# 치료 방법 및 연령대
treatment_methods = ['A', 'B', 'C']
age_groups = ['Teenager', 'Adult', 'Senior']

# 치료 효과 점수 생성
data = []
for treatment in treatment_methods:
    for age in age_groups:
        if treatment == 'A':
            mean = 70 if age == 'Teenager' else 65 if age == 'Adult' else 60
        elif treatment == 'B':
            mean = 75 if age == 'Teenager' else 70 if age == 'Adult' else 65
        else:  # treatment == 'C'
            mean = 65 if age == 'Teenager' else 60 if age == 'Adult' else 55
        scores = np.random.normal(mean, 10, 30)  # 각 조합당 30명 샘플
        data.extend([(treatment, age, score) for score in scores])

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['treatment', 'age_group', 'effectiveness'])

# Two-Way ANOVA
model = ols('effectiveness ~ C(treatment) + C(age_group) + C(treatment):C(age_group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("ANOVA Table:\n", anova_table)

# 시각화 (상호작용 효과)
sns.pointplot(data=df, x='age_group', y='effectiveness', hue='treatment', errorbar='sd', dodge=True)
plt.title('Interaction Effect of Treatment and Age Group on Effectiveness')
plt.ylabel('Effectiveness')
plt.xlabel('Age Group')
plt.legend(title='Treatment Method')
plt.show()
