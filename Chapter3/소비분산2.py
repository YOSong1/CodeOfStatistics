def calculate_variance(data):
    n = len(data)
    mean_value = sum(data) / n
    variance = sum((x - mean_value) ** 2 for x in data) / n  # 모집단 분산
    return variance


# 소비 금액 데이터: 한 달(30일) 동안 매일 소비한 금액 (단위: 만원)
daily_expenses = [
        30, 40, 35, 50, 45, 60, 55, 40, 50, 45, 35, 30, 60, 50, 40,
        30, 55, 45, 40, 50, 60, 50, 35, 40, 30, 50, 55, 60, 45, 40
    ]
    
# 분산 계산
variance = calculate_variance(daily_expenses)

# 결과 출력
print()
print("한 달 동안 매일 소비한 금액의 분산:")
print(f"분산: {variance:.2f} (만원^2)")

