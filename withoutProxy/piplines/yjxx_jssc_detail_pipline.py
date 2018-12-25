#张峻珲
#全国公路建设市场(业绩信息)

import pymysql
import time

from withoutProxy.config.database import *


def yjxx_jssc_detail_pipline(data):
    print('--------yjxx_jssc_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT
    )
    cursor = conn.cursor()
    time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ts = int(time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S")))
    sql = 'select count(*) from gljs_yeji where proj_id = %s'
    cursor.execute(sql,data['proj_id'])
    rows = cursor.fetchall()
    if rows[0][0] == 0:
        sql = 'INSERT into gljs_yeji(gs_id,proj_id,gsmc,xmmc,link,htj,jsj,kgsj,zygcl,yz,zf,szsf,yj_type,bdlx,bdmc,zbqy,sfwg,jgysdf,jsgm,other,xmlx,jsdj,htdmc,jgrq,jgsj,kszh,jszh,zlpdqk,xmdm,valid,created,modified) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        par = [data['gs_id'],data['proj_id'],data['gsmc'],data['xmmc'],data['link'],data['htj'],data['jsj'],data['kgsj'],data['zygcl'],data['yz'],data['zf'],data['szsf'],data['yj_type'],data['bdlx'],data['bdmc'],data['zbqy'],data['sfwg'],data['jgysdf'],data['jsgm'],data['other'],data['xmlx'],data['jsdj'],data['htdmc'],data['jgrq'],data['jgsj'],data['kszh'],data['jszh'],data['zlpdqk'],data['xmdm'],data['valid'],ts,ts]
        cursor.execute(sql,par)
        conn.commit()
        id = int(cursor.lastrowid)
        sql = 'insert into gljs_yeji_glry(yj_id,gs_id,gsmc,xmmc,name,gw,rzsj,type,created,modified) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for i in data['ry_list']:
            time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            ts = int(time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S")))
            par = [id,data['gs_id'],i['gsmc'],i['xmmc'],i['name'],i['gw'],i['rzsj'],i['type'],ts,ts]
            cursor.execute(sql, par)
            conn.commit()
        cursor.close()
        conn.close()