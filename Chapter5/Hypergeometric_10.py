import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 매개변수
N = 20  # 총 제품 수
K = 5   # 불량품 수
n = 5   # 뽑는 샘플 수

# Hypergeometric 분포
x = range(0, n + 1)
pmf = hypergeom.pmf(x, N, K, n)

# 시각화
plt.bar(x, pmf, color="red")
plt.title("Hypergeometric 분포 (N=20, K=5, n=5)")
plt.xlabel("불량품 뽑은 횟수")
plt.ylabel("확률")
plt.show()

