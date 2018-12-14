import re
import requests
import json
from withoutProxy.config.database import *

# # 公路建设 人员
def gljs_ry_detail(response):
    print('-----gljs_ry_detail-----')
    html = response.text
    text = json.loads(html)
    zid = text['rows'][0]['companyId']

    data={
        'page':'1',
        'rows':'15',
        'comId':zid,
        'type':'0'
    }
    rtn_data = {}
    data_list = []
    tmp_data = []
    ye = text['pageObj']['maxPage']
    for page in range(1,int(ye) + 1) :
        print('page',page)
        data['page'] = page
        response = requests.post(url='http://glxy.mot.gov.cn/person/getPersonList.do', data=data)
        html = response.text
        text = json.loads(html)
        for text in text['rows']:
            staff_id = text['id']

            url = "http://glxy.mot.gov.cn/person/personInfo.do?perId="+text['id']+"&type=0"
            gsmc = text['company']
            response = requests.get(url=url)
            html = response.text
            conend = json.loads(html)
        # 基本信息
            gljs_xm = conend['data']['name'] # 姓名
            gljs_byyx = conend['data']['topCollege'] # 毕业院校
            idcard = conend['data']['idCard']
            gljs_xl = conend['data']['topEducation'] # 学历
            gljs_xb = conend['data']['sex'] #性别
            gljs_sxzy = conend['data']['topMajor'] # 所学专业
            gljs_zw = conend['data']['position'] # 职务
            gljs_birth = conend['data']['birthDate'] # 出生日期
            gljs_ksgznf = conend['data']['majorStartDate'][0:4] # 开始工作年份

            person_link = "http://glxy.mot.gov.cn/person/base.do?id="+text['id']+"&type=0&companyid="+zid+""
            gljs_type = '基本信息'
            xxly = '公路建设市场'
            jbxx_list = {
                'idcard':idcard,
                'gljs_xm': gljs_xm,
                'gljs_byyx': gljs_byyx,
                'gljs_xl': gljs_xl,
                'gljs_xb': gljs_xb,
                'gljs_sxzy': gljs_sxzy,
                'gljs_zw': gljs_zw,
                'gljs_birth': gljs_birth,
                'gljs_ksgznf': gljs_ksgznf,
                'person_link': person_link,
                'gljs_type': gljs_type,
                'xxly': xxly,
                'gsmc':gsmc,
                'staff_id':staff_id
            }
            zcxx_list = []
        #  职称信息
            zcxx = []
            url = "http://glxy.mot.gov.cn/person/getPersonAcademicList.do?perId="+text['id']+""
            response = requests.get(url=url)
            html = response.text
            conend = json.loads(html)
            for zc in conend['rows']:
                zcc = zc['academicName'] # 职称
                zsbh = zc['academicID'] # 证书标号
                zczy = zc['academicMajor'] # 职称专业
                hfjg = zc['acaIssueAuthority'] # 核发机关
                hfrq = zc['acaIssueDate'] # 核发日期
                zcxx = {
                    'zcc': zcc,
                    'zsbh': zsbh,
                    'zczy': zczy,
                    'hfjg': hfjg,
                    'hfrq': hfrq,
                }
                zcxx_list.append(zcxx)
            zyzgxx_list = []
        # 执业资格信息
            zyzgxx = []
            url = "http://glxy.mot.gov.cn/person/getPersonPracticeCertList.do?perId=" + text['id'] + ""
            response = requests.get(url=url)
            html = response.text
            conend = json.loads(html)
            for zg in conend['rows']:
                zclb = zg['regTypeName']
                zcdj = zg['regLevel']
                fzjg = zg['issueAuthority']
                zsbh = zg['regCANumber']
                fzrq = zg['regAnnounceDate']
                zcyxqz = zg['regValidityTerm']
                zyzgxx = {
                    'zclb': zclb,
                    'zcdj': zcdj,
                    'fzjg': fzjg,
                    'zsbh': zsbh,
                    'fzrq': fzrq,
                    'zcyxqz': zcyxqz,
                }
                zyzgxx_list.append(zyzgxx)
        # 履历信息
            flxx_list = []
            flxx = []
            url = "http://glxy.mot.gov.cn/person/getPersonRecordList.do?perId=" + text['id'] + ""
            response = requests.get(url=url)
            html = response.text
            conend = json.loads(html)
            for fl in conend['rows']:
                zw = fl['position']
                rzsj = fl['workStartDate']
                lzsj = fl['workEndDate']
                gsmc = fl['corpName']
                zwlx = fl['ddldutytype']
                rzzt = fl['workStatus']
                flxx = {
                    'gsmc': gsmc,
                    'zwlx': zwlx,
                    'rzzt': rzzt,
                    'zw': zw,
                    'rzsj': rzsj,
                    'lzsj': lzsj,
                }
                flxx_list.append(flxx)
        # 个人业绩 gljs_gryj
            gryj_list = []
            gryj_list_list = []
            url = "http://glxy.mot.gov.cn/person/getPersonAchieveList.do?perId=" + text['id'] + ""
            response = requests.get(url=url)
            html = response.text
            conend = json.loads(html)
            for yj in conend['rows']:
                proj_id= yj['project_id']
                gljs_xmname = yj['projectName']
                gljs_bdname = yj['segmentName']
                gsmc = yj['achievementCompany']
                gljs_drzw = yj['achievementPosition']
                gljs_start_time = yj['achievementStartDate']
                gljs_end_time = yj['achievementEndDate']
                gryj_list = {
                    'gljs_xmname': gljs_xmname,
                    'gljs_bdname': gljs_bdname,
                    'gsmc': gsmc,
                    'gljs_drzw': gljs_drzw,
                    'gljs_start_time': gljs_start_time,
                    'gljs_end_time': gljs_end_time,
                    'proj_id':proj_id
                }
                gryj_list_list.append(gryj_list)
            tmp_data ={
                'gryj_list_list':gryj_list_list,
                'flxx_list':flxx_list,
                'zyzgxx_list':zyzgxx_list,
                'zcxx_list':zcxx_list,
                'jbxx_list':jbxx_list
            }
            data_list.append(tmp_data)

    if ('items' not in rtn_data):
        rtn_data['items'] = []
    rtn_data['items'].append({'data': data_list})
    return rtn_data