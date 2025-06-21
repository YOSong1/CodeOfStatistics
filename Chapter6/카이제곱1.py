import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 매개변수
df = 4    # 자유도

# 카이제곱 분포 생성
x = np.linspace(0, 20, 1000)
pdf = chi2.pdf(x, df)

# 시각화
plt.plot(x, pdf, label="카이제곱 분포")
plt.title("카이제곱 분포 (df=4)")
plt.xlabel("값")
plt.ylabel("확률 밀도")
plt.legend()
plt.show()