# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time

from withoutProxy.config.database import *

#---------- 唐 - 水利建设-人员信息

def slj_ry_detail_pipline(data):
    print('--------scjst_info_detail_pipline--------')
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
    timeArray = int(time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S")))

    # 查询表中是否有这个公司名称
    sql = 'SELECT id FROM sc_gss_his WHERE gsmc=(%s)'
    par = [data['data_list'][0]['gsmc']]
    cursor.execute(sql, par)
    gs_id = cursor.fetchone()

    sql = "insert into slj_ry(cj_id,gs_id,gsmc,xm,sfzh,zw,zgzbh,zc,zgzsh,zczsh,yxqz,zczy,zczsbh,dj,zylb,zszy," \
          "gw,gwzsh,zslb,zsbh,zygz,fzjg,zcyzy,start_year,zybh,xl,fzzzlb,ssbm,lb,ry_type,created,modified,link) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    sql_lb = "insert into slj_statistic(cj_id,gs_id,gsmc,p_type,s_type,total) VALUES (%s,%s,%s,%s,%s,%s)"

    sql_zgzs = 'insert into slj_active_staff(cj_id,gs_id,gsmc,year,ryzs,gjzcrs,zjzcrs,cjzcrs,bs,ss,bk,zk,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    if gs_id:
        # 人员类型
        for lb in data['lsj_lb_list']:
            par_lb = [data['data_list'][0]['cj_id'], gs_id, data['data_list'][0]['gsmc'], '人员', lb['s_type'],
                      lb['total']]
            try:
                cursor.execute(sql_lb, par_lb)
                conn.commit()
            except Exception as e:
                print(e)
        # 职工总数
        for zg in data['sjl_zgzs_list']:
            par_zg = [data['data_list'][0]['cj_id'], gs_id, data['data_list'][0]['gsmc'], zg['year'], zg['ryzs'],
                      zg['gjzcrs'], zg['zjzcrs'], zg['cjzcrs'], zg['bs'], zg['ss'], zg['bk'], zg['zk'], data['data_list'][0]['link']]
            try:
                cursor.execute(sql_zgzs, par_zg)
                conn.commit()
            except Exception as e:
                print(e)
        # 人员信息
        for list in data['data_list']:
            par = [list['cj_id'], gs_id, list['gsmc'], list['xm'], list['sfzh'], list['zw'], list['zgzbh']
                , list['zc'], list['zgzsh'], list['zczsh'], list['yxqz'], list['zczy'], list['zczsbh'], list['dj']
                , list['zylb'], list['zszy'], list['gw'], list['gwzsh'], list['zslb'], list['zsbh'], list['zygz']
                , list['fzjg'], list['zcyzy'], list['start_year'], list['zybh'], list['xl'], list['fzzzlb'], list['ssbm']
                , list['lb'], list['ry_type'], timeArray,timeArray, list['link']]
            try:
                cursor.execute(sql, par)
                conn.commit()
            except Exception as e:
                print(e)

        cursor.close()
        conn.close()

