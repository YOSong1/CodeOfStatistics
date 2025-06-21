import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr

# 한글 폰트 설정 (환경에 맞게 설정)
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 예제 데이터 생성: 시험 점수와 합격 여부
data_exam = {
    'student_id': range(1, 21), # 학생 ID
    'test_score': [56, 75, 45, 71, 62, 50, 49, 90, 65, 85, 55, 78, 40, 68, 72, 51, 60, 80, 47, 92], # 시험 점수
    'pass_fail': [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1] # 합격 여부 (0=불합격, 1=합격) [cite: 192]
}
df_exam = pd.DataFrame(data_exam)

print("\n생성된 샘플 데이터 (시험 점수와 합격 여부):")
print(df_exam.head())

# 점-이계열 상관계수 및 p-value 계산
correlation_exam, p_value_exam = pointbiserialr(df_exam['pass_fail'], df_exam['test_score'])

# 상관계수 결과 출력
print("\n점-이계열 상관 분석 결과 (시험 점수와 합격 여부)")
print(f"상관계수: {correlation_exam:.2f}")
print(f"p-value: {p_value_exam:.4f}")

if p_value_exam < 0.05:
    print("시험 점수와 합격 여부 간에 유의미한 상관관계가 있습니다.")
else:
    print("시험 점수와 합격 여부 간에 유의미한 상관관계가 없습니다.")

# 시각화 1: 시험 점수 분포와 합격 여부 (히스토그램 및 KDE)
plt.figure(figsize=(12, 6))
sns.histplot(data=df_exam, x='test_score', hue='pass_fail', kde=True, 
             palette={0: 'red', 1: 'green'}, bins=10) # palette로 색상 지정
plt.title("시험 점수 분포와 합격 여부", fontsize=14)
plt.xlabel("시험 점수", fontsize=12)
plt.ylabel("학생 수", fontsize=12)
plt.legend(labels=['불합격', '합격'], title='합격 여부', loc='upper left') # 범례 추가
plt.show()

# 시각화 2: 시험 점수 vs 합격 여부 (박스 플롯)
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_exam, x='pass_fail', y='test_score', palette={0: 'red', 1: 'green'})
plt.title("시험 점수와 합격 여부의 관계", fontsize=14)
plt.xlabel("합격 여부 (0=불합격, 1=합격)", fontsize=12) # x축 레이블 수정
plt.ylabel("시험 점수", fontsize=12)
plt.xticks([0, 1], ['불합격 (0)', '합격 (1)']) # x축 눈금 레이블 명시
plt.show()    