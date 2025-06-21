import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 매개변수
N = 100  # 도서관에 있는 전체 책 수
K = 20   # 특정 주제와 관련된 책 수
n = 10   # 대출된 책의 수

# Hypergeometric 분포
x = range(0, n + 1)
pmf = hypergeom.pmf(x, N, K, n)

# 시각화
plt.bar(x, pmf, color='blue')
plt.title("Hypergeometric 분포: 대출된 책 중 특정 주제 책 개수")
plt.xlabel("대출된 특정 주제 책 개수")
plt.ylabel("확률")
plt.show()

