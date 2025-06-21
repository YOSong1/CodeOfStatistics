import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency


# 1. 데이터 생성
data = np.array([[50, 30],  # 광고 유형 A
                 [20, 50],  # 광고 유형 B
                 [30, 20]]) # 광고 유형 C

# 데이터프레임 생성
df = pd.DataFrame(data, columns=["Yes (구매)", "No (구매 안 함)"], index=["Ad A", "Ad B", "Ad C"])
print("Observed Data:")
print(df)

# 2. 카이제곱 검정 수행
chi2, p, dof, expected = chi2_contingency(data)

# 결과 출력
print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"p-value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies:")
print(pd.DataFrame(expected, columns=["Yes (구매)", "No (구매 안 함)"], index=["Ad A", "Ad B", "Ad C"]))

# 3. 결과 해석
alpha = 0.05  # 유의수준
if p < alpha:
    print("\n결론: p-value가 유의수준보다 작으므로, 광고 유형과 구매 여부는 독립이 아닙니다.")
else:
    print("\n결론: p-value가 유의수준보다 크므로, 광고 유형과 구매 여부는 독립입니다.")
