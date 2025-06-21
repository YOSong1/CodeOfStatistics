# 데이터
temperature = [25, 28, 30, 27, 29, 33, 35]  # 기온 (X)
sales = [100, 120, 130, 115, 125, 150, 130]  # 판매량 (Y)

# 평균값 계산
def calculate_mean(data):
    return sum(data) / len(data)

mean_temperature = calculate_mean(temperature)
mean_sales = calculate_mean(sales)

# 편차 계산
def calculate_deviation(data, mean):
    return [x - mean for x in data]

deviation_temperature = calculate_deviation(temperature, mean_temperature)
deviation_sales = calculate_deviation(sales, mean_sales)

# 편차 곱 계산
def calculate_covariance(dev1, dev2):
    deviation_products = [dev1[i] * dev2[i] for i in range(len(dev1))]
    return sum(deviation_products) / len(deviation_products)

# 공분산 계산
covariance = calculate_covariance(deviation_temperature, deviation_sales)

print()
# 결과 출력
print("공분산 (Cov(X, Y)):", round(covariance, 2))
