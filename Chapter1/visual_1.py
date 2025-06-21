import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 시각화 예시에 사용할 Pandas DataFrame
data = {'Name': ['Choi', 'Song', 'Kim', 'Park'],
        'Score': [85, 90, 78, 92],
        'Major': ['Math', 'CS', 'Math', 'Eco']}
df = pd.DataFrame(data)


sns.histplot(data=df, x='Score', kde=True)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

sns.barplot(data=df, x='Name', y='Score')
plt.title('Scores by Student')
plt.show()

df['Height'] = [165, 180, 172, 175]
sns.scatterplot(data=df, x='Height', y='Score')
plt.title('Height vs Score')
plt.show()




