import threading
import time

# def printhi():
#     print("hi")

# threading.Timer(5, printhi).start()
# printhi()

# hi = []
# print(len(hi))

# def test():
#     hi = []
#     hi.append(1)
#     hi.append(2)
#     print(hi)
#     return hi

# hi = test()
def removeZero(items):
    removed_items = []

    for item in items:
        if item != 0:
            removed_items.append(item)
    return removed_items

Kospi_volatile_item = [[1200,10],[1520,20],[0,0],[0,0],[250,10],[250,15],[0,0]]
test_list = [[1,1,1,1,1,'1번',1423,132],[1,1,1,1,1,'2번',1523,132],[1,1,1,1,1,'3번',423,12],[1,1,1,1,1,'4번',0,0],[1,1,1,1,1,'5번',10,210]]

EPS_list = []
BPS_list = []
for item in Kospi_volatile_item:
    if item[0] != 0:
        EPS_list.append(item[0])
    if item[1] != 0:
        BPS_list.append(item[1])
EPS_AVG = sum(EPS_list) // len(EPS_list)
BPS_AVG = sum(BPS_list) // len(BPS_list)

result_list = []
print(EPS_AVG, BPS_AVG)
for item in test_list:
    if item[-2] > EPS_AVG and item[-1] > BPS_AVG:
        result_list.append(item[-3])
print(result_list)