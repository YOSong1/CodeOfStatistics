import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 매개변수
mu = 3    # 평균 배송 시간 (일)
sigma = 0.5  # 표준편차

# 정규 분포 생성
x = np.linspace(mu - 3 * sigma, mu + 3 *   sigma, 1000)
pdf = norm.pdf(x, loc=mu, scale=sigma)

# 시각화
plt.plot(x, pdf, label="배송 시간   분포")
plt.title("정규 분포: 배송 시간")
plt.xlabel("배송 시간 (일)")
plt.ylabel("확률 밀도")
plt.legend()
plt.show()