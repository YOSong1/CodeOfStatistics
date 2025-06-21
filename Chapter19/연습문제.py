import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# --- 1. 실험 조건 정의 ---
np.random.seed(101) # 결과 재현성을 위한 시드
n_subjects = 12
subjects_ui = np.repeat(np.arange(1, n_subjects + 1), 2)
periods_ui = np.tile([1, 2], n_subjects)

# --- 처리 순서 그룹 배정 ---
treatments_ui = []
sequences_ui = []
# 그룹 1 (A -> B), 피험자 1~6
for _ in range(n_subjects // 2):
    treatments_ui.extend(['A', 'B'])
    sequences_ui.extend(['A->B', 'A->B'])
# 그룹 2 (B -> A), 피험자 7~12
for _ in range(n_subjects // 2):
    treatments_ui.extend(['B', 'A'])
    sequences_ui.extend(['B->A', 'B->A'])

# --- 데이터프레임 초기 구성 ---
df_ui = pd.DataFrame({
    'Subject': subjects_ui,
    'Period': periods_ui,
    'Sequence': sequences_ui,
    'Treatment': treatments_ui
})

# --- 2. 가상의 반응 변수(과업 완료 시간) 데이터 생성 ---
# UI 효과, 기간 효과, 개인차 효과를 임의로 설정
base_time = 120 # 기본 과업 완료 시간 (초)
treatment_effects_ui = {'A': 0, 'B': -15} # UI B가 A보다 15초 빠름 (기준: A)
period_effects_ui = {1: 0, 2: -10} # 2차 기간에 학습 효과로 10초 단축 (기준: 1차)
subject_random_effects_ui = np.repeat(np.random.normal(0, 10, n_subjects), 2) # 개인별 숙련도 차이
noise_ui = np.random.normal(0, 5, n_subjects * 2) # 순수 오차

df_ui['Time'] = base_time + df_ui['Treatment'].map(treatment_effects_ui) \
                + df_ui['Period'].map(period_effects_ui) \
                + subject_random_effects_ui + noise_ui
df_ui['Time'] = df_ui['Time'].round(1)

