import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 가상 데이터 생성
np.random.seed(42)
ad_budget = np.random.uniform(10, 100, 50)  # 광고 비용 (10 ~ 100)
sales = 2.5 * ad_budget + np.random.normal(0, 10, 50)  # 매출 (노이즈 추가)

# 데이터프레임 생성
data = pd.DataFrame({
    'Ad_Budget': ad_budget,
    'Sales': sales
})

# 데이터 시각화
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Ad_Budget', y='Sales')
plt.title("Ad Budget vs Sales")
plt.xlabel("Advertising Budget (in $1000s)")
plt.ylabel("Sales (in $1000s)")
plt.grid(True)
plt.show()

# 데이터 분리
X = data[['Ad_Budget']]  # 독립 변수
y = data['Sales']  # 종속 변수

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 모델 계수 확인
print(f"회귀 계수 (기울기): {model.coef_[0]:.2f}")
print(f"절편: {model.intercept_:.2f}")

# 예측
y_pred = model.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 실제 값과 예측 값 시각화
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.title("Actual vs Predicted Sales")
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.grid(True)
plt.show()
