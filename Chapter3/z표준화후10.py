import numpy as np

# 일별 매출 금액(만원)과 방문자 수(명)
sales = [300, 320, 310, 330, 305, 400, 310, 320, 315, 310]  # 매출 금액 (단위: 만원)
visitors = [1500, 1600, 1550, 1700, 1580, 2500, 1550, 1600, 1570, 1550]  # 방문자 수 (단위: 명)

# Z-점수 표준화 적용
def z_score_standardize(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return [(x - mean) / std_dev for x in data]

# Z-점수 표준화
sales_standardized = z_score_standardize(sales)
visitors_standardized = z_score_standardize(visitors)

# 표준화된 데이터의 합 계산
total_standardized = [s + v for s, v in 
                      zip(sales_standardized, visitors_standardized)]

print()
# 결과 출력
print("\nZ-점수 표준화를 적용한 결과:")
print("표준화된 매출: ")
print([f'{x:.2f}' for x in sales_standardized])
print("표준화된 방문자 수:")
print([f'{x:.2f}' for x in visitors_standardized])
print("표준화된 데이터 합계:")
print([f'{x:.2f}' for x in total_standardized])
