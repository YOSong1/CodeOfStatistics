import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 고객 구매 확률
p = [0.1, 0.2, 0.15, 0.3, 0.4, 0.25, 0.35, 0.45, 0.5, 0.2]
n = len(p)

# 포아송-이항 분포 확률 계산
def poisson_binomial_pmf(k, p):
    """포아송-이항 분포의 PMF 계산"""
    n = len(p)
    probabilities = 0
    for indices in product([0, 1], repeat=n):
        if sum(indices) == k:
            prob = 1
            for i, bit in enumerate(indices):
                prob *= p[i] if bit else (1 - p[i])
            probabilities += prob
    return probabilities

# PMF 계산
pmf_values = [poisson_binomial_pmf(k, p) for k in range(n + 1)]

# 결과 출력
for k, prob in enumerate(pmf_values):
    print(f"P(X = {k}): {prob:.4f}")

# 시각화
plt.bar(range(n + 1), pmf_values, color="skyblue", edgecolor="black")
plt.title("포아송-이항 분포 (Poisson-Binomial Distribution)")
plt.xlabel("구매한 고객 수")
plt.ylabel("확률")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
