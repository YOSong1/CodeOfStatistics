import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, ttest_1samp

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 1. 샘플 데이터 준비 (저항값 측정)
# 제조된 저항기의 샘플 10개
resistor_samples = [98.5, 101.2, 99.8, 100.5, 100.1, 101.0, 98.7, 99.5, 100.3, 99.9]
nominal_value = 100  # 공칭 값 (100 Ω)

# 2. 단일 표본 t 검정 수행
t_stat, p_val = ttest_1samp(resistor_samples, nominal_value)

# 결과 출력
print("샘플 데이터:", resistor_samples)
print(f"t 통계량: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")

# 3. t 분포 시각화
df = len(resistor_samples) - 1  # 자유도
x = np.linspace(-4, 4, 1000)  # t 분포 범위
pdf = t.pdf(x, df)  # t 분포의 PDF

plt.figure(figsize=(8, 5))
plt.plot(x, pdf, label=f"t 분포 (자유도={df})", color='blue')
plt.axvline(t_stat, color='red', linestyle='--', label=f"t 통계량 ({t_stat:.2f})")
plt.title("t 분포와 t 검정 결과")
plt.xlabel("t 값")
plt.ylabel("확률 밀도")
plt.legend()
plt.grid()
plt.show()

# 4. 결과 해석
alpha = 0.05  # 유의 수준
if p_val < alpha:
    print("결론: 저항기의 평균 값이 공칭 값과 통계적으로 유의미하게 다릅니다.")
else:
    print("결론: 저항기의 평균 값이 공칭 값과 통계적으로 유의미하게 다르지 않습니다.")

"""
========== 문제 ==========

한 전자부품 제조회사에서 100Ω 저항기를 생산하고 있습니다. 
품질관리를 위해 생산된 저항기 10개를 샘플로 선택하여 저항값을 측정했습니다.
위 코드는 이 샘플 데이터를 이용하여 t 검정을 수행하는 예제입니다.

문제 1: t 분포와 정규분포의 차이점은 무엇인가요? 
   언제 t 분포를 사용해야 하는지 설명하세요.

문제 2: 위 코드에서 수행한 단일 표본 t 검정의 귀무가설과 대립가설을 명확히 설정하세요.
   - 귀무가설(H₀): 
   - 대립가설(H₁): 

문제 3: 코드 실행 결과를 분석해보세요:
   - t 통계량의 의미는 무엇인가요?
   - p-value가 의미하는 바는 무엇인가요?
   - 유의수준 α=0.05에서 귀무가설을 기각할 수 있나요?

문제 4: 자유도(degrees of freedom)의 개념을 설명하고, 
   이 예제에서 자유도가 9인 이유를 설명하세요.

문제 5: 다음 상황들에 대해 코드를 수정하여 분석해보세요:
   a) 샘플 크기를 20개로 늘렸을 때의 결과 비교
   b) 공칭값을 99Ω으로 변경했을 때의 결과
   c) 유의수준을 0.01로 변경했을 때의 결론 변화

문제 6: t 분포의 형태가 자유도에 따라 어떻게 변하는지 시각화해보세요.
   자유도 1, 5, 10, 30일 때의 t 분포를 하나의 그래프에 그려보세요.

문제 7: 실제 제조업에서 이러한 t 검정을 어떻게 활용할 수 있는지 
   구체적인 응용 사례 3가지를 제시하세요.

문제 8: 95% 신뢰구간을 계산하여 저항기의 평균값에 대한 구간추정을 해보세요.
   이 신뢰구간이 공칭값 100Ω을 포함하는지 확인하세요.

=============================
"""
