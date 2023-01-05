from enum import Enum

# api 및 참고 홈페이지
# http://finlife.fss.or.kr/PageLink.do?link=openapi/detail02&menuId=2000126
# https://www.knowingasset.com/app/product/savings/0010024/21000111

# 'region/endregion' 사용 커멘드 키 : Ctrl + M,R

예금_URL = "http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?"
적금_URL = "http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?"
API_KEY = "e5accbd69194b9c4049f9b8206e4dcad"
PAGE_NUM = 1

class commonEnum(Enum):
    공시제출월 = 'dcls_month'       #공통
    금융회사코드 = 'fin_co_no'      #공통
    금융상품코드 = 'fin_prdt_cd'    #공통
    결과 = 'result'
    상품 = 'baseList'
    상품디테일 = 'optionList'

# region [예금 Enum]
class base예금Enum(Enum):
    은행이름 = 'kor_co_nm'
    상품명 = 'fin_prdt_nm'
    가입방법 = 'join_way'
    만기후이자율 = 'mtrt_int'
    우대조건 = 'spcl_cnd'
    가입대상 = 'join_member'
    가입제한 = 'join_deny'
    유의사항 = 'etc_note'
    최고한도 = 'max_limit'
    공시시작일 = 'dcls_strt_day'
    공시종료일 = 'dcls_end_day'
    금융회사제출일 = 'fin_co_subm_day'

class option예금Enum(Enum):
    이자유형명 = 'intr_rate_type_nm'
    이자유형 = 'intr_rate_type'
    기간월 = 'save_trm'
    금리 = 'intr_rate'
    우대금리 = 'intr_rate2'
# endregion

# region [적금 Enum]
class base적금Enum(Enum):
    은행이름 = 'kor_co_nm'
    상품명 = 'fin_prdt_nm'
    가입방법 = 'join_way'
    만기후이자율 = 'mtrt_int'
    우대조건 = 'spcl_cnd'
    가입대상 = 'join_member'
    가입제한 = 'join_deny'
    유의사항 = 'etc_note'
    최고한도 = 'max_limit'
    공시시작일 = 'dcls_strt_day'
    공시종료일 = 'dcls_end_day'
    금융회사제출일 = 'fin_co_subm_day'

class option적금Enum(Enum):
    이자유형명 = 'intr_rate_type_nm'
    이자유형 = 'intr_rate_type'
    적립유형명 = 'rsrv_type_nm'
    적립유형 = 'rsrv_type' 
    기간월 = 'save_trm'
    금리 = 'intr_rate'
    우대금리 = 'intr_rate2'
# endregion

class bankAreaEnum(Enum):
    은행 = '020000'
    여신전문 = '030200'
    저축은행 = '030300'
    보험 = '050000'
    금융투자 = '060000'

class bankEnum(Enum):
    경남은행 = '0010024'
    광주은행 = '0010019'
    국민은행 = '0010927'
    농협은행주식회사 = '0013175'
    대구은행 = '0010016'
    부산은행 = '0010017'
    새마을금고 = '0090045'
    수협은행 = '0014807'
    신한은행 = '0011625'
    우리은행 = '0010001'
    전북은행 = '0010022'
    제주은행 = '0010020'
    중소기업은행 = '0010026'
    카카오뱅크 = '0015130'
    케이뱅크 = '0014674'
    토스뱅크 = '0017801'
    하나은행 = '0013909'
    한국산업은행 = '0010030'
    한국스탠다드차타드은행 = '0010002'