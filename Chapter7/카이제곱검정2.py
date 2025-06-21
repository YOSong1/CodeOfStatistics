import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# 1. 데이터 생성
data = np.array([[60, 40],  # 서비스 A
                 [30, 70],  # 서비스 B
                 [40, 30]]) # 서비스 C

# 데이터프레임 생성
df = pd.DataFrame(data, columns=["Satisfied (만족)", "Dissatisfied (불만족)"], index=["Service A", "Service B", "Service C"])
print("Observed Data (관찰 데이터):")
print(df)

# 2. 카이제곱 검정 수행
chi2, p, dof, expected = chi2_contingency(data)

# 결과 출력
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"p-value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies (기대 빈도):")
print(pd.DataFrame(expected, columns=["Satisfied (만족)", "Dissatisfied (불만족)"], index=["Service A", "Service B", "Service C"]))

# 3. 결과 해석
alpha = 0.05  # 유의수준
if p < alpha:
    print("\n결론: p-value가 유의수준보다 작으므로, 서비스 종류와 고객 만족도는 독립이 아닙니다.")
else:
    print("\n결론: p-value가 유의수준보다 크므로, 서비스 종류와 고객 만족도는 독립입니다.")
