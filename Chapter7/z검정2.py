import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest  # statsmodels에서 ztest 함수 가져오기


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 1. 데이터 생성
np.random.seed(42)
sales_A = np.random.normal(loc=110, scale=15, size=100)  # 캠페인 실행 지역
sales_B = np.random.normal(loc=100, scale=15, size=100)  # 캠페인 미실행 지역

# 2. Z-검정 수행
z_stat, p_value = ztest(sales_A, sales_B)

# 3. 결과 출력
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# 4. 결론 해석
alpha = 0.05
if p_value < alpha:
    print("결론: 캠페인이 평균 매출에 유의미한 영향을 미칩니다.")
else:
    print("결론: 캠페인이 평균 매출에 유의미한 영향을 미치지 않습니다.")

# 5. 데이터 시각화
plt.figure(figsize=(10, 6))
plt.hist(sales_A, bins=15, alpha=0.7, label="Region A (캠페인 실행)")
plt.hist(sales_B, bins=15, alpha=0.7, label="Region B (캠페인 미실행)")
plt.axvline(np.mean(sales_A), color='blue', linestyle='--', label="Region A 평균")
plt.axvline(np.mean(sales_B), color='red', linestyle='--', label="Region B 평균")
plt.title("캠페인 실행 여부에 따른 일일 매출 분포")
plt.xlabel("일일 매출")
plt.ylabel("빈도")
plt.legend()
plt.grid()
plt.show()
