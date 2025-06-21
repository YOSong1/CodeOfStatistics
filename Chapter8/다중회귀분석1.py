import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 가상 데이터 생성
np.random.seed(42)
n_samples = 100

horsepower = np.random.uniform(50, 300, n_samples)  # 마력
mpg = np.random.uniform(10, 40, n_samples)          # 연비
year = np.random.uniform(2000, 2022, n_samples)     # 연식
price = 20000 + (horsepower * 50) - (mpg * 1000) + ((year - 2000) * 200) + np.random.normal(0, 5000, n_samples)

# 데이터프레임 생성
data = pd.DataFrame({
    'Horsepower': horsepower,
    'MPG': mpg,
    'Year': year,
    'Price': price
})

# 데이터 시각화
sns.pairplot(data)
plt.suptitle("Pairplot of Features and Price", y=1.02)
plt.show()

# 독립 변수와 종속 변수 분리
X = data[['Horsepower', 'MPG', 'Year']]  # 독립 변수
y = data['Price']                        # 종속 변수

# 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 다중 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 모델 계수 확인
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print("회귀 계수:")
print(coefficients)

print(f"절편: {model.intercept_:.2f}")

# 예측
y_pred = model.predict(X_test)

# 모델 평가
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"평균 제곱 오차 (MSE): {mse:.2f}")
print(f"결정 계수 (R^2): {r2:.2f}")

# 실제 값과 예측 값 비교 시각화
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title("Actual vs Predicted Car Prices")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.grid(True)
plt.show()
