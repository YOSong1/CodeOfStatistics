import pandas as pd
import numpy as np

# 데이터 생성
def generate_visit_data(num_days=100):
    data = {
        'chicken_visit': np.random.choice([0, 1], size=num_days),  # 1: 치킨집 방문, 0: 방문하지 않음
        'pizza_visit': np.random.choice([0, 1], size=num_days)    # 1: 피자집 방문, 0: 방문하지 않음
    }
    return pd.DataFrame(data)

# 확률 계산
def calculate_probabilities(df):
    total_days = len(df)
    p_a = df['chicken_visit'].mean()  # P(A): 치킨집 방문 확률
    p_b = df['pizza_visit'].mean()    # P(B): 피자집 방문 확률
    p_a_and_b = df[(df['chicken_visit'] == 1) 
                   & (df['pizza_visit'] == 1)].shape[0] / total_days  # P(A ∩ B)

    return p_a, p_b, p_a_and_b

# 덧셈 법칙 계산
def addition_rule(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b

# 데이터 생성
visit_data = generate_visit_data(num_days=100)

# 확률 계산
p_a, p_b, p_a_and_b = calculate_probabilities(visit_data)

# 덧셈 법칙 계산
p_a_or_b = addition_rule(p_a, p_b, p_a_and_b)

# 결과 출력
print("기록된 데이터 기반:")
print(f"치킨집 방문 확률 (P(A)): {round(p_a, 2)}")
print(f"피자집 방문 확률 (P(B)): {round(p_b, 2)}")
print(f"둘 다 방문 확률 (P(A ∩ B)): {round(p_a_and_b, 2)}")
print(f"치킨집이나 피자집을 방문할 확률 (P(A ∪ B)): {round(p_a_or_b, 2)}")