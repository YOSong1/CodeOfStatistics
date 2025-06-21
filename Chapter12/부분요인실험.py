import numpy as np
import pandas as pd
import statsmodels.api as sm # 회귀분석을 위해 statsmodels.api 모듈 사용
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Windows 사용자의 경우)
plt.rc('font', family='Malgun Gothic')
# macOS 사용자의 경우 아래 주석 해제 또는 다른 한글 지원 폰트로 변경
# plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

# 1) 데이터프레임 구성
# PDF 의 데이터는 C열이 표준 2^3 설계와 다릅니다.
# 표준적인 2^3 설계 (A, B, C)와 D=ABC 관계, 그리고 재배열된 반응값을 사용합니다.
data = {
    'A': [-1,  1, -1,  1, -1,  1, -1,  1],
    'B': [-1, -1,  1,  1, -1, -1,  1,  1],
    'C': [-1, -1, -1, -1,  1,  1,  1,  1],
    # D = A*B*C 계산
    'D': [(-1)*(-1)*(-1), ( 1)*(-1)*(-1), (-1)*( 1)*(-1), ( 1)*( 1)*(-1),
          (-1)*(-1)*( 1), ( 1)*(-1)*( 1), (-1)*( 1)*( 1), ( 1)*( 1)*( 1)],
    'y': [50, 52, 55, 57, 60, 63, 65, 70] # 가상의 반응값 (순서 일치)
}
df = pd.DataFrame(data)

print("구성된 데이터프레임:")
print(df)

# 2) 회귀분석을 위한 디자인 매트릭스(X) 및 반응 변수(y) 준비
# 독립변수: A, B, C, D (이미 -1, +1로 코딩되어 있음)
X_factors = df[['A', 'B', 'C', 'D']]

# statsmodels 회귀분석 시 절편(상수항)을 추가하기 위해 add_constant 사용
X_design_matrix = sm.add_constant(X_factors) #
y_response = df['y'] #

print("\n회귀분석용 디자인 매트릭스 (X_design_matrix):")
print(X_design_matrix)

# 3) 회귀모델 적합 (OLS: Ordinary Least Squares)
model = sm.OLS(y_response, X_design_matrix).fit() #

# 분석 결과 요약 출력
print("\n회귀분석 결과 요약 (OLS Regression Results):")
print(model.summary()) # [cite: 33, 34, 865, 866]

# 4) 주효과(회귀 계수) 시각화
main_effects_coeffs = model.params[1:] #

plt.figure(figsize=(8, 5)) # 그래프 크기 조절
plt.bar(main_effects_coeffs.index, main_effects_coeffs.values)
plt.xlabel('요인 (Factors)')

plt.ylabel('회귀 계수 (Coefficient = Effect / 2)')
plt.title('부분 요인 실험으로부터의 주효과 회귀 계수')
plt.grid(axis='y', linestyle='--')
plt.show()
















# import numpy as np
# import pandas as pd
# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# # 1) 데이터프레임 구성
# data = {
#     'A':  [-1, -1, -1, -1,  1,  1,  1,  1],
#     'B':  [-1, -1,  1,  1, -1, -1,  1,  1],
#     'C':  [-1,  1, -1,  1, -1,  1, -1,  1],
#     'D':  [-1,  1,  1, -1,  1, -1, -1,  1],
#     'y':  [50, 60, 55, 65, 52, 63, 57, 70]  # 가상의 반응값
# }
# df = pd.DataFrame(data)

# # 2) 회귀분석을 위한 디자인 매트릭스 구성
# # 통상적으로 2수준 요인 실험을 분석할 때는 상수항(절편) 추가를 위해 add_constant 사용
# X = df[['A','B','C','D']]
# X = sm.add_constant(X)
# y = df['y']

# # 3) 회귀모델 적합
# model = sm.OLS(y, X).fit()
# print(model.summary())

# # 4) 주효과(계수) 시각화
# coeffs = model.params[1:]  # const 제외
# plt.bar(coeffs.index, coeffs.values)
# plt.xlabel('Factors')
# plt.ylabel('Effect Estimate')
# plt.title('Main Effects from Fractional Factorial Experiment')
# plt.show()
