import re
import json
import datetime
import requests
from withoutProxy.config.database import *
from bs4 import BeautifulSoup

def gljs_jbxx_detail(response):
    # 全国公路基本信息
    # 孙国强
    print('-----gljs_jbxx_detail-----')
    return_data = {}
    if response.url.find('company') != -1:
        html = json.loads(response.text)
        html = html.get('data')

        zzjgdm = html['corpCode']  # 组织机构代码
        qymc = html['corpName']  # 企业名称
        zcsf = html['regProvinceCode']  # 注册省份
        zccs = html['regCityCode']  # 注册城市
        cymc = html['corpUseName']  # 曾用名称
        xzzgbm = html['chargeDepartment']  # 行政主管部门名称
        yyzzzch = html['businessLicence']  # 营业执照注册号
        zczj = html['regFund']  # 注册资金
        qylx = html['corpType']  # 企业类型
        qyxz = html['natureType']  # 企业性质
        yyzzzcrq = html['regDate']  # 营业执照注册日期
        clrq = html['certificationdate']  # 成立日期
        fddbr = html['legalRepresentative']  # 法定代表人
        fddbrzc = html['artificialpersonTitle']  # 法定代表人职称
        qyfzr = html['enterpriseLeader']  # 企业负责人
        qyfzrzc = html['leaderTitle']  # 企业负责人职称
        jsfzr = html['technicalLeader']  # 技术负责人
        jsfzrzc = html['technicalLeaderDuty']  # 技术负责人职称
        qyqk = html['assetsInvestment']  # 资产构成情况及投资关联企业情况
        shxydm = html['businessLicence']  # 统一社会信用代码
        yyfw = html['businessScope']  # 营业范围
        link = response.url  # 基本信息链接
        corpCode = html['id']  # 公司标识
        created = datetime.datetime.now()  # 写入时间
        modified = datetime.datetime.now()  # 写入时间
        return_data = {
            'items': [
                {
                    'data': [
                        {
                            # 基本信息表
                            'zzjgdm': zzjgdm,
                            'qymc': qymc,
                            'zcsf': zcsf,
                            'zccs': zccs,
                            'cymc': cymc,
                            'xzzgbm': xzzgbm,
                            'yyzzzch': yyzzzch,
                            'zczj': zczj,
                            'qylx': qylx,
                            'qyxz': qyxz,
                            'yyzzzcrq': yyzzzcrq,
                            'clrq': clrq,
                            'yyfw': yyfw,
                            'link': link,
                            'corpCode': corpCode,
                            'created': created,
                            'modified': modified,
                            'fddbr': fddbr,
                            'fddbrzc': fddbrzc,
                            'qyfzr': qyfzr,
                            'qyfzrzc': qyfzrzc,
                            'jsfzr': jsfzr,
                            'jsfzrzc': jsfzrzc,
                            'qyqk': qyqk,
                            'shxydm': shxydm,
                        }
                    ]
                }
            ]
        }
        if ('requests' not in return_data):
            return_data['requests'] = []
        return_data['requests'].append('http://glxy.mot.gov.cn/evaluate/getEvaluateList.do?comId=' + html['id'] + '&rows=15&page=' + str(1))
        return return_data

    # 信用等级信息
    elif response.url.find('evaluate') != -1:
        data_list = []
        r = requests.get(response.url).content
        soup = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')
        dj = json.loads(soup.text)
        xydj = 'http://glxy.mot.gov.cn/evaluate/getEvaluateList.do?comId=' + dj['rows'][0]['companyId'] + '&rows=15'
        max_page = dj['pageObj']['maxPage']
        currentPage = dj['pageObj']['curpage']

        list = dj['rows']
        for li in list:
            data={
                'pjsf': li['evaluateprovince'],
                'gsmc': li['corpName'],
                'pjnf': li['oeriodCode'],
                'dj': li['evaGrade'],
                'gszt': li['companyType'],
                'url': response.url,
                'created': datetime.datetime.now(),
                'modified': datetime.datetime.now(),
                'companyId': li['companyId'],
            }
            data_list.append(data)
        if ('items' not in return_data):
            return_data['items'] = []
        return_data['items'].append({'data': data_list})
        if ('requests' not in return_data):
            return_data['requests'] = []
        if currentPage < max_page:
            currentPage = currentPage + 1
            return_data['requests'].append(xydj+'&page='+str(currentPage))
        return return_data
