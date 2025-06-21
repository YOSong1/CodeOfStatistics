import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. Cauchy 분포 매개변수
x0 = 0  # 중앙값 (평균 수익률)
gamma = 2  # 변동성

# 2. Cauchy 분포 확률 밀도 함수 (PDF)
x = np.linspace(-20, 20, 1000)
pdf = cauchy.pdf(x, loc=x0, scale=gamma)

# 3. 주식 수익률 샘플 데이터 생성
np.random.seed(42)  # 재현성 보장
sample_data = cauchy.rvs(loc=x0, scale=gamma, size=1000)
print(sample_data)

# 4. 시각화
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f"Cauchy PDF (x₀={x0}, γ={gamma})", color='blue')
plt.hist(sample_data, bins=30, density=True, alpha=0.6, color='gray', label="샘플 데이터 히스토그램")
plt.title("Cauchy 분포를 활용한 주식 수익률 분석")
plt.xlabel("일일 수익률 (%)")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 5. 특정 손실 임계값 이하 (-5%) 확률 계산
loss_threshold = -5
prob_below_loss = cauchy.cdf(loss_threshold, loc=x0, scale=gamma)
print(f"일일 수익률이 {loss_threshold}% 이하일 확률: {prob_below_loss:.4f}")

# 6. 극단적 수익률 (+10%) 이상 확률 계산
extreme_profit = 10
prob_above_extreme = 1 - cauchy.cdf(extreme_profit, loc=x0, scale=gamma)
print(f"일일 수익률이 {extreme_profit}% 이상일 확률: {prob_above_extreme:.4f}")


