import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 파라미터 설정
lambda_rate = 2  # 평균 발생률 (1분당 2번 발생)
scale = 1 / lambda_rate  # scale = 1/λ (평균 간격)

# 1. 데이터 생성
sample_size = 1000
waiting_times = np.random.exponential(scale, sample_size)

# 2. 특정 시간 내에 요청이 들어올 확률 계산 (예: 1분 이내)
prob_within_1_min = expon.cdf(1, scale=scale)  # CDF를 사용
print(f"1분 이내에 요청이 들어올 확률: {prob_within_1_min:.4f}")

# 3. PDF 시각화
x = np.linspace(0, 5, 1000)  # 0~5분까지의 시간
pdf = expon.pdf(x, scale=scale)

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label="PDF (λ=2)", color='blue')
plt.hist(waiting_times, bins=30, density=True, alpha=0.5, label="시뮬레이션 데이터")
plt.axvline(x=1, color='red', linestyle='--', label="1분 경계")
plt.title("지수분포: 고객 대기 시간")
plt.xlabel("대기 시간 (분)")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()
