import numpy as np
from scipy.stats import f_oneway
import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)
line_a = np.random.normal(loc=50, scale=2, size=30)  # 생산 라인 A: 평균 50, 표준편차 2
line_b = np.random.normal(loc=50, scale=3, size=30)  # 생산 라인 B: 평균 50, 표준편차 3

# F-검정 수행
f_stat, p_value = f_oneway(line_a, line_b)

# 결과 출력
print(f"F-statistic: {f_stat:.3f}, p-value: {p_value:.3f}")

if p_value < 0.05:
    print("두 생산 라인의 품질 변동 차이가 통계적으로 유의미합니다.")
else:
    print("두 생산 라인의 품질 변동 차이가 통계적으로 유의미하지 않습니다.")

# 시각화
plt.boxplot([line_a, line_b], labels=["Line A", "Line B"])
plt.title("Quality Variance Comparison by Production Line")
plt.ylabel("Quality Measure")
plt.grid()
plt.show()
