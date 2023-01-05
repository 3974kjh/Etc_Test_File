import requests, sys
from bs4 import BeautifulSoup
# import finance_DB
from multiprocessing import Pool

def printProgress(iteration, total, prefix = '', suffix = '', barLength = 100): 
    percent = round(100 * (iteration / total), 1)
    filledLength = int(round(barLength * iteration / total, 1))
    bar = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

# #오류검출 테스트
# here = []
# count = 0
# for item in finance_DB.Kospi_codes:
#     for code, hi, hello in item:
#         url = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + code

#         response = requests.get(url)
#         response.raise_for_status()
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')
#         test = soup.select_one('div.cmp-table-div')
#         test_test = test.select('b')
#         if "" == test_test[1].get_text() or "N/A" == test_test[1].get_text():
#             EPS = 0
#         else:
#             EPS = int(test_test[1].get_text().replace(',', ''))
#         if "" == test_test[2].get_text() or "N/A" == test_test[2].get_text():
#             BPS = 0
#         else:
#             BPS = int(test_test[2].get_text().replace(',', ''))
#         if "" == test_test[3].get_text() or "N/A" == test_test[3].get_text():
#             PER = 0
#         else:
#             PER = float(test_test[3].get_text())
#         if "" == test_test[4].get_text() or "N/A" == test_test[4].get_text():
#             Sector_PER = 0
#         else:
#             Sector_PER = float(test_test[4].get_text())
#         if "" == test_test[5].get_text() or "N/A" == test_test[5].get_text():
#             PBR = 0
#         else:
#             PBR = float(test_test[5].get_text())
#         if "" == test_test[6].get_text() or "N/A" == test_test[6].get_text():
#             Dividend_Rate = 0
#         else:    
#             Dividend_Rate = test_test[6].get_text()
#         here.append([EPS, BPS, PER, Sector_PER, PBR, Dividend_Rate])
#         count+=1
#         printProgress(count, 940, "start", "wait...", 100)

# error = 0
# for i in here:
#     if len(i) != 6:
#         error+=1
# print(error)


# url = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + '096300'

# response = requests.get(url)
# response.raise_for_status()
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# test = soup.select_one('div.cmp-table-div')
# test_test = test.select('b')
# if "" == test_test[1].get_text():
#     EPS = 0
# else:
#     EPS = int(test_test[1].get_text().replace(',', ''))
# if "" == test_test[2].get_text():
#     BPS = 0
# else:
#     BPS = int(test_test[2].get_text().replace(',', ''))
# if "" == test_test[3].get_text():
#     PER = 0
# else:
#     PER = float(test_test[3].get_text())
# if "" == test_test[4].get_text():
#     Sector_PER = 0
# else:
#     Sector_PER = float(test_test[4].get_text())
# if "" == test_test[5].get_text():
#     PBR = 0
# else:
#     PBR = float(test_test[5].get_text())
# if "" == test_test[6].get_text():
#     Dividend_Rate = 0
# else:    
#     Dividend_Rate = test_test[6].get_text()
# print(EPS,BPS,PER,Sector_PER,PBR,Dividend_Rate)

# # MultiProcessing Crawling 방식 1
# code = [['141000','082920','035600','047310','043150','091990','039440','054450','067000','122870'], 
# ['230360', '178320','189980','247540','319660','192440','361390','051370','200670','299900','030520','089600','054950','146320','282880','078340','403870']]

# def get_content(code):
#     url = 'https://finance.naver.com/item/main.nhn?code=' + code
#     response = requests.get(url)
#     response.raise_for_status()
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     # 52주 최고, 최저 찾고 숫자로 만들기
#     fiftyTwoWeek = soup.find('div', id = 'tab_con1')
#     fiftyTwoWeek_item = fiftyTwoWeek.select('em')
#     cnt += 1
#     return fiftyTwoWeek_item[1].get_text()

# if __name__=='__main__':
#     full = []
#     pool = Pool(processes=4)
#     for item in code:
#         full = pool.map(get_content, item)
#     print(full)

# # MultiProcessing Crawling 방식 2
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# from selenium import webdriver

# code = [['141000','082920','035600','047310','043150','091990','039440','054450','067000','122870'], 
# ['230360', '178320','189980','247540','319660','192440','361390','051370','200670','299900','030520','089600','054950','146320','282880','078340','403870']]

# def get_content(code):
#     url1 = 'https://finance.naver.com/item/main.nhn?code=' + code
#     response1 = requests.get(url1)
#     response1.raise_for_status()
#     html1 = response1.text

#     url2 = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + code
#     response2 = requests.get(url2)
#     response2.raise_for_status()
#     html2 = response2.text

#     kospi_kosdaq_url = 'https://finance.naver.com/item/sise_day.naver?code=' + code
#     driver.get(kospi_kosdaq_url)
#     html3 = driver.page_source

#     return [html1, html2, html3]

# full = []
# hi = []
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

# if __name__=='__main__':
#     count = 0
#     pool = Pool(processes=4)
#     for item in code:
#         full = pool.map(get_content, item)
#         here = []
#         # 52주 최고, 최저 찾고 숫자로 만들기
#         for html1, html2, html3 in full:
#             soup1 = BeautifulSoup(html1, 'html.parser')
#             fiftyTwoWeek = soup1.find('div', id = 'tab_con1')
#             fiftyTwoWeek_item = fiftyTwoWeek.select('em')

#             soup2 = BeautifulSoup(html2, 'html.parser')
#             test = soup2.select_one('div.cmp-table-div')
#             test_test = test.select('b')
#             if "" == test_test[1].get_text() or "N/A" == test_test[1].get_text():
#                 EPS = 0
#             else:
#                 EPS = int(test_test[1].get_text().replace(',', ''))

#             soup = BeautifulSoup(html3, 'html.parser')
#             volumne_value = soup.select('span')

#             here.append([fiftyTwoWeek_item[1].get_text(), EPS, volumne_value[1].get_text()])
#             count += 1
#             printProgress(count, 27, "start", "wait...", 100)
#         hi += here
#     print(hi)

# test = '001492'

# def MakePreCode(code):
#     pre_code = ''
#     for item in code:
#         if item != '0':
#             pre_code += item
#     return pre_code

# print(MakePreCode(test))
