import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 샘플 데이터 준비
# 포트폴리오 A와 B의 일일 수익률 데이터 (단위: %)
portfolio_a = [1.2, -0.5, 2.3, -1.0, 0.8, 1.5, -0.7, 1.0, -0.3, 0.6]
portfolio_b = [0.4, 0.3, -0.2, 0.5, 0.1, -0.1, 0.4, 0.2, -0.3, 0.6]

# 2. F 통계량 및 p-value 계산
var_a = np.var(portfolio_a, ddof=1)  # 포트폴리오 A의 분산
var_b = np.var(portfolio_b, ddof=1)  # 포트폴리오 B의 분산
f_stat = var_a / var_b  # F 통계량
df1 = len(portfolio_a) - 1  # 포트폴리오 A의 자유도
df2 = len(portfolio_b) - 1  # 포트폴리오 B의 자유도
p_val = 1 - f.cdf(f_stat, df1, df2)  # p-value 계산

# 결과 출력
print(f"포트폴리오 A의 분산: {var_a:.4f}")
print(f"포트폴리오 B의 분산: {var_b:.4f}")
print(f"F 통계량: {f_stat:.4f}")
print(f"p-value: {p_val:.4f}")

# 3. F 분포 시각화
x = np.linspace(0, 5, 1000)  # F 분포 범위
pdf = f.pdf(x, df1, df2)  # F 분포의 PDF

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"F 분포 (df1={df1}, df2={df2})", color='blue')
plt.axvline(f_stat, color='red', linestyle='--', label=f"F 통계량 ({f_stat:.2f})")
plt.title("F 분포와 F 검정 결과")
plt.xlabel("F 값")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 4. 결과 해석
alpha = 0.05  # 유의 수준
if p_val < alpha:
    print("결론: 두 포트폴리오의 수익률 변동성이 통계적으로 유의미하게 다릅니다.")
else:
    print("결론: 두 포트폴리오의 수익률 변동성이 통계적으로 유의미하게 다르지 않습니다.")
