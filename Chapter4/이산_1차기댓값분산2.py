import numpy as np

# 처리 시간 값과 각 값의 확률
processing_times = np.array([10, 15, 20, 25, 30])
probabilities = np.array([0.1, 0.3, 0.4, 0.15, 0.05])

# 기대값 계산
expected_value = np.sum(processing_times * probabilities)

# 분산 계산
expected_value_squared = np.sum((processing_times ** 2) * probabilities)
variance = expected_value_squared - (expected_value ** 2)

print()
# 결과 출력
print("[라이브러리 이용 결과]")
print(f"기대값 (평균 처리 시간): {expected_value:.2f}분")
print(f"분산 (처리 시간의 변동성): {variance:.2f}")