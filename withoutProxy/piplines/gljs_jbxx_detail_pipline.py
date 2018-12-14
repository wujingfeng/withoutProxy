import pymysql
from withoutProxy.config.database import *

# 全国公路基本信息
# 孙国强
def gljs_jbxx_detail_pipline(data):
    print('--------gljs_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT,
        cursorclass = pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    if 'qymc' in data.keys():  # 新增数据到 基本信息表
        cursor.execute("select id from sc_gss_his where gsmc = %s", data['qymc'])  # 查询公司表gs_id
        repetition = cursor.fetchone()
        if repetition:
            gs_id = repetition['id']
            proj_id = data['corpCode']  # 业绩表id
        sql = "insert into gljs_baseinfo(proj_id,gs_id,qymc,corpCode,link,zzjgdm,zcsf,zccs,cymc,xzzgbm,yyzzzch,zczj,qylx,qyxz,yyzzzcrq,clrq,fddbr,fddbzc,qyfzr,qyfzrzc,jsfzr,jsfzrzc,shxydm,yyfw,qyqk,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        par = [proj_id,gs_id,data['qymc'],data['corpCode'],data['link'],data['zzjgdm'],data['zcsf'],data['zccs'],data['cymc'],data['xzzgbm'],data['yyzzzch'],data['zczj'],data['qylx'],data['qyxz'],data['yyzzzcrq']
            ,data['clrq'],data['fddbr'],data['fddbrzc'],data['qyfzr'],data['qyfzrzc'],data['jsfzr'],data['jsfzrzc'],data['shxydm'],data['yyfw'],data['qyqk'],data['created'],data['modified']]
        cursor.execute(sql,par)
        conn.commit()
    if 'gsmc' in data.keys():  # 新增数据到 信用表
        cursor.execute("select id from gljs_baseinfo where  corpCode = %s", data['companyId'])
        repetition = cursor.fetchone()
        if repetition:
            gs_id = repetition['id']
            mysql = 'insert into gljs_creditrating(gs_id,gsmc,url,pjsf,pjnf,dj,gszt,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            par = [gs_id, data['gsmc'], data['url'], data['pjsf'], data['pjnf'], data['dj'], data['gszt'],
                        data['created'], data['modified']]

            cursor.execute(mysql, par)

            conn.commit()

    cursor.close()
    conn.close()
