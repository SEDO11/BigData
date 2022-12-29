# 셀레니움

from bs4 import BeautifulSoup as bs
from random import randrange as rd
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

l = ['서울', '부산']
t_min = 1
t_max = 2

options = webdriver.ChromeOptions()
# options.headless = True # 웹페이지가 보이지 않고 프로그램 실행
# options.add_argument("winddow-size=1920x1080") # 웹페이지가 보이지 않고 프로그램 실행
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36") # 봇 우회

wd = webdriver.Chrome('C:/j/chromedriver.exe')

def input_click(ele):
    wd.execute_script(f"{ele}.click()", ele)
    time.sleep(1)
    # print('클릭')

def CoffeeBean_store(result):
    coffeeBean_url = "https://www.coffeebeankorea.com/store/store.asp"

    for i in range(2):
        wd.get(coffeeBean_url)
        time.sleep(1)
        
        btn = wd.find_element(By.XPATH, '//*[@id="region_srh"]')
        input_click(btn)
        time.sleep(1)
        
        btn = wd.find_element(By.XPATH, '//*[@id="localTitle"]')
        input_click(btn)
        time.sleep(1)
        
        wd.execute_script(f"storeLocal2({l[i]})")
        html = wd.page_source
        soupCB = bs(html, 'html.parser')
        id_storeList = soupCB.find('ul', id='storeListUL')

        for store in id_storeList.find_all('li'):
            if len(store) <= 3:
                break
            store_td = store.find_all('p')
            store_name = store_td[0].string
            store_address = store_td[2].string
            store_phone = store_td[3].string
            result.append([store_name]+[store_address]+[store_phone])
    return

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>')
    CoffeeBean_store(result)
    
    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./coffeeBean.csv', encoding='utf-8-sig', mode='w')
    
if __name__ == '__main__':
    main()