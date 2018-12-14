#张峻珲
#全国水利建设(业绩信息+信用评价)

import pymysql
import time

from withoutProxy.config.database import *

def sljs_jbxx_detail_pipline(data):
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
    ts = int(time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S")))
    sql = 'INSERT INTO slj_baseinfo (cj_id,gs_id,gsmc,ssss,dwxz,jycd,mj,yyzz_jyfw,yyzz_clrq,yyzz_zczbj,yyzz_fzjg,yyzz_djzclx,`yyzz_zch,yyzz_fddbr,zfgs,zzjgdmz_zzjgdmzh,zzjgdmz_fzjg,zzjgdmz_yxqz,swdjz_fzrq,swdjz_swdjzh,swdjz_fzjg,aqscxkz_fzjg,aqscxkz_aqscxk,sbdjh_fzjg,sbdjh_sbdjz,wzlink,glrztx,glzd,xyjs_is_glry,xyjs_is_jlglbm,xyjs_is_mqglbm,zcdz_zcdz,zcdz_yzbm,jydz_zcdz,jydz_yzbm,wz_dwwz,wz_plwz,wz_plsj,zyyw,dwlsyg,created,modified,xxly,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        # data['gs_id'] = 1
        par = [data['cj_id'],data['gs_id'],data['gsmc'],data['ssss'],data['dwxz'],data['jycd'],data['mj'],data['yyzz_jyfw'],data['yyzz_clrq'],data['yyzz_zczbj'],data['yyzz_fzjg'],data['yyzz_djzclx'],data['yyzz_zch'],data['yyzz_fddbr'],data['zfgs'],data['zzjgdmz_zzjgdmzh'],data['zzjgdmz_fzjg'],data['zzjgdmz_yxqz'],data['swdjz_fzrq'],data['swdjz_swdjzh'],data['swdjz_fzjg'],data['aqscxkz_fzjg'],data['aqscxkz_aqscxk'],data['sbdjh_fzjg'],data['sbdjh_sbdjz'],data['wzlink'],data['glrztx'],data['glzd'],data['xyjs_is_glry'],data['xyjs_is_jlglbm'],data['xyjs_is_mqglbm'],data['zcdz_zcdz'],data['zcdz_yzbm'],data['jydz_zcdz'],data['jydz_yzbm'],data['wz_dwwz'],data['wz_plwz'],data['wz_plsj'],data['zyyw'],data['dwlsyg'],ts,ts,data['xxly'],data['link']]
        cursor.execute(sql,par)
        for i in data['list']:
            # i['gs_id'] = 1
            time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            ts = int(time.mktime(time.strptime(time1, "%Y-%m-%d %H:%M:%S")))
            sql = 'INSERT INTO slj_xypj (gs_id,gsmc,lb,pjjg,pjrq,pjjgg,yxq,link,created,modified) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            par = [i['gs_id'],i['gsmc'],i['lb'],i['pjjg'],i['pjrq'],i['pjjgg'],i['yxq'],i['link'],ts,ts]
            cursor.execute(sql,par)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()