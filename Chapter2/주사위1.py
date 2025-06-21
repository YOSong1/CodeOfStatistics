import random

# 1. 전체 사건의 합은 1
# 주사위: 숫자 1~6
def coin_probability():
    data = [1, 2, 3, 4, 5, 6]
    probabilities = {outcome: 1 / len(data) for outcome in data}  
    total_probability = round(sum(probabilities.values()), 1)  
    print("\n1. 전체 사건의 합은 1")
    print("주사위 확률:")    
    for number, probability in probabilities.items():
        print(number, ":", probability)    
    print("전체 사건의 합:", total_probability)

# 2. 불가능한 사건의 확률은 0
# 주사위: 숫자 1~6, 숫자 7은 불가능한 사건
def impossible_event():
    data = [1, 2, 3, 4, 5, 6]
    event = 7
    probability = 1 / len(data) if event in data else 0
    print("\n2. 불가능한 사건의 확률은 0")
    print(f"주사위 숫자 {event}의 확률:", probability)

# 3. 여사건의 확률
# 주사위: 짝수가 나올 확률
def complement_event():
    data = [1, 2, 3, 4, 5, 6]
    even_numbers = [2, 4, 6]    
    prob_even = len(even_numbers) / len(data)
    prob_odd = 1 - prob_even  
    print("\n3. 여사건의 확률")
    print("짝수가 나올 확률:", prob_even)
    print("홀수가 나올 확률 (여사건):", prob_odd)


# 실행
coin_probability()
impossible_event()
complement_event()

