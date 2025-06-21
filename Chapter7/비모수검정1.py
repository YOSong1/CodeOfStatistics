import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성 (A와 B 집단의 클릭률)
np.random.seed(42)
group_a = np.random.exponential(scale=1.0, size=30)  # 그룹 A: 비정규 분포
group_b = np.random.exponential(scale=1.5, size=35)  # 그룹 B: 비정규 분포

# 데이터 시각화
plt.figure(figsize=(10, 6))
sns.histplot(group_a, kde=True, color="blue", label="Group A", bins=15)
sns.histplot(group_b, kde=True, color="orange", label="Group B", bins=15)
plt.title("Distribution of Group A and Group B")
plt.xlabel("Click-Through Rate (CTR)")  # x축 라벨 추가
plt.ylabel("Frequency")  # y축 라벨 추가
plt.legend()
plt.show()

# Mann-Whitney U Test 수행
stat, p_value = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')
print(f"Mann-Whitney U Test 결과:\nU-통계량 = {stat}, p-값 = {p_value:.4f}")

# 해석
if p_value < 0.05:
    print("유의미한 차이가 있습니다. (귀무가설 기각)")
else:
    print("유의미한 차이가 없습니다. (귀무가설 채택)")
