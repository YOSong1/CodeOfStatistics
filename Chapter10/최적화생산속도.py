import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 샘플 데이터 생성
np.random.seed(42)
data = {
    'speed': np.arange(50, 101, 5),  # 생산 속도 (제품/분)
    'defect_rate': [1.5 + 0.1 * (i - 50) for i in np.arange(50, 101, 5)]  # 불량률 (%)
}
df = pd.DataFrame(data)
df['production'] = 480 / df['speed']  # 제품 하나당 시간 (분)
df['defect_cost'] = df['production'] * (df['defect_rate'] / 100) * 100  # 불량 비용 가정
df['total_cost'] = df['production'] + df['defect_cost']  # 총 비용

# 비용 함수 정의
def total_cost(speed):
    defect_rate = 1.5 + 0.1 * (speed - 50)  # 불량률 (%)
    production = 480 / speed  # 제품 하나당 시간
    defect_cost = production * (defect_rate / 100) * 100  # 불량 비용
    return production + defect_cost

# 최적 속도 찾기
result = minimize(total_cost, x0=70, bounds=[(50, 100)])  # 초기 속도는 70, 범위는 50~100
optimal_speed = result.x[0]

# 결과 출력
print(f"최적 생산 속도: {optimal_speed:.2f} 제품/분")
print(f"최소 총 비용: {total_cost(optimal_speed):.2f}")

# 시각화
plt.plot(df['speed'], df['total_cost'], label='Total Cost', color='blue')
plt.axvline(x=optimal_speed, color='red', linestyle='--', label=f'Optimal Speed ({optimal_speed:.2f})')
plt.title('Production Speed vs Total Cost')
plt.xlabel('Production Speed (products/min)')
plt.ylabel('Total Cost')
plt.legend()
plt.show()



# 결과 해석
# 최적 생산 속도:

# 출력된 **optimal_speed**는 생산 속도와 불량률 간의 균형점입니다.
# 이 속도에서 총 비용이 최소화됩니다.
# 시각화:

# 속도에 따른 총 비용 그래프에서 최저점이 최적 생산 속도를 나타냅니다.
# 5. 추가 고려 사항
# 정확한 불량률 데이터:

# 다양한 속도에서의 실측 불량률 데이터를 확보하여 신뢰도 높은 분석 수행.
# 비용 구성 요소의 세부화:

# 불량률이 높은 경우 발생하는 재작업 비용, 폐기 비용, 고객 신뢰 손실 등을 추가적으로 고려.
# 다변량 분석:

# 작업자 숙련도, 기계 상태, 환경 요인(예: 온도) 등 다른 변수와의 상관관계 분석.
# 시뮬레이션 모델링:

# 실제 생산 환경에서의 시뮬레이션을 통해 최적 생산 속도 설정.
# 결론
# 위 방법을 통해 생산 속도와 불량률의 상충 관계를 정량적으로 분석하고, 총 비용을 최소화하는 최적 생산 속도를 도출할 수 있습니다. 이를 기반으로 효율성과 품질을 동시에 관리하는 생산 전략을 설계할 수 있습니다.






