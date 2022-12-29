
import pandas as pd

wine = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/wine.csv", header=0, engine='python')
print(wine.info())

# 컬럼 이름 공백 바꾸기
wine.columns = wine.columns.str.replace(' ', '_')

print(wine.head(10))
print()

# 개수(count), 평균(mean), 표준편차(std), 최소값(min) 전체 데이터 백분율에 대해 25번째 백분위 수(25%) 중앙값(50%), 75번째(75%), 100번째(최대값(max))
print(wine.describe())
print()

# 현재 데이터 내에 있는 quality의 값을 중복 없이 출력
print(sorted(wine.quality.unique()))
print()

# quality내의 값별로 데이터 개 수 출력
print(wine.quality.value_counts())
print()

# quality를 기준으로 데이터를 정렬하여 사용하고 싶은 경우
# wine = wine.sort_values('quality')

# print(wine.head(10))
# print()



#데이터 모델링

# 타입에 따라 그룹으로 나눈 후 quantity에 대한 값 비교
print(wine.groupby('type')['quality'].describe())
print()

# 평균
print(wine.groupby('type')['quality'].mean())
print()

# 표준편차
print(wine.groupby('type')['quality'].std())
print()

# 여러개 동시에 비교
print(wine.groupby('type')['quality'].agg(['mean', 'std']))
print()