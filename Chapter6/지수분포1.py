import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 매개변수
lambda_ = 1  # 평균 대기 시간의 역수

# 지수 분포 생성
x = np.linspace(0, 5, 1000)
pdf = expon.pdf(x, scale=1/lambda_)

# 시각화
plt.plot(x, pdf, label="지수 분포")
plt.title("지수 분포")
plt.xlabel("대기 시간")
plt.ylabel("확률 밀도")
plt.legend()
plt.show()