import numpy as np

# 데이터
temperature = np.array([25, 28, 30, 27, 29, 33, 35])  # 기온 (X)
sales = np.array([100, 120, 130, 115, 125, 150, 130])  # 판매량 (Y)

# 공분산 계산
covariance = np.cov(temperature, sales, ddof=0)[0, 1]

print()
# 결과 출력
print("공분산 라이브러리리 (Cov(X, Y)):", round(covariance, 2))

