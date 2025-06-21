import matplotlib.pyplot as plt
import numpy as np

# 소비 금액 데이터: 한 달(30일) 동안 매일 소비한 금액 (단위: 만원)
daily_expenses = [
    30, 40, 35, 50, 45, 60, 55, 40, 50, 45, 35, 30, 60, 50, 40,
    30, 55, 45, 40, 50, 60, 50, 35, 40, 30, 50, 55, 60, 45, 40
]

# 평균 및 분산 계산
mean_expense = np.mean(daily_expenses)
variance = np.var(daily_expenses)  # 모집단 분산

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 라인 그래프 생성
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), daily_expenses, marker='o', linestyle='-', label="일별 소비 금액")
plt.axhline(mean_expense, color='red', linestyle='dashed', linewidth=1, label=f"평균 소비 금액: {mean_expense:.2f}만원")

# 분산 강조: 변동성 시각적 표현
plt.title(f"한 달 동안의 일별 소비 금액 (분산: {variance:.2f})")
plt.xlabel("날짜")
plt.ylabel("소비 금액 (만원)")
plt.legend()
plt.grid()
plt.show()

