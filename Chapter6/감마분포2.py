import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 감마 분포 매개변수 설정
alpha = 2  # 형상 매개변수 (평균 이벤트 수)
beta = 7   # 척도 매개변수 (1회 이벤트당 평균 시간, 일 단위)

# 2. 감마 분포 확률 밀도 함수 (PDF) 계산
x = np.linspace(0, 50, 500)  # 시간 (0~50일)
pdf = gamma.pdf(x, a=alpha, scale=beta)

# 3. 샘플 데이터 생성
sample_data = gamma.rvs(a=alpha, scale=beta, size=1000)

# 4. 감마 분포 시각화
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"Gamma PDF (α={alpha}, β={beta})", color='blue')
plt.hist(sample_data, bins=30, density=True, alpha=0.6, color='gray', label="샘플 데이터 히스토그램")
plt.title("감마 분포: 목표 가격 도달 시간 분석")
plt.xlabel("시간 (일)")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 5. 옵션 만기 (30일) 전에 목표 도달할 확률 계산
target_time = 30
prob_within_target = gamma.cdf(target_time, a=alpha, scale=beta)
print(f"{target_time}일 이내에 목표 가격에 도달할 확률: {prob_within_target:.4f}")

# 6. 평균 목표 도달 시간 계산
expected_time = alpha * beta
print(f"평균 목표 도달 시간: {expected_time:.2f} 일")

# 7. 옵션 만기 이후(30일 이상)에도 목표 미달성할 확률 계산
prob_above_target = 1 - gamma.cdf(target_time, a=alpha, scale=beta)
print(f"{target_time}일 이후 목표 미달성 확률: {prob_above_target:.4f}")
