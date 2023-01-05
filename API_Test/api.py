import requests
import setting

# HTTP요청에 따른 함수 사용
# GET 방식: requests.get()
# POST 방식: requests.post()
# PUT 방식: requests.put()
# DELETE 방식: requests.delete()

# # 내가 보낸 request 객체에 접근 가능
# response.request
# # 응답 코드
# response.status_code
# # 200 (OK 코드)이 아닌 경우 에러 raise
# response.raise_for_status()
# # json response일 경우 딕셔너리 타입으로 바로 변환
# response.json()
# # content 속성을 통해 바이너리 타입으로 데이터를 받을 수 있다.
# response.content
# # text 속성을 통해 UTF-8로 인코딩된 문자열을 받을 수 있다.
# response.text
# # encoding 정보 확인
# response.encoding

bank_area_code = [
    setting.bankAreaEnum.은행.value, 
    setting.bankAreaEnum.여신전문.value, 
    setting.bankAreaEnum.저축은행.value, 
    setting.bankAreaEnum.보험.value, 
    setting.bankAreaEnum.금융투자.value
    ]
bank_code = [
    setting.bankEnum.경남은행.value,
    setting.bankEnum.광주은행.value,
    setting.bankEnum.국민은행.value,
    setting.bankEnum.농협은행주식회사.value,
    setting.bankEnum.대구은행.value,
    setting.bankEnum.부산은행.value,
    setting.bankEnum.새마을금고.value,
    setting.bankEnum.수협은행.value,
    setting.bankEnum.신한은행.value,
    setting.bankEnum.우리은행.value,
    setting.bankEnum.전북은행.value,
    setting.bankEnum.제주은행.value,
    setting.bankEnum.중소기업은행.value,
    setting.bankEnum.카카오뱅크.value,
    setting.bankEnum.케이뱅크.value,
    setting.bankEnum.토스뱅크.value,
    setting.bankEnum.하나은행.value,
    setting.bankEnum.한국산업은행.value,
    setting.bankEnum.한국스탠다드차타드은행.value,
    ]

def MakeAvg(list_A):
    return round(sum(list_A) / len(list_A), 2)

적금_list = []
for bankCode in bank_code:
    params = {
        'auth' : setting.API_KEY,
        'topFinGrpNo' : bank_area_code[0],
        'pageNo' : setting.PAGE_NUM,
        'financeCd' : bankCode
    }

    적금_responce = requests.get(setting.적금_URL, params=params)
    if 적금_responce.status_code != 200:
        print("응답 실패" + str(적금_responce.status_code))
    else:
        적금_금리 = []
        적금_우대금리 = []
        if 적금_responce.json()[setting.commonEnum.결과.value]['err_cd'] == '101':
            continue
        for base in 적금_responce.json()[setting.commonEnum.결과.value][setting.commonEnum.상품.value]:
            for option in 적금_responce.json()[setting.commonEnum.결과.value][setting.commonEnum.상품디테일.value]:
                if option[setting.commonEnum.금융상품코드.value] == base[setting.commonEnum.금융상품코드.value]:
                    if option[setting.option적금Enum.금리.value] != None:
                        적금_금리.append(option[setting.option적금Enum.금리.value])
                    if option[setting.option적금Enum.우대금리.value] != None:
                        적금_우대금리.append(option[setting.option적금Enum.우대금리.value])
        if (len(적금_금리) != 0 or len(적금_우대금리) != 0):
            적금_금리_avg = MakeAvg(적금_금리)
            적금_우대금리_avg = MakeAvg(적금_우대금리)
            적금_list.append([base[setting.base적금Enum.은행이름.value],적금_금리_avg, 적금_우대금리_avg])
print(적금_list)

예금_list = []
for bankCode in bank_code:
    params = {
        'auth' : setting.API_KEY,
        'topFinGrpNo' : bank_area_code[0],
        'pageNo' : setting.PAGE_NUM,
        'financeCd' : bankCode
    }

    예금_responce = requests.get(setting.예금_URL, params=params)
    if 예금_responce.status_code != 200:
        print("응답 실패" + str(예금_responce.status_code))
    else:
        예금_금리 = []
        예금_우대금리 = []
        if 예금_responce.json()[setting.commonEnum.결과.value]['err_cd'] == '101':
            continue
        for base in 예금_responce.json()[setting.commonEnum.결과.value][setting.commonEnum.상품.value]:
            for option in 예금_responce.json()[setting.commonEnum.결과.value][setting.commonEnum.상품디테일.value]:
                if option[setting.commonEnum.금융상품코드.value] == base[setting.commonEnum.금융상품코드.value]:
                    if option[setting.option예금Enum.금리.value] != None:
                        예금_금리.append(option[setting.option예금Enum.금리.value])
                    if option[setting.option예금Enum.우대금리.value] != None:
                        예금_우대금리.append(option[setting.option예금Enum.우대금리.value])
        if (len(예금_금리) != 0 or len(예금_우대금리) != 0):
            예금_금리_avg = MakeAvg(예금_금리)
            예금_우대금리_avg = MakeAvg(예금_우대금리)
            예금_list.append([base[setting.base예금Enum.은행이름.value],예금_금리_avg, 예금_우대금리_avg])
print(예금_list)