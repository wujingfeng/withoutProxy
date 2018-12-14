import pymysql
import time
from withoutProxy.config.cj_database import *

# 公路工程建设 id
def gljs_id_detail_pipline(data):
    print('--------gljs_id_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT
    )
    cursor = conn.cursor()

    id = data['comp_id']
    # gsmc = data['gsmc']
    # sql = "UPDATE gljs_comp_id SET comp_id = '"+id+"' WHERE gsmc = '"+gsmc+"'"
    urls = [
        'http://glxy.mot.gov.cn/company/CompanyInfo.do?comId='+id, # 基本信息
        'http://glxy.mot.gov.cn/person/getPersonList.do?page=1&rows=15&comId='+id+"&type=0", # 人员
        'http://glxy.mot.gov.cn/company/getCompanyAchieveList.do?companyId='+id+'&type=1a', # 业绩
        'http://glxy.mot.gov.cn/awards/getAwardsList.do?comId='+id, # 良好
        'http://glxy.mot.gov.cn/evaluate/getEvaluateList.do?compId='+id #信用等级

    ]
    sql = "replace into task(url) VALUES(%s)"
    par = urls

    try:
        cursor.executemany(sql,par)
        conn.commit()
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()