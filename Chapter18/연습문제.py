import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import pandas as pd # 데이터 관리를 위해 추가

# 한글 폰트 설정 (환경에 맞게 주석 해제 또는 변경)
plt.rc('font', family='Malgun Gothic') # Windows 예시
# plt.rc('font', family='AppleGothic') # macOS 예시
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

# --- 1. 가상의 세척 후 오염물 양 데이터 생성 ---
# 결과의 재현성을 위한 시드 고정
np.random.seed(101)

# 각 세정제 그룹별 데이터 생성 (각 그룹당 6회 반복)
# 그룹 A: 평균 15mg, 표준편차 2.5
contaminant_A = np.random.normal(loc=15, scale=2.5, size=6)

# 그룹 B: 평균 10mg, 표준편차 2.5
contaminant_B = np.random.normal(loc=10, scale=2.5, size=6)

# 그룹 C: 평균 12mg, 표준편차 2.5
contaminant_C = np.random.normal(loc=12, scale=2.5, size=6)

# (선택 사항) 데이터프레임으로 구성하여 데이터 확인
df_detergent = pd.DataFrame({
    'Type': ['A']*6 + ['B']*6 + ['C']*6,
    'Contaminant_mg': np.concatenate([contaminant_A, contaminant_B, contaminant_C])
})
print("=== 생성된 세정제 효과 실험 데이터 ===")
print(df_detergent.groupby('Type').head(2)) # 그룹별 앞 2개씩만 확인

