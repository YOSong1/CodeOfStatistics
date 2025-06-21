import pandas as pd
import itertools
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

# 요인(Factors)와 수준(Levels) 정의
factors = {
    "Coating_Temperature": [30, 35], # 코팅 온도 (°C)
    "Mixing_Speed": [50, 100],      # 혼합 속도 (rpm)
    "Cooling_Time": [5, 10]         # 냉각 시간 (minutes)
}

# 각 조건에 대해 반복 실험 추가 (n=3)
np.random.seed(42)
experiment_data = []

for temp in factors["Coating_Temperature"]:
    for speed in factors["Mixing_Speed"]:
        for time in factors["Cooling_Time"]:
            # 각 조건에 대해 3번 반복 실험
            for rep in range(3):
                # 효과 계산
                temp_effect = 5 * (temp - 32.5) / 2.5  # 온도 효과
                speed_effect = 2 * (speed - 75) / 25   # 속도 효과  
                time_effect = 3 * (time - 7.5) / 2.5  # 시간 효과
                
                # 상호작용 효과
                temp_time_interaction = 1.5 * ((temp - 32.5) / 2.5) * ((time - 7.5) / 2.5)
                
                # 노이즈 추가
                noise = np.random.normal(0, 1.5)
                
                # 반응 변수 계산
                quality = 85 + temp_effect + speed_effect + time_effect + temp_time_interaction + noise
                
                experiment_data.append({
                    "Coating_Temperature": temp,
                    "Mixing_Speed": speed,
                    "Cooling_Time": time,
                    "Replicate": rep + 1,
                    "Coating_Quality": quality
                })

df_experiment = pd.DataFrame(experiment_data)

print("=== 반복 실험이 있는 완전 요인 설계 ===")
print(f"총 실험 횟수: {len(df_experiment)}개 (각 조건당 3회 반복)")
print("\n실험 데이터 (처음 12개):")
print(df_experiment.head(12))

# 전체 모델 (3차 상호작용 포함)
formula_full = "Coating_Quality ~ Coating_Temperature * Mixing_Speed * Cooling_Time"
model_full = smf.ols(formula=formula_full, data=df_experiment).fit()

print("\n--- 전체 모델 결과 (3차 상호작용 포함) ---")
print(f"관측값 수: {model_full.nobs}")
print(f"모델 파라미터 수: {len(model_full.params)}")
print(f"잔차 자유도: {model_full.df_resid}")
print(f"R-squared: {model_full.rsquared:.4f}")
print("\n모델 계수:")
print(model_full.params)

# 간단한 모델 (주효과 + 2차 상호작용만)
print("\n" + "="*60)
print("=== 간단한 모델 (주효과 + 2차 상호작용) ===")

formula_simple = "Coating_Quality ~ Coating_Temperature + Mixing_Speed + Cooling_Time + Coating_Temperature:Cooling_Time"
model_simple = smf.ols(formula=formula_simple, data=df_experiment).fit()

print(f"\n간단한 모델 결과:")
print(f"관측값 수: {model_simple.nobs}")
print(f"모델 파라미터 수: {len(model_simple.params)}")
print(f"잔차 자유도: {model_simple.df_resid}")
print(f"R-squared: {model_simple.rsquared:.4f}")

print("\n--- 간단한 모델 요약 ---")
print(model_simple.summary())

# 시각화
plt.figure(figsize=(15, 10))

# 1. 주효과 시각화
plt.subplot(2, 3, 1)
sns.boxplot(data=df_experiment, x="Coating_Temperature", y="Coating_Quality")
plt.title("코팅 온도의 주효과")

plt.subplot(2, 3, 2)
sns.boxplot(data=df_experiment, x="Mixing_Speed", y="Coating_Quality")
plt.title("혼합 속도의 주효과")

plt.subplot(2, 3, 3)
sns.boxplot(data=df_experiment, x="Cooling_Time", y="Coating_Quality")
plt.title("냉각 시간의 주효과")

# 2. 상호작용 효과
plt.subplot(2, 3, 4)
sns.pointplot(data=df_experiment, x='Cooling_Time', y='Coating_Quality', 
              hue='Coating_Temperature', dodge=True, errorbar='sd')
plt.title('온도 × 냉각시간 상호작용')
plt.legend(title='온도(°C)')

# 3. 잔차 분석
plt.subplot(2, 3, 5)
plt.scatter(model_simple.fittedvalues, model_simple.resid, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title("잔차 vs 예측값")
plt.xlabel("예측값")
plt.ylabel("잔차")

plt.subplot(2, 3, 6)
stats.probplot(model_simple.resid, dist="norm", plot=plt.gca())
plt.title("잔차 Q-Q Plot")

plt.tight_layout()
plt.show()

