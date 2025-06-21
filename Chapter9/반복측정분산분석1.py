import pandas as pd
import numpy as np
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns


# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # macOS
plt.rc('axes', unicode_minus=False)

# 데이터 생성
np.random.seed(42)
participants = list(range(1, 11))  # 10명의 참가자
weeks = ['Week1', 'Week2', 'Week3']

data = {
    'participant': np.repeat(participants, len(weeks)),
    'week': weeks * len(participants),
    'effectiveness': np.concatenate([
        np.random.normal(70, 5, 10),  # Week1 점수
        np.random.normal(75, 5, 10),  # Week2 점수
        np.random.normal(80, 5, 10)   # Week3 점수
    ])
}

df = pd.DataFrame(data)

# 반복 측정 ANOVA 수행
rm_anova = AnovaRM(data=df, depvar='effectiveness', subject='participant', within=['week']).fit()
print(rm_anova)

# 시각화
sns.lineplot(data=df, x='week', y='effectiveness', marker='o', errorbar=None)
plt.title('Effectiveness Over Time')
plt.xlabel('Week')
plt.ylabel('Effectiveness Score')
plt.show()

