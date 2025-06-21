import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

 # 성공 확률 (상담사 연결 확률)
p =0.2
 # 1. 특정 시도에서 성공 확률 계산
specific_attempt =5  # 5번째 시도에서 성공할 확률
prob_specific_attempt = geom.pmf(specific_attempt, p)
print(f"5번째 시도에서 성공할 확률: {prob_specific_attempt:.4f}")

# 2. 누적 성공 확률 계산
max_attempt =5  # 5번 시도까지 성공할 확률
cumulative_prob = geom.cdf(max_attempt, p)
print(f"5번 시도까지 성공할 확률: {cumulative_prob:.4f}")

# 3. 누적 확률에 따른 최소 시도 횟수 계산
required_prob =0.8  # 80% 확률로 성공하기 위한 최소 시도 횟수
min_attempt_for_prob = geom.ppf(required_prob, p)
print(f"80% 확률로 성공하기 위한 최소 시도 횟수: {min_attempt_for_prob:.0f}")

# 4. 기하 분포 샘플 생성
n_customers =100  # 고객 수
samples = geom.rvs(p, size=n_customers)
print(f"첫 성공까지의 평균 시도 횟수: {np.mean(samples):.2f}")

# 5. 결과 시각화: 고객의 첫 성공까지 시도한 횟수 분포
plt.hist(samples, bins=range(1, np.max(samples) +1),
           color='skyblue', edgecolor='black', alpha=0.7)
plt.title("고객의 첫 성공까지 시도한 횟수 분포")
plt.xlabel("시도 횟수")
plt.ylabel("빈도수")
plt.grid()
plt.show()

# 6. 성공 확률 변화에 따른 분석
attempts = np.arange(1, 21)  # 1~20번 시도
p_values = [0.1, 0.2, 0.3]  # 성공 확률 3가지
for prob in p_values:
   probabilities = geom.pmf(attempts, prob)
   plt.plot(attempts, probabilities, marker='o', label=f'p={prob}')

plt.title("성공 확률 변화에 따른 기하 분포")
plt.xlabel("시도 횟수")
plt.ylabel("확률")
plt.legend()
plt.grid()
plt.show()
