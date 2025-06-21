import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 감마 분포 매개변수 설정
alpha = 2  # 형상 매개변수 (고장 발생 주기의 평균 수)
beta = 3   # 척도 매개변수 (평균 시간 단위)

# 2. 감마 분포 확률 밀도 함수 (PDF) 계산
x = np.linspace(0, 20, 500)  # 시간 (0~20)
pdf = gamma.pdf(x, a=alpha, scale=beta)

# 3. 샘플 데이터 생성
sample_data = gamma.rvs(a=alpha, scale=beta, size=1000)

# 4. 감마 분포 시각화
plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"Gamma PDF (α={alpha}, β={beta})", color='blue')
plt.hist(sample_data, bins=30, density=True, alpha=0.6, color='gray', label="샘플 데이터 히스토그램")
plt.title("감마 분포: 시스템 고장 발생 시간 분석")
plt.xlabel("시간")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 5. 고장이 10시간 이하에 발생할 확률 계산
prob = gamma.cdf(10, a=alpha, scale=beta)
print(f"10시간 이내에 고장이 발생할 확률: {prob:.4f}")

# 6. 평균 고장 발생 시간 계산
expected_time = alpha * beta
print(f"평균 고장 발생 시간: {expected_time:.2f} 시간")
