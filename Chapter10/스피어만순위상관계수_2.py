import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 데이터 생성
data = pd.DataFrame({
    "Drug_Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # 약물 효능 기대치 순위
    "Effectiveness_Rank": [1, 3, 2, 5, 4, 6, 8, 7, 10, 9]  # 약물 실제 효과 순위 (임상 결과)
})

# 스피어만 순위 상관계수 계산
spearman_corr, p_value = spearmanr(data["Drug_Rank"], data["Effectiveness_Rank"])

# 결과 출력
print(f"스피어만 순위 상관계수: {spearman_corr:.3f}")
print(f"p-value: {p_value:.3f}")

# 데이터 시각화
plt.scatter(data["Drug_Rank"], data["Effectiveness_Rank"], alpha=0.7)
plt.title("약물 순위와 효과 순위 간의 관계")
plt.xlabel("약물 효능 기대치 순위")
plt.ylabel("약물 실제 효과 순위")
plt.grid()
plt.show()


