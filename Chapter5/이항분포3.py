from scipy.stats import binom
 # 입력값
n =10  # 총 시행 횟수
k =2  # 성공 횟수
p =0.2# 성공 확률

# 이항 분포 확률 계산 (PMF: P(X = k))
result = binom.pmf(k, n, p)
print()
 # 결과 출력
print(f"scipy.stats.binom 결과 P(X = {k}) = {result:.5f}")