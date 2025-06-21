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

# 데이터 생성
np.random.seed(42)
n_samples = 200

# 독립 변수 생성
material_quality = np.random.uniform(60, 100, n_samples)  # 원재료 품질 (60 ~ 100)
production_speed = np.random.uniform(50, 150, n_samples)  # 생산 속도 (50 ~ 150 제품/분)
environment_temperature = np.random.uniform(15, 35, n_samples)  # 환경 온도 (15 ~ 35°C)

# 종속 변수 생성 (제품 품질 점수)
product_quality = (
    0.5 * material_quality - 
    0.2 * production_speed - 
    1.5 * (environment_temperature - 25) + 
    np.random.normal(0, 5, n_samples)  # 노이즈 추가
)

# 데이터프레임 생성
data = pd.DataFrame({
    'Material_Quality': material_quality,
    'Production_Speed': production_speed,
    'Environment_Temperature': environment_temperature,
    'Product_Quality': product_quality
})

# 데이터 시각화
sns.pairplot(data)
plt.suptitle("Pairplot of Manufacturing Features", y=1.02)
plt.show()

# 데이터 분리
X = data[['Material_Quality', 'Production_Speed', 'Environment_Temperature']]  # 독립 변수
y = data['Product_Quality']  # 종속 변수

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
plt.title("Actual vs Predicted Product Quality")
plt.xlabel("Actual Quality")
plt.ylabel("Predicted Quality")
plt.grid(True)
plt.show()

"""
========== 연습 문제 ==========

제조업 데이터를 활용한 다중회귀분석 코드입니다.
원재료 품질, 생산 속도, 환경 온도가 제품 품질에 미치는 영향을 분석합니다.

문제 1: 다중회귀분석의 기본 개념을 설명하세요.
   - 단순회귀분석과 다중회귀분석의 차이점을 설명하세요.
   - 다중회귀분석의 수학적 모델 (y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε)에서 각 요소의 의미를 설명하세요.
   - 이 예제에서 독립변수와 종속변수를 식별하고, 각각의 의미를 해석하세요.
   - 다중회귀분석을 사용하는 이유와 장점을 설명하세요.

문제 2: 회귀계수의 해석을 수행하세요.
   - 각 독립변수의 회귀계수가 양수/음수인 이유를 실제 제조 상황과 연결하여 설명하세요.
   - 원재료 품질이 1단위 증가할 때 제품 품질의 변화량을 해석하세요.
   - 생산 속도 계수가 음수인 이유를 제조업 관점에서 설명하세요.
   - 환경 온도와 제품 품질의 관계를 해석하세요 (최적 온도 25°C 기준).

문제 3: 모델 성능 평가를 확장하세요.
   a) 현재 계산된 MSE와 R² 외에 추가로 다음 지표들을 계산하세요:
      - RMSE (Root Mean Square Error)
      - MAE (Mean Absolute Error)
      - 조정된 R² (Adjusted R²)
   b) 각 평가 지표의 의미와 해석 방법을 설명하세요.
   c) 훈련 데이터와 테스트 데이터에서의 성능을 비교하여 과적합 여부를 판단하세요.

문제 4: 다중공선성을 분석하세요.
   - 독립변수들 간의 상관계수 행렬을 계산하고 히트맵으로 시각화하세요.
   - VIF (Variance Inflation Factor)를 계산하여 다중공선성을 확인하세요.
   - 다중공선성이 회귀분석에 미치는 영향을 설명하세요.
   - 다중공선성이 발견될 경우의 해결 방법을 제시하세요.

문제 5: 잔차 분석을 수행하세요.
   a) 잔차(residuals)를 계산하고 다음 플롯들을 그리세요:
      - 잔차 vs 예측값 플롯
      - 잔차 vs 각 독립변수별 플롯
      - 잔차의 히스토그램
   b) Q-Q 플롯을 그려 잔차의 정규성을 확인하세요.
   c) 잔차 플롯을 통해 모델의 가정 위반 여부를 진단하세요.

문제 6: 특성 선택(Feature Selection)을 수행하세요.
   a) 전진 선택법(Forward Selection)을 구현하세요.
   b) 후진 제거법(Backward Elimination)을 구현하세요.
   c) 단계별 선택법(Stepwise Selection)을 적용하세요.
   d) 각 방법의 결과를 비교하고 최적의 특성 조합을 선택하세요.

문제 7: 데이터 전처리의 영향을 분석하세요.
   a) 독립변수들을 표준화(Standardization)한 후 모델을 다시 학습시키세요.
   b) 독립변수들을 정규화(Min-Max Normalization)한 후 모델을 학습시키세요.
   c) 전처리 전후의 회귀계수와 모델 성능을 비교하세요.
   d) 언제 표준화/정규화가 필요한지 설명하세요.

문제 8: 교차검증을 적용하세요.
   - K-fold 교차검증(k=5)을 수행하여 모델의 안정성을 평가하세요.
   - 각 fold별 성능 지표(R², MSE)를 계산하고 평균과 표준편차를 구하세요.
   - 홀드아웃 검증과 교차검증 결과를 비교하세요.
   - 교차검증의 장점과 단점을 설명하세요.

문제 9: 이상치 탐지와 처리를 수행하세요.
   a) Cook's Distance를 계산하여 영향력이 큰 관측치를 찾으세요.
   b) 표준화 잔차를 이용해 이상치를 탐지하세요.
   c) 이상치를 제거한 후 모델을 다시 학습시키고 성능 변화를 분석하세요.
   d) 이상치 처리의 다양한 방법들을 제시하세요.

문제 10: 다항 특성과 상호작용 항을 추가하세요.
   a) 2차 다항 특성(polynomial features)을 추가한 모델을 만드세요.
   b) 독립변수들 간의 상호작용 항(interaction terms)을 추가하세요.
   c) 원래 모델과 확장된 모델의 성능을 비교하세요.
   d) 과적합을 방지하기 위한 정규화 기법(Ridge, Lasso)을 적용하세요.

문제 11: 다중회귀분석의 가정을 검증하세요.
   a) 선형성 가정: 각 독립변수와 종속변수의 선형 관계 확인
   b) 독립성 가정: 더빈-왓슨 검정(Durbin-Watson test) 수행
   c) 등분산성 가정: 브로이쉬-페이건 검정(Breusch-Pagan test) 수행
   d) 정규성 가정: 샤피로-윌크 검정(Shapiro-Wilk test) 수행
   각 가정이 위배될 때의 해결 방법을 제시하세요.

문제 12: 예측 구간과 신뢰 구간을 계산하세요.
   - 새로운 데이터 포인트에 대한 95% 예측 구간을 계산하세요.
   - 회귀계수들의 95% 신뢰구간을 계산하세요.
   - 예측 구간과 신뢰 구간의 차이점을 설명하세요.
   - 구간 추정의 실제 활용 방안을 제시하세요.


"""