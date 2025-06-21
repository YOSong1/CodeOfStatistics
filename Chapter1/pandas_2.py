import pandas as pd

# 딕셔너리로 DataFrame 생성
data = {'Name': ['Choi', 'Song', 'Kim', 'Park'],
        'Score': [85, 90, 78, 92],
        'Major': ['Math', 'CS', 'Math', 'Eco']}
df = pd.DataFrame(data)

print(df.head())      # 처음 5개 행 출력
print(df.info())      # 데이터프레임의 요약 정보 (결측치, 자료형 등)
print(df.describe())  # 수치형 데이터의 기술 통계량 요약