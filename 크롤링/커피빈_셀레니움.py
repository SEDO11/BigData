# 셀레니움

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# options.headless = True # 웹페이지가 보이지 않고 프로그램 실행
# options.add_argument("winddow-size=1920x1080") # 웹페이지가 보이지 않고 프로그램 실행
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36") # 봇 우회

def CoffeeBean_store(result):
    coffeeBean_url = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome('C:/j/chromedriver.exe')

    for i in range(1, 50):
        wd.get(coffeeBean_url)
        time.sleep(1)
        try:
            wd.execute_script(f"storePop2({i})")
            time.sleep(1)
            html = wd.page_source
            soupCB = bs(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(store_name)
            
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue
    return

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>')
    CoffeeBean_store(result)
    
    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('./coffeeBean.csv', encoding='utf-8-sig', mode='w')
    
if __name__ == '__main__':
    main()