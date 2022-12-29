# t-검정 회귀 분석

# 회귀 분석에 필요한 라이브러리 호출
from scipy import stats
from statsmodels.formula.api import ols, glm

# 그래프 그리기 위한 라이브러리 호출
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

wine = pd.read_csv("C:/Users/donha/OneDrive/바탕 화면/git/BigData/빅데이터_와인/wine.csv", header=0, engine='python')

# 컬럼 이름 공백 바꾸기
wine.columns = wine.columns.str.replace(' ', '_')

# 레드 와인 샘플의 quality값만 찾아서 저장
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']

# 화이트 와인 샘플의 quality값만 찾아서 저장
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']

# ttest_ind()를 이용하여 t 검정을 하고 두 그룹 간 차이를 확인한다
print(stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var=False))

# 선형회귀 분석식의 종속 변수(y1)와 독립변수(x1~x10)를 구성, 종속변수는 quantity고 나머지는 독립변수이다
# 구성방식은 종속변수 ~ 독립변수1 + 독립변수2 + ...
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'

# ols 선형 회귀 모델을 통해 생성
regression = ols(Rformula, data = wine).fit()

# 선형 회귀 분석 관련 통계값 출력
# print(regession.summary())

# 'quality', 'type'를 제외하고 독립변수만 추출하여 저장
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[:5][:] # 5개의 행, 모든 열 추출해서 저장

# 회귀 예측값 저장
sample1_predict = regression.predict(sample1)

# 예측한 quality 확인
print(sample1_predict, end='\n\n')

# 원래의 quality값을 확인 맞게 예측 되었는 지 위의 값과 비교하여 확인
print(wine[:5]['quality'], end='\n\n')

# 회귀식에 사용할 임의의 독립변수 생성
data = {"fixed_acidity" : [8.5, 8.1],
        "volatile_acidity" : [0.8, 0.5],
        "citric_acid" : [0.3, 0.4],
        "residual_sugar" : [6.1, 5.8],
        "chlorides" : [0.055, 0.04], 
        "free_sulfur_dioxide" : [30.0, 31.0],
        "total_sulfur_dioxide" : [98.0, 99.0],
        "density" : [0.996, 0.91],
        "pH" : [3.25, 3.01],
        "sulphates" : [0.4, 0.35],
        "alcohol" : [9.0, 0.88]
}

sample2 = pd.DataFrame(data, columns=sample1.columns)
print(sample2, end='\n\n')

sample2_predict = regression.predict(sample2)
print(sample2_predict, end='\n\n')

sns.set_style('dark')
sns.displot(red_wine_quality, kde=True, color="red", label="red wine")
sns.displot(red_wine_quality, kde=True, label="white wine")