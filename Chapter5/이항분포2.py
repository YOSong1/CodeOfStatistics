from math import comb

def binomial_probability(n, k, p):
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

# 결과 출력
print(f"comb() 결과 P(X = {k}) = {result:.5f}")