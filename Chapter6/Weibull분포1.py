import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. Weibull 분포 매개변수
k = 1.5  # 형상 매개변수
lambda_ = 1000  # 척도 매개변수

# 2. Weibull 분포 확률 밀도 함수 (PDF)
x = np.linspace(0, 3000, 500)
pdf = weibull_min.pdf(x, c=k, scale=lambda_)

# 3. 샘플 데이터 생성
sample_data = weibull_min.rvs(c=k, scale=lambda_, size=1000)

# 4. 시각화
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"Weibull PDF (k={k}, λ={lambda_})", color='blue')
plt.hist(sample_data, bins=30, density=True, alpha=0.6, color='gray', label="샘플 데이터 히스토그램")
plt.title("Weibull 분포: 기계 부품 수명 분석")
plt.xlabel("시간 (시간)")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 5. 800시간 내에 고장날 확률 계산
target_time = 800
prob_within_target = weibull_min.cdf(target_time, c=k, scale=lambda_)
print(f"{target_time}시간 내에 고장날 확률: {prob_within_target:.4f}")

# 6. 평균 수명 계산
expected_life = weibull_min.mean(c=k, scale=lambda_)
print(f"평균 수명: {expected_life:.2f} 시간")

# 7. 보증 기간 설정 (고장 확률 5% 이하)
warranty_time = weibull_min.ppf(0.05, c=k, scale=lambda_)
print(f"보증 기간 (고장 확률 5% 이하): {warranty_time:.2f} 시간")
