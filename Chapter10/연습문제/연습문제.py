import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 데이터 생성
np.random.seed(42)
production_time = np.random.uniform(5, 20, 100)  # 생산 시간 (분)
defect_rate = 20 - (production_time * 0.8) + np.random.normal(0, 1, 100)  # 결함률 (%), 역관계 추가
