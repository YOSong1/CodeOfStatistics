import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 제품 생산 데이터: 일별 생산량(개)과 불량률(%)
production = [150, 200, 180, 220, 210, 250, 190, 205, 195, 180]  # 일별 생산량 (단위: 개)
defect_rate = [2.5, 3.0, 2.8, 3.5, 3.2, 4.0, 3.0, 3.1, 2.9, 2.8]  # 불량률 (단위: %)

# Min-Max 스케일링 함수
def min_max_scale(data):
    min_value = np.min(data)
    max_value = np.max(data)
    return [(x - min_value) / (max_value - min_value) for x in data]

# Min-Max 스케일링 적용
production_scaled = min_max_scale(production)
defect_rate_scaled = min_max_scale(defect_rate)

# 1. Min-Max 스케일링 전 시각화
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(range(1, 11), production, label="생산량 (개)", marker='o', linestyle='-')
plt.plot(range(1, 11), defect_rate, label="불량률 (%)", marker='s', linestyle='--')
plt.title("Min-Max 스케일링 전 데이터")
plt.xlabel("일")
plt.ylabel("값")
plt.legend()
plt.grid()

# 2. Min-Max 스케일링 후 시각화
plt.subplot(2, 1, 2)
plt.plot(range(1, 11), production_scaled, label="스케일링된 생산량", marker='o', linestyle='-')
plt.plot(range(1, 11), defect_rate_scaled, label="스케일링된 불량률", marker='s', linestyle='--')
plt.title("Min-Max 스케일링 후 데이터")
plt.xlabel("일")
plt.ylabel("스케일링된 값 (0 ~ 1)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
