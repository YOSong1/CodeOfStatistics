import pandas as pd
import numpy as np
from statsmodels.multivariate.manova import MANOVA
import seaborn as sns
import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)

# 생산 공정 (A, B, C)
processes = ['A', 'B', 'C']
num_samples = 50  # 각 공정당 샘플 수

data = {
    'process': np.repeat(processes, num_samples),
    'quality_score': np.concatenate([
        np.random.normal(85, 5, num_samples),  # A 공정: 평균 품질 점수 85
        np.random.normal(80, 5, num_samples),  # B 공정: 평균 품질 점수 80
        np.random.normal(90, 5, num_samples)   # C 공정: 평균 품질 점수 90
    ]),
    'defect_rate': np.concatenate([
        np.random.normal(5, 1, num_samples),  # A 공정: 평균 불량률 5%
        np.random.normal(6, 1, num_samples),  # B 공정: 평균 불량률 6%
        np.random.normal(4, 1, num_samples)   # C 공정: 평균 불량률 4%
    ])
}

df = pd.DataFrame(data)


