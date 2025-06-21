import pandas as pd
import statsmodels.formula.api as smf # 수식 기반 모델링을 위해
import statsmodels.api as sm # OLS 직접 사용 및 add_constant를 위해
import numpy as np # 혹시 필요할 수 있으므로 임포트
import matplotlib.pyplot as plt # 시각화를 위해
import seaborn as sns # 시각화를 위해

# 한글 폰트 설정 (환경에 맞게 주석 해제 또는 변경)
# plt.rc('font', family='Malgun Gothic') # Windows 예시
# plt.rc('font', family='AppleGothic') # macOS 예시
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

# 실험 데이터 정의
data_yield = {
    'A_Temperature': [-1,  1, -1,  1], # 요인 A: 반응 온도
    'B_Time':        [-1, -1,  1,  1], # 요인 B: 반응 시간
    'C_Catalyst':    [ 1, -1, -1,  1], # 요인 C: 촉매 양 (C=AB로 생성됨)
    'Yield':         [65, 75, 60, 85]  # 반응 변수: 반응 수율 (%)
}


