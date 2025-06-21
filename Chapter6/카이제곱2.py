import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
from scipy.stats import chi2

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 데이터 준비
data = np.array([[20, 30],  # 남성 (감염, 비감염)
                 [15, 35]])  # 여성 (감염, 비감염)
categories = ['감염', '비감염']
index = ['남성', '여성']

# 교차표 생성
df = pd.DataFrame(data, columns=categories, index=index)
print("교차표:\n", df)

# 2. 카이제곱 독립성 검정
chi2_stat, p_val, dof, expected = chi2_contingency(data)

print("\n카이제곱 통계량: {:.4f}".format(chi2_stat))
print("p-value: {:.4f}".format(p_val))
print("자유도: {}".format(dof))
print("기대빈도표:\n", expected)

# 3. 카이제곱 분포 시각화
x = np.linspace(0, 10, 1000)  # 카이제곱 분포 x값 (범위 설정)
pdf = chi2.pdf(x, dof)  # PDF 계산

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"카이제곱 분포 (자유도={dof})", color='blue')
plt.axvline(chi2_stat, color='red', linestyle='--', label="검정 통계량")
plt.title("카이제곱 분포와 검정 통계량")
plt.xlabel("카이제곱 통계량")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 4. 결과 해석
if p_val < 0.05:
    print("결과: 유의미한 관계가 있습니다. 성별과 감염 여부는 독립적이지 않습니다.")
else:
    print("결과: 유의미한 관계가 없습니다. 성별과 감염 여부는 독립적입니다.")
