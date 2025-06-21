import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. L9 직교배열 및 요인 수준 정의 ---
# 인자 A (점화 시점) 수준 (예시: BTDC 10, 12, 14)
levels_A_engine = [10, 12, 14]
# 인자 B (연료 분사압) 수준 (예시: 100, 120, 140 bar)
levels_B_engine = [100, 120, 140]
# 인자 C (공기흡입량) 수준 (예시: 300, 350, 400 L/min)
levels_C_engine = [300, 350, 400]

# L9 직교배열 인덱스 (0, 1, 2는 각 levels 리스트의 인덱스)
l9_design_indices_engine = [
    (0, 0, 0), (0, 1, 1), (0, 2, 2),
    (1, 0, 1), (1, 1, 2), (1, 2, 0),
    (2, 0, 2), (2, 1, 0), (2, 2, 1)
]

# --- 2. 가상의 연비(반응값) 데이터 생성 ---
# 실제로는 실험 측정값 사용. 여기서는 예시를 위해 임의 생성
np.random.seed(123) # 결과 재현성을 위한 시드
base_efficiency = 10.0 # 기본 연비
# 각 요인 수준에 따른 효과 (임의로 설정, 학생들이 찾아야 할 숨겨진 효과)
effect_A = {10: 0.5, 12: 1.0, 14: 0.2} # 점화 시점 효과
effect_B = {100: 0.8, 120: 0.5, 140: -0.2} # 연료 분사압 효과
effect_C = {300: -0.3, 350: 0.6, 400: 1.2} # 공기흡입량 효과

simulated_responses_engine = []
for a_idx, b_idx, c_idx in l9_design_indices_engine:
    # 해당 수준의 실제 값 가져오기
    val_A = levels_A_engine[a_idx]
    val_B = levels_B_engine[b_idx]
    val_C = levels_C_engine[c_idx]
    
    # 가상 연비 계산 (기본 연비 + 각 요인 효과 + 약간의 상호작용(선택적) + 노이즈)
    # 예시: 간단한 주효과 합 + 노이즈
    current_efficiency = base_efficiency + effect_A[val_A] + effect_B[val_B] + effect_C[val_C] \
                         + np.random.normal(0, 0.3) # 평균 0, 표준편차 0.3의 노이즈
    simulated_responses_engine.append(round(current_efficiency, 2))


