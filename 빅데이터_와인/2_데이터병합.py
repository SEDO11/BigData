#데이터 병합

import pandas as pd

red_df = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/red.csv", header=0, engine='python')
white_df = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/white.csv", header=0, engine='python')

print(red_df.head())

# 데이터에 와인종류 컬럼 추가 값은 red, white를 가짐
print()
red_df.insert(0, column='type', value='red')
white_df.insert(0, column='type', value='white')

# 데이터 합치기
wine = pd.concat([red_df, white_df])
print('레드 와인 데이터 수 : ', red_df.shape)
print('화이트 와인 데이터 수 : ', white_df.shape)
print('총합 와인 데이터 수 : ', wine.shape)

# 합친 데이터 csv 파일로 저장
wine.to_csv('./빅데이터_와인/wine.csv', index=False)