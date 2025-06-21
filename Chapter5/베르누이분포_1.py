import numpy as np
import matplotlib.pyplot as plt

# 성공 확률 (광고 클릭 확률)
p = 0.2

# 고객 수
n_customers = 100

# 베르누이 분포 샘플 생성 (클릭 여부: 0 = 실패, 1 = 성공)
clicks = np.random.binomial(1, p, n_customers)  # n=1인 경우 베르누이 분포

# 결과 분석
total_clicks = clicks.sum()  # 클릭한 고객 수
click_rate = total_clicks / n_customers  # 클릭 비율

print()
# print("[단일 실험 결과]")
print(f"총 고객 수: {n_customers}")
print(f"클릭한 고객 수: {total_clicks}")
print(f"실제 클릭 비율: {click_rate:.2%}")
