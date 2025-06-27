import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 (환경에 맞게 주석 해제 또는 변경)
plt.rc('font', family='Malgun Gothic') # Windows 예시
# plt.rc('font', family='AppleGothic') # macOS 예시
plt.rc('axes', unicode_minus=False) # 마이너스 부호 깨짐 방지

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
np.random.seed(123) # 결과 재현성을 위한 시드
base_efficiency = 10.0 # 기본 연비
effect_A = {10: 0.5, 12: 1.0, 14: 0.2} # 점화 시점 효과
effect_B = {100: 0.8, 120: 0.5, 140: -0.2} # 연료 분사압 효과
effect_C = {300: -0.3, 350: 0.6, 400: 1.2} # 공기흡입량 효과

simulated_responses_engine = []
experiment_details_list = [] # 각 실험의 상세 정보를 저장할 리스트

for i, (a_idx, b_idx, c_idx) in enumerate(l9_design_indices_engine):
    val_A = levels_A_engine[a_idx]
    val_B = levels_B_engine[b_idx]
    val_C = levels_C_engine[c_idx]
    
    current_efficiency = base_efficiency + effect_A[val_A] + effect_B[val_B] + effect_C[val_C] \
                         + np.random.normal(0, 0.3)
    current_efficiency_rounded = round(current_efficiency, 2)
    simulated_responses_engine.append(current_efficiency_rounded)
    experiment_details_list.append([i + 1, val_A, val_B, val_C, current_efficiency_rounded])

# --- 실험 데이터프레임 구성 ---
df_engine = pd.DataFrame(experiment_details_list, columns=["Run", "Ignition_Timing", "Fuel_Pressure", "Air_Intake", "Fuel_Efficiency"])

print("=== 엔진 연비 개선 실험 데이터 ===")
print(df_engine)


# S/N비 계산 함수 정의 (망대특성: 더 클수록 좋은)
# S/N = -10 * log10 ( (1/n) * Σ(1/y_i^2) )
# 이 예제에서는 각 실험 조건당 반복(n)이 없으므로, n=1로 간주합니다.
def sn_ratio_larger_the_better_engine(y_values_engine):
    # y_values_engine는 해당 Run의 반응값(들)을 담은 numpy 배열이어야 함
    # 이 예제에서는 반복이 없으므로 y_values_engine은 단일 값을 가진 배열임
    return -10 * np.log10(np.mean(1 / (y_values_engine**2)))

# DataFrame의 'Fuel_Efficiency' 값에 대해 S/N비 계산 함수 적용
df_engine['SN_Ratio'] = df_engine['Fuel_Efficiency'].apply(lambda x: sn_ratio_larger_the_better_engine(np.array([x])))

print("\n=== S/N 비 계산 결과 추가된 데이터 ===")
print(df_engine)


# 각 인자 수준별 평균 S/N비 계산
sn_means_timing = df_engine.groupby('Ignition_Timing')['SN_Ratio'].mean().reset_index(name='SN_Mean_Timing')
sn_means_pressure = df_engine.groupby('Fuel_Pressure')['SN_Ratio'].mean().reset_index(name='SN_Mean_Pressure')
sn_means_intake = df_engine.groupby('Air_Intake')['SN_Ratio'].mean().reset_index(name='SN_Mean_Intake')

print("\n=== 점화 시점 (Ignition_Timing) 수준별 평균 S/N ===")
print(sn_means_timing)
print("\n=== 연료 분사압 (Fuel_Pressure) 수준별 평균 S/N ===")
print(sn_means_pressure)
print("\n=== 공기흡입량 (Air_Intake) 수준별 평균 S/N ===")
print(sn_means_intake)


# 주효과도 시각화
plt.figure(figsize=(18, 5)) # 전체 그림 영역 크기 설정

# 인자 A: 점화 시점
plt.subplot(1, 3, 1) # 1행 3열 중 첫 번째 위치
plt.plot(levels_A_engine, sn_means_timing['SN_Mean_Timing'], marker='o', linestyle='-')
plt.title('점화 시점(A) 대 평균 S/N비')
plt.xlabel('점화 시점 (BTDC °)')
plt.ylabel('평균 S/N비')
plt.xticks(levels_A_engine)
plt.grid(True)

# 인자 B: 연료 분사압
plt.subplot(1, 3, 2) # 1행 3열 중 두 번째 위치
plt.plot(levels_B_engine, sn_means_pressure['SN_Mean_Pressure'], marker='s', linestyle='--')
plt.title('연료 분사압(B) 대 평균 S/N비')
plt.xlabel('연료 분사압 (bar)')
plt.ylabel('평균 S/N비')
plt.xticks(levels_B_engine)
plt.grid(True)

# 인자 C: 공기흡입량
plt.subplot(1, 3, 3) # 1행 3열 중 세 번째 위치
plt.plot(levels_C_engine, sn_means_intake['SN_Mean_Intake'], marker='^', linestyle='-.')
plt.title('공기흡입량(C) 대 평균 S/N비')
plt.xlabel('공기흡입량 (L/min)')
plt.ylabel('평균 S/N비')
plt.xticks(levels_C_engine)
plt.grid(True)

