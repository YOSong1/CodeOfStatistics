import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest  # statsmodels에서 ztest 함수 가져오기


import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터 정의
count = np.array([12, 6])  # 각 그룹의 불량품 수 (기존 공정, 새로운 공정)
nobs = np.array([100, 120])  # 각 그룹의 총 샘플 수

# Z-검정 수행
stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')

# 결과 출력
print(f"Z-통계량: {stat:.4f}")
print(f"p-값: {p_value:.4f}")

# 결과 해석
alpha = 0.05  # 유의수준
if p_value < alpha:
    print("결론: 두 공정 간 불량률의 차이는 통계적으로 유의합니다.")
else:
    print("결론: 두 공정 간 불량률의 차이는 통계적으로 유의하지 않습니다.")
