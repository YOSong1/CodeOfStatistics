from math import factorial

def comb(n, k):
 return factorial(n) // (factorial(k) * factorial(n - k))

def binomial_probability(n, k, p):
 # 조합 계산
 combination = comb(n, k)
 # 확률 계산
 probability = combination * (p ** k) * ((1- p) ** (n - k))
 return probability

# 입력값
n =10  # 총 시행 횟수
k =2  # 성공 횟수
p =0.2# 성공 확률
# 이항 분포 확률 계산
result = binomial_probability(n, k, p)

print()
 # 결과 출력
print(f"P(X = {k}) = {result:.5f}")