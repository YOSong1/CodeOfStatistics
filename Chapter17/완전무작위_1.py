import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# ---------------------------------------
# 1. 가상의 실험 데이터 생성
# ---------------------------------------
# 비료 A, B, C 각각 10개씩 (가상적으로 정규분포를 따르는 무작위 데이터)
np.random.seed(42)  # 재현성 유지를 위해 시드 고정

fertilizer_A = np.random.normal(loc=10, scale=2, size=10)  # 평균 10, 표준편차 2
fertilizer_B = np.random.normal(loc=12, scale=2, size=10)  # 평균 12, 표준편차 2
fertilizer_C = np.random.normal(loc=14, scale=2, size=10)  # 평균 14, 표준편차 2

# ---------------------------------------
# 2. ANOVA (One-Way) 수행
# ---------------------------------------
f_stat, p_value = f_oneway(fertilizer_A, fertilizer_B, fertilizer_C)
print("일원분산분석 결과")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value     : {p_value:.4f}")

# ---------------------------------------
# 3. 결과 해석
# ---------------------------------------
if p_value < 0.05:
    print("=> 유의수준 5%에서 처리(비료 종류) 간 평균의 차이가 통계적으로 유의합니다.")
else:
    print("=> 유의수준 5%에서 처리(비료 종류) 간 평균의 차이가 통계적으로 유의하지 않습니다.")

# ---------------------------------------
# 4. 데이터 시각화
# ---------------------------------------
# 그룹별 boxplot
data = [fertilizer_A, fertilizer_B, fertilizer_C]
labels = ["Fertilizer A", "Fertilizer B", "Fertilizer C"]

plt.boxplot(data, tick_labels=labels)
plt.title("Completely Randomized Design Example")
plt.xlabel("Fertilizer Type")
plt.ylabel("Plant Growth (cm)")
plt.show()
