import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.multivariate.manova import MANOVA


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)

# 치료 방법(A, B, C)
treatment = ['A', 'B', 'C']
num_samples = 30  # 각 그룹당 샘플 수

data = {
    'treatment': np.repeat(treatment, num_samples),
    'blood_pressure': np.concatenate([
        np.random.normal(120, 10, num_samples),  # A 그룹
        np.random.normal(115, 10, num_samples),  # B 그룹
        np.random.normal(110, 10, num_samples)   # C 그룹
    ]),
    'blood_sugar': np.concatenate([
        np.random.normal(90, 5, num_samples),  # A 그룹
        np.random.normal(85, 5, num_samples),  # B 그룹
        np.random.normal(80, 5, num_samples)   # C 그룹
    ])
}

df = pd.DataFrame(data)

# MANOVA 수행
manova = MANOVA.from_formula('blood_pressure + blood_sugar ~ treatment', data=df)
print(manova.mv_test())

# 시각화
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df, x='treatment', y='blood_pressure')
plt.title('Blood Pressure by Treatment')
plt.show()

sns.boxplot(data=df, x='treatment', y='blood_sugar')
plt.title('Blood Sugar by Treatment')
plt.show()
