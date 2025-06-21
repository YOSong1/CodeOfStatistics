import pandas as pd

# 딕셔너리로 DataFrame 생성
data = {'Name': ['Choi', 'Song', 'Kim', 'Park'],
        'Score': [85, 90, 78, 92],
        'Major': ['Math', 'CS', 'Math', 'Eco']}
df = pd.DataFrame(data)

# 'Score' 열 선택
scores = df['Score']

# 여러 열 선택
subset = df[['Name', 'Score']]

# 조건을 이용한 필터링: 점수가 90점 이상인 학생
high_scores = df[df['Score'] >= 90]
print(high_scores)