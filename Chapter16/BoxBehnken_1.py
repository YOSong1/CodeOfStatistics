import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)


# 1. Box-Behnken 설계 데이터 생성
data = {
    "X1": [-1, 1, -1, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0],
    "X2": [-1, -1, 1, 1, 0, 0, 0, 0, -1, 1, -1, 1, 0, 0, 0],
    "X3": [0, 0, 0, 0, -1, -1, 1, 1, -1, -1, 1, 1, 0, 0, 0],
    "Y": [70, 80, 75, 85, 60, 65, 78, 88, 55, 60, 72, 82, 80, 82, 81]
}

df = pd.DataFrame(data)

# 2. 설계 행렬 (X) 생성
X = np.ones((df.shape[0], 10))  # 상수항 포함
X[:, 1] = df["X1"]
X[:, 2] = df["X2"]
X[:, 3] = df["X3"]
X[:, 4] = df["X1"] * df["X2"]
X[:, 5] = df["X1"] * df["X3"]
X[:, 6] = df["X2"] * df["X3"]
X[:, 7] = df["X1"] ** 2
X[:, 8] = df["X2"] ** 2
X[:, 9] = df["X3"] ** 2

Y = df["Y"].values

# 3. 회귀 계수 계산: β = (XᵀX)⁻¹XᵀY
beta = np.linalg.inv(X.T @ X) @ X.T @ Y
print("회귀 계수 (Beta):")
print(beta)

# 4. 요인 간 관계 분석
print("\n요인 간 관계 분석:")
print(f"상수항 (β0): {beta[0]:.2f}")
print(f"물의 온도 (β1): {beta[1]:.2f}")
print(f"추출 시간 (β2): {beta[2]:.2f}")
print(f"원두의 양 (β3): {beta[3]:.2f}")
print(f"온도-시간 상호작용 (β4): {beta[4]:.2f}")
print(f"온도-원두 상호작용 (β5): {beta[5]:.2f}")
print(f"시간-원두 상호작용 (β6): {beta[6]:.2f}")
print(f"온도^2 (β7): {beta[7]:.2f}")
print(f"시간^2 (β8): {beta[8]:.2f}")
print(f"원두^2 (β9): {beta[9]:.2f}")

# 계수의 해석
print("\n해석:")
print("- β1, β2, β3은 각 요인이 맛 점수에 미치는 1차적인 영향을 나타냅니다.")
print("- β4, β5, β6은 요인 간 상호작용이 맛 점수에 미치는 영향을 나타냅니다.")
print("- β7, β8, β9는 요인의 비선형성(2차 효과)을 나타냅니다.")

# 5. 시각화 (물의 온도와 추출 시간에 따른 Y)
X1_vals = np.linspace(-1, 1, 50)
X2_vals = np.linspace(-1, 1, 50)
X1_grid, X2_grid = np.meshgrid(X1_vals, X2_vals)

X3_fixed = 0  # 원두량 고정 (중간값)
Y_vals = np.zeros_like(X1_grid)

for i in range(X1_grid.shape[0]):
    for j in range(X1_grid.shape[1]):
        x1, x2 = X1_grid[i, j], X2_grid[i, j]
        X_eval = np.array([
            1, x1, x2, X3_fixed,
            x1 * x2, x1 * X3_fixed, x2 * X3_fixed,
            x1 ** 2, x2 ** 2, X3_fixed ** 2
        ])
        Y_vals[i, j] = X_eval @ beta

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(
    85 + (95 - 85) * (X1_grid + 1) / 2,  # X1 실제 값 변환
    20 + (30 - 20) * (X2_grid + 1) / 2,  # X2 실제 값 변환
    Y_vals,
    cmap="viridis",
    alpha=0.8
)
ax.set_xlabel("물의 온도 (°C)")
ax.set_ylabel("추출 시간 (초)")
ax.set_zlabel("맛 점수 (Y)")
fig.colorbar(surface, shrink=0.5, aspect=10)
plt.title("물의 온도와 추출 시간에 따른 맛 점수")
plt.show()
