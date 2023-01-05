from os import system
from re import T
import struct
import requests, sys
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

Top_deal = soup.select('table.tbl_home > tbody > tr')

def MakeSameWidth(textlen):
    width = ""
    for i in range(30-textlen):
        width += " "
    return width

Rank = 0
flag_count = 0

def show_guide_line(cnt):
    if cnt == 1:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|오늘 거래 상위 종목|><>-<')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    elif cnt == 16:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|오늘 최고 상승 종목|><>-<')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=') 
    elif cnt == 31:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|오늘 최고 하락 종목|><>-<')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')  
    elif cnt == 46:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|오늘 국내 시총 상위 종목|><>-<')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=') 

for i in range(1, 61):
    show_guide_line(i)
    blank = ""
    a = Top_deal[i-1].get_text().split()[::-1]
    Top_deal_item = []
    Top_filter_item = []
    name_check = 0
    name_list = []
    name = ""
    for item in a:
        name_check += 1
        if (name_check >= 5):
            name_list.append(item)
        else:
            Top_filter_item.append(item)
    for item in name_list[::-1]:
        name += item    
    Top_filter_item.append(name)
    Top_deal_item = Top_filter_item[::-1]
    Rank+=1
    if (Rank >= 10):
        print_Rank = str(Rank)+"st"
    else:
        print_Rank = str(Rank)+"st"+" "
    blank = MakeSameWidth(len(Top_deal_item[0]))
    if (Top_deal_item[3] == '보합'):
        print(print_Rank, "종목 명 :",Top_deal_item[1], blank," | ","현재 가 :",Top_deal_item[2]+"원", "("+Top_deal_item[4]+")"," | ","전일 대비","0"+"원",Top_deal_item[3])
    else:
        print(print_Rank, "종목 명 :",Top_deal_item[0], blank," | ","현재 가 :",Top_deal_item[1]+"원", "("+Top_deal_item[4]+")"," | ","전일 대비",Top_deal_item[3]+"원",Top_deal_item[2])
    if i % 15 == 0:
        Rank = 0
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

# doller_list = []
# for i in range(60, 64):
#     a = Top_deal[i].get_text()
#     Top_deal_item = []
#     for j in a.split():
#         Top_deal_item.append(j)
#     doller_list.append(Top_deal_item)