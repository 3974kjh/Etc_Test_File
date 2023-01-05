from os import system
from re import T
import requests, sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver

url2 = 'https://finance.naver.com/world/'

# 해외 시작
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url2)
html2 = driver.page_source
soup2 = BeautifulSoup(html2, 'html.parser')

# 다우산업 데이터 가공
daou = soup2.select_one('div.market1 > div > ul > li > dl')
daou_text = daou.get_text().split()
daou_list = []
text = ""
count = 0
flag = 0
for i in daou_text[1]:
    text += i
    if (i == "업"):
        daou_list.append(text)
        text = ""
    elif (count == 1):
        daou_list.append(text)
        count = 10
        text = ""
        flag = 0
    elif (flag == 1):
        count += 1
    if (i == '.'):
        flag = 1
    elif (i == '-' or i == '+'):
        daou_list.append(text[:-1])
        text = text[-1:]
    elif (i == '%'):
        daou_list.append(text)
        text = ""
    if (i == '락' or i == '승'):
        daou_list.append(text)
        text = ""
daou_list.append(text)
daou_list[0] = daou_text[0] + daou_list[0]
daou_list.append(daou_text[2])        
daou_list.append(daou_text[3])

if daou_list[4] == '상승':
    daou_status = '+'
elif daou_list[4] == '하락':
    daou_status = '-'
else:
    daou_status = 'o'
# print(daou_list)        

# 나스닥종합 데이터 가공
nasdac = soup2.select_one('div.market2 > div > ul > li > dl')
nasdac_text = nasdac.get_text().split()
nasdac_list = []
text = ""
count = 0
flag = 0
for i in nasdac_text[1]:
    text += i
    if (i == "합"):
        nasdac_list.append(text)
        text = ""
    elif (count == 1):
        nasdac_list.append(text)
        count = 10
        text = ""
        flag = 0
    elif (flag == 1):
        count += 1
    if (i == '.'):
        flag = 1
    elif (i == '-' or i == '+'):
        nasdac_list.append(text[:-1])
        text = text[-1:]
    elif (i == '%'):
        nasdac_list.append(text)
        text = ""
    if (i == '락' or i == '승'):
        nasdac_list.append(text)
        text = ""
nasdac_list.append(text)
nasdac_list[0] = nasdac_text[0] + nasdac_list[0]
nasdac_list.append(nasdac_text[2])        
nasdac_list.append(nasdac_text[3])

if nasdac_list[4] == '상승':
    nasdac_status = '+'
elif nasdac_list[4] == '하락':
    nasdac_status = '-'
else:
    nasdac_status = 'o'
# print(nasdac_list)  

# S&P500 데이터 가공
sp500 = soup2.select_one('div.market3 > div > ul > li > dl')
sp500_text = sp500.get_text().split()
sp500_list = []
text = ""
count = 0
flag = 0
sp500_list.append(sp500_text[1][:3])
for i in sp500_text[1][3:]:
    text += i
    if (count == 1):
        sp500_list.append(text)
        count = 10
        text = ""
        flag = 0
    elif (flag == 1):
        count += 1
    if (i == '.'):
        flag = 1
    elif (i == '-' or i == '+'):
        sp500_list.append(text[:-1])
        text = text[-1:]
    elif (i == '%'):
        sp500_list.append(text)
        text = ""
    if (i == '락' or i == '승'):
        sp500_list.append(text)
        text = ""
sp500_list.append(text)
sp500_list[0] = sp500_text[0] + sp500_list[0]
sp500_list.append(sp500_text[2])        
sp500_list.append(sp500_text[3])

if sp500_list[4] == "상승":
    sp500_status = '+'
elif sp500_list[4] == "하락":
    sp500_status = '-'
else:
    sp500_status = 'o'
# print(sp500_list)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('>-<><|해외 증시|><>-<')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(daou_status,daou_list[0],"=","현재 지수 : " + daou_list[1], "("+daou_list[3]+")","|","어제 대비",daou_list[2],daou_list[4],"|",daou_list[5],daou_list[6])
print(nasdac_status,nasdac_list[0],"=","현재 지수 : " + nasdac_list[1], "("+nasdac_list[3]+")","|","어제 대비",nasdac_list[2],nasdac_list[4],"|",nasdac_list[5],nasdac_list[6])
print(sp500_status,sp500_list[0],"=","현재 지수 : " + sp500_list[1], "("+sp500_list[3]+")","|","어제 대비",sp500_list[2],sp500_list[4],"|",sp500_list[5],sp500_list[6])

driver.quit()