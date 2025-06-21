import matplotlib.pyplot as plt
from scipy.stats import geom


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 성공 확률
p = 0.2

# 샘플 생성 (100명의 고객)
n_customers = 100
attempts = geom.rvs(p, size=n_customers)

# 평균 시도 횟수 계산
mean_attempts = attempts.mean()

print(f"평균 시도 횟수: {mean_attempts:.2f}")
print(f"최소 시도 횟수: {attempts.min()}, 최대 시도 횟수: {attempts.max()}")

# 시각화
plt.hist(attempts, bins=10, color='orange', edgecolor='black', alpha=0.7)
plt.title("고객 연결까지의 시도 횟수 분포")
plt.xlabel("시도 횟수")
plt.ylabel("빈도수")
plt.show()

"""
[문제] 콜센터 고객 연결 분석

어떤 콜센터에서 고객에게 전화를 걸 때, 한 번의 시도로 고객과 연결될 확률이 20%라고 한다.
콜센터 직원은 고객과 연결될 때까지 계속 전화를 시도한다.

1. 이 상황은 어떤 확률분포를 따르는가? 그 이유를 설명하시오.

2. 100명의 고객에게 전화를 걸어 연결될 때까지의 시도 횟수를 시뮬레이션하여 다음을 구하시오:
   - 평균 시도 횟수
   - 최소 시도 횟수와 최대 시도 횟수
   - 시도 횟수의 분포를 히스토그램으로 나타내시오

3. 이론적으로 첫 번째 성공까지의 평균 시도 횟수는 얼마인가?

4. 시뮬레이션 결과와 이론값을 비교하여 해석하시오.

[힌트]
- 기하분포의 평균: E(X) = 1/p
- 성공 확률 p = 0.2일 때, 이론적 평균 = 1/0.2 = 5
- 기하분포는 첫 번째 성공까지의 시행 횟수를 나타내는 이산확률분포
"""
