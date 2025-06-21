import pandas as pd
import itertools
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (Windows 사용자의 경우)
plt.rc('font', family='Malgun Gothic')
# macOS 사용자의 경우 아래 주석 해제 또는 다른 한글 지원 폰트로 변경
# plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

# 요인(Factors)과 수준(Levels) 정의
factors_etching = {
    "Etching_Time": [15, 30],        # 식각 시간 (초)
    "Plasma_Intensity": [200, 300],  # 플라즈마 강도 (W)
    "Gas_Mixture_Ratio": [50, 70]    # 가스 혼합 비율 (A가스 비율 %, 50% 또는 70%)
}

# 각 조건에 대해 반복 실험을 포함한 데이터 생성 (n=3)
np.random.seed(42) # 결과 재현성을 위한 시드 고정
etching_experiment_data = []

for time in factors_etching["Etching_Time"]:
    for intensity in factors_etching["Plasma_Intensity"]:
        for ratio in factors_etching["Gas_Mixture_Ratio"]:
            # 각 조건에 대해 3번 반복 실험
            for rep in range(3):
                # 가상 데이터 생성을 위한 효과 계산 (PDF 로직과 유사하게 조정)
                # (-1, +1) 코딩을 위한 중심값 및 스케일링 인수 설정
                time_norm = (time - 22.5) / 7.5       # 15초 -> -1, 30초 -> +1
                intensity_norm = (intensity - 250) / 50 # 200W -> -1, 300W -> +1
                ratio_norm = (ratio - 60) / 10        # 50% -> -1, 70% -> +1
                
                # 주효과 크기 (임의 설정)
                time_effect = 1.5 * time_norm       # 식각 시간 길어질수록 거칠기 약간 증가
                intensity_effect = -2.5 * intensity_norm # 플라즈마 강도 높아질수록 거칠기 크게 감소
                ratio_effect = 0.5 * ratio_norm     # 가스 A 비율 높아질수록 거칠기 약간 증가
                
                # 상호작용 효과 예시 (시간 * 강도, 임의 설정)
                time_intensity_interaction = -1.0 * time_norm * intensity_norm 
                                                # 시간이 길고 강도가 높을 때 (-1*-1=1 or 1*1=1) 추가 감소 효과
                                                # 또는 한쪽만 높을 때 (+1*-1 = -1)는 반대 효과
                
                # 랜덤 노이즈 추가
                noise = np.random.normal(0, 0.5) # 평균 0, 표준편차 0.5
                
                # 기본 표면 거칠기 10nm에 각 효과와 노이즈를 더하여 최종 표면 거칠기 계산
                surface_roughness = 10 + time_effect + intensity_effect + ratio_effect + \
                                    time_intensity_interaction + noise
                
                etching_experiment_data.append({
                    "Etching_Time": time,
                    "Plasma_Intensity": intensity,
                    "Gas_Mixture_Ratio": ratio,
                    "Replicate": rep + 1,
                    "Surface_Roughness": surface_roughness
                })

df_etching_experiment = pd.DataFrame(etching_experiment_data)

print("=== 반도체 식각 공정 실험 데이터 (일부) ===")
print(df_etching_experiment.head(12))
print(f"\n총 실험 횟수: {len(df_etching_experiment)}회 (각 조건당 3회 반복)")
