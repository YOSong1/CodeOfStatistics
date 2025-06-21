import matplotlib.pyplot as plt
from scipy.stats import multinomial


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 생산 데이터 설정
n = 500  # 하루 생산량
p = [0.6, 0.3, 0.1]  # 품질별 확률: [우수, 보통, 불량]

# 1. 특정 품질 분포의 확률 계산
x = [300, 150, 50]  # 우수 300, 보통 150, 불량 50
prob = multinomial.pmf(x, n, p)
print(f"우수 300개, 보통 150개, 불량 50개의 확률: {prob:.6f}")

# 2. 품질 분포 시뮬레이션
n_days = 1000  # 시뮬레이션할 기간 (1000일)
samples = multinomial.rvs(n, p, size=n_days)

# 각 품질의 평균 발생량 계산
category_means = samples.mean(axis=0)
categories = ['우수', '보통', '불량']

# 3. 시각화: 품질별 평균 발생량
plt.bar(categories, category_means, color=['green', 'blue', 'red'], alpha=0.7)
plt.title("품질별 평균 발생량 (1000일 기준)")
plt.xlabel("품질")
plt.ylabel("평균 발생량")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 4. 품질별 발생 비율 분석
total_samples = samples.sum(axis=1)
quality_ratios = samples / total_samples[:, None]
mean_ratios = quality_ratios.mean(axis=0)

print(f"품질별 평균 발생 비율:")
for category, ratio in zip(categories, mean_ratios):
    print(f"  {category}: {ratio:.2%}")

# 5. 일별 불량품 발생 수 히스토그램
plt.hist(samples[:, 2], bins=20, color='red', alpha=0.7, edgecolor='black')
plt.title("일별 불량품 발생 수 분포")
plt.xlabel("불량품 수")
plt.ylabel("빈도")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

"""
[문제] 전자제품 생산 품질 관리 시스템 분석

ABC 전자제품 제조회사에서는 매일 500개의 스마트폰을 생산합니다. 
품질 검사 결과, 각 제품은 다음과 같은 확률로 품질 등급이 결정됩니다:
- 우수 등급 (A급): 60% (p₁ = 0.6)
- 보통 등급 (B급): 30% (p₂ = 0.3)  
- 불량 등급 (C급): 10% (p₃ = 0.1)

위 코드를 실행하고 결과를 분석하여 다음 질문들에 답하시오:

1. 다항분포의 정의와 특성
   - 이 상황이 다항분포를 따르는 이유를 설명하시오
   - 다항분포의 모수 n, p₁, p₂, p₃의 값을 확인하시오

2. 특정 품질 분포 확률 계산
   - 특정 날에 A급 300개, B급 150개, C급 50개가 생산될 확률을 해석하시오
   - 이 확률이 매우 작은 이유를 설명하시오

3. 시뮬레이션 결과 분석 (1000일간)
   - 각 품질별 평균 발생량을 이론값과 비교하시오
     * 이론값: E(X₁) = 500×0.6 = 300, E(X₂) = 500×0.3 = 150, E(X₃) = 500×0.1 = 50
   - 시뮬레이션 평균 비율이 이론적 확률(0.6, 0.3, 0.1)과 얼마나 일치하는지 확인하시오

4. 불량품(C급) 분포 특성 분석
   - 불량품 발생 수의 히스토그램을 보고 분포의 형태를 설명하시오
   - 불량품 발생량의 평균과 표준편차를 계산하시오
     * 이론값: 평균 = 50, 분산 = 500×0.1×0.9 = 45, 표준편차 = √45 ≈ 6.71

5. 품질 관리 의사결정 지원
   - 하루 불량품이 60개 이상 발생하는 날의 비율을 시뮬레이션 결과에서 계산하시오
   - 연속 3일간 모두 불량품이 40개 미만인 상황의 발생 가능성을 추정하시오
   - 1000일 중 가장 많은 불량품이 발생한 날의 수량과 그 확률을 추정하시오

[다항분포 핵심 공식]
- 확률질량함수: P(X₁=x₁, X₂=x₂, X₃=x₃) = (n!)/(x₁!x₂!x₃!) × p₁^x₁ × p₂^x₂ × p₃^x₃
- 평균: E(Xᵢ) = n × pᵢ
- 분산: Var(Xᵢ) = n × pᵢ × (1-pᵢ)
- 공분산: Cov(Xᵢ, Xⱼ) = -n × pᵢ × pⱼ (i≠j)
"""
