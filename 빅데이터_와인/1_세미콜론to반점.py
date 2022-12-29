# csv 파일 구분자가 ;으로 되 있는데 이걸 ,으로 바꾸기

import pandas as pd

red_df = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/winequality-red.csv", sep=';', header=0, engine='python')
white_df = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/winequality-white.csv", sep=';', header=0, engine='python')

# index=False로 해야 csv내에 번호가 없음
red_df.to_csv('./빅데이터_와인/red.csv', index=False)
white_df.to_csv('./빅데이터_와인/white.csv', index=False)