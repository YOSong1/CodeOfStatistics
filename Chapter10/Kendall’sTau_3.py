#두 심사위원의 평가 순위 간의 상관관계 구하기

from scipy.stats import kendalltau

# 데이터 생성
judge_1_scores = [1, 2, 3, 4, 5]  # 심사위원 1 순위
judge_2_scores = [2, 1, 3, 5, 4]  # 심사위원 2 순위

# Kendall's Tau 계산
correlation, p_value =   kendalltau(judge_1_scores, judge_2_scores)

print("Kendall's Tau 상관 분석 결과")
print(f"상관계수:   {correlation:.2f}")
print(f"p-value:   {p_value:.4f}")
if p_value < 0.05:
      print("두 심사위원의 순위 간에 유의미한 상관관계가 있습니다.")
else:
      print("두 심사위원의 순위 간에 유의미한 상관관계가 없습니다.")

