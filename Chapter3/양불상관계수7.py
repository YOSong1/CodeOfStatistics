import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 데이터
temperature = [20, 22, 23, 25, 24, 21, 19]  # 생산 라인 온도 (X)
defect_rate = [3.5, 3.0, 2.8, 2.5, 2.6, 3.2, 3.8]  # 제품 불량률 (Y)

# 평균값 계산
def calculate_mean(data):
    return sum(data) / len(data)

mean_temperature = calculate_mean(temperature)
mean_defect_rate = calculate_mean(defect_rate)

# 편차 계산
def calculate_deviation(data, mean):
    return [x - mean for x in data]

deviation_temperature = calculate_deviation(temperature, mean_temperature)
deviation_defect_rate = calculate_deviation(defect_rate, mean_defect_rate)

# 공분산 계산
def calculate_covariance(data1, data2):
    deviation1 = calculate_deviation(data1, calculate_mean(data1))
    deviation2 = calculate_deviation(data2, calculate_mean(data2))
    deviation_products = [deviation1[i] * deviation2[i] for i in range(len(deviation1))]
    return sum(deviation_products) / len(deviation_products)

covariance = calculate_covariance(temperature, defect_rate)

# 분산 및 표준편차 계산
def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

std_temperature = calculate_variance(temperature) ** 0.5
std_defect_rate = calculate_variance(defect_rate) ** 0.5

# 상관계수 계산
def calculate_correlation(covariance, std1, std2):
    return covariance / (std1 * std2)

correlation = calculate_correlation(covariance, std_temperature, std_defect_rate)

print()
# 결과 출력
print("공분산 (Cov(X, Y)):", round(covariance, 2))
print("생산 라인 온도의 표준편차 (σ_X):", round(std_temperature, 2))
print("제품 불량률의 표준편차 (σ_Y):", round(std_defect_rate, 2))
print("상관계수 (ρ):", round(correlation, 2))

# 시각화 추가
plt.figure(figsize=(8, 6))
plt.scatter(temperature, defect_rate, color='blue', label='Data Points')
plt.title('Scatter Plot of Temperature vs Defect Rate')
plt.xlabel('Temperature (°C)')
plt.ylabel('Defect Rate (%)')
plt.axhline(y=mean_defect_rate, color='green', linestyle='--', 
            label='Mean Defect Rate')
plt.axvline(x=mean_temperature, color='red', linestyle='--', 
            label='Mean Temperature')
plt.legend()
plt.grid()
plt.show()