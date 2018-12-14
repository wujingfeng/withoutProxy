#张峻珲
#全国公路建设市场(业绩信息)

import re
import time
import requests
import json
import pymysql
from withoutProxy.config.database import *


#访问get
def get(url):
    i = 0
    while True:
        try:
            requests1 = requests.get(url,timeout=60)
            return requests1
        except:
            print("访问链接失败重试..."+url+"")
            i = i+1
            if i == 5:
                break
            pass
#访问psot
def post(url,data):
    i = 0
    while True:
        try:
            requests1 = requests.post(url,data=data,timeout=10)
            return requests1
        except:
            i = i + 1
            if i == 5:
                break
            pass


from withoutProxy.config.database import *

def yjxx_jssc_detail(response):
    # 数据库配置
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT
    )
    cursor = conn.cursor()

    rtn_data = {}
    data_list = []
    print('-----yjxx_jssc_detail-----')
    zid = re.findall(r'companyId=(.*?)&',response.url,re.S)[0]
    #(总包/分包)-(已建/在建)-省厅审核
    list = [11,12,21,22]
    for li in list:
        url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveList.do?companyId=%s&type=%s&page=1&rows=15&sourceInfo=1'%(zid,li)
        requests1 = get(url)
        html = requests1.text
        html = json.loads(html)
        max_page = html['pageObj']['maxPage']
        for pag in range(1 , int(max_page) + 1):
            url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveList.do?companyId=%s&type=%s&page=%s&rows=15&sourceInfo=1' % (zid,li,pag)
            requests1 = get(url)
            html = requests1.text
            html = json.loads(html)
            for i in html['rows']:
                id = i['id']
                url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveInfo.do?id=%s'%(id)
                requests1 = get(url)
                html = requests1.text
                html = json.loads(html)

                gsmc = html['data']['corpName']
                xmmc = html['data']['projectName']
                link = 'http://glxy.mot.gov.cn/company/companyAchieveInfo.do?id=%s&companyId=%s&type=%s&companyType=0'%(id,zid,li)
                htj = html['data']['contractPrice']
                jsj = html['data']['settlementPrice']
                kgsj = html['data']['beginDate']
                zygcl = html['data']['remark']
                if li == 11 or li == 21:
                    yz = 1
                else:
                    yz = 2
                if li == 11 or li == 12:
                    zf = 1
                else:
                    zf = 2
                szsf = html['data']['province']
                yj_type = 2
                xmlx = html['data']['projectType']
                jsdj = html['data']['technologyGrade']
                htdmc = html['data']['segmentName']
                jgrq = html['data']['endDate']
                jgsj = html['data']['handDate']
                kszh = html['data']['stakeStart']
                jszh = html['data']['stakeEnd']
                zlpdqk = html['data']['quality']
                xmdm = html['data']['projectCode']
                proj_id = id
                valid = 1

                #人员履约信息
                url = 'http://glxy.mot.gov.cn/person/getPersonAchieveListByCompanyAchieveId.do'
                data = {
                    'page':'1',
                    'rows':'10',
                    'companyAchieveId':id,
                    'Referer':link
                }
                requests1 = post(url,data)
                html = requests1.text
                html = json.loads(html)
                r_data = {}
                rylexx_data = []
                for x in html['rows']:
                    name = x['personName']
                    gw = x['achievementPosition']
                    rzsj = x['achievementStartDate'] + '~' + x['achievementEndDate']

                    r_data = {
                        'gsmc' : gsmc,
                        'xmmc' : xmmc,
                        'name' : name,
                        'gw' : gw,
                        'rzsj' : rzsj,
                        'type' : yj_type,
                        'validx' : valid
                    }
                    rylexx_data.append(r_data)

                sql = 'SELECT id FROM sc_gss_his where gsmc = %s'
                cursor.execute(sql, gsmc)
                rows = cursor.fetchall()

                rtn_data = {
                    'gs_id':rows,
                    'gsmc':gsmc,
                    'xmmc':xmmc,
                    'link':link,
                    'htj':htj,
                    'jsj':jsj,
                    'kgsj':kgsj,
                    'zygcl':zygcl,
                    'yz':yz,
                    'zf':zf,
                    'szsf':szsf,
                    'yj_type':yj_type,
                    'xmlx':xmlx,
                    'jsdj':jsdj,
                    'htdmc':htdmc,
                    'jgrq':jgrq,
                    'jgsj':jgsj,
                    'kszh':kszh,
                    'jszh':jszh,
                    'zlpdqk':zlpdqk,
                    'xmdm':xmdm,
                    'valid':valid,
                    'ry_list':rylexx_data,
                    'bdlx': '',
                    'bdmc': '',
                    'zbqy': '',
                    'sfwg': '',
                    'jgysdf': '',
                    'jsgm': '',
                    'other': '',
                    'proj_id':id
                }
                data_list.append(rtn_data)

    # (总包/分包)-(已建/在建)-省厅录入
    list = [11, 12, 21, 22]
    for li in list:
        url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveList.do?companyId=%s&type=%s&page=1&rows=15&sourceInfo=2' % (
        zid, li)
        requests1 = get(url)
        html = requests1.text
        html = json.loads(html)
        max_page = html['pageObj']['maxPage']
        for pag in range(1, int(max_page) + 1):
            url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveList.do?companyId=%s&type=%s&page=%s&rows=15&sourceInfo=2' % (
            zid, li, pag)
            requests1 = get(url)
            html = requests1.text
            html = json.loads(html)
            for i in html['rows']:
                id = i['id']
                url = 'http://glxy.mot.gov.cn/company/getCompanyAchieveInfo.do?id=%s' % (id)
                requests1 = get(url)
                html = requests1.text
                html = json.loads(html)

                gsmc = html['data']['corpName']
                xmmc = html['data']['projectName']
                link = 'http://glxy.mot.gov.cn/company/companyAchieveInfo.do?id=%s&companyId=%s&type=%s&companyType`=0' % (
                id, zid, li)
                htj = html['data']['contractPrice']
                jsj = html['data']['settlementPrice']
                kgsj = html['data']['beginDate']
                zygcl = html['data']['mainProject']
                if li == 11 or li == 21:
                    yz = 1
                else:
                    yz = 2
                if li == 11 or li == 12:
                    zf = 1
                else:
                    zf = 2
                szsf = html['data']['province']
                yj_type = 1
                bdlx = html['data']['segmentType']
                bdmc = html['data']['segmentName']
                zbqy = html['data']['corpName']
                sfwg = html['data']['isFinished']
                jgysdf = html['data']['workScore']
                jsgm = html['data']['segmentSize']
                other = html['data']['remark']
                proj_id = id

                valid = 1

                # 人员履约信息
                url = 'http://glxy.mot.gov.cn/person/getPersonAchieveListByCompanyAchieveId.do'
                data = {
                    'page': '1',
                    'rows': '10',
                    'companyAchieveId': id,
                    'Referer': link
                }
                requests1 = post(url, data)
                html = requests1.text
                html = json.loads(html)
                r_data = {}
                rylexx_data = []
                for x in html['rows']:
                    name = x['personName']
                    gw = x['achievementPosition']
                    rzsj = x['achievementStartDate'] + '~' + x['achievementEndDate']

                    r_data = {
                        'gsmc': gsmc,
                        'xmmc': xmmc,
                        'name': name,
                        'gw': gw,
                        'rzsj': rzsj,
                        'type': yj_type,
                        'validx': valid
                    }
                    rylexx_data.append(r_data)

                sql = 'SELECT id FROM sc_gss_his where gsmc = %s'
                cursor.execute(sql, gsmc)
                results = cursor.fetchone()

                rtn_data = {
                    'gs_id': results,
                    'gsmc': gsmc,
                    'xmmc': xmmc,
                    'link': link,
                    'htj': htj,
                    'jsj': jsj,
                    'kgsj': kgsj,
                    'zygcl': zygcl,
                    'yz': yz,
                    'zf': zf,
                    'szsf': szsf,
                    'yj_type': yj_type,
                    'bdlx':bdlx,
                    'bdmc':bdmc,
                    'zbqy':zbqy,
                    'sfwg':sfwg,
                    'jgysdf':jgysdf,
                    'jsgm':jsgm,
                    'other':other,
                    'valid': valid,
                    'ry_list': rylexx_data,
                    'xmlx': '',
                    'jsdj': '',
                    'htdmc': '',
                    'jgrq': '',
                    'jgsj': '',
                    'kszh': '',
                    'jszh': '',
                    'zlpdqk': '',
                    'xmdm': '',
                    'proj_id':id
                }
                data_list.append(rtn_data)

    if rtn_data == {}:
        rtn_data = {
            'msg': 'find empty comp: ' + response.url
        }
        return rtn_data

    if ('items' not in rtn_data):
        rtn_data['items'] = []
    rtn_data['items'].append({'data': data_list})
    return rtn_data