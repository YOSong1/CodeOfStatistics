import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 가상 데이터 생성
np.random.seed(42)
dose = np.random.uniform(5, 50, 100)  # 약물 용량 (5 ~ 50mg)
effect =2.0* dose + np.random.normal(0, 10, 100)  # 치료 효과 (노이즈 추가)

# 데이터프레임 생성
data = pd.DataFrame({
'Dose': dose,
'Effect': effect
})

# 생성된 데이터 확인 (처음 5개 행)
print("생성된 샘플 데이터 (처음 5개 행):")
print(data.head())