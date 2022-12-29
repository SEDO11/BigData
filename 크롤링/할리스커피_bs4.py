from bs4 import BeautifulSoup as bs
import urllib.request as ur
import pandas as pd

result = []

print('크롤링을 몇 페이지 까지 하시겠습니까? : ', end=' ')
p = int(input())

if p < 1:
    p = 1
elif p > 53:
    p = 53

for i in range(1, p+1):
    hollys_url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    print(hollys_url)
    html = ur.urlopen(hollys_url)
    soupHollys = bs(html, 'html.parser')
    tag_tbody = soupHollys.find('tbody')
    
    for store in tag_tbody.find_all('tr'):
        if len(store) <= 3:
            break
        store_td = store.find_all('td')
        store_name = store_td[1].string
        store_sido = store_td[0].string
        store_address = store_td[3].string
        store_phone = store_td[-1].string
        result.append([store_name]+[store_sido]+[store_address]+[store_phone])

hollys_tbl = pd.DataFrame(result, columns=('store', 'sido', 'address', 'phone'))
hollys_tbl = hollys_tbl.set_index('store') # 번호 열 제거하기 위해 store을 기본 인덱스로 사용
hollys_tbl.to_csv('C:/Users/donha/OneDrive/바탕 화면/git/WebCrawling/할리스커피.csv', encoding='utf-8-sig', mode='w')
