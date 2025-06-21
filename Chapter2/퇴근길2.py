import random

def generate_visit_data(num_days=100):    
    data = []
    for _ in range(num_days):
        chicken_visit = random.choice([0, 1])  
        pizza_visit = random.choice([0, 1])    
        data.append((chicken_visit, pizza_visit))
    return data

def calculate_probabilities(data):    
    total_days = len(data)
    chicken_visits = sum([1 for record in data if record[0] == 1])
    pizza_visits = sum([1 for record in data if record[1] == 1])
    both_visits = sum([1 for record in data if record[0] == 1 and record[1] == 1])
    
    p_a = chicken_visits / total_days  # P(A): 치킨집 방문 확률
    p_b = pizza_visits / total_days   # P(B): 피자집 방문 확률
    p_a_and_b = both_visits / total_days  # P(A ∩ B): 둘 다 방문 확률
    
    return p_a, p_b, p_a_and_b

def addition_rule(p_a, p_b, p_a_and_b):    
    p_a_or_b = p_a + p_b - p_a_and_b
    return p_a_or_b

# 데이터 생성
visit_data = generate_visit_data(num_days=100)

# print(visit_data)

# 확률 계산
p_a, p_b, p_a_and_b = calculate_probabilities(visit_data)

# 덧셈 법칙 계산
result = addition_rule(p_a, p_b, p_a_and_b)

# 결과 출력
print("기록된 데이터 기반:")
print(f"치킨집 방문 확률 (P(A)): {round(p_a, 2)}")
print(f"피자집 방문 확률 (P(B)): {round(p_b, 2)}")
print(f"둘 다 방문 확률 (P(A ∩ B)): {round(p_a_and_b, 2)}")
print(f"치킨집이나 피자집을 방문할 확률 (P(A ∪ B)): {round(result, 2)}")
