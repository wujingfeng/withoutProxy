import time

import pymysql

from withoutProxy.config.database import *

def slj_yj_detail_pipline(data):
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQLS_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT,
        cursorclass = pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    for i in data['jbxx_list']:
        cursor.execute("select id from sc_gss_his where gsmc = %s", i['gsmc'])  # 查询公司表gs_id
        repetition = cursor.fetchone()
        created = int(time.time())
        modified = int(time.time())
        if repetition:
            gs_id = repetition['id']
        else:
            gs_id = 0
        cursor.execute("select id from slj_gcyj_jbxx where link = %s",i['link'])
        repetition = cursor.fetchone()
        if repetition:
            print('已存在')
            pass
        else:
            # 业绩基本信息
            sql = "insert into slj_gcyj_jbxx(gs_id,gsmc,xmmc,xmbh,htmc,gczt,szd,xmfzr,jsfzr,jsdw,gcdj_db,gcdj_jb,kgrq,wgrq,htgq,gjzb,htje,jsje,zynr,`type`,xglsjl,link,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            par = [gs_id, i['gsmc'], i['xmmc'], i['xmbh'], i['htmc'], i['gczt'],i['szd'], i['xmfzr'], i['jsfzr'], i['jsdw'], i['gcdj_db'],i['gcdj_jb'], i['kgrq'], i['wgrq'], i['htgq'],
                           i['gjzb'], i['htje'], i['jsje'], i['zynr'], i['type'], i['xglsjl'], i['link'], created, modified]
            cursor.execute(sql, par)



    # 业绩人员信息
    for i in data['ryxx_list']:
        cursor.execute("select id from sc_gss_his where gsmc = %s", i['gsmc'])  # 查询公司表gs_id
        repetition = cursor.fetchone()
        created = int(time.time())
        modified = int(time.time())
        if repetition:
            gs_id = repetition['id']
        else:
            gs_id = 0
        cursor.execute("select id from slj_gcyj_jbxx where link = %s", i['link'])  # 查询基本信息表jbxx_id
        repetition = cursor.fetchone()
        if repetition:
            jbxx_id = repetition['id']
        # 业绩人员信息
        sql = "insert into slj_gcyj_ry(jbxx_id,gs_id,gsmc,xmmc,`name`,zw,zc,zsmc,zsbh,zszy,dj,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        par = [jbxx_id, gs_id, i['gsmc'], i['xmmc'], i['name'], i['zw'], i['zc'],i['zsmc'], i['zsbh'], i['zszy'], i['dj'],created, modified]
        cursor.execute(sql, par)

    # 业绩工程获奖
    for i in data['hjxx_list']:
        cursor.execute("select id from sc_gss_his where gsmc = %s", i['gsmc'])  # 查询公司表gs_id
        repetition = cursor.fetchone()
        created = int(time.time())
        modified = int(time.time())
        if repetition:
            gs_id = repetition['id']
        else:
            gs_id = 0
        cursor.execute("select id from slj_gcyj_jbxx where xmmc = %s", i['xmmc'])  # 查询基本信息表jbxx_id
        repetition = cursor.fetchone()
        if repetition:
            jbxx_id = repetition['id']

        # 业绩获奖信息
        sql = "insert into slj_gcyj_hj(jbxx_id,gs_id,gsmc,xmmc,jxmc,jxlb,jxjb,jxdb,bjdw,bjwh,bjsj,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        par = [jbxx_id, gs_id, i['gsmc'], i['xmmc'], i['jxmc'], i['jxlb'], i['jxjb'],i['jxdb'], i['bjdw'], i['bjwh'], i['bjsj'],created, modified]
        cursor.execute(sql, par)

    # 统计信息表
    for i in data['tjxx_list']:
        cursor.execute("select id from sc_gss_his where gsmc = %s", i['gsmc'])  # 查询公司表gs_id
        repetition = cursor.fetchone()
        created = int(time.time())
        modified = int(time.time())
        if repetition:
            gs_id = repetition['id']
        else:
            gs_id = 0
        # 统计信息
        sql = "insert into slj_statistic(cj_id,gs_id,gsmc,p_type,s_type,total,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        par = [i['cj_id'], gs_id, i['gsmc'], i['p_type'], i['s_type'], i['total'],created, modified]
        cursor.execute(sql, par)
    conn.commit()
    cursor.close()
    conn.close()

