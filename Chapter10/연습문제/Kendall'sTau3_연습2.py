import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kendalltau


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 생성
np.random.seed(42)

# 생산 라인 속도 (단위: 제품/분)와 불량률 (단위: %)
data = {
    'line_speed': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],  # 생산 라인 속도
    'defect_rate': [1.5, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0]  # 불량률
}

df = pd.DataFrame(data)

# Kendall's Tau 계산
tau, p_value = kendalltau(df['line_speed'], df['defect_rate'])
print(f"Kendall's Tau: {tau:.3f}, p-value: {p_value:.3f}")

# 시각화
plt.scatter(df['line_speed'], df['defect_rate'], c='blue', label='Data Points')
plt.title("Line Speed vs Defect Rate")
plt.xlabel("Line Speed (products/min)")
plt.ylabel("Defect Rate (%)")
plt.axline((50, 1.5), slope=(6.0 - 1.5) / (95 - 50), color="red", linestyle="--", label="Trend Line")
plt.legend()
plt.show()


"""
===== 문제 출제 =====

【문제】 생산 라인 속도와 불량률 간의 관계 분석

어떤 제조업체에서는 생산 라인의 속도를 높일수록 제품의 불량률이 증가하는 경향이 있는지를 
조사하고자 합니다. 다음은 생산 라인 속도(제품/분)와 불량률(%) 데이터입니다.

생산 라인 속도: [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
불량률: [1.5, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0]

위 코드를 실행한 결과를 바탕으로 다음 질문에 답하시오:

1. Kendall's Tau 계수값은 얼마이며, 이 값이 의미하는 바는 무엇인가?

2. p-value를 통해 생산 라인 속도와 불량률 간의 상관관계가 통계적으로 유의한지 
   판단하시오 (유의수준 α = 0.05).

3. 산점도와 추세선을 보고, 생산 라인 속도가 증가할 때 불량률의 변화 패턴을 
   설명하시오.

4. 이 분석 결과를 바탕으로 제조업체에게 어떤 실무적 조언을 할 수 있는가?

5. Kendall's Tau를 사용한 이유는 무엇이며, Pearson 상관계수 대신 사용할 때의 
   장점은 무엇인가?

【예상 답안】
1. Kendall's Tau = 1.000 (완벽한 양의 상관관계)
2. p-value < 0.05이므로 통계적으로 유의한 상관관계 존재
3. 생산 라인 속도가 증가할수록 불량률이 일관되게 증가하는 단조증가 관계
4. 생산 속도를 높이면 불량률이 증가하므로, 최적의 속도 설정 필요
5. 순위 기반 비모수 검정으로 이상값에 덜 민감하고 단조관계 탐지에 효과적 

"""