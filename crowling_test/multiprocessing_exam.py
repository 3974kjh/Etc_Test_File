import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import finance_DB

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

codes = ['296640','215600','096300','015750','005930','000990','000660','035720','323410','377300','293490','263750','293490','036570','225570','259960','181710','251270','217270','112040','201490','206560','299900','048260','145720','403550','019680'] # 종목코드 리스트

def get_content(code):
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

if __name__=='__main__':
    pool = Pool(processes=4)
    pool.map(get_content, codes)
    # pool.close()
    # pool.join()