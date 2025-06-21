import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_1samp

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 데이터 준비
data = [118, 122, 120, 121, 119, 123, 117, 119, 121, 120]  # 환자 혈압
mu_expected = 120  # 기대되는 평균 혈압

# 2. 단일 표본 t 검정 수행
t_stat, p_val = ttest_1samp(data, mu_expected)

# 결과 출력
print(f"t 통계량: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")

# 3. t 분포 시각화
df = len(data) - 1  # 자유도
x = np.linspace(-4, 4, 1000)  # t 분포 범위
pdf = t.pdf(x, df)  # t 분포의 PDF

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"t 분포 (자유도={df})", color='blue')
plt.axvline(t_stat, color='red', linestyle='--', label=f"t 통계량 ({t_stat:.2f})")
plt.title("t 분포와 t 검정 결과")
plt.xlabel("t 값")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 4. 결과 해석
alpha = 0.05  # 유의 수준
if p_val < alpha:
    print("결론: 신약의 효과가 기대와 통계적으로 유의미하게 다릅니다.")
else:
    print("결론: 신약의 효과는 기대와 통계적으로 유의미하게 다르지 않습니다.")
