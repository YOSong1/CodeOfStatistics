import numpy as np
import pandas as pd
# from scipy.optimize import minimize # 최적화 시 필요
# import matplotlib.pyplot as plt # 시각화 시 필요
# from mpl_toolkits.mplot3d import Axes3D # 3D 시각화 시 필요
# import statsmodels.formula.api as smf # 모델링 시 필요

# --- 1. Box-Behnken 설계점 (3요인, 15점 예시 - 코드화된 값) ---
# 이 설계점은 pyDOE2 또는 다른 통계 패키지에서 생성하거나,
# 직접 입력할 수 있습니다. 여기서는 대표적인 형태를 직접 입력합니다.
# (순서는 다를 수 있으나, 각 요인의 -1, 0, 1이 균형있게 조합되어야 함)
design_points_coded = [
    [-1, -1,  0], [ 1, -1,  0], [-1,  1,  0], [ 1,  1,  0],
    [-1,  0, -1], [ 1,  0, -1], [-1,  0,  1], [ 1,  0,  1],
    [ 0, -1, -1], [ 0,  1, -1], [ 0, -1,  1], [ 0,  1,  1],
    [ 0,  0,  0], [ 0,  0,  0], [ 0,  0,  0]  # 중심점 3회 반복
]
df_design_coded = pd.DataFrame(design_points_coded, columns=['X1', 'X2', 'X3'])

# --- 2. 실제 요인 수준으로 변환 ---
# 열처리 온도 (X1): 450(-1), 500(0), 550(+1)
df_design_coded['Heat_Treatment_Temp'] = df_design_coded['X1'].apply(lambda x: 500 + x * 50)
# 합금 원소 A 첨가량 (X2): 1.0%(-1), 1.5%(0), 2.0%(+1)
df_design_coded['Alloy_A_Percentage'] = df_design_coded['X2'].apply(lambda x: 1.5 + x * 0.5)
# 압연 속도 (X3): 5m/min(-1), 10m/min(0), 15m/min(+1)
df_design_coded['Rolling_Speed'] = df_design_coded['X3'].apply(lambda x: 10 + x * 5)

# --- 3. 가상의 인장 강도(반응값) 데이터 생성 ---
np.random.seed(888) # 결과 재현성을 위한 시드
base_strength = 650 # 기본 인장 강도 (MPa)

# 각 요인 및 상호작용의 가상 효과 (학생들은 이 효과를 찾아야 함)
# X1, X2, X3는 코드화된 값 (-1, 0, +1)
X1_coded = df_design_coded['X1']
X2_coded = df_design_coded['X2']
X3_coded = df_design_coded['X3']

# 효과 부여 (예시)
tensile_strength_values = (
    base_strength
    + 20 * X1_coded  # 온도가 높을수록 강도 증가
    + 15 * X2_coded  # 합금 A 첨가량 많을수록 강도 증가
    + 5 * X3_coded   # 압연 속도 빠를수록 강도 약간 증가
    - 8 * X1_coded**2 # 최적 온도가 존재 (위로 볼록)
    - 6 * X2_coded**2 # 최적 첨가량이 존재 (위로 볼록)
    # - 2 * X3_coded**2 # 압연 속도도 최적점 가정 (선택적)
    + 4 * X1_coded * X2_coded # 온도와 첨가량의 양의 상호작용
    + np.random.normal(0, 5, len(df_design_coded)) # 평균 0, 표준편차 5의 노이즈
)
df_design_coded['Tensile_Strength'] = np.round(tensile_strength_values, 1)

# 최종 분석용 데이터프레임 준비 (실제값 기준 열과 반응 변수만 사용)
df_strength_experiment = df_design_coded[['Heat_Treatment_Temp', 
                                           'Alloy_A_Percentage', 
                                           'Rolling_Speed', 
                                           'Tensile_Strength']].copy()

print("=== 신소재 인장 강도 최적화 실험 데이터 (일부) ===")
print(df_strength_experiment.head())
print(f"\n총 생성된 데이터 포인트 수: {len(df_strength_experiment)}")

