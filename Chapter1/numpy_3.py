import numpy as np

scores = np.array([88, 92, 76, 100, 64])

print("평균:", np.mean(scores))
print("표준편차:", np.std(scores))
print("분산:", np.var(scores))
print("최댓값:", np.max(scores))
print("최솟값:", np.min(scores))