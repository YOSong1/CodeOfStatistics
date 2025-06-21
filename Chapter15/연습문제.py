import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns # 시각화를 위해 추가

# --- 1. 실험 조건 정의 ---
treatments = ['A', 'B', 'C'] # 학습 방법
blocks = ['Block1_High', 
          'Block2_Mid', 
          'Block3_Low'] # 성취 수준 그룹 (블록)
replicates_per_cell = 2 # 각 블록-처리 조합당 반복 수

# --- 2. 가상의 반응 변수(점수) 데이터 생성 ---
np.random.seed(555) # 결과 재현성을 위한 시드
simulated_data_education = []

# 블록 효과 및 처리 효과 (임의 설정)
block_effects = {'Block1_High': 15, 
                 'Block2_Mid': 5, 
                 'Block3_Low': -5} # 블록별 기본 점수 차이
treatment_effects = {'A': 5, 
                     'B': -2, 
                     'C': 8} # 학습 방법별 효과 차이
base_score = 60 # 기본 평균 점수

for block in blocks:
    for treatment in treatments:
        for _ in range(replicates_per_cell):
            # 가상 점수 계산
            score = base_score + block_effects[block] + treatment_effects[treatment] \
                    + np.random.normal(0, 3) # 평균 0, 표준편차 3의 노이즈
            score = round(np.clip(score, 0, 100), 1) # 0~100점 사이로 조정 및 소수점 첫째자리까지
            
            simulated_data_education.append({'Block': block, 
                                             'Treatment': treatment, 
                                             'Score': score})

