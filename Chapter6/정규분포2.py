import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 파라미터 설정
mu = 500  # 평균
sigma = 10  # 표준편차

# 데이터 생성
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)  # 평균 ± 4표준편차 범위
pdf = norm.pdf(x, mu, sigma)  # 확률 밀도 함수 계산

# 특정 구간의 확률 계산
lower, upper = 490, 510  # 범위
prob = norm.cdf(upper, mu, sigma) - norm.cdf(lower, mu, sigma)  # 누적 확률

# 결과 출력
print(f"무게가 {lower}g에서 {upper}g 사이에 있을 확률: {prob:.4f}")

# 시각화
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label="정규분포 (μ=500, σ=10)", color='blue')
plt.fill_between(x, pdf, where=(x >= lower) & (x <= upper), color='skyblue', alpha=0.5, label="490g ~ 510g 구간")
plt.title("정규분포와 특정 구간 확률")
plt.xlabel("무게 (g)")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()
