import os
import pandas as pd


def calculate_conditional_probability(df):
    total_emails = len(df)
    discount_count = df['has_discount'].sum()
    spam_and_discount_count = df[(df['is_spam']) & (df['has_discount'])].shape[0]

    p_discount = discount_count / total_emails

    p_spam_given_discount = (spam_and_discount_count / discount_count) if discount_count > 0 else 0

    return p_spam_given_discount, p_discount


file_path = os.path.join(os.getcwd(), "email_data.xlsx")


try:
    data = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"파일이 경로에 존재하지 않습니다: {file_path}")
    exit()

# 조건부 확률 계산
p_spam_given_discount, p_discount = calculate_conditional_probability(data)

# 결과 출력
print("기록된 데이터 기반:")
print(f"P(스팸 | 할인): {round(p_spam_given_discount, 2)}")
print(f"P(할인): {round(p_discount, 2)}")