import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 데이터
temperature = np.array([20, 22, 23, 25, 24, 21, 19])  # 생산 라인 온도 (X)
defect_rate = np.array([3.5, 3.0, 2.8, 2.5, 2.6, 3.2, 3.8])  # 제품 불량률 (Y)

# 평균값 계산
mean_temperature = np.mean(temperature)
mean_defect_rate = np.mean(defect_rate)

# 공분산 및 상관계수 계산
covariance = np.cov(temperature, defect_rate, ddof=0)[0, 1]  # 공분산
correlation = np.corrcoef(temperature, defect_rate)[0, 1]  # 상관계수

# 결과 출력
print("공분산 (Cov(X, Y)):", round(covariance, 2))
print("생산 라인 온도의 평균 (E[X]):", round(mean_temperature, 2))
print("제품 불량률의 평균 (E[Y]):", round(mean_defect_rate, 2))
print("상관계수 (ρ):", round(correlation, 2))

# 시각화 추가
plt.figure(figsize=(8, 6))
plt.scatter(temperature, defect_rate, color='blue', label='Data Points')
plt.title('Scatter Plot of Temperature vs Defect Rate')
plt.xlabel('Temperature (°C)')
plt.ylabel('Defect Rate (%)')
plt.axhline(y=mean_defect_rate, color='green', linestyle='--', label='Mean Defect Rate')
plt.axvline(x=mean_temperature, color='red', linestyle='--', label='Mean Temperature')
plt.legend()
plt.grid()
plt.show()