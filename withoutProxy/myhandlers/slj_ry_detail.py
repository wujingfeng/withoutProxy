# -*- coding: utf-8 -*-

#----------唐 - 水利建设-人员信息
import requests
import pymysql
from lxml import etree
import re
# --------------------------------------全国水利建设_人员信息------------------------
from withoutProxy.config.database import *
def slj_ry_detail(response):
    # 人员信息
    print('-----scjst_info_detail-----')
    html = response.text
    content = etree.HTML(html)
    lsj_data_list=[]
    rtn_data = {}
    data_list = []
    lsj_lb_list=[]
    sjl_zgzs_list=[]

    # 采集表id
    cj_id = re.findall(r'id=(.*?)$', response.url, re.S)[0]
    # 公司链接
    link = "http://rcpu.cwun.org/UInfo.aspx?id="+cj_id+""
    gsmcc = requests.get(url=link)
    gsmcc= gsmcc.text
    gsmcc = etree.HTML(gsmcc)
    # 公司名称
    gsmc = gsmcc.xpath('//*[@id="ContentPlaceHolder1_lbUNCHNM"]/text()')[0].strip()
    # 获取所有人员类别
    for data in content.xpath('//ul[@id="ulinfo"]/li'):
        tmp_data = tmp(cj_id,link,gsmc)
        data_url = data.xpath('a/@data-url')[0].strip('/General')
        data_id = data.xpath('a/@data-tx')[0].strip()
        data_mc = data.xpath('a/text()')[0].strip()
        try:
            data_sl = data.xpath('a/span/text()')[0].strip()[1:-1]
        except:
            data_sl = 0
        url = 'http://rcpu.cwun.org/General/'+data_url+data_id
        response = requests.get(url=url)
        if response.status_code ==200 and response.text != '':
            if data_mc != '行政与技术负责人':
                slj_lb = {
                    's_type': data_mc,
                    'total': data_sl
                }
                lsj_lb_list.append(slj_lb)
            content = etree.HTML(response.text)
            # 其他类别
            qtlb = content.xpath('//*[@id="form1"]/div/text()')[1].strip()
            if qtlb == '水利工程建设监理员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):

                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    tmp_data['ry_type'] = '水利工程建设监理员'
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczy'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zczy'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)



            elif qtlb =='水利工程造价工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '水利工程造价工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zybh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zybh'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='质量检测员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '质量检测员'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zybh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zybh'] = None
                    try:
                        tmp_data['zcyzy'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['zcyzy'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='建造师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '建造师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['zczy'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['zczy'] = None
                    try:
                        tmp_data['dj'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['dj'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[9]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='安全工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '安全工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='监理工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '监理工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zybh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zybh'] = None
                    try:
                        tmp_data['zcyzy'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['zcyzy'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='总监理工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '总监理工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['gwzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['gwzsh'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='建筑师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '建筑师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['dj'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['dj'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='结构工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '结构工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['dj'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['dj'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='投标委托代理人':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '投标委托代理人'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='建设工程造价工程师':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '建设工程造价工程师'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['zylb'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['zylb'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb =='造价员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '造价员'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zszy'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zszy'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb == '全国水利水电工程施工现场管理人员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '全国水利水电工程施工现场管理人员'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['gwzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['gwzsh'] = None
                    try:
                        tmp_data['gw'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['gw'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None


                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb == '施工企业三类人员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '施工企业三类人员'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zslb'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zslb'] = None
                    try:
                        tmp_data['zsbh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zsbh'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None


                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb == '其他执（从）业人员':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '其他执（从）业人员'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['zgzsh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zgzsh'] = None
                    try:
                        tmp_data['zczsh'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zczsh'] = None
                    try:
                        tmp_data['zcyzy'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['zcyzy'] = None
                    try:
                        tmp_data['gw'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['gw'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[9]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb == '中级以上技术工人':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '中级以上技术工人'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['sfzh'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                         tmp_data['sfzh'] = None
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['lb'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['lb'] = None
                    try:
                        tmp_data['zygz'] = slj_jsy.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['zygz'] = None
                    try:
                        tmp_data['fzjg'] = slj_jsy.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['fzjg'] = None
                    try:
                        tmp_data['zsbh'] = slj_jsy.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['zsbh'] = None
                    try:
                        tmp_data['start_year'] = slj_jsy.xpath('td[9]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None


                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

            elif qtlb == '中级以上职称人员（水利水电专业）':
                for slj_jsy in content.xpath('//*[@id="form1"]/table/tbody/tr'):
                    tmp_data['ry_type'] = '中级以上职称人员（水利水电专业）'
                    tmp_data['xm'] = slj_jsy.xpath('td[2]/text()')[0].strip()
                    try:
                        tmp_data['zc'] = slj_jsy.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['zc'] =None
                    try:
                        tmp_data['zylb'] = slj_jsy.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zylb'] =None
                    try:
                        tmp_data['zsbh'] = slj_jsy.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zsbh'] =None


                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)
            else:
                # 获取法定代表人与单位负责人
                for fdry in content.xpath('//*[@id="form1"]/table[1]/tr'):

                    try:
                        ry_type_d = fdry.xpath('th/text()')[0].strip()
                        if ry_type_d == '法定代表人' or ry_type_d == '单位负责人':
                            try:
                                tmp_data['ry_type'] = ry_type_d
                            except:
                                tmp_data['ry_type'] = None
                            try:
                                tmp_data['xm'] = fdry.xpath('td[1]/span/text()')[0].strip()
                            except:
                                tmp_data['xm'] = None
                            try:
                                tmp_data['zw'] = fdry.xpath('td[2]/span/text()')[0].strip()
                            except:
                                tmp_data['zw'] = None
                            try:
                                tmp_data['zc'] = fdry.xpath('td[3]/span/text()')[0].strip()
                            except:
                                tmp_data['zc'] = None
                        if ry_type_d == '身份证号':
                            try:
                                tmp_data['sfzh'] = fdry.xpath('td[1]/span/text()')[0].strip()
                            except:
                                tmp_data['sfzh'] = None
                            try:
                                tmp_data['xl'] = fdry.xpath('td[2]/span/text()')[0].strip()
                            except:
                                tmp_data['xl'] = None
                            try:
                                tmp_data['start_year'] = fdry.xpath('td[3]/span/text()')[0].strip()
                            except:
                                tmp_data['start_year'] = None
                            data_list.append(tmp_data)
                            tmp_data = tmp(cj_id,link,gsmc)

                    except:
                        tmp_data = tmp(cj_id,link,gsmc)
                # 技术负责人
                for jsfzr in content.xpath('//*[@id="form1"]/table[2]/tbody/tr'):

                    tmp_data['ry_type'] = '项目负责人'
                    try:
                        tmp_data['xm'] = jsfzr.xpath('td[2]/text()')[0].strip()
                    except:
                        tmp_data['xm'] = None
                    try:
                        tmp_data['sfzh'] = jsfzr.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['sfzh'] = None
                    try:
                        tmp_data['zw'] = jsfzr.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zw'] = None
                    try:
                        tmp_data['zc'] = jsfzr.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['fzzzlb'] = jsfzr.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['fzzzlb'] = None
                    try:
                        tmp_data['xl'] = jsfzr.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['xl'] = None
                    try:
                        tmp_data['start_year'] = jsfzr.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

                # 管理团队
                for jsfzr in content.xpath('//*[@id="form1"]/table[3]/tbody/tr'):

                    tmp_data['ry_type'] = '管理团队'
                    try:
                        tmp_data['xm'] = jsfzr.xpath('td[2]/text()')[0].strip()
                    except:
                        tmp_data['xm'] = None
                    try:
                        tmp_data['sfzh'] = jsfzr.xpath('td[3]/text()')[0].strip()
                    except:
                        tmp_data['sfzh'] = None
                    try:
                        tmp_data['zw'] = jsfzr.xpath('td[4]/text()')[0].strip()
                    except:
                        tmp_data['zw'] = None
                    try:
                        tmp_data['zc'] = jsfzr.xpath('td[5]/text()')[0].strip()
                    except:
                        tmp_data['zc'] = None
                    try:
                        tmp_data['xl'] = jsfzr.xpath('td[6]/text()')[0].strip()
                    except:
                        tmp_data['xl'] = None
                    try:
                        tmp_data['start_year'] = jsfzr.xpath('td[7]/text()')[0].strip()
                    except:
                        tmp_data['start_year'] = None
                    try:
                        tmp_data['ssbm'] = jsfzr.xpath('td[8]/text()')[0].strip()
                    except:
                        tmp_data['ssbm'] = None

                    data_list.append(tmp_data)
                    tmp_data = tmp(cj_id,link,gsmc)

                # 职工总数
                for zgzs in content.xpath('//*[@id="form1"]/table[4]/tbody/tr'):

                    try:
                        year = zgzs.xpath('td[2]/text()')[0].strip()
                    except:
                        year = None
                    try:
                        ryzs = zgzs.xpath('td[3]/text()')[0].strip()
                    except:
                        ryzs = None
                    try:
                        gjzcrs = zgzs.xpath('td[4]/text()')[0].strip()
                    except:
                        gjzcrs = None
                    try:
                        zjzcrs = zgzs.xpath('td[5]/text()')[0].strip()
                    except:
                        zjzcrs = None
                    try:
                        cjzcrs = zgzs.xpath('td[6]/text()')[0].strip()
                    except:
                        cjzcrs = None
                    try:
                        bs = zgzs.xpath('td[7]/text()')[0].strip()
                    except:
                        bs = None
                    try:
                        ss = zgzs.xpath('td[8]/text()')[0].strip()
                    except:
                        ss = None
                    try:
                        bk = zgzs.xpath('td[9]/text()')[0].strip()
                    except:
                        bk = None
                    try:
                        zk = zgzs.xpath('td[10]/text()')[0].strip()
                    except:
                        zk = None
                    zgzs_list = {
                        'year':year,
                        'ryzs':ryzs,
                        'gjzcrs' : gjzcrs,
                        'zjzcrs' :zjzcrs,
                        'cjzcrs' :cjzcrs,
                        'bs' :bs,
                        'ss' :ss,
                        'bk':bk,
                        'zk':zk,
                    }
                    sjl_zgzs_list.append(zgzs_list)


    lb_list={
        'data_list':data_list,
        'lsj_lb_list':lsj_lb_list,
        'sjl_zgzs_list':sjl_zgzs_list
    }
    lsj_data_list.append(lb_list)
    if ('items' not in rtn_data):
        rtn_data['items'] = []
    rtn_data['items'].append({'data': lsj_data_list})
    return rtn_data

def tmp(cj_id,link,gsmc):
    tmp_data = {
        'cj_id': cj_id,
        'xm': '',
        'zw': '',
        'sfzh': '',
        'zybh': '',
        'zgzbh': '',
        'zc': '',
        'zgzsh': '',
        'zczsh': '',
        'yxqz': '',
        'zczy': '',
        'zczsbh': '',
        'dj': '',
        'zylb': '',
        'zszy': '',
        'gw': '',
        'gwzsh': '',
        'zslb': '',
        'zsbh': '',
        'zygz': '',
        'fzjg': '',
        'zcyzy': '',
        'start_year': '',
        'xl': '',
        'fzzzlb': '',
        'ssbm': '',
        'lb': '',
        'ry_type': '',
        'created': '',
        'link': link,
        'gsmc': gsmc

    }
    return tmp_data



