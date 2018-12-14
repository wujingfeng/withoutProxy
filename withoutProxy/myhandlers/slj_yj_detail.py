import datetime
import json
import re

import requests
from bs4 import BeautifulSoup
from withoutProxy.config.database import *

def slj_yj_detail(response):
    # 解析数据
    print('-----水利局业绩-----')
    try:
        return_data = {}
        data_list = []
        jbxx_list = []  # 基本信息集合
        ry_list = []  # 人员集合
        hj_list = []  # 获奖集合
        tjxx_list = []  # 统计集合
        r = requests.get(response.url).content
        soup = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')
        list = response.xpath('//*[@id="ulinfo"]/li')
        id = response.xpath('//*[@id="form1"]/@action').extract_first().split('=')[1]
        for li in list:
            sgyj = li.xpath('./a/@data-url').extract_first().strip()
            if sgyj == '/General/NPROJ_DEL.aspx?id=':
                pass
            else:
                s_type = li.xpath('./a/text()').extract_first().strip()
                url = 'http://rcpu.cwun.org/UInfo.aspx?id='+ id
                r = requests.get(url).content
                su = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')
                gsmc = su.find('span',id='ContentPlaceHolder1_lbUNCHNM').text
                p_type = su.find('a', id='tab-proj').text
                total = li.xpath('./a/span/text()').extract_first().strip().split('(')[1].split(')')[0]
                lj = 'http://rcpu.cwun.org'+sgyj+id
                r = requests.get(lj).content
                soup = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')
                tbody = soup.find('tbody')
                list = tbody.find_all('tr')
                xglsjl = ''
                for lis in list:
                    url = 'http://rcpu.cwun.org'+ sgyj.replace('.','_1.') + lis.find('span').attrs['data-rid']
                    r = requests.get(url).content
                    soup = BeautifulSoup(r, 'html.parser', from_encoding='utf-8')
                    table = soup.find_all('table', class_='layui-table')
                    xmmc = soup.find('span', id='TextBoxEngName').text
                    #  人员信息
                    ry_table = table[1]
                    ry_table = ry_table.find('tbody')
                    ry_lists = ry_table.find_all('tr')
                    if ry_lists:
                        for ry in ry_lists:
                            li = ry.find_all('td')
                            name = li[0].text.strip()
                            if name:
                                if name == '没有记录':
                                    pass
                                else:
                                    zw_msg = {
                                        'gsmc': gsmc,
                                        'link': url,
                                        'xmmc': xmmc,
                                        'name': name,
                                        'zw': li[2].text,
                                        'zc': li[3].text,
                                        'zsmc': li[4].text,
                                        'zsbh': li[5].text,
                                        'zszy': li[6].text,
                                        'dj': li[7].text,
                                    }
                                    ry_list.append(zw_msg)

                    #  获奖信息
                    hj_table = table[2]
                    hj_table = hj_table.find('tbody')
                    hj_lists = hj_table.find_all('tr')
                    if hj_lists:
                        for hj in hj_lists:
                            li = hj.find_all('td')
                            jxmc = li[0].text.strip()
                            if jxmc:
                                if jxmc == '没有记录':
                                    pass
                                else:
                                    hj_msg = {
                                        'gsmc': gsmc,
                                        'xmmc': xmmc,
                                        'jxmc': jxmc,
                                        'link': url,
                                        'jxlb': li[1].text,
                                        'jxjb': li[2].text,
                                        'jxdb': li[3].text,
                                        'bjdw': li[4].text,
                                        'bjwh': li[5].text,
                                        'bjsj': li[6].text,
                                    }
                                    hj_list.append(hj_msg)

                    #  修改历史记录
                    lsjl = soup.find('div', id=re.compile('DIVHIS'))
                    if lsjl:
                        lsjl_msg = lsjl.find('tbody')
                        lsjl_msg_lists = lsjl_msg.find_all('tr')
                        for hj in lsjl_msg_lists:
                            li = hj.find_all('td')
                            xglsjl = li[1].text.strip() + ',' + li[2].text.strip() + ';'
                    else:
                        xglsjl = ''
                    #  基本信息

                    try:
                        xmbh = soup.find('span', id='TextBoxEngCode').text,# 项目编号
                    except:
                        xmbh = ''
                    try:
                        htmc = soup.find('span', id='TextBoxProjectName').text,  # 合同名称
                    except:
                        htmc = ''
                    try:
                        gczt = soup.find('span', id='lbSTATUS').text,  # 工程状态
                    except:
                        gczt = ''
                    try:
                        szd = soup.find('span', id='lbADDRESS').text,  # 所在地
                    except:
                        szd = ''
                    try:
                        xmfzr = soup.find('span', id='TextBoxProjectManager').text,  # 项目负责人
                    except:
                        xmfzr = ''
                    try:
                        jsfzr = soup.find('span', id='TextBoxTechManager').text,  # 技术负责人
                    except:
                        jsfzr = ''
                    try:
                        jsdw = soup.find('span', id='TextBoxBuildUnit').text,  # 建设单位
                    except:
                        jsdw = ''
                    try:
                        gcdj_db = soup.find('span', id='lbLEVEL').text,  # 工程等级-等别
                    except:
                        gcdj_db = ''
                    try:
                        gcdj_jb = soup.find('span', id='lbGRADE').text,  # 工程等级-级别
                    except:
                        gcdj_jb = ''
                    try:
                        kgrq = soup.find('span', id='TextBoxStartTime').text,  # 开工日期
                    except:
                        kgrq = ''
                    try:
                        wgrq = soup.find('span', id='TextBoxEndTime').text,  # 完工日期
                    except:
                        wgrq = ''
                    try:
                        htgq = soup.find('span', id='TextBoxContractTime').text,  # 合同工期
                    except:
                        htgq = ''
                    try:
                        gjzb = soup.find('span', id='TextBoxKPI').text,  # 工程关键指标
                    except:
                        gjzb = ''
                    try:
                        htje = soup.find('span', id='TextBoxContrctMoney').text,  # 合同金额(万元)
                    except:
                        htje = ''
                    try:
                        jsje = soup.find('span', id='TextBoxPayment').text,  # 结算金额(万元)
                    except:
                        jsje = ''
                    try:
                        zynr = soup.find('span', id='TextBoxMainContent').text,  # 合同主要内容
                    except:
                        zynr = ''

                    list = {
                        'gsmc': gsmc,  # 公司名称
                        'xmmc':  xmmc,  # 项目名称
                        'xmbh': xmbh,# 项目编号
                        'htmc': htmc,# 合同名称
                        'gczt': gczt,# 工程状态
                        'szd': szd,# 所在地
                        'xmfzr': xmfzr,# 项目负责人
                        'jsfzr': jsfzr,# 技术负责人
                        'jsdw': jsdw,# 建设单位
                        'gcdj_db': gcdj_db,# 工程等级-等别
                        'gcdj_jb': gcdj_jb,# 工程等级-级别
                        'kgrq': kgrq,# 开工日期
                        'wgrq': wgrq,# 完工日期
                        'htgq': htgq,# 合同工期
                        'gjzb': gjzb,# 工程关键指标
                        'htje': htje,# 合同金额(万元)
                        'jsje': jsje,# 结算金额(万元)
                        'zynr': zynr,# 合同主要内容
                        'type': s_type,# 业绩类型
                        'xglsjl': xglsjl, # 修改历史记录
                        'link': url,# 网站链接
                    }
                    jbxx_list.append(list)
                tj_list = {
                    'gsmc': gsmc,
                    'cj_id': id,
                    's_type': s_type,
                    'p_type': p_type,
                    'total': total,
                }
                tjxx_list.append(tj_list)
                tmp_data = {
                    'jbxx_list': jbxx_list,
                    'hjxx_list': hj_list,
                    'ryxx_list': ry_list,
                    'tjxx_list': tjxx_list,
                }

                data_list.append(tmp_data)


        if ('items' not in return_data):
            return_data['items'] = []
        return_data['items'].append({'data': data_list})
        return return_data

    except Exception as e:
        print(e)
