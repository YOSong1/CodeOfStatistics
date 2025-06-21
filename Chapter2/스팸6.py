import random

def generate_email_data(num_emails=1000):    
    data = []
    for _ in range(num_emails):
        is_spam = random.choices([True, False], weights=[0.3, 0.7])[0]  # 스팸 30%, 일반 70%
        if is_spam:
            has_discount = random.choices([True, False], weights=[0.9, 0.1])[0]  # 스팸 중 "할인" 90%
        else:
            has_discount = random.choices([True, False], weights=[0.2, 0.8])[0]  # 일반 중 "할인" 20%
        data.append((is_spam, has_discount))
    return data

def calculate_conditional_probability(data):    
    total_emails = len(data)
    discount_count = sum(1 for email in data if email[1])
    spam_and_discount_count = sum(1 for email in data if email[0] and email[1])
   
    p_discount = discount_count / total_emails
    
    p_spam_given_discount = (spam_and_discount_count / discount_count) if discount_count > 0 else 0

    return p_spam_given_discount, p_discount

# 데이터 생성
email_data = generate_email_data(num_emails=1000)

# 조건부 확률 계산
p_spam_given_discount, p_discount = calculate_conditional_probability(email_data)

# 결과 출력
print()
print("P(스팸 | 할인):", round(p_spam_given_discount, 2))
print("P(할인):", round(p_discount, 2))

