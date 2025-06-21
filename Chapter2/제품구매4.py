import random

def generate_purchase_data(num_customers=1000):   
    data = []
    for _ in range(num_customers):        
        product_purchase = random.choice([0, 1])          
        service_purchase = random.choice([0, 1]) if product_purchase == 1 else 0  
        data.append((product_purchase, service_purchase))
    return data

def calculate_probabilities(data):    
    total_customers = len(data)
    product_purchases = sum([1 for record in data if record[0] == 1])
    service_purchases = sum([1 for record in data if record[1] == 1])
    both_purchases = sum([1 for record in data if record[0] == 1 and record[1] == 1])

    p_a = product_purchases / total_customers
    p_b_given_a = both_purchases / product_purchases if product_purchases > 0 else 0
    p_a_and_b = both_purchases / total_customers

    return p_a, p_b_given_a, p_a_and_b

# 데이터 생성
num_customers = 1000
purchase_data = generate_purchase_data(num_customers)

# 확률 계산
p_a, p_b_given_a, p_a_and_b = calculate_probabilities(purchase_data)

# 결과 출력
print("기록된 데이터 기반:")
print(f"제품 A 구매 확률 (P(A)): {round(p_a, 2)}")
print(f"제품 A를 구매한 후 서비스 B 구매 확률 (P(B|A)): {round(p_b_given_a, 2)}")
print(f"제품 A와 서비스 B를 구매할 확률 (P(A ∩ B)): {round(p_a_and_b, 2)}")
