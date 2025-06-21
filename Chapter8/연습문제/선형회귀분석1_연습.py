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
dose = np.random.uniform(5, 50, 100)  # 약물 용량 (5 ~ 50mg)
effect = 2.0 * dose + np.random.normal(0, 10, 100)  # 치료 효과 (노이즈 추가)

# 데이터프레임 생성
data = pd.DataFrame({
    'Dose': dose,
    'Effect': effect
})

# 데이터 시각화
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Dose', y='Effect', color='blue', alpha=0.7)
plt.title("Dose vs Treatment Effect")
plt.xlabel("Dose (mg)")
plt.ylabel("Treatment Effect (Score)")
plt.grid(True)
plt.show()

# 데이터 분리
X = data[['Dose']]  # 독립 변수
y = data['Effect']  # 종속 변수

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
sns.scatterplot(x=y_test, y=y_pred, color='green', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', linewidth=2)
plt.title("Actual vs Predicted Treatment Effect")
plt.xlabel("Actual Effect")
plt.ylabel("Predicted Effect")
plt.grid(True)
plt.show()


"""
연습 문제: 약물 용량과 치료 효과 분석

문제 배경:
한 제약회사에서 새로운 진통제의 효과를 측정하기 위해 실험을 진행했습니다.
100명의 환자를 대상으로 각각 다른 용량(5mg ~ 50mg)의 약물을 투여하고, 
치료 효과를 점수(0~100점)로 측정했습니다.

문제 1: 데이터 탐색 및 시각화
- 약물 용량과 치료 효과 간의 관계를 산점도로 시각화하여 선형 관계가 있는지 확인하세요.
- 두 변수 간의 상관관계는 어떻게 나타나나요?

문제 2: 선형 회귀 모델링
- 약물 용량을 독립변수로, 치료 효과를 종속변수로 하는 선형 회귀 모델을 구축하세요.
- 회귀 방정식을 구하고, 회귀 계수와 절편의 의미를 해석하세요.

문제 3: 모델 성능 평가
- 구축한 모델의 성능을 평가하기 위해 다음 지표들을 계산하세요:
  * 평균 제곱 오차 (MSE)
  * 결정 계수 (R²)
- R² 값을 통해 모델이 데이터를 얼마나 잘 설명하는지 해석하세요.

문제 4: 예측 및 해석
- 25mg의 약물을 투여했을 때 예상되는 치료 효과는 얼마인가요?
- 실제값과 예측값을 비교하는 산점도를 그려 모델의 예측 성능을 시각적으로 평가하세요.

문제 5: 결과 해석 및 결론
- 약물 용량이 1mg 증가할 때마다 치료 효과는 얼마나 증가하나요?
- 이 모델을 바탕으로 제약회사에 어떤 권장사항을 제시할 수 있나요?


"""
