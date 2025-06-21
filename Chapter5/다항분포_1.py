import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 설문 조사 파라미터
n = 100  # 고객 수 (실험 횟수)
p = [0.3, 0.5, 0.2]  # 각 카테고리의 확률: [만족, 보통, 불만족]

# 1. 특정 결과의 확률 계산
x = [30, 50, 20]  # 만족, 보통, 불만족 응답 수
prob = multinomial.pmf(x, n, p)
print(f"만족 30명, 보통 50명, 불만족 20명의 확률: {prob:.4f}")

# 2. 다항 분포 샘플 생성
n_samples = 1000  # 생성할 샘플 개수
samples = multinomial.rvs(n, p, size=n_samples)

# 3. 시각화: 각 카테고리의 평균 발생 횟수
category_means = samples.mean(axis=0)
categories = ['만족', '보통', '불만족']
plt.bar(categories, category_means, color=['green', 'blue', 'red'], alpha=0.7)
plt.title("카테고리별 평균 응답 수")
plt.xlabel("카테고리")
plt.ylabel("평균 응답 수")
plt.grid()
plt.show()

# 4. 다항 분포에서 평균, 분산 및 공분산 계산
mean = [n * pi for pi in p]
variance = [n * pi * (1 - pi) for pi in p]
covariance = -n * np.outer(p, p)
np.fill_diagonal(covariance, variance)

print(f"기대값 (평균): {mean}")
print(f"분산: {variance}")
print(f"공분산 행렬:\n{covariance}")
