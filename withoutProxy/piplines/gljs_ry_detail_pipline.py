import pymysql
import time
from withoutProxy.config.database import *

# 公路建设 人员
def gljs_ry_detail_pipline(data):
    print('--------scjst_info_detail_pipline--------')
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT
    )

    timeArray = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    created = int(time.mktime(time.strptime(timeArray, "%Y-%m-%d %H:%M:%S")))
    cursor = conn.cursor()
    # 人员信息
    rysql = "INSERT INTO gljs_person(staff_id,gs_id,gljs_xm,gljs_xb,gljs_birth,idcard,gsmc,gljs_xl,gljs_byyx,gljs_sxzy,gljs_zw,gljs_ksgznf,person_link,created,modified,gljs_type,xxly) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # 个人业绩
    yjsql = "INSERT INTO gljs_gryj(staff_id,proj_id,gljs_xm,gsmc,person_link,gljs_xmname,gljs_bdname,gljs_drzw,gljs_start_time,gljs_end_time,gljs_type,xxly,created,modified) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # 职称信息
    zcsql = "INSERT INTO gljs_zcxx(staff_id,zc,zsbh,zczy,hfjg,hfrq,created) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # zcsql = "insert into gljs_zcorzy(ry_id,gs_id,gljs_xm,gsmc,person_link,gljs_zcname,gljs_fztime,gljs_fzjg,gljs_zcnumber,gljs_zclb,gljs_type,xxly,created)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # 执业信息
    cysql = "INSERT INTO gljs_zyzgxx(staff_id,zclb,zcdj,fzjg,zsbh,fzrq,zcyxqz,created) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # cysql = "insert into gljs_zcorzy(ry_id,gs_id,gljs_xm,gsmc,person_link,gljs_fztime,gljs_fzjg,gljs_zyjb,gljs_yxtime,gljs_zsnumber,gljs_type,xxly,created)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # 履历信息
    flsql = "INSERT INTO gljs_llxx(staff_id,gsmc,xm,zwlx,zw,rzzt,rzsj,lzsj,created) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # 查询表中是否有这个公司名称
    sql = 'SELECT id FROM sc_gss_his WHERE gsmc=(%s)'
    par = [data['jbxx_list']['gsmc']]
    cursor.execute(sql, par)
    results = cursor.fetchone()

    if results:

        # 人员信息
        rypar = [data['jbxx_list']['staff_id'], results, data['jbxx_list']['gljs_xm'], data['jbxx_list']['gljs_xb'],
                 data['jbxx_list']['gljs_birth'],data['jbxx_list']['idcard'],
                 data['jbxx_list']['gsmc'], data['jbxx_list']['gljs_xl'], data['jbxx_list']['gljs_byyx'],
                 data['jbxx_list']['gljs_sxzy'], data['jbxx_list']['gljs_zw'],
                 data['jbxx_list']['gljs_ksgznf'], data['jbxx_list']['person_link'], created,created,
                 data['jbxx_list']['gljs_type'], data['jbxx_list']['xxly']]
        cursor.execute(rysql, rypar)

        # 个人业绩
        for list in data['gryj_list_list']:
            yjpar = [data['jbxx_list']['staff_id'],list['proj_id'], data['jbxx_list']['gljs_xm'], list['gsmc'],
                     data['jbxx_list']['person_link'], list['gljs_xmname'],
                     list['gljs_bdname'],
                     list['gljs_drzw'], list['gljs_start_time'], list['gljs_end_time'], '个人业绩', '公路建设网', created,created]
            try:
                cursor.execute(yjsql, yjpar)
            except Exception as a:
                print(a)

        # 职称信息
        for list in data['zcxx_list']:
            zcpar = [data['jbxx_list']['staff_id'], list['zcc'], list['zsbh'], list['zczy'], list['hfjg'], list['hfrq'],
                     timeArray]
            try:
                cursor.execute(zcsql, zcpar)
            except Exception as a:
                print(a)

        # 执业信息
        for list in data['zyzgxx_list']:
            cypar = [data['jbxx_list']['staff_id'], list['zclb'], list['zcdj'], list['fzjg'], list['zsbh'],
                     list['fzrq'], list['zcyxqz'], timeArray]
            try:
                cursor.execute(cysql, cypar)
            except Exception as a:
                print(a)

        # 履历信息
        for list in data['flxx_list']:
            flpar = [data['jbxx_list']['staff_id'], list['gsmc'], data['jbxx_list']['gljs_xm'], list['zwlx'],
                     list['zw'], list['rzzt'],
                     list['rzsj'], list['lzsj'], timeArray]
            try:
                cursor.execute(flsql, flpar)
            except Exception as a:
                print(a)
    conn.commit()
    cursor.close()
    conn.close()