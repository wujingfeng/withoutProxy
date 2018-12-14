#彭青山
#全国奖惩记录
import pymysql
import time
from withoutProxy.config.database import *


def allcountry_info_detail_pipline(data):
    print('--------allcountry_info_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute("select id from sc_gss_his where gsmc = %s", data['qymc'])
    id = cursor.fetchone()
    now = int(time.time())
    sql = "insert into gljs_goodrecord(gs_id,gsmc,dlink,bt,fwh,lb,jddw,xmmc,jdrq,nr,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    par = [id['id'],data['qymc'],data['dlink'],data['title'],data['fnumber'],data['type'],data['jddw'],data['xmmc'],data['jddate'],data['nr'],now,now]
    cursor.execute(sql,par)
    conn.commit()

    cursor.close()
    conn.close()
