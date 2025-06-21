import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, levene, shapiro, bartlett
from scipy import stats
import pandas as pd
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

# --- 1. 가상의 시험 점수 데이터 생성 ---
# 결과의 재현성을 위한 시드 고정
np.random.seed(999)

# 각 소프트웨어 버전 그룹별 시험 점수 생성 (각 그룹당 10명)
# Version A 그룹: 평균 75점, 표준편차 8
score_A = np.random.normal(loc=75, scale=8, size=10)

# Version B 그룹: 평균 82점, 표준편차 8
score_B = np.random.normal(loc=82, scale=8, size=10)

# Version C 그룹: 평균 77점, 표준편차 8
score_C = np.random.normal(loc=77, scale=8, size=10)

# 데이터프레임으로 구성하여 데이터 확인용
df_scores = pd.DataFrame({
    'Version A': score_A,
    'Version B': score_B,
    'Version C': score_C
})
