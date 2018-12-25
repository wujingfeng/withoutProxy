import pymysql
import time
from withoutProxy.config.cj_database import *

# 水利建设 公司id
def slj_id_detail_pipline(data):
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
    urls = [
        'http://rcpu.cwun.org/General/NBASE.aspx?id='+id, # 基本信息
        'http://rcpu.cwun.org/General/NPER_Z.aspx?id='+id+"", # 人员
        'http://rcpu.cwun.org/General/NPROJ_Z.aspx?id='+id+'', # 业绩
        'http://rcpu.cwun.org/General/NCRED_Z.aspx?id='+id, # 良好
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