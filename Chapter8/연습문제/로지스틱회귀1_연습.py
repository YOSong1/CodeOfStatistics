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
n_samples = 300

age = np.random.uniform(20, 60, n_samples)  # 연령
income = np.random.uniform(20000, 80000, n_samples)  # 연소득
credit_score = np.random.uniform(300, 850, n_samples)  # 신용 점수

# 대출 승인 여부 생성 (로지스틱 관계)
loan_approval = (0.3 * age + 0.5 * (income / 1000) + 0.2 * (credit_score / 100)) > 50
loan_approval = loan_approval.astype(int)

# 데이터프레임 생성
data = pd.DataFrame({
    'Age': age,
    'Annual_Income': income,
    'Credit_Score': credit_score,
    'Loan_Approval': loan_approval
})

# 데이터 분포 시각화
sns.pairplot(data, hue='Loan_Approval', diag_kind='kde', palette='Set2')
plt.suptitle("Pairplot of Features and Loan Approval", y=1.02)
plt.show()

# 데이터 분리
X = data[['Age', 'Annual_Income', 'Credit_Score']]  # 독립 변수
y = data['Loan_Approval']  # 종속 변수

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 로지스틱 회귀 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 모델 평가
y_pred = model.predict(X_test)
print("분류 보고서:")
print(classification_report(y_test, y_pred))

# 혼동 행렬 시각화
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Rejected', 'Approved'], yticklabels=['Rejected', 'Approved'])
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

"""
  연습 문제                                      
======================================================================================

문제 1. 로지스틱 회귀의 기본 개념 (이론)
---------------------------------------
1-1) 로지스틱 회귀와 선형 회귀의 차이점을 설명하시오.
1-2) 로지스틱 회귀에서 사용되는 시그모이드 함수의 특징과 역할을 설명하시오.
1-3) 본 코드에서 종속변수가 이진 분류인 이유와 로지스틱 회귀가 적합한 이유를 설명하시오.

문제 2. 데이터 생성 및 전처리 (실습)
------------------------------------
2-1) 본 코드에서 대출 승인 여부를 결정하는 공식을 분석하고, 각 변수의 가중치를 설명하시오.
     공식: 0.3 * age + 0.5 * (income / 1000) + 0.2 * (credit_score / 100) > 50
2-2) 만약 샘플 수를 500개로 늘리고, 연령 범위를 18-65세로 확대한다면 코드를 어떻게 수정해야 하는가?
2-3) 새로운 독립변수 '직업 경력(years_experience)'을 추가하여 데이터를 재생성하는 코드를 작성하시오.

문제 3. 데이터 시각화 해석 (분석)
--------------------------------
3-1) Pairplot 결과를 통해 각 변수들 간의 관계와 대출 승인 여부에 미치는 영향을 분석하시오.
3-2) 어떤 변수가 대출 승인에 가장 큰 영향을 미치는지 시각적으로 판단하는 방법을 설명하시오.
3-3) 만약 특정 변수들 간에 강한 상관관계가 발견된다면 어떤 문제가 발생할 수 있는가?

문제 4. 모델 학습 및 예측 (실습)
-------------------------------
4-1) train_test_split에서 test_size=0.3으로 변경했을 때의 장단점을 설명하시오.
4-2) LogisticRegression() 모델에 추가할 수 있는 주요 하이퍼파라미터 3가지를 설명하시오.
4-3) 새로운 고객 데이터 [나이: 35, 연소득: 50000, 신용점수: 700]에 대한 대출 승인 확률을 예측하는 코드를 작성하시오.

문제 5. 모델 평가 지표 해석 (분석)
---------------------------------
5-1) 분류 보고서(Classification Report)에서 나타나는 정밀도(Precision), 재현율(Recall), F1-score의 의미를 설명하시오.
5-2) 대출 승인 모델에서 False Positive와 False Negative 중 어느 것이 더 위험한지 비즈니스 관점에서 설명하시오.
5-3) 혼동 행렬(Confusion Matrix) 결과를 해석하고, 모델 성능을 개선하기 위한 방안을 제시하시오.

문제 6. ROC 곡선 분석 (고급)
---------------------------
6-1) ROC 곡선에서 AUC(Area Under Curve) 값의 의미와 해석 방법을 설명하시오.
6-2) AUC가 0.5에 가까우면 어떤 의미이며, 1.0에 가까우면 어떤 의미인지 설명하시오.
6-3) 만약 비즈니스 요구사항이 "대출 부도 위험을 최소화"라면, ROC 곡선에서 어떤 임계값을 선택해야 하는가?


"""
