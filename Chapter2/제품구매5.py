import pandas as pd
import numpy as np

# 데이터 생성
def generate_purchase_data(num_customers=1000):
    data = {
        'product_purchase': np.random.choice([0, 1], size=num_customers),  # 제품 A 구매 여부
        'service_purchase': np.zeros(num_customers, dtype=int)  # 서비스 B 구매 여부 (초기화)
    }
    df = pd.DataFrame(data)
    df.loc[df['product_purchase'] == 1, 'service_purchase'] = \
        np.random.choice([0, 1], size=df['product_purchase'].sum())
    
    return df


def calculate_probabilities(df):
    total_customers = len(df)
    product_purchases = df['product_purchase'].sum()
    both_purchases = df[(df['product_purchase'] == 1) &
                         (df['service_purchase'] == 1)].shape[0]

    p_a = product_purchases / total_customers
    p_b_given_a = both_purchases / product_purchases \
           if product_purchases > 0 else 0    
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