plt.tight_layout() # 서브플롯 간 간격 자동 조절
plt.show()

print("\n" + "="*70)
print("                  다구찌 방법 종합 분석")
print("="*70)

# 1. 실험 결과 종합 분석
print("1/6: 실험 결과 종합 분석 중...")
plt.figure(figsize=(15, 10))

# 1-1. 연비와 S/N비 비교
plt.subplot(2, 3, 1)
runs = df_engine['Run']
plt.bar(runs, df_engine['Fuel_Efficiency'], alpha=0.7, color='skyblue', label='연비')
plt.xlabel('실험 번호')
plt.ylabel('연비 (km/L)')
plt.title('실험별 연비 결과')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 3, 2)
plt.bar(runs, df_engine['SN_Ratio'], alpha=0.7, color='lightcoral', label='S/N비')
plt.xlabel('실험 번호')
plt.ylabel('S/N비 (dB)')
plt.title('실험별 S/N비 결과')
plt.legend()
plt.grid(True, alpha=0.3)

# 1-3. 연비 vs S/N비 상관관계
plt.subplot(2, 3, 3)
plt.scatter(df_engine['Fuel_Efficiency'], df_engine['SN_Ratio'], 
           s=60, alpha=0.7, color='green')
correlation = np.corrcoef(df_engine['Fuel_Efficiency'], df_engine['SN_Ratio'])[0,1]
plt.xlabel('연비 (km/L)')
plt.ylabel('S/N비 (dB)')
plt.title(f'연비 vs S/N비 상관관계\n(r = {correlation:.3f})')
plt.grid(True, alpha=0.3)

# 1-4. L9 직교배열 시각화
plt.subplot(2, 3, 4)
# 각 요인을 숫자로 매핑
factor_mapping = {
    'A': {10: 1, 12: 2, 14: 3},
    'B': {100: 1, 120: 2, 140: 3},
    'C': {300: 1, 350: 2, 400: 3}
}

A_levels = [factor_mapping['A'][val] for val in df_engine['Ignition_Timing']]
B_levels = [factor_mapping['B'][val] for val in df_engine['Fuel_Pressure']]
C_levels = [factor_mapping['C'][val] for val in df_engine['Air_Intake']]

scatter = plt.scatter(A_levels, B_levels, c=df_engine['SN_Ratio'], 
                     s=100, cmap='viridis', alpha=0.8)
plt.colorbar(scatter, label='S/N비 (dB)')
plt.xlabel('점화 시점 수준')
plt.ylabel('연료 분사압 수준')
plt.title('L9 직교배열 실험점 분포')
plt.xticks([1, 2, 3], ['10°', '12°', '14°'])
plt.yticks([1, 2, 3], ['100bar', '120bar', '140bar'])
plt.grid(True, alpha=0.3)

# 1-5. 요인별 기여도 분석
plt.subplot(2, 3, 5)
# 각 요인의 S/N비 범위 계산 (기여도 지표)
range_A = sn_means_timing['SN_Mean_Timing'].max() - sn_means_timing['SN_Mean_Timing'].min()
range_B = sn_means_pressure['SN_Mean_Pressure'].max() - sn_means_pressure['SN_Mean_Pressure'].min()
range_C = sn_means_intake['SN_Mean_Intake'].max() - sn_means_intake['SN_Mean_Intake'].min()

factors = ['점화 시점(A)', '연료 분사압(B)', '공기흡입량(C)']
ranges = [range_A, range_B, range_C]
colors = ['red', 'blue', 'green']

bars = plt.bar(factors, ranges, color=colors, alpha=0.7)
plt.ylabel('S/N비 범위 (dB)')
plt.title('요인별 기여도 분석')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 각 막대 위에 값 표시
for bar, range_val in zip(bars, ranges):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             f'{range_val:.2f}', ha='center', va='bottom')

# 1-6. 최적 조건 예측
plt.subplot(2, 3, 6)
# 각 요인별 최적 수준 찾기
optimal_A = sn_means_timing.loc[sn_means_timing['SN_Mean_Timing'].idxmax(), 'Ignition_Timing']
optimal_B = sn_means_pressure.loc[sn_means_pressure['SN_Mean_Pressure'].idxmax(), 'Fuel_Pressure']
optimal_C = sn_means_intake.loc[sn_means_intake['SN_Mean_Intake'].idxmax(), 'Air_Intake']

optimal_levels = [optimal_A, optimal_B, optimal_C]
factor_names = ['점화 시점\n(BTDC °)', '연료 분사압\n(bar)', '공기흡입량\n(L/min)']

bars = plt.bar(factor_names, optimal_levels, color=['red', 'blue', 'green'], alpha=0.7)
plt.ylabel('최적 수준')
plt.title('예측된 최적 조건')
plt.grid(True, alpha=0.3)

# 각 막대 위에 값 표시
for bar, level in zip(bars, optimal_levels):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + bar.get_height()*0.02,
             f'{level}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
