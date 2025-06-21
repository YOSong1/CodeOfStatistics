import numpy as np
import matplotlib.pyplot as plt

# 일별 매출 금액(만원)과 방문자 수(명)
# 매출 금액 (단위: 만원)
sales = [300, 320, 310, 330, 305, 400, 310, 320, 315, 310]  
# 방문자 수 (단위: 명)
visitors = [1500, 1600, 1550, 1700, 1580, 2500, 1550, 1600, 1570, 1550]  

# Z-점수 표준화 함수
def z_score_standardize(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return [(x - mean) / std_dev for x in data]

# Z-점수 표준화
sales_standardized = z_score_standardize(sales)
visitors_standardized = z_score_standardize(visitors)


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 시각화
plt.figure(figsize=(12, 6))

# 표준화 전
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), sales, label="매출 (만원)", 
         marker='o', linestyle='-')
plt.plot(range(1, 11), visitors, label="방문자 수 (명)", 
         marker='s', linestyle='--')
plt.title("표준화 전 데이터")
plt.xlabel("일")
plt.ylabel("값")
plt.legend()
plt.grid()

# 표준화 후
plt.subplot(1, 2, 2)
plt.plot(range(1, 11), sales_standardized, label="표준화된 매출", 
         marker='o', linestyle='-')
plt.plot(range(1, 11), visitors_standardized, label="표준화된 방문자 수", 
         marker='s', linestyle='--')
plt.title("표준화 후 데이터")
plt.xlabel("일")
plt.ylabel("표준화 값")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
