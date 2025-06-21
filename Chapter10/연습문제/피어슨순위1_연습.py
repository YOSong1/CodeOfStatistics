from scipy.stats import spearmanr

# 데이터 생성
judge_1_scores = [1, 2, 3, 4, 5]  # 심사위원 1 순위
judge_2_scores = [2, 1, 3, 5, 4]  # 심사위원 2 순위

# Spearman's Rank Correlation 계산
correlation, p_value = spearmanr(judge_1_scores, judge_2_scores)

print("Spearman's Rank Correlation 분석 결과")
print(f"상관계수:   {correlation:.2f}")
print(f"p-value:   {p_value:.4f}")
if p_value < 0.05:
    print("두 심사위원의 순위 간에 유의미한 상관관계가 있습니다.")
else:
    print("두 심사위원의 순위 간에 유의미한 상관관계가 없습니다.")



"""
   연습 문제

문제: 음성 경연대회 심사위원 순위 분석

한 음성 경연대회에서 5명의 참가자가 경연을 펼쳤습니다.
두 명의 심사위원이 각각 독립적으로 참가자들에게 순위를 매겼습니다.

심사위원 1의 순위 평가: 1위, 2위, 3위, 4위, 5위
심사위원 2의 순위 평가: 2위, 1위, 3위, 5위, 4위

위 데이터를 바탕으로 다음 질문에 답하세요:

1) 두 심사위원의 순위 평가 간에 상관관계가 있는지 스피어만 순위 상관계수를 사용하여 분석하세요.
2) 계산된 상관계수 값을 해석하세요.
3) 유의수준 0.05에서 두 심사위원의 평가가 유의미한 상관관계를 보이는지 판단하세요.
4) 분석 결과를 바탕으로 두 심사위원의 평가 일치도에 대해 설명하세요.

기대 결과:
- 상관계수가 양수인지 음수인지 확인
- p-value를 통한 통계적 유의성 검정
- 두 심사위원의 평가 경향 파악
"""