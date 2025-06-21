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
ad_budget = np.random.uniform(100, 1000, 50)  # 광고비 (단위: 백만 원)
monthly_sales = ad_budget * 0.8 + np.random.normal(0, 50, 50)  # 매출 (단위: 백만 원)

# 데이터프레임 생성
data = pd.DataFrame({
    "Ad_Budget": ad_budget,
    "Monthly_Sales": monthly_sales
})

# 피어슨 상관계수 계산 (Pandas)
corr_pandas = data.corr().loc["Ad_Budget", "Monthly_Sales"]

# 피어슨 상관계수 및 p-value 계산 (Scipy)
corr_scipy, p_value = pearsonr(data["Ad_Budget"], data["Monthly_Sales"])

# 결과 출력
print(f"피어슨 상관계수 (Pandas): {corr_pandas:.3f}")
print(f"피어슨 상관계수 (Scipy): {corr_scipy:.3f}, p-value: {p_value:.3f}")

# 시각화
plt.scatter(data["Ad_Budget"], data["Monthly_Sales"], alpha=0.7)
plt.title("광고비와 매출 간의 관계")
plt.xlabel("광고비 (백만 원)")
plt.ylabel("월간 매출 (백만 원)")
plt.grid()
plt.show()
