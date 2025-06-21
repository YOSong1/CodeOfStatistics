import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)
n_samples = 1000

# 독립 변수 생성
voltage = np.random.uniform(3.0, 5.0, n_samples)  # 전압 (3.0V ~ 5.0V)
current = np.random.uniform(10, 100, n_samples)  # 전류 (10mA ~ 100mA)
temperature = np.random.uniform(20, 80, n_samples)  # 온도 (20°C ~ 80°C)
production_speed = np.random.uniform(100, 500, n_samples)  # 생산 속도 (100 ~ 500 단위/시간)

# 품질 생성 (로지스틱 관계)
# logit의 임계값을 조정하여 양품과 불량이 고르게 분포되도록 설정
logit = -1 + 2 * (voltage - 4) + 0.02 * (80 - current) + 0.05 * (60 - temperature) - 0.005 * production_speed

# 확률 계산
probability = 1 / (1 + np.exp(-logit))  # 시그모이드 함수로 확률 계산

# 양품 비율을 70%, 불량 비율을 30%로 설정 (직접적인 확률 기반 할당)
# 양품 확률을 높게 조정하여 양품이 더 많이 생성되도록 합니다.
quality = (probability > 0.3).astype(int)  # 확률이 0.3보다 크면 양품, 0.3 이하로 불량

# 데이터프레임 생성
data = pd.DataFrame({
    'Voltage': voltage,
    'Current': current,
    'Temperature': temperature,
    'Production_Speed': production_speed,
    'Quality': quality
})

# 클래스 분포 확인
print("클래스 분포:")
print(data['Quality'].value_counts())

# 데이터 시각화
sns.pairplot(data, hue='Quality', diag_kind='kde', palette='Set1')
plt.suptitle("Pairplot of Features and Quality", y=1.02)
plt.show()

# 데이터 분리
X = data[['Voltage', 'Current', 'Temperature', 'Production_Speed']]  # 독립 변수
y = data['Quality']  # 종속 변수

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 로지스틱 회귀 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 모델 계수 출력
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
})
print("회귀 계수:")
print(coefficients)

print(f"절편: {model.intercept_[0]:.2f}")

# 예측
y_pred = model.predict(X_test)

# 분류 보고서 출력
print("\n분류 보고서:")
print(classification_report(y_test, y_pred))

# 혼동 행렬 시각화
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Defective', 'Good'], yticklabels=['Defective', 'Good'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ROC 곡선 시각화
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
