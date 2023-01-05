from os import system
from threading import Thread
from pyautogui import sleep
import requests, sys
from bs4 import BeautifulSoup

def makenum(A):
    if ('N/A' == A):
        return 0
    num = ''
    for cost in A:
        if cost != ',':
            num +=cost
    return int(num)

url = "https://finance.naver.com/item/main.naver?code=" + '028670'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
category = soup.find('div', id = 'tab_con1')
category_sub1 = category.select('em')

print(len(category_sub1))

for item in range(len(category_sub1)):
    print(category_sub1[item].get_text())
print(float(category_sub1[8].get_text()))