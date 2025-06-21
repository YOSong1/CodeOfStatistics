import numpy as np

data = np.array([1, 2, 3])

# 반복문 없이 모든 요소에 10을 더하기
result = data + 10
print(result) # 출력: [11 12 13]

# 배열 간의 연산
data2 = np.array([10, 20, 30])
result2 = data + data2
print(result2) # 출력: [11 22 33]