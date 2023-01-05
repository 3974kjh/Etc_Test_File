import requests, sys
from bs4 import BeautifulSoup
import finance_DB

def printProgress(iteration, total, prefix = '', suffix = '', barLength = 100): 
    percent = round(100 * (iteration / total), 1)
    filledLength = int(round(barLength * iteration / total, 1))
    bar = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

#오류검출 테스트
here = []
count = 0
for item in finance_DB.Kospi_codes:
    for code, hi, hello in item:
        url = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' + code

        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        test = soup.select_one('div.cmp-table-div')
        test_test = test.select('b')
        if "" == test_test[1].get_text() or "N/A" == test_test[1].get_text():
            EPS = 0
        else:
            EPS = int(test_test[1].get_text().replace(',', ''))
        if "" == test_test[2].get_text() or "N/A" == test_test[2].get_text():
            BPS = 0
        else:
            BPS = int(test_test[2].get_text().replace(',', ''))
        if "" == test_test[3].get_text() or "N/A" == test_test[3].get_text():
            PER = 0
        else:
            PER = float(test_test[3].get_text())
        if "" == test_test[4].get_text() or "N/A" == test_test[4].get_text():
            Sector_PER = 0
        else:
            Sector_PER = float(test_test[4].get_text())
        if "" == test_test[5].get_text() or "N/A" == test_test[5].get_text():
            PBR = 0
        else:
            PBR = float(test_test[5].get_text())
        if "" == test_test[6].get_text() or "N/A" == test_test[6].get_text():
            Dividend_Rate = 0
        else:    
            Dividend_Rate = test_test[6].get_text()
        here.append([EPS, BPS, PER, Sector_PER, PBR, Dividend_Rate])
        count+=1
        printProgress(count, 940, "start", "wait...", 100)

error = 0
for i in here:
    if len(i) != 6:
        error+=1
print(error)

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