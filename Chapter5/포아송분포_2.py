import matplotlib.pyplot as plt
from scipy.stats import poisson

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 평균 사건 발생률 (λ = 3, 10분당 평균 3건)
lam = 3

# 100번의 10분 구간 동안 전화 건수 시뮬레이션
n_simulations = 100
simulated_calls = poisson.rvs(mu=lam, size=n_simulations)

# 시뮬레이션 결과 분석
print(f"시뮬레이션된 전화 건수 평균: {simulated_calls.mean():.2f}")
print(f"시뮬레이션된 전화 건수 분산: {simulated_calls.var():.2f}")

# 히스토그램 시각화
plt.hist(simulated_calls, bins=10, color='skyblue', edgecolor='black', alpha=0.7, density=True)
plt.title("전화 건수 시뮬레이션 분포 (λ=3)")
plt.xlabel("전화 건수")
plt.ylabel("확률")
plt.show()
