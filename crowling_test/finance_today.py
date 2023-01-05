from os import system
from threading import Thread
from pyautogui import sleep
import requests, sys
from bs4 import BeautifulSoup
import pymssql

def MakeCodes(code):
    now_code_len = len(code)

    if now_code_len < 6:
        for i in range(6 - now_code_len):
            code = '0' + code
    return code

def makenum(A):
    num = ''
    for cost in A:
        if cost != ',':
            num +=cost
    return num

def dividenum(A):
    integer = ''
    decimal = ''
    dot_flag = 0
    for cost in A:
        if cost == '.':
            dot_flag = 1
        if dot_flag == 0 and cost != ',' and cost != '.':
            integer +=cost
        elif dot_flag == 1 and cost != ',' and cost != '.':
            decimal +=cost
    return integer, decimal

def makecomma(A):
    make_comma_cost = ''
    for i in range(len(A)):
        if i != 0 and i % 3 == 0:
            make_comma_cost += ','
        make_comma_cost += A[len(A)-i-1]
    return make_comma_cost

# 코스피 정보 출력============================================================================================================
url = 'https://finance.naver.com/'

# 국내 시장
response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

kospi = soup.select_one('div.heading_area')
kospi_info = kospi.select_one('a > span')
kospi_num = kospi.select_one('.num')
kospi_updown = kospi.select_one('.num2')
kospi_persent = kospi.select_one('.num3')
kospi_text = kospi.select_one('.blind')
kospi_now_i, kospi_now_f  = dividenum(kospi_num.get_text())
kospi_gap_i, kospi_gap_f = dividenum(kospi_updown.get_text())

if '-' in kospi_persent.get_text():
    yesterday_kospi_i = int(kospi_now_i) + int(kospi_gap_i)
    yesterday_kospi_f = int(kospi_now_f) + int(kospi_gap_f)
    if 2 < len(str(yesterday_kospi_f)):
        yesterday_kospi_i += 1
        yesterday_kospi_f = int(str(yesterday_kospi_f)[1:])

else:
    yesterday_kospi_i = int(kospi_now_i) - int(kospi_gap_i)
    if int(kospi_now_f) >= int(kospi_gap_f):
        yesterday_kospi_f = int(kospi_now_f) - int(kospi_gap_f)
    else:
        yesterday_kospi_i -= 1
        yesterday_kospi_f = int(kospi_now_f) + 100 - int(kospi_gap_f)

print_yesterday_kospi_i = makecomma(str(yesterday_kospi_i))[::-1]
print_yesterday_kospi = print_yesterday_kospi_i + '.' + str(yesterday_kospi_f)

print('>-<><|코스피 정보|><>-<')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(kospi_persent.get_text()[0], '코스피 =','현재 지수 : ' + kospi_num.get_text(),'/ 어제 지수 : ' + print_yesterday_kospi, '/ 전일대비 ( '+kospi_updown.get_text()+','+kospi_persent.get_text()+' )')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print('>-<><|관심종목|><>-<')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# 종목 별 주식 정보 출력============================================================================================================
# 핫이슈 종목
# 이노룰스          296640
# 신라젠            215600
# 베트남개발1       096300
# 성우하이텍        015750

# 반도체 종목
# 삼성전자          005930
# DB하이텍          000990
# SK하이닉스        000660

# 카카오 4형제
# 카카오            035720
# 카카오뱅크        323410
# 카카오페이        377300
# 카카오게임즈      293490

# 게임 종목
# 펄어비스          263750
# 카카오게임즈      293490
# NCSOFT            036570
# NEXON             225570
# 크래프톤          259960
# NHN               181710
# 넷마블            251270 

# 메타버스 종목
# 넵튠               217270
# 위메이드          112040
# 미투온            201490
# 덱스터            206560
# 위지윅스튜디오    299900

# 헬스케어 종목
# 오스템임플        048260
# 덴티움            145720

# 기타 종목
# 쏘카              403550
# 대교              019680

def CheckCode(code):
    flag = False
    if code == '핫이슈':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|핫 이슈 주|><>-<\n')
        return flag
    elif code == '반도체':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|반도체 관련 주|><>-<\n')
        return flag
    elif code == '카카오':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|카카오 4형제|><>-<\n')
        return flag
    elif code == '게임':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|게임 관련 주|><>-<\n')
        return flag
    elif code == '메타버스':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|메타버스 관련 주|><>-<\n')
        return flag
    elif code == '헬스케어':
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|헬스케어 관련 주|><>-<\n')
        return flag
    elif code == "기타":
        flag = True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('>-<><|기타|><>-<\n')
        return flag
    else:
        return flag

codes = ['핫이슈','296640','215600','096300','015750','반도체','005930','000990','000660','카카오','035720','323410','377300','293490','게임','263750','293490','036570','225570','259960','181710','251270','메타버스','217270','112040','201490','206560','299900','헬스케어','048260','145720','기타','403550','019680'] # 종목코드 리스트


while (1):
    for code in codes:
        if CheckCode(code):
            continue
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
        
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.select_one('div.new_totalinfo')
        company = name.select_one('div > div > h2')
        today = soup.select_one('div.rate_info')
        info1 = today.select_one('div > p.no_today')
        price = info1.select_one('.blind')
        info2 = today.select_one('div > p.no_exday')
        context = info2.select('span')
        volumn = today.select_one('table.no_info')
        deal_volumn = volumn.select('span.blind')[3].get_text()
        deal_money = volumn.select('span.blind')[-1].get_text()
        today_cost = makenum(price.get_text())
        upordown_cost = makenum(context[2].get_text())
        yesterday_cost = ''

        if context[1].get_text() == '하락':
            yesterday_cost = int(today_cost) + int(upordown_cost)
            status = '-'
        elif context[1].get_text() == '보합':
            yesterday_cost = int(today_cost) + int(upordown_cost)
            status = 'o'
        else:
            yesterday_cost = int(today_cost) - int(upordown_cost)
            status = '+'
        percent_cost = round(int(upordown_cost)*100 / yesterday_cost, 2)
        print_yesterday_cost = makecomma(str(yesterday_cost))[::-1]

        print(status,'('+str(percent_cost)+'%'+')',company.get_text(), "=","|","거래량 : "+deal_volumn+"개","/","거래대금(백만원단위) : ",deal_money,"|","현재 금액 :",price.get_text()+'원', "| 어제 금액 :", print_yesterday_cost," |",context[0].get_text(), '(',context[2].get_text()+'원',context[1].get_text(), ')')

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
    # sleep(60)
    # system("pause")
    # system("cls")
    