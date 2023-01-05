import pandas as pd
import os
from datetime import datetime

highly_volatile_item = [["111","123",1],["222","123",3],["333","123",3]]
df = pd.DataFrame(highly_volatile_item, columns=['코드','회사명','점수'])
df1 = pd.DataFrame(highly_volatile_item, columns=['코드','회사명','점수'])
df2 = pd.DataFrame(highly_volatile_item, columns=['코드','회사명','점수'])
nowdate = str(datetime.now().date()) + '.xlsx'
path = 'C:/Users/Osstem/Desktop/'+ nowdate
excel_list = [[df, 'kospi'],[df1, 'kosdoc'],[df2, 'total']]
with pd.ExcelWriter(path) as writer:
    for item, name in excel_list:
        item.to_excel(writer, sheet_name=name, index = False)

# 참고 : https://ponyozzang.tistory.com/619