import numpy as np

# 일별 매출 금액(만원)과 방문자 수(명)
sales = [300, 320, 310, 330, 305, 400, 310, 320, 315, 310]  # 매출 금액 (단위: 만원)
visitors = [1500, 1600, 1550, 1700, 1580, 2500, 1550, 1600, 1570, 1550]  # 방문자 수 (단위: 명)

# 데이터의 평균 계산
mean_sales = np.mean(sales)
mean_visitors = np.mean(visitors)

# 데이터의 합을 계산해 관계를 단순히 분석
total = [s + v for s, v in zip(sales, visitors)]

print()
# 결과 출력
print(f"매출 평균: {mean_sales:.2f} 만원")
print(f"방문자 평균: {mean_visitors:.2f} 명")
print("일별 매출 + 방문자 수 (단순 합계):")
print(total)
