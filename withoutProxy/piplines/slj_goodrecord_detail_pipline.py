#彭青山
#全国水利良好
import pymysql
import time
from withoutProxy.config.database import *


def slj_goodrecord_detail_pipline(data):
    print('--------slj_goodrecord_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    now = int(time.time())
    cursor = conn.cursor()
    sql = "insert into slj_statistic(`cj_id`,`gs_id`,`gsmc`,`p_type`,`s_type`,`total`) VALUES (%s,%s,%s,%s,%s,%s) "
    for list in data['tmp_list']:
        par = [list['cj_id'],list['gs_id'],list['gsmc'],list['p_type'],list['s_type'],list['total']]
        cursor.execute(sql, par)

    conn.commit()
    cursor.close()
    conn.close()
