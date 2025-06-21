import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, norm


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 1. Cauchy와 정규분포 비교
np.random.seed(42)
cauchy_data = cauchy.rvs(loc=0, scale=2, size=1000)  # Cauchy 분포 샘플 데이터
normal_data = norm.rvs(loc=0, scale=2, size=1000)   # 정규 분포 샘플 데이터

# 2. 시각화
plt.figure(figsize=(14, 6))

# Cauchy 분포 데이터 히스토그램
plt.subplot(1, 2, 1)
plt.hist(cauchy_data, bins=30, density=True, alpha=0.6, color='orange', label="Cauchy 분포 데이터")
plt.title("Cauchy 분포를 활용한 이상치 포함 데이터")
plt.xlabel("수익률 (%)")
plt.ylabel("밀도")
plt.legend()
plt.grid()

# 정규 분포 데이터 히스토그램
plt.subplot(1, 2, 2)
plt.hist(normal_data, bins=30, density=True, alpha=0.6, color='blue', label="정규 분포 데이터")
plt.title("정규 분포를 활용한 데이터")
plt.xlabel("수익률 (%)")
plt.ylabel("밀도")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# 3. 이상치 탐지
outliers_cauchy = cauchy_data[np.abs(cauchy_data) > 10]  # 이상치 기준: 수익률 > 10%
outliers_normal = normal_data[np.abs(normal_data) > 10]

print(f"Cauchy 분포에서 탐지된 이상치 개수: {len(outliers_cauchy)}")
print(f"정규 분포에서 탐지된 이상치 개수: {len(outliers_normal)}")

"""
========== 문제 ==========

투자 포트폴리오 분석에서 주식 수익률 데이터는 때때로 극단적인 값(이상치)을 포함합니다.
위 코드는 Cauchy 분포와 정규 분포를 비교하여 이상치가 포함된 데이터의 특성을 분석합니다.

문제 1: Cauchy 분포와 정규 분포의 주요 차이점은 무엇인가요?
   - Cauchy 분포의 특징 3가지를 설명하세요.
   - 왜 Cauchy 분포에서는 평균과 분산이 정의되지 않는지 설명하세요.
   - 정규 분포 대비 Cauchy 분포의 꼬리(tail)가 더 두꺼운 이유를 설명하세요.

문제 2: 위 코드를 실행했을 때 나타나는 시각화 결과를 분석해보세요.
   - 두 히스토그램의 모양에서 어떤 차이점을 관찰할 수 있나요?
   - Cauchy 분포에서 극단값(이상치)이 더 자주 나타나는 이유는 무엇인가요?
   - 실제 금융 데이터에서 이러한 특성이 어떤 의미를 갖는지 설명하세요.

문제 3: 이상치 탐지 결과를 분석해보세요.
   - Cauchy 분포와 정규 분포에서 탐지된 이상치 개수의 차이는 얼마인가요?
   - 이상치 기준을 5%, 15%로 변경했을 때 결과가 어떻게 달라질지 예상해보세요.
   - 샘플 크기를 10,000개로 늘렸을 때 이상치 비율이 어떻게 변할 것으로 예상되나요?

문제 4: 다음 추가 분석을 수행해보세요.
   - loc(위치 모수)을 5로, scale(척도 모수)을 1로 변경했을 때의 결과
   - 두 분포의 중앙값(median)과 사분위수 범위(IQR) 계산 및 비교
   - Box plot을 그려서 두 분포의 이상치 분포 패턴 비교

문제 5: 실제 비즈니스 상황에서 Cauchy 분포를 활용할 수 있는 분야를 설명하세요.
   - 금융 리스크 관리에서의 활용 방안
   - 품질 관리에서 극단적 불량품 발생 모델링
   - 웹사이트 접속 시간이나 서버 응답 시간 분석
   - 각 분야에서 Cauchy 분포가 정규 분포보다 적합한 이유를 설명하세요.

문제 6: 통계적 추론의 관점에서 생각해보세요.
   - Cauchy 분포에서는 왜 중심극한정리가 적용되지 않는지 설명하세요.
   - 표본 평균의 분포가 Cauchy 분포를 따를 때의 문제점은 무엇인가요?
   - 이러한 특성이 실제 데이터 분석에서 어떤 주의사항을 시사하는지 설명하세요.

=============================
"""
