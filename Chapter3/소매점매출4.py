import numpy as np
import matplotlib.pyplot as plt

# 일별 매출 데이터 (단위: 만원)
daily_sales = [
    300, 320, 310, 330, 305, 400, 310, 320, 315, 310,
    300, 500, 310, 320, 310, 330, 310, 320, 325, 315,
    300, 310, 305, 310, 320, 330, 315, 300, 310, 400
]

# 평균 및 표준편차 계산
mean_sales = np.mean(daily_sales)
std_dev_sales = np.std(daily_sales)  # 모집단 표준편차

# 이상치 범위 설정 (평균 ± 2표준편차)
lower_bound = mean_sales - 2 * std_dev_sales
upper_bound = mean_sales + 2 * std_dev_sales

# 이상치 식별
outliers = [sale for sale in daily_sales 
            if sale < lower_bound or sale > upper_bound]

# 분석 결과 출력
print()
print(f"평균 매출: {mean_sales:.2f} 만원")
print(f"표준편차: {std_dev_sales:.2f} 만원")
print(f"이상치 탐지 기준: {lower_bound:.2f} ~ {upper_bound:.2f} 만원")
print(f"이상치 데이터: {outliers}")

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 시각화
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), daily_sales, marker='o', label="일별 매출")
plt.axhline(mean_sales, color='red', linestyle='dashed', 
            linewidth=1, label=f"평균 매출: {mean_sales:.2f} 만원")
plt.fill_between(range(1, 31), lower_bound, upper_bound, 
                 color='blue', alpha=0.2, label="이상치 범위")
plt.scatter([i+1 for i, sale in enumerate(daily_sales) if sale in outliers], 
                 outliers, color='orange', label="이상치", zorder=5)
plt.title("소매점의 일별 매출 분석")
plt.xlabel("일")
plt.ylabel("매출 (만원)")
plt.legend()
plt.grid()
plt.show()
