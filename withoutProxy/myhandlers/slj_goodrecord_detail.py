#彭青山
#全国水利良好
import re
import requests
from bs4 import BeautifulSoup
import pymysql
import time
from withoutProxy.config.database import *

def slj_goodrecord_detail(response):
    print('-----slj_goodrecord_detail-----')
    conn = pymysql.connect(host=MYSQL_HOST,  user=MYSQL_USER,   password=MYSQL_PASSWORD,  db=MYSQL_DB,  charset=MYSQL_CHATSET, port=MYSQL_PORT, cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    tabs = response.xpath('//ul[@class="datas_tabs"]/li')
    id = re.search('\d+',response.url).group()
    u = 'http://rcpu.cwun.org/UInfo.aspx?id=' + id
    html = requests.get(u).text
    gsmc = re.search('<span id="ContentPlaceHolder1_lbUNCHNM">(.*?)</span>', html).group(1)
    try:
        cursor.execute("select id from sc_gss_his where gsmc = %s", gsmc)
        gs_id = cursor.fetchone()
        gs_id = int(gs_id['id'])
    except Exception as e:
        print(e,'无此公司gs_id')
        gs_id = 0
    xxly = '全国水利建设市场信用信息平台'
    rtn_data = {}
    list = []
    data_list = []
    for li in tabs:
        url = 'http://rcpu.cwun.org' + li.xpath('.//a/@data-url').extract_first() + id
        # url = 'http://rcpu.cwun.org/General/NCRED4.aspx?id=186'
        jl_type = li.xpath('.//a/text()').extract_first()
        p_type = '良好行为'
        if jl_type != '删除的项':
            total = li.xpath('.//span/text()').extract_first().replace('(','').replace(')','')
            tmp_data = {
                'cj_id': id,
                'gs_id': gs_id,
                'gsmc': gsmc,
                'p_type': p_type,
                's_type': jl_type,
                'total': total,
            }
            data_list.append(tmp_data)

        link = u
        t = requests.get(url).content
        soup = BeautifulSoup(t, 'lxml')
        trs = soup.find_all('tr')
        if jl_type.find('单位获奖') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                dwhj_jxmc = td[1].get_text()
                dwhj_jxjb = td[2].get_text()
                dwhj_bjdw = td[3].get_text()
                dwhj_bjwh = td[4].get_text()
                dwhj_bjsj = td[5].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`dwhj_jxmc`,`dwhj_jxjb`,`dwhj_bjdw`,`dwhj_bjwh`,`dwhj_bjsj`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, dwhj_jxmc, dwhj_jxjb,dwhj_bjdw, dwhj_bjwh,dwhj_bjsj, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('工程获奖') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                gchj_xmmc = td[1].get_text()
                gchj_jxmc = td[2].get_text()
                gchj_jxlb = td[3].get_text()
                gchj_jxjb = td[4].get_text()
                gchj_bjdw = td[5].get_text()
                gchj_bjwh = td[6].get_text()
                gchj_bjsj = td[7].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`gchj_xmmc`,`gchj_jxmc`,`gchj_jxlb`,`gchj_jxjb`,`gchj_bjdw`,`gchj_bjwh`,`gchj_bjsj`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, gchj_xmmc, gchj_jxmc, gchj_jxlb, gchj_jxjb,gchj_bjdw, gchj_bjwh, gchj_bjsj, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('企业参与抢险救灾、慈善公益活动情况') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                gyhd_sj = td[1].get_text()
                gyhd_cy_or_zc = td[2].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`gyhd_sj`,`gyhd_cy_or_zc`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, gyhd_sj, gyhd_cy_or_zc, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('专利') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                patents_name = td[1].get_text()
                patents_num = td[2].get_text()
                patents_sq_time = td[3].get_text()
                patents_valid = td[4].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`patents_name`,`patents_num`,`patents_sq_time`,`patents_valid`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, patents_name, patents_num,patents_sq_time,patents_valid, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('工法') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                gf_name = td[1].get_text()
                gf_num = td[2].get_text()
                gf_pz_time = td[3].get_text()
                gf_valid = td[4].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`gf_name`,`gf_num`,`gf_pz_time`,`gf_valid`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, gf_name, gf_num, gf_pz_time, gf_valid, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('编著专著培训教材情况') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                jcqk_name = td[1].get_text()
                jcqk_num = td[2].get_text()
                jcqk_time = td[3].get_text()
                jcqk_bz = td[4].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`jcqk_name`,`jcqk_num`,`jcqk_time`,`jcqk_bz`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, jcqk_name, jcqk_num, jcqk_time, jcqk_bz, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('正式期刊发表论文情况') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                zsqkfb_tm = td[1].get_text()
                zsqkfb_zz = td[2].get_text()
                zsqkfb_name = td[3].get_text()
                zsqkfb_num = td[4].get_text()
                zsqkfb_time = td[5].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`zsqkfb_tm`,`zsqkfb_zz`,`zsqkfb_name`,`zsqkfb_num`,`zsqkfb_time`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, zsqkfb_tm, zsqkfb_zz, zsqkfb_name, zsqkfb_num,zsqkfb_time, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('新工艺新方法') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                xgyff_name = td[1].get_text()
                xgyff_lb = td[2].get_text()
                xgyff_jdjg = td[3].get_text()
                xgyff_time = td[4].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`xgyff_name`,`xgyff_lb`,`xgyff_jdjg`,`xgyff_time`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, xgyff_name, xgyff_lb, xgyff_jdjg, xgyff_time, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('软件著作权') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                rjzzq_name = td[1].get_text()
                rjzzq_num = td[2].get_text()
                rjzzq_zsh = td[3].get_text()
                rjzzq_djrq = td[4].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`rjzzq_name`,`rjzzq_num`,`rjzzq_zsh`,`rjzzq_djrq`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, rjzzq_name, rjzzq_num, rjzzq_zsh, rjzzq_djrq, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
        elif jl_type.find('主编技术标准') != -1:
            for i in range(1,len(trs)):
                td = trs[i].find_all('td')
                zbjsbz_name = td[1].get_text()
                zbjsbz_num = td[2].get_text()
                zbjsbz_fb_time = td[3].get_text()
                zbjsbz_ss_time = td[4].get_text()
                zbjsbz_bz = td[5].get_text()

                sql = "insert into slj_goodrecord(`gs_id`,`gsmc`,`zbjsbz_name`,`zbjsbz_num`,`zbjsbz_fb_time`,`zbjsbz_ss_time`,`zbjsbz_bz`,`xxly`,`jl_type`,`link`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                try:
                    par = [gs_id, gsmc, zbjsbz_name, zbjsbz_num, zbjsbz_fb_time, zbjsbz_ss_time,zbjsbz_bz, xxly, jl_type, link]
                    cursor.execute(sql, par)
                except Exception as e:
                    print(e)
    tmp_datas = {
        'tmp_list': data_list
    }
    list.append(tmp_datas)
    if ('items' not in rtn_data):
        rtn_data['items'] = []
    rtn_data['items'].append({'data': list})
    return rtn_data



