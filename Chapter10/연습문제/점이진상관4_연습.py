import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 데이터 생성: 고객 만족도와 재구매 여부
data = {
    'customer_id': range(1, 26),
    'satisfaction_score': [78, 85, 62, 92, 58, 70, 88, 65, 75, 95, 45, 80, 50, 68, 82, 90, 60, 72, 98, 55, 79, 86, 63, 71, 89],
    'repeat_purchase':    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1] # 0: 재구매 안함, 1: 재구매 함
}
df = pd.DataFrame(data)

# Point-Biserial Correlation 계산
# 'repeat_purchase'가 이분형 변수, 'satisfaction_score'가 연속형 변수
correlation, p_value = pointbiserialr(df['repeat_purchase'], df['satisfaction_score'])

# 상관계수 결과 출력
print("점이진 상관관계 분석 결과")
print(f"상관계수:   {correlation:.3f}")
print(f"p-value:   {p_value:.3f}")

if p_value < 0.05:
    print("고객 만족도 점수와 재구매 여부 간에 유의미한 상관관계가 있습니다.")
else:
    print("고객 만족도 점수와 재구매 여부 간에 유의미한 상관관계가 없습니다.")

# 시각화: 고객 만족도 점수 분포와 재구매 여부
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='satisfaction_score', hue='repeat_purchase', kde=True, palette={0: 'orange', 1: 'blue'}, bins=10)
plt.title("고객 만족도 점수 분포와 재구매 여부", fontsize=15)
plt.xlabel("고객 만족도 점수", fontsize=12)
plt.ylabel("고객 수", fontsize=12)
plt.legend(labels=['재구매 안함', '재구매 함'], title='재구매 여부')
plt.show()

# 시각화: 고객 만족도 점수 vs 재구매 여부 (박스 플롯)
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='repeat_purchase', y='satisfaction_score', palette={0: 'orange', 1: 'blue'})
plt.title("고객 만족도 점수와 재구매 여부의 관계", fontsize=15)
plt.xlabel("재구매 여부 (0: 안함, 1: 함)", fontsize=12)
plt.ylabel("고객 만족도 점수", fontsize=12)
plt.xticks([0, 1], ['재구매 안함', '재구매 함'])
plt.show()

"""
문제:
어떤 회사에서 직원들의 월별 교육 프로그램 참여 시간과 분기별 성과 평가 결과(우수/보통) 사이의 관계를 분석하려고 합니다.
직원 25명을 대상으로 월별 평균 교육 참여 시간(시간)과 분기 성과 평가 결과(0: 보통, 1: 우수)를 조사했습니다.
수집된 데이터를 바탕으로 점이진 상관계수를 계산하고, 교육 참여 시간이 성과 평가에 영향을 미치는지 통계적으로 검정하세요.
또한, 분석 결과를 시각화하여 교육 프로그램의 효과를 직관적으로 파악할 수 있도록 하세요.

분석 요구사항:
1. 점이진 상관계수를 계산하여 교육 시간과 성과 평가 간의 상관관계 강도를 측정하세요.
2. 통계적 유의성 검정을 통해 상관관계가 유의미한지 판단하세요. (α = 0.05)
3. 히스토그램을 사용하여 교육 참여 시간의 분포를 성과 평가 결과별로 시각화하세요.
4. 박스플롯을 사용하여 성과 평가 결과에 따른 교육 참여 시간의 차이를 시각화하세요.
5. 분석 결과를 바탕으로 교육 프로그램의 효과에 대한 결론을 도출하세요.
"""

