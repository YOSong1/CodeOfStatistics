import numpy as np
from scipy.stats import f_oneway, f
import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 포트폴리오 수익률 데이터 생성
np.random.seed(42)

# 포트폴리오 A: 평균 0.1%, 표준편차 0.5% (대형주)
portfolio_a = np.random.normal(loc=0.001, scale=0.005, size=250)

# 포트폴리오 B: 평균 0.1%, 표준편차 1.0% (중소형주)
portfolio_b = np.random.normal(loc=0.001, scale=0.01, size=250)

# 2. F-검정 수행
f_stat, p_value = f_oneway(portfolio_a, portfolio_b)

# 3. 결과 출력
print(f"F-statistic: {f_stat:.3f}, p-value: {p_value:.3f}")

if p_value < 0.05:
    print("두 포트폴리오의 변동성 차이가 통계적으로 유의미합니다.")
else:
    print("두 포트폴리오의 변동성 차이가 통계적으로 유의미하지 않습니다.")

# 4. 시각화
plt.boxplot([portfolio_a, portfolio_b], labels=["Portfolio A", "Portfolio B"])
plt.title("Investment Portfolio Risk Comparison")
plt.ylabel("Daily Returns (%)")
plt.grid()
plt.show()

# 5. 추가 분석: F-분포의 이론적 비율 계산
dof_a = len(portfolio_a) - 1  # 자유도 A
dof_b = len(portfolio_b) - 1  # 자유도 B

critical_value = f.ppf(0.95, dof_a, dof_b)
print(f"임계값 (Critical F): {critical_value:.3f}")
if f_stat > critical_value:
    print("F-statistic이 임계값을 초과하므로 귀무가설을 기각합니다.")
else:
    print("F-statistic이 임계값 이내이므로 귀무가설을 기각하지 않습니다.")

"""
========== 문제 ==========

한 투자회사에서 두 개의 포트폴리오(대형주 포트폴리오 A, 중소형주 포트폴리오 B)의 
위험 수준을 비교하기 위해 각각 250일간의 일일 수익률 데이터를 수집했습니다.
위 코드는 F-검정을 통해 두 포트폴리오의 변동성(위험) 차이를 분석하는 예제입니다.

문제 1: F-검정의 기본 개념과 용도를 설명하세요.
   - F-검정은 언제 사용하나요?
   - t-검정과 F-검정의 차이점은 무엇인가요?
   - F-통계량은 어떻게 계산되나요?

문제 2: 위 코드에서 수행한 F-검정의 가설을 명확히 설정하세요.
   - 귀무가설(H₀): 
   - 대립가설(H₁): 
   - 이 검정에서 무엇을 검증하고자 하는 것인가요?

문제 3: 코드에서 사용된 f_oneway 함수에 대해 설명하세요.
   - f_oneway는 정확히 무엇을 검정하는 함수인가요?
   - 이 함수가 적절한 선택인지 판단하고 그 이유를 설명하세요.
  
문제 4: F-분포의 특성을 설명하세요.
   - F-분포의 모양은 어떻게 결정되나요?
   - 자유도가 F-분포에 미치는 영향을 설명하세요.
   - 이 예제에서 자유도는 각각 몇 개인가요?

문제 5: 코드 실행 결과를 해석해보세요.
   - F-통계량의 의미는 무엇인가요?
   - p-value가 0.05보다 작거나 클 때 각각 어떤 결론을 내릴 수 있나요?
   - 투자 관점에서 이 결과가 의미하는 바는 무엇인가요?

문제 6: 다음 상황들에 대해 코드를 수정하여 분석해보세요.
   a) 포트폴리오 A의 표준편차를 0.8%로 변경했을 때의 결과
   b) 샘플 크기를 100개로 줄였을 때와 500개로 늘렸을 때의 결과 비교
   c) 유의수준을 0.01로 변경했을 때의 결론 변화
   d) 세 번째 포트폴리오 C를 추가했을 때의 분석 방법

문제 7: 박스플롯 시각화를 해석하고 개선해보세요.
   - 박스플롯에서 관찰할 수 있는 두 포트폴리오의 차이점은?
   - 히스토그램이나 다른 시각화 방법을 추가해보세요.
   - F-분포 곡선을 함께 그려 임계값을 시각적으로 표현해보세요.

문제 8: 실제 금융업계에서 F-검정의 활용 사례를 제시하세요.
   - 포트폴리오 관리에서의 활용 방안 3가지
   - 위험 관리 측면에서의 의의
   - F-검정의 한계점과 주의사항

문제 9: 등분산성 검정(Levene's test)과 비교해보세요.
   - scipy.stats.levene을 사용하여 동일한 데이터를 분석해보세요.
   - F-검정과 Levene 검정의 결과가 다를 수 있는 이유를 설명하세요.
   - 어떤 상황에서 어떤 검정을 사용해야 하나요?

문제 10: 다음 추가 분석을 수행해보세요.
   - 각 포트폴리오의 샤프 비율(Sharpe Ratio) 계산
   - VaR(Value at Risk) 비교
   - 상관계수 분석을 통한 포트폴리오 다각화 효과 검증

=============================
"""
