import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)
new_drug = np.random.normal(loc=10, scale=2, size=20)  # 신약 효과
existing_drug = np.random.normal(loc=7, scale=2, size=20)  # 기존 약물 효과

# t-검정 수행
t_stat, p_value = ttest_ind(new_drug, existing_drug)

# 결과 출력
print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")

if p_value < 0.05:
    print("신약의 효과가 기존 약물과 통계적으로 유의미하게 다릅니다.")
else:
    print("신약과 기존 약물 간의 효과 차이가 통계적으로 유의미하지 않습니다.")

# 데이터 시각화
plt.boxplot([new_drug, existing_drug], labels=["New Drug", "Existing Drug"])
plt.title("Effectiveness of New Drug vs Existing Drug")
plt.ylabel("Blood Pressure Reduction")
plt.grid()
plt.show()
