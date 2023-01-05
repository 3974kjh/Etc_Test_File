# hi = {1 : '농업', 2 : '수산업'}

# # print(hi[1])
# # print(hi[2])

# hello = [('12','24','151'),('42','5125','524')]

# # hi = 1.116
# # print(round(hi,2))

# h = ["1","2","3"]

# h.insert(2,"4")
# # => h = ["1", "2", "4", "3"]
# # print(h)

# import time


# def returntime(start, end):
#     total_time = round(end - start, 2)
#     if total_time >= 60:
#         min = int(total_time) // 60
#     else:
#         min = 0
#     second = round(total_time % 60)

#     printTime = str(min) + '분' + " " + str(second) + '초'
#     return printTime

# start = time.time()

# time.sleep(8.5)

# print(returntime(start, time.time()))

# hi = [[1,2,3],[1,2,3]]
# hello = [[1,3,2],[4,1,2]]
# jjj = [[142,414,42],[1312,312,31]]
# hi += hello +jjj
# print(hi)

# def SumMatricsByTwo(matrics):
#     sum = 0
#     for item in matrics:
#         sum += item[0]
#     return sum

# hi = [[1,2,3],[2,3,4],[5,6,1]]
# print(SumMatricsByTwo(hi))

# hi = None
# print(type(hi))
# import sys, os
# sys.path.append('C:\\Users\\samsung\\Desktop\\Python_project\\finace_program_V2.0')
# import finance_DB_V2

# Good_Invest_Real_list = [['006040', 'kospi'],
# ['030720','kospi'],
# ['222980','kosdaq'],
# ['208140','kosdaq'], ['276730','kosdaq']]

# def MakePreCode(code):
#     for idx in range(len(code)):
#         if code[idx] == '0':
#             continue
#         elif '0' <= code[-1] <= '9':
#             return code[idx:]
#         else:
#             return code

# DatabaseStart = finance_DB_V2.Database()
# result = []
# for item in Good_Invest_Real_list:
#     print(MakePreCode(item[0]))
#     # result.append(DatabaseStart.UpdateCount(MakePreCode(item[0]), item[1]))
#     # print(result)