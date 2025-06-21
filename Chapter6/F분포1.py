import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 샘플 데이터 준비
# Line A와 Line B의 샘플 데이터 (생산 품질 점수)
line_a = [85, 87, 90, 88, 86, 89, 91, 92, 88, 87]
line_b = [82, 83, 85, 84, 86, 87, 85, 86, 84, 83]

# 2. F 통계량 및 p-value 계산
var_a = np.var(line_a, ddof=1)  # Line A의 분산
var_b = np.var(line_b, ddof=1)  # Line B의 분산
f_stat = var_a / var_b  # F 통계량
df1 = len(line_a) - 1  # Line A의 자유도
df2 = len(line_b) - 1  # Line B의 자유도
p_val = 1 - f.cdf(f_stat, df1, df2)  # p-value 계산

# 결과 출력
print(f"Line A의 분산: {var_a:.2f}")
print(f"Line B의 분산: {var_b:.2f}")
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
    print("결론: 두 생산 라인의 품질 변동성이 통계적으로 유의미하게 다릅니다.")
else:
    print("결론: 두 생산 라인의 품질 변동성이 통계적으로 유의미하게 다르지 않습니다.")