import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 가상 데이터 생성
np.random.seed(42) # 결과의 재현성을 위한 시드 고정

# 총 10명의 피험자 (Subject)
subjects = np.repeat(np.arange(1, 11), 2) # 각 피험자별로 2개의 데이터 포인트 (Period 1, 2)

# 기간(Period) 변수: 10명의 피험자가 각각 Period 1과 2를 경험
periods = np.tile([1, 2], 10) # [1, 2] 패턴을 10번 반복

# 처리(Treatment) 및 순서 그룹(Sequence) 변수 생성
treatments = []
sequences = []
# 그룹 1 (A -> B), 피험자 1~5
for _ in range(5):
    treatments.extend(['A', 'B'])
    sequences.extend(['A->B', 'A->B'])
# 그룹 2 (B -> A), 피험자 6~10
for _ in range(5):
    treatments.extend(['B', 'A'])
    sequences.extend(['B->A', 'B->A'])

# 데이터프레임 생성
df = pd.DataFrame({
    'Subject': subjects,
    'Period': periods,
    'Sequence': sequences,
    'Treatment': treatments
})

# 가상의 반응값(통증 완화 점수) 생성
# 가정: 약물 A 효과=10, 약물 B 효과=12, 기간2 효과=-1, 개인차(랜덤)
treatment_effect = df['Treatment'].map({'A': 10, 'B': 12})
period_effect = df['Period'].map({1: 0, 2: -1}) # 2차 기간에 약간 피로 효과 가정
subject_random_effect = np.repeat(np.random.normal(0, 1.5, 10), 2) # 개인별 차이 (랜덤 효과)
noise = np.random.normal(0, 1, 20) # 순수 오차

df['Score'] = treatment_effect + period_effect + subject_random_effect + noise
df['Score'] = df['Score'].round(2)

print("=== 교차 설계 실험 데이터 (일부) ===")
print(df.head(6))

# 2. 혼합 효과 모형 분석
# 모형 정의:
# Score ~ Treatment + Period (고정 효과)
# groups=df['Subject'] (피험자별 개인차를 랜덤 효과로 처리)
model = smf.mixedlm("Score ~ Treatment + Period", data=df, groups=df["Subject"])
result = model.fit()

print("\n--- 혼합 효과 모형 분석 결과 ---")
print(result.summary())


# 한글 폰트 설정 (환경에 맞게 주석 해제 또는 변경)
plt.rc('font', family='Malgun Gothic') # Windows 예시
# plt.rc('font', family='AppleGothic') # macOS 예시
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

plt.figure(figsize=(18, 6)) # 전체 그래프 영역 크기 설정

# 1. 처리(Treatment)별 점수 분포 (Boxplot)
plt.subplot(1, 3, 1) # 1행 3열 중 첫 번째 위치
sns.boxplot(x='Treatment', y='Score', data=df)
plt.title('처리(진통제)별 통증 완화 점수')
plt.xlabel('진통제 종류')
plt.ylabel('점수 (Score)')

# 2. 기간(Period)별 점수 분포 (Boxplot)
plt.subplot(1, 3, 2) # 1행 3열 중 두 번째 위치
sns.boxplot(x='Period', y='Score', data=df)
plt.title('기간(Period)별 통증 완화 점수')
plt.xlabel('기간')
plt.ylabel('점수 (Score)')

# 3. 순서 그룹 및 기간에 따른 상호작용 그림 (Line Plot)
plt.subplot(1, 3, 3) # 1행 3열 중 세 번째 위치
sns.pointplot(data=df, x='Period', y='Score', hue='Sequence', 
              dodge=True, errorbar='sd', capsize=.1)
plt.title('순서 그룹별 기간에 따른 평균 점수 변화')
plt.xlabel('기간 (Period)')
plt.ylabel('평균 점수 (Mean Score)')
plt.legend(title='순서 그룹 (Sequence)')

plt.tight_layout() # 그래프 간 간격 자동 조절
plt.show()