# 처리 시간 값과 각 값의 확률
processing_times = [10, 15, 20, 25, 30]
probabilities = [0.1, 0.3, 0.4, 0.15, 0.05]

# 기대값 계산
expected_value = 0
for i in range(len(processing_times)):
    expected_value += processing_times[i] * probabilities[i]

# 분산 계산
expected_value_squared = 0
for i in range(len(processing_times)):
    expected_value_squared += (processing_times[i] ** 2) * probabilities[i]

variance = expected_value_squared - (expected_value ** 2)

print()
# 결과 출력
print(f"기대값 (평균 처리 시간): {expected_value:.2f}분")
print(f"분산 (처리 시간의 변동성): {variance:.2f}")